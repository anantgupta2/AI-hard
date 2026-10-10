# Family 102: downstream targets for the quadratic latent gadget

Analyst role: downstream. Date: 2026-10-09. Machine-readable version: `downstream.json`.

**How this was done.**
- Text level only. The Lean was not compiled; there is no toolchain and no local Mathlib.
- **Web precedent searches were rerun on 2026-10-10** (31 WebSearch queries); they had failed on a session limit in the first pass. WebFetch failed on DNS for every host, so literature claims are checked against search-result summaries only, and unconfirmed claims are marked as such.

## Part A: is the item in the Lean?

**lean_status: as in paper.**
- `Quadratic/Block.lean` defines Q, its polar D and the block spaces U_A, exactly as in eq. (2.4)/(2.5).
- `Gadgets/` runs the paper's construction to `exists_actual_gadget` (Final.lean:19):
  - the oriented recursion;
  - the harmonic-rank argument;
  - the quotient;
  - the enlargement.
- That theorem is lem:latent. It has a rank threshold r fixed before ℓ, change probability ≤ p and detection ≥ 1/8.

**Chain from the comparator to the item.**
`theorem11` → `Theorem.exists_binaryGapReduction` → `Decoder.MatrixGap.exists_parameters` → `parameters_of_inverse` → `Gadget.exists_split_gadget` → `exists_actual_gadget` → `BaseConstruction.exists_base` → `QuadraticStageNoise.stage`/`actual_kernel` → `Quadratic.U`/`Q`/`D`.

The knockout is unambiguous: `parameters_of_inverse` is the gadget's only consumer.

**The other comparators.**
- **OptimalMaxCut** and **DirectedFeedback** do depend on the item. Each goes through a *namespace-renamed full copy* of the UG development:
  - `MaxCutGames.theorem11`, with Q at `MaxCut/Games/OrientationVectors.lean:95`;
  - `DFVSGames.theorem11`, with Q at `DirectedFeedback/Games/ChildLifts.lean:422`.
- So the Lean Max-Cut proof takes the UG route. The Max-Cut paper instead takes a direct route that avoids the gadget, using DKKMS 2-to-1 games plus Majority Is Stablest.
- **VertexCover** and **MinUncut** do not depend on the item.

**Gaps.**
- The paper's lemma promises a terminating algorithm that finds the data. Lean proves only existence.
- Lean states detection through linear maps rather than dual subspaces. This is equivalent.
- The Lean threshold is explicit: r = 3d + 2.

### Verbatim Lean declarations
See `downstream.json → lean_source` for the full text. Entries:

- `OAI.UniqueGamesTheorem.Quadratic.Q` (def), `OAI/Computability/UniqueGames/Quadratic/Block.lean:19`
- `OAI.UniqueGamesTheorem.Quadratic.D` (def), `OAI/Computability/UniqueGames/Quadratic/Block.lean:22`
- `OAI.UniqueGamesTheorem.Quadratic.D_eq_polar` (theorem), `OAI/Computability/UniqueGames/Quadratic/Block.lean:107`
- `OAI.UniqueGamesTheorem.Quadratic.Q_add_of_mem_line` (theorem), `OAI/Computability/UniqueGames/Quadratic/Block.lean:145`
- `OAI.UniqueGamesTheorem.Quadratic.U` (def), `OAI/Computability/UniqueGames/Quadratic/Block.lean:152`
- `OAI.UniqueGamesTheorem.Gadget.ActualGadget.Data` (structure), `OAI/Computability/UniqueGames/Gadgets/ActualGadgetLemmas.lean:21`
- `OAI.UniqueGamesTheorem.Gadget.ActualGadget.Satisfies` (def), `OAI/Computability/UniqueGames/Gadgets/ActualGadgetLemmas.lean:99`
- `OAI.UniqueGamesTheorem.Gadget.QuadraticStageNoise.actual_kernel` (theorem), `OAI/Computability/UniqueGames/Gadgets/QuadraticStageNoise.lean:33`
- `OAI.UniqueGamesTheorem.Gadget.QuadraticStageNoise.stage_error` (theorem), `OAI/Computability/UniqueGames/Gadgets/QuadraticStageNoise.lean:44`
- `OAI.UniqueGamesTheorem.Gadget.BaseConstruction.exists_base` (theorem), `OAI/Computability/UniqueGames/Gadgets/BaseConstruction.lean:95`
- `OAI.UniqueGamesTheorem.Gadget.exists_actual_gadget` (theorem), `OAI/Computability/UniqueGames/Gadgets/Final.lean:17`
- `OAI.UniqueGamesTheorem.Gadget.exists_split_gadget` (theorem), `OAI/Computability/UniqueGames/Gadgets/Final.lean:68`
- `OAI.UniqueGamesTheorem.theorem11` (theorem), `OAI/Computability/UniqueGames/Theorem.lean:23`

## Part B: speedup targets (known theorems)

**Verdict.** No strong device-level speedup target found. Every known theorem that clearly gets shorter with the gadget available (Max-Cut at alpha_GW, Vertex Cover 2-epsilon, Raghavendra CSPs, DFVS, Min-UnCut, sparsest cut, kernel clustering, 2-to-2 games with completeness 1-epsilon) gets shorter through theorem11, so it is a corollary and does not count as device reuse. The release's own Lean is the strongest measurable evidence: for OptimalMaxCut and DirectedFeedback the formalizers chose the gadget/theorem11 route over the papers' direct routes, and vendored about 63k-66k lines of copied UG development each.

### S1. Perfect completeness for 2-to-1 games (release family 105)
- **Statement:** For every rational delta in (0,1) it is NP-hard to distinguish satisfiable 2-to-1 games from games of value <= delta, over a fixed alphabet (OAI.PerfectCompleteness.Theorem11.exists_reduction).
- **Reference:** OpenAI release fd4aeeb, preprints/Perfect-completeness-for-2-to-1-games-September-23-2026; Lean OAI/Computability/PerfectCompleteness (581 files).
- **Status:** claimed proved (unrefereed); Lean-formalized end to end in the release
- **Current proof size:** Paper about 60+ pages (not counted precisely); Lean 581 files.
- **How the item helps:** The two proofs share an architecture: a recursive tree whose spaces are spanned by products of child functions, explored along a random root-to-leaf path. The genericity and harmonic rank-loss lemmas in UniqueGames/Quadratic (GenericSeparationLemmas, HarmonicLoss, GenericSubspaceProbability) might replace parts of 105's rank-splitting decoders (Algebra/DecoderRankSplit, FunctionSpaceLowerRank). The Q block itself cannot be used as completeness noise, because perfect completeness forbids change probability p > 0 (see negative control N1).
- **Expected speedup:** low
- **Confidence:** low
- **Lean:** statable now. Needs: PerfectCompleteness comparator as released. Missing: none. Formal proof to compare: yes: run the 105 comparator with and without UniqueGames/Quadratic + Gadgets imported; Lean-vs-Lean size comparison is direct.

### S2. Near-perfect-completeness hardness with quadratic or low-degree codes (Khot-Saket 2014; Dinur-Guruswami 2013)
- **Statement:** Khot-Saket (FOCS 2014): given a graph that is almost q-colorable (q-colorable after removing an epsilon fraction of vertices or edges), it is NP-hard to find an independent set of small relative size. Exact size bound not recalled; check against the paper. Dinur-Guruswami (FOCS 2013): PCPs via the low-degree long code, giving hardness for constrained hypergraph coloring.
- **Reference:** S. Khot, R. Saket, 'Hardness of finding independent sets in almost q-colorable graphs', FOCS 2014 (arXiv 1408.0262 per novelty.json); I. Dinur, V. Guruswami, 'PCPs via the low-degree long code and hardness for constrained hypergraph coloring', FOCS 2013 / Israel J. Math 2015. Parameters quoted from memory, unverified.
- **Status:** known theorems
- **Current proof size:** about 30-40 pages each (from memory); no formalization known.
- **How the item helps:** Both papers face the same obstruction as lem:latent: tests that are linear in the code lose completeness under translation noise, and quadratic or low-degree codes are used to recover completeness close to 1. The latent gadget is a different fix: the honest answer is nonlinear in the table, while any linear observation of high rank detects the noise. A gadget-based test could replace the low-degree-code completeness analysis. This is speculative; no concrete reduction was worked out.
- **Expected speedup:** low
- **Confidence:** low
- **Lean:** statable with < 300 lines of new definitions. Needs: Mathlib SimpleGraph.Coloring / IsIndepSet; the release's BinaryFormula, BinaryLanguage and TM2ComputableInPolyTime reduction contract (UniqueGamesTheorem.Explicit.MachineOutputContract pattern). Missing: almost-q-colorable promise and gap-reduction contract for independent sets (~150 lines). Formal proof to compare: none.

### S3. Håstad's 3-bit PCP / Max-3-Lin(F2) with completeness 1-epsilon (calibration)
- **Statement:** For every epsilon, delta > 0 it is NP-hard to distinguish Max-3-Lin(F2) instances with value >= 1-epsilon from those with value <= 1/2 + delta.
- **Reference:** J. Håstad, 'Some optimal inapproximability results', JACM 48 (2001).
- **Status:** known theorem
- **Current proof size:** about 15 pages for the 3-Lin part (on top of Label Cover and parallel repetition); no Lean formalization known.
- **How the item helps:** This is the classical case where completeness 1-epsilon comes from long-code noise. The latent gadget is an alternative noise mechanism that keeps a nonlinear decoder stable. One expects no gain, because Håstad's noise analysis is already short; the target is useful as a calibration point that should show no speedup.
- **Expected speedup:** low (expected none; calibration)
- **Confidence:** medium
- **Lean:** statable with < 300 lines of new definitions. Needs: release reduction contract plus a 3-Lin instance type (~80 lines). Missing: Max-3-Lin instance/value definitions; Label Cover with parallel repetition is NOT in the library, so the proof needs a major library even though the statement is cheap. Formal proof to compare: none.

## Open or new problems

### O1. Quantitative gadget trade-off r_*(p_*) and the UG alphabet size
- **Statement:** Determine the least rank threshold r_*(p) for which a latent gadget (equivariant C, change probability <= p, detection >= 1/8 for every linear family with restriction rank >= r) exists, and the least ambient dimension. Lower bounds on r_*(p) would bound how small the UG alphabet F_2^s can be for given (epsilon, delta).
- **Reference:** New question raised by lem:latent (preprints/The-Unique-Games-Theorem-September-23-2026, sec. 2). Context: Khot's UGC alphabet dependence; ABS10 subexponential algorithm (Arora-Barak-Steurer, FOCS 2010), https://doi.org/10.1145/2775105 (https://github.com/openai/math (release fd4aeeb))
- **Status:** open (new)
- **Obstruction match:** Directly the item: the Lean threshold r = 3d + 2 depends on the field size 2^d chosen for genericity (exists_uniform_generic_field), and the harmonic depth governs p.
- **Adaptation:** Upper bound: optimise d and the depth in BaseConstruction.effective_parameters. Lower bound: extend the p = 0 impossibility argument (N1) to a quantitative statement, e.g. show r_*(p) >= c log(1/p) by a counting/Fourier argument on the noise support.
- **Payoff / confidence / difficulty:** medium (alphabet-size bounds for UG hardness) / medium / medium
- **Lean:** statable now. Needs: OAI ActualGadget.Data / Satisfies, Module.finrank, ZMod 2. Missing: none. Formal proof to compare: partial: exists_actual_gadget gives the upper-bound side.

### O2. Odd-characteristic latent gadget (direct translation UG over F_p^s)
- **Statement:** For odd prime p, construct C: V -> K = F_p^l with C(x+k) = C(x)+k, small change probability under a noise law, and detection by every F_p-linear family of restriction rank >= r_* with r_* independent of l.
- **Reference:** New; adaptation of lem:latent. KKMO07 (SICOMP 37) reduce UG to Gamma-Max-2-Lin(Z_q), so the hardness consequence is already a corollary; the payoff is a direct construction. (https://doi.org/10.1137/S0097539705447372)
- **Status:** open (new)
- **Obstruction match:** Lean's block relies on characteristic 2 (Block.lean: D_eq_polar, cross_self_zero, D_smul_smul_zero, and U being closed under addition). In odd characteristic D(tv, sv) = 2ts*Q(v)-type terms do not vanish on lines, so U_A is not a subgroup.
- **Adaptation:** Replace F-lines by Q-isotropic lines, or use a quadratic map whose polar vanishes on chosen lines; then rerun the oriented-recursion and harmonic-rank argument with F_p characters.
- **Payoff / confidence / difficulty:** low-medium / medium / medium
- **Lean:** statable with < 300 lines of new definitions. Needs: generalise ActualGadget.Data from F2 to ZMod p (~50 lines). Missing: Data/Satisfies over ZMod p. Formal proof to compare: none.

### O3. NP-hardness of Small-Set Expansion (SSEH)
- **Statement:** For every eta there is delta such that it is NP-hard to distinguish graphs having a set of measure delta with expansion <= eta from graphs in which every set of measure delta has expansion >= 1-eta.
- **Reference:** P. Raghavendra, D. Steurer, 'Graph expansion and the unique games conjecture', STOC 2010; Raghavendra-Steurer-Tulsiani, CCC 2012. (https://doi.org/10.1145/1806689.1806792)
- **Status:** open as of the analyst's knowledge; status after the release unverified (no web)
- **Obstruction match:** Weak. SSEH needs UG hardness on constraint graphs that are small-set expanders. The gadget only fixes the completeness noise. The shortcode/Grassmann test graphs have non-expanding zoom-in/zoom-out sets, and the gadget does not change that.
- **Adaptation:** Check whether the latent noise law mu, run over the matrix shortcode, changes the expansion profile of the test graph. If it does, try the RST12 route from UG on SSE graphs to SSE.
- **Payoff / confidence / difficulty:** very high / very low / very high
- **Lean:** statable with < 300 lines of new definitions. Needs: Mathlib SimpleGraph, Finset measure; release reduction contract. Missing: edge expansion of vertex sets and SSE gap promise (~120 lines). Formal proof to compare: none.

### O4. Sliding Scale Conjecture / Projection Games Conjecture
- **Statement:** NP-hardness of Label Cover with soundness 1/poly(n) (BGLR93), or with alphabet size and soundness polynomially related at near-linear size (Moshkovitz 2012).
- **Reference:** Bellare-Goldwasser-Lund-Russell, STOC 1993; D. Moshkovitz, 'The projection games conjecture and the NP-hardness of ln n-approximating set-cover', APPROX 2012. (https://doi.org/10.1007/978-3-642-32512-0_24)
- **Status:** open
- **Obstruction match:** Weak. The gadget's rank threshold is fixed before the alphabet dimension, which gives alphabet-independent decoding loss. That is the property sliding-scale reductions need. But the gadget only works at constant soundness.
- **Adaptation:** Ask whether r_* can be kept constant while the detection probability 1/8 is pushed towards 1 (amplified detection). That would feed low-soundness Label Cover through the matrix decoder.
- **Payoff / confidence / difficulty:** high / very low / very high
- **Lean:** statable with < 300 lines of new definitions. Needs: release reduction contract. Missing: projection Label Cover instance/value (~100 lines). Formal proof to compare: none.

### O5. UG reduction size vs the ABS subexponential algorithm
- **Statement:** Find the optimal blow-up n^{f(epsilon, delta)} of 3SAT -> UG reductions, and whether Unique Games with completeness 1-epsilon requires time exp(n^{epsilon^c}) under ETH, matching Arora-Barak-Steurer.
- **Reference:** S. Arora, B. Barak, D. Steurer, 'Subexponential algorithms for unique games and related problems', FOCS 2010 / JACM 2015. (https://doi.org/10.1145/2775105)
- **Status:** open
- **Obstruction match:** The gadget's size (field 2^d, depth n) and the repetition-before-alphabet step determine the reduction's exponent; quantitative gadget bounds (first open problem) feed in directly.
- **Adaptation:** Instrument the Lean parameter selection (ParameterSelection.exists_outerParameters, BaseConstruction.effective_parameters) to extract f(epsilon, delta), then compare with ABS's exp(n^{poly(epsilon)}).
- **Payoff / confidence / difficulty:** medium / low / high
- **Lean:** statable with < 300 lines of new definitions. Needs: Mathlib Turing.TM2ComputableInPolyTime; release contract. Missing: ETH hypothesis and explicit size accounting (~150 lines). Formal proof to compare: none.

### O6. Near-perfect-completeness agreement tests on HDX / quasi-linear PCPs with small soundness
- **Statement:** Construct agreement or linearity-type tests on high-dimensional expanders with completeness 1-epsilon and small soundness, usable in quasi-linear-size PCPs that reach UG- or 2-to-2-type gaps.
- **Reference:** Bafna-Minzer-Vyas (2024) and Dikstein-Dinur-Lubotzky (2024) HDX-based PCP line; titles and venues from memory, unverified.
- **Status:** open (active area)
- **Obstruction match:** Medium in form. Linear tests on subspace complexes lose completeness under translation-type noise. The gadget converts completeness 1/2 into 1-epsilon while keeping linear-rank soundness.
- **Adaptation:** Replace the matrix-shortcode test noise by latent noise over HDX-based subspace codes, and check whether the inverse theorem there tolerates the extra ambient coordinates.
- **Payoff / confidence / difficulty:** medium / low / high
- **Lean:** needs major new library. Needs: -. Missing: high-dimensional expanders, agreement tests. Formal proof to compare: none.

## Theorem corollaries (not device reuse)

- Max-Cut NP-hard beyond alpha_GW (KKMO07 + MOO10). In Lean, OptimalMaxCut is proved via a vendored theorem11 copy; the Max-Cut paper proves it directly without the gadget.
- Vertex Cover NP-hard below factor 2 (Khot-Regev 2008), paper sec. 7. The release proves VertexCover directly (66k Lean lines, no gadget). That gives a measurable with/without comparison at corollary level, if KR08 were formalized.
- Raghavendra's optimal CSP thresholds (cor:raghavendra-consequence) and ordering CSPs (Guruswami-Håstad-Manokaran-Raghavendra-Charikar 2011).
- Multicut, non-uniform sparsest cut, Min-2CNF-equivalence deletion, correlation clustering (CKKRS06; sec. 7).
- DFVS constant-factor hardness (Svensson's UG reduction). In Lean, DirectedFeedback is proved via a vendored DFVSGames.theorem11 copy.
- Uniform sparsest cut constant-factor hardness (family 117 paper uses the UG theorem as premise; its Lean comparator covers only the integrality gap).
- Kernel clustering hardness (family 096; Lean covers only the propeller bound).
- 2-to-2 games with completeness 1-epsilon: immediate from UG by label doubling (KMS18 then becomes a corollary).

## Reuse inside the release

- Full-tree grep: Q is defined in exactly three places in OAI: UniqueGames/Quadratic/Block.lean:20, MaxCut/Games/OrientationVectors.lean:95 and DirectedFeedback/Games/ChildLifts.lean:422. exists_actual_gadget / StableNonlinearDispersion appear only in those three trees.
- MaxCut/Games (117 files, about 63k lines) and DirectedFeedback/Games (about 66k lines) are namespace-renamed copies of the UG development, consumed through theorem11. That is reuse of the theorem, not independent reuse of the design.
- Family 105 (2-to-1 perfect completeness) shares the recursive product-tree architecture (quadraticSpan, dependentQuadraticSpan in Construction/FactoredFunctionsLemmas.lean) but not Q, U_A or the latent separation property. This looks like a house style; priority between the two is unknown.
- The Max-Cut paper's 'latent resampling rows' (decoding.tex) are a different device (planted zero coefficients); only the name is shared.

## Negative controls

- **N1 (proved-false analogue): latent gadget with p_* = 0.**
  - Statement: There is no Data g over K = F_2^l with stabilityError g = 0 and kernelError <= nu < 1 for every S of restriction rank >= r, whenever l >= r.
  - Why it should fail or not help: If C(x+a) = C(x) for all a in supp(mu), let A = span(supp mu). Equivariance forces A ∩ K = 0. Then G = A^perp restricts onto all of K^*, so it has rank l >= r_*, yet it vanishes on every noise vector, so the detection probability is 0. Any gadget must therefore pay p > 0. This is why perfect-completeness results (105, approximate coloring under 2-to-1) cannot use it as completeness noise.
  - Lean: statable now.
- **N2: Unique Games with perfect completeness, on expanders, or with entangled provers.**
  - Statement: Satisfiable UG is in P (propagation / Gaussian elimination for translations); UG on spectral expanders is easy (Arora-Khot-Kolla-Steurer-Tulsiani-Vishnoi 2008); entangled-prover UG is in P (Kempe-Regev-Toner 2008).
  - Why it should fail or not help: Gadget-based reductions must yield imperfect completeness, non-expanding constraint graphs and classical-only soundness. Targets that need any of these three properties should show no speedup.
  - Lean: statable with < 300 lines of new definitions.
- **N3: VertexCover and MinUncut comparators.**
  - Statement: The release's own direct proofs of Vertex Cover 2-epsilon and Min-UnCut hardness.
  - Why it should fail or not help: They contain no Q or gadget. Importing UniqueGames/Quadratic + Gadgets should not shorten them unless they are rerouted through theorem11, and that rerouting would be corollary use.
  - Lean: statable now.

## Top 5 (Lean-usable first)

1. **Quantitative trade-off r_*(p_*) / UG alphabet size** (statable now). This is the only target that tests the device itself rather than its theorem, and it needs no new definitions: Data and Satisfies already express it. An upper-bound improvement is a direct measure of how much the construction can be compressed. A lower bound, extending the proved-false p = 0 control, would show whether the gadget's parameters are forced. Both feed the alphabet and size of UG hardness.
2. **Odd-characteristic latent gadget** (statable with < 300 lines). This is a clean test of device generality. The Lean pins exactly which lemmas are characteristic-2 specific (D_eq_polar, cross_self_zero, D_smul_smul_zero). If a prover with Quadratic/ in its library finds an odd-characteristic analogue much faster than one without it, that is device reuse. The hardness consequence is already a corollary via KKMO, so the result has to be judged as a construction.
3. **Family 105 Lean (2-to-1 perfect completeness)** (statable now; formal proof exists). This is the only Lean-vs-Lean measurable device-level comparison. Run the 105 comparator with and without UniqueGames/Quadratic + Gadgets imported. Expectation is low: N1 forbids using the gadget as noise, but the genericity and harmonic lemmas may transfer. Even a null result calibrates the test.
4. **Khot-Saket / Dinur-Guruswami near-perfect-completeness hardness** (statable with < 300 lines). These are the closest known theorems facing the same completeness-under-linear-structure obstruction, which they solve with quadratic or low-degree codes. A gadget-based reproof would be genuine device reuse. Confidence is low, and the PCP infrastructure (Label Cover, repetition) exists only inside the UG tree.
5. **Small-Set Expansion Hypothesis** (statable with < 300 lines). The payoff is very high, but the obstruction match is weak: the gadget does not touch the expansion of the constraint graph. Include it as a long shot and as a check on whether a prover over-generalises the device.

## Precedent

- **post_release_uses:** None found (web rerun 2026-10-10). No paper, preprint or blog post after 2026-10-06 uses or discusses the latent alphabet gadget, the block y + Q(x) or the map (x2x3, x1x3, x1x2) in a UG/PCP context. Post-release coverage is about the release and the race: Quanta 2026-10-07, remio.ai, kingy.ai, mindstudio.ai, officechai, and Aaronson's 'Mathocalypse' (seen only through secondary coverage). One secondary summary (kingy.ai) mentions 'quadratic gadgets' from the reasoning summary as building on existing PCP work, without technical detail. A GitHub commentary bot PR (mahrud/openai-math-comments #102, 2026-10-09) exists. It was not readable here: the repo is outside the session's GitHub scope. Per the search summary it points to arXiv 2610.12378 (= FMW) and Quanta. There is no Computational Complexity blog, Kalai or Windows on Theory post on it in the results, and no arXiv cs.CC follow-up was found. The release-internal copies (MaxCut, DirectedFeedback) are not independent.
- **earlier_equivalent:** None found in the novelty pass (data/pilot/102/novelty.md): Khot-Saket quadratic code, low-degree/short codes, Cremona map (object only), FMW ECCC TR26-179 (2026-09-14; no nonlinear decoder). The closest is the same-release 2-to-1 companion (architecture only). No new precedent found here; the release-internal copies in MaxCut/DirectedFeedback are not independent.
- **Web rerun 2026-10-10:**
  - *Post-release uses:* None found. See post_release_uses. Searches for 'latent alphabet gadget', '(x2x3, x1x3, x1x2) unique games' and 'quadratic block Unique Games Theorem' returned nothing relevant: toy pages, Hastad et al. 2-LIN gadgets and generic UG material.
  - *Earlier equivalents:* No earlier equivalent found. No search tied the standard quadratic (Cremona/Steiner) map (x2x3, x1x3, x1x2) to codes, PCPs, UG or label cover. The only hit for the map is birational geometry: 'Combinatorics of Cremona monomial maps', arXiv:0904.4065, where it is the Steiner involution. Searches for nonlinear/quadratic gadgets or decoders for UG/label cover and for 'y + Q(x)' shift codes found only standard linear constructions (long code, short code, Hadamard, Khot-Safra point-vs-subspace) and Chen's perfect-completeness hypergraph dictatorship test (arXiv:0811.1922). None is a nonlinear equivariant decoder.
  - *Literature claims, verified or corrected:*
    - Khot-Saket quadratic code: VERIFIED as a precedent for the object class only, not the device. The quadratic code is the degree-2 low-degree long code: the table at x is linear in x tensor x. It was used in a 12-query inner verifier for 2-colourable 12-uniform hypergraph colouring (quasi-NP-hard, 2^{(log n)^Omega(1)} colours), per arXiv:1408.0262 (Varma) and the Dinur-Guruswami listings. The honest table is linear in the quadratic code coordinates, which is consistent with novelty.md. https://arxiv.org/pdf/1408.0262
    - Low-degree long code / short code: VERIFIED. BGHMRS, 'Making the long code shorter' (arXiv:1111.0405), and Dinur-Guruswami FOCS 2013 (arXiv:1311.7407, ECCC TR13-122) are linear low-degree evaluations, and BGHMRS suggests alphabet reduction for UG. Neither has a nonlinear block. https://arxiv.org/pdf/1111.0405 ; https://arxiv.org/pdf/1311.7407
    - Khot-Minzer-Safra 2-to-2: VERIFIED. 'Pseudorandom sets in Grassmann graph have near-perfect expansion', Annals 198(1) 2023, ECCC TR18-006. It completes 2-to-2 with imperfect completeness via DKKMS + BKS18 inverse short code. There is no quadratic gadget. https://annals.math.princeton.edu/2023/198-1/p01
    - Minzer-Zheng arXiv:2404.07441: PARTLY VERIFIED. The title, authors and STOC 2024 venue are confirmed, and the inner PCP is a Grassmann/low-degree test. The search showed v1-v3 only. The v4 date (2026-05-13) and the 106-page count in novelty.md were NOT confirmed. https://arxiv.org/abs/2404.07441
    - FMW ECCC TR26-179: VERIFIED and REFINED. Fei-Minzer-Wang, 'On the Hardness of 4-to-1 Games with Perfect Completeness', ECCC dated 14 Sep 2026, also arXiv:2610.12378. Per the search summary of the abstract, it uses quadratic equations in the outer PCP for perfect completeness, a middle PCP with low-rank tests, and a new inner PCP. Whether that inner PCP uses a nonlinear decoder could NOT be checked (no full text; WebFetch DNS failure). The novelty.md statement 'no nonlinear decoder' therefore stays unverified at full-text level. It is the main residual risk for an earlier/contemporaneous equivalent. https://eccc.weizmann.ac.il/report/2026/179/ ; https://arxiv.org/abs/2610.12378
    - Quanta 2026-10-07 and the rumour date: CONSISTENT. Search summaries say rumours reached Minzer on Sep 11 and that the 95-page paper was posted early with a 'complete mathematically' disclaimer. Some summaries mislabel the FMW result as 2-to-1. https://www.quantamagazine.org/as-ai-closed-in-on-unique-games-proof-researchers-raced-to-beat-the-machines-20261007/
    - Khot-Moshkovitz 'Candidate hard unique game' (real code; ECCC TR14-142, STOC 2016): VERIFIED as an existing human reduction with a real-code test. It bears on C1 (the concept, N2), not on the explicit quadratic block. https://cs.utexas.edu/~danama/papers/ugc/candidate-linear.pdf
    - Cremona map (object only): VERIFIED as classical (Steiner involution). No PCP/coding use found, so it is a transfer of an object (N0 for the object), not an earlier equivalent of the device.
    - ProofAtlas UGC page (https://www.proofatlas.ai/collaboration/unique-games-conjecture/) appeared in one result list. Its content (the tensor-rank-one programme) could not be fetched or re-checked.
    - Aaronson 'The Mathocalypse': known only through secondary coverage (ecosistemastartup.com, tildes.net). The original post was not retrieved.
  - *Failures:* WebFetch failed with getaddrinfo ENOTFOUND for quantamagazine.org (both hosts), eccc.weizmann.ac.il, tildes.net, arxiv.org (twice) and lance.fortnow.com. GitHub MCP access to mahrud/openai-math-comments was refused (repo outside the session scope). WebSearch hit no rate limits.
- **verdict:** No downgrade. The 2026-10-10 web rerun found no earlier equivalent of the explicit quadratic latent gadget and no post-release use. The closest human work is FMW TR26-179 (contemporaneous, 2026-09-14), which uses quadratic equations in the outer PCP. Its inner PCP was not read in full, so this is the open check to do when full text is reachable. N3 (provisional) stands, pending the downstream speedup test.

## Search log

- grep 'x 1 * x 2, x 0 * x 2' over all of lean/OAI -> 3 hits (UniqueGames, MaxCut, DirectedFeedback)
- grep exists_actual_gadget|exists_split_gadget|StableNonlinearDispersion over lean/OAI/Computability -> UG, MaxCut, DFVS only
- grep theorem11 in MaxCut, DirectedFeedback, MinUncut, VertexCover -> MaxCut/Games/Theorem.lean:23, DirectedFeedback/RankGraph/OutputDef.lean:20; none in MinUncut/VertexCover
- grep latent|gadget in sibling preprints; read Max-Cut paper introduction
- grep Unique|theorem11 in Combinatorics/SparsestCut, Computability/PerfectCompleteness, Probability/GaussianPropeller -> no gadget copies
- WebSearch 'Unique Games theorem 2026 latent gadget quadratic follow-up' -> FAILED (session limit)
- WebSearch was unavailable for the whole session (account session limit); no web query returned results. Literature items below are from the analyst's own knowledge and from data/pilot/102/novelty.* and must be checked.
- Web 2026-10-10: '"latent alphabet gadget"' -> no relevant hit (toy/alphabet pages only)
- Web 2026-10-10: '(x2x3, x1x3, x1x2) unique games quadratic gadget' -> no match; Hastad-Huang-Manokaran-O'Donnell-Wright 2-LIN gadget slides, unrelated
- Web 2026-10-10: 'quadratic block "Unique Games Theorem"' -> no match; Lasserre/2-to-2 background only
- Web 2026-10-10: 'Unique Games Conjecture proved OpenAI October 2026' -> release coverage: Quanta 2026-10-07, officechai, tildes (Mathocalypse), 1023jack; no gadget discussion
- Web 2026-10-10: 'Unique Games theorem 2026 latent gadget quadratic follow-up' -> no follow-up; BGHMRS 1111.0405 and background
- Web 2026-10-10: 'Fei Minzer Wang ECCC TR26-179' -> no relevant hit
- Web 2026-10-10: 'Aaronson "Mathocalypse" Unique Games' -> no original post; generic UG background
- Web 2026-10-10: 'Fei Minzer Wang 4-to-1 games perfect completeness 2026' -> diariobitcoin secondary report of the FMW 4-to-1 result
- Web 2026-10-10: 'Khot Saket quadratic code hardness approximation' -> Varma arXiv:1408.0262 etc.; quadratic code = degree-2 low-degree long code, 12-query inner verifier (verified)
- Web 2026-10-10: 'Khot Minzer Safra pseudorandom sets Grassmann graph 2-to-2 games theorem' -> Annals 2023 / ECCC TR18-006 confirmed; Barak 2018 Windows on Theory post
- Web 2026-10-10: 'Minzer Zheng near optimal alphabet-soundness tradeoff PCPs arXiv 2404.07441' -> confirmed (STOC 2024); v1-v3 seen, v4 not confirmed
- Web 2026-10-10: 'standard quadratic Cremona transformation (x2x3, x1x3, x1x2) finite field code PCP hardness' -> no Cremona-PCP/code link found
- Web 2026-10-10: 'nonlinear gadget unique games label cover quadratic nonlinear decoder perfect completeness' -> no nonlinear gadget/decoder; Brakensiek-Guruswami, DKKMS 2-to-1 only
- Web 2026-10-10: 'Computational Complexity blog Fortnow Gasarch OpenAI Unique Games October 2026' -> no blog post found; release coverage only
- Web 2026-10-10: 'Gil Kalai OpenAI Unique Games conjecture proof 2026' -> no Kalai post found
- Web 2026-10-10: 'Windows on Theory Boaz Barak OpenAI Unique Games proof' -> only the 2018 2-to-2 post; nothing on 2026
- Web 2026-10-10: 'Scott Aaronson Shtetl-Optimized Mathocalypse OpenAI math release' -> secondary coverage only (ecosistemastartup, aiweekly, mindstudio); no technical content on the gadget
- Web 2026-10-10: 'arXiv cs.CC October 2026 unique games quadratic gadget perfect completeness follow-up OpenAI proof' (extended) -> Fortnow TCS selection page, remio, kingy ('quadratic gadgets' building on existing PCP work), ProofAtlas; no arXiv follow-up
- Web 2026-10-10: 'low degree long code short code Barak Gopalan Hastad Meka Raghavendra Steurer unique games' -> BGHMRS arXiv:1111.0405 confirmed; linear low-degree code
- Web 2026-10-10: 'OpenAI Unique Games proof "quadratic gadget" OR "latent alphabet" OR "nonlinear code" experts' (extended) -> no expert technical analysis; secondary blogs only
- Web 2026-10-10: 'Khot Moshkovitz 2016 candidate hard unique game real code noise test' -> Khot-Moshkovitz real code confirmed (ECCC TR14-142)
- Web 2026-10-10: 'Dinur Guruswami PCPs via low-degree long code quadratic code hypergraph coloring' -> arXiv:1311.7407 confirmed; linear low-degree code
- Web 2026-10-10: 'Minzer Fei Wang 95-page paper 4-to-1 games quadratic equations outer PCP ECCC September 2026' (extended) -> FMW confirmed: ECCC TR26-179 (14 Sep 2026), arXiv:2610.12378; quadratic equations in outer PCP, middle low-rank PCP, new inner PCP
- Web 2026-10-10: 'OpenAI Unique Games proof noise test recursive structure "update spaces" OR "quadratic map" analysis blog' -> no technical analysis found
- Web 2026-10-10: 'Cremona map x1x2 x1x3 x2x3 characteristic 2 coding theory APN quadratic function' -> map = Steiner involution (arXiv:0904.4065); no coding/APN link
- Web 2026-10-10: '"4-to-1 Games with Perfect Completeness" inner PCP low-rank test quadratic' -> FMW not returned; Khot-Safra 2013, Chen 2008
- Web 2026-10-10: 'arXiv 2610 "Unique Games" OpenAI proof simplification OR verification OR follow-up' (extended) -> github mahrud/openai-math-comments PR #102 (bot commentary, 2026-10-09, cites arXiv 2610.12378 = FMW); no simplification/follow-up
- Web 2026-10-10: 'nonlinear equivariant encoding PCP inner verifier y + Q(x) quadratic shift code dictatorship test' -> no match; Chen 0811.1922, Macaulay-bases PCP 2511.03703 (algebraic, linear)
- Web 2026-10-10: 'mahrud openai-math-comments 102 Unique Games Conjecture optimal approximation thresholds comment' -> PR text not indexed; GitHub MCP refused (repo out of scope)
- Web 2026-10-10: 'ProofAtlas Unique Games Conjecture collaboration tensor rank one verifier' -> ProofAtlas page not returned
- Web 2026-10-10: 'arXiv 2610.12378 Fei Minzer Wang abstract inner PCP' -> abstract not returned; inner-PCP nonlinearity unchecked
- Web 2026-10-10: WebFetch on quantamagazine.org, eccc.weizmann.ac.il/report/2026/179, tildes.net, arxiv.org/abs/2404.07441, arxiv.org/abs/2610.12378, lance.fortnow.com -> FAILED (getaddrinfo ENOTFOUND, every host)
