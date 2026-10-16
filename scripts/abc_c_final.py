"""Two-axis proof type (data/abc_c/C_PLAN.md): compare the independent passes, prepare adjudication batches, merge
final labels and print the joint split against the v2 labels.

python scripts/abc_c_final.py prep   -> pass agreement, data/abc_c/full/disputes.json, adj_<k>.txt batches
python scripts/abc_c_final.py final  -> data/abc_c/labels_c.json, stats.json, and a markdown report on stdout"""
import glob
import json
import sys
from collections import Counter
from math import sqrt
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data/abc_c"
FORM = {"F1": "Direct", "F2": "Contradiction", "F3": "Induction / iteration", "F4": "Explicit construction",
        "F5": "Non-constructive existence", "F6": "Exhaustion / cases"}
ENGINE = {"E1": "Estimates", "E2": "Algebraic computation", "E3": "Combinatorial", "E4": "Structural / categorical",
          "E5": "Geometric / topological", "E6": "Assembly of cited results", "E7": "Computation"}


def load(pattern):
    out = {}
    for p in sorted(glob.glob(str(D / "full" / pattern))):
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                out[str(r["fid"]).zfill(3)] = r
    return out


def kappa(x, y):
    n = len(x)
    po = sum(a == b for a, b in zip(x, y)) / n
    cx, cy = Counter(x), Counter(y)
    pe = sum(cx[k] * cy[k] for k in set(x) | set(y)) / n ** 2
    return po, (po - pe) / (1 - pe)


def cramers_v(x, y):
    xs, ys, N = sorted(set(x)), sorted(set(y)), len(x)
    tab, rx, ry = Counter(zip(x, y)), Counter(x), Counter(y)
    chi2 = sum((tab[(i, j)] - rx[i] * ry[j] / N) ** 2 / (rx[i] * ry[j] / N) for i in xs for j in ys)
    return sqrt(chi2 / (N * (min(len(xs), len(ys)) - 1)))


A, B = load("pass_a*.jsonl"), load("pass_b*.jsonl")
common = sorted(set(A) & set(B))


def prep():
    print(f"pass A {len(A)}, pass B {len(B)}, both {len(common)}")
    for k in ("form", "engine"):
        po, kk = kappa([A[f][k] for f in common], [B[f][k] for f in common])
        print(f"{k}: agreement {100 * po:.0f}%, kappa {kk:.2f}")
    disputes = {f: {"fields": [k for k in ("form", "engine") if A[f][k] != B[f][k]], "a": A[f], "b": B[f]}
                for f in common if A[f]["form"] != B[f]["form"] or A[f]["engine"] != B[f]["engine"]}
    # Sweeps of agreed families for the conventions in adjudicator_brief.md, and 248 (the brief's worked example).
    import re
    SCALING = re.compile(r"tightness|subsequential|scaling limit|continuum limit|converge[sd]? (?:in law|weakly)", re.I)
    for f in common:
        if f in disputes:
            continue
        text = " ".join([A[f].get("backbone") or "", B[f].get("backbone") or ""])
        if SCALING.search(text) and A[f]["form"] != "F5":
            disputes[f] = {"fields": ["form (scaling-limit convention check)"], "a": A[f], "b": B[f]}
        elif f == "248":
            disputes[f] = {"fields": ["form (worked example in the brief: decide from the paper)"], "a": A[f], "b": B[f]}
    (D / "full/disputes.json").write_text(json.dumps(disputes, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    fids = sorted(disputes)
    k = max(1, round(len(fids) / 30))
    for i in range(k):
        (D / f"full/adj_{i}.txt").write_text("\n".join(fids[i::k]) + "\n")
    print(f"{len(disputes)} disputed families in {k} batches")


def final():
    ADJ = load("adjudicated_*.jsonl")
    v2 = {r["fid"]: r for r in json.loads((ROOT / "data/abc_v2/labels_v2.json").read_text(encoding="utf-8"))}
    rows = []
    for f in sorted(v2):
        r = ADJ.get(f) or A[f]
        rows.append({"fid": f, "form": r["form"], "form_secondary": r.get("form_secondary", []), "engine": r["engine"],
                     "engine_secondary": r.get("engine_secondary", []), "computer_assisted": r.get("computer_assisted", False),
                     "backbone": r.get("backbone"), "source": "adjudicated" if f in ADJ else "agreed",
                     "outer": v2[f]["A_outer"], "matrix": v2[f]["A_matrix"], "problem": v2[f]["B_problem"],
                     "outcome": v2[f]["B_outcome"], "lean": v2[f]["lean_vs_headline"], "subject": v2[f]["subject"]})
    (D / "labels_c.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    n = len(rows)
    stats = {"n": n, "adjudicated": len(ADJ), "interrater": {}, "assoc": {}}
    print(f"# Proof type on two axes, all {n} families\n")
    print(f"{n - len(ADJ)} families agreed on both axes in two independent passes; {len(ADJ)} were adjudicated.\n")
    print("| Axis | Pass agreement | κ |\n|---|---|---|")
    for k in ("form", "engine"):
        po, kk = kappa([A[f][k] for f in common], [B[f][k] for f in common])
        stats["interrater"][k] = [round(po, 3), round(kk, 3)]
        print(f"| {k} | {100 * po:.0f}% | {kk:.2f} |")
    for key, names in (("form", FORM), ("engine", ENGINE)):
        c = Counter(r[key] for r in rows)
        stats[f"dist_{key}"] = dict(c)
        print(f"\n**{key}:** " + " · ".join(f"{k} {names.get(k, k)} {v} ({100 * v / n:.0f}%)" for k, v in sorted(c.items())))
    print(f"\nComputer-assisted: {sum(r['computer_assisted'] for r in rows)}\n")

    def table(rk, rnames, ck, cols, label, pct=True):
        out = [f"| {label} | " + " | ".join(cols) + " | n |", "|" + "---|" * (len(cols) + 2)]
        for a in rnames:
            sub = [r for r in rows if r[rk] == a]
            if not sub:
                continue
            cnt = Counter(r[ck] for r in sub)
            out.append(f"| {a} {rnames[a]} | " + " | ".join((f"{100 * cnt[k] / len(sub):.0f}%" if pct else str(cnt[k])) if cnt[k] else "·" for k in cols) + f" | {len(sub)} |")
        cnt = Counter(r[ck] for r in rows)
        out.append("| **All** | " + " | ".join((f"{100 * cnt[k] / n:.0f}%" if pct else str(cnt[k])) for k in cols) + f" | {n} |")
        return "\n".join(out)

    pairs = [("outer", ["∀", "∃", "none", "ℙ"], "outer quantifier"),
             ("matrix", ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12"], "asserts"),
             ("problem", ["P1", "P2", "P3", "P4", "P5"], "posed"),
             ("outcome", ["O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9"], "outcome")]
    for axis, names in (("form", FORM), ("engine", ENGINE)):
        for ck, cols, label in pairs:
            v = cramers_v([r[axis] for r in rows], [r[ck] for r in rows])
            stats["assoc"][f"{axis}x{ck}"] = round(v, 3)
            print(f"### {axis} × {label} (row %, Cramér's V = {v:.2f})\n\n" + table(axis, names, ck, cols, axis) + "\n")
    v = cramers_v([r["form"] for r in rows], [r["engine"] for r in rows])
    stats["assoc"]["formxengine"] = round(v, 3)
    print(f"### form × engine (counts, Cramér's V = {v:.2f})\n\n" + table("form", FORM, "engine", list(ENGINE), "form", pct=False) + "\n")
    (D / "stats.json").write_text(json.dumps(stats, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    {"prep": prep, "final": final}[sys.argv[1]]()
