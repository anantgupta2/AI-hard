"""Joint split of proof type (axis C from the bulk pass, data/abc_bulk/labels_all.json) against the v2 labels
(data/abc_v2/labels_v2.json): outermost quantifier, what is asserted, what was posed, outcome, and Lean coverage.
C is the primary proof method: C1 construction, C2 induction/iteration, C3 indirect, C4 estimation chain,
C5 reduction/transfer. Writes data/proof_type_joint.json and prints markdown tables."""
import json
import sys
from collections import Counter
from math import sqrt
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
C = {"C1": "Construction", "C2": "Induction / iteration", "C3": "Indirect", "C4": "Estimation chain", "C5": "Reduction / transfer"}
bulk = {r["fid"]: r for r in json.loads((ROOT / "data/abc_bulk/labels_all.json").read_text(encoding="utf-8"))}
v2 = json.loads((ROOT / "data/abc_v2/labels_v2.json").read_text(encoding="utf-8"))
rows = [{**r, "C": bulk[r["fid"]]["C"], "C_all": bulk[r["fid"]]["C_all"], "computer_assisted": bulk[r["fid"]]["computer_assisted"]} for r in v2]
n = len(rows)


def cramers_v(x, y):
    xs, ys, N = sorted(set(x)), sorted(set(y)), len(x)
    tab, rx, ry = Counter(zip(x, y)), Counter(x), Counter(y)
    chi2 = sum((tab[(i, j)] - rx[i] * ry[j] / N) ** 2 / (rx[i] * ry[j] / N) for i in xs for j in ys)
    return sqrt(chi2 / (N * (min(len(xs), len(ys)) - 1)))


def table(key, cols, label):
    out = [f"| Proof type \\ {label} | " + " | ".join(cols) + " | n |", "|" + "---|" * (len(cols) + 2)]
    for c in C:
        sub = [r for r in rows if r["C"] == c]
        cnt = Counter(r[key] for r in sub)
        out.append(f"| {c} {C[c]} | " + " | ".join(f"{100 * cnt[k] / len(sub):.0f}%" if cnt[k] else "·" for k in cols) + f" | {len(sub)} |")
    cnt = Counter(r[key] for r in rows)
    out.append("| **All** | " + " | ".join(f"{100 * cnt[k] / n:.0f}%" for k in cols) + f" | {n} |")
    return "\n".join(out)


res = {"n": n, "C": dict(Counter(r["C"] for r in rows)), "assoc": {}}
print("Proof type: " + " · ".join(f"{c} {C[c]} {k} ({100 * k / n:.0f}%)" for c, k in sorted(res["C"].items())) + "\n")
for key, cols, label in [("A_outer", ["∀", "∃", "none", "ℙ"], "outer quantifier"),
                         ("A_matrix", ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12"], "asserts"),
                         ("B_problem", ["P1", "P2", "P3", "P4", "P5"], "posed"),
                         ("B_outcome", ["O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9"], "outcome"),
                         ("lean_vs_headline", ["same", "weaker", "different", "no_lean"], "Lean")]:
    v = cramers_v([r["C"] for r in rows], [r[key] for r in rows])
    res["assoc"][key] = round(v, 3)
    print(f"### Proof type × {label} (row %, Cramér's V = {v:.2f})\n\n" + table(key, cols, label) + "\n")
res["computer_assisted"] = sum(r["computer_assisted"] for r in rows)
(ROOT / "data/proof_type_joint.json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
