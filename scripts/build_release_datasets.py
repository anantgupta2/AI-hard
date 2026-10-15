"""Release-wide datasets for the atlas: v2 A/B labels for all 372 families joined with proof lengths
(data/proof_lengths.json) and the Lean scope check (data/lean_scope/scope_all.json), plus the label statistics
(data/abc_v2/stats.json). Also per-manuscript lengths and the human frontier baseline (data/frontier_lengths.json).
Writes data/dashboard/{release_labels,label_stats,lean_scope,manuscript_lengths,frontier_lengths}.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/dashboard"
labels = json.loads((ROOT / "data/abc_v2/labels_v2.json").read_text(encoding="utf-8"))
stats = json.loads((ROOT / "data/abc_v2/stats.json").read_text(encoding="utf-8"))
lengths = {f["fid"]: f for f in json.loads((ROOT / "data/proof_lengths.json").read_text(encoding="utf-8"))["families"]}
scope = {r["fid"]: r for r in json.loads((ROOT / "data/lean_scope/scope_all.json").read_text(encoding="utf-8"))}

rows = []
for r in labels:
    L, s = lengths[r["fid"]], scope.get(r["fid"], {})
    rows.append({
        "fid": r["fid"], "title": r["title"], "subject": r["subject"], "claim": r["claim_formal"],
        "prefix": r["A_prefix"], "outer": r["A_outer"], "alternations": r["alternations"], "matrix": r["A_matrix"],
        "A_flags": ", ".join(r["A_flags"]), "problem": r["B_problem"], "outcome": r["B_outcome"],
        "B_flags": ", ".join(r["B_flags"]), "lean": r["lean_vs_headline"], "lean_fixed_from": r.get("lean_vs_headline_fixed_from"),
        "scope_category": s.get("category"), "label_source": r["source"],
        "pages": L["pages"], "technical_pages": L["technical_pages"], "proof_pages": L["proof_pages"], "n_proofs": L["n_proofs"], "longest_proof_pages": L["longest_proof_pages"], "manuscripts": L["n_ms"], "lean_lines": L["lean_lines"] or None,
    })
st = [{"key": f"kappa|{k}", "kind": "kappa", "a": k, "b": "", "value": v[1], "agreement": v[0], "p": None}
      for k, v in stats["interrater"].items()]
st += [{"key": f"assoc|{k}", "kind": "assoc", "a": k.split("x")[0], "b": k.split("x", 1)[1], "value": v[0], "agreement": None, "p": v[1]}
       for k, v in stats["assoc"].items()]
a, b, n = stats["vs_deep_v1"]
st += [{"key": "deep|A", "kind": "vs_deep", "a": "A", "b": f"{n} families", "value": None, "agreement": a, "p": None},
       {"key": "deep|B", "kind": "vs_deep", "a": "B", "b": f"{n} families", "value": None, "agreement": b, "p": None}]
sc = [{k: v for k, v in r.items()} for r in scope.values()]
ms = [{"key": f"{m['fid']}|{i}", "fid": m["fid"], "title": m["title"], "pages": m["pages"], "technical_pages": m["technical_pages"],
       "proof_pages": m["proof_pages"], "longest_proof_pages": m["longest_proof_pages"], "n_proofs": m["n_proofs"]}
      for i, m in enumerate(json.loads((ROOT / "data/proof_lengths.json").read_text(encoding="utf-8"))["manuscripts"]) if m["doc_words"]]
fr = [{"key": r["arxiv"], "arxiv": r["arxiv"], "name": r["name"], "title": r["title"], "pages": r["pages"], "technical_pages": r["technical_pages"],
       "proof_pages": r["proof_pages"], "longest_proof_pages": r["longest_proof_pages"], "uses_proof_blocks": (r["proof_share"] or 0) > 0.25}
      for r in json.loads((ROOT / "data/frontier_lengths.json").read_text(encoding="utf-8")) if "error" not in r]
for name, data in (("release_labels", rows), ("label_stats", st), ("lean_scope", sc), ("manuscript_lengths", ms), ("frontier_lengths", fr)):
    (OUT / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(name, len(data), (OUT / f"{name}.json").stat().st_size // 1024, "KB")
