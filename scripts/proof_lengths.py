"""Proof length per manuscript and family: PDF page count (fetched one at a time from raw.githubusercontent.com at
the pinned commit, never stored; the sparse checkout skips PDFs), .tex word count, and Lean lines in the family's
formalization directories. Writes data/proof_lengths.json and prints a summary."""
import csv
import json
import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from statistics import median, quantiles

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
REL = ROOT / "data/raw/openai-math"
RAW = "https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/"
OUT = ROOT / "data/proof_lengths.json"
cache = json.loads(OUT.read_text()) if OUT.exists() else {}
pages_cache = {m["pdf_path"]: m["pages"] for m in cache.get("manuscripts", []) if m.get("pages")}


def pages(pdf):
    if pdf in pages_cache:
        return pages_cache[pdf]
    with tempfile.NamedTemporaryFile(suffix=".pdf") as t:
        r = subprocess.run(["curl", "-sSf", "--retry", "3", "-o", t.name, RAW + pdf], capture_output=True)
        if r.returncode:
            return None
        m = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", t.name], capture_output=True, text=True).stdout)
        return int(m.group(1)) if m else None


def tex_words(ms_dir):
    d = REL / "preprints" / ms_dir
    n = 0
    for p in d.rglob("*.tex"):
        txt = re.sub(r"(?<!\\)%.*", "", p.read_text(encoding="utf-8", errors="ignore"))
        n += len(txt.split())
    return n


def lean_lines(dirs):
    n = 0
    for d in [x for x in dirs.split(";") if x]:
        for p in (REL / "lean" / d).rglob("*.lean"):
            n += sum(1 for line in p.open(encoding="utf-8", errors="ignore") if line.strip() and not line.strip().startswith("--"))
    return n


ms = list(csv.DictReader(open(ROOT / "data/catalog_manuscripts.csv", encoding="utf-8")))
with ThreadPoolExecutor(8) as ex:
    pg = list(ex.map(lambda m: pages(m["pdf_path"]), ms))
rows = [{"fid": m["family_id"], "title": m["ms_title"], "pdf_path": m["pdf_path"], "pages": p,
         "tex_words": tex_words(m["ms_dir"]), "withdrawn": m["withdrawn"] == "True"} for m, p in zip(ms, pg)]
fam = defaultdict(lambda: {"pages": 0, "tex_words": 0, "n_ms": 0})
for r in rows:
    if r["withdrawn"]:
        continue
    f = fam[r["fid"]]
    f["pages"] += r["pages"] or 0
    f["tex_words"] += r["tex_words"]
    f["n_ms"] += 1
cat = {r["family_id"]: r for r in csv.DictReader(open(ROOT / "data/catalog_families.csv", encoding="utf-8"))}
fams = []
for fid in sorted(cat):
    f = fam.get(fid, {"pages": 0, "tex_words": 0, "n_ms": 0})
    fams.append({"fid": fid, **f, "lean_lines": lean_lines(cat[fid]["lean_dirs"])})
OUT.write_text(json.dumps({"manuscripts": rows, "families": fams}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def summ(xs, unit):
    xs = sorted(x for x in xs if x)
    q = quantiles(xs, n=10)
    return (f"n={len(xs)}, median {median(xs):.0f} {unit}, IQR {quantiles(xs, n=4)[0]:.0f}–{quantiles(xs, n=4)[2]:.0f}, "
            f"10th–90th pct {q[0]:.0f}–{q[-1]:.0f}, min {xs[0]}, max {xs[-1]}, total {sum(xs)}")


print("missing pages:", sum(1 for r in rows if r["pages"] is None))
print("Manuscript pages:", summ([r["pages"] for r in rows if not r["withdrawn"]], "pp"))
print("Family pages:", summ([f["pages"] for f in fams], "pp"))
print("Family Lean lines (formalized):", summ([f["lean_lines"] for f in fams], "lines"))
