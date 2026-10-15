"""Bundle each family whose Lean statement differs from its headline (labels_v2 lean_vs_headline weaker/different)
with OpenAI's own scope note (lean/docs/<fid>.md), the comparator statements, and which manuscripts
lean/formalization.yaml lists as having a formalized main result. Output: data/lean_scope/bundles/<fid>.txt."""
import csv
import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAN = ROOT / "data/raw/openai-math/lean"
OUT = ROOT / "data/lean_scope/bundles"
OUT.mkdir(parents=True, exist_ok=True)
cat = {r["family_id"]: r for r in csv.DictReader(open(ROOT / "data/catalog_families.csv", encoding="utf-8"))}
ms = {}
for r in csv.DictReader(open(ROOT / "data/catalog_manuscripts.csv", encoding="utf-8")):
    ms.setdefault(r["family_id"], []).append(r)
recs = {}
for p in sorted(glob.glob(str(ROOT / "data/abc_v2/full/pass_a*.jsonl"))) + sorted(glob.glob(str(ROOT / "data/abc_v2/full/adjudicated_*.jsonl"))):
    for line in open(p, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            recs[str(r["fid"]).zfill(3)] = r
labels = json.load(open(ROOT / "data/abc_v2/labels_v2.json", encoding="utf-8"))
todo = [r for r in labels if r["lean"] and r["lean_vs_headline"] in ("weaker", "different")]
for r in todo:
    f, c, x = r["fid"], cat[r["fid"]], recs[r["fid"]]
    parts = [f"FAMILY {f}: {c['title']}", f"OPENAI SUMMARY: {c['summary']}",
             f"OUR LABEL: lean_vs_headline = {r['lean_vs_headline']}", f"OUR HEADLINE (semi-formal): {r['claim_formal']}",
             f"OUR NOTES: {x.get('notes') or x.get('reason') or ''}", "", "MANUSCRIPTS (in_formalization_yaml = listed in lean/formalization.yaml as a paper with a formalized main result):"]
    for m in ms.get(f, []):
        parts.append(f"- {m['ms_title']} | in_formalization_yaml={m['in_formalization_yaml']} | withdrawn={m['withdrawn']} | main_tex={m['ms_dir']}/{m['main_tex']}")
        parts.append(f"  ABSTRACT: {m['abstract'][:1500]}")
    doc = LEAN / "docs" / f"{f}.md"
    parts += ["", "=== OPENAI SCOPE NOTE (lean/docs/%s.md) ===" % f, doc.read_text(encoding="utf-8") if doc.exists() else "(none)"]
    for comp in [s for s in c["comparators"].split(";") if s]:
        p = LEAN / "ComparatorChallenges" / f"{comp}.lean"
        txt = p.read_text(encoding="utf-8") if p.exists() else "(missing)"
        parts += ["", f"=== COMPARATOR {comp} ===", txt[:9000] + ("\n…(truncated)" if len(txt) > 9000 else "")]
    (OUT / f"{f}.txt").write_text("\n".join(parts) + "\n", encoding="utf-8")
(OUT.parent / "fids.json").write_text(json.dumps([r["fid"] for r in todo]) + "\n")
print(len(todo))
