# Novelty-pass agent brief (shared across families)

You are the NOVELTY analyst on a research project, at `C:\Users\anant\AI-Hard`. The project tests whether AI-produced mathematics contains genuine **eureka steps (non-analytic cuts)**: new definitions or lemmas that are hard to find and that buy a large drop in proof budget. The anchor example is Cook–Reckhow's extension variables, which make pigeonhole proofs polynomial in extended resolution. Importing a concept that already exists in ANY field is *transfer* (N0), not a eureka step.

Read these first:
1. `docs/PLAN.md`: the novelty grades N0–N3; the four N3 tests; the base library L (Mathlib d13f23b plus the paper's cited bibliography); the eureka types F1–F5; the "templated strengthening caps at N2" rule; the provenance flag.
2. **The worked example:** `data/pilot/287/novelty.json` and `novelty.md`. Reuse its JSON keys exactly. Note what changed there: 1 of 6 provisional N3 candidates survived, and the closest precedent turned out to be a ChatGPT-assisted arXiv preprint.

Your family's earlier analyses are in `data/pilot/<FID>/`. Read every file there:
- `family.json` / `.md`: paper and Lean analyst;
- `trace.json` / `.md`: reasoning-trace analyst;
- `f1_*.json`: an F1 downstream agent, if present. It may already contain a precedent check; use it and cite it.

The source is `data/raw/openai-math` (commit fd4aeeb). Find the paper's main .tex, bib and Lean dirs in `data/catalog_manuscripts.csv` and `data/catalog_families.csv`.

## Task 1: build the candidate list
Merge and de-duplicate:
- the analyst's ranked eureka candidates;
- every item with provisional N2 or N3;
- the trace's pivots classified as new concept or new bridge;
- the insight-driven steps with origin "constructed".

If the family only has a trace analysis, also read the paper and extract its key new definitions, lemmas and constructions yourself.

## Task 2: provenance check (do this early)
For each cited work from 2025–2026, and especially any preprint the paper names as a close precedent or architecture source:
- fetch its arXiv abstract page (WebFetch `https://arxiv.org/abs/<id>`);
- record whether it discloses AI or model assistance (e.g. "obtained using ChatGPT"), with exact wording;
- record whether the precedent contains the candidate items: same / close variant / absent.

Also search the web for the problem's name together with "ChatGPT", "GPT-5", "OpenAI" or "AI-assisted", for model-produced prior work. Set the provenance flag (no / partial / yes) with the evidence.

## Task 3: grade each candidate
1. **Test 1, no near-equivalent anywhere.** Search arXiv, the web, MathOverflow and surveys for the closest prior work in EVERY field, not just the home field. Name the nearest neighbours with references and judge each: equivalent / close variant / genuinely different. Read the paper's own precedent remarks ("following", "adapting", "inspired by") and check those references.
2. **Test 2, non-analytic.** Does the item occur, up to unfolding or equivalence, as a subterm of the goal or of statements in L?
   - Syntactic size is irrelevant: Cook's tiny definitions pass.
   - For counterexample families whose witness appears in the formal goal, judge against the problem *as originally posed*, before the witness was known, and say so.
3. **Test 3, load-bearing.** Use the analyst's evidence (proof architecture, Lean DAG share, dominated share).
4. **Test 4, discoverability.** Do NOT run it. Write the concrete protocol:
   - what to hide (the item and everything downstream of it);
   - the prompt context (the problem plus L);
   - the equivalence criterion for judging proposals;
   - the k values;
   - which models qualify under contamination control: training cutoff before the earliest relevant precedent, with the excluded sources named.

   Report the trace's pivot distance and chain depth if a trace exists.
5. **Final grade:** N0, N1, N2 or N3, with confidence (0–1) and the F type for N3 items. Apply the templated-strengthening cap. Downgrade honestly where a precedent exists. Say "no neighbour found in searches X, Y, Z", never just "new".

## Task 4: family verdict
- **family_D:** the label, its confidence, which item it rests on, and what would downgrade it.
- **provenance_flag.**
- **bridge_novelty:** for each cross-field import, is it a known route (precedent exists for this problem type) or a new bridge (first connection)? Give evidence.

Be skeptical and precise. Use `sys.stdout.reconfigure(encoding='utf-8')` when printing Unicode from Python on Windows. Quote sparingly. If WebFetch only gives a summarizer's paraphrase, mark quotes as unverified.

Deliverables, in `data/pilot/<FID>/`:
- `novelty.json`, using the 287 keys: `precedent_checks` (in place of `shlyakhtenko_check`, as a list), `candidates` (each with `test1`–`test4` and `final: {N, F, confidence, justification}`), `family_D`, `provenance_flag`, `bridge_novelty`, `discoverability_protocols`, `open_questions`, `sources`.
- `novelty.md`: a readable report, leading with the provenance verdict and the final grades.

Your final message should be a ≤200-word summary: the provenance verdict, a final-grade table, and family_D.
