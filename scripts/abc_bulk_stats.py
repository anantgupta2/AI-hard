"""Merge the cheap A/B/C labels for all 372 families (data/abc_bulk/labels_*.jsonl), report distributions,
breakdowns by subject and Lean, pairwise associations (Cramer's V, permutation p), and agreement with the
in-depth labels of the analysed families (Cohen's kappa).

Run: python scripts/abc_bulk_stats.py  -> prints a markdown report, writes data/abc_bulk/labels_all.json
and data/abc_bulk/stats.json
"""
import csv
import glob
import json
import random
import re
import sys
from collections import Counter
from itertools import combinations
from math import sqrt
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
CODES = {"A": ["A1", "A2", "A3", "A4", "A5"], "B": ["B1", "B2", "B3", "B4"], "C": ["C1", "C2", "C3", "C4", "C5"]}
NAMES = {"A1": "universal", "A2": "existential", "A3": "quantitative/sharp", "A4": "characterization", "A5": "impossibility",
         "B1": "confirms", "B2": "refutes", "B3": "partial/conditional", "B4": "extends",
         "C1": "construction", "C2": "induction", "C3": "indirect", "C4": "estimation", "C5": "reduction"}

cat = {r["family_id"]: r for r in csv.DictReader(open(ROOT / "data/catalog_families.csv", encoding="utf-8"))}
labels = {}
for p in sorted(glob.glob(str(ROOT / "data/abc_bulk/labels_*.jsonl"))):
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            labels[str(r["fid"]).zfill(3)] = r
rows = []
for fid, r in sorted(labels.items()):
    c = cat.get(fid, {})
    rows.append({"fid": fid, "A": r["A"], "B": r["B"], "C": r["C_primary"],
                 "C_all": sorted(set([r["C_primary"]] + list(r.get("C_secondary") or []))),
                 "subject": c.get("subject", "?"), "lean": "Lean" if c.get("lean_dirs") else "no Lean",
                 "computer_assisted": bool(r.get("computer_assisted")), "confidence": r.get("confidence")})
n = len(rows)
missing = sorted(set(cat) - set(labels))
(ROOT / "data/abc_bulk/labels_all.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def cramers_v(x, y):
    xs, ys = sorted(set(x)), sorted(set(y))
    if len(xs) < 2 or len(ys) < 2:
        return 0.0
    tab, rx, ry, N = Counter(zip(x, y)), Counter(x), Counter(y), len(x)
    chi2 = sum((tab[(i, j)] - rx[i] * ry[j] / N) ** 2 / (rx[i] * ry[j] / N) for i in xs for j in ys)
    return sqrt(chi2 / (N * (min(len(xs), len(ys)) - 1)))


def perm_p(x, y, iters=5000, seed=20261012):
    rng, v0, y, hits = random.Random(seed), cramers_v(x, y), list(y), 0
    for _ in range(iters):
        rng.shuffle(y)
        hits += cramers_v(x, y) >= v0 - 1e-12
    return v0, (hits + 1) / (iters + 1)


def crosstab(x, y, ys=None):
    xs, ys = sorted(set(x)), ys or sorted(set(y))
    tab = Counter(zip(x, y))
    out = ["| | " + " | ".join(ys) + " | n |", "|" + "---|" * (len(ys) + 2)]
    for i in xs:
        tot = sum(tab[(i, j)] for j in ys)
        out.append(f"| {i} | " + " | ".join(f"{100 * tab[(i, j)] / tot:.0f}%" if tab[(i, j)] else "·" for j in ys) + f" | {tot} |")
    return "\n".join(out)


stats = {"n": n, "missing": missing}
print(f"# A/B/C labels for the whole release ({n} of {len(cat)} families)\n")
if missing:
    print("Missing:", ", ".join(missing), "\n")
for ax in "ABC":
    cnt = Counter(r[ax] for r in rows)
    stats[f"dist_{ax}"] = dict(sorted(cnt.items()))
    print(f"**{ax}:** " + " · ".join(f"{k} {NAMES[k]} {v} ({100 * v / n:.0f}%)" for k, v in sorted(cnt.items())))
call = Counter(c for r in rows for c in r["C_all"])
stats["c_any"] = dict(sorted(call.items()))
print("\n**C anywhere (primary or secondary):** " + " · ".join(f"{k} {100 * v / n:.0f}%" for k, v in sorted(call.items())))
print(f"\nComputer-assisted: {sum(r['computer_assisted'] for r in rows)} · mean label confidence "
      f"{sum(r['confidence'] or 0 for r in rows) / n:.2f}\n")

print("## Associations (Cramer's V, permutation p)\n\n| pair | V | p |\n|---|---|---|")
stats["assoc"] = {}
for u, w in [("A", "B"), ("A", "C"), ("B", "C"), ("A", "subject"), ("B", "subject"), ("C", "subject"),
             ("A", "lean"), ("B", "lean"), ("C", "lean")]:
    v, p = perm_p([r[u] for r in rows], [r[w] for r in rows])
    stats["assoc"][f"{u}x{w}"] = [round(v, 3), round(p, 4)]
    print(f"| {u} × {w} | {v:.2f} | {p:.3f} |")

for u, w in [("A", "B"), ("A", "C"), ("B", "C")]:
    print(f"\n### {u} × {w} (row %)\n\n" + crosstab([r[u] for r in rows], [r[w] for r in rows], CODES[w]))
for ax in "ABC":
    print(f"\n### {ax} by subject (row %)\n\n" + crosstab([r["subject"] for r in rows], [r[ax] for r in rows], CODES[ax]))
for ax in "ABC":
    print(f"\n### {ax} by Lean (row %)\n\n" + crosstab([r["lean"] for r in rows], [r[ax] for r in rows], CODES[ax]))

# Agreement with the in-depth family labels.
deep = {}
for f in json.loads((ROOT / "data/dashboard/families.json").read_text(encoding="utf-8")):
    g = {ax: (re.search(rf"\b{ax}[1-5]\b", str(f[k] or "")) or [None])[0] for ax, k in (("A", "A"), ("B", "B"), ("C", "C_primary"))}
    if all(g.values()):
        deep[f["fid"]] = g


def kappa(a, b):
    N = len(a)
    po = sum(x == y for x, y in zip(a, b)) / N
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(a) | set(b)) / N ** 2
    return po, (po - pe) / (1 - pe) if pe < 1 else 1.0


common = [f for f in deep if f in labels]
stats["agreement"] = {}
print(f"\n## Agreement with the in-depth labels ({len(common)} families)\n\n| axis | raw agreement | Cohen's κ |\n|---|---|---|")
by_fid = {r["fid"]: r for r in rows}
for ax in "ABC":
    po, k = kappa([deep[f][ax] for f in common], [by_fid[f][ax] for f in common])
    stats["agreement"][ax] = [round(po, 3), round(k, 3)]
    print(f"| {ax} | {100 * po:.0f}% | {k:.2f} |")
(ROOT / "data/abc_bulk/stats.json").write_text(json.dumps(stats, indent=1) + "\n", encoding="utf-8")
