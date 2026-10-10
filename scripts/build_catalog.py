"""Build family- and manuscript-level catalogues of the openai/math release.

Joins CONTENTS.md (families, manuscripts), overview.tex (subjects),
lean/formalization.yaml + lean/docs/NNN.md (Lean coverage), history.md
(withdrawals) and the preprint directories (LaTeX source location).

Usage: python scripts/build_catalog.py [--repo data/raw/openai-math] [--out data]
"""

import argparse
import json
import re
import sys
from pathlib import Path

import pandas as pd
import yaml

sys.stdout.reconfigure(encoding="utf-8")

BS = "\\"


def parse_overview(text):
    """Map family id -> (subject, short title) from overview.tex."""
    out = {}
    for block in text.split(BS + "cataloguesection{")[1:]:
        subject = block[: block.find("}")]
        for entry in block.split(BS + "resultentry{")[1:]:
            fid = entry[:3]
            rest = entry[entry.find("}") + 2 :]
            out[fid] = (subject, rest[: rest.find("}")])
    return out


def strip_html(s):
    return re.sub(r"<[^>]+>", "", s).replace("&emsp;", "").strip()


def parse_contents(text):
    """Return families {id: {...}} and manuscripts [{...}] from CONTENTS.md."""
    families, manuscripts = {}, []
    cur, pending_ms = None, None
    fam_re = re.compile(r"^\*\*(\d{3})\. (.+?)\*\*\s*(.*)$")
    ms_re = re.compile(r"\[(.+?)\]\((preprints/([^/]+)/[^)]+)\)")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("<"):
            continue
        m = fam_re.match(line)
        if m:
            cur = m.group(1)
            summary = m.group(3)
            families[cur] = {
                "family_id": cur,
                "title": strip_html(m.group(2)).rstrip("."),
                "summary": strip_html(re.sub(r"\(\[Lean\]\([^)]*\)\)", "", summary)),
                "has_lean_doc": "[Lean](lean/docs/" in summary,
            }
            pending_ms = None
            continue
        m = ms_re.search(line)
        if m and line.startswith("&emsp;") and cur:
            pending_ms = {
                "family_id": cur,
                "ms_title": strip_html(m.group(1)),
                "pdf_path": m.group(2),
                "ms_dir": m.group(3),
                "abstract": "",
            }
            manuscripts.append(pending_ms)
            continue
        if pending_ms and not pending_ms["abstract"]:
            pending_ms["abstract"] = strip_html(line)
    return families, manuscripts


def parse_withdrawn(history):
    """Titles listed under **Withdrawals** in history.md."""
    titles, on = set(), False
    for line in history.splitlines():
        if line.startswith("**Withdrawals**"):
            on = True
        elif line.startswith("**"):
            on = False
        elif on and line.startswith("- "):
            titles.add(line[2:].strip())
    return titles


def parse_lean_doc(text):
    """Comparator stems and paper dirs referenced by lean/docs/NNN.md."""
    comps = re.findall(r"ComparatorChallenges/([A-Za-z0-9_]+)\.lean", text)
    papers = re.findall(r"preprints/([^/]+)/", text)
    return comps, papers


def find_main_tex(ms_path):
    """Top-level .tex (contains \\documentclass) under the manuscript dir."""
    hits = []
    for p in ms_path.rglob("*.tex"):
        try:
            head = p.read_text(encoding="utf-8", errors="replace")[:20000]
        except OSError:
            continue
        if BS + "documentclass" in head or BS + "begin{document}" in head:
            hits.append((p, BS + "begin{document}" in head))
    # A preamble file can carry \documentclass without the document body; prefer the file with \begin{document}.
    hits.sort(key=lambda h: (not h[1], len(h[0].parts), h[0].name != "main.tex"))
    hits = [h[0] for h in hits]
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="data/raw/openai-math")
    ap.add_argument("--out", default="data")
    args = ap.parse_args()
    repo, out = Path(args.repo), Path(args.out)

    overview = parse_overview((repo / "overview.tex").read_text(encoding="utf-8"))
    families, manuscripts = parse_contents((repo / "CONTENTS.md").read_text(encoding="utf-8"))
    withdrawn = parse_withdrawn((repo / "history.md").read_text(encoding="utf-8"))
    fz = yaml.safe_load((repo / "lean" / "formalization.yaml").read_text(encoding="utf-8"))

    # comparator stem -> main_results entries
    by_comp = {}
    for e in fz["status"]["main_results"]:
        stem = Path(e["comparator_config"]).stem
        by_comp.setdefault(stem, []).append(e)
    formalized_dirs = {Path(s["id"]).parent.name for s in fz["sources"]}

    traces = {}
    for line in (repo / "README.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d{3})\s*\|\s*\[(.+?)\]\((reasoning_traces/[^)]+)\)", line)
        if m:
            traces[m.group(1)] = m.group(3)

    # Lean coverage per family
    for fid, fam in families.items():
        subj, short = overview.get(fid, (None, None))
        fam["subject"] = subj
        fam["short_title"] = short
        fam["reasoning_trace"] = traces.get(fid, "")
        comps, decls, files = [], [], []
        doc = repo / "lean" / "docs" / f"{fid}.md"
        if doc.exists():
            comps, _ = parse_lean_doc(doc.read_text(encoding="utf-8"))
            for c in comps:
                # Comparator JSON is authoritative; formalization.yaml covers only ~200 of them.
                cj = repo / "lean" / "ComparatorChallenges" / f"{c}.json"
                if cj.exists():
                    spec = json.loads(cj.read_text(encoding="utf-8"))
                    mod_file = spec["solution_module"].replace(".", "/") + ".lean"
                    for t in spec.get("theorem_names", []):
                        decls.append(t)
                        files.append(mod_file)
                else:
                    for e in by_comp.get(c, []):
                        decls.append(e["declaration"])
                        files.append(e["file"])
        # Solution modules may sit at OAI/<Field>/<Topic>.lean (no topic dir); keep the dir level only.
        lean_dirs = sorted({"/".join(Path(f).parts[:3]) for f in files if len(Path(f).parts) > 3}
                           | {"/".join(Path(f).parts[:2]) + "/" + Path(f).stem for f in files if len(Path(f).parts) == 3})
        fam["comparators"] = ";".join(comps)
        fam["lean_declarations"] = ";".join(decls)
        fam["lean_dirs"] = ";".join(lean_dirs)
        fam["lean_fields"] = ";".join(sorted({d.split("/")[1] for d in lean_dirs}))

    # Transitive closure of OAI directories imported by each family's Lean (comparator dirs miss these).
    lean_root = repo / "lean"
    dir_imports = {}

    def imports_of(d):
        if d not in dir_imports:
            found = set()
            base = lean_root / d
            paths = list(base.rglob("*.lean")) if base.is_dir() else []
            if base.with_suffix(".lean").exists():
                paths.append(base.with_suffix(".lean"))
            for p in paths:
                for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
                    if line.startswith("import OAI."):
                        parts = line.split()[1].split(".")
                        if len(parts) >= 3:
                            found.add("/".join(parts[:3]))
            dir_imports[d] = found - {d}
        return dir_imports[d]

    for fam in families.values():
        own = [d for d in fam["lean_dirs"].split(";") if d]
        seen, stack = set(own), list(own)
        while stack:
            for nxt in imports_of(stack.pop()):
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        fam["lean_dirs_imported"] = ";".join(sorted(seen - set(own)))

    # Manuscript-level details
    for ms in manuscripts:
        d = repo / "preprints" / ms["ms_dir"]
        ms["dir_exists"] = d.exists()
        mains = find_main_tex(d) if d.exists() else []
        ms["main_tex"] = mains[0].relative_to(repo).as_posix() if mains else ""
        ms["n_main_tex_candidates"] = len(mains)
        ms["n_tex_files"] = len(list(d.rglob("*.tex"))) if d.exists() else 0
        bibs = list(d.rglob("*.bib")) if d.exists() else []
        ms["bib"] = ";".join(b.relative_to(repo).as_posix() for b in bibs)
        ms["in_formalization_yaml"] = ms["ms_dir"] in formalized_dirs
        readme = d / "README.md"
        readme_txt = readme.read_text(encoding="utf-8", errors="replace").lower() if readme.exists() else ""
        ms["withdrawn"] = ms["ms_title"] in withdrawn or "withdrawn" in readme_txt
        ms["revised"] = "version" in readme_txt and "previous" in readme_txt
        m = re.search(r"-([A-Z][a-z]+-\d{1,2}-\d{4})$", ms["ms_dir"])
        ms["date"] = m.group(1) if m else ""

    fam_df = pd.DataFrame(families.values())
    ms_df = pd.DataFrame(manuscripts)
    counts = ms_df.groupby("family_id").size()
    fam_df["n_manuscripts"] = fam_df["family_id"].map(counts).fillna(0).astype(int)
    fam_df["any_ms_formalized"] = fam_df["family_id"].map(
        ms_df.groupby("family_id")["in_formalization_yaml"].any()
    )

    out.mkdir(parents=True, exist_ok=True)
    fam_df.to_csv(out / "catalog_families.csv", index=False)
    ms_df.to_csv(out / "catalog_manuscripts.csv", index=False)

    # Reconciliation report
    all_dirs = {p.name for p in (repo / "preprints").iterdir() if p.is_dir()}
    listed = set(ms_df["ms_dir"])
    print(f"families: {len(fam_df)}  (ids {fam_df.family_id.min()}..{fam_df.family_id.max()})")
    print(f"manuscripts in CONTENTS: {len(ms_df)}  unique dirs: {len(listed)}")
    print(f"preprint dirs on disk: {len(all_dirs)}  not in CONTENTS: {len(all_dirs - listed)}")
    print(f"listed but missing on disk: {len(listed - all_dirs)}")
    print(f"withdrawn titles in history.md: {len(withdrawn)}  matched in CONTENTS: {int(ms_df.withdrawn.sum())}")
    print(f"families with subject: {fam_df.subject.notna().sum()}")
    print(f"families with Lean doc: {int(fam_df.has_lean_doc.sum())}  with resolved declarations: {(fam_df.lean_declarations != '').sum()}")
    print(f"manuscripts in formalization.yaml: {int(ms_df.in_formalization_yaml.sum())}")
    print(f"manuscripts with main .tex: {(ms_df.main_tex != '').sum()}  with >1 candidate: {(ms_df.n_main_tex_candidates > 1).sum()}")
    print(f"reasoning traces: {len(traces)}")
    print("subjects:\n" + fam_df.subject.value_counts().to_string())
    extra = sorted(all_dirs - listed)
    if extra:
        print("\nsample dirs not in CONTENTS:", *extra[:8], sep="\n  ")


if __name__ == "__main__":
    main()
