# Family 103: downstream targets (L = RL = BPL)

Date: 2026-10-10. Analyst: downstream-target agent.

**Method.** Text-level reading of the Lean only. I did not run lake, lean or comparator, because another process is building in the workspace. The comparator PASS on 2026-10-10 is the orchestrator's result. Literature claims rest on WebSearch snippets; WebFetch was not used because arxiv.org is blocked.

**Item (F5 (copy-space embedding) + F4 (entry x support potential); construction).** C1 correction-and-copy hierarchy (shallow exact reward target). Each stage replaces C by D = C - E + EC, so that I - D = (I+E)(I-C), with E a detector-gated, soft-thresholded Neumann correction. Remaining large entries are then split over M copies, and rewards are carried by W_{l+1} = project(W_l + E_l W_l). After k stages 0 <= v(x) - W_k(primary copy) <= |S| 2^k 2^{-4(i+k)} (Hie.Prize.finish).

## Part A: Is the item in the Lean?

**lean_status: as in paper.** The hierarchy is formalized as a standalone matrix-level construction. This covers Hie.correct/adjust/residual (correction, I06-I07), Stg.next/newMat/copyZone (copy step, I11), Prize/plus/Correct.raise (reward identity, I12) and Prize.finish (the paper's 0 <= p0(x0) - W_l(z_l) <= |V0| 2^{-(H-1)l} with H = 4). It is consumed on the comparator chain through Stage.Matter.identity -> probes -> Rock.convince -> BPL_subset_L. Checked at text level only; I did not build. The orchestrator reports the comparator PASS on 2026-10-10.

**Gaps**

- NOT COMPILED BY ME: text-level reading only, because another process is building in the workspace. The comparator PASS (2026-10-10) is the orchestrator's; data/lean_checks.json had no 103 entry when read.
- Constants are specialized: H = 4 (rate j = 2^{-4j}), A = 1/4096 and Q = shoulder A A. Const {T,K,J,M} is existential (exists_const), so there are no numerals for k_*, D0 and so on.
- Detectors (Hie.U, Stg.update) are exact averages over a channel environment ZMod n with n prime; Prize.finish needs 2^{i+k} <= n. The paper's sampled detectors are the same object; the prime modulus is an implementation parameter.
- Comparator is weaker than the paper: only L = RL = BPL. Thm 1.2 (variable precision), Thm fixed-precision ((n+2)^{-d}), Cor. promise-bpl, Cor. certified-search and the compiler are NOT formalized. The Lean estimator has fixed error 1/32 (Equality.fixed_precision_estimator, Scope.Sane.shard).
- The surrounding route differs from the paper but does not touch C1: a Fourier "square torus gap" (AffineSampling.lean) replaces Shalom's property (T), and the Sec. 9 fingerprints are absent (novelty pass).
- Extractor correction: the novelty pass's "912 dependents (35% of DAG)" for residual/substochastic/factorial comes from Hie.kOK's `T.factorial` (Nat.factorial) being linked to Hie.factorial, which puts the lemma under every user of Wares/Const. Without that edge, residual has 254 and factorial 50 DAG dependents. The whole hierarchy module still has a 2,260-declaration downstream cone (44% of the 5,166-declaration DAG), so test 3 passes at module level.

**Comparator chain**

1. `OAI.ExactDerandomization.exact_logarithmic_space_derandomization (Equality.lean:104; comparator target)`
1. `OAI.ExactDerandomization.BPL_subset_L (Equality.lean:83)`
1. `OAI.ExactDerandomization.Grain.Rock.convince (FiniteFieldPrograms.lean:519)`
1. `OAI.ExactDerandomization.Stage.Matter.probes (ProbabilityDecision.lean:314)`
1. `OAI.ExactDerandomization.Stage.Matter.identity (ProbabilityDecision.lean:138)`
1. `OAI.ExactDerandomization.Hie.Prize.finish (ProbabilityHierarchy.lean:1268)`
1. `OAI.ExactDerandomization.Hie.Prize.all / Prize.Correct.raise (ProbabilityHierarchy.lean:1214 / 1176)`
1. `OAI.ExactDerandomization.Hie.Stg.commute / Stg.newGood / Stg.few_nodes (ProbabilityHierarchy.lean:1057 / 1010 / 1085)`
1. `OAI.ExactDerandomization.Hie.Stg.next / Stg.newMat / copyZone (ProbabilityHierarchy.lean:966 / 962 / 908)`
1. `OAI.ExactDerandomization.Hie.Stg.D = residual P.S P.C (P.corr n P.p.T) (ProbabilityHierarchy.lean:740 / 179)`
1. `OAI.ExactDerandomization.Hie.substochastic / Hie.factorial (ProbabilityHierarchy.lean:182 / 277)`
- Entry from the machine side: Stage.Raw.H and Raw.honestly (ProbabilityDecision.lean:51 / 54) build a Correct Prize from the configuration chain. The second branch is Matter.lineup -> cseq -> Stg.next (copy-zone size bound).

**Key declarations** (verbatim text is in downstream.json, `lean_source`)

| Declaration | Kind | File:line |
|---|---|---|
| `SB` | structure (support) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:31 |
| `combine` | def (item: correction product) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:66 |
| `correct` | def (item: soft-thresholded, column-gated correction) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:107 |
| `adjust` | def (item: Neumann-type iteration E <- fQ((C+EC)/f)g) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:161 |
| `residual` | def (item: D = C - E + EC) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:179 |
| `substochastic` | lemma (key property) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:182 |
| `factorial` | lemma (key property: ordered-support truncation) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:277 |
| `Stg` | structure (item: one stage) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:713 |
| `copyZone` | def (item: copy space V x {0..M-1}) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:907 |
| `OAI.ExactDerandomization.Hie.Stg.newMat / next / project` | def (item: copy step) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:961 |
| `few_nodes` | lemma (key property: active vertices at most double) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:1085 |
| `OAI.ExactDerandomization.Hie.Prize / plus / Correct` | structure + def (item: reward hierarchy W_{l+1} = project(W_l + E_l W_l)) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:1148 |
| `finish` | lemma (headline property of the item: shallow exact target) | OAI/Computability/Logspace/ProbabilityHierarchy.lean:1268 |
| `identity` | lemma (use: item applied at the machine start) | OAI/Computability/Logspace/ProbabilityDecision.lean:138 |
| `BPL_subset_L` | theorem (comparator side) | OAI/Computability/Logspace/Equality.lean:82 |

## Verdict on speedup
No strong device-reuse candidate. Every measurable Lean target (S1-S4) is a corollary of the theorem or of its proof. The open problems where the device would be genuinely new (O1, O2) are exactly where its hypotheses (time order, nonnegativity) fail.

## Top 5 (Lean-usable first)

1. **S1: PromiseBPL = PromiseL** (Lean-usable: yes). The only target that is statable in about 30 lines and has an exact internal baseline (BPL_subset_L, 20 lines; convince, 28 lines). Use it to calibrate the harness: with the full library minus Equality.lean's final theorems, a prover should finish in about 100 lines. Without the hierarchy cone (27,687 lines removed) it is as hard as the main theorem. It is a proof corollary, so a success here says nothing about a jump.

2. **S2: inverse-polynomial gap at threshold 1/2** (Lean-usable: yes). The best device-level measurement available. The accuracy is a parameter of the hierarchy (number of stages k in Prize.finish), which the Lean fixes at error 1/32. The control arm (Chernoff amplification inside BPL, then S1) separates "uses the device" from "uses the theorem". If the prover re-parametrizes Prize.finish rather than amplifying, that is weak evidence that the device is a reusable lever.

3. **S3: DAG absorption probabilities from an explicit matrix** (Lean-usable: yes). It tests portability. Prize.finish/Correct.raise are stated for any Prize, so a Prize built directly from an input matrix (as Raw.H does from the configuration chain) should drive identity/probes without the machine-configuration layer. The cost is about 150-250 lines of encoding. It is borderline because the same problem follows from S1 by a sampling reduction; record which route the prover takes.

4. **O1: BP_H L = L (no time bound)** (Lean-usable: yes). The open problem where the device's hypotheses fail exactly: there is no time order, so SB.loc and the factorial bound break. It is statable in about 40 lines (pInf as a supremum over t of acceptanceProbability). Low confidence, but this is the right place to look for a new idea, and a failure is informative.

5. **S4: certified accepting computations** (Lean-usable: yes). It needs the estimator at shifted starts (Prize.reach and child are start-generic) plus a bit-query formulation of a logspace function. It is a proof corollary of the same kind as S1/S2, so it is useful as a second calibration point.

## Speedup targets (known theorems)

### S1. PromiseBPL = PromiseL (paper Cor. cor:promise-bpl)
- **Statement:** Every promise problem (Y,N) separated with error 1/3 by a polynomial-time randomized logspace machine is separated by a total deterministic logspace machine.
- **Reference / status:** Paper conclusion.tex Cor. cor:promise-bpl; Pyne-Raz-Zhan 2023 (universal estimator from prBPL in SPACE[S]). Status: Proved in the paper (2026-09-23); NOT formalized in OAI (comparator covers languages only).
- **Current proof size:** Paper: 6 lines given Thm fixed-precision. Lean: no proof; expected edit of Equality.BPL_subset_L (lines 83-102, 20 lines) plus Grain.Rock.convince (FiniteFieldPrograms.lean:519-546, 28 lines) to quantify over Y and N separately: about 60-120 lines.
- **How the item helps:** convince only uses the gap hypotheses at the input x it decides, and fixed_precision_estimator holds for every input, so the promise version reuses the whole estimator unchanged. This is reuse of the item's own proof, not of the device in a new setting.
- **Counts as:** proof corollary / harness calibration. It does NOT count toward a confirmed jump.
- **Expected speedup:** high (with arm: about 100 lines; without arm: equivalent to re-proving the main theorem). **Confidence:** high.
- **Lean statement:**

```lean
def PrBPL : Set (Language × Language) := {YN | Disjoint YN.1 YN.2 ∧ ∃ (q w h : ℕ) (M : Machine q w h), M.LogSpace ∧ ∃ (c k : ℕ), 0 < c ∧ ∀ x : Word, M.HaltsBy x (polynomialClock c k x.length) ∧ (x ∈ YN.1 → (2/3 : ℚ) ≤ M.acceptanceProbability x (polynomialClock c k x.length)) ∧ (x ∈ YN.2 → M.acceptanceProbability x (polynomialClock c k x.length) ≤ 1/3)}
def PrL : Set (Language × Language) := {YN | ∃ (q w h : ℕ) (M : Machine q w h), M.Deterministic ∧ M.LogSpace ∧ ∀ x : Word, ∃ (t : ℕ) (b : Bool), (x ∈ YN.1 → b = true) ∧ (x ∈ YN.2 → b = false) ∧ ∀ coins, M.output (M.run x coins t).state = some b}
theorem prBPL_subset_prL : PrBPL ⊆ PrL
```
- **With arm:** Full OAI/Computability/Logspace library (39 files, 43,045 lines) except the target-specific glue named below. Item declarations (ProbabilityHierarchy.lean, 1,305 lines, 153 declarations): Hie.SB, combine, correct, adjust, residual, substochastic, factorial, kOK, Const, Stg, Stg.next/newMat/project, copyZone, Prize, Prize.plus/Correct/Correct.raise/iterate/finish. Remove only BPL_subset_L and exact_logarithmic_space_derandomization (Equality.lean:82-114) so the prover cannot pattern-match the final 30 lines.
- **Without arm:** Remove ProbabilityHierarchy.lean and its import cone (24 files, 27,687 lines: ProbabilityAtoms, HierarchicalEstimator, ProbabilityDecision, FiniteFieldPrograms, the Estimator*/Compression*/Evaluation files, UniformEstimator, Equality). What remains is the 14,053-line machine/plumbing layer (Deterministic, TransitionTables, CounterPrograms, ConfigurationGraph, RecursivePrograms, ContourTraversal, CatalyticComparison, DyadicArithmetic, AffineSampling, Amplification, ...). Caveat: the hierarchy cannot be removed without the estimator that consumes it, so 'without' also removes the estimator; this is a ceiling, not a clean single-device ablation.
- **Baseline formal proof:** No external formal proof. Internal reference: BPL_subset_L (Equality.lean:83-102, 20 lines) + convince (28 lines) on top of a 43,045-line development; comparator DAG 5,166 declarations.
- **Lean feasibility:** statable with < 300 lines of new definitions. Needs: OAI ExactDerandomization.Machine, LogSpace, HaltsBy, acceptanceProbability, polynomialClock (all in the comparator challenge file).. Missing: PrBPL / PrL definitions (about 20-30 lines). Compare against: Equality.lean BPL_subset_L (20 lines) + Rock.convince (28 lines); full development 43,045 lines / 39 files..

### S2. Inverse-polynomial gap at an arbitrary threshold (paper Thm fixed-precision, decision form)
- **Statement:** For every fixed d and every logspace polytime randomized M, the promise problem Y_d={x: p_M(x) >= 1/2+(n+2)^-d}, N_d={x: p_M(x) <= 1/2-(n+2)^-d} is in PromiseL.
- **Reference / status:** Paper Thm thm:fixed-precision (conclusion.tex:18-30) and Thm 1.2 (introduction.tex). Status: Proved in the paper; not formalized (Lean fixes the precision at 1/32 via shard / Matter.identity).
- **Current proof size:** Paper: about 2 pp. (proof of Thm fixed-precision) on top of the whole paper. Lean: none.
- **How the item helps:** Device-level: Prize.finish gives error |S| 2^k rate(k) for ANY k, so the target accuracy is a stage-count parameter (k = c*B with c depending on d). The Lean hardwires k = B and 64 bins (Scope.Sane.shard). The with-arm prover must re-parametrize the hierarchy depth and the estimator precision. Control route: amplify M by (n+2)^{2d} repetitions with an O(log n) counter (Chernoff) and apply S1; that route uses the item only through S1.
- **Counts as:** proof variant (re-parametrized device); weak reuse
- **Expected speedup:** med. **Confidence:** medium (the amplification control may be cheaper than re-parametrizing the device, which would itself be informative).
- **Lean statement:**

```lean
theorem vanishing_gap (d : ℕ) {q w h : ℕ} (M : Machine q w h) (hM : M.LogSpace) (c k : ℕ) (hc : 0 < c) (hH : ∀ x, M.HaltsBy x (polynomialClock c k x.length)) : (({x | (1/2 : ℚ) + 1/((x.length+2 : ℚ)^d) ≤ M.acceptanceProbability x (polynomialClock c k x.length)}, {x | M.acceptanceProbability x (polynomialClock c k x.length) ≤ 1/2 - 1/((x.length+2 : ℚ)^d)}) : Language × Language) ∈ PrL
```
- **With arm:** Full OAI/Computability/Logspace library (39 files, 43,045 lines) except the target-specific glue named below. Item declarations (ProbabilityHierarchy.lean, 1,305 lines, 153 declarations): Hie.SB, combine, correct, adjust, residual, substochastic, factorial, kOK, Const, Stg, Stg.next/newMat/project, copyZone, Prize, Prize.plus/Correct/Correct.raise/iterate/finish. Plus S1's PrL definitions. Keep Prize.finish generic; remove Equality.lean's two final theorems.
- **Without arm:** Remove ProbabilityHierarchy.lean and its import cone (24 files, 27,687 lines: ProbabilityAtoms, HierarchicalEstimator, ProbabilityDecision, FiniteFieldPrograms, the Estimator*/Compression*/Evaluation files, UniformEstimator, Equality). What remains is the 14,053-line machine/plumbing layer (Deterministic, TransitionTables, CounterPrograms, ConfigurationGraph, RecursivePrograms, ContourTraversal, CatalyticComparison, DyadicArithmetic, AffineSampling, Amplification, ...). Caveat: the hierarchy cannot be removed without the estimator that consumes it, so 'without' also removes the estimator; this is a ceiling, not a clean single-device ablation. Control arm: with-arm library plus Amplification.lean generalized to n^{2d} repetitions (measures whether the device or amplification is the cheaper route).
- **Baseline formal proof:** None external. Internal: fixed_precision_estimator (Equality.lean:70-79) is the d = O(1), error 1/32 instance.
- **Lean feasibility:** statable with < 300 lines of new definitions. Needs: S1 definitions; OAI Machine.acceptanceProbability; ℚ arithmetic.. Missing: PrL (shared with S1). Compare against: none external; fixed_precision_estimator (10 lines) + the 43,045-line development.

### S3. Absorption probabilities of explicitly given time-ordered (DAG) substochastic matrices, decided in deterministic logspace
- **Statement:** Given a strictly upper-triangular nonnegative rational matrix C (row sums <= 1, binary entries of poly bit-length), a 0/1 reward vector e and an index s, decide whether ((I-C)^{-1} e)_s >= 1/2+1/n or <= 1/2-1/n, in deterministic logspace.
- **Reference / status:** Classical BPL-complete formulation (Saks survey; AKMPSV20 for undirected/Eulerian variants). Follows from S1 by a logspace sampler for rational transitions. Status: Follows from the paper (via S1); not formalized.
- **Current proof size:** Via S1: reduction from the matrix to a randomized machine (sampling rational transitions bit by bit), about 1-2 pp. Direct device route: build a Hie.Prize from the matrix exactly as Raw.H builds one from the configuration chain (ProbabilityDecision.lean:51-52), then reuse identity/probes.
- **How the item helps:** Prize.finish and Correct.raise are stated for an arbitrary Prize, i.e. any strictly forward substochastic matrix with v = W + Cv. The direct route skips the machine model entirely, so this is the cleanest test of whether the hierarchy is a portable lemma or is welded to the configuration-graph encoding.
- **Counts as:** direct device instance on a new input format (borderline: the problem is also a corollary of S1)
- **Expected speedup:** med. **Confidence:** medium.
- **Lean statement:**

```lean
Encode (C, e, s) as a Word via a fixed binary format (decoder about 150-250 lines). Statement: theorem dag_absorption_prL : (YesDAG, NoDAG) ∈ PrL, with YesDAG = {w | decode w = some (C,e,s) ∧ 1/2 + 1/len w ≤ absorb C e s}, absorb C e s := ((1 - C)⁻¹ e) s computed as the finite Neumann sum over the strictly upper-triangular C (Matrix.mulVec, nilpotent sum).
```
- **With arm:** Full OAI/Computability/Logspace library (39 files, 43,045 lines) except the target-specific glue named below. Item declarations (ProbabilityHierarchy.lean, 1,305 lines, 153 declarations): Hie.SB, combine, correct, adjust, residual, substochastic, factorial, kOK, Const, Stg, Stg.next/newMat/project, copyZone, Prize, Prize.plus/Correct/Correct.raise/iterate/finish.
- **Without arm:** Remove ProbabilityHierarchy.lean and its import cone (24 files, 27,687 lines: ProbabilityAtoms, HierarchicalEstimator, ProbabilityDecision, FiniteFieldPrograms, the Estimator*/Compression*/Evaluation files, UniformEstimator, Equality). What remains is the 14,053-line machine/plumbing layer (Deterministic, TransitionTables, CounterPrograms, ConfigurationGraph, RecursivePrograms, ContourTraversal, CatalyticComparison, DyadicArithmetic, AffineSampling, Amplification, ...). Caveat: the hierarchy cannot be removed without the estimator that consumes it, so 'without' also removes the estimator; this is a ceiling, not a clean single-device ablation.
- **Baseline formal proof:** none
- **Lean feasibility:** statable with < 300 lines of new definitions. Needs: Mathlib Matrix, Matrix.mulVec, Finset sums; OAI Word/Machine; S1 PrL.. Missing: binary encoding/decoder of rational matrices into Word (about 150-250 lines); PrL (from S1). Compare against: none.

### S4. Certified accepting computations (paper Cor. cor:certified-search)
- **Statement:** If p_M(x) >= (n+2)^-d then a deterministic logspace transducer outputs a coin string on which M accepts x.
- **Reference / status:** Paper conclusion.tex Cor. cor:certified-search; cf. Cheng-Hoza 2022 (hitting sets imply L = BPL), which this is the white-box converse of. Status: Proved in the paper; not formalized.
- **Current proof size:** Paper: about 1-2 pp. (prefix self-reduction using variable-precision estimates).
- **How the item helps:** Prefix-by-prefix search needs the estimator at a shifted start configuration (Matter.x0 replaced by the configuration after the prefix): Prize.finish and Prize.reach are already start-generic (child H x k for any x in S).
- **Counts as:** proof corollary (self-reduction on top of S2)
- **Expected speedup:** med. **Confidence:** medium.
- **Lean statement:**

```lean
Needs a transducer notion (the OAI model has deciders only). Language form avoiding output tapes: {(x, π) | π is a prefix of the lexicographically least accepting coin string chosen by the procedure} ∈ L, or: ∀ x with p ≥ (n+2)^-d, ∃ deterministic logspace machine D with D accepting (x, i) iff bit i of a fixed accepting coin string is 1.
```
- **With arm:** Full OAI/Computability/Logspace library (39 files, 43,045 lines) except the target-specific glue named below. Item declarations (ProbabilityHierarchy.lean, 1,305 lines, 153 declarations): Hie.SB, combine, correct, adjust, residual, substochastic, factorial, kOK, Const, Stg, Stg.next/newMat/project, copyZone, Prize, Prize.plus/Correct/Correct.raise/iterate/finish. Plus S2.
- **Without arm:** Remove ProbabilityHierarchy.lean and its import cone (24 files, 27,687 lines: ProbabilityAtoms, HierarchicalEstimator, ProbabilityDecision, FiniteFieldPrograms, the Estimator*/Compression*/Evaluation files, UniformEstimator, Equality). What remains is the 14,053-line machine/plumbing layer (Deterministic, TransitionTables, CounterPrograms, ConfigurationGraph, RecursivePrograms, ContourTraversal, CatalyticComparison, DyadicArithmetic, AffineSampling, Amplification, ...). Caveat: the hierarchy cannot be removed without the estimator that consumes it, so 'without' also removes the estimator; this is a ceiling, not a clean single-device ablation.
- **Baseline formal proof:** none
- **Lean feasibility:** statable with < 300 lines of new definitions. Needs: OAI Machine, extendCoins, run; S1/S2 definitions.. Missing: bit-query formulation of a logspace function (about 50-100 lines); S2. Compare against: none.

## Open or new problems

| ID | Problem | Status | Obstruction match | Payoff / confidence / difficulty | Lean |
|---|---|---|---|---|---|
| O1 | BP_H L = L: bounded-error logspace machines that halt with probability 1 but have NO polynomial time bound | open as far as I could find (snippet-level; the original Saks-Zhou model definition was not read) | exact: the device needs a strictly forward (time-layered) chain. SB.loc requires x<y and the factorial bound counts ordered supports (Hie.sub, sub_choose). Halting-a.s. chains have cycles and cannot be layered in polynomial size. | high (removes the polynomial-time hypothesis from Thm 1.1) / low / hard | statable with < 300 lines of new definitions |
| O2 | Logspace approximation of absorption/hitting probabilities in general directed (cyclic) chains with exponential condition number | open for general directed chains (polynomially conditioned chains reduce to the paper via Neumann truncation, a corollary) | same as O1: the hierarchy needs a time order | high / low / hard | statable with < 300 lines of new definitions |
| O3 | Randomized vs deterministic catalytic logspace for small catalysts (CBPL vs CL outside c = 2^{Θ(s)}) | open in the general parameter range (search snippet; not verified) | partial: the device is white-box on a configuration graph; with a catalyst the graph has 2^{s+c} vertices and the hierarchy's per-stage cost is log|V|. It could help only if the catalyst coordinates can be kept implicit, as the paper keeps matrices implicit. | medium / low / hard | needs major new library |
| O4 | Constant-visit two-way random tapes: BPL with each random cell visited O(1) times | open (polylog space known per the paper's citation) | partial: the chain on configurations is no longer Markov in fresh bits; the device needs read-once randomness. | medium / low / moderate-hard | statable with < 300 lines of new definitions |
| O5 | BQL vs L (unitary / signed transition products) | open | the device needs nonnegativity: SB.nn, Fgrow (monotonicity of the correction) and mono_steps use it. Signed entries break the potential. | high / very low / very hard | needs major new library |

- **O1.** Is every language decided with bounded error by a randomized logspace machine that halts almost surely (expected time possibly 2^{2^{O(log n)}}) in L? Reference: Saks-Zhou, JCSS 58 (1999): BP_H SPACE(s) ⊆ DSPACE(s^{3/2}) per a course-report snippet (improving the earlier s^2 bound); the paper's Thm 1.1 requires polynomial time. (https://www.cmi.ac.in/~somnathb/coursework/CT2/cpth_report.pdf). Adaptation: Replace time layering by an SCC/absorbing decomposition; the identity I-D=(I+E)(I-C) still holds for cyclic C, but the factorial truncation and few_nodes need a new potential. Test: does the hierarchy survive on a strongly connected 2-cycle gadget?
- **O2.** Given a substochastic P on n states with (I-P) invertible, approximate ((I-P)^{-1} e)_s to ±1/poly in deterministic O(log n) space, with no bound on ||(I-P)^{-1}||. Reference: Ahmadinejad-Kelner-Murtagh-Peebles-Sidford-Vadhan FOCS 2020 (Eulerian / undirected); Murtagh-Reingold-Sidford-Vadhan (undirected Laplacians, arXiv:1708.04634). (https://arxiv.org/pdf/1708.04634). Adaptation: As O1.
- **O3.** Is CBSPACE[s,c] = CSPACE[s,c] for catalyst sizes c far below 2^{Θ(s)}? Reference: Cook-Li-Mertz-Pyne, STOC 2025 (ECCC TR24-106): unconditional CBPL = CL only for c = 2^{Θ(s)} (per a 2026 citing paper's summary). (https://arxiv.org/pdf/2504.08444). Adaptation: Run the hierarchy on the catalyst-free projection, using CatalyticComparison-style restoring tests (C9, N0) for the catalyst.
- **O4.** Is polytime logspace with a two-way random tape visited O(1) times per cell equal to L? Reference: Cheng-Wu, arXiv:2609.23603 (2026), Theorems 5-6: polylog-space simulation (as cited in the paper's introduction). (https://arxiv.org/abs/2609.23603). Adaptation: Compose Cheng-Wu's reduction (if it outputs a read-once program of poly size) with the device; if so this is a corollary, otherwise open.
- **O5.** Can bounded-error quantum logspace be simulated in deterministic logspace? Reference: Hoza 2021 weighted pseudorandomness (signed weights) and Chen-Cohen-Doron-Khaskelberg-Ta-Shma 2026, as cited by the paper. (https://eccc.weizmann.ac.il/report/2023/040/download). Adaptation: Unlikely. Listed as an expected failure that calibrates negative control N2.

## Theorem corollaries (do not count as reuse)

- Undirected s-t connectivity in L (Reingold 2005/2008) from USTCON in RL (Aleliunas-Karp-Lipton-Lovasz-Rackoff 1979) plus RL = L. Lean: statable with < 300 lines (graph encoding into Word); proof = AKLLR random walk (cover time) + the comparator theorem. No Lean formalization of Reingold found (the 2025 formalization is in bounded arithmetic VL, not a proof assistant). Large proof-size contrast but theorem-level reuse only.
- BPL ⊆ DSPACE(log^{3/2} n) (Saks-Zhou 1999), BPL ⊆ DSPACE(log^{3/2} n/sqrt(log log n)) (Hoza 2021), BPL ⊆ SC (Nisan 1994): immediate since L is contained in all of them.
- BPL ⊆ CL (catalytic logspace; Cook-Li-Mertz-Pyne line): immediate from L ⊆ CL.
- BPSPACE(s) with time 2^{O(s)} equals DSPACE(s) for space-constructible s >= log n, by padding.
- Cheng-Hoza 2022 conditional (hitting sets imply L = BPL): its conclusion is now unconditional; its premise is NOT implied (see negative control N4).
- Erdős-style: ZPL = RL = L; prRL = prL via S1.

## Negative controls

- **BPL ⊆ DSPACE(log^2 n) (Borodin-Cook-Pippenger 1983; Nisan 1992): no-speedup control.** Every BPL language is decided deterministically in O(log^2 n) space. Why the device must fail: Repeated squaring of the time-layered transition matrix with truncation already gives this in a few pages. The hierarchy evaluated by plain recursion also gives log^2, but should not be cheaper. If the with-arm wins big here, the harness is rewarding library size, not the device. Lean: statable with < 300 lines of new definitions; compare against: none.
- **Signed transitions: the correction hierarchy is false without nonnegativity (expected proved-false analogue).** The analogue of Hie.mono_steps / Hie.substochastic with SB.nn weakened to |C x y| <= k*f is false (expected: a counterexample on a 3-node strictly forward chain with one negative entry). Why the device must fail: Fgrow and mono_steps use C >= 0 to make the soft-thresholded Neumann iteration monotone. With signed C the residual can leave [0,(t+1)f]. A prover with the device must refute this variant, not prove it. The counterexample was not constructed or checked here; building it is part of the control. Lean: statable now; compare against: Hie.substochastic (ProbabilityHierarchy.lean:182-222, 41 lines) for the nonnegative case.
- **Directed s-t connectivity (NL ⊆ L): must-not-prove control.** STCON in L. Why the device must fail: Reducing STCON to a probability makes the relevant path weight as small as n^{-n}, far below the additive accuracy |V0| 2^{-(H-1)L} of the shallow target. If the device appeared to decide STCON, NL = L would follow and the run is buggy. Lean: statable with < 300 lines of new definitions; compare against: none.
- **Black-box derandomization: O(log n)-seed hitting-set generators for width-n ROBPs.** Construct, in logspace, a 1/2-hitting set of polynomial size for all width-n, length-n read-once branching programs. Why the device must fail: The hierarchy is white-box: detectors (Hie.U) and the copy routing read the transition matrix. A generator cannot see the program, so the device should give no HSG. Cheng-Hoza's implication runs only HSG -> L = BPL. Lean: statable with < 300 lines of new definitions; compare against: none.

## Release reuse

- None found. grep of all preprint .tex for "substochastic" and "copy hierarchy" hits family 103 itself plus unrelated statistical-physics families (Lipschitz surfaces, FK maps, Heisenberg). CONTENTS.md search for logspace / derandomi / catalytic / branching program / BPL finds only 103 and 137.
- Could use it: 137 (one-tape time T simulated in O(T^{2/5} polylog) space): deterministic time-space simulation with no randomness, so the device is irrelevant. Listed only to record that the closest release neighbour does not reuse it.
- Lean note: Text-level only. The hierarchy module ProbabilityHierarchy.lean imports only AffineSampling and is imported by ProbabilityAtoms and HierarchicalEstimator; its import cone is 24 files / 27,687 lines, i.e. every estimator file. A clean "without device" arm therefore cannot keep the estimator.

## Precedent

**Earlier equivalent found: no.** No earlier equivalent of the correction-and-copy hierarchy was found. This rests on the novelty pass's searches plus one 2026-10-10 search for reactions to the L = BPL claim, which found none indexed. The hierarchy's parts are individually precedented (left preconditioning, ILUT-style thresholding, AKMPSV lifts, Saks-Zhou rounding). Downstream, every known theorem I found that the device reaches is a corollary of the main theorem or of its proof (S1-S4, theorem_corollaries). No KNOWN theorem outside that cone was identified where the hierarchy, rather than L = BPL itself, would shorten a proof. Strict verdict: no strong device-reuse speedup candidate found; the measurable Lean targets are calibration-grade.

Nearest neighbours:
- Cohen-Doron-Sberlo-Ta-Shma STOC 2023 (precision-alternating Richardson recursion)
- Ahmadinejad-Kelner-Murtagh-Peebles-Sidford-Vadhan FOCS 2020 (cycle lifts, Eulerian inversion)
- Saks-Zhou 1999; Hoza 2021 (recursive powering with random rounding; weighted PRGs)
- Pyne-Raz-Zhan 2023 (universal estimator from prBPL in SPACE[S])

Post-release use: None found (WebSearch 2026-10-10: no indexed discussion of a 2026 L = BPL proof).

Caveats: The comparator PASS (2026-10-10) certifies the class equality; it does not certify Thm 1.2, the promise corollary, certified search or the compiler, none of which is formalized. The novelty pass's "912 dependents (35% of DAG)" for residual/substochastic/factorial is an extractor artifact (Hie.kOK's Nat.factorial misresolved to Hie.factorial). The corrected per-declaration figures are residual 254 and factorial 50. The module-level cone is 2,260/5,166 (44%), so test 3 still passes.

## Search log

- Local: read the brief, the 248 template, the 103 novelty/family files, the comparator config, lean/docs/103.md, ProbabilityHierarchy.lean (all 1,305 lines), ProbabilityDecision.lean, Equality.lean, convince in FiniteFieldPrograms.lean, and introduction.tex + conclusion.tex. Lean was NOT built or run (another process is building in the workspace); everything is text-level.
- Local DAG: BFS over data/items/103_lean.json uses-edges from the comparator target to Hie.* declarations. Found the spurious kOK -> factorial edge and recomputed dependents.
- Local release: grep CONTENTS.md for logspace|derandomi|catalytic|branching program|BPL|random walk; grep all preprint .tex for "substochastic|copy hierarchy". No device reuse.
- WebSearch "Cook Li Mertz Pyne structure of catalytic space CBPL = CL": CLMP STOC 2025; unconditional collapse only for c = 2^Θ(s) (snippet from arXiv 2504.08444 / 2510.12005).
- WebSearch "Saks Zhou BP_H SPACE(S) halting with probability one": course-report snippet BPHSPACE(s) ⊆ DSPACE(s^{3/2}); the model definition was not confirmed.
- WebSearch "L = BPL 2026 OpenAI reaction": nothing indexed about the 2026 claim.
- WebSearch "Lean 4 formalization Savitch / Reingold / space complexity": none found; Reingold formalized only in bounded arithmetic VL (2025).
- WebFetch not attempted (arxiv.org blocked per environment); all literature claims are snippet-level.

## Sources

- data/pilot/103/novelty.json, novelty.md, family.json
- data/items/103_lean.json (text-level DAG; recomputed dependents with the spurious Hie.kOK -> Hie.factorial edge removed)
- data/raw/openai-math/lean/OAI/Computability/Logspace/{ProbabilityHierarchy,ProbabilityDecision,Equality,FiniteFieldPrograms,AffineSampling}.lean
- data/raw/openai-math/lean/ComparatorChallenges/LogspaceEquality.{json,lean}; lean/docs/103.md
- data/raw/openai-math/preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/sections/{introduction,conclusion}.tex
- https://www.cmi.ac.in/~somnathb/coursework/CT2/cpth_report.pdf
- https://courses.cs.cornell.edu/cs6815/2018fa/Lec_17.pdf
- https://arxiv.org/pdf/2504.08444
- https://arxiv.org/pdf/2510.12005
- https://arxiv.org/pdf/1708.04634
- https://lacker.io/complexity/problems/bpl-derandomization-exponent.html
- https://www.tcs.tifr.res.in/web/events/1689
