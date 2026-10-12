"""Distributions and pairwise associations of the codebook labels A (logical form), B (relation to the
posed problem) and C (proof method), over the analysed families in data/dashboard/families.json.

Association = Cramer's V with a permutation p-value (no scipy needed). With ~40 families, treat
every p-value as descriptive: cells are small and many pairs are tested.

Run: python scripts/abc_label_stats.py  -> prints a report, writes data/abc_label_stats.json
"""
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
fams = json.loads((ROOT / "data/dashboard/families.json").read_text(encoding="utf-8"))

NAMES = {
    "A": {"A1": "universal", "A2": "existential/counterexample", "A3": "quantitative/sharp",
          "A4": "characterization", "A5": "impossibility"},
    "B": {"B1": "confirms", "B2": "refutes", "B3": "partial/conditional", "B4": "extends"},
    "C": {"C1": "construction", "C2": "induction", "C3": "indirect", "C4": "estimation chain",
          "C5": "reduction/transfer"},
}


def first(label, axis):
    """Headline label: the first A1..A5 / B1..B4 / C1..C5 code in the field (e.g. 'A3 (M1) / A1 (M2)' -> A3)."""
    m = re.search(rf"\b{axis}[1-5]\b", str(label or ""))
    return m.group(0) if m else None


def all_codes(text, axis):
    return sorted(set(re.findall(rf"\b{axis}[1-5]\b", str(text or ""))))


rows = []
for f in fams:
    a, b, c = first(f["A"], "A"), first(f["B"], "B"), first(f["C_primary"], "C")
    if not (a and b and c):
        continue
    d = "D2" if str(f["D"]).startswith("D2") else "D3"
    ih = str(f.get("ih_template") or "").strip().lower()
    rows.append({
        "fid": f["fid"], "A": a, "B": b, "C": c, "D": d,
        "C_all": sorted(set([c] + all_codes(f["C_secondary"], "C"))),
        "lean": "Lean" if f["has_lean"] else "no Lean",
        "ih_strengthened": "no" if ih in ("", "false", "n/a") or ih.startswith("n/a") else "yes",
        "D_conf": float(f["D_confidence"]) if f.get("D_confidence") not in (None, "") else None,
    })
n = len(rows)


def cramers_v(x, y):
    xs, ys = sorted(set(x)), sorted(set(y))
    if len(xs) < 2 or len(ys) < 2:
        return 0.0
    tab = Counter(zip(x, y))
    rx, ry = Counter(x), Counter(y)
    chi2 = sum((tab[(i, j)] - rx[i] * ry[j] / len(x)) ** 2 / (rx[i] * ry[j] / len(x)) for i in xs for j in ys)
    return sqrt(chi2 / (len(x) * (min(len(xs), len(ys)) - 1)))


def perm_p(x, y, iters=20000, seed=20261012):
    rng = random.Random(seed)
    v0 = cramers_v(x, y)
    y = list(y)
    hits = 0
    for _ in range(iters):
        rng.shuffle(y)
        hits += cramers_v(x, y) >= v0 - 1e-12
    return v0, (hits + 1) / (iters + 1)


def crosstab(x, y):
    xs, ys = sorted(set(x)), sorted(set(y))
    tab = Counter(zip(x, y))
    head = "| | " + " | ".join(ys) + " | total |\n|" + "---|" * (len(ys) + 2)
    lines = [head] + [f"| **{i}** | " + " | ".join(str(tab[(i, j)] or "·") for j in ys) + f" | {sum(tab[(i, j)] for j in ys)} |" for i in xs]
    return "\n".join(lines)


out = {"n_families": n, "distributions": {}, "c_cooccurrence": {}, "associations": []}
print(f"# A/B/C label statistics ({n} families with all three headline labels)\n")
for ax in "ABC":
    cnt = Counter(r[ax] for r in rows)
    out["distributions"][ax] = dict(sorted(cnt.items()))
    print(f"## {ax}")
    for k, v in sorted(cnt.items()):
        print(f"- {k} {NAMES[ax][k]}: {v} ({100 * v / n:.0f}%)")
    print()

# C as a multi-label: how often each method appears at all, and which methods co-occur.
call = Counter(c for r in rows for c in r["C_all"])
out["c_any"] = dict(sorted(call.items()))
print("## C as primary or secondary (share of families using each method at all)")
for k, v in sorted(call.items()):
    print(f"- {k} {NAMES['C'][k]}: {v} ({100 * v / n:.0f}%)")
pairs = Counter(p for r in rows for p in combinations(r["C_all"], 2))
out["c_cooccurrence"] = {f"{a}+{b}": v for (a, b), v in sorted(pairs.items())}
print("\nMost common method pairs:", ", ".join(f"{a}+{b} {v}" for (a, b), v in pairs.most_common(6)), "\n")

print("## Associations (Cramer's V, permutation p; descriptive only)\n")
print("| pair | V | p |\n|---|---|---|")
for u, w in [("A", "B"), ("A", "C"), ("B", "C"), ("A", "D"), ("B", "D"), ("C", "D"),
             ("C", "ih_strengthened"), ("A", "lean"), ("B", "lean"), ("C", "lean")]:
    v, p = perm_p([r[u] for r in rows], [r[w] for r in rows])
    out["associations"].append({"pair": f"{u}x{w}", "cramers_v": round(v, 3), "perm_p": round(p, 4)})
    print(f"| {u} × {w} | {v:.2f} | {p:.3f} |")

for u, w in [("A", "C"), ("A", "B"), ("B", "C")]:
    print(f"\n### {u} × {w}\n")
    print(crosstab([r[u] for r in rows], [r[w] for r in rows]))

print("\n## Mean confidence in the N3 candidate, D3 families only, by label\n")
for ax in "ABC":
    by = {}
    for r in rows:
        if r["D_conf"] is not None and r["D"] == "D3":
            by.setdefault(r[ax], []).append(r["D_conf"])
    out.setdefault("d3_conf_by", {})[ax] = {k: round(sum(v) / len(v), 3) for k, v in sorted(by.items())}
    print(f"- {ax}: " + ", ".join(f"{k} {sum(v)/len(v):.2f} (n={len(v)})" for k, v in sorted(by.items())))

(ROOT / "data/abc_label_stats.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
