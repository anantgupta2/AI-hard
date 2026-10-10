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
