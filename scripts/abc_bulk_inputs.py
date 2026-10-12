"""Build one small text bundle per family for cheap A/B/C labelling: title, OpenAI summary, each
manuscript's abstract and its first theorem-like statements (\\input/\\include resolved).
Writes data/abc_bulk/inputs/<fid>.txt."""
import csv, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/openai-math"
OUT = ROOT / "data/abc_bulk/inputs"; OUT.mkdir(parents=True, exist_ok=True)
fams = {r["family_id"]: r for r in csv.DictReader(open(ROOT / "data/catalog_families.csv", encoding="utf-8"))}
mss = list(csv.DictReader(open(ROOT / "data/catalog_manuscripts.csv", encoding="utf-8")))
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
THM_RE = re.compile(r"\\begin\{(theorem|maintheorem|mainthm|thm|theoremA|thmx|conjecture|proposition)\*?\}(.*?)\\end\{\1\*?\}", re.S)

def expand(path, depth=0):
    try:
        t = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    if depth > 4:
        return t
    def sub(m):
        name = m.group(1)
        p = (path.parent / name)
        if not p.suffix:
            p = p.with_suffix(".tex")
        return expand(p, depth + 1) if p.exists() else ""
    return INPUT_RE.sub(sub, t)

def clean(s, n):
    s = re.sub(r"%.*", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:n]

for fid, f in sorted(fams.items()):
    parts = [f"FAMILY {fid}: {f['title']}", f"SUBJECT: {f['subject']}", f"SUMMARY: {f['summary']}",
             f"LEAN: {'yes' if f['lean_dirs'] else 'no'}"]
    for m in [m for m in mss if m["family_id"] == fid]:
        parts.append(f"\n--- MANUSCRIPT: {m['ms_title']} ({m['date']})\nABSTRACT: {clean(m['abstract'], 1500)}")
        tex = expand(RAW / m["main_tex"]) if m["main_tex"] else ""
        thms = THM_RE.findall(tex)[:3]
        for kind, body in thms:
            parts.append(f"[{kind}] {clean(body, 900)}")
    (OUT / f"{fid}.txt").write_text("\n".join(parts) + "\n", encoding="utf-8")
print(len(fams), "bundles")
