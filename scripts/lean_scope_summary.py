"""Aggregate the Lean scope check (data/lean_scope/scope_*.jsonl, brief in data/lean_scope/brief.md) into
data/lean_scope/scope_all.json and print a markdown report (save as data/lean_scope/report.md)."""
import glob
import json
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
D = Path(__file__).resolve().parent.parent / "data/lean_scope"
rows = sorted((json.loads(l) for p in glob.glob(str(D / "scope_*.jsonl")) for l in open(p, encoding="utf-8") if l.strip()),
              key=lambda r: r["fid"])
assert len(rows) == len({r["fid"] for r in rows}) == len(json.loads((D / "fids.json").read_text()))
(D / "scope_all.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
n = len(rows)
print(f"# Lean scope check ({n} families whose Lean statement differs from the headline)\n")
for k in ("category", "disclosure", "lean_vs_ms_main", "our_label_check", "ms_is_headline", "yaml_listed_but_partial"):
    print(f"**{k}:** " + " · ".join(f"{a} {b}" for a, b in Counter(str(r[k]) for r in rows).most_common()) + "\n")
print("## Flagged\n")
for r in rows:
    if r["category"] in ("partial_undisclosed", "label_error") or r["disclosure"] == "overstated" \
            or r["yaml_listed_but_partial"] or r["our_label_check"] != "confirmed":
        print(f"- **{r['fid']}** {r['category']} · disclosure {r['disclosure']} · label {r['our_label_check']}"
              f"{' · yaml lists it as formalized' if r['yaml_listed_but_partial'] else ''}: {r['gap']}")
print("\n## All\n\n| fid | category | Lean vs its paper | disclosure | gap |\n|---|---|---|---|---|")
for r in rows:
    print(f"| {r['fid']} | {r['category']} | {r['lean_vs_ms_main']} | {r['disclosure']} | {r['gap']} |")
