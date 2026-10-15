"""Technical pages per paper by field: release manuscripts (subject of their family) against the human frontier
baseline (data/frontier_lengths.json, tagged with the same subject names). Writes data/length_by_field.json and
prints a markdown table."""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import median

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
subj = {r["family_id"]: r["subject"] for r in csv.DictReader(open(ROOT / "data/catalog_families.csv", encoding="utf-8"))}
rel, hum = defaultdict(list), defaultdict(list)
for m in json.loads((ROOT / "data/proof_lengths.json").read_text(encoding="utf-8"))["manuscripts"]:
    if m["doc_words"]:
        rel[subj[m["fid"]]].append(m)
for r in json.loads((ROOT / "data/frontier_lengths.json").read_text(encoding="utf-8")):
    if "error" not in r:
        hum[r["subject"]].append(r)
rows = []
for f in sorted(rel, key=lambda f: -median(m["technical_pages"] for m in rel[f])):
    rt, ht = [m["technical_pages"] for m in rel[f]], [r["technical_pages"] for r in hum.get(f, [])]
    rp = [m["longest_proof_pages"] for m in rel[f] if m["n_proofs"]]
    hp = [r["longest_proof_pages"] for r in hum.get(f, []) if (r["proof_share"] or 0) > 0.25]
    rows.append({"key": f, "subject": f, "release_n": len(rt), "release_median": round(median(rt), 1),
                 "human_n": len(ht), "human_median": round(median(ht), 1) if ht else None,
                 "ratio": round(median(rt) / median(ht), 2) if ht else None,
                 "release_longest_proof_median": round(median(rp), 1) if rp else None,
                 "human_longest_proof_median": round(median(hp), 1) if hp else None, "human_longest_proof_n": len(hp),
                 "human_papers": "; ".join(r["name"].split(":")[0] for r in hum.get(f, []))})
(ROOT / "data/length_by_field.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
allr = [m["technical_pages"] for v in rel.values() for m in v]
allh = [r["technical_pages"] for v in hum.values() for r in v]
print(f"All fields: release {median(allr):.0f} (n={len(allr)}), human {median(allh):.0f} (n={len(allh)})\n")
print("| Field | Release median (n) | Human median (n) | Release ÷ human | Longest proof: release / human |\n|---|---|---|---|---|")
for r in rows:
    print(f"| {r['subject']} | {r['release_median']:.0f} ({r['release_n']}) | {r['human_median'] if r['human_median'] is not None else '–'} ({r['human_n']}) | "
          f"{r['ratio'] if r['ratio'] else '–'} | {r['release_longest_proof_median']} / {r['human_longest_proof_median'] if r['human_longest_proof_median'] is not None else '–'} ({r['human_longest_proof_n']}) |")
