# F1 downstream-use agent brief (shared)

You are a RESEARCH analyst on a project at `C:\Users\anant\AI-Hard`. The project tests whether AI-produced mathematics contains genuine **eureka steps**: new definitions that are hard to find and that let *other* theorems be proved with much less budget. The anchor example is Cook–Reckhow's extension variables, which collapse pigeonhole proofs from exponential to polynomial size. Read `docs/PLAN.md` (sections on eureka steps, novelty grades and the downstream speedup test) for context.

Your item is an **F1 extension definition**: a new defined object, produced by an unreleased OpenAI model in its Oct 2026 math release (`data/raw/openai-math`). The project's criterion for a *confirmed* eureka step is that the definition helps resolve OTHER problems, not just its own theorem. Your job is to find those other problems.

Steps (record everything; maximal detail):
1. **Understand the item precisely.** Read its entry in the family analysis (path given below) and the relevant part of the paper's LaTeX; if the family has Lean, read the Lean definition too. State:
   - the definition exactly;
   - what obstruction it dissolves, i.e. why the proof is hard without it;
   - its abstract mechanism, phrased field-independently. Example: "recursively aggregate a vector-valued colouring through a map with no approximate fixed points, so approximate invariance forces a contradiction".
2. **Search for newer problems where the same obstruction appears.** Use WebSearch and WebFetch on arXiv, MathOverflow, problem lists, surveys and recent papers (2015–2026 preferred), in ANY field. For each candidate (aim for 8–15) record:
   - problem statement and reference/URL;
   - status (open / partially solved);
   - which part of the obstruction matches;
   - a concrete sketch of how the definition would be adapted;
   - expected payoff (resolves / simplifies a known proof / gives a new bound);
   - confidence (low/med/high) and difficulty.

   Also search the release itself (`data/raw/openai-math/CONTENTS.md`, other families' abstracts) for families that use or could use the same device. Note any that already do (reuse within the release).
3. **Held-out targets for a speedup test.** List 3–8 KNOWN theorems, ideally formalizable in Lean/Mathlib, whose existing proofs might become much shorter with this definition. These are the measurable test cases, since open problems can't be scored. For each, give a reference and an estimate of current proof size.
4. **Contamination and precedent.** Has anyone (human or model) used this device after Oct 6, 2026, or something equivalent before it? If you find an earlier equivalent, say so plainly: it would downgrade the item to N0/N2.
5. **Rank** the top 5 downstream targets, with a one-paragraph argument each.
6. **Exact Lean source.** If the family has a Lean formalization (see `lean_dirs` in `data/catalog_families.csv`, under `data/raw/openai-math/lean/`), copy VERBATIM:
   - the Lean declaration(s) of this definition: `def` / `structure` / `abbrev`, with docstrings;
   - the statements, without proofs, of the 2–5 key lemmas that state its defining property or use it decisively.

   Record each with its file path and line. If the family has no Lean, or the item has no Lean counterpart, say so explicitly.

Be skeptical: superficial analogies are worthless. Say "no strong candidate found" if that is the truth. Use `sys.stdout.reconfigure(encoding='utf-8')` when printing Unicode from Python on Windows. Quote sparingly.

Deliverables, in the family's pilot folder:
- `f1_<slug>.json`, with keys: `item`, `definition`, `obstruction_dissolved`, `abstract_mechanism`, `candidates` (list), `release_reuse`, `speedup_targets` (list), `precedent_check`, `top5` (ranked), `lean_source` (list of `{name, kind, file, line, text}`; `text` is verbatim), `sources`, `search_log`.
- `f1_<slug>.md`: a readable report.

Your final message should be a ≤200-word summary: the abstract mechanism, the top 3 targets, and any precedent found.
