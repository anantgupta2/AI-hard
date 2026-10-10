"""Run the family analysis + novelty pass for given families through the Claude API (your API key).

Same outputs as the in-session agents: data/pilot/<FID>/{family,novelty}.{json,md}, plus
api_<phase>_raw.json (full response, usage, cost) for auditing.

Per family, two streamed requests share a cached prefix (tools -> system -> paper):
  1. family  : labels A-E, every item with provisional N/F, proof architecture, eureka candidates
  2. novelty : provenance check, tests 1-4 per candidate, final grades, family_D (web search + fetch)

Auth: set ANTHROPIC_API_KEY in your shell (or use an `ant auth login` profile). Nothing is hardcoded.

Usage:
  python scripts/api_pipeline.py 046 079 357 368 367 --dry-run         # build prompts, estimate cost, no API calls
  python scripts/api_pipeline.py 046 079 357 368 367 --max-usd 40      # run
  python scripts/api_pipeline.py 046 --phase novelty                   # rerun one phase
"""

import argparse
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "data" / "raw" / "openai-math"
PILOT = ROOT / "data" / "pilot"
MODEL = "claude-opus-5-5"
# $ per million tokens for claude-opus-5-5 (input, output, cache write 5m, cache read); web search $ per search.
PRICE = {"in": 4.00, "out": 20.00, "cache_write": 5.00, "cache_read": 0.20, "search": 0.01}
TOOLS = [
    {"type": "web_search_20260209", "name": "web_search", "max_uses": 30},
    {"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": 20},
]
MAX_CONTINUATIONS = 6
BS = "\\"

SYSTEM = """You are a research analyst on a project testing whether AI-produced mathematics contains genuine eureka steps (non-analytic cuts): new definitions or lemmas that are hard to find and that buy a large drop in proof budget. The anchor example is Cook-Reckhow's extension variables, which make pigeonhole proofs polynomial in extended resolution. Importing a concept that already exists in ANY field is transfer (grade N0), not a eureka step.

The corpus is OpenAI's Oct 6, 2026 release `openai/math` (372 result families, produced by an unreleased internal model; Apache-2.0). You analyse one family at a time. You cannot read files: the paper's full LaTeX source, the catalogue entry and (where it exists) the Lean comparator statement are provided in the user turn. You have web_search and web_fetch for literature and provenance checks.

The project plan below defines the codebook (axes A-F with precedence rules and flags), the novelty grades N0-N3, the four N3 tests, the base library L, and the search-dynamics terms. Apply it exactly.

Standards: be rigorous and skeptical; these are unreviewed claims. Every label needs evidence: a verbatim quote of at most 2 lines with file:line. Never write "new" without saying where you searched ("no neighbour found in searches X, Y, Z"). Downgrade honestly where a precedent exists. Quote sparingly.

<project_plan>
{plan}
</project_plan>
"""

FAMILY_TASK = """PHASE 1: FAMILY ANALYSIS for family {fid}.

Produce, at maximal detail:
- main_statement: verbatim plus paraphrase. If a Lean comparator is provided: the comparator statement, whether it matches the paper, and what is formalized vs claimed. Note that only the comparator and docs were provided, not the Lean library, so you cannot audit the trust surface; say so.
- labels: A-E with evidence (quote + file:line) and confidence. Include C2 flags (ih_strengthened, ih_template), the computer_assisted flag, the provenance flag (builds on prior model-produced result?), and E split into problem / method fields, each method field tagged essential / corollary-only / background-cited.
- items: EVERY definition (including inline \\emph and prose definitions), lemma, proposition and key construction. Each item has id, kind, name, file_line, statement, cited_or_new (with the paper's cue phrase), uses_items, load_bearing_guess, analytic_check, provisional_N with justification, and provisional_F (N3 only).
- invoked_external_theorems: field, and whether re-proved or cited.
- proof_architecture.
- eureka_candidates_ranked: a list of objects {{rank, item, name, provisional_N, provisional_F, for: [..], against: [..]}} for the 1-5 strongest. Use web_search for a QUICK nearest-neighbour check on each.
- correctness_audit (look for gaps and "proves too much" failures) and extraction_friction.

Output format, exactly:
<json>
{{ a single JSON object with keys: family, title, main_statement, labels, items, invoked_external_theorems, proof_architecture, eureka_candidates_ranked, correctness_audit, extraction_friction }}
</json>
<report>
A readable markdown report (any length needed) with the same content.
</report>"""

NOVELTY_TASK = """PHASE 2: NOVELTY PASS for family {fid}. Your Phase 1 analysis is below.

<phase1>
{phase1}
</phase1>

1. Candidate list: merge and de-duplicate the ranked eureka candidates and every item with provisional N2 or N3.
2. Provenance (do this early): for each cited work from 2025-2026, and any preprint the paper names as a close precedent, web_fetch its arXiv abstract page (https://arxiv.org/abs/<id>). Record whether it discloses AI or model assistance (exact wording) and whether it contains the candidates: same / close variant / absent. Also web_search the problem's name with "ChatGPT", "GPT-5", "OpenAI" and "AI-assisted". Set provenance_flag: no / partial / yes, with evidence.
3. For each candidate:
   - test1: nearest neighbours in EVERY field, with references; judge equivalent / close variant / different.
   - test2: non-analytic against L. For counterexample witnesses, judge against the problem as originally posed.
   - test3: load-bearing.
   - test4: a discoverability PROTOCOL, not run: what to hide, the prompt context, the equivalence criterion, the k values, and which models qualify under contamination control (cutoff before the earliest relevant precedent, excluded sources named).
   - final: {{N, F, confidence (0-1), justification}}. Apply the templated-strengthening cap.
4. family_D: {{label, confidence, rests_on, falls_to}}; provenance_flag; bridge_novelty (for each cross-field import: known route vs new bridge, with evidence).

Output format, exactly:
<json>
{{ a single JSON object with keys: family, precedent_checks (list), candidates (list, each with id, name, statement, test1, test2, test3, test4, final), family_D, provenance_flag, bridge_novelty, discoverability_protocols, open_questions, sources }}
</json>
<report>
A readable markdown report, leading with the provenance verdict and a final-grade table.
</report>"""


def resolve_tex(path, seen=None, depth=0, root=None):
    """Inline \\input / \\include recursively; drop full-line comments.

    LaTeX resolves input paths relative to the main file's directory, so try `root` before the including file's directory.
    """
    seen = seen or set()
    root = root or path.parent
    if depth > 12 or path in seen or not path.exists():
        return f"% [missing: {path.name}]\n" if not path.exists() else ""
    seen.add(path)
    out = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.lstrip().startswith("%"):
            continue
        m = re.search(r"\\(?:input|include)\{([^}]+)\}", line)
        if m:
            name = m.group(1).strip()
            fname = name if name.endswith(".tex") else name + ".tex"
            candidates = [root / fname, path.parent / fname, path.parent / Path(fname).name]
            child = next((c for c in candidates if c.exists()), candidates[0])
            out.append(f"% ===== begin {child.name} =====")
            out.append(resolve_tex(child, seen, depth + 1, root))
            out.append(f"% ===== end {child.name} =====")
        else:
            out.append(line)
    return "\n".join(out)


def family_material(fid):
    fams = pd.read_csv(ROOT / "data" / "catalog_families.csv", dtype={"family_id": str})
    mss = pd.read_csv(ROOT / "data" / "catalog_manuscripts.csv", dtype={"family_id": str})
    row = fams[fams.family_id == fid].iloc[0]
    parts = [f"<catalogue>\nfamily_id: {fid}\ntitle: {row.title}\nsubject: {row.subject}\nsummary: {row.summary}\n"
             f"lean_dirs: {row.lean_dirs if isinstance(row.lean_dirs, str) else 'none'}\n</catalogue>"]
    for _, ms in mss[mss.family_id == fid].iterrows():
        main = REPO / ms.main_tex
        tex = resolve_tex(main)
        bib = ""
        if isinstance(ms.bib, str):
            for b in ms.bib.split(";"):
                p = REPO / b
                if p.exists():
                    bib += p.read_text(encoding="utf-8", errors="replace")
        parts.append(f'<manuscript title="{ms.ms_title}" dir="{ms.ms_dir}" main_tex="{ms.main_tex}">\n'
                     f"<abstract>{ms.abstract}</abstract>\n<latex>\n{tex}\n</latex>\n<bibliography>\n{bib}\n</bibliography>\n</manuscript>")
    doc = REPO / "lean" / "docs" / f"{fid}.md"
    if doc.exists():
        lean = [f"<lean_docs>\n{doc.read_text(encoding='utf-8')}\n</lean_docs>"]
        for c in re.findall(r"ComparatorChallenges/([A-Za-z0-9_]+)\.lean", doc.read_text(encoding="utf-8")):
            for ext in (".lean", ".json"):
                p = REPO / "lean" / "ComparatorChallenges" / f"{c}{ext}"
                if p.exists():
                    lean.append(f'<comparator file="ComparatorChallenges/{c}{ext}">\n{p.read_text(encoding="utf-8")}\n</comparator>')
        parts.append("\n".join(lean))
    return "\n\n".join(parts)


def usage_cost(u):
    def g(name):
        return getattr(u, name, 0) or 0
    searches = getattr(getattr(u, "server_tool_use", None), "web_search_requests", 0) or 0
    cost = (g("input_tokens") * PRICE["in"] + g("output_tokens") * PRICE["out"]
            + g("cache_creation_input_tokens") * PRICE["cache_write"] + g("cache_read_input_tokens") * PRICE["cache_read"]) / 1e6
    cost += searches * PRICE["search"]
    return {"input": g("input_tokens"), "output": g("output_tokens"), "cache_write": g("cache_creation_input_tokens"),
            "cache_read": g("cache_read_input_tokens"), "web_searches": searches, "usd": round(cost, 4)}


def run_phase(client, system, material, task):
    """One analysis turn, continuing through pause_turn. Returns (final_text, usage_list, stop_reason, model)."""
    messages = [{"role": "user", "content": [
        {"type": "text", "text": material, "cache_control": {"type": "ephemeral", "ttl": "1h"}},
        {"type": "text", "text": task},
    ]}]
    usages, texts = [], []
    for _ in range(MAX_CONTINUATIONS + 1):
        with client.beta.messages.stream(
            model=MODEL,
            max_tokens=64000,
            betas=["server-side-fallback-2026-07-01"],
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral", "ttl": "1h"}}],
            tools=TOOLS,
            thinking={"type": "adaptive"},
            output_config={"effort": "high"},
            messages=messages,
            extra_body={"fallbacks": "default"},
        ) as stream:
            final = stream.get_final_message()
        usages.append(usage_cost(final.usage))
        texts.extend(b.text for b in final.content if b.type == "text")
        if final.stop_reason == "refusal":
            cat = getattr(final.stop_details, "category", None) if final.stop_details else None
            raise RuntimeError(f"refusal (category={cat})")
        if final.stop_reason != "pause_turn":
            return "\n".join(texts), usages, final.stop_reason, final.model
        # Server tool loop paused: resend with the partial assistant turn appended.
        messages = messages + [{"role": "assistant", "content": [b.to_dict() for b in final.content]}]
    return "\n".join(texts), usages, "max_continuations", MODEL


def parse_output(text):
    j = re.search(r"<json>\s*(.*?)\s*</json>", text, re.S)
    r = re.search(r"<report>\s*(.*?)\s*</report>", text, re.S)
    data = None
    if j:
        raw = j.group(1).strip()
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            data = {"_parse_error": str(e), "_raw": raw[:200000]}
    return data, (r.group(1) if r else text)


def process(client, fid, phases, plan):
    system = SYSTEM.format(plan=plan)
    material = family_material(fid)
    out = PILOT / fid
    out.mkdir(parents=True, exist_ok=True)
    total = 0.0
    for phase in phases:
        if phase == "family":
            task = FAMILY_TASK.format(fid=fid)
        else:
            p1 = out / "family.json"
            if not p1.exists():
                raise RuntimeError("novelty phase needs family.json; run the family phase first")
            task = NOVELTY_TASK.format(fid=fid, phase1=p1.read_text(encoding="utf-8"))
        t0 = time.time()
        text, usages, stop, served_by = run_phase(client, system, material, task)
        data, report = parse_output(text)
        cost = round(sum(u["usd"] for u in usages), 4)
        total += cost
        (out / f"api_{phase}_raw.json").write_text(json.dumps(
            {"family": fid, "phase": phase, "model": served_by, "stop_reason": stop, "seconds": round(time.time() - t0),
             "usage": usages, "usd": cost, "text": text}, ensure_ascii=False, indent=1), encoding="utf-8")
        if data is not None:
            data.setdefault("family", fid)
            data["_produced_by"] = f"api_pipeline.py ({served_by})"
            (out / f"{phase}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        (out / f"{phase}.md").write_text(report, encoding="utf-8")
        ok = "ok" if data is not None and "_parse_error" not in data else "JSON PARSE FAILED (see raw)"
        print(f"[{fid}] {phase}: {ok}, stop={stop}, ${cost:.2f}, {round(time.time() - t0)}s", flush=True)
    return fid, total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("families", nargs="+")
    ap.add_argument("--phase", choices=["family", "novelty", "both"], default="both")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--max-usd", type=float, default=50.0, help="stop launching new families once spend passes this")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    fids = [f.zfill(3) for f in args.families]
    phases = ["family", "novelty"] if args.phase == "both" else [args.phase]
    plan = (ROOT / "docs" / "PLAN.md").read_text(encoding="utf-8")

    if args.dry_run:
        sys_tok = len(SYSTEM.format(plan=plan)) / 3.5
        est_total = 0.0
        for fid in fids:
            mat = family_material(fid)
            tok = len(mat) / 3.5
            # rough: phase 1 writes the cache, phase 2 reads it; ~25k output per phase; ~20 searches in phase 2
            est = ((sys_tok + tok) * PRICE["cache_write"] + (sys_tok + tok) * PRICE["cache_read"] + 2 * 25000 * PRICE["out"]) / 1e6 + 20 * PRICE["search"]
            est_total += est
            print(f"[{fid}] material ~{tok / 1000:.0f}k tokens (+{sys_tok / 1000:.0f}k system); rough cost ${est:.2f}")
        print(f"rough total ${est_total:.2f} (continuations and long outputs can raise this; --max-usd caps launches)")
        return

    import anthropic  # imported here so --dry-run works without credentials
    client = anthropic.Anthropic(max_retries=4)
    spent = 0.0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {}
        for fid in fids:
            if spent >= args.max_usd:
                print(f"budget reached (${spent:.2f}); not launching {fid}")
                continue
            futures[pool.submit(process, client, fid, phases, plan)] = fid
        for fut in as_completed(futures):
            fid = futures[fut]
            try:
                _, cost = fut.result()
                spent += cost
            except anthropic.AuthenticationError:
                print("Authentication failed: set ANTHROPIC_API_KEY in this shell.")
                raise
            except Exception as e:  # keep the other families running
                print(f"[{fid}] FAILED: {type(e).__name__}: {e}")
    print(f"total spend ${spent:.2f}")


if __name__ == "__main__":
    main()
