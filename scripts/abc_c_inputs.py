"""Per-family inputs for the two-axis proof-type labelling (data/abc_c/C_PLAN.md): the family's OpenAI summary and
v2 headline sentence, then for each manuscript (up to 4) the abstract, the main theorem statements, the paper's own
proof-strategy paragraphs (introduction paragraphs or subsections that talk about the proof), the section outline,
and the opening of its longest proofs. Writes data/abc_c/inputs/<fid>.txt."""
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from proof_text_lengths import body, proofs, resolve  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/openai-math"
OUT = ROOT / "data/abc_c/inputs"
fams = {r["family_id"]: r for r in csv.DictReader(open(ROOT / "data/catalog_families.csv", encoding="utf-8"))}
mss = list(csv.DictReader(open(ROOT / "data/catalog_manuscripts.csv", encoding="utf-8")))
v2 = {r["fid"]: r for r in json.loads((ROOT / "data/abc_v2/labels_v2.json").read_text(encoding="utf-8"))}
ENV = r"theorem|maintheorem|mainthm|thm|theoremA|thmx|theoremx|proposition|prop|corollary|cor"
THM_RE = re.compile(rf"\\begin\{{({ENV})\*?\}}(.*?)\\end\{{\1\*?\}}", re.S)
SEC_RE = re.compile(r"\\(section|subsection)\*?\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
STRAT = re.compile(r"strateg|outline|overview|idea of|sketch|approach|the proof (?:of|proceeds|is)|we prove|our (?:argument|method|proof)|"
                   r"key (?:step|idea|lemma|ingredient)|main (?:idea|difficulty|step)|by (?:induction|contradiction)|we construct|organi[sz]ation", re.I)


def clean(s, n):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n] + " […]"


def strategy(doc, cap=3500):
    """Paragraphs from the first quarter of the paper (or the introduction) that discuss the proof."""
    head = doc[: max(len(doc) // 4, 15000)]
    paras = [p for p in re.split(r"\n\s*\n", head) if STRAT.search(p) and not THM_RE.search(p)]
    out, n = [], 0
    for p in paras:
        c = clean(p, 1200)
        if n + len(c) > cap:
            break
        out.append(c)
        n += len(c)
    return out


def main():
    for fid, f in sorted(fams.items()):
        parts = [f"FAMILY {fid}: {f['title']}", f"SUBJECT: {f['subject']}", f"OPENAI SUMMARY: {f['summary']}",
                 f"HEADLINE (v2, semi-formal): {v2[fid]['claim_formal']}"]
        for m in [m for m in mss if m["family_id"] == fid][:4]:
            main_tex = RAW / m["main_tex"] if m["main_tex"] else None
            full = resolve(main_tex, set(), RAW / "preprints") if main_tex and main_tex.exists() else ""
            doc = body(full)
            parts.append(f"\n=== MANUSCRIPT: {m['ms_title']} [{m['main_tex']}]\nABSTRACT: {clean(m['abstract'], 1500)}")
            for kind, b in THM_RE.findall(doc)[:3]:
                parts.append(f"[{kind}] {clean(b, 800)}")
            st = strategy(doc)
            if st:
                parts.append("PROOF STRATEGY (paper's own words):\n- " + "\n- ".join(st))
            secs = [f"{'  ' if k == 'subsection' else ''}{clean(t, 90)}" for k, t in SEC_RE.findall(doc)][:40]
            if secs:
                parts.append("SECTION OUTLINE:\n" + "\n".join(secs))
            pf = sorted(proofs(doc), key=len, reverse=True)[:3]
            for i, p in enumerate(pf, 1):
                parts.append(f"LONGEST PROOF #{i} (opening): {clean(p, 900)}")
        txt = "\n".join(parts)
        (OUT / f"{fid}.txt").write_text((txt if len(txt) <= 18000 else txt[:18000] + "\n[…]") + "\n", encoding="utf-8")
    print(len(fams), "families")


if __name__ == "__main__":
    main()
