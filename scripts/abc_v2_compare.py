"""Compare the two independent v2 labelling passes (data/abc_v2/BUCKETS_PLAN.md).

Usage: python scripts/abc_v2_compare.py <dir>   (reads <dir>/pass_a*.jsonl and <dir>/pass_b*.jsonl)
Prints per-field agreement and Cohen's kappa, agreement with the in-depth v1 labels through the v1 mapping,
the bucket usage (incl. "other"), and every disagreement; writes <dir>/disagreements.json.
"""
import glob
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
D = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data/abc_v2/pilot"


def load(pattern):
    out = {}
    for p in sorted(glob.glob(str(D / pattern))):
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                out[str(r["fid"]).zfill(3)] = r
    return out


A, B = load("pass_a*.jsonl"), load("pass_b*.jsonl")
common = sorted(set(A) & set(B))
print(f"# v2 pass agreement ({len(common)} families; pass A {len(A)}, pass B {len(B)})\n")


def kappa(x, y):
    n = len(x)
    po = sum(a == b for a, b in zip(x, y)) / n
    cx, cy = Counter(x), Counter(y)
    pe = sum(cx[k] * cy[k] for k in set(x) | set(y)) / n ** 2
    return po, ((po - pe) / (1 - pe) if pe < 1 else 1.0)


def norm_prefix(p):
    p = str(p or "").replace(" ", "").replace("^", "")
    return "none" if p.lower() in ("", "none", "∅") else p


def outer(p):
    p = norm_prefix(p)
    return "none" if p == "none" else p[0]


def flagset(r, k):
    out = set()
    for f in r.get(k) or []:
        out |= set(f) if isinstance(f, dict) else {f}
    return out


fields = {
    "A_matrix": lambda r: r.get("A_matrix"),
    "A_prefix (exact)": lambda r: norm_prefix(r.get("A_prefix")),
    "A_prefix (outermost)": lambda r: outer(r.get("A_prefix")),
    "B_problem": lambda r: r.get("B_problem"),
    "B_outcome": lambda r: r.get("B_outcome"),
}
print("| field | agreement | κ |\n|---|---|---|")
dis = {}
for name, get in fields.items():
    x, y = [get(A[f]) for f in common], [get(B[f]) for f in common]
    po, k = kappa(x, y)
    print(f"| {name} | {100 * po:.0f}% | {k:.2f} |")
    dis[name] = [{"fid": f, "a": get(A[f]), "b": get(B[f])} for f in common if get(A[f]) != get(B[f])]
for k in ("A_flags", "B_flags"):
    agree = sum(flagset(A[f], k) == flagset(B[f], k) for f in common)
    print(f"| {k} (identical set) | {100 * agree / len(common):.0f}% | – |")

# v1 mapping, compared with the in-depth labels.
V1A = {"M1": "A1", "M2": "A2", "M3": "A2", "M4": "A5", "M5": "A4", "M6": "A4", "M7": "A1", "M8": "A3", "M9": "A3",
       "M10": "A5", "M11": "A5"}
V1B = {"O1": "B1", "O2": "B2", "O3": "B2", "O4": "B1", "O5": "B3", "O6": "B3", "O7": "B3", "O8": "B4", "O9": "B4"}
deep = {}
for f in json.loads((ROOT / "data/dashboard/families.json").read_text(encoding="utf-8")):
    g = {ax: (re.search(rf"\b{ax}[1-5]\b", str(f[k] or "")) or [None])[0] for ax, k in (("A", "A"), ("B", "B"))}
    if all(g.values()):
        deep[f["fid"]] = g
gold = [f for f in common if f in deep]
if gold:
    print(f"\n## Against the in-depth v1 labels, via the v1 mapping ({len(gold)} families)\n")
    print("| pass | A agreement | B agreement |\n|---|---|---|")
    for nm, P in (("A", A), ("B", B)):
        a = sum(V1A.get(P[f].get("A_matrix")) == deep[f]["A"] for f in gold) / len(gold)
        b = sum(V1B.get(P[f].get("B_outcome")) == deep[f]["B"] for f in gold) / len(gold)
        print(f"| {nm} | {100 * a:.0f}% | {100 * b:.0f}% |")

print("\n## Bucket usage (both passes)\n")
for k in ("A_matrix", "B_problem", "B_outcome"):
    c = Counter([A[f].get(k) for f in common] + [B[f].get(k) for f in common])
    print(f"- {k}: " + ", ".join(f"{a} {b}" for a, b in sorted(c.items(), key=lambda t: str(t[0]))))
c = Counter([norm_prefix(A[f].get("A_prefix")) for f in common] + [norm_prefix(B[f].get("A_prefix")) for f in common])
print("- A_prefix: " + ", ".join(f"{a} {b}" for a, b in c.most_common()))
others = [(f, p) for f in common for p, P in (("a", A), ("b", B)) if "other" in (P[f].get("A_matrix"), P[f].get("B_outcome"), P[f].get("B_problem"))]
print(f"- 'other' used: {len(others)} times " + ", ".join(f"{f}{p}" for f, p in others))

print("\n## Disagreements\n")
for name in ("A_matrix", "A_prefix (exact)", "B_problem", "B_outcome"):
    for d in dis[name]:
        f = d["fid"]
        print(f"- {f} {name}: A={d['a']} B={d['b']} | A: {A[f].get('claim_formal', '')[:110]}")
(D / "disagreements.json").write_text(json.dumps(dis, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
