# Family 257: A hyperbolic group without a geometric CAT(0) action

Paper: `preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026` (author "OpenAI", 25 Sep 2026). Lean: `OAI/Geometry/HyperbolicGroups` (422 files, 57,027 lines). Comparator: `HyperbolicObstruction`. No reasoning trace. Machine-readable version: `family.json`.

## Main statement
**Thm 1.1** (01-introduction.tex:6-13): there is a finite, connected, 2-dimensional, aspherical simplicial complex K with a linear combinatorial disk-filling inequality, such that π₁K has no geometric (proper, cocompact, isometric) action on any proper complete CAT(0) space. Consequences:
- π₁K is word-hyperbolic;
- no finite complex homotopy equivalent to K carries a locally CAT(0) metric, and hence none carries a locally CAT(−1) metric.

This answers negatively Gromov's realization question (BMS Problem H11; Stark 2025 OP 2.15; Duchesne–Simon 2026 Question W). The proof is an existence argument and does not give an effective size for K (01:15).

**Comparator** (`OAI.HyperbolicObstruction.main`). It is faithful but **weaker than the headline**:
- **Included:** connectedness, asphericity (π_{n+2}=1), linear disk filling, no geometric CAT(0) action, word-hyperbolicity (four-point condition), and exclusion of locally CAT(−1) metrics on every homotopy-equivalent finite complex.
- **Omitted:** that K is 2-dimensional, and the exclusion of locally CAT(0) models.

`lean/docs/257.md` states these omissions itself. I found no loophole in the definitions: CAT(0) is the CN inequality along segments, properness is defined via compact sets, and X is required to be nonempty.

## Trust surface
- **Counts:** 0 `sorry`, 0 `axiom` declarations, 0 `admit`, 0 `native_decide`/`implemented_by`/`extern`/`unsafe`/`opaque`/`set_option`. The raw grep hits for "admit", "axiom" and "macro" are prose.
- **`decide`:** 230 uses, all finite Fano-template checks.
- **Imports:** only Mathlib.
- **Not re-proved in the paper:** Hurewicz/Whitehead, planar separators, Cartan–Hadamard, linear Dehn function ⇒ hyperbolic, tangent cones. The Lean re-proves or bypasses all of these.
- **Verdict:** clean at the text level. The Lean was not compiled here.

## Labels
| Axis | Label | Evidence / note | Conf. |
|---|---|---|---|
| A | **A2** (hard conjunct A5: ¬∃ action) | "There exist a finite connected two-dimensional aspherical simplicial complex K…" (01:7) | high |
| B | **B2** (refutes "every hyperbolic group is CAT(0)"; also answers the CAT(−1) question) | 01:2. Full only together with prior results: no. Adds corollaries: yes. | high |
| C | **C3 primary** (random presentation selected with positive probability, plus contradiction via a limiting configuration); secondaries C1 (template), C4 (counting/variance/TV chains), C5 (cited textbook tools), C2 (local recursions only) | "existence argument" (01:15) | high / medium on primacy |
| C flags | computer-assisted **no**; ih_strengthened **no**; ih_template none | `decide` is used only on finite template facts | high |
| D | **D3 (provisional)** | rests on P37 / P08 / P03+P47 | low-medium |
| Provenance | **no** | No model-produced work is cited. The 2025–26 citations (Stark 2506.10108, Duchesne–Simon 2603.03863) are used only for the problem's status. | medium (novelty pass to verify) |
| E | Problem field: Group theory (20F67, 20F65, 20F06, 20P05). Lean-dir field: Geometry. | See below. | medium-high |

**E, method fields:**
- **Essential:**
  - probabilistic combinatorics;
  - combinatorial group theory (pictures and diagrams);
  - planar separators;
  - CAT(0)/CAT(1) metric geometry (tangent cones, flat rigidity, parallel sets);
  - harmonic-energy and barycenter theory (Gromov, Izeki–Nayatani, Sturm);
  - ultralimits;
  - finite geometry (PG(2,2), GL₃(F₂));
  - algebraic topology (Hurewicz, Whitehead);
  - linear Dehn function ⇔ hyperbolic.
- **Corollary-only:** Cartan–Hadamard.
- **Background-cited:** IKN 2012, Toyoda 2016, Ollivier–Wise, Brady–Crisp.

There are 6 essential fields outside group theory.

## Proof architecture (with Lean DAG shares)
The extractor missed the entire metric branch because it does not follow dot-notation edges such as `finalFinite_noAction.exists`. I added 77 edges, which raised the reach from 3,287 to 3,726 declarations, and recomputed the dominators from `main`.

1. **Template and nested tables (Sec 2).**
   - The template is the doubled-Fano incidence graph Γ: A, B, C, D are doubled, and the edge Y_D–CD is omitted, which leaves the loose edge X_D–CD.
   - Fans are sampled at N^{2−α}. Tops are marked only over already-selected fans, at N^{3−β}.
   - There are 90 square decoration tables at N^{2−δ} and one six-letter table at N^{3−δ}, both near density 1/2.
2. **Diagrams (Sec 3).**
   - A coincidence-rank first-moment bound counts shared fans once.
   - Pictures are put into a normal form, and multiplicity weights w_b = max{r_b, m_b} are introduced.
   - Weighted-contact and apex inequalities give A ≤ B/κ.
   - Lipton–Tarjan separators then give linear filling and the absence of spherical pictures, hence asphericity.
   - Lean: ≈60% of DAG nodes. `original_letter_linear_filling_list` dominates 8.6%; the explicit contraction for asphericity dominates 16.2%.
3. **Sampling (Sec 4).**
   - Tools: the critical exponent h(W), closures U, stars, second-moment concentration, and the uniform law on stars, which gives a TV coupling of t matches that agree on I and whose leaves are near-iid.
   - Lean: ≈11%.
4. **Energy and limit (Sec 5).**
   - Steps: a normalized energy minimizer, then a six-letter displacement bound, then the uniform conditional test ⟨h_I, v_e⟩ ≤ 0, then an L² product over matches and its ultralimit.
   - In the limit: squared two-step distance is 2, all core hexagons share one center at radius √3/2, and the ternary midpoint test gives a right angle at CD.
   - Lean: `impossible_sequence` dominates 9.7%.
5. **Obstruction (Sec 6).**
   - Line vectors pairwise have cos = −1/3. The fan identities M_i hold, and h₀ = M_C ⊕ x_D.
   - M_C and M_D are antipodal. Splitting the parallel set of their axis gives a flat transverse square, which makes M_A and M_B antipodal. That contradicts ⟨M_A, M_B⟩ ≥ 0.
   - Lean: `no_finite_obstruction` dominates 1.3%. The Lean proves this step by a shorter algebraic route, without the CAT(1) local-geodesic theorem or the parallel-set theorem.
6. **Selection and finite model (Sec 7).** A diagonal sequence, a simplicial model, and Cartan–Hadamard. Lean: ≈18%, which includes its own development space for Cartan–Hadamard and its own proof that linear Dehn ⇒ four-point hyperbolicity.

**Lean route differences:**
- asphericity by an explicit contraction (paper: Hurewicz + Whitehead);
- infinitude by a rank count on six-cells (paper: Euler characteristic);
- an algebraic proof of antipodality and of the transverse square;
- displacement bound M = 8;
- a tangent cone built from scratch.

## Items (51 paper, 12 Lean; full list in JSON)
Provisional grades:
- **N3:** P03 (template gadget, F3), P08 (nested near-critical model, F3), P37 (uniform conditional test, F5), P47 (finite CAT(0) obstruction, F3).
- **N2:** P10, P13–P16, P19–P23, P25, P26, P28–P31, P33, P35, P39, P41–P43, P46.
- **N0 / N1:** everything else (textbook tools and bookkeeping).

## Eureka candidates (provisional)
1. **P37, uniform conditional test (N3, F5).** For any bounded h_I that depends only on the labels in I, the limsup of E⟨h_I, v_e⟩ is ≤ 0, uniformly over actions chosen after the tables are sampled. It is built from the star coupling P31, the inductive means P36 and the displacement bound P35.
   - *For:* this uniformity is exactly what IKN and Toyoda lack; their constants depend on the target.
   - *Against:* every ingredient is cited or standard.
2. **P08, nested near-critical random model (N3, F3).** Fans are sampled first, tops only over selected fans, and the decorations sit just below the density-1/2 collapse threshold.
   - *For:* it reconciles hyperbolicity with metric rigidity in the limit.
   - *Against:* the square and hexagonal models (Odrzygóźdź) are already hyperbolic below 1/2.
3. **P03 + P47, doubled-Fano gadget and its finite CAT(0) obstruction (N3/N2, F3).**
   - *For:* it is tiny, it appears nowhere in L, and it must contradict every CAT(0) space.
   - *Against:* a template search may be routine once the target identities are known, and the Lean proof is short.
4. **P20/P21, multiplicity weights w_b (N2).** The paper itself names the precedents (Ollivier, AFL).
5. **P35, six-letter displacement bound (N2).**

## Correctness
- **No gap found.** I re-did all the numerical identities, including:
  - the counts 32/90/212/98, h(F) = 3 and the master exponent;
  - κ, and the inductive mean bound a_j ≤ 1/j;
  - the hexagon radius √3/2, the fan and exceptional identities, the arccos relation 2a + b = π, and the final ⟨M_A, M_B⟩ ≥ 0.
- **Concerns:**
  - This is an extraordinary claim with an unreviewed, non-effective proof.
  - Sec 3 is long and intricate.
  - The comparator is weaker than the headline.
  - The Lean was not compiled here.
- If the comparator passed, the core existence claim is machine-checked. That makes the residual risk small relative to most families.

## Extraction friction
- The extractor drops edges written as dot-notation on theorem names.
- One file, `IndexedFillingValue.lean`, is a 7,843-line monolith.
- Most definitions are inline `\emph`.
- The comparator is weaker than the headline.
- The grep has prose false positives.
- Two bibliography entries are never cited.
- There is no trace.
