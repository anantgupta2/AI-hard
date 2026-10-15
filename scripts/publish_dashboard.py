"""Prepare the dashboard store documents (datasets + page) as JSON files for ArtifactData batch writes.

Usage: python scripts/publish_dashboard.py <assets.json>
assets.json maps dataset id -> uploaded blob url, e.g. {"families": "/_blob/..."}.
Writes data/dashboard/store/*.json (one file per document).
"""
import json, sys
from datetime import datetime, timezone
from pathlib import Path

DESC = {
    "families": ("Families and codebook buckets", "One row per analysed family: labels A-D, strongest eureka candidate, trust and correctness notes. Built from the agents' paper/family/lean/novelty JSON in data/pilot."),
    "trace_metrics": ("Search metrics per trace", "CDCL-style search metrics coded from each reasoning trace: backtracks by distance and trigger, restarts, depth, lesson reuse."),
    "trace_nodes": ("Search tree nodes", "Every approach node in each coded trace, with its level, length, outcome and the lesson drawn when it was abandoned."),
    "backtracks": ("Backtracks", "Each backtrack in each trace: from and to node, distance, trigger (conflict or insight), and how long the abandoned branch ran."),
    "pivots": ("Decisive pivots", "Moments where the search changed direction, classified as known technique, transfer, known route, new bridge or new concept."),
    "f1_items": ("F1 extension definitions", "Each item graded F1 (a new defined object): definition, abstract mechanism, obstruction dissolved, precedent check and reuse inside the release. From the F1 research agents' f1_*.json files."),
    "f1_targets": ("F1 downstream targets", "For each F1 item: ranked top-5 targets, newer open problems it might help with, and known theorems to use as speedup-test targets."),
    "f1_lean": ("F1 exact Lean source", "Verbatim Lean declarations of each F1 definition and its key lemmas, copied from the openai/math Lean library at commit fd4aeeb."),
    "shortlist": ("Eureka-step shortlist", "Priority tiers for the items that survived the novelty pass at N3, with the evidence for and against each and the next test to run. Curated by Claude in data/eureka_shortlist.json from the agents' findings."),
    "downstream": ("Related problems per shortlisted item", "For each Lean-formalized shortlist item: top-5 targets, known theorems for the speedup test, open problems, negative controls and theorem corollaries, each with how easily it can be stated in Lean. From the downstream agents' data/pilot/<fid>/downstream.json."),
    "prover_tasks": ("Prover task queue", "What the next agent should try to prove for each Lean eureka-shortlist item: speedup tests (with vs without the item), discoverability tests, negative controls and open problems, each with its statement, library arms, baseline and success criterion. Built by scripts/build_prover_tasks.py; the same list is data/prover_tasks.json."),
    "release_labels": ("Release-wide labels", "All 372 families on the v2 buckets (quantifier prefix, what is asserted, what was posed, outcome, Lean vs headline), with page, technical-page and proof-page counts and Lean scope category. Two independent labelling passes plus adjudication (data/abc_v2/labels_v2.json), joined with data/proof_lengths.json and data/lean_scope/scope_all.json by scripts/build_release_datasets.py."),
    "label_stats": ("Label statistics", "Cramér's V with permutation p-values between label axes, Cohen's kappa between the two labelling passes, and agreement with the in-depth v1 labels. From data/abc_v2/stats.json."),
    "lean_scope": ("Lean scope check", "For the 67 families whose Lean statement is weaker than or different from the headline: which paper the Lean formalizes, how much of it, whether OpenAI's scope note discloses the gap, and corrections to our labels. From data/lean_scope/scope_all.json."),
    "manuscript_lengths": ("Manuscript lengths", "Every manuscript in the release: PDF pages, technical pages (all but front matter, introduction / conclusion-type sections and references), pages inside proof blocks, and its longest single proof. From data/proof_lengths.json (scripts/proof_lengths.py, scripts/proof_text_lengths.py)."),
    "frontier_lengths": ("Human frontier baseline", "71 well-known human frontier papers from arXiv (all fields) measured the same way as the release: PDF pages, technical pages, proof-block pages and longest proof. From data/frontier_lengths.json (scripts/frontier_lengths.py)."),
    "items": ("Lemmas and definitions", "Every extracted lemma, definition and construction with its novelty grade (N0-N3) and eureka type (F), from the paper, family, trace and novelty analysts."),
}
assets = json.loads(Path(sys.argv[1]).read_text())
out = Path("data/dashboard/store"); out.mkdir(parents=True, exist_ok=True)
now = datetime.now(timezone.utc).isoformat(timespec="seconds")
for k, url in assets.items():
    if k.startswith("_"):
        continue
    t, d = DESC[k]
    doc = {"title": t, "description": d, "source": {"kind": "file", "url": url, "name": f"{k}.json", "format": "json"},
           "updated": {"at": now, "by": "Claude (scripts/build_dashboard_data.py)"}}
    (out / f"dataset_{k}.json").write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
(out / "page.json").write_text(json.dumps({"text": Path("dashboard/index.html").read_text(encoding="utf-8")}, ensure_ascii=False), encoding="utf-8")
print("ok", sorted(p.name for p in out.iterdir()), (out / "page.json").stat().st_size // 1024, "KB page")
