# Family 293: Invariant projections, hyperinvariant subspaces, and transitive algebras

Family-analyst report covering the paper and the Lean, both manuscripts. Prepared 2026-10-10 for the influential-problems pass. Source: `openai/math` at commit fd4aeeb.

**The Lean was read at text level only.** It was not compiled; the orchestrator compiles the comparators. Web claims rest on search-result snippets: WebFetch failed (ar5iv DNS error) and arXiv is blocked.

| id | Manuscript | Date | Lean |
|---|---|---|---|
| BI | *Backward intertwiners and a transitive commutant* | 2026-09-27 | `OAI/Analysis/BackwardIntertwiners` (5.8k lines, imports only Mathlib) |
| IP | *Invariant-projection counterexamples for every irrational rotation* | 2026-09-27 | `RotationWeights` (18.4k), `IrrationalRotation` (97.3k), `FiniteFactor` (22.6k), `BrownMeasure` (1.8k), `Hyperinvariant` (0.4k) |

## 1. Which problem is solved

**The hyperinvariant-subspace problem (HSP), not the invariant-subspace problem (ISP).**
- The HSP asks: does every nonscalar bounded operator on a separable infinite-dimensional complex Hilbert space have a nontrivial closed subspace invariant under its whole commutant? It goes back to Douglas–Pearcy 1972 and Kim–Pearcy–Shields 1976, and is open in particular for quasinilpotent operators.
- Claimed answer: **no**. The counterexample is nonzero and norm-quasinilpotent. Its commutant is a proper, SOT-closed, transitive unital algebra.
- Relation to the ISP:
  - An ISP counterexample would automatically be an HSP counterexample. The converse fails.
  - The operators here have many ordinary invariant subspaces, e.g. `L^2(X; K_{>=h})` in BI (conclusion.tex:27-32).
  - So the ISP on Hilbert space is **untouched**. Enflo's 2023 claimed positive ISP solution is not contradicted.
  - Kérchy–Pearcy's claimed equivalence HSP⇔ISP was withdrawn after Bercovici found a counterexample to its Theorem 3. If that equivalence and this family were both correct, the ISP would fail. BI explicitly says the two problems "must remain distinct".
- By-products and conflicts:
  - **The transitive algebra problem is answered negatively.** The commutant is a non-dense transitive SOT-closed algebra. This is a corollary.
  - **Zhu–Fang–Shi's question is answered negatively.** The question (Math. Scand. 120 (2017) p.264) concerns u f(v) in the hyperfinite II_1 factor with Fuglede–Kadison determinant 0. The answer holds at every prescribed irrational angle.
  - **The relative ISP in the hyperfinite II_1 factor is answered negatively** in the case Haagerup–Schultz leave open (Brown measure a point mass). The product model has Brown measure δ_0.
  - **It refutes Cho–Ko–Lee 2017, Cor 2.8**, as IP's Remark 1.5 itself states.
  - **It contradicts claimed *affirmative* HSP solutions:** Garayev, arXiv 2607.16373 (Jul 2026), and Sa Ge Lee, arXiv 2306.13940. Both are known from snippets only.

## 2. Main statements and Lean match

**BI Cor 1.2** (introduction.tex:72-77): "Every infinite-dimensional separable complex Hilbert space admits a nonzero bounded norm-quasinilpotent operator with no nonzero proper closed hyperinvariant subspace. Its commutant is a proper strongly closed unital transitive complex operator algebra."

How the BI construction works:
- **The fibers.** `S` is the direct integral, over the 2-adic odometer `x ↦ x+1` on Z_2, of bilateral weighted shifts `S_x e_j = β_j(x) e_{j+1}`.
- **The weights.** The log-weights are `a_k^±(x) = c(k+1) + J_m + D·T_m(x)` and `c(k+1) + J_m + D(N_m−1−T_m(x))`, on blocks `I_m = [8^{m−1}, 8^m)`, with c=10 and D=100.
- **Each fiber is unicellular (Domar-type):** its invariant subspaces are exactly the tails.
- **A backward intertwiner.** There is a contraction `V ∈ {S}'` with `(Vf)(θx) = V_x f(x)` and `V_x e_j = b_j(x) e_{j−1}`. It maps the tail `K_{≥h}` at x densely onto `K_{≥h−1}` at θx.
- **Descent closes the argument.** An invariant subspace of alg(S, V, M_g) would be a field of tails `K_{≥s(x)}` with `s(θx) ≤ s(x)−1`. That is impossible on a probability space.

**IP Thm 1.1** (00-introduction.tex:33-41): for every irrational θ there is a continuous f: T→[0,1] with these properties:
- f vanishes only at 1;
- ∫ log f = −∞;
- U f(V) has no invariant projection in R_θ other than 0 and 1.

**IP Cor 1.4** derives the HSP from this via Dykema's Prop 2.1: hyperinvariant projections of T ∈ M lie in M.

Six comparators, all with `definition_names: []`:

| Comparator | Target | Route | Match |
|---|---|---|---|
| BackwardIntertwiners | `direct_algebra_corollary` | BI direct | exact to BI Cor 1.2 |
| HyperinvariantSubspaces | `Hyperinvariant.main_theorem` | **IP appendix product model** (FiniteFactor) + Dykema bridge | same FullClaim |
| IrrationalRotation | `prescribed_irrational_counterexample`, `product_realization` | IP circle and product models | exact to IP Thm 1.1 + quasinilpotence + FK det 0 |
| ContinuousCircleWeight | `main_theorem` | RotationWeights | **∃θ only** (an earlier, weaker existence result) |
| FiniteFactor | `main_theorem` | product model | II_1 factor with separable predual; **hyperfiniteness not stated** |
| ProductBrown | `productBrown` | BrownMeasure | Brown measure δ_0 (supporting result) |

FullClaim (statement check):
- `TransitiveCommutant T` holds when every closed submodule invariant under all A with A*T = T*A is ⊥ or ⊤.
- The rest of FullClaim: `commutant T ≠ ⊤`, the commutant is SOT-closed (SOT is the topology induced by pointwise evaluation), `T ≠ 0`, and ‖T^n‖^{1/n} → 0.
- Faithful to the paper. **The HSP is formalized twice, by independent constructions.**

## 3. Trust surface

Grep scope: 1,306 files, about 146k lines.

| Pattern | Count |
|---|---|
| `sorry` / `axiom` / `admit` / `native_decide` / `implemented_by` / `extern` / `unsafe` / `opaque` / `set_option` / `#eval` | 0 |
| plain `decide` | 106, all Bool coercions such as `decide (i ∈ I)` |
| `run_cmd Lean.modifyEnv fun env => Lean.Meta.auxLemmasExt.setState env {}` | 2 in the solution (BrownMeasure/Model.lean:91, IrrationalRotation/Model/Product.lean:116), plus 2 in the IrrationalRotation challenge |

**Flag for the orchestrator:**
- the `run_cmd` environment edits;
- the empty `definition_names` in all six configs. Confirm that the statement definitions are locked.

## 4. Labels

- **A2**, existential counterexample. Explicit rate: `‖S^n‖ ≤ exp(−10⌊(n+1)²/4⌋)`.
- **B2**, refutes the HSP. Flags:
  - *full only together with prior results*: no. The work is self-contained; Domar's criterion is re-proved.
  - *adds corollaries for other conjectures*: **yes**. The transitive algebra problem, the ZFS question, the relative ISP in R, and Cho–Ko–Lee.
- **C1** primary.
  - Secondaries:
    - C3: descent/contradiction, and the obstruction in IP.
    - C4: Domar convolution estimates; the IP sampling and tail chains.
    - C2: IP's recursive parameter choice only.
    - C5: weak. Dykema's Prop 2.1 is cited but also re-proved.
  - Computer-assisted: **no**.
  - ih_strengthened: **no**.
- **D3, provisional**, confidence 0.45. It rests on E1 (below).
- Provenance flag: **no**. The only "prior" model output is the same-day companion: BI imports two elementary lemmas from IP.
- **E. Fields.**
  - Problem field: operator algebras / operator theory (MSC 47A15, 47L, 46L10, 47B37).
  - Lean-dir field: Analysis.
  - Method fields, essential to the BI route:
    - weighted shifts (Domar);
    - ergodic theory (odometer, recurrence);
    - measure theory and direct integrals;
    - discrete convexity;
    - p-adic Haar measure.
  - Method fields added by the IP route, also essential:
    - von Neumann algebras: crossed products, traces, FK determinant, affiliated operators;
    - probability: couplings, conditional independence, Kakutani-type product densities;
    - harmonic analysis: Fejér kernel, equidistribution.
  - Method field cited as background: Brown measure and free probability (Haagerup–Schultz, Dykema–Haagerup DT-operators).
  - Cross-field count: 6.

## 5. Items (43; full list in family.json)

BI items:
- B01–B03, the vocabulary and base: N0.
- B08–B12, the Domar-type criterion, the support separation and the convex envelope / slope matching: N0–N1. The paper says it "follows the method of Domar".
- B13–B15, the residues, ergodicity and fiber verification: N0–N1.
- **B16, the two-ended residue-corrected weights: N3 candidate** (part of E1).
- **B17, the two-ended drift lemma, with an a.e.-finite non-integrable C(x): N3 candidate** (part of E1).
- **B18, the backward intertwiner V:**
  - Closed form: `b̃_j(x) = w_{j−1}(θx)/(e^c w_j(x))`.
  - It is normalized by the fiberwise sup L(x).
  - **Provisional grade: N3, F3** (F5 flavour).
- B19–B21, the fiber identities, the strict-descent lemma (Poincaré recurrence) and the assembly: N1.
- B22, the structural side results (atomic/diffuse polar algebras, non-compactness, Arveson inapplicable): N1, corollary-only.

IP items:
- C01, C03, C09, C14, C20, the standard tools, Dykema Prop 2.1 and ZFS Thm 2.3: N0.
- C06, C07, C10, C11, C19, the sampling kernels, Laurent compactness, positive diagonal, compact transfer and coboundary smoothing: N1.
- C08 and C12, the prescribed-angle parameters and the measurable cost cocycle of rare drops: N2.
- C13, the rational-graph transfer: N2.
- C15–C17, the ordered biased couplings and the **conditional convolution obstruction**: N2, borderline N3.
- C18, affiliated trace-preserving transport: N2 (Mori, Prop 3.1).
- C21, the product realization: N2.

## 6. Proof architecture

**The BI direct route** (Lean DAG about 2.5k lines):
1. **Domar-type criterion.** This branch is about 43% of the lines.
2. **2-adic weights.** Every fiber satisfies the criterion, and S has a uniform power bound.
3. **Two-ended drift.** Solve the commutation recurrence, show the coefficients decay at both ends, and normalize to get the contraction V. This branch is about 37% of the lines.
4. **Descent.** Use the field-of-tails labels, or in Lean the support order plus ergodic late-intersection recurrence. This step is about 8% of the lines.
5. **Commutant lemma and unitary transport.**

**The IP route:**
1. Choose parameters at the prescribed angle. Trial phases are picked first and then realized by divisible characters.
2. Set up the measurable cost cocycle g_*. Derive a projection field with covariance and a positive central diagonal.
3. Prove the invariance identity on orbit pairs. Transfer it to rational translations and then to ordered biased couplings.
4. Run the conditional convolution obstruction.
5. Make the weight continuous via a coboundary relocation plus affiliated transport. Quasinilpotence follows.
6. Apply Dykema's bridge to reach the HSP.

**The Lean HSP comparator uses the appendix product model, not the circle model.**

Lean route differences in BI:
- transitivity uses support order plus recurrence, not tail labels;
- goodBase = Z_2 minus the integers replaces Borel–Cantelli;
- the error bound is 400√n;
- rawBackward is given in closed form.

## 7. Eureka candidates

**E1. Backward intertwiner across odometer fibers.** Items B16, B17, B18. Provisional **N3, F3**.
- For:
  - It is the only non-classical step.
  - It reduces the HSP to a 1-D descent.
  - It is syntactically tiny (the corrections ±D·T_m).
  - It is invisible in the problem statement.
  - It is bounded only across fibers, with pointwise-finite but non-integrable constants.
  - No neighbour turned up in searches, which found only Bastian 1976 (direct-integral decomposition) and Jódar 1986 (commutants of weighted shifts).
- Against:
  - Commutation forces the recurrence, so after the architecture is chosen only the weight design remains.
  - The architecture shadows the known II_1-factor route (Dykema Prop 2.1; the commutant contains JMJ), which the same release's companion follows.
  - The drift/coboundary pattern is common in ergodic cocycle theory.
  - There is no reasoning trace.

**E2. Conditional convolution obstruction on ordered biased couplings.** Items C15–C17. Provisional N2, borderline N3.
- The key trick is to condition one Cauchy–Schwarz factor on each endpoint, which avoids a union bound.
- Against:
  - Strassen and Edwards supply the coupling theory.
  - The rest is an elementary compactness lower bound.
  - It is heavy technique rather than a short cut, and BI shows it is not needed for the HSP.

**E3. Rare-drop cost cocycle at a prescribed angle.** Items C08, C12. Provisional N2. It combines classical step cocycles with successive-approximation choices.

**E4. Affiliated trace-preserving transport.** Items C18, C19. Provisional N2 (Mori).

**E5. Domar criterion and descent.** Items B09, B20. Provisional N0–N1.

## 8. Correctness and trust concerns

1. **Extraordinary claim.**
   - The HSP and the transitive algebra problem are long open. The Chalendar–Partington 2025 survey (snippet) lists the ISP as open on Hilbert space.
   - I read the BI proof in full and found no gap.
   - Checks I did:
     - the weight monotonicity;
     - the commutation identity;
     - the two-ended decay, roughly −90 per step at each end;
     - V is a contraction;
     - the descent argument;
     - growth-class hyperinvariant manifolds are dense here, so nothing obvious is missed.
   - The Domar-type criterion was not checked line by line, but it is formalized.
   - IP was read but not verified in detail.
   - **Trust should rest on compiling the BackwardIntertwiners and HyperinvariantSubspaces comparators.**
2. **Conflicts with the literature** (both sides cannot be right):
   - Cho–Ko–Lee 2017 Cor 2.8 (published);
   - Garayev 2026 and Lee 2023 (affirmative HSP preprints);
   - the withdrawn Kérchy–Pearcy equivalence.
3. **Comparator configs.** `definition_names` is empty, and there are `run_cmd` environment edits (see §3).
4. **Hyperfiniteness is not formalized as a property.** FiniteFactor states only II_1. IrrationalRotation uses the concrete R_θ, whose hyperfiniteness is classical.
5. **Catalog inconsistency.** The catalog lists IP as not formalized, but lean/docs/293.md links four comparators to it.

## 9. Extraction friction

- **BI has no definition environments.** The weights, V, X_* and L(x) are defined only in display math.
- **The comparators do not line up with the manuscripts.** Six comparators span two manuscripts and six dirs, and the HSP comparator runs through IP's appendix.
- **IrrationalRotation is very large:** 97k lines in 933 files. The extractor's DAG misses some links.
- **Namespaces do not match the family id.** `Invariant233` and `Hyperinvariant233` are not 293.
