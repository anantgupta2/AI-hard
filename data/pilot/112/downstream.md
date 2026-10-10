# Family 112: downstream targets for the clause-count-free restriction lemma

Analyst role: downstream. Date: 2026-10-09. Machine-readable version: `downstream.json`.

**How this was done.**
- Text level only. The Lean was not compiled.
- The web precedent searches, rate-limited in the first pass, were **rerun on 2026-10-10**: 38 WebSearch queries, none rate-limited, plus a GitHub repository search.
- WebFetch reached github.com but failed with DNS errors for arXiv, ECCC, lacker.io and mathweb.ucsd.edu, so some literature checks rest on abstracts and search snippets. See Precedent below.

## Part A: is the item in the Lean?

**lean_status: as in paper.**
- `cnf_restriction_bound` (Restriction.lean:59) is Lemma 2.1 verbatim in shape:
  - W depends only on H and the restriction;
  - `restrictionAvg p W ≤ 1/(1−θ)`, with the paper's θ;
  - `|E G·H_σ| ≤ W·corr_b G` for every real G.
- The proof follows the paper's four steps:
  - violation-path expansion (`indexedCNF_restriction_expansion`);
  - marker mixture;
  - reweighting;
  - backward counting (`restrictionAvg_pathCost_le`, `reverseTheta`).

**Chain from the comparator to the item.**
`exists_polynomial_time_language_depth_three_lower_bound` → `language_depth_three_gate_lower_bound` → `exists_language_slice_small_correlations` (+ `circuit_lower_bound_of_small_cnf_correlations`) → `wide_correlation_of_good_restrictions` → `restrictionAvg_cnfRestrictionCost_le_two` + `cnf_restricted_correlation_le_cost` → `restrictionAvg_restrictionCost_le` / `restricted_correlation_le_cost`.

**Gaps.**
- No mathematical gap was found. The comparator uses the θ ≤ 1/2 form; the general 1/(1−θ) form is also proved.
- **Useful for the speedup test:** `wide_correlation_of_good_restrictions` and `circuit_lower_bound_of_small_cnf_correlations` are *generic in f*. So the device can be reused on other functions without touching the language code.
- But the counting lemma hard-wires the ω(√n) constants. A c·√n target such as parity needs a re-parametrised copy.

**Size.**
- The restriction cluster is 4,238 of 25,007 Lean lines.
- Turing-machine plumbing is 12,740 lines.

**Switching-lemma formalizations.**
- **Updated 2026-10-10:** formalizations exist, all outside Mathlib and outside the release.
  - **arXiv 2609.24188**, "Formalizing PARITY Circuit Lower Bounds in Lean" (Sept 2026).
    - From search snippets, it states Håstad's lemma (O'Donnell's form) as a ratio of bad restrictions to all restrictions, using Mathlib `countP`.
    - The constant is 10 under a rounding hypothesis, 40 without.
    - The full text could not be fetched, so whether it includes a depth-3 parity bound is unknown.
  - **github.com/codula-code/SwitchingLemma** (created 2026-09-03).
    - Core Lean 4, no Mathlib, toolchain v4.33.1.
    - Proves Håstad 2014 Lemma 3.3: Pr[DT depth ≥ h] ≤ (10wε)^h for width-w DNFs, plus a conditional version.
    - The README claims no sorry and only the standard axioms. Not verified here.
  - **github.com/Quantyra/formal-switching-lemma** (v0.10.0, Lean v4.13.0; cited in 2609.24188 as Fredriksen's).
    - A SimpleDNF switching lemma (`switchingLemmaTermSimple_proved`) with CNF duals and layer schedules.
    - It disclaims a general PHP switching lemma.
  - No Isabelle AFP or Coq entry was found. Bounded-arithmetic formalizations (APC1; Krajíček, PV1+WPHP) exist but are not proof-assistant code.
- Mathlib d13f23b still has no circuit-complexity library. There is no local checkout to grep.
- The depth-3 parity and depth-hierarchy targets below were updated to name these comparator candidates (on other toolchains than the pinned v4.34.1).
- The release itself never formalizes a switching lemma. DepthThree avoids it.

### Verbatim Lean declarations
See `downstream.json → lean_source` for the full text. Entries:

- `OAI.DepthThreeLowerBound.Circuit3` (structure), `OAI/Computability/DepthThree/Model.lean:39`
- `OAI.DepthThreeLowerBound.Restriction / Live` (abbrev), `OAI/Computability/DepthThree/FiniteProbability.lean:19`
- `OAI.DepthThreeLowerBound.restrictionAvg` (def), `OAI/Computability/DepthThree/FiniteProbability.lean:135`
- `OAI.DepthThreeLowerBound.corr` (def), `OAI/Computability/DepthThree/RestrictionCorrelation.lean:50`
- `OAI.DepthThreeLowerBound.pathWeight / pathCost / restrictionCost` (def), `OAI/Computability/DepthThree/RestrictionPathData.lean:61`
- `OAI.DepthThreeLowerBound.restrictionTheta` (def), `OAI/Computability/DepthThree/Restriction.lean:17`
- `OAI.DepthThreeLowerBound.cnfRestrictionCost` (def), `OAI/Computability/DepthThree/Restriction.lean:30`
- `OAI.DepthThreeLowerBound.cnf_restricted_correlation_le_cost` (theorem), `OAI/Computability/DepthThree/Restriction.lean:37`
- `OAI.DepthThreeLowerBound.cnf_restriction_bound` (theorem), `OAI/Computability/DepthThree/Restriction.lean:59`
- `OAI.DepthThreeLowerBound.restrictionAvg_cnfRestrictionCost_le_two` (theorem), `OAI/Computability/DepthThree/Restriction.lean:71`
- `OAI.DepthThreeLowerBound.indexedCNF_restriction_expansion` (theorem), `OAI/Computability/DepthThree/RestrictionCostCorrelation.lean:124`
- `OAI.DepthThreeLowerBound.restrictionAvg_restrictionCost_le` (theorem), `OAI/Computability/DepthThree/RestrictionExpectedCost.lean:163`
- `OAI.DepthThreeLowerBound.wide_correlation_of_good_restrictions` (theorem), `OAI/Computability/DepthThree/WideCorrelation.lean:17`
- `OAI.DepthThreeLowerBound.circuit_lower_bound_of_small_cnf_correlations` (theorem), `OAI/Computability/DepthThree/CircuitQuantitative.lean:10`
- `OAI.DepthThreeLowerBound.exists_polynomial_time_language_depth_three_lower_bound` (theorem), `OAI/Computability/DepthThree/Main.lean:8`

## Part B: speedup targets (known theorems)

### S1. Depth-3 parity lower bound 2^{Omega(sqrt n)} (Håstad 1986/89; PPZ99 sharp form)
- **Statement:** Every OR-AND-OR circuit computing parity of n bits has 2^{c·sqrt n} gates for some absolute c > 0 (sharp: Theta(n^{1/4} 2^{sqrt n}), PPZ99).
- **Reference:** J. Håstad, 'Almost optimal lower bounds for small depth circuits', STOC 1986 / Computational limitations of small-depth circuits (MIT Press 1987), cited as H89; Paturi-Pudlák-Zane, 'Satisfiability coding lemma', Chicago J. TCS 1999, Thm 6; HJP95 Thm 3.3.
- **Status:** known theorem
- **Current proof size:** Switching-lemma route: about 8-10 pages including the switching lemma. PPZ route: about 3-4 pages. No Lean formalization known (see switching_lemma_formalizations).
- **How the item helps:** With C1 and the f-generic Lean skeleton (wide_correlation_of_good_restrictions plus a re-parametrised circuit_lower_bound_of_small_cnf_correlations), the only new ingredient is a parity-vs-narrow-CNF correlation bound corr_b(parity on m live vars) <= 2^{-Omega(m/b)}. That bound is expected true but was NOT verified here, and the paper does not state it. Taking b = O(1) and pk a small constant gives 2^{c sqrt n}. This replaces the switching lemma by C1. It would not beat the short PPZ argument, so the gain is mainly against the switching-lemma route.
- **Expected speedup:** medium vs switching-lemma route; low vs PPZ
- **Confidence:** medium
- **Lean:** statable now. Needs: OAI DepthThreeLowerBound: Circuit3, Circuit3.Computes, gateCount, CNF, CNF.WidthAtMost, finiteAvg, sign, indicator, corr, Restriction, restrictionAvg; parity as fun x => decide (Odd (card {i | x i})). Missing: none for the statement; proof needs a parity/narrow-CNF correlation lemma (~150-300 lines) and a re-parametrised counting lemma (~100-200 lines). Formal proof to compare (updated 2026-10-10): switching-lemma formalizations exist outside Mathlib (arXiv 2609.24188; codula-code/SwitchingLemma; Quantyra/formal-switching-lemma), on other toolchains; no PPZ formalization known.

### S2. PPSZ05 code-membership depth-3 lower bound ((pi/sqrt 6)·sqrt n exponent)
- **Statement:** Membership in suitable codes requires depth-3 circuits of size 2^{(pi/sqrt6 - o(1)) sqrt n}.
- **Reference:** Paturi-Pudlák-Saks-Zane, 'An improved exponential-time algorithm for k-SAT', JACM 52 (2005), Thm 6 (as cited in 00_introduction.tex).
- **Status:** known theorem
- **Current proof size:** a few pages on top of the PPSZ isolated-solution analysis (about 20 pages); no formalization.
- **How the item helps:** C1 gives a correlation route to some 2^{c sqrt n} bound for any function whose random restrictions have b-independent correlation decay against narrow CNFs. Code membership with large dual distance is a candidate. It cannot recover the sharp constant pi/sqrt6, because C1's constants are crude.
- **Expected speedup:** low
- **Confidence:** low
- **Lean:** statable with < 300 lines of new definitions. Needs: OAI DepthThreeLowerBound: Circuit3, Circuit3.Computes, gateCount, CNF, CNF.WidthAtMost, finiteAvg, sign, indicator, corr, Restriction, restrictionAvg. Missing: linear codes / dual distance on Fin n -> Bool (~100 lines; Mathlib has basic coding-theory pieces only). Formal proof to compare: none.

### S3. Bounded independence fools CNFs (Bazzi 2009; Razborov's simplified proof)
- **Statement:** Every polylog(m/epsilon)-wise independent distribution epsilon-fools every m-clause CNF.
- **Reference:** L. Bazzi, 'Polylogarithmic independence can fool DNF formulas', SICOMP 38 (2009); A. Razborov, 'A simple proof of Bazzi's theorem', ACM TOCT 1 (2009).
- **Status:** known theorem
- **Current proof size:** Razborov: about 5 pages; no formalization known.
- **How the item helps:** Speculative. C1 says a randomly restricted wide CNF is, in the dual (correlation) sense, an O(1)-mass mixture of width-b CNFs, with no dependence on the number of clauses. If width-b CNFs are fooled by O(b)-wise-independent restrictions, a clause-count-free fooling statement could follow. But Bazzi's bound depends on m only polylogarithmically, and fooling needs the distribution itself, not a random restriction, so the fit is weak.
- **Expected speedup:** low
- **Confidence:** low
- **Lean:** statable with < 300 lines of new definitions. Needs: CNF, finiteAvg; Mathlib PMF. Missing: k-wise independent distributions on the cube (~120 lines). Formal proof to compare: none.

### S4. Håstad's depth-d AC0 parity lower bound exp(Omega(n^{1/(d-1)}))
- **Statement:** Depth-d unbounded fan-in circuits computing parity need size exp(Omega(n^{1/(d-1)})).
- **Reference:** Håstad 1986/89 (switching lemma); Rossman's entropy proof of the switching lemma (2017, cited in novelty.json); Håstad-Rossman-Servedio-Tan (JACM 2017) average-case depth hierarchy.
- **Status:** known theorem
- **Current proof size:** about 10-15 pages including the switching lemma; no Lean formalization known.
- **How the item helps:** Probably none. The switching lemma converts CNFs into DNFs, so layers can be collapsed and the argument iterates. C1 only bounds correlations, and its output is still a CNF mixture, so it cannot collapse a depth-4 middle layer, which is a DNF of CNFs. This is a boundary test of whether a prover over-applies C1.
- **Expected speedup:** low (expected none)
- **Confidence:** medium
- **Lean:** statable with < 300 lines of new definitions. Needs: CNF/Clause from DepthThree. Missing: general depth-d circuit inductive type and size (~150 lines). Formal proof to compare: arXiv 2609.24188 (Formalizing PARITY Circuit Lower Bounds in Lean, Sept 2026) is the closest candidate; its depth-d coverage is unverified (updated 2026-10-10).

## Open or new problems

### O1. An explicit function with depth-3 complexity 2^{n^{1/2+epsilon}} (HJP95 Problem 2)
- **Statement:** Find an explicit f with S_3(f) >= 2^{n^{1/2+epsilon}} for a fixed epsilon > 0.
- **Reference:** Håstad-Jukna-Pudlák, 'Top-down lower bounds for depth-three circuits', Comput. Complexity 5 (1995), Sec. 5 Problem 2; GPPST24 Sec. 1.1; GKPRT26 (arXiv 2601.04446). (https://arxiv.org/abs/2601.04446)
- **Status:** open
- **Obstruction match:** Exact match of the barrier C1 partly breaks. C1 needs pk = O(1) for a constant b. At width k ~ n^{1/2+epsilon} this forces p ~ n^{-1/2-epsilon}, so the live set m ~ n^{1/2-epsilon} is smaller than k and the slice correlation 2^{-m/16} cannot beat 2^{-k}. Letting pk grow forces b to grow, and the sparse partition then becomes tower-sized.
- **Adaptation:** Either a version of C1 with E W <= 2 for pk = n^{delta} at b = n^{O(delta)}, or slices whose corr_b decays like 2^{-m·g(b)} with g growing.
- **Payoff / confidence / difficulty:** very high / low / very high
- **Lean:** statable now. Needs: OAI DepthThreeLowerBound: Circuit3, Circuit3.Computes, gateCount, CNF, CNF.WidthAtMost, finiteAvg, sign, indicator, corr, Restriction, restrictionAvg; TM model from DepthThree (MultiTapeHaltsIn) for explicitness. Missing: none. Formal proof to compare: none.

### O2. Valiant's depth-3 program: 2^{omega(n/log log n)} for an explicit function
- **Statement:** An explicit f with S_3(f) >= 2^{omega(n/log log n)} would rule out linear-size logarithmic-depth circuits for a related function.
- **Reference:** L. Valiant, 'Graph-theoretic arguments in low-level complexity', MFCS 1977; surveyed in GPPST24. (https://doi.org/10.1007/3-540-08353-7_135)
- **Status:** open
- **Obstruction match:** Same correlation-decay obstruction, far more extreme.
- **Adaptation:** None concrete; listed for completeness.
- **Payoff / confidence / difficulty:** very high / very low / extreme
- **Lean:** statable now. Needs: OAI DepthThreeLowerBound: Circuit3, Circuit3.Computes, gateCount, CNF, CNF.WidthAtMost, finiteAvg, sign, indicator, corr, Restriction, restrictionAvg. Missing: none for the depth-3 statement (the Valiant implication would need a general circuit library). Formal proof to compare: none.

### O3. Effective rate: an explicit omega(1) factor
- **Statement:** Give an explicit unbounded g (e.g. iterated log) with S_3(f_n) >= 2^{g(n) sqrt n} for an explicit language.
- **Reference:** Open question 3 in data/pilot/112/novelty.md; the paper's omega is ineffective (b(A), M(b,1/8) tower-like).
- **Status:** open
- **Obstruction match:** C1 itself is effective: theta is explicit and E W <= 2. The loss is in the sparse-partition count M(b, eta) from Erdős-Rado, which C1 makes necessary by pushing b up.
- **Adaptation:** Replace Erdős-Rado sparsification with a sunflower bound à la Alweiss-Lovett-Wu-Zhang (2020) in SparsePartition.lean, then track b(A) explicitly.
- **Payoff / confidence / difficulty:** medium / medium / medium
- **Lean:** statable now. Needs: OAI DepthThreeLowerBound: Circuit3, Circuit3.Computes, gateCount, CNF, CNF.WidthAtMost, finiteAvg, sign, indicator, corr, Restriction, restrictionAvg; Real.sqrt, Real.logb. Missing: none. Formal proof to compare: partial: the existing ineffective proof.

### O4. A natural explicit function without advice-style parameter bits
- **Statement:** Prove 2^{omega(sqrt n)} for a natural function (e.g. a fixed polynomial evaluation, a Paley/quadratic-character function, or a function in NP) instead of a language whose hard slice is chosen by the probabilistic method and supplied through input bits.
- **Reference:** GKPRT26 Sec. 1 (problem still listed open); PSZ00 Sec. 5 (input-index trick). (https://arxiv.org/abs/2601.04446)
- **Status:** open
- **Obstruction match:** C1 transfers the problem to finding f whose random restrictions have corr_b <= 2^{-cm} with c independent of b. Any explicit function with that pseudorandomness property works, through the generic wide_correlation_of_good_restrictions.
- **Adaptation:** Test candidate functions with small-bias or k-wise independent restrictions (e.g. Nisan-Wigderson or quadratic-residue-based) for the good-restriction property, using the IPZ01 moment method in HardSliceMoment.lean.
- **Payoff / confidence / difficulty:** high / low-medium / high
- **Lean:** statable now. Needs: OAI DepthThreeLowerBound: Circuit3, Circuit3.Computes, gateCount, CNF, CNF.WidthAtMost, finiteAvg, sign, indicator, corr, Restriction, restrictionAvg; goodRestriction (HardSliceSelection.lean:63). Missing: definition of the candidate function (~50-150 lines). Formal proof to compare: the paper's slice proof as template.

### O5. Average-case version: depth-3 correlation bounds beyond sqrt n
- **Statement:** An explicit f such that every OR-AND-OR circuit of size 2^{A sqrt n} agrees with f on at most a 1/2 + o(1) fraction of inputs, for every A.
- **Reference:** Natural strengthening; cf. correlation bounds for AC0 (Håstad 2014 SICOMP; Impagliazzo-Matthews-Paturi SODA 2012).
- **Status:** open (to the analyst's knowledge)
- **Obstruction match:** C1 already gives correlation control for each middle CNF. The present counting step uses exactness (gH = H for middle gates of an exact OR), so it fails for approximate computation.
- **Adaptation:** Bound the correlation of an OR of S CNFs by inclusion-exclusion truncation or a Fourier argument over the middle layer; each term is again a CNF and C1 applies.
- **Payoff / confidence / difficulty:** medium / low-medium / medium-high
- **Lean:** statable now. Needs: OAI DepthThreeLowerBound: Circuit3, Circuit3.Computes, gateCount, CNF, CNF.WidthAtMost, finiteAvg, sign, indicator, corr, Restriction, restrictionAvg. Missing: none. Formal proof to compare: none.

### O6. Pseudorandom version of C1 and PRGs for depth-3 circuits
- **Statement:** Does C1 hold (E W = O(1)) when the restriction is drawn from a k-wise independent or small-bias family? If so, does it yield improved PRGs for depth-3 or CNF-of-CNF circuits, in the Trevisan-Xue / Servedio-Tan pseudorandom switching-lemma line?
- **Reference:** Trevisan-Xue, 'A derandomized switching lemma and an improved derandomization of AC0', CCC 2013; Servedio-Tan, 'Improved pseudorandom generators from pseudorandom multi-switching lemmas', RANDOM 2019. Titles from memory.
- **Status:** open (new question)
- **Obstruction match:** The C1 proof uses full independence in the reweighting step (sample y first, then mask) and in the backward count. That is exactly where the pseudorandom switching lemmas pay their cost.
- **Adaptation:** Check whether restrictionAvg_pathCost_le only needs O(k·j)-wise independence of the mask on each path's revealed set.
- **Payoff / confidence / difficulty:** medium / low / medium-high
- **Lean:** statable with < 300 lines of new definitions. Needs: OAI DepthThreeLowerBound: Circuit3, Circuit3.Computes, gateCount, CNF, CNF.WidthAtMost, finiteAvg, sign, indicator, corr, Restriction, restrictionAvg. Missing: k-wise independent restriction families (~150 lines). Formal proof to compare: none.

### O7. Res(k) lower bounds for k >= log n
- **Statement:** Superpolynomial lower bounds for k-DNF resolution refutations of natural formulas when k = Omega(log n).
- **Reference:** Segerlind-Buss-Impagliazzo, FOCS 2002 / SICOMP 2004; A. Razborov, 'Pseudorandom generators hard for k-DNF resolution and polynomial calculus resolution', Annals of Math. 181 (2015). (https://mathweb.ucsd.edu/~sbuss/ResearchWeb/resK/focs02.pdf)
- **Status:** open
- **Obstruction match:** Weak. These lower bounds are stuck at the small-restriction (pk small) switching regime that C1 escapes. But proof complexity needs restrictions that preserve the structure of proof lines, and C1 is a correlation statement only.
- **Adaptation:** Look for a semantic (correlation or measure) Res(k) lower-bound framework into which C1 would plug.
- **Payoff / confidence / difficulty:** high / very low / very high
- **Lean:** needs major new library. Needs: -. Missing: proof systems, Res(k) derivations. Formal proof to compare: none.

## Theorem corollaries (not device reuse)

- Pi_3 (AND-OR-AND) version: the complement language (also in P) needs 2^{omega(sqrt n)} AND-OR-AND gates (De Morgan).
- One-sided structural corollary from the proof: every middle CNF of an exact OR representation accepts at most 6·2^{-m0/16} + S·2^{-k} of the inputs.
- Any other result that only needs 'explicit P-language with Sigma_3 complexity 2^{omega(sqrt n)}' as a black box. None in the release.

## Reuse inside the release

- grep for restrictionCost|narrowTests|MarkerMixture|reverseTheta over lean/OAI/Computability outside DepthThree: no hits. The device is used only in family 112.
- No other family in CONTENTS.md mentions random restrictions or switching lemmas. Family 135 (homogeneous depth-5 arithmetic circuits, DepthFive comparator) and family 274 (QAC0 parity) are circuit lower bounds by unrelated methods.

## Negative controls

- **N1 (proved-false analogue): parity requires 2^{omega(sqrt n)} depth-3 gates.**
  - Statement: False: parity has OR-AND-OR circuits of size O(n^{1/4} 2^{sqrt n}) (PPZ99).
  - Why it should fail or not help: corr_b(parity on m live vars) decays like 2^{-m/b}, at a rate that depends on b. So taking b large to allow constant pk destroys the slice bound. The C1 route must stall at c·sqrt n for parity, and a prover using C1 must not 'prove' the false statement.
  - Lean: statable now.
- **N2: Majority.**
  - Statement: Depth-3 lower bounds for Majority (HJP95 Thm 3.5; GPPST24 bottom fan-in 3).
  - Why it should fail or not help: Majority correlates Theta(1/sqrt m) with a single literal, so corr_1 does not decay exponentially and C1 yields nothing. Majority bounds need top-down or enumeration methods.
  - Lean: statable now.
- **N3: depth-2 parity correlation 2^{-Omega(n/log S)}.**
  - Statement: Parity has correlation 2^{-Omega(n/log S)} with size-S CNFs.
  - Why it should fail or not help: After deleting clauses wider than log S, a direct width-k correlation bound already suffices. C1's width reduction is redundant here, so no speedup is expected.
  - Lean: statable now.
- **N4: Parity not in QAC0 (family 274).**
  - Statement: OAI.QAC.parity_lower_bound (QACParity comparator).
  - Why it should fail or not help: Quantum circuits with Toffoli gates have no CNF structure, so C1 is inapplicable. Importing DepthThree should not shorten the 274 proof.
  - Lean: statable now.

## Top 5 (Lean-usable first)

1. **Depth-3 parity 2^{Omega(sqrt n)} via C1** (statable now). This is the cleanest measurable device-reuse test. The statement uses only DepthThree's own Circuit3 vocabulary, the downstream skeleton (wide_correlation_of_good_restrictions) is already generic in f, and the target is a classic switching-lemma consequence. With C1 the remaining work is a parity/narrow-CNF correlation lemma plus re-parametrised counting; without it a prover must find a switching lemma or the PPZ coding lemma. The expected gain is medium against the switching route and low against PPZ, and either outcome is informative.
2. **Natural explicit function with 2^{omega(sqrt n)}** (statable now). This is genuine reuse of C1 on new functions. C1 reduces the open question to a pseudorandomness property of random restrictions, and the Lean pipeline after the slice is f-generic. A success would be new mathematics using the device unchanged.
3. **Average-case (correlation) version** (statable now). C1 already controls each middle CNF's correlation; only the counting step uses exact computation. A prover with C1 in its library should reach this much faster than one without, which makes it a good speedup probe with a plausible positive outcome.
4. **Effective omega rate** (statable now). C1 is effective, so this tests whether provers can isolate the true bottleneck (sparsification) once the device is given. Moderate payoff and moderate difficulty.
5. **HJP95 2^{n^{1/2+epsilon}}** (statable now). This is the true frontier. C1 provably does not suffice as stated (see obstruction_match), so it doubles as a check on whether provers over-claim. Low confidence.

## Precedent

- **post_release_uses: none found** (web rerun 2026-10-10).
  - Searches covered the exact title, "2^{ω(√n)} depth-3 2026", "restriction lemma clause count depth-three", "signed combination width-b CNF random restriction", and OpenAI with depth-three.
  - They also covered the Computational Complexity blog, ECCC, Gödel's Lost Letter, Shtetl-Optimized and Combinatorics and More.
  - No item after 2026-10-06 cites or uses the lemma or the 2^{ω(√n)} claim. Press coverage of the release (Scientific American, Gizmodo and others) does not mention depth-3 circuits.
  - Index lag four days after release is a real limitation; recheck later.
- **Was the barrier open in 2025–26? Yes.**
  - [lacker.io](https://lacker.io/complexity/problems/depth3-circuits-past-sqrt-n.html), verified 2026-08-10 per the snippet, lists it as open. Its record is 2^{1.282√n} (PPSZ05).
  - Talebanfard's Sapienza talk of 17 Apr 2026 ([link](https://www.diag.uniroma1.it/node/30665)) says the lower bounds "have not changed since the 80s".
  - GKPRT26 ([2601.04446](https://arxiv.org/abs/2601.04446)) and [2601.04072](https://arxiv.org/abs/2601.04072) do not break √n.
  - [arXiv 1705.03588](https://arxiv.org/abs/1705.03588) calls a 2^{ω(√n)} bound for a function in P "wide open". HJP95 ([Springer](https://link.springer.com/article/10.1007/BF01268140)) poses the question, and GPPST24 ([CCC 2024](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2024.17)) gives a route to it.
- **earlier_equivalent: none.** Each neighbour was checked with a URL; details are in `downstream.json → precedent_check.update_2026_10_10_web`.
  - **H89:** the bound is (10σw)^d for σ ≤ 1/5 ([Katz notes](https://www.cs.umd.edu/~jkatz/complexity/f05/switching-lemma.pdf)), so it needs pk below a constant.
  - **Razborov encoding:** it pays d·lg w + 2d auxiliary bits ([2609.24188](https://arxiv.org/pdf/2609.24188), [1504.03398](https://arxiv.org/pdf/1504.03398)).
  - **Rossman 2017:** the bound is O(p log(m+1))^t, so clause count enters as log m ([logsize.pdf](https://www.math.utoronto.ca/rossman/logsize.pdf)).
  - **Lovett–Wu–Zhang:** E[#useful terms] ≤ (4/(1−α))^w at mild rates ([1909.10658](https://arxiv.org/abs/1909.10658)). This is closest in spirit, but its conclusion is term compression, not a correlation-preserving narrow-CNF expansion.
  - **IMP12:** a multi-formula switching lemma in Håstad's regime ([PDF](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoMatthewsPaturi_2012_soda.pdf)).
  - **PPZ97, PPSZ05 and HJP95:** different mechanisms, all capped at c√n.
  - **Golovnev–Kulikov–Williams:** a depth reduction ([1811.04828](https://arxiv.org/abs/1811.04828)), not a restriction lemma.
  - **"Kurur et al.":** could not be identified.
  - **Pre-release 2026 neighbours, not equivalent:** [2609.18166](https://arxiv.org/pdf/2609.18166) (approximate degree of width-k CNFs) and [2606.12631](https://arxiv.org/pdf/2606.12631) (a natural-proofs barrier for the switching lemma).
- **Correction: SBI is not "small p".** Segerlind–Buss–Impagliazzo ([abstract](https://sites.math.rutgers.edu/~saks/DMSEM/F02/0910.html)) is a *small-restriction* lemma: only a small fraction of variables is fixed.
  - It takes DNFs with tiny terms to CNFs of modestly small width.
  - So SBI, with Razborov's improvement, is a closer neighbour than recorded. It is still a pointwise switching statement that needs tiny k, not a signed width-b expansion with E W ≤ 1/(1−θ) at every constant pk.
  - Whether its failure bound is free of the term count was not verified: the full text could not be fetched.
- **verdict: No downgrade.** There is no earlier equivalent and no post-release use. C1 stays N3 provisional. The residual risk is expert folklore, plus the SBI and Razborov full texts that could not be fetched.

## Search log

- Read the Restriction*.lean chain and the comparator; traced Main -> LanguageLowerBound -> HardSlice -> WideCorrelation -> Restriction
- wc -l: restriction cluster 4,238 lines; plumbing (Tape/Machine/Language) 12,740 of 25,007
- grep restrictionCost|narrowTests|MarkerMixture|reverseTheta over lean/OAI/Computability excluding DepthThree -> none
- grep -i switching|random restriction|Hastad over lean/OAI/{Computability,InformationTheory,Combinatorics} -> none
- Searched for a local Mathlib checkout to grep for switching lemmas -> none present
- WebSearch 'Lean 4 formalization Håstad switching lemma' and 'switching lemma formalized Lean' -> FAILED (session limit)
- WebSearch was unavailable for the whole session (account session limit); no web query returned results. Literature items below are from the analyst's own knowledge and from data/pilot/112/{family,novelty}.* and must be checked.
- Web 2026-10-10: '"Beyond the square-root exponent" depth-three circuits' -> title not indexed; only lacker.io problem page, Talebanfard 2026 seminar, Bun-Thaler 2018, IAS chasm pages
- Web 2026-10-10: 'depth-3 circuit lower bound 2^omega(sqrt n) 2026' -> no 2026 result; problem open per lacker.io (verified 2026-08-10), HJP open question, PPSZ05 record
- Web 2026-10-10: 'restriction lemma clause count depth-three circuits' -> IPS97 threshold restriction lemma, HJP, PPZ coding lemma, arXiv 2606.12631, arXiv 2601.04072; nothing equivalent
- Web 2026-10-10: 'signed combination width-b CNF random restriction correlation' -> HRST 1504.03398, arXiv 2609.18166, ECCC TR25-124 (Chalupa); nothing equivalent
- Web 2026-10-10: 'OpenAI depth three circuits lower bound October 2026' -> nothing linking OpenAI to depth-3; classical papers only
- Web 2026-10-10: 'Computational Complexity blog OpenAI math release depth-3 circuits' -> no blog post found; GKPRT26 (2601.04446), ECCC 2023/106
- Web 2026-10-10: 'ECCC 2026 depth-three circuits lower bound explicit function beyond sqrt n' -> no 2026 ECCC report breaking sqrt n
- Web 2026-10-10: 'Aaronson Shtetl-Optimized OpenAI math results October 2026' -> no Aaronson post on the release; press coverage (SciAm, yourstory, aiweekly, interestingengineering) without depth-3 mention
- Web 2026-10-10: 'Goedel's Lost Letter depth-three circuits OpenAI 2026' -> no GLL post; arXiv 2609.18166, GKPRT26, Talebanfard seminar
- Web 2026-10-10: 'Gil Kalai Combinatorics and more OpenAI 372 math results' -> no Kalai post on the release; release coverage only
- Web 2026-10-10: WebFetch arxiv.org/abs/2609.18166 and eccc.weizmann.ac.il/report/2026/158 -> FAILED (DNS ENOTFOUND); curl via proxy -> 403; retried arxiv/export.arxiv/alphaxiv/lacker.io/mathweb.ucsd.edu -> all ENOTFOUND
- Web 2026-10-10: 'Lovett Wu Zhang 2020 decision list compression sunflower switching lemma mild random restriction' -> LWZ arXiv 1909.10658 confirmed: restriction lemma fixing a small fraction of variables, term compression
- Web 2026-10-10: 'Segerlind Buss Impagliazzo switching lemma small restrictions k-DNF resolution' -> SBI SICOMP 2004 confirmed; small restrictions (few variables fixed), OR of tiny ANDs -> AND of modestly small ORs
- Web 2026-10-10: 'Impagliazzo Matthews Paturi 2012 satisfiability algorithm AC0 extended switching lemma' -> IMP12 confirmed: extended switching lemma for multiple k-CNFs/k-DNFs
- Web 2026-10-10: 'Razborov encoding proof switching lemma Hastad bad restrictions' -> encoding with auxiliary bits confirmed; found arXiv 2609.24188 (Lean PARITY formalization)
- Web 2026-10-10: '"Formalizing PARITY Circuit Lower Bounds in Lean"' -> arXiv 2609.24188 (references only in snippet); cites Fredriksen SimpleDNF Lean switching lemma
- Web 2026-10-10: 'Lean 4 formalization Hastad switching lemma' -> arXiv 2609.24188; Quantyra/formal-switching-lemma via its bibliography
- Web 2026-10-10: 'switching lemma formalized Lean' -> arXiv 2609.24188 states Hastad's lemma (O'Donnell form) with Mathlib countP; no other formalization
- Web 2026-10-10: 'switching lemma formalization Isabelle AFP Coq parity AC0' -> no AFP or Coq entry; only bounded-arithmetic formalizations (APC1, Krajicek)
- Web 2026-10-10: 'Quantyra formal-switching-lemma Lean 4 SimpleDNF Fredriksen' -> nothing beyond 2609.24188
- Web 2026-10-10: 'arXiv 2609.24188 Lean parity AC0 switching lemma abstract' -> abstract not indexed; WebFetch arxiv FAILED (DNS)
- Web 2026-10-10: GitHub search_repositories 'switching lemma lean' -> codula-code/SwitchingLemma (Lean 4, created 2026-09-03); 'formal-switching-lemma' -> Quantyra/formal-switching-lemma (created 2026-06-19); 'parity AC0 lean', 'hastad lean4', 'circuit lower bound lean random restriction' -> none. WebFetch of both GitHub READMEs succeeded (summaries in switching_lemma_formalizations)
- Web 2026-10-10: 'Golovnev Kulikov Williams circuit depth reductions depth-3 2^{omega(sqrt n)} open problem Valiant' -> GKW ITCS 2021 confirmed (OR of 2^{s/3.9} 16-CNFs); exact open-problem wording not surfaced
- Web 2026-10-10: 'Goldreich Wigderson depth-three circuits open problem 2^{sqrt n} barrier multilinear circuits' -> GW depth-3 multilinear paper; Hastad exp(sqrt n) still best per GW
- Web 2026-10-10: 'Hastad Jukna Pudlak top-down lower bounds depth-three circuits 1995 2^{omega(sqrt n)} majority open' -> HJP95 confirmed (0.618/0.849 constants); PSZ97 says techniques cannot reach 2^{h(n) sqrt n}
- Web 2026-10-10: 'Talebanfard 2026 seminar depth-three circuits lower bounds Sapienza' -> 17 Apr 2026 talk: lower bounds 'have not changed since the 80s'
- Web 2026-10-10: '"The Switching Lemma shows what the Switching Lemma cannot prove" natural proofs barrier' -> arXiv 2606.12631 (June 2026), barrier for switching-lemma properties; not a precedent
- Web 2026-10-10: 'Paturi Pudlak Zane satisfiability coding lemma depth-3 lower bound parity' -> PPZ97 Theta(n^{1/4} 2^{sqrt n}) and PPSZ05 2^{1.282 sqrt n} confirmed
- Web 2026-10-10: 'Rossman entropy proof switching lemma 2017 log size m clauses' -> O(p log(m+1))^t confirmed
- Web 2026-10-10: 'Kurur depth-3 Boolean circuits lower bound random restriction' -> no Kurur paper found; reference unidentified
- Web 2026-10-10: 'random restriction CNF width reduction independent of number of clauses constant restriction probability lemma' -> only standard switching lemma and CIP width reduction; nothing equivalent
- Web 2026-10-10: '"Decision list compression by mild random restrictions" restriction lemma small fraction of variables fixed' -> LWZ bound E[#useful terms] <= (4/(1-alpha))^w confirmed
- Web 2026-10-10: 'correlation with k-CNF under random restriction bounded by correlation with narrow CNFs depth-3 lower bound technique' -> nothing equivalent (GC0 correlation bounds, ECCC 2011/131 sparsification, PPZ)
- Web 2026-10-10: 'Segerlind Buss Impagliazzo "switching lemma for small restrictions" statement probability r-DNF s-CNF fraction of variables fixed' (and a second phrasing) -> only abstract-level statements; exact failure bound not retrieved; WebFetch of mathweb.ucsd.edu focs02.pdf FAILED (DNS)
- Web 2026-10-10: '"Learning Depth-3 Circuits with Polynomial Savings" abstract' -> Chen-Fatehpuria-Patel-Servedio, arXiv 2609.18166, approximate degree of width-k CNFs; pre-release, not equivalent
- Web 2026-10-10: 'ECCC TR26-158' -> not identified (search returned unrelated ECCC acronyms)
- Web 2026-10-10: 'OpenAI math release complexity theory depth-3 circuit lower bound reaction experts' -> coverage of Aug 2026 Astra release and Oct release (Gizmodo, Henry Yuen blog); no depth-3 discussion
- Web 2026-10-10: 'Gurumukhani Paturi Pudlak Saks Talebanfard CCC 2024 Local enumeration and majority lower bounds depth-3 open problem' -> GPPST24 confirmed (1.251^n Sigma_3^3 Majority)
- Web 2026-10-10: '"depth-3" OR "depth-three" circuits "2^{omega(sqrt n)}" explicit function in P 2026 preprint' -> no 2026 preprint; arXiv 1705.03588 calls it 'wide open'
