"""Collect the fields where the two v2 passes disagree and split them into adjudication batches.
Writes data/abc_v2/full/disputes.json and data/abc_v2/full/adj_<k>.txt (fids, ~40 per batch)."""
import glob, json, re, sys
from pathlib import Path
PRIOR_RE = re.compile(r"already (proved|settled|known)|earlier work|prior (work|result)|previously (proved|settled)|full_only|remaining case|last open", re.I)
import csv as _csv
SUBJ = {r["family_id"]: r["subject"] for r in _csv.DictReader(open(Path(__file__).resolve().parent.parent / "data/catalog_families.csv", encoding="utf-8"))}
LIMIT_RE = re.compile(r"scaling limit|converge|in law|in distribution|universality|→ ?∞|n ?→ ?∞|limit shape|free energy|lim(_| )|tends to", re.I)
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
D = Path(__file__).resolve().parent.parent / "data/abc_v2/full"
def load(pat):
    out = {}
    for p in sorted(glob.glob(str(D / pat))):
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line); out[str(r["fid"]).zfill(3)] = r
    return out
A, B = load("pass_a*.jsonl"), load("pass_b*.jsonl")
norm = lambda p: "none" if str(p or "").replace(" ", "").replace("^", "").lower() in ("", "none") else str(p).replace(" ", "").replace("^", "")
FIELDS = {"A_matrix": lambda r: r.get("A_matrix"), "A_prefix": lambda r: norm(r.get("A_prefix")),
          "B_problem": lambda r: r.get("B_problem"), "B_outcome": lambda r: r.get("B_outcome"),
          "lean_vs_headline": lambda r: r.get("lean_vs_headline")}
missing = sorted(set(A) ^ set(B))
disputes = {}
for f in sorted(set(A) & set(B)):
    d = [k for k, g in FIELDS.items() if g(A[f]) != g(B[f])]
    # Rule 13 (M12 limit law) was added after labelling: send every plausible limit theorem for a check.
    text = " ".join(str(r.get(k, "")) for r in (A[f], B[f]) for k in ("claim_formal", "notes"))
    if LIMIT_RE.search(text) and "A_matrix" not in d:
        d.append("A_matrix (rule 13 check)")
    # Rules 12 and 18 were written after labelling began: re-check agreed labels they may change.
    subj = SUBJ.get(f, "")
    if "A_matrix" not in d and A[f].get("A_matrix") in ("M8", "M9") and subj == "Theoretical computer science":
        d.append("A_matrix (rule 18 check)")
    if "B_outcome" not in d and A[f].get("B_outcome") == "O5" and PRIOR_RE.search(text):
        d.append("B_outcome (rule 12 check)")
    if d:
        disputes[f] = {"fields": d, "pass_a": A[f], "pass_b": B[f]}
(D / "disputes.json").write_text(json.dumps(disputes, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
fids = sorted(disputes); k = max(1, -(-len(fids) // 30))
for i in range(k):
    (D / f"adj_{i}.txt").write_text("\n".join(fids[i::k]) + "\n", encoding="utf-8")
print(f"{len(set(A) & set(B))} families in both passes; missing from one pass: {missing}")
print(f"{len(disputes)} families with a disputed field, in {k} batches")
from collections import Counter
print(Counter(x for v in disputes.values() for x in v["fields"]))
