# Family 103: Exact derandomization of logarithmic space, L = RL = BPL

FAMILY analysis of the paper and the Lean, done at text level. This agent did not build the Lean; the orchestrator compiles the comparator. Corpus: `openai/math` at fd4aeeb. Manuscript: `preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/` (13 sections, 8,533 TeX lines). There is no reasoning trace. Machine-readable version: `family.json` (31 items).

## 1. Main statement
- **Paper** (`sections/introduction.tex:28-51`):
  - Thm 1.1: L = RL = BPL.
  - Thm 1.2: a deterministic algorithm approximates the acceptance probability p_M(x) of any poly-time logspace randomized machine to within 2^-q. It uses O(log n + q) space and (n+2)^{O(1)} 2^{O(q)} time, and needs **no gap promise**.
- **Comparator**: `ComparatorChallenges/LogspaceEquality.lean` proves `OAI.ExactDerandomization.exact_logarithmic_space_derandomization : L = RL ∧ RL = BPL`. Permitted axioms are propext, Quot.sound and Classical.choice.
- **The model.** Explicit machines with:
  - h two-way read-only input heads with endmarkers;
  - w binary work tapes indexed by Z;
  - one fresh coin per step.

  Space is the number of distinct work cells visited, on every coin tape and at every t, bounded by c·clog2(n+2). RL and BPL require halting within c(n+2)^k on all coin tapes, and an exact rational acceptance probability with thresholds 1/2 and 0, or 2/3 and 1/3.
- **Match check.**
  - The 20 comparator definitions are textually identical to `OAI/Computability/Logspace/Deterministic.lean`.
  - The model is the standard one: multi-head input is equivalent to single-head logspace.
  - I found no loophole. The class equality matches the paper exactly.
- **Not formalized:**
  - Thm 1.2 with its explicit variable-precision bounds;
  - PromiseBPL = PromiseL;
  - certified accepting runs;
  - the effective compiler (as `lean/docs/103.md` states).

## 2. Trust surface (text-level grep over all 39 files, 43,045 lines)
- None of the following appear: `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, the `opaque` keyword, `ofReduceBool`, `partial def`.
- The only imports are Mathlib (plus `Mathlib.NumberTheory.Bertrand`) and the family's own files.
- There are 65 `decide` uses, all on small Bool/Prop facts, and 38 raised `maxHeartbeats`.
- Identifiers are code-named (Rock, Umbra, Folk, Helix…). This is not a trust issue, but it makes auditing hard.
- **Compile status: pending (orchestrator).** If the comparator builds with only the permitted axioms, BPL ⊆ L is machine-checked.

## 3. Labels
| Axis | Label | Conf. | Evidence |
|---|---|---|---|
| A | **A4** (class equality). Hard direction is A1: for every BPL machine there exists a deterministic decider. The explicit-rate flag is set (Thm 1.2) | 0.75 | intro.tex:28-51 |
| B | **B1**: resolves the AKLLR 1979 question. Adds corollaries: PromiseBPL = PromiseL, approximation without a gap promise, certified runs, compiler | 0.85, conditional on correctness | intro.tex:75-79 |
| C | **C1** primary: an explicit estimator, then enumerate environments and take the median. Secondaries: C2 (well-founded induction over stages and budgets), C4 (moment chains), C5 (Shalom, Riesz–Thorin and Bertrand cited, in the paper only) | 0.7 | intro.tex:255-273 |
| C2 flags | ih_strengthened = **yes**. The induction proves an integrated L_s bound for every task and every retained vertex, plus a coupled actual-vs-clean discrepancy. Template: uniform/quantitative version, plus carry an extra tracked quantity | 0.6 | fingerprints.tex:614-752 |
| Computer-assisted | **no** | 0.95 | |
| D | **D3 (provisional)**: the correction-and-copy hierarchy and the slack-telescoped estimator | 0.45 | |
| Provenance | **no** model-produced precedent among the cited 2026 works (checked from search snippets only) | 0.7 | |

**E: fields.**
- Problem field: TCS (MSC 68Q15, 68Q87).
- Lean dir: Computability.
- Method fields:
  - linear algebra / preconditioning;
  - sampling / probability;
  - **group theory**: property (T) and relative (T) via Shalom, in the paper only;
  - harmonic analysis (Riesz–Thorin);
  - expanders;
  - algebraic fingerprinting (paper only);
  - catalytic computing;
  - logspace traversal (Cook–McKenzie, LMT);
  - redundant-digit arithmetic;
  - Bertrand's postulate.
- About 8 cross-field method fields; roughly 60% of the invoked external theorems are non-TCS.

## 4. Proof architecture
1. **Configuration reduction.** p(x) = ((I−S)^{-1}e)(x0), with S strictly forward, substochastic, and with bounded-degree paired ports.
2. **Correction-and-copy hierarchy** (Sec. 3). At each stage:
   - The pilot detectors U_i(y) choose a column multiplier g. U_i(y) is the rank-J order statistic of row-gated scores over a sampled set of rows.
   - k_* fixed iterations of the soft-threshold correction E = fQ((C+EC)/f)g are applied. The factorial truncation bound makes k_* independent of n.
   - The residual is D = C − E + EC. Then I − D = (I+E)(I−C), so the removed transition mass moves into the reward.
   - Copies split the remaining large entries over D0 children. The maximum entry drops by 2^H while the active vertex count at most doubles.

   The reward recursion is W_{l+1} = r(W_l + E_l W_l). After L = O(log n) stages, 0 ≤ p0(x) − W_L(primary copy) ≤ |V0|·2^{-(H−1)L}.
3. **Stochastic atoms** (Sec. 5). Matrix entries become row-bounded sampled tables with *exact* conditional-mean identities, in one shared O(log n)-bit environment of rank channels. A rank channel is a frame-conditioned random polynomial hash with box retention.
4. **Conditional averaging** (Sec. 6). An affine SL_H(Z) ⋉ Z^H walk on each retention slice has a uniform spectral gap (Shalom's property (T), then Riesz–Thorin). Validated variants let a walk be specified before its conditioned endpoint is known.
5. **Additive estimation** (Sec. 7).
   - Average differences of child estimates at consecutive budgets m and m−1, using walks of length ∝ slack M−m.
   - Means telescope, and noise contracts as 2^{-p−K_n d}.
   - An immediate path costs O(slack) bits.
6. **Compression** (Sec. 8). Each prefix is compressed to a default-plus-exceptions list, with first-overflow charging.
7. **Fingerprints** (Sec. 9).
   - Short Schwartz/Carter–Wegman keys are used within budget blocks.
   - A coupling with a block-clean calculation gives the integrated 8th-moment bound (Thm fp-estimators).
   - A catalytic 4-excursion equality test avoids storing a key index in each frame.
8. **Implementation** (Secs. 10–11).
   - Digit-query arithmetic and a single cursor.
   - Inverse ports by contour traversal (Cook–McKenzie / LMT).
   - Allowance potential Φ = Aw + Dt: the space of each frame telescopes along the call chain, giving O(log n) in total.
9. **Final step** (Sec. 12). Condition on the start; the factor N this costs is paid by p = Θ(B). Then enumerate environments, take the median and threshold at 1/2. Padding gives variable precision, and Sec. 13 builds the compiler.

## 5. Lean structure
- 6,077 declarations; 5,166 are in the comparator's proof DAG.
- The **mathematical core** is 1,398 DAG declarations (27%), about 32% of DAG lines. The core files are ProbabilityHierarchy, ProbabilityAtoms, AffineSampling, Estimator*, CompressionBounds, HierarchicalEstimator, IterationSchedule and ProbabilityDecision. The remaining ~70% is machine, program, arithmetic and traversal plumbing.
- `residual`, `substochastic` and `factorial` (ProbabilityHierarchy.lean:179-277) each have about 35% of the whole DAG downstream (912 dependents).
- Dominated shares: `fixed_precision_estimator` 0.63, `Umbra.Scope.Sane.bells0` 0.38, `Grain.Rock.convince` 0.15, `Net.error_estimate` 0.12.

**The Lean route differs from the paper's in three places** (text-level; worth flagging):
1. It uses **fourth** moments (s = 4), where the paper uses eighth (AffineSampling.lean:15-18).
2. Mixing comes from "an elementary Fourier proof of a square torus gap ... without assuming a property-(T) result" (AffineSampling.lean:723-727). This is a Gabber–Galil/Margulis-style shear argument, not Shalom's.
3. There are **no fingerprint, hash or collision declarations**. `CatalyticComparison.lean` does "Deterministic catalytic ID comparisons" digit by digit. The paper's Sec. 9 adaptive-fingerprint coupling seems to have no Lean counterpart.

So Secs. 6 and 9 of the paper are not themselves certified by the Lean.

## 6. Items
Full list in the JSON, I01–I31. Summary of provisional N:
- **N0:**
  - I01 (vocabulary), I02 (configuration reduction), I05 (sampling estimates);
  - I15 (sparse default representation);
  - I16 (property-(T) gap, a transfer), I22 (fingerprints), I24 (catalytic equality), I27 (contours).
- **N1:**
  - I03, I04 (rank channel, a polynomial hash), I06 (the preconditioning identity itself), I10, I14, I18, I19;
  - I25 (arithmetic), I26, I29, I30, I31.
- **N2:** I07 (soft-threshold correction), I08 (factorial truncation), I09 (detectors), I13 (atoms; the paper itself relates them to weighted PRGs), I17 (validated walks), I21 (compression), I23 (fingerprint coupling), I28 (allowance potential).
- **N3 candidates:** I11 + I12 (the copy step and the shallow reward hierarchy), and I20 (slack-telescoped multilevel estimator).

## 7. Eureka candidates (provisional; full grading is in novelty.md)
1. **Correction-and-copy hierarchy** (I06 + I07 + I09 + I11 + I12). Provisional N3, F5/F1.
   - What it does: it turns a poly-length chain into O(log n) stages via the potential "max entry × active vertices", and invents vertex sets V_l with rewards W_l. These occur nowhere in the goal.
   - Neighbours: Richardson / (I+S) preconditioning (CDRST21, AKMPSV20, CDST23), graph lifts, and sampling-based heavy-column detection.
   - Against: on its own it does not beat log² n.
2. **Slack-telescoped shared-environment estimator** (I20). Provisional N3, F3.
   - What it does: per-level cost O(slack) rather than O(log n).
   - Neighbours: multilevel Monte Carlo (Giles 2008), and CDST23's precision-alternating recursion, which also avoids paying log n per level.
3. **Allowance potential** (I28). N2.
4. **Detectors** (I09). N2.
5. **Fingerprint clean-block coupling** (I23). N2, and not backed by the Lean.

Quick searches found no equivalent of candidates 1 and 2. These are snippet-level only; WebFetch is unavailable.

## 8. Correctness and trust concerns
- This is an extraordinary, unrefereed claim. Searches on 2026-10-10 found no public expert reaction.
- What I checked by hand:
  - the hierarchy algebra and the copy-step counting;
  - factorial truncation;
  - the one-start Markov step;
  - comparator faithfulness.
- Secs. 7–11 were read at the level of statements and proof sketches. They make many "sufficiently large constant" choices, ordered in conclusion.tex:38-112.
- **Trust therefore rests on the comparator build.** Lean and paper diverge in parts (s, the mixing proof, fingerprints). Even if the build succeeds, it certifies the theorem, not every section of the paper.
- Extraction friction:
  - Code-named Lean identifiers.
  - The extractor misses tactic-internal links: `slice_gap` and `U_heavy` are reported outside the DAG but are used.
