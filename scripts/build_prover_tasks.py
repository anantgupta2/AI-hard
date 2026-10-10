"""Build the prover task queue: what the next (prover) agent should try to prove, per Lean eureka-shortlist item.

Usage: python scripts/build_prover_tasks.py
Reads data/eureka_shortlist.json (items only; the informal list is not prover work), data/lean_checks.json and,
per item, data/pilot/<fid>/downstream.json (targets) and novelty.json (discoverability protocols).
Writes data/prover_tasks.json (committed; the hand-off) and data/dashboard/prover_tasks.json (dashboard dataset).

Task kinds (within an item the analysts' top-5 picks come first, then in this order):
  speedup        a known theorem: prove it WITH the item's Lean declarations in the library and WITHOUT them, same budget.
  discoverability  hide the item and its downstream cone; ask contamination-controlled models to propose it (test 4).
  negative_control a setting where the device must NOT help (or a false statement it must not prove).
  open_problem   exploratory: attempt with the item in the library; any proof is a result.
Corollaries of the item's own theorem are not device reuse and are left out.
"""
import json
import re
from pathlib import Path

PILOT = Path("data/pilot")
KIND_ORDER = {"speedup": 0, "discoverability": 1, "negative_control": 2, "open_problem": 3}
SUCCESS = {
    "speedup": ("Run both arms with the same prover and budget. A positive result is: solved WITH the item and not WITHOUT, "
                "or solved in both with a large budget gap (record tokens, attempts and wall-clock; report pass@k per arm). "
                "Only this kind of result can confirm a eureka step, and only on a theorem other than the item's own."),
    "discoverability": ("Report the discovery curve: hit rate (judged equivalent to the hidden item) against k = 1..K, per arm. "
                        "Low hit rate at k = K in the contamination-controlled arm, compared with the calibration controls, "
                        "supports hard discoverability."),
    "negative_control": ("Expected outcome: no budget gap between arms, and no proof of a false statement. A gap here means "
                         "the harness or the item is leaking something; flag it."),
    "open_problem": ("Exploratory: attempt WITH the item in the library. Any formal proof is a result; record the budget used "
                     "and whether the item's declarations appear in the proof."),
}


def load(p):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def txt(v):
    if v is None or v == "" or v == []:
        return ""
    if isinstance(v, (dict, list)):
        if isinstance(v, list) and all(isinstance(x, str) for x in v):
            return "; ".join(v)
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def first(*vals):
    for v in vals:
        if v not in (None, "", []):
            return v
    return None


def lean_rank(score):
    s = (score or "").lower()
    return 0 if "now" in s else 1 if "300" in s else 2 if s else 3


def words(s):
    return {w for w in re.findall(r"[a-z0-9]+", (s or "").lower()) if len(w) > 2}


def link_top5(top5, targets):
    """Map each top5 entry to a target index by explicit id (S1, O2, ...) or by title overlap."""
    out = {}
    for r, t in enumerate(top5, 1):
        name = first(t.get("target"), t.get("title"), "") or ""
        ids = re.findall(r"\b([SON]\d+)\b", name.split(":")[0])
        hit = None
        for i, tg in enumerate(targets):
            if tg.get("id") and tg["id"] in ids:
                hit = i
                break
        if hit is None:
            w = words(name)
            best = 0.0
            for i, tg in enumerate(targets):
                v = words(" ".join(str(first(tg.get(k), "")) for k in ("title", "target", "statement")))
                j = len(w & v) / max(1, min(len(w), len(v)))
                if j > best:
                    best, hit = j, i
            if best < 0.5:
                hit = None
        out[r] = hit
    return out


def nov_protocol(fid):
    """The strongest N3 candidate's discoverability protocol, merged with the family's common settings."""
    d = load(PILOT / fid / "novelty.json") or {}
    cands = [c for c in d.get("candidates") or [] if isinstance(c, dict) and "N3" in txt(c.get("final"))[:120]]
    if not cands:
        return None

    def conf(c):
        f = c.get("final")
        return f.get("confidence", 0) if isinstance(f, dict) and isinstance(f.get("confidence"), (int, float)) else 0
    c = max(cands, key=conf)
    protos = d.get("discoverability_protocols") or {}
    t4 = c.get("test4") if isinstance(c.get("test4"), dict) else {}
    pid = t4.get("protocol")
    p = protos.get(pid) if isinstance(protos, dict) and pid else None
    if p is None and isinstance(protos, dict):
        p = next((v for k, v in protos.items() if k != "common" and c["id"] in k), None)
    return {"candidate": c["id"], "name": c.get("name"), "test4": t4, "protocol": p,
            "common": protos.get("common") if isinstance(protos, dict) else None}


def main():
    sl = load("data/eureka_shortlist.json")
    checks = load("data/lean_checks.json") or {}
    passed = {}
    for c in checks.get("comparator", []):
        passed.setdefault(c["fid"], []).append(f"{c['config']}: {c['result']}")
    tasks = []
    for pos, it in enumerate(sl["items"]):
        fid = it["fid"]
        tier = it.get("tier")
        dd = load(PILOT / fid / "downstream.json") or {}
        with_lib = first(it.get("lean_decls"), "; ".join(
            f"{s.get('name')} ({s.get('file', '').split('lean/')[-1]}:{s.get('line')})"
            for s in dd.get("lean_source") or [] if isinstance(s, dict)))
        base = {"fid": fid, "eureka_item": it["item"], "tier": tier, "item_pos": pos, "item_F": it.get("F"),
                "item_confidence": it.get("novelty_conf"),
                "lean_check": "; ".join(passed.get(fid, [])) or "not yet run",
                "with_item_library": txt(with_lib),
                "without_item_library": ("Same library with the item's declarations listed under with_item_library removed, "
                                         "together with every declaration that depends on them (their downstream cone). "
                                         "Generic background (Mathlib, unrelated OAI files) stays."),
                "source": f"data/pilot/{fid}/downstream.json"}
        targets = []
        for lst, kind in (("speedup_targets", "speedup"), ("negative_controls", "negative_control"), ("open_problems", "open_problem")):
            for j, t in enumerate(dd.get(lst) or []):
                if isinstance(t, dict):
                    targets.append((kind, j + 1, t))
        top5 = [t for t in dd.get("top5") or [] if isinstance(t, dict)]
        links = link_top5(top5, [t for _, _, t in targets])
        top_rank = {i: r for r, i in links.items() if i is not None}
        for i, (kind, j, t) in enumerate(targets):
            lf = t.get("lean_feasibility") if isinstance(t.get("lean_feasibility"), dict) else {"score": txt(t.get("lean_feasibility"))}
            r = top_rank.get(i)
            tasks.append({**base, "kind": kind, "list_order": j, "top5_rank": r,
                          "top5_argument": txt(first(top5[r - 1].get("argument"), top5[r - 1].get("why"))) if r else "",
                          "title": txt(first(t.get("title"), t.get("target"), t.get("theorem"), t.get("name"))),
                          "statement": txt(first(t.get("statement"), t.get("argument"))),
                          "reference": txt(t.get("reference")), "status": txt(t.get("status")),
                          "how_item_helps": txt(first(t.get("how_item_helps"), t.get("adaptation"), t.get("adaptation_sketch"),
                                                      t.get("why_device_must_fail"), t.get("why"))),
                          "expected": txt(first(t.get("expected_speedup"), t.get("payoff"))), "confidence": txt(t.get("confidence")),
                          "lean_score": txt(first(lf.get("score"), t.get("lean"))), "lean_statable_with": txt(lf.get("statable_with")),
                          "lean_missing": txt(lf.get("missing")), "baseline_formal_proof": txt(lf.get("formal_proof_to_compare")),
                          "current_proof_size": txt(t.get("current_proof_size")), "success_criterion": SUCCESS[kind]})
        for r, t in enumerate(top5, 1):
            if links.get(r) is not None:
                continue
            lean = txt(first(t.get("lean"), t.get("lean_usable")))
            name = txt(first(t.get("target"), t.get("title"))).lower()
            kind = "negative_control" if ("control" in name or "non-target" in name) else "open_problem" if re.search(r"\bopen\b", name) else "speedup"
            tasks.append({**base, "kind": kind, "list_order": 0, "top5_rank": r,
                          "top5_argument": txt(first(t.get("argument"), t.get("why"))),
                          "title": txt(first(t.get("target"), t.get("title"))), "statement": "", "reference": "", "status": "",
                          "how_item_helps": "", "expected": "", "confidence": "",
                          "lean_score": "statable now" if lean in ("True", "true") else lean, "lean_statable_with": "",
                          "lean_missing": "", "baseline_formal_proof": "", "current_proof_size": "",
                          "success_criterion": SUCCESS[kind]})
        p = nov_protocol(fid)
        if p:
            pr = p["protocol"] if isinstance(p["protocol"], dict) else {"text": txt(p["protocol"])}
            cm = p["common"] if isinstance(p["common"], dict) else {}
            tasks.append({**base, "kind": "discoverability", "list_order": 0, "top5_rank": None, "top5_argument": "",
                          "title": f"Test 4: can a model rediscover {p['candidate']} ({p['name']})?",
                          "statement": txt(first(cm.get("prompt_template"), pr.get("prompt"))),
                          "reference": f"data/pilot/{fid}/novelty.json discoverability_protocols", "status": txt(p["test4"].get("status")),
                          "how_item_helps": txt(first(pr.get("hide"), pr.get("hidden"))),
                          "expected": txt(first(p["test4"].get("pivot_distance"), pr.get("expected"))),
                          "confidence": "", "lean_score": "", "lean_statable_with": "", "lean_missing": "",
                          "baseline_formal_proof": "", "current_proof_size": "",
                          "protocol_models": txt(cm.get("models")), "protocol_arms": txt(cm.get("arms")),
                          "protocol_sampling": txt(cm.get("sampling")), "protocol_judging": txt(cm.get("judging")),
                          "protocol_controls": txt(cm.get("controls")), "protocol_item": txt(pr),
                          "success_criterion": SUCCESS["discoverability"]})
    tier_key = lambda t: (t["tier"] if isinstance(t["tier"], (int, float)) else 9)
    # Items in shortlist order (tier, then rank); within an item the analysts' top-5 picks first, then the
    # discoverability test, then the rest by kind and by how easily the statement can be written in Lean.
    tasks.sort(key=lambda t: (tier_key(t), t["item_pos"], t["top5_rank"] or 99, KIND_ORDER[t["kind"]],
                              lean_rank(t["lean_score"]), t["list_order"]))
    for n, t in enumerate(tasks, 1):
        t["queue"] = n
        t["task_id"] = f"{t['fid']}-{t['kind'][:3]}-{n:03d}"
        t["runnable_now"] = t["kind"] == "discoverability" or lean_rank(t["lean_score"]) == 0
    doc = {"note": ("Prover task queue: what the next agent should try to prove, for each item on the Lean eureka shortlist. "
                    "Built by scripts/build_prover_tasks.py from data/eureka_shortlist.json, data/pilot/<fid>/downstream.json and "
                    "novelty.json. Work top-down by `queue`. A confirmed eureka step needs a speedup on a theorem OTHER than the "
                    "item's own; see docs/PLAN.md."),
           "setup": ["bash scripts/fetch_release.sh", "bash scripts/setup_lean.sh",
                     "cd data/raw/openai-math/lean && lake build <module>  # e.g. the comparator's solution_module",
                     "Comparator: lake env comparator ComparatorChallenges/<config>.json (see data/lean_checks.json)"],
           "environment": "Lean v4.34.1, Mathlib d13f23b, OAI library at openai/math fd4aeeb (lean/).",
           "tasks": tasks}
    Path("data/prover_tasks.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    Path("data/dashboard").mkdir(parents=True, exist_ok=True)
    Path("data/dashboard/prover_tasks.json").write_text(json.dumps(tasks, ensure_ascii=False), encoding="utf-8")
    by = {}
    for t in tasks:
        by[t["kind"]] = by.get(t["kind"], 0) + 1
    print(len(tasks), "tasks", by, "runnable now:", sum(t["runnable_now"] for t in tasks))


if __name__ == "__main__":
    main()
