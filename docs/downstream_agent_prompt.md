# Downstream-target agent brief (Lean shortlist; shared)

You are a RESEARCH analyst on a project at `C:\Users\anant\AI-Hard`. The project tests whether AI-produced mathematics contains genuine **eureka steps**: new definitions, constructions or lemmas that are hard to find and that let *other* theorems be proved with much less budget. The anchor example is Cook–Reckhow's extension variables, which collapse pigeonhole proofs from exponential to polynomial size.

Read `docs/PLAN.md` for context: eureka steps, N0–N3, axis F, tests 1–4 and the speedup test. The jump definition is STRICT:
- Importing known math from another field is transfer (N0), not a jump.
- Novelty is judged against all of mathematics.
- Only a downstream speedup on OTHER theorems confirms a jump.

Your item is on the project's **eureka shortlist** (`data/eureka_shortlist.json`). The speedup and discoverability tests will be run **in Lean 4**: Mathlib at d13f23b plus the openai/math library at commit fd4aeeb (`data/raw/openai-math/lean/`, toolchain leanprover/lean4:v4.34.1). That raises two questions, and your job is to answer both.

## Part A: Is the item really in the Lean?
1. Read the family's analyses in `data/pilot/<fid>/`: `novelty.json` (the N3 candidate, especially `test3`), `family.json`, and `lean.json` if present. Also read the shortlist entry's `lean_decls` hint.
2. Locate the item's Lean declarations under `data/raw/openai-math/lean/OAI/...`. Copy VERBATIM the defining declaration(s) (`def` / `structure` / `abbrev` / key `theorem` statement, with docstrings, without proofs), and the 2–5 key lemmas that state its defining property or use it decisively. Record each with file and line.
3. Check that the comparator target actually depends on it. Comparators are in `lean/ComparatorChallenges/*.json` and `lean/docs/<fid>.md`. Trace the dependency chain from the comparator's `solution_module` theorem down to the item; you may run `python scripts/extract_lean.py` (read its docstring for usage) or read imports and proofs by hand. Record the chain as a list of declaration names.
4. Record every gap between the paper's item and the Lean version: a different proof route, a weaker or special-case statement, extra hypotheses, or a comparator weaker than the headline.
5. Give `lean_status`, one of:
   - `"as in paper"`
   - `"formalized, different route"`
   - `"special case only"`
   - `"statement only"`
   - `"not formalized"`

   Give a one-sentence justification. If the item is not really in the Lean, say so plainly; it will be dropped from the shortlist.

The Lean has not been compiled; there is no local toolchain. Work at text level, and say that you did.

## Part B: Related problems to try it on
Find the problems we should run the item on, in two groups.

1. **Speedup targets** (3–8): KNOWN theorems whose existing proofs might become much shorter, or whose proof search much cheaper, if the item is in the prover's library. These are the measurable cases. For each, give:
   - statement and reference;
   - current proof size (pages, and Lean lines if a formalization exists anywhere: Mathlib, other Lean libraries, or other OAI families);
   - how the item would shorten it;
   - expected speedup (low / med / high).
2. **Open or new problems** (5–12) where the same obstruction appears, in ANY field. Prefer 2015–2026 problem lists, surveys and MathOverflow. For each, give:
   - statement, reference and URL;
   - status;
   - which part of the obstruction matches;
   - an adaptation sketch;
   - payoff, confidence and difficulty.

For EVERY target in both groups, also give `lean_feasibility`:
- **(a) Statable now?** Can the statement be written with Mathlib d13f23b plus the OAI library? Name the Mathlib/OAI notions it needs.
- **(b) Missing definitions.** If any are missing, list them with a rough line-count estimate.
- **(c) Size comparison.** Is there an existing formal proof to compare sizes against?
- **Score:** `"statable now"`, `"statable with < 300 lines of new definitions"`, or `"needs major new library"`.

Prefer targets that are statable now: a target we cannot state in Lean is not usable for the test. Rank Lean-usable targets first.

**Rules for what counts as reuse:**
- A **corollary of the theorem** is NOT reuse of the device. Record those separately under `theorem_corollaries`: they show the result has reach, but they don't count toward a jump.
- **Witness items** (a counterexample object): device reuse means the same *design* produces other witnesses, or refutes other conjectures. Check the release itself (`data/raw/openai-math/CONTENTS.md` and other families' sources) for families that already reuse the design.
- **Negative controls**: give 1–3 theorems or settings where the device should NOT help, or should fail. A proved-false analogue is ideal.

## Precedent
Note anything found after Oct 6, 2026 that uses the device, or any earlier equivalent. An earlier equivalent downgrades the item; say so plainly.

Be skeptical: superficial analogies are worthless. Say "no strong candidate found" if that is the truth. Use `sys.stdout.reconfigure(encoding='utf-8')` when printing Unicode from Python on Windows. Quote sparingly. Do not modify files outside your family's pilot folder.

## Deliverables (per family, in `data/pilot/<fid>/`)
- `downstream.json`, with keys:
  - `fid`, `item`, `item_type` (F1–F5, lemma or witness);
  - `lean_status`, `lean_status_why`, `lean_gaps`;
  - `comparator_chain` (list of declaration names);
  - `lean_source` (list of `{name, kind, file, line, text}`, with `text` verbatim);
  - `speedup_targets` (list), `open_problems` (list); each target has `title`, `statement`, `reference`, `status`, `how_item_helps`, `expected_speedup` / `payoff`, `confidence`, `lean_feasibility` `{score, statable_with, missing, formal_proof_to_compare}`;
  - `theorem_corollaries`, `release_reuse`, `negative_controls`;
  - `top5`: ranked, Lean-usable first, with a one-paragraph argument each;
  - `precedent_check`, `sources`, `search_log`.
- `downstream.md`: a readable report.

Your final message should be a ≤200-word summary: `lean_status` (one line), the top 3 Lean-usable targets, and any precedent.
