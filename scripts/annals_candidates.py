"""Sampling frame for a reproducible human baseline: arXiv papers whose journal reference is the Annals of
Mathematics, published 2016-2025. Uses arXiv's HTML advanced search on the journal-ref field (the arXiv API host is
not reachable from this environment). Writes data/annals_candidates.json."""
import html
import json
import re
import subprocess
import time
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parent.parent
TERMS = ["Annals of Mathematics", "Ann. of Math.", "Ann. Math.", "Ann. of Math", "Annals of Math."]
ANNALS = re.compile(r"\b(Annals\s+of\s+Math(ematics|\.)?|Ann\.?\s*(of\s+)?Math\.?)(?!\s*(Stat|Phys|Inform|Sci|Qu[eé]b|Blaise|Fac|Inst|Toulouse|Henri))", re.I)
NOT_ANNALS = re.compile(r"Qu[eé]|Physics|Philosoph|Sil|Chin|Artificial|Ann\\. Math\\. Blaise|Probab|Statist|Applied|Global Anal|Combinator|Pure and Applied|Henri|Toulouse|Blaise|Institute|Quebec|Québec|PDE|Functional Anal|K-[Tt]heory|Fenn|Sci\.|Polon|Univ|Acad|Finnic|Represent|Discrete|Rev\.|Logic", re.I)


MATH_LIKE = ("math.", "math-ph", "cs.CC", "cs.DS", "cs.DM", "cs.IT", "quant-ph")


def page(term, start, field="journal_ref"):
    url = ("https://arxiv.org/search/advanced?advanced=1&terms-0-operator=AND&terms-0-term=" + quote_plus(term) +
           "&terms-0-field=" + field + "&classification-physics_archives=all&classification-include_cross_list=include"
           "&date-filter_by=all_dates&abstracts=hide&size=200&order=-announced_date_first&start=" + str(start))
    r = subprocess.run(["curl", "-sSL", "--retry", "3", "-A", "Mozilla/5.0 (research script)", url], capture_output=True, text=True)
    return r.stdout


def parse(t):
    out = []
    for x in t.split('<li class="arxiv-result">')[1:]:
        aid = re.search(r'arxiv\.org/abs/([^"]+)"', x).group(1)
        prim = re.search(r'tag is-small is-link[^>]*>([^<]+)<', x)
        title = re.search(r'<p class="title is-5 mathjax">\s*(.*?)\s*</p>', x, re.S)
        jr = re.search(r'Journal ref:</span>\s*(.*?)</p>', x, re.S)
        cm = re.search(r'Comments:</span>\s*(.*?)</', x, re.S)
        clean = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()
        out.append({"arxiv": aid, "primary": prim.group(1).strip() if prim else None,
                    "title": " ".join(clean(title.group(1) if title else "").split()),
                    "journal_ref": " ".join(clean(jr.group(1) if jr else "").split()),
                    "comments": " ".join(clean(cm.group(1) if cm else "").split())})
    return out


def main():
    seen = {}
    for term, field in [(t, "journal_ref") for t in TERMS] + [("Annals of Mathematics", "comments"), ("Ann. of Math", "comments")]:
        start = 0
        while True:
            t = page(term, start, field)
            rows = parse(t)
            m = re.search(r"Showing [\d,]+&ndash;[\d,]+ of ([\d,]+) results", t)
            total = int(m.group(1).replace(",", "")) if m else 0
            for r in rows:
                seen.setdefault(r["arxiv"], r)
            start += 200
            time.sleep(3)
            if not rows or start >= total or start >= 10000:
                break
        print(term, field, total, len(seen))
    keep = []
    for r in seen.values():
        src = r["journal_ref"] if ANNALS.search(r["journal_ref"] or "") else r["comments"]
        y = re.search(r"\((20\d\d)\)|\b(20\d\d)\b", src or "")
        year = int(y.group(1) or y.group(2)) if y else None
        if not ANNALS.search(src or "") or NOT_ANNALS.search(src) or not (r["primary"] or "").startswith(MATH_LIKE):
            continue
        if src is r["comments"] and not re.search(r"(to appear|accepted|published)\s+(in\s+)?(the\s+)?Ann", src, re.I):
            continue
        if year is None and src is r["comments"]:
            year = 2000 + int(r["arxiv"][:2]) if r["arxiv"][:2].isdigit() else None
        vol = re.search(r"(?:\(2\)\s*|Vol\.?\s*|\bv\.?\s*)?\b(1[89]\d|20[0-2])\b(?!\d)", re.sub(r"\b20\d\d\b", "", src))
        if not vol or not 183 <= int(vol.group(1)) <= 202:  # Annals volumes 183 (2016) to 202 (2025)
            continue
        if year and 2016 <= year <= 2025:
            keep.append({**r, "year": year, "source": "journal_ref" if src is r["journal_ref"] else "comments"})
    keep.sort(key=lambda r: r["arxiv"])
    (ROOT / "data/annals_candidates.json").write_text(json.dumps(keep, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("kept", len(keep))


if __name__ == "__main__":
    main()
