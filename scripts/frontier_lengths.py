"""Baseline for the release's proof lengths: the same measures (scripts/proof_text_lengths.py) applied to well-known
human frontier papers on arXiv. For each paper: the title from its abstract page (to confirm the id), the PDF page
count, and the LaTeX source (e-print), unpacked into its own scratch directory and only read as text.
Writes data/frontier_lengths.json."""
import gzip
import io
import json
import re
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from proof_text_lengths import measure  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PAPERS = [  # (arXiv id, short name)
    ("1311.4600", "Maynard: small gaps between primes"),
    ("1603.04246", "Viazovska: sphere packing in dimension 8"),
    ("1603.06518", "Cohn–Kumar–Miller–Radchenko–Viazovska: dimension 24"),
    ("1907.00847", "Huang: sensitivity conjecture"),
    ("2302.05537", "Kelley–Meka: 3-term progressions"),
    ("2303.09521", "Campos–Griffiths–Morris–Sahasrabudhe: diagonal Ramsey"),
    ("2311.05762", "Gowers–Green–Manners–Tao: Marton's conjecture"),
    ("2203.17207", "Park–Pham: Kahn–Kalai conjecture"),
    ("1509.05363", "Tao: Erdős discrepancy problem"),
    ("1512.01565", "Bourgain–Demeter–Guth: Vinogradov mean value"),
    ("math/0404188", "Green–Tao: primes in arithmetic progressions"),
    ("math/0211159", "Perelman: entropy formula for Ricci flow"),
    ("1303.5113", "Hairer: theory of regularity structures"),
    ("1111.4914", "Scholze: perfectoid spaces"),
    ("1401.3665", "Keevash: existence of designs"),
    ("0910.5501", "Kahn–Markovic: surface subgroups"),
    ("1204.2810", "Agol: virtual Haken conjecture"),
    ("1007.0575", "Duminil-Copin–Smirnov: connective constant"),
    ("1011.4105", "Guth–Katz: Erdős distinct distances"),
    ("2502.17655", "Wang–Zahl: Kakeya conjecture in R^3"),
    ("2410.02545", "Gladkov–Pak–Zimin: bunkbed conjecture is false"),
]


def get(url):
    r = subprocess.run(["curl", "-sSfL", "--retry", "3", "-A", "Mozilla/5.0 (research script)", url], capture_output=True)
    if r.returncode:
        raise RuntimeError(f"{url}: {r.stderr.decode()[:200]}")
    return r.stdout


def main():
    out = []
    scratch = Path(tempfile.mkdtemp(prefix="frontier_"))
    for aid, short in PAPERS:
        rec = {"arxiv": aid, "name": short}
        try:
            html = get(f"https://arxiv.org/abs/{aid}").decode("utf-8", "ignore")
            m = re.search(r'<meta name="citation_title" content="([^"]+)"', html)
            rec["title"] = m.group(1) if m else None
            pdf = scratch / (aid.replace("/", "_") + ".pdf")
            pdf.write_bytes(get(f"https://arxiv.org/pdf/{aid}"))
            pm = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout)
            rec["pages"] = int(pm.group(1)) if pm else None
            pdf.unlink()
            src = get(f"https://arxiv.org/e-print/{aid}")
            d = scratch / aid.replace("/", "_")
            d.mkdir()
            try:
                with tarfile.open(fileobj=io.BytesIO(src)) as tf:
                    tf.extractall(d, filter="data")
            except tarfile.TarError:
                raw = gzip.decompress(src) if src[:2] == b"\x1f\x8b" else src
                (d / "main.tex").write_bytes(raw)
            mains = [p for p in d.rglob("*.tex") if re.search(r"\\begin\{document\}", p.read_text(errors="ignore"))]
            main_tex = max(mains, key=lambda p: p.stat().st_size) if mains else None
            rec.update(measure(main_tex, rec["pages"], stop=d))
        except Exception as e:  # keep going; record the failure
            rec["error"] = str(e)[:300]
        out.append(rec)
        print(aid, rec.get("pages"), rec.get("proof_pages"), rec.get("technical_pages"), rec.get("longest_proof_pages"), "|", (rec.get("title") or rec.get("error", ""))[:70])
    (ROOT / "data/frontier_lengths.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
