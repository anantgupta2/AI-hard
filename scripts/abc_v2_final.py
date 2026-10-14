"""Merge the v2 A/B labels (data/abc_v2/BUCKETS_PLAN.md) and report statistics for the whole release.

Final record per family: the adjudicated record if the family was disputed, otherwise pass A (both passes agreed
on every compared field). Writes data/abc_v2/labels_v2.json, data/abc_v2/stats.json and prints a markdown report
(save it as data/abc_v2/report.md).
"""
import csv
import glob
import json
import random
import re
import sys
from collections import Counter
from math import sqrt
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data/abc_v2"
cat = {r["family_id"]: r for r in csv.DictReader(open(ROOT / "data/catalog_families.csv", encoding="utf-8"))}

MATRIX = {"M1": "property holds", "M2": "existence", "M3": "counterexample", "M4": "non-existence",
          "M5": "equivalence", "M6": "classification", "M7": "identity/isomorphism", "M8": "one-sided bound",
          "M9": "exact value/sharp", "M10": "computational status", "M11": "metamathematical", "M12": "limit law"}
PROBLEM = {"P1": "named conjecture", "P2": "open question", "P3": "problem list", "P4": "record", "P5": "nothing posed"}
OUTCOME = {"O1": "settled yes", "O2": "settled no", "O3": "refute + replace", "O4": "independent",
           "O5": "special case", "O6": "conditional", "O7": "record progress", "O8": "extension", "O9": "new proof"}


def load(pattern):
    out = {}
    for p in sorted(glob.glob(str(D / pattern))):
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                out[str(r["fid"]).zfill(3)] = r
    return out


A, B, ADJ = load("full/pass_a*.jsonl"), load("full/pass_b*.jsonl"), load("full/adjudicated_*.jsonl")
disputed = json.loads((D / "full/disputes.json").read_text(encoding="utf-8"))
missing_adj = sorted(set(disputed) - set(ADJ))


def norm_prefix(p):
    p = str(p or "").replace(" ", "").replace("^", "")
    return "none" if p.lower() in ("", "none", "∅") else p


def flags(r, k):
    out = []
    for f in r.get(k) or []:
        out += list(f) if isinstance(f, dict) else [f]
    return sorted(set(out))


final = []
for fid in sorted(cat):
    r = ADJ.get(fid) or A[fid]
    c = cat[fid]
    pre = norm_prefix(r.get("A_prefix"))
    final.append({
        "fid": fid, "title": c["title"], "subject": c["subject"], "lean": bool(c["lean_dirs"] or c["comparators"]),
        "claim_formal": r.get("claim_formal"), "A_prefix": pre,
        "A_outer": "none" if pre == "none" else pre[0],
        "alternations": 0 if pre == "none" else sum(1 for i in range(1, len(pre)) if (pre[i] in "∀ℙ") != (pre[i - 1] in "∀ℙ") and pre[i] in "∀∃ℙ"),
        "A_matrix": r.get("A_matrix"), "A_flags": flags(r, "A_flags"),
        "B_problem": r.get("B_problem"), "B_outcome": r.get("B_outcome"), "B_flags": flags(r, "B_flags"),
        "lean_vs_headline": r.get("lean_vs_headline"), "source": "adjudicated" if fid in ADJ else "agreed",
    })
(D / "labels_v2.json").write_text(json.dumps(final, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
n = len(final)


def cramers_v(x, y):
    xs, ys = sorted(set(x)), sorted(set(y))
    if len(xs) < 2 or len(ys) < 2:
        return 0.0
    tab, rx, ry, N = Counter(zip(x, y)), Counter(x), Counter(y), len(x)
    chi2 = sum((tab[(i, j)] - rx[i] * ry[j] / N) ** 2 / (rx[i] * ry[j] / N) for i in xs for j in ys)
    return sqrt(chi2 / (N * (min(len(xs), len(ys)) - 1)))


def perm_p(x, y, iters=3000, seed=20261014):
    rng, v0, y, hits = random.Random(seed), cramers_v(x, y), list(y), 0
    for _ in range(iters):
        rng.shuffle(y)
        hits += cramers_v(x, y) >= v0 - 1e-12
    return v0, (hits + 1) / (iters + 1)


def dist(key, names=None):
    c = Counter(r[key] for r in final)
    return " · ".join(f"{k}{' ' + names[k] if names and k in names else ''} {v} ({100 * v / n:.0f}%)"
                      for k, v in sorted(c.items(), key=lambda t: -t[1]))


def crosstab(rows_key, cols_key, cols, pct=True):
    xs = sorted(set(r[rows_key] for r in final), key=str)
    tab = Counter((r[rows_key], r[cols_key]) for r in final)
    out = [f"| {rows_key} \\ {cols_key} | " + " | ".join(cols) + " | n |", "|" + "---|" * (len(cols) + 2)]
    for i in xs:
        tot = sum(1 for r in final if r[rows_key] == i)
        cells = [(f"{100 * tab[(i, j)] / tot:.0f}%" if pct else str(tab[(i, j)])) if tab[(i, j)] else "·" for j in cols]
        out.append(f"| {i} | " + " | ".join(cells) + f" | {tot} |")
    return "\n".join(out)


stats = {"n": n, "adjudicated": len(ADJ), "missing_adjudication": missing_adj}
print(f"# v2 A/B labels for the whole release ({n} families)\n")
print(f"{n - len(ADJ)} families agreed on every field in two independent passes; {len(ADJ)} were adjudicated."
      + (f" Missing adjudication: {missing_adj}" if missing_adj else "") + "\n")
print("## Distributions\n")
print("**A.matrix:** " + dist("A_matrix", MATRIX) + "\n")
print("**A.prefix, outermost quantifier:** " + dist("A_outer") + "\n")
pc = Counter(r["A_prefix"] for r in final)
print("**A.prefix, full (top 12):** " + " · ".join(f"`{k}` {v}" for k, v in pc.most_common(12)) + f" · {len(pc)} distinct prefixes\n")
print("**Quantifier alternations:** " + " · ".join(f"{k}: {v}" for k, v in sorted(Counter(r['alternations'] for r in final).items())) + "\n")
fc = Counter(f for r in final for f in r["A_flags"])
print("**A.flags:** " + " · ".join(f"{k} {v}" for k, v in fc.most_common()) + "\n")
print("**B.problem:** " + dist("B_problem", PROBLEM) + "\n")
print("**B.outcome:** " + dist("B_outcome", OUTCOME) + "\n")
bc = Counter(f for r in final for f in r["B_flags"])
print("**B.flags:** " + " · ".join(f"{k} {v}" for k, v in bc.most_common()) + "\n")
print("**Lean vs headline:** " + dist("lean_vs_headline") + "\n")
for k in ("A_matrix", "A_outer", "B_problem", "B_outcome", "lean_vs_headline"):
    stats[f"dist_{k}"] = dict(Counter(r[k] for r in final))
stats["dist_prefix"] = dict(pc)
stats["A_flags"], stats["B_flags"] = dict(fc), dict(bc)

print("## Associations (Cramér's V, permutation p)\n\n| pair | V | p |\n|---|---|---|")
stats["assoc"] = {}
for u, w in [("A_matrix", "B_outcome"), ("A_matrix", "B_problem"), ("A_outer", "A_matrix"), ("B_problem", "B_outcome"),
             ("A_matrix", "subject"), ("B_outcome", "subject"), ("A_outer", "subject"), ("A_matrix", "lean"),
             ("B_outcome", "lean"), ("lean_vs_headline", "B_outcome")]:
    rows = [r for r in final if not (u == "lean_vs_headline" and r[u] == "no_lean")]
    v, p = perm_p([r[u] for r in rows], [r[w] for r in rows])
    stats["assoc"][f"{u}x{w}"] = [round(v, 3), round(p, 4)]
    print(f"| {u} × {w} | {v:.2f} | {p:.3f} |")

print("\n## A.matrix × B.outcome (counts)\n\n" + crosstab("A_matrix", "B_outcome", list(OUTCOME), pct=False))
print("\n## A.matrix by subject (row %)\n\n" + crosstab("subject", "A_matrix", list(MATRIX)))
print("\n## B.outcome by subject (row %)\n\n" + crosstab("subject", "B_outcome", list(OUTCOME)))
print("\n## Outermost quantifier by A.matrix (counts)\n\n" + crosstab("A_matrix", "A_outer", ["∀", "∃", "ℙ", "none"], pct=False))
lr = [r for r in final if r["lean"]]
print(f"\n## Lean coverage of the headline ({len(lr)} formalized families)\n")
print(" · ".join(f"{k} {v} ({100 * v / len(lr):.0f}%)" for k, v in Counter(r['lean_vs_headline'] for r in lr).most_common()))

# Reliability: the two passes against each other, and the final labels against the in-depth v1 labels.
print("\n## Reliability\n")
def kappa(x, y):
    N = len(x); po = sum(a == b for a, b in zip(x, y)) / N
    cx, cy = Counter(x), Counter(y); pe = sum(cx[k] * cy[k] for k in set(x) | set(y)) / N ** 2
    return po, (po - pe) / (1 - pe)
print("| field | pass A vs pass B agreement | κ |\n|---|---|---|")
for k, g in [("A_matrix", lambda r: r.get("A_matrix")), ("A_prefix", lambda r: norm_prefix(r.get("A_prefix"))),
             ("B_problem", lambda r: r.get("B_problem")), ("B_outcome", lambda r: r.get("B_outcome"))]:
    po, kk = kappa([g(A[f]) for f in sorted(cat)], [g(B[f]) for f in sorted(cat)])
    stats.setdefault("interrater", {})[k] = [round(po, 3), round(kk, 3)]
    print(f"| {k} | {100 * po:.0f}% | {kk:.2f} |")
V1A = {"M1": "A1", "M2": "A2", "M3": "A2", "M4": "A5", "M5": "A4", "M6": "A4", "M7": "A1", "M8": "A3", "M9": "A3",
       "M10": "A5", "M11": "A5", "M12": "A3"}
V1B = {"O1": "B1", "O2": "B2", "O3": "B2", "O4": "B1", "O5": "B3", "O6": "B3", "O7": "B3", "O8": "B4", "O9": "B4"}
deep = {}
for f in json.loads((ROOT / "data/dashboard/families.json").read_text(encoding="utf-8")):
    g = {ax: (re.search(rf"\b{ax}[1-5]\b", str(f[k] or "")) or [None])[0] for ax, k in (("A", "A"), ("B", "B"))}
    if all(g.values()):
        deep[f["fid"]] = g
fd = {r["fid"]: r for r in final}
gold = [f for f in deep if f in fd]
a = sum(V1A.get(fd[f]["A_matrix"]) == deep[f]["A"] for f in gold) / len(gold)
b = sum(V1B.get(fd[f]["B_outcome"]) == deep[f]["B"] for f in gold) / len(gold)
stats["vs_deep_v1"] = [round(a, 3), round(b, 3), len(gold)]
print(f"\nFinal labels vs the in-depth v1 labels through the v1 mapping ({len(gold)} families): A {100 * a:.0f}%, B {100 * b:.0f}%.")
(D / "stats.json").write_text(json.dumps(stats, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
