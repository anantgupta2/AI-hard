"""Length of the proofs alone (text inside proof environments) and of the claim statements (theorem, lemma,
proposition, corollary, claim and similar environments, found from \\newtheorem / \\declaretheorem) in each manuscript.

Resolves the main .tex through \\input/\\include/\\subfile, strips comments, and collects every environment whose name
contains "proof" (proof, proof*, proofof, proofsketch, ...; nested ones counted once). Words are whitespace tokens
(math tokens included). Pages are estimated per manuscript as proof words x (PDF pages / document words), using the
page counts in data/proof_lengths.json. Updates data/proof_lengths.json in place and prints a summary."""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import median, quantiles
import csv

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
REL = ROOT / "data/raw/openai-math"
PL = ROOT / "data/proof_lengths.json"
INC = re.compile(r"\\(?:input|include|subfile|import\{[^}]*\})\s*\{([^}]+)\}")
ENV = re.compile(r"\\(begin|end)\{([A-Za-z]*proof[A-Za-z]*\*?)\}")


def strip(t):
    return re.sub(r"(?<!\\)%.*", "", t)


def resolve(p, seen):
    if p in seen or not p.exists():
        return ""
    seen.add(p)
    t = strip(p.read_text(encoding="utf-8", errors="ignore"))
    def sub(m):
        name = m.group(1).strip()
        for base in (p.parent, *p.parents):
            for c in (base / name, base / (name + ".tex")):
                if c.is_file():
                    return resolve(c, seen)
            if base == REL / "preprints":
                break
        return ""
    return INC.sub(sub, t)


def body(t):
    m = re.search(r"\\begin\{document\}(.*?)(\\end\{document\}|$)", t, re.S)
    return m.group(1) if m else t


NEWTHM = re.compile(r"\\newtheorem\*?\{([^}]+)\}(?:\[[^\]]*\])?\{([^}]+)\}")
DECLTHM = re.compile(r"\\declaretheorem(?:\[([^\]]*)\])?\{([^}]+)\}")
CLAIMLIKE = re.compile(r"theorem|lemma|proposition|corollary|claim|fact|observation|step", re.I)


def statement_envs(full):
    envs = {}
    for env, lab in NEWTHM.findall(full):
        envs[env.strip()] = lab
    for opts, env in DECLTHM.findall(full):
        m = re.search(r"name\s*=\s*\{?([A-Za-z ]+)", opts or "")
        envs[env.strip()] = m.group(1) if m else env
    return {e for e, lab in envs.items() if CLAIMLIKE.search(lab) and not re.search(r"proof", e, re.I)}


def statements(t, envs):
    out = []
    for e in envs:
        out += re.findall(r"\\begin\{%s\}(.*?)\\end\{%s\}" % (re.escape(e), re.escape(e)), t, re.S)
    return out


def proofs(t):
    out, depth, start = [], 0, 0
    for m in ENV.finditer(t):
        if m.group(1) == "begin":
            if depth == 0:
                start = m.end()
            depth += 1
        elif depth:
            depth -= 1
            if depth == 0:
                out.append(t[start:m.start()])
    return out


data = json.loads(PL.read_text(encoding="utf-8"))
ms_csv = {r["pdf_path"]: r for r in csv.DictReader(open(ROOT / "data/catalog_manuscripts.csv", encoding="utf-8"))}
fam = defaultdict(lambda: {"proof_words": 0, "proof_pages": 0.0, "n_proofs": 0, "longest_proof_pages": 0.0, "statement_pages": 0.0, "n_statements": 0})
for m in data["manuscripts"]:
    c = ms_csv[m["pdf_path"]]
    main = REL / "preprints" / c["ms_dir"] / c["main_tex"].split(c["ms_dir"] + "/")[-1] if c["main_tex"] else None
    if main is None or not main.exists():
        main = REL / c["main_tex"] if c["main_tex"] else None
    full = resolve(main, set()) if main and main.exists() else ""
    doc = body(full)
    pf = proofs(doc)
    st = statements(doc, statement_envs(full))
    dw, pw = len(doc.split()), sum(len(x.split()) for x in pf)
    per_page = m["pages"] / dw if dw else 0
    m.update(doc_words=dw, proof_words=pw, n_proofs=len(pf), proof_pages=round(pw * per_page, 1),
             n_statements=len(st), statement_pages=round(sum(len(x.split()) for x in st) * per_page, 1),
             longest_proof_pages=round(max((len(x.split()) for x in pf), default=0) * per_page, 1), proof_share=round(pw / dw, 3) if dw else None)
    f = fam[m["fid"]]
    f["proof_words"] += pw; f["proof_pages"] += pw * per_page; f["n_proofs"] += len(pf)
    f["statement_pages"] += m["statement_pages"]; f["n_statements"] += len(st)
    f["longest_proof_pages"] = max(f["longest_proof_pages"], m["longest_proof_pages"])
for f in data["families"]:
    f.update({k: (round(v, 1) if isinstance(v, float) else v) for k, v in fam[f["fid"]].items()})
PL.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def summ(xs, unit):
    xs = sorted(xs)
    q, d = quantiles(xs, n=4), quantiles(xs, n=10)
    return f"median {median(xs):.1f} {unit}, IQR {q[0]:.1f}–{q[2]:.1f}, 10–90% {d[0]:.1f}–{d[-1]:.1f}, max {xs[-1]:.1f}"


ms = data["manuscripts"]
print("manuscripts with no proof environment:", sum(1 for m in ms if not m["n_proofs"]), "| no main tex resolved:", sum(1 for m in ms if not m["doc_words"]))
ok = [m for m in ms if m["n_proofs"]]
print("Manuscript proof pages:", summ([m["proof_pages"] for m in ok], "pp"))
print("Proof share of manuscript:", summ([m["proof_share"] for m in ok], ""))
print("Proofs per manuscript:", summ([m["n_proofs"] for m in ok], ""))
print("Longest single proof per manuscript:", summ([m["longest_proof_pages"] for m in ok], "pp"))
print("Family proof pages:", summ([f["proof_pages"] for f in data["families"] if f["n_proofs"]], "pp"))
st_ok = [m for m in ok if m["n_statements"]]
print("manuscripts with no theorem-like statements found:", len(ok) - len(st_ok))
print("Statement pages per manuscript:", summ([m["statement_pages"] for m in st_ok], "pp"))
print("Statements + proofs per manuscript:", summ([m["statement_pages"] + m["proof_pages"] for m in st_ok], "pp"))
print("Per result (statement + proofs) / statements, pooled:", round(sum(m["statement_pages"] + m["proof_pages"] for m in st_ok) / sum(m["n_statements"] for m in st_ok), 2), "pp over", sum(m["n_statements"] for m in st_ok), "statements")
print("Total proof pages:", round(sum(m["proof_pages"] for m in ms)), "of", sum(m["pages"] for m in ms))
