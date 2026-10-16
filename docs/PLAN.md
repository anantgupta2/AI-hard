# Plan: Mapping and bucketing OpenAI's Oct 6, 2026 math release (`openai/math`)

## Context
The user is testing an AI-easy vs AI-hard hypothesis:
- **AI-easy:** solvable by recombining existing definitions and theorems.
- **AI-hard:** needs a **eureka step (non-analytic cut)**.

The anchor example is the pigeonhole principle (PHP):
- In plain resolution, which has no new definitions, every PHP proof is exponential in size (Haken 1985).
- In extended resolution, Cook–Reckhow (1979) add a few extension variables that encode the reduction from n+1 pigeons to n. With them, the proof becomes polynomial.
- Those definitions are syntactically tiny, yet hard to find. In general, proof search in extended systems is believed not to be automatable.

So a eureka step is something **hard to construct** that buys a **large drop in proof budget**. Being syntactically complex is not the criterion. Importing a known concept from another field is **transfer, not a eureka step**.

The test corpus is OpenAI's Oct 6, 2026 release. Before any eureka-step test we need a structured map of it:
- **what** was proven, and **how**;
- **which fields** it uses, including theorems borrowed from other fields;
- every **new lemma and definition**, graded for whether it is *sufficiently* new.

A pilot probe of three formalized families (173, 132, 179) has been run.

## What exists in the repo (pinned commit `fd4aeeb`)
| Item | Path | Use |
|---|---|---|
| 372 families / 719 manuscripts | `CONTENTS.md` (`**NNN. Title.**` + manuscript links + abstracts) | Master index. IDs run to 377 with gaps; the 3 withdrawals are in `history.md` |
| 17-subject taxonomy | `overview.tex` (`\cataloguesection{…}`, `\resultentry{NNN}{…}`) | Problem-field label |
| 749 preprint dirs | `preprints/<Title>-<Date>/`: README (BibTeX), PDF, LaTeX source + `references.bib`. **The layout varies**: `build/source/main.tex`, `build/main.tex` + `sections/`, or `build/paper.tex` + `sections/` | Statements, proofs, definitions, citations |
| Lean library, ~300/719 top-line formalized | `lean/OAI/<Field>/<Topic>/`, `lean/formalization.yaml` (`main_results`), `lean/docs/NNN.md` (scope + **all** comparators), `lean/ComparatorChallenges/*.json` | Quantifier structure, declaration DAG, imports |
| Lean deps | `lean/lake-manifest.json` (Mathlib `d13f23b` + about 30 external libraries) | Cross-library use. Also pins L (see below) |
| Reasoning traces (10 families) | `reasoning_traces/*.pdf` | The only view of the *process* |

Families per subject:
- TCS 40
- Combinatorics 37
- Algebraic and complex geometry 36
- Number theory 31
- Probability and statistical mechanics 29
- Differential geometry 29
- Mathematical physics 25
- Operator algebras 19
- Algebra 18
- Topology 18
- Real and complex analysis 16
- PDE 16
- Convex and metric geometry 15
- Group theory 14
- Dynamical systems and ergodic theory 12
- Functional analysis 11
- Logic 6

There are 66 single-manuscript families with Lean formalizations, a pool for further pilots.

## Pilot results (families 173, 132, 179)
| | 173 Seymour 2nd-neighbourhood | 132 sensitivity vs block sensitivity | 179 circulant Hadamard |
|---|---|---|---|
| LaTeX ↔ Lean statement match | Exact | Exact for the ∀d ratio bound. The **α>2 headline is not the comparator target** (it is the sibling `fixed_power_separation`) | Exact for Hadamard. Barker: **even case only** |
| A Form | A2 (∀G ∃v) | A2 (a family of counterexamples indexed by d) | A4, hard direction A5 |
| B | B1 | B2 | B1 (Barker B1 only together with prior work) |
| C primary (secondary) | C3 (C2, C5, C1) | C1 (C2, C3 probabilistic, C4) | C3 (C2, C5) |
| Computer-assisted | No | No (9 `decide` uses, all Bool coercions) | No (`decide` used only on trivia) |
| Lean size | 76 def / 261 thm | ~60 def / 268 thm | 148 def / 660 thm |
| Eureka candidates | Pruning lemma, which charges conflict-deletion cost to points left uncovered; extremal objective M+d | Joint-sensitivity profile J; gated-tournament predicates, adapted from Meiburg2026, **which credits GPT-5.6-Sol** | Δ(x): an alternating product of character values over subsets of primes. The paper names close precedents |
| Problem field / Lean dir / method field | Combinatorics / Combinatorics / + linear algebra (generic rank), matching theory | TCS / Combinatorics / + combinatorics, elementary probability | Combinatorics / LinearAlgebra / **algebraic number theory + commutative algebra** |
| Cited but not used | LP/Farkas (corollaries only) | Huang's spectral proof (context only) | Schmidt field descent (background only) |

Lessons from the pilot:
1. A naive extractor fails in four places:
   - Definitions are often inline (`\emph{}`) rather than in environments.
   - The comparator target is not always the headline theorem.
   - Families can span several Lean dirs.
   - Lean namespaces (e.g. `Paper320`) are not family IDs.
2. Plumbing definitions dominate Lean's def count, so a load-bearing ranking is essential.
3. "Cited" ≠ "used". A cross-field signal should count only invoked theorems.
4. Field labels split three ways. Keep problem, method and Lean-dir fields separately.
5. Some "prior literature" is earlier model output. This needs a provenance flag.
6. The strongest candidate in 173 is a **lemma**, not a definition. Lemmas must also be candidates.

## Codebook
Each axis has 2–5 classes. Each label is backed by a verbatim quote plus its file and line, and a confidence.

**A. Logical form.** Read from the innermost conclusion of the *headline* claim. Treat parameters that only index a family of witnesses as outer ∀.
- A1 Universal ∀
- A2 Existential ∃, including counterexamples
- A3 Quantitative/sharp
- A4 Characterization ⇔
- A5 Impossibility ¬∃

Secondary fields: *hard-direction form* (for A4); *explicit-rate* flag.

**B. Relation to the posed problem.**
- B1 Confirms fully
- B2 Refutes
- B3 Partial, conditional or special case
- B4 Extends a known result

Flags: *full only together with prior results*; *adds corollaries for other conjectures*.

**C. Proof method.** One primary label plus secondaries.
- C1 Construction
- C2 Induction/iteration
- C3 Indirect/non-constructive
- C4 Estimation chain
- C5 Reduction/transfer

Precedence rules:
- If the witnessing object is built, C1 is primary.
- A minimal-counterexample argument is C3, with C2 as a secondary only if there is real descent.
- C5 applies only to cited results *invoked without being re-proved*.

Flags:
- *computer-assisted*: only when there is real search, not Bool coercions.
- **On C2:** *induction hypothesis strengthened?* (yes/no). If yes, *by a standard template?*, naming which entry of the template library in `docs/templates.md` it matches:
  - add a parameter;
  - generalize a constant;
  - carry an extra tracked quantity;
  - uniform/quantitative version;
  - strengthen to all subsets/substructures.

**D. Novelty of machinery.** The family's label is the maximum novelty grade among its items.
- D1: every item is N0 or N1
- D2: the best item is N2
- D3: at least one item is N3 (a eureka candidate). Cross-field transfer alone never yields D3.

Flag *builds on prior model-produced result* (e.g. Meiburg2026).

**E. Fields.**
- **Problem field:** OpenAI's subject, also mapped to MSC 2020.
- **Lean-dir field.**
- **Method fields:** every field of an *invoked* theorem or *used* import, each tagged *essential*, *corollary-only* or *background-cited*.

Metrics:
- per family: cross-field count, and share of invoked theorems from other fields;
- corpus-level: a problem × method **field-flow matrix**.

**F. Eureka type (N3 items only).**
- F1 Extension definition: a new defined object or variable, as in Cook's PHP variables.
- F2 Strengthened hypothesis or invariant.
- F3 Auxiliary construction: a gadget or object built only to drive the proof.
- F4 Potential or monovariant.
- F5 Change of representation, including embedding into a larger structure.

## Extracting new lemmas and definitions, with graded novelty
**Extraction.**
- **LaTeX side.**
  - Resolve `\input`/`\include`.
  - Collect all theorem-like environments, including custom `\newtheorem`s.
  - Collect inline definitions (`\emph{…}` in "we call/define/say that" sentences).
  - Record cue phrases: "adapt", "same construction as", "new", "following [x]".
- **Lean side.**
  - Collect `def`/`structure`/`inductive`/`class`/`abbrev` and `theorem`/`lemma` declarations.
  - Build the DAG from the comparator target(s) **and sibling headline theorems**.
- **Join** LaTeX and Lean items by name, docstring and file, with an LLM assisting.
- **Candidates are both definitions and lemmas.** A definition qualifies if it appears in the statement or hypothesis of a load-bearing theorem and is used in more than one file. A lemma qualifies if it is load-bearing and its statement is not already a subterm of the goal (test 2 below).

**The base library L** = Mathlib at the pinned commit `d13f23b`, plus the family's cited bibliography. Analyticity (test 2) is judged against L. Existence (N0) is judged against the wider literature in every field.

**Novelty grade.**
- **N0 Existing:** it, or an equivalent, exists in *any* field, including concepts transplanted across fields. Sources: Mathlib via Loogle/LeanSearch, the bibliography, zbMATH/arXiv.
- **N1 Abbreviation:** a renaming, special case or conjunction of concepts already in L.
- **N2 Variant:** a close neighbour exists, including precedents the paper names itself. **Templated strengthenings of an induction hypothesis are capped at N2.**
- **N3 Eureka candidate:** passes all four tests below.
- **Confirmed eureka step:** N3, *plus* the downstream speedup test (step 9). Only this counts as evidence against the hypothesis.

**N3 tests.**
1. **No near-equivalent anywhere.** Find nearest neighbours by embedding search over Mathlib and the literature, across all fields. Then attempt a Lean equivalence proof, or use an LLM judge whose prompt includes the paper's own precedent remarks.
2. **Non-analytic.** The item is analytic if, up to unfolding or equivalence, it occurs as a subterm of the goal or of statements in L. Operationalize this as a normalized subterm match, plus a bounded attempt to prove equivalence against the nearest matches.
   - **Syntactic size is irrelevant.** Cook's PHP definitions are tiny Boolean combinations but occur nowhere in the goal, so they pass.
3. **Load-bearing.** At least *k*% of the DAG on the path to the main theorem depends on the item (*k* starts at 20%). Step 3b checks this proxy against actual compression.
   - **Pilot finding:** measure the share relative to the **mathematical core** of the DAG, not the whole formalization. In 287, 66% of the DAG re-proves classical background theory (transfer), and in 112, about 60% is Turing-machine plumbing. In both, the key new item falls below 20% of the whole but clears it within the core.
   - Exclude re-proved background results and encoding or plumbing layers before computing the share.
   - **Extractor v3 (2026-10-10):** compute Lean DAG shares with `scripts/extract_lean.py` v3 or later. v2 resolved field notation `x.foo` and qualified names such as `Nat.foo` by their last component alone, so 103's `T.factorial` (`T : ℕ`) became the local `Hie.factorial`, at 35% of the DAG instead of 2%. `scripts/test_extract_lean.py` is the regression check. Figures that the v3 rerun moved carry a dated `correction_2026_10_10_extractor_v3` note in test3 of `novelty.json`; a changed verdict goes in `corrected_verdict_2026_10_10`, and the original text stays.
4. **Discoverability.**
   - Hide the item and everything downstream of it. Give a model the problem plus L, and sample *k* proposals. Check each for equivalence with the hidden item (Lean where possible, otherwise an LLM judge).
   - Report a **discovery curve**: hit rate as a function of *k*, for k = 1…K. Passing means the hit rate at k = K is below a threshold calibrated on positive and negative controls.
   - **Contamination control:** use only models whose training cutoff predates the release *and* any source paper of the item (e.g. Meiburg2026).
   - Also record:
     - **pivot**: is the item one step from something in L?
     - **chain depth**: does it pay off only after other new items are in place?

**Downstream speedup test** (decides "confirmed eureka step"):
- Add the item to L.
- Have a prover attempt held-out theorems: other open problems, Mathlib theorems, and other families in this release.
- Compare success under a fixed budget with and without the item.
- An item that only helps its own theorem is a one-off device, not a eureka step.
- **Lean only** (decided 2026-10-09): the test runs in Lean 4 (Mathlib d13f23b plus the OAI library at fd4aeeb, toolchain v4.34.1).
  - An item is eligible only if it exists as Lean declarations that the comparator target depends on. Five N3 items (046, 079, 357, 368, 367) are excluded on this ground; they remain candidates, but cannot be tested in Lean.
  - Each shortlisted item gets a downstream list (`data/pilot/<fid>/downstream.json`, brief `docs/downstream_agent_prompt.md`): speedup targets, open problems and negative controls, each scored for whether it can be stated in Lean now.
  - Corollaries of the item's theorem are recorded separately and do not count as reuse of the device.
- **Informal eureka list** (decided 2026-10-10): N3 items that cannot enter the Lean shortlist (no Lean declarations behind the comparator, or no Lean at all) go in a separate list, `data/eureka_informal.json`.
  - It holds the five `excluded_no_lean` items and the N3 items of the influential-problems pass that lack Lean.
  - These items are graded with the same N-tests at text level. Their discoverability and speedup protocols are written informally (LLM-judge and pen-and-paper), and they never count as confirmed eureka steps.
  - An item moves to the Lean shortlist if it is later formalized.

**Influential-problems pass** (added 2026-10-10): the release's highest-profile results get the full family + novelty analysis whether or not they are formalized, so that the most important claims are not missed by the Lean-only filter.
- Lean-formalized: 103 (L = RL = BPL), 107 (ω ≤ 9/4), 003 (quasi-Riemann hypothesis, zero-free for Re s > 7/8), 293 (hyperinvariant-subspace counterexample) and 158 (the plane is not 5-colorable). Their comparators are compiled locally; eligible N3 items join the Lean shortlist.
- Not formalized: 004 (Hilbert's tenth problem over ℚ), 002 (BSD formula in Selmer coranks 0 and 1) and 074 (Kakeya in R^3 maximal and R^4 dimension). These are analyzed fully, and their N3 items go on the informal list only.
- 102 (Unique Games) already has its analyses; its comparators are compiled in this pass.

**Stratified batch 2** (added 2026-10-12, `data/random_batch_2.json`): one Lean-formalized family per subject, for the 12 subjects with the fewest analysed families, drawn with seed 20261012: 033, 094, 143, 161, 194, 222, 240, 255, 262, 312, 322, 342. Each gets the family and novelty passes; eligible N3 items get a downstream list, then join the Lean shortlist. Per the user (2026-10-12), the release's Lean formalizations are trusted as published (OpenAI would not claim a formalization that does not check), so new families get no Comparator re-checks; `data/lean_checks.json` covers only the families checked before this batch. Lean is still run whenever it yields other information, such as dependency chains, declaration statements or downstream speedup experiments.
- Results (2026-10-12): 7 Lean-backed N3 items join the shortlist at tier 5 (322 C1, 312 C1, 262 C1, 255 C1, 194 C1, 143 E1, 161 C1; confidence 0.35–0.45, all provisional); 033 C1 (adjoint positivity, no Lean behind the comparator) joins the informal list; 094, 240, 342 and 222 are D2. The prover queue grows to 445 tasks (197 runnable now).
- No downstream agent found a strong device-reuse speedup on a known theorem: in every family the known theorems the item reaches are corollaries of its own theorem. Release-wide reuse: 342's closedness theorem is re-proved by 341 for a new criterion (weak device reuse, no Lean); 317 is only an analogue of 312's cylinders; 161's template has one post-release reuse (a second 13-point complex, Codex repo, unverified).
- arXiv re-check (2026-10-12, after arxiv.org was allowed): the decisive precedents were read in full and recorded under `verified_checks` in each novelty.json. No item was downgraded:
  - 255: Peng II §4 (1002.4451) solves the same sub-problem by a measure-vs-length argument, not C1's reflection doubling; C1 0.35 → 0.40.
  - 312: Lanari 2018 and Taylor 2609.20860 have full cylinders only, no partial ones or descending bootstrap; C1 0.35 → 0.45.
  - 262: Read–Schulz 2609.10478 uses a K-free cumulative-mass device, not M_δ; C1 0.40 → 0.45. Read–Schulz is itself AI-assisted ("A first version of the main argument was developed by GPT-6 Astra"), so the γ=1 case of the 1D Lieb–Thirring conjecture was also settled with AI help, 9 days before 262.
  - 033: BFMT 2508.19215 is conditional (Remark 4.8) and needs an effective boundary over the generic point; it neither contains nor implies C1; 0.40 → 0.45.
  - 322: 15 Tingley/Mazur–Ulam full texts use no fixed-point argument like C1; C1 0.45 → 0.50. Tingley 1987 and Ding's survey are not on arXiv and remain unread.
  - 094: the GGNS ChatGPT 5.5 Pro disclosure is verified verbatim.

**Bulk A/B/C pass** (2026-10-12): every one of the 372 families labelled on axes A–C from a short bundle (summary, abstracts, first theorem statements; `scripts/abc_bulk_inputs.py`, brief `docs/abc_bulk_prompt.md`), by 8 cheap agents. Results in `data/abc_bulk/` (`labels_all.json`, `stats.json`, `report.md`, from `scripts/abc_bulk_stats.py`). Agreement with the in-depth labels on 39 families: A κ = 0.77, B κ = 0.79, C κ = 0.44, so A and B are usable release-wide and C is only indicative.

**Calibration items.**
- **Positive control:** Cook's ER extension variables for PHP, formalized as a small Lean or DIMACS example. These must pass tests 2–4.
- **Negative controls:** plumbing definitions and analytic abbreviations from the pilot.
- **173:**
  - The pruning lemma's cost-charging idea is an N3 candidate, F2.
  - The objective M+d is an N3 candidate, F4.
  - Edmonds generic rank, matching and König are **N0 transfer**.
  - The NL=AB matrices are N1.
  - `Counterexample` and `SubsetDeficit` are N1.
- **132:**
  - J is an N3 candidate, F2. Check whether "carry an extra tracked quantity" is a templated strengthening; if so it is capped at N2.
  - The gated predicates are N2 (Meiburg).
  - S_{ℓ,b} is N1.
- **179:**
  - Cyclotomic local rings and Kronecker are **N0 transfer**.
  - Δ(x) is N2 or N3 (F3). This is the borderline case for the judge and the discovery curve.

## Search dynamics from the reasoning traces (CDCL analogy)
The 10 released traces show *how* the model searched. Code each one as a conflict-driven clause-learning (CDCL) search, the way SAT solvers backtrack and restart, so the analogy is recorded quantitatively and not just remarked on.

**Search tree.** Reconstruct the commitments as a tree:
- Level 1 is a top-level strategy (e.g. obstruction vs construction).
- Level 2 is an approach within a strategy.
- Level 3+ is a sub-approach.

Each node records: id, parent, level, description and trace location. It also records **how long it ran before the backtrack**:
- words of trace text, and their share of the trace;
- number of child decisions;
- number of propagation steps;
- number of literature items invoked;
- any explicit time, effort or iteration markers.

These are summary-text proxies, not wall-clock compute.

**Coding scheme.**

| CDCL concept | Trace counterpart | Recorded |
|---|---|---|
| Decision | Committing to an approach | Node at level ℓ |
| Propagation | Forced consequences derived inside an approach | Rough count |
| Conflict | The approach fails | Obstruction type: counterexample / missing estimate / circularity / invariant constant on family / no transport mechanism / other |
| Learned clause | The reusable lesson drawn from the conflict | Text; where it is **reused** later |
| Backjump | Resuming at level k after a conflict at level ℓ | Distance d = ℓ − k. d=1 is chronological; d≥2 is non-chronological |
| Restart | Returning to level 1 and abandoning the strategy | Which learned clauses survive |
| Subsumption (insight-driven backtrack) | An approach is abandoned *not* because it failed, but because a new idea resolves things much more simply | The new idea; **simplification ratio** (remaining work on the old route vs the new route); **origin**: retrieved (points to N0) or constructed (points to N2–N3) |

**Per dead end, record what was learned, in full detail:**
- the precise obstruction;
- the lesson as a clause, with a verbatim excerpt;
- its form: negative result / constraint / salvaged tool / reformulation / sharpened target;
- its generality: local, or rules out a whole class of approaches;
- whether it is a *known* fact (rediscovery, with the reference) or new;
- its correctness;
- what was salvaged and reused;
- its influence on later nodes;
- lessons missed or relearned.

A top-level **knowledge-flow graph** traces how lessons accumulate into the final route. The traces are scarce, so annotate them at maximal detail.

Every backtrack gets a trigger type: **conflict** / **insight** / unclear. Every insight-driven step is an **automatic candidate for novelty grading**. If it survives the N-tests it lands at N2–N3; if it was a retrieved known result it is N0. The simplification ratio is the trace-level counterpart of the step-3b compression check.

**Metrics per trace:**
- number of decisions, conflicts, backtracks (conflict vs insight) and restarts;
- backtrack-distance histogram, split by trigger type, and maximum distance;
- branch length before backtrack (mean, median, list), split by trigger type; the length-vs-distance relation; whether long branches end in restarts;
- maximum depth;
- learned-clause reuse rate;
- **final route conflict-driven?**: is the successful idea traceable to a learned clause?
- fraction of the trace before the final route.

**Link to the eureka-step test.**
- A eureka step reached *after* a restart, with no visible trigger, is evidence of hard discoverability.
- One reached by propagating a learned clause one step is evidence that it was reachable (low pivot distance).

**Ambiguity.**
- Levels are reconstructed, so the level-assignment rules are fixed on trace 287 and then applied to the other 9.
- The traces are curated summaries, so backtracks may be compressed or omitted. Treat the counts as lower bounds.
- Note where the analogy fails, e.g. informal "clauses" and no explicit unit propagation.

## Pipeline
The project lives at `C:\Users\anant\AI-Hard`.

1. **Snapshot**: blobless sparse clone of `openai/math` at `fd4aeeb` into `data/raw/openai-math`, without PDFs. *(done)*
2. **Catalogue** (`scripts/build_catalog.py` → `data/catalog_{families,manuscripts}.csv`)
   - Subject, Lean dirs and comparators, top-level `.tex`, status, trace flag, date.
   - Reconcile 749 dirs against 719 manuscripts.
3. **Extractors** (`scripts/extract_lean.py`, `scripts/extract_latex.py` → `data/items/`)
   - Develop against the three pilot families as the gold set.
   - **3b. Compression check on the pilot items (now, not at the end).**
     - Cheap version: inline each item everywhere it is used and measure the growth of the proof term, both as a tree and as a DAG with sharing. The PHP signature is exponential blow-up when extension variables are unfolded.
     - Expensive version: a prover with and without the item, run only if the cheap version is ambiguous.
     - Goal: test whether the 20% load-bearing proxy tracks actual proof-size reduction.
4. **Codebook pilot 2**
   - 15–20 more families, stratified by subject, including some with no Lean.
   - The user and an LLM label independently. Target κ ≥ 0.6 on axes A–C, then freeze the codebook.
5. **Scaled annotation**: two LLM passes, a JSON schema, evidence quotes, and human review of disagreements.
6. **Objective cross-checks**:
   - Lean quantifiers vs axis A.
   - Lean imports vs method fields.
   - Invoked theorems vs the bibliography's MSC codes.
7. **Novelty grading**: tests 1–4 on the filtered candidates, then F labels for the N3 items.
8. **Analysis**
   - Axis distributions and cross-tabs.
   - The field-flow matrix.
   - D3 rate and the F-type mix by subject.
   - Discovery curves.
   - A process study of the 10 traces, including CDCL search-dynamics metrics compared across traces and against each trace's eureka candidates.
9. **Downstream speedup test** on N3 items, plus Mathlib knockout validation on historical eureka steps.

## Working hypothesis: scaled-up resolution (informal, 2026-10-10)
This is an analogy, not yet a formal definition.
- **The formula is all of mathematics.** Each field is a set of clauses: its theorems and named concepts. The whole formula is their union.
- **Resolution** is any step that combines existing clauses, from any field. Cross-field transfer is still resolution: a resolvent whose two premises come from different fields.
- **A jump** is an extension: a concept from outside the existing vocabulary that, once named, helps resolve things already in mathematics.
  - The line is drawn at the literature's vocabulary, not at definability from primitives. Everything is definable from primitives, including Cook–Reckhow's extension variables (x ↔ a ∧ b). What makes those an extension is that they are new names whose introduction shortens other proofs.
  - Mapping to the codebook: N0–N2 are resolution steps, N3 is a candidate extension, and the downstream speedup test separates a real extension from a local abbreviation.
- **Claim, as of 2026-10-10.** The model behaves like resolution scaled to the whole formula, bridging all of mathematics at once in a way no human can. No extension has been confirmed: every step is N0–N2, or an N3 candidate not yet shown to shorten anything else.
  - Supporting: wide cross-field resolvents (004 logic ↔ heights, 075 information theory ↔ Carleson, 158 spectral rigidity ↔ colouring, 107 representation tensors ↔ complexity). Analysts repeatedly find that "new" items are new combinations of precedented parts. For 103, the best downstream targets were corollaries, not reuse of the device.
  - Falsifier: any N3 device that passes the speedup test on a theorem other than its own. The prover queue (`data/prover_tasks.json`) is that experiment.
  - Weakening evidence to track: device reuse across the model's own manuscripts (e.g. 002's Heisenberg-commutator choice in all three BSD papers, 271's splice, 107's separation lemma). Count it release-wide.
    - The strongest case so far (found 2026-10-10): 003's sextic-twist duality is reused by family 029 to claim Artin's primitive root conjecture for base 2. That is a different famous problem, so it is a device reused across problems, not a corollary. Whether 029 needs the device or only 003's theorem is the deciding check (its downstream target 2).
- **Prediction (not a finding).** Had humans resolved this set of problems, over perhaps 100–150 years, they would very likely have produced reusable frameworks along the way, as Wiles's R = T, Gowers's higher-order Fourier analysis and Perelman's surgery did. Revisit in 12–24 months: does any model device enter the human literature or Mathlib as a named tool?

## Caveats
- The "how" labels describe the written proof, not the search that found it.
- Results are unreviewed. Drop withdrawals and track revisions.
- Lean covers about 42% of top-line results, so the formalized subset may be biased.
- Model-produced "prior literature" blurs novelty. Use the provenance flag.
- Comparator targets can be weaker than the headline claim. Record both.
- Eureka status is **relative to L**. Cook's induction is routine in ordinary mathematics and a eureka step only relative to resolution's language. Always report which L was used.

## Verification
- The catalogue reproduces 372 families, 719 manuscripts, about 300 formalized and 3 withdrawn.
- The extractors recover every pilot gold item, lemmas included, and filter out plumbing.
- κ ≥ 0.6 on axes A–C; a 10% hand-check of scaled annotations.
- The PHP positive control passes tests 2–4. The negative controls fail at least one test.
- The pilot gold items land in their expected grades and F types. Δ(x) and J are reviewed by hand.
- The step-3b compression results are reported against the load-bearing proxy. If they disagree, *k* is recalibrated or the proxy is replaced.

**Release-wide v2 labels, Lean scope check and proof lengths** (2026-10-15): the v2 A/B labels for all 372 families (`data/abc_v2/`), the Lean scope check of the 67 families whose Lean differs from the headline (`data/lean_scope/report.md`; 6 `lean_vs_headline` labels corrected), and PDF page counts for all 719 manuscripts plus Lean lines per family (`scripts/proof_lengths.py` → `data/proof_lengths.json`; PDFs fetched one at a time from raw.githubusercontent.com, never stored) are on the atlas's *Release labels* tab, built by `scripts/build_release_datasets.py` (datasets `release_labels`, `label_stats`, `lean_scope`).
Proof-only length: `scripts/proof_text_lengths.py` measures the text inside proof environments (main .tex resolved through \input/\include), converted to pages per manuscript; written into `data/proof_lengths.json` and shown on the atlas.
Technical-body length (everything except front matter, introduction / conclusion / discussion-type sections and the bibliography) is also in `data/proof_lengths.json`. Human baseline: `scripts/frontier_lengths.py` applies the same measures to 71 well-known human frontier papers across fields from arXiv (`data/frontier_lengths.json`). Compare technical pages, not proof-environment pages: many human authors write proofs as plain "Proof." paragraphs, which the proof-environment count misses.
Reproducible baseline (option 1, 2026-10-16): `scripts/annals_candidates.py` builds the frame of Annals of Mathematics papers, volumes 183–202 (2016–2025), whose arXiv entry carries the journal reference (53 papers; arXiv's HTML search is the only bibliographic source reachable here), and `scripts/annals_baseline.py` measures them (`data/annals_lengths.json`). `scripts/length_by_field.py` compares the release with both baselines. A complete Annals frame needs api.openalex.org or api.crossref.org in the network allowlist.
Discoverability test for 304 (P-C1C2, scaled down): `data/pilot/304/discoverability/` (prompts, 36 samples, two blind judges, report.md).
