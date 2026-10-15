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
from concurrent.futures import ThreadPoolExecutor
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
    # Number theory
    ("1312.7748", "Helfgott: ternary Goldbach problem"),
    ("1006.1002", "Bhargava–Shankar: average rank via binary quartic forms"),
    ("2009.07180", "Newton–Thorne: symmetric power functoriality II"),
    ("1812.09999", "Allen et al.: potential automorphy over CM fields"),
    ("1909.03562", "Tao: almost all Collatz orbits"),
    ("1501.04585", "Matomäki–Radziwiłł: multiplicative functions in short intervals"),
    ("2007.03528", "Bloom–Sisask: logarithmic bounds for Roth"),
    ("1604.01041", "Maynard: primes with restricted digits"),
    ("2405.20552", "Guth–Maynard: large value estimates for Dirichlet polynomials"),
    # Combinatorics
    ("1611.06827", "Glock–Kühn–Lo–Osthus: designs via iterative absorption"),
    ("1910.13433", "Frankston–Kahn–Narayanan–Park: thresholds"),
    ("1908.08483", "Alweiss–Lovett–Wu–Zhang: sunflowers"),
    ("2211.09055", "Gilmer: union-closed sets"),
    ("2001.02665", "Montgomery–Pokrovskiy–Sudakov: Ringel's conjecture"),
    ("2201.04554", "Kwan–Sah–Sawhney–Simkin: high-girth Steiner triple systems"),
    ("2306.04007", "Mattheus–Verstraete: r(4,t)"),
    ("1605.09223", "Ellenberg–Gijswijt: cap sets"),
    ("2402.17995", "Leng–Sah–Sawhney: Szemerédi bounds"),
    # Analysis and PDE
    ("1403.5335", "Bourgain–Demeter: l2 decoupling"),
    ("1709.10033", "Buckmaster–Vicol: Navier–Stokes nonuniqueness"),
    ("1608.08301", "Isett: Onsager's conjecture"),
    ("1402.0290", "Tao: averaged Navier–Stokes blowup"),
    ("2210.07191", "Chen–Hou: Euler blowup, computer-assisted"),
    ("1904.04795", "Elgindi: finite-time singularity for Euler"),
    ("2503.01800", "Deng–Hani–Ma: Hilbert's sixth problem"),
    # Probability and mathematical physics
    ("1507.00719", "Miller–Sheffield: Liouville quantum gravity and the Brownian map I"),
    ("0708.0039", "Smirnov: conformal invariance in random cluster models I"),
    ("1912.07973", "Aizenman–Duminil-Copin: marginal triviality"),
    # Geometry and topology
    ("math/0303109", "Perelman: Ricci flow with surgery"),
    ("math/0307245", "Perelman: finite extinction time"),
    ("1303.2354", "Manolescu: triangulation conjecture"),
    ("1808.02923", "Piccirillo: Conway knot is not slice"),
    ("0705.0766", "Brendle–Schoen: differentiable sphere theorem"),
    ("1202.6036", "Marques–Neves: Willmore conjecture"),
    ("1806.08816", "Song: Yau's conjecture on minimal surfaces"),
    ("1101.1330", "Kahn–Markovic: Ehrenpreis conjecture"),
    ("1302.3320", "Eskin–Mirzakhani: invariant measures for SL(2,R)"),
    # Algebraic geometry, representation theory
    ("1609.05543", "Birkar: singularities of linear systems, BAB"),
    ("math/0610203", "Birkar–Cascini–Hacon–McKernan: existence of minimal models"),
    ("1212.0791", "Elias–Williamson: Hodge theory of Soergel bimodules"),
    ("1905.08229", "Bhatt–Scholze: prisms and prismatic cohomology"),
    ("2102.13459", "Fargues–Scholze: geometrization of local Langlands"),
    ("2405.03599", "Gaitsgory et al.: geometric Langlands I"),
    ("1511.02888", "Adiprasito–Huh–Katz: Hodge theory for combinatorial geometries"),
    ("1902.03719", "Brändén–Huh: Lorentzian polynomials"),
    # Logic and theoretical computer science
    ("2001.04383", "Ji–Natarajan–Vidick–Wright–Yuen: MIP* = RE"),
    ("1512.03547", "Babai: graph isomorphism in quasipolynomial time"),
    ("2203.00671", "Chen–Kyng–Liu–Peng–Probst Gutenberg–Sachdeva: almost-linear max flow"),
    ("1704.01914", "Zhuk: CSP dichotomy"),
    ("1703.03021", "Bulatov: CSP dichotomy"),
]


def get(url):
    r = subprocess.run(["curl", "-sSfL", "--retry", "3", "-A", "Mozilla/5.0 (research script)", url], capture_output=True)
    if r.returncode:
        raise RuntimeError(f"{url}: {r.stderr.decode()[:200]}")
    return r.stdout


def one(arg):
    (aid, short), scratch = arg
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
    return rec


def main():
    scratch = Path(tempfile.mkdtemp(prefix="frontier_"))
    with ThreadPoolExecutor(6) as ex:
        out = list(ex.map(one, [(p, scratch) for p in PAPERS]))
    for rec in out:
        print(rec["arxiv"], rec.get("pages"), rec.get("technical_pages"), rec.get("longest_proof_pages"), "|", rec["name"][:40], "|", (rec.get("title") or rec.get("error", ""))[:70])
    (ROOT / "data/frontier_lengths.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
