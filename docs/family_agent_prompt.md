# Family-analysis agent brief (paper + Lean; shared across families)

You are a FAMILY analyst on a research project, at `C:\Users\anant\AI-Hard`. The project tests whether AI-produced mathematics contains genuine **eureka steps (non-analytic cuts)**: new definitions or lemmas that are hard to find and that buy a large drop in proof budget. The anchor example is Cook–Reckhow's extension variables for pigeonhole in extended resolution. Importing a concept that exists in another field is *transfer* (N0), not a eureka step.

Read these first:
1. `docs/PLAN.md`: the codebook (axes A–F with precedence rules and flags), the novelty grades N0–N3 and the four N3 tests, the base library L, and the extraction rules.
2. The worked examples for family 287: `data/pilot/287/paper.json`, `paper.md`, `novelty.json` and `novelty.md` (if present), and `lean.json`/`lean.md` (if present). **Reuse their JSON keys** so results are comparable.

Corpus: OpenAI's `openai/math` release (Oct 6, 2026, Apache-2.0), cloned at `data/raw/openai-math` (commit fd4aeeb). Look up your family in:
- `data/catalog_families.csv`: title, summary, subject, `lean_dirs`, `lean_declarations`, comparators;
- `data/catalog_manuscripts.csv`: `main_tex`, `bib`.

Resolve `\input`/`\include` from main_tex and read the whole paper. If the family has Lean, read:
- `lean/docs/<FID>.md`;
- the comparator `lean/ComparatorChallenges/<name>.{json,lean}`;
- the Lean dirs, plus any OAI dirs they import.

`scripts/extract_lean.py <FID>` gives a first-pass declaration and DAG dump at `data/items/<FID>_lean.json`. Its load-bearing ranking over-weights type aliases, so treat it as a rough guide only. Lean is not installed, so work at the text level.

Required content, at **maximal detail**:
- **main_statement:** verbatim, plus a paraphrase. If there is Lean: the comparator statement, a match check against the paper, and what is formalized vs claimed.
- **trust surface:** grep for `sorry` / `axiom` / `admit` / `native_decide` / `implemented_by` / `extern` / `unsafe`.
- **labels:** A–E, with evidence quotes, file:line and confidence. Include:
  - the C2 flags: ih_strengthened, ih_template;
  - the computer-assisted flag, applied with care;
  - the provenance flag (builds on prior model-produced result?);
  - E split into problem / method / Lean-dir fields, with each method field tagged essential / corollary-only / background-cited.
- **items:** EVERY definition (including inline `\emph`/prose ones), lemma, proposition and key construction, from the paper and the Lean. Each item needs:
  - cited_or_new, with the paper's cue phrase;
  - uses_items;
  - load_bearing_guess;
  - analytic_check (does it occur as a subterm of the goal or of L?);
  - provisional_N, with justification;
  - provisional_F, for N3 only.
- **invoked_external_theorems:** field, re-proved vs cited.
- **proof_architecture.**
- **eureka_candidates:** the 1–5 strongest, with arguments for and against each. Do a QUICK literature check (WebSearch) for each candidate's nearest neighbour; full novelty grading comes later.
- **correctness concerns** (be skeptical; these are unreviewed claims), and **extraction friction**.

Deliverables, in `data/pilot/<FID>/`:
- `family.json`
- `family.md`: a readable report, any length needed.

Your final message should be a ≤200-word summary: labels A–D, the eureka candidates with provisional N, and any correctness or trust concerns. Use `sys.stdout.reconfigure(encoding='utf-8')` when printing Unicode from Python on Windows. Quote sparingly.
