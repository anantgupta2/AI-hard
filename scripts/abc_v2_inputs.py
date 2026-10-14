"""Rich per-family inputs for the v2 A/B labelling (data/abc_v2/BUCKETS_PLAN.md): for each manuscript the
abstract, the introduction (<= 4,000 chars), up to 10 theorem-like statements (introduction first), and for
each Lean comparator the challenge file (definitions + statement, <= 4,000 chars).
Writes data/abc_v2/inputs/<fid>.txt."""
import csv, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/openai-math"
OUT = ROOT / "data/abc_v2/inputs"; OUT.mkdir(parents=True, exist_ok=True)
fams = {r["family_id"]: r for r in csv.DictReader(open(ROOT / "data/catalog_families.csv", encoding="utf-8"))}
mss = list(csv.DictReader(open(ROOT / "data/catalog_manuscripts.csv", encoding="utf-8")))
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
ENV = r"theorem|maintheorem|mainthm|thm|theoremA|thmx|theoremx|conjecture|conj|proposition|prop|corollary|cor|question|problem"
THM_RE = re.compile(rf"\\begin\{{({ENV})\*?\}}(.*?)\\end\{{\1\*?\}}", re.S)
SEC_RE = re.compile(r"\\section\*?\{([^}]*)\}")

def expand(path, depth=0):
    try:
        t = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    if depth > 4:
        return t
    def sub(m):
        p = path.parent / m.group(1)
        if not p.suffix:
            p = p.with_suffix(".tex")
        return expand(p, depth + 1) if p.exists() else ""
    return INPUT_RE.sub(sub, t)

def clean(s, n):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n] + " […]"

def intro_of(tex):
    secs = list(SEC_RE.finditer(tex))
    for i, m in enumerate(secs):
        if "intro" in m.group(1).lower() or i == 0:
            end = secs[i + 1].start() if i + 1 < len(secs) else len(tex)
            return tex[m.end():end]
    b = tex.find("\\begin{document}")
    return tex[b:b + 8000] if b >= 0 else tex[:8000]

n_lean = 0
for fid, f in sorted(fams.items()):
    parts = [f"FAMILY {fid}: {f['title']}", f"SUBJECT: {f['subject']}", f"OPENAI SUMMARY: {f['summary']}"]
    for m in [m for m in mss if m["family_id"] == fid]:
        tex = expand(RAW / m["main_tex"]) if m["main_tex"] else ""
        intro = intro_of(tex)
        thms = THM_RE.findall(intro) or THM_RE.findall(tex)
        parts.append(f"\n=== MANUSCRIPT: {m['ms_title']} ({m['date']}) [{m['main_tex']}]\nABSTRACT: {clean(m['abstract'], 2000)}")
        parts.append("INTRODUCTION (start): " + clean(THM_RE.sub(" [statement] ", intro), 4000))
        for kind, body in thms[:10]:
            parts.append(f"[{kind}] {clean(body, 1200)}")
    for c in [c for c in f["comparators"].split(";") if c.strip()]:
        p = RAW / "lean/ComparatorChallenges" / f"{c.strip()}.lean"
        if p.exists():
            n_lean += 1
            t = p.read_text(encoding="utf-8", errors="replace")
            t = re.sub(r"/-[\s\S]*?-/", "", t)
            t = re.sub(r"\n\s*\n+", "\n", t)
            parts.append(f"\n=== LEAN COMPARATOR {c.strip()} (exact formal statement)\n" + (t if len(t) <= 8000 else t[:8000] + "\n[…]"))
    (OUT / f"{fid}.txt").write_text("\n".join(parts) + "\n", encoding="utf-8")
print(len(fams), "families,", n_lean, "comparator files included")
