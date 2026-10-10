"""Flatten the per-family agent outputs in data/pilot/<fid>/ into dashboard datasets.

Writes data/dashboard/{families,trace_metrics,trace_nodes,backtracks,pivots,candidates}.json.
Agents' JSON varies slightly between families, so every field is read defensively.

Usage: python scripts/build_dashboard_data.py
"""

import json
import sys
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

PILOT = Path("data/pilot")
OUT = Path("data/dashboard")
CAT = pd.read_csv("data/catalog_families.csv", dtype={"family_id": str}).set_index("family_id")
TXT = 700  # cap long text fields so datasets stay small


def load(p):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def g(d, *path, default=None):
    """Nested get that tolerates missing keys, lists and non-dicts."""
    for k in path:
        if isinstance(d, dict) and k in d:
            d = d[k]
        else:
            return default
    return d


def first(*vals):
    for v in vals:
        if v not in (None, "", [], {}):
            return v
    return None


def txt(v, n=TXT):
    if v is None:
        return ""
    if not isinstance(v, str):
        v = json.dumps(v, ensure_ascii=False)
    v = " ".join(v.split())
    return v if len(v) <= n else v[: n - 1] + "…"


def label(lbls, axis):
    v = g(lbls, axis)
    if isinstance(v, dict):
        return first(v.get("label"), v.get("primary"), v.get("grade"), v.get("value"))
    return v


def as_list(v):
    if isinstance(v, list):
        return v
    if isinstance(v, dict):
        for k in ("list", "items", "candidates", "nodes"):
            if isinstance(v.get(k), list):
                return v[k]
    return []


def prov_text(v):
    if isinstance(v, dict):
        return " ".join(str(x) for x in (v.get("applies"), v.get("explanation")) if x)
    return v


def family_row(fid, files):
    cat = CAT.loc[fid] if fid in CAT.index else None
    paper = files.get("paper") or files.get("family") or {}
    lean = files.get("lean") or {}
    nov = files.get("novelty") or {}
    trace = files.get("trace") or {}
    lbls = paper.get("labels") or {}
    C = g(lbls, "C") or {}
    cands = as_list(first(nov.get("candidates"), paper.get("eureka_candidates"), trace.get("eureka_candidates")))
    top = cands[0] if cands else {}
    ranked = as_list(paper.get("eureka_candidates_ranked"))
    if not top and ranked:
        if isinstance(ranked[0], dict):
            top = ranked[0]
        else:
            top = next((it for it in as_list(paper.get("items")) if str(it.get("id")) == str(ranked[0]).split("/")[0]), {})
    if nov:
        best = next((c for c in as_list(nov.get("candidates")) if "N3" in str(g(c, "final", "N"))), None)
        if best:
            top = {"name": best.get("name"), "N": g(best, "final", "N")}
    concerns = first(paper.get("correctness_audit"), paper.get("correctness_concerns"), g(lean, "statement_vs_paper_claim"))
    trust = first(g(lean, "axioms_and_trust", "summary"), g(lean, "axioms_and_trust"), g(paper, "trust_surface"))
    return {
        "fid": fid,
        "title": cat.title if cat is not None else first(paper.get("title"), trace.get("title")),
        "subject": cat.subject if cat is not None else "",
        "n_manuscripts": int(cat.n_manuscripts) if cat is not None else None,
        "has_lean": bool(cat is not None and isinstance(cat.lean_dirs, str)),
        "analyses": ", ".join(sorted(files)),
        "has_trace": "trace" in files,
        "A": label(lbls, "A"),
        "B": label(lbls, "B"),
        "C_primary": first(C.get("primary"), C.get("label")) if isinstance(C, dict) else C,
        "C_secondary": ", ".join(str(x.get("label") if isinstance(x, dict) else x) for x in (C.get("secondaries") or C.get("secondary") or [])) if isinstance(C, dict) else "",
        "computer_assisted": txt(first(g(C, "computer_assisted"), g(lbls, "computer_assisted")), 80),
        "ih_template": txt(first(g(C, "ih_template"), g(C, "ih_strengthened")), 120),
        "D": first(label(nov, "family_D"), nov.get("family_D") if isinstance(nov.get("family_D"), str) else None, label(lbls, "D")),
        "D_source": "novelty" if nov else ("paper" if lbls else ""),
        "D_confidence": g(nov, "family_D", "confidence"),
        "D_rests_on": txt(g(nov, "family_D", "rests_on"), 400),
        "D_downgrade_if": txt(first(g(nov, "family_D", "falls_to"), g(nov, "family_D", "downgrade_if"), g(nov, "family_D", "what_would_downgrade")), 500),
        "bridge_novelty": flat(nov.get("bridge_novelty"), 900) if nov else "",
        "provenance_flag": txt(first(prov_text(nov.get("provenance_flag")), g(lbls, "provenance_flag"), g(lbls, "D", "flag_builds_on_prior_model_produced_result")), 200),
        "top_candidate": txt(first(top.get("name"), top.get("item"), top.get("id"), top.get("new_idea")) if isinstance(top, dict) else top, 160),
        "top_candidate_N": first(short_grade(first(g(top, "final_N"), g(top, "final_grade"), g(top, "N"), g(top, "provisional_N"))), g(top, "provisional_grade"), g(top, "novelty_grade_proposed"), g(top, "grade_guess"), g(top, "suggested_grade")) if isinstance(top, dict) else None,
        "main_statement": txt(first(g(paper, "main_statement", "paraphrase"), g(paper, "main_statement")), 500),
        "trust": txt(trust, 400),
        "concerns": txt(concerns, 600),
    }


def trace_rows(fid, t):
    sd = t.get("search_dynamics") or {}
    hist = sd.get("backtrack_distance_histogram") or {}
    st = g(sd, "abandoned_branch_length_stats", "all") or {}
    metrics = {
        "fid": fid,
        "trace_words": first(t.get("summary_body_words"), g(sd, "nodes", 0, "length_words")),
        "n_decisions": sd.get("n_decisions"),
        "n_conflicts": sd.get("n_conflicts"),
        "n_backtracks": sd.get("n_backtracks"),
        "bt_conflict": sd.get("n_conflict_backtracks"),
        "bt_insight": sd.get("n_insight_backtracks"),
        "bt_unclear": sd.get("n_unclear_backtracks"),
        "d1": hist.get("1", 0),
        "d2": hist.get("2", 0),
        "d3plus": sum(v for k, v in hist.items() if str(k).isdigit() and int(k) >= 3),
        "max_distance": sd.get("max_backtrack_distance"),
        "n_restarts": sd.get("n_restarts"),
        "max_depth": sd.get("max_depth"),
        "clause_reuse_rate": sd.get("learned_clause_reuse_rate"),
        "frac_before_final": first(sd.get("fraction_of_trace_words_before_final_route"), sd.get("fraction_of_trace_before_final_route")),
        "branch_len_mean": st.get("mean"),
        "branch_len_median": st.get("median"),
        "final_route_conflict_driven": txt(first(sd.get("final_route_conflict_driven_qualified"), sd.get("final_route_conflict_driven")), 300),
    }
    nodes = []
    for n in sd.get("nodes") or []:
        les = n.get("lesson") or {}
        nodes.append({
            "fid": fid, "node": n.get("id"), "parent": n.get("parent"), "level": n.get("level"),
            "description": txt(n.get("description"), 300), "outcome": txt(n.get("outcome"), 80),
            "length_words": n.get("length_words"), "length_share": n.get("length_share"),
            "location": txt(n.get("location"), 60),
            "obstruction": txt(first(les.get("obstruction"), n.get("conflict")), 400),
            "lesson": txt(les.get("lesson_statement"), 500),
            "lesson_form": txt(les.get("lesson_form"), 80),
            "generality": txt(les.get("generality"), 120),
            "known_in_literature": txt(les.get("known_in_literature"), 200),
            "influence": txt(first(les.get("influence"), les.get("reused_at")), 200),
            "salvage": txt(les.get("salvage"), 200),
        })
    by_node = {n.get("id"): n for n in sd.get("nodes") or []}
    bts = []
    for i, b in enumerate(sd.get("backtracks") or []):
        src = by_node.get(b.get("from_node")) or {}
        dst = by_node.get(b.get("to_node")) or {}
        ab = by_node.get(b.get("abandoned_branch")) or src
        les = first(src.get("lesson"), ab.get("lesson")) or {}
        bts.append({
            "fid": fid, "seq": i + 1, "from_node": b.get("from_node"), "to_node": b.get("to_node"),
            "abandoned_branch": b.get("abandoned_branch"),
            "from_level": first(b.get("conflict_level"), src.get("level")), "to_level": first(b.get("resume_level"), dst.get("level")),
            "distance": b.get("distance"), "trigger": b.get("trigger_type"), "restart": bool(b.get("is_restart")),
            "repair": bool(b.get("kept_branch_repair")),
            "conflict": txt(first(b.get("conflict"), src.get("conflict")), 300),
            "from_desc": txt(src.get("description"), 300), "to_desc": txt(dst.get("description"), 300),
            "length_words": first(b.get("abandoned_branch_length_words"), b.get("length_words")),
            "leaf_words": b.get("leaf_length_words"),
            "location": txt(src.get("location"), 60),
            "obstruction": txt(les.get("obstruction"), 600),
            "lesson": txt(les.get("lesson_statement"), 600),
            "lesson_form": txt(les.get("lesson_form"), 80),
            "influence": txt(first(les.get("influence"), les.get("reused_at")), 300),
            "origin": b.get("origin"), "simplification": txt(b.get("simplification_estimate"), 300),
        })
    pivots = []
    for p in as_list(t.get("pivots")):
        if not isinstance(p, dict):
            continue
        pivots.append({
            "fid": fid, "pivot": p.get("id"), "new_idea": txt(p.get("new_idea"), 400),
            "classification": txt(p.get("classification"), 60), "trigger": txt(p.get("trigger"), 200),
            "pivot_distance": txt(p.get("pivot_distance"), 120), "chain_depth": txt(p.get("chain_depth"), 80),
            "F_type": txt(p.get("F_type"), 40), "final_item": txt(p.get("final_paper_item"), 160),
        })
    return metrics, nodes, bts, pivots


def join_list(v):
    return " ".join(map(str, v)) if isinstance(v, list) else v


def short_grade(v):
    """'N3 (provisional: ...)' -> 'N3'; keeps other strings."""
    v = grade(v)
    if isinstance(v, str):
        import re
        m = re.match(r"\s*([NFD]\d)", v)
        return m.group(1) if m else v
    return v


def grade(v):
    """Pull an N/F grade string out of a str or {grade|type, justification} dict."""
    if isinstance(v, dict):
        return first(v.get("grade"), v.get("type"), v.get("label"))
    return v


def item_rows(fid, files):
    """Every extracted lemma/definition (paper or family analyst), plus novelty and eureka candidates."""
    rows = []
    for src in ("paper", "family"):
        d = files.get(src) or {}
        ranked = [str(x) for x in as_list(first(d.get("eureka_candidates_ranked"), []))]
        for it in as_list(d.get("items")):
            if not isinstance(it, dict):
                continue
            iid = str(it.get("id", ""))
            rank = next((i + 1 for i, r in enumerate(ranked) if iid and iid in r.split("/")), None)
            rows.append({
                "fid": fid, "source": src, "id": iid, "rank": rank,
                "name": txt(it.get("name"), 160), "kind": txt(it.get("kind"), 60),
                "where": txt(it.get("file_line"), 60),
                "statement": txt(it.get("statement"), 500),
                "cited_or_new": txt(first(g(it, "cited_or_new", "status"), it.get("cited_or_new")), 80),
                "N": txt(short_grade(first(it.get("final_N"), it.get("provisional_N"))), 12),
                "F": txt(short_grade(first(it.get("final_F"), it.get("provisional_F"))), 12),
                "load_bearing": txt(grade(it.get("load_bearing_guess")), 12),
                "why": txt(first(g(it, "provisional_N", "justification"), it.get("justification")), 500),
            })
    for src in ("paper", "family"):
        for c in as_list((files.get(src) or {}).get("eureka_candidates_ranked")):
            if isinstance(c, dict):
                joined = lambda v: " ".join(v) if isinstance(v, list) else v
                rows.append({
                    "fid": fid, "source": src + "-candidate", "id": txt(first(c.get("item"), c.get("id")), 40), "rank": c.get("rank"),
                    "name": txt(c.get("name"), 160), "kind": "eureka candidate", "where": "",
                    "statement": txt(c.get("statement"), 500), "cited_or_new": "",
                    "N": txt(short_grade(c.get("provisional_N")), 12), "F": txt(short_grade(c.get("provisional_F")), 12),
                    "load_bearing": "", "why": txt(joined(c.get("for")), 500),
                })
    nov = files.get("novelty") or {}
    for c in as_list(nov.get("candidates")):
        if not isinstance(c, dict):
            continue
        rows.append({
            "fid": fid, "source": "novelty", "id": txt(first(c.get("id"), c.get("item_id")), 40), "rank": None,
            "name": txt(first(c.get("name"), c.get("item")), 160), "kind": txt(c.get("kind"), 60), "where": "",
            "statement": txt(first(c.get("statement"), c.get("description")), 500), "cited_or_new": "",
            "N": txt(short_grade(first(g(c, "final", "N"), c.get("final_N"), c.get("N"))), 12),
            "F": txt(short_grade(first(g(c, "final", "F"), c.get("final_F"), c.get("F"))), 12),
            "load_bearing": "", "why": txt(first(g(c, "final", "justification"), c.get("justification")), 500),
        })
    for src in ("trace", "family"):
        for c in as_list((files.get(src) or {}).get("eureka_candidates")):
            if isinstance(c, dict):
                rows.append({
                    "fid": fid, "source": src + "-candidate", "id": txt(c.get("id"), 40), "rank": None,
                    "name": txt(first(c.get("name"), c.get("item"), c.get("new_idea")), 160), "kind": "",
                    "where": "", "statement": txt(first(c.get("statement"), c.get("description")), 500),
                    "cited_or_new": "", "N": txt(first(c.get("provisional_grade"), c.get("novelty_grade_proposed"), c.get("grade_guess"), c.get("suggested_grade"), short_grade(first(c.get("provisional_N"), c.get("N")))), 12),
                    "F": txt(short_grade(first(c.get("provisional_F"), c.get("F_type"), c.get("F"))), 12),
                    "load_bearing": "", "against": txt(join_list(c.get("arguments_against")), 400), "why": txt(first(join_list(c.get("arguments_for")), c.get("argument_for"), join_list(c.get("for")), c.get("justification")), 500),
                })
    return rows


def flat(v, n=TXT):
    """Dict/list/str -> readable text."""
    if isinstance(v, dict):
        return txt(" · ".join(f"{k.replace('_', ' ')}: {flat(x, 10_000)}" for k, x in v.items() if x not in (None, "", [], {})), n)
    if isinstance(v, list):
        return txt(" · ".join(flat(x, 10_000) for x in v), n)
    return txt(v, n)


def f1_rows(fid, path):
    d = load(path) or {}
    slug = path.stem.replace("f1_", "")
    item = d.get("item")
    pretty = slug.replace("_", " ").capitalize()
    name = first(g(item, "name"), item if isinstance(item, str) else None,
                 (g(item, "family_title") or "") + " · " + pretty if isinstance(item, dict) else None, pretty)
    pc = d.get("precedent_check")
    head = {
        "fid": fid, "slug": slug, "key": f"{fid}|{slug}",
        "name": txt(name, 300),
        "definition": flat(d.get("definition"), 2500),
        "mechanism": txt(d.get("abstract_mechanism"), 2000),
        "obstruction": flat(d.get("obstruction_dissolved"), 1500),
        "precedent": flat(first(g(pc, "verdict"), pc), 1500),
        "precedent_detail": flat(pc, 3000) if isinstance(pc, dict) else "",
        "release_reuse": flat(d.get("release_reuse"), 1200),
        "n_candidates": len(as_list(d.get("candidates"))),
        "n_speedup_targets": len(as_list(d.get("speedup_targets"))),
        "n_lean": len(as_list(d.get("lean_source"))),
    }
    targets = []
    for c in as_list(d.get("top5")):
        targets.append({
            "fid": fid, "slug": slug, "list": "top5", "rank": c.get("rank"),
            "title": txt(first(c.get("title"), c.get("target"), c.get("candidate"), c.get("id")), 300),
            "reference": "", "status": "", "match": "", "payoff": "", "confidence": "",
            "detail": txt(c.get("argument"), 1500),
        })
    for c in as_list(d.get("candidates")):
        targets.append({
            "fid": fid, "slug": slug, "list": "open problem", "rank": None,
            "title": txt(first(c.get("problem"), c.get("id")), 400),
            "reference": txt(first(c.get("reference"), c.get("url")), 300),
            "status": txt(c.get("status"), 120), "match": txt(c.get("obstruction_match"), 600),
            "payoff": txt(first(c.get("expected_payoff"), c.get("payoff")), 400),
            "confidence": txt(c.get("confidence"), 40),
            "detail": txt(first(c.get("adaptation_sketch"), c.get("adaptation")), 1200),
        })
    for c in as_list(d.get("speedup_targets")):
        targets.append({
            "fid": fid, "slug": slug, "list": "speedup target", "rank": None,
            "title": txt(first(c.get("theorem"), c.get("id")), 400),
            "reference": txt(c.get("reference"), 300), "status": txt(c.get("formalizable"), 120),
            "match": txt(first(c.get("current_proof_size"), c.get("current_size")), 300),
            "payoff": txt(first(c.get("expected_speedup"), c.get("how_device_shortens"), c.get("device_route"), c.get("with_item"), c.get("test")), 600),
            "confidence": "", "detail": txt(first(c.get("caveat"), c.get("note")), 600),
        })
    lean = []
    for i, c in enumerate(as_list(d.get("lean_source"))):
        lean.append({
            "fid": fid, "slug": slug, "key": f"{fid}|{slug}|{i + 1}", "order": i + 1,
            "name": txt(c.get("name"), 200), "kind": txt(c.get("kind"), 40),
            "file": txt(c.get("file"), 200), "line": c.get("line"),
            "note": txt(c.get("note"), 400),
            "text": (c.get("text") or "")[:8000],
        })
    for i, t in enumerate(targets):
        t["key"] = f"{fid}|{slug}|{t['list']}|{i + 1}"
    return head, targets, lean


def main():
    fams, tm, tn, bt, pv, cd = [], [], [], [], [], []
    f1, f1t, f1l = [], [], []
    ds = []
    for d in sorted(p for p in PILOT.iterdir() if p.is_dir()):
        fid = d.name
        files = {p.stem: load(p) for p in d.glob("*.json") if not p.stem.startswith("f1_")}
        files = {k: v for k, v in files.items() if isinstance(v, dict)}
        if not files:
            continue
        fams.append(family_row(fid, files))
        if "trace" in files:
            m, n, b, p = trace_rows(fid, files["trace"])
            tm.append(m), tn.extend(n), bt.extend(b), pv.extend(p)
        cd.extend(item_rows(fid, files))
        for p in sorted(d.glob("f1_*.json")):
            h, t, l = f1_rows(fid, p)
            f1.append(h), f1t.extend(t), f1l.extend(l)
    # Curated eureka-priority tiers (data/eureka_shortlist.json), joined onto families.
    sl_doc = load(Path("data/eureka_shortlist.json")) or {}
    tiers = sl_doc.get("tiers", {})
    shortlist = []
    for it in sl_doc.get("items", []):
        row = dict(it)
        row["key"] = f"{it['fid']}|{it['rank']}"
        row["tier_label"] = tiers.get(str(it["tier"]), "")
        shortlist.append(row)
    for i, it in enumerate(sl_doc.get("excluded_no_lean", [])):
        row = dict(it)
        row.update(tier=9, rank=100 + i, key=f"{it['fid']}|x", tier_label="Excluded: not formalized in Lean, so untestable there")
        shortlist.append(row)
    by_fid_sl = {r["fid"]: r for r in shortlist if r["tier"] != 9}
    # Downstream targets per shortlisted item (data/pilot/<fid>/downstream.json; Lean-usable related problems).
    for it in sl_doc.get("items", []):
        dd = load(PILOT / it["fid"] / "downstream.json")
        if not dd:
            continue
        for lst in ("top5", "speedup_targets", "open_problems", "negative_controls", "theorem_corollaries"):
            for j, t in enumerate(dd.get(lst) or []):
                t = t if isinstance(t, dict) else {"title": str(t)}
                lf = t.get("lean_feasibility") or {}
                lf = lf if isinstance(lf, dict) else {"score": str(lf)}
                ds.append({"fid": it["fid"], "list": lst, "order": j + 1, "key": f"{it['fid']}|{lst}|{j + 1}",
                           "title": txt(first(t.get("title"), t.get("target"), t.get("theorem"), t.get("candidate"), t.get("name"))),
                           "statement": txt(first(t.get("statement"), t.get("argument"), t.get("why"))),
                           "reference": txt(t.get("reference")), "status": txt(t.get("status")),
                           "how": txt(first(t.get("how_item_helps"), t.get("adaptation"), t.get("adaptation_sketch"), t.get("why_device_must_fail"), t.get("why"), t.get("argument") if t.get("statement") else None)),
                           "size": txt(t.get("current_proof_size")), "match": txt(t.get("obstruction_match")),
                           "payoff": txt(first(t.get("expected_speedup"), t.get("payoff"))), "confidence": txt(t.get("confidence")),
                           "lean_score": txt(first(lf.get("score"), t.get("lean_usable"), t.get("lean"))), "lean_needs": txt(first(lf.get("missing"), lf.get("statable_with"))),
                           "lean_compare": txt(lf.get("formal_proof_to_compare"))})
        row = by_fid_sl.get(it["fid"])
        if row is not None:
            row["lean_status"] = txt(dd.get("lean_status")) or row.get("lean_status")
            row["lean_status_why"] = txt(dd.get("lean_status_why"))
            row["lean_gaps"] = txt(dd.get("lean_gaps"))
            cc = dd.get("comparator_chain")
            row["comparator_chain"] = " → ".join(map(str, cc)) if isinstance(cc, list) else txt(cc)
    # Claude's F1 verdicts (f1_review), joined onto the F1 rows by fid|slug.
    rev = {f"{r['fid']}|{r['slug']}": r for r in sl_doc.get("f1_review", [])}
    for row in f1:
        r = rev.get(row["key"])
        if r:
            row.update(review_status=r["status"], review_grade=r["grade"], review_verdict=r["verdict"],
                       review_test=r["decisive_test"], p_n3=r["p_n3"], p_jump=r["p_jump"])
    by_fid = {r["fid"]: r for r in shortlist if r["tier"] != 9}
    for fam in fams:
        s = by_fid.get(fam["fid"])
        fam["priority_tier"] = s["tier"] if s else None
        fam["priority_rank"] = s["rank"] if s else None
        excl = {r["fid"] for r in shortlist if r["tier"] == 9}
        fam["priority_label"] = (s["tier_label"] if s else "N3 item, but not in Lean (excluded)" if fam["fid"] in excl
                                 else "No N3 item (D2)" if fam.get("D") and "D2" in str(fam["D"]) else "")

    # Stable unique keys so the dashboard can cite single rows.
    for rows, cols in [(tn, ("fid", "node")), (bt, ("fid", "seq")), (pv, ("fid", "pivot")), (cd, ("fid", "source", "id"))]:
        seen = {}
        for r in rows:
            k = "|".join(str(r.get(c) or "") for c in cols)
            seen[k] = seen.get(k, 0) + 1
            r["key"] = k if seen[k] == 1 else f"{k}#{seen[k]}"
    OUT.mkdir(parents=True, exist_ok=True)
    for name, rows in [("families", fams), ("trace_metrics", tm), ("trace_nodes", tn), ("backtracks", bt), ("pivots", pv), ("items", cd), ("f1_items", f1), ("f1_targets", f1t), ("f1_lean", f1l), ("shortlist", shortlist), ("downstream", ds)]:
        (OUT / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, default=str), encoding="utf-8")
        print(f"{name}: {len(rows)} rows, {(OUT / f'{name}.json').stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
