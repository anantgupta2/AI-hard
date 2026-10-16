"""Reproducible human baseline: every Annals of Mathematics paper (volumes 183-202, 2016-2025) whose arXiv entry
carries the journal reference (data/annals_candidates.json, from scripts/annals_candidates.py), measured with the same
length measures as the release (scripts/proof_text_lengths.py via scripts/frontier_lengths.py). Subjects come from the
arXiv primary category, mapped to the release's subject names. Writes data/annals_lengths.json."""
import json
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from frontier_lengths import one  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CAT = {"math.NT": "Number theory", "math.AG": "Algebraic and complex geometry", "math.DS": "Dynamical systems and ergodic theory",
       "math.DG": "Differential geometry", "math.CO": "Combinatorics", "math.LO": "Mathematical logic",
       "math.AP": "Partial differential equations", "math-ph": "Mathematical physics", "math.MP": "Mathematical physics",
       "math.GR": "Group theory", "math.RT": "Algebra", "math.RA": "Algebra", "math.AC": "Algebra", "math.QA": "Algebra",
       "math.KT": "Algebra", "math.OA": "Operator algebras", "math.PR": "Probability and statistical mechanics",
       "math.ST": "Probability and statistical mechanics", "math.CA": "Real and complex analysis",
       "math.CV": "Real and complex analysis", "math.FA": "Functional analysis", "math.MG": "Convex and metric geometry",
       "math.GT": "Topology", "math.AT": "Topology", "math.GN": "Topology", "math.SG": "Differential geometry"}


def main():
    cands = json.loads((ROOT / "data/annals_candidates.json").read_text(encoding="utf-8"))
    scratch = Path(tempfile.mkdtemp(prefix="annals_"))
    with ThreadPoolExecutor(6) as ex:
        recs = list(ex.map(one, [((c["arxiv"], c["title"]), scratch) for c in cands]))
    out = []
    for c, r in zip(cands, recs):
        r.update(year=c["year"], primary=c["primary"], journal_ref=c["journal_ref"],
                 subject=CAT.get(c["primary"], "Theoretical computer science" if c["primary"].startswith("cs.") else None))
        out.append(r)
        print(c["arxiv"], r.get("pages"), r.get("technical_pages"), r["subject"], "|", (r.get("error") or "")[:60])
    (ROOT / "data/annals_lengths.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
