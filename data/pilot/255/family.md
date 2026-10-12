# Family 255: Quasi-isometric recognition of virtually polycyclic groups

This is a FAMILY analysis of the paper and the Lean, done at text level. This agent did not build the Lean, because the checkout is shared; the orchestrator compiles the comparator. `scripts/extract_lean.py 255` (v3) was run and wrote `data/items/255_lean.json`.

- Corpus: `openai/math` at fd4aeeb.
- Manuscript: `preprints/quasi-isometric-recognition-of-virtually-polycyclic-groups-September-24-2026/build/`. It has 13 TeX files (5,465 lines) and 28 bib entries.
- There is no reasoning trace.
- Machine-readable version: `family.json` (45 items).

## 1. Main statement
**Paper:**
- **Thm 1.1** (`introduction.tex:10-12`): every finitely generated group quasi-isometric to a finitely generated virtually polycyclic group is virtually polycyclic. No algebraic hypothesis is placed on H.
- **Cor 1.2:** this is the Eskin–Fisher–Whyte lattice-recognition formulation. A group QI to a lattice in a simply connected solvable Lie group is virtually a uniform lattice in some, possibly different, such group.
- **Thm 1.4** (uniform bounded height, `introduction.tex:95-101`): let G be a connected simply connected real-triangulable unimodular Lie group, and let π : G → W = 𝔤/∩ker χ_j be its exponential height map. Then there is a finite group 𝒜_G ≤ GL(W) such that every (K,C) self-QI F satisfies ‖πF(g) − πF(1) − A_F π(g)‖ ≤ B(G,K,C) for some A_F ∈ 𝒜_G.

**Comparator** (`ComparatorChallenges/PolycyclicRecognition.lean`):
- It has three targets: `group_recognition`, `main_uniform_bounded_height` and `lattice_recognition`.
- Permitted axioms are propext, Quot.sound and Classical.choice. There are no `definition_names`.

**Match check:**
- **Thm 1.1 and Cor 1.2: exact.** `group_recognition` also includes the Dekimpe uniform-lattice realization of the recognized group.
- **Thm 1.4: exact or slightly more general.**
  - The metric can be any proper, compatible, left-invariant chain metric.
  - W can be any normed space isomorphic to the height quotient.
  - The statement asks only for "some finite subgroup A". The proof (`ConditionalBoundedHeight.lean:102`) still uses the paper's group, `templateSymmetryGroup` (the symmetry group of P).
- QI between f.g. groups is encoded algebraically as `GroupCoarseEquivalence`. This is equivalent to QI.
- I found no loophole at text level.

**Formalized vs claimed:** everything the paper claims is formalized. All cited inputs except Gromov are re-proved or bypassed (section 6). Gromov's theorem (forward direction) comes from the external package `Aaron1011/gromov`.

## 2. Trust surface
The grep covers 3,090 files and 262,281 lines.
- **Zero hits:** `sorry`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `ofReduceBool`, `maxHeartbeats` overrides.
- **Docstring English only:** the 13 `admit` hits, 1 `axiom` hit and 5 `partial` hits are all English words in docstrings.
- **`decide`:** 44 uses, all on numerals or Bool filters.
- **Cited theorems as Props.** Cited theorems appear as Prop-valued `*Input` definitions, which are later proved, e.g. `liFinitenessInput`, `bieriDualityInput`, `dekimpeLatticeRealizationInput`, `cornulierTesseraModelInput`, `remezPolynomialInput` and `normalizedPair_ergodicDecomposition`.
  - The final theorems take no Input hypotheses.
  - The KMN Input appears only in a legacy path that the final theorems do not use.
- **`gromov` package:** 76 files and 26.9k lines. Its only `sorry`s are commented out. It is part of the trust base.
- **Compile status: pending (orchestrator).**

## 3. Labels
| Axis | Label | Conf. | Evidence |
|---|---|---|---|
| A | **A1**: a universal closure statement. Thm 1.4 is also A1, with a uniform constant that is not explicit. Explicit-rate flag: no | 0.85 | intro:10-12 |
| B | **B1**: resolves the EFW conjecture (EFW 2007, Conj. 1.2 and Rem. (3), p. 929). Secondary B4: Thm 1.4 extends Peng's and EFW's height-respecting theorems. Flags: full only with prior results = no; adds corollaries = yes (Cor 1.2, and bounded height for all unimodular real-triangulable groups) | 0.8, conditional on correctness | intro:26-35, 74-78 |
| C | **C4** primary: volume-exponent estimation chains, "P(E) ≤ P(E′)". C3 is nearly co-primary (weak limits, contradiction arguments, ergodic decomposition). C5: Gromov, Cornulier–Tessera 2020, Li, KMN, Bieri, Dekimpe, Hörmander. C2 is minor (scale telescoping). ih_strengthened: **no**. Computer-assisted: **no** | 0.6 / 0.7 | intro:123-135 |
| D | **D3, provisional**. Max item: I31, reflection doubling (N3 candidate). Runner-up: I35, quotient-Haar offset probes. Flag "builds on a model-produced result": no for the paper. The Lean does reuse three other OAI dirs | 0.4 | labels.tex:39-54 |
| E | Problem field: group theory (MSC 20F65, 20F16, 22E25, 22E40). Lean dir: GroupTheory. 13 method fields, 10 of them cross-field (listed below) | — | — |

**E: method fields.**
- **Essential:**
  - Lie theory: Cartan subalgebras, weights, Dixmier, BCH.
  - Nilpotent large-scale geometry: Guivarc'h, Pansu.
  - Convex and polyhedral geometry.
  - Ergodic and measured group theory: Shalom couplings, ergodic decomposition.
  - Unitary representations and reduced H¹ (Cornulier–Tessera). The Lean replaces this with nilpotent vanishing on D.
  - Remez-type polynomial inequalities.
  - PDE: Hörmander. The paper uses it; the Lean avoids it.
  - Haar and Radon measure theory.
  - Amenability.
  - Gromov growth.
  - Homological group theory: Li, Bieri, KMN. The Lean avoids KMN.
  - Lattices in solvable Lie groups: Dekimpe, Farb–Weinberger, Geng.
- **Background-cited:** coarse differentiation (EFW, Peng) and boundary conjugation (Dymarz, DFX).
- About 75% of the invoked external theorems come from outside geometric group theory.

## 4. Proof architecture
1. **Model reduction (§11.1).** P is virtually a uniform lattice Γ in S (Dekimpe). S is QI to a real-triangulable G (Cornulier–Tessera 2017). H is amenable and G is unimodular. Γ is of type F and a PD group.
2. **Lie coordinates (§2).**
   - Cartan model q: N⋊D → G. It keeps the overlap N∩D rather than requiring a complement.
   - Graded limit D_∞, with dilations Δ_r.
   - Canonical height W ≅ V/∩ker α_i.
   - Exact weight dilations S_w preserve Haar measure (unimodularity).
3. **Volume calculus (§3).**
   - Bracket words Z, support exponents s_i(E), widths h_Z(E) (a sum of separate maxima), and P(E) = max over word bases of Σ h_Z(E).
   - Boxes B_r(E,L).
   - Two-sided packing: about e^{rP(E)} separated endpoints are reachable with heights in rE, and no more.
   - p(w) = P([0,w]) is a polyhedral norm. **𝒜_G = {A : P∘A = P} is finite** and permutes the generator-weight rays.
4. **Restricted products keep their volume (§4).** This combines a quantitative Remez-type polynomial-image lemma with a Cauchy–Schwarz "backward recurrence" lemma.
5. **Stationary slopes (§5).**
   - A compact space of normalized Lipschitz QI pairs, following Shalom's coupling.
   - Reduced-H¹ vanishing gives a slope l for each ergodic invariant measure.
   - Volume comparison gives l = Aπ.
   - The inverse coupling (Haar×μ) gives the slope A⁻¹ for F̄, so A ∈ 𝒜_G.
6. **Chart profiles (§6).**
   - Random rescaled height functions on D-sheets: f_{r,x,n}(z) = (πF(xnΔ_r z) − πF(x))/r.
   - Occupation measures are invariant.
   - Limits satisfy two inequalities: increments lie in conv(𝒜πv) (convexity), and P(f(J)) ≥ T·p(πv) (no folding).
   - The **affinity criterion** forces f = Aπz + b.
7. **Neighbouring sheets (§7–8).**
   - **Labels agree by reflection doubling.** Suppose the labels differ. Then they differ by the reflection at a facet of the polytope 𝒞. Alternating switch bundles on the two sheets then reach target volume e^{2rP(E)}, while the source terminal points number only e^{rP(E)}.
   - **Offsets agree.** Pure and mixed words give cone quotients L_S = N/I_S, on which G acts with exact Haar multiplier e^{ℓ_S(π g)}. Conditioned probes with an exact cancellation n₁⁻¹n₂ give e^{rP₁} ≤ e^{r(P₁ − ℓ(b₂ − b₁))}. So every cone trace of b₂ − b₁ vanishes.
8. **Uniform sublinear estimate (§9).** The chart laws concentrate, labels stabilize across scales and basepoints, and telescoping gives ‖πF(xg) − πF(x) − A_Fπg‖ ≤ ε(R)R.
9. **Bounded error (§10).**
   - Contracting rays give ray-quotient boundary homeomorphisms f_β.
   - vol f_β(xU) ≍ e^{ℓ_β(πF(x))}.
   - Height variation along N-fibers is bounded, via the positive relation among the weights.
   - Radon-measure averaging gives ℓ_β∘πF = ℓ_α∘π + O(1). This proves Thm 1.4.
10. **Recognition (§11).**
    - The labels define a homomorphism H → 𝒜_G.
    - An invariant mean corrects the bounded-defect height to a homomorphism τ.
    - Every f.g. subgroup of ker τ has polynomial growth, so it is virtually nilpotent (Gromov). Hence H is elementary amenable.
    - Li gives FP_∞. KMN gives type F and solvability. Li gives PD transfer. Bieri then gives a polycyclic finite-index subgroup.

## 5. Items (45; full list in `family.json`)
Grades are provisional.
- **N0:**
  - Vocabulary (I01–I03).
  - Cartan model (I05) and nilpotent coordinates (I06).
  - Logarithmic distortion (I12).
  - Lipschitz representatives (I20).
  - Reduced-cohomology slope (I22, transfer).
  - Model reduction (I41), amenable correction (I43), endgame (I44), Cor 1.2 (I45).
- **N1:**
  - Height map (I04, analytic: it is in the statement) and canonical-height lemma (I07).
  - Boxes (I09), product schemes (I11), support paths (I13), polynomial packing (I15), fixed-sheet packing and lift multiplicity (I16).
  - Polynomial image (I17), backward recurrence (I18), restricted products (I19).
  - Pair space (I21, after Shalom).
  - Stationary labels (I25), occupation invariance (I27), affine limits (I30), tuple lifts (I32), ideal tiling (I34), uniformity (I36).
  - Boundary maps (I37), Radon averaging (I39), kernel growth (I42).
- **N2:**
  - P(E) (I08) and the symmetry group 𝒜_G (I10).
  - Path packing (I14).
  - Forward volume comparison (I23) and inverse coupling (I24).
  - Chart profiles (I26), segment inequalities (I28), affinity criterion (I29).
  - Cone quotients (I33) and boundary-volume height (I38).
- **N3 candidates:** reflection doubling (I31), and offset probes (I35, weak).

## 6. Lean structure
**Size.**
- 10,961 declarations: 8,239 theorems, 2,201 defs, 315 instances.
- Target DAG: 7,308 declarations. By subdirectory: Algebra 2,794, Geometry 2,274, Analysis 1,274, Finiteness 642, Lattices 200; other OAI dirs 117.

**Core.** The closure of `CartanWordModel.exists_uniform_height_intrinsic` (the engine of Thm 1.4) has 3,970 declarations, 54% of the DAG. Its dominated share of the whole DAG is 0.398. The rest is mostly background re-proved as transfer: BCH, Lie integration, Dixmier, Dekimpe, Cornulier–Tessera, Li, Bieri and Remez.

**Load-bearing shares within the height core:**
- Prop 9.4, the sublinear estimate, dominates 49%.
- The affinity criterion dominates 4.6%.
- The inverse coupling dominates 1.8%.
- The reflection lemma dominates 0.1%; offset probes 0.2–0.4%.
- `supportIn`/`boxCost` (P) are used by 10% and 7% of the core but dominate nothing, because they are shared vocabulary.
- The formalization is too distributed for any single item to reach the 20% proxy, so measure by cluster instead.

**Route differences from the paper:**
1. **Cornulier–Tessera replaced.** The Lean proves reduced-H¹ vanishing for nilpotent groups (`Finiteness/NilpotentReducedCohomology.lean`) and applies it to the Cartan factor D (`Geometry/CartanCocycleRestriction.lean`).
2. **Hörmander avoided.** `Analysis/LocalProfileAffinity.lean` uses generator words and the inverse function theorem instead.
3. **KMN avoided** (`Algebra/RecognitionWithoutKMN.lean`).
4. **Unimodularity** is obtained from a lattice comparison rather than from Følner sets.
5. **Metric generality.** The height theorem is proved for any proper chain metric.

## 7. Eureka candidates (quick literature check only)
| # | Item | N / F | For | Against / nearest neighbour |
|---|---|---|---|---|
| 1 | I31: reflection doubling for neighbouring labels | N3 / F3 (F4) | Turns a label mismatch into an exponent contradiction, 2P(E) vs P(E), through an alternating two-sheet gadget. It is absent from the goal and from L | Conceptual cousin of EFW's up/down quadrilateral arguments (coarse differentiation; Peng). Tiny Lean share |
| 2 | I35 (+I33/I34): cone-quotient Haar "trace tests" with conditioned probes | N3 (weak) / F3/F5 | The exact cancellation lets one endpoint carry both an ideal and a quotient restriction. The tile sum reads off ℓ_S(b₂ − b₁) | Haar/modular detection of height and boundary quotients of N are known (Farb–Mosher, Dymarz, DFX) |
| 3 | I08 + I10: bracket-word volume exponent P (a sum of separate maxima) and its finite symmetry group 𝒜_G | N2 (N3 if there is no nonabelian precedent) / F1 | A single two-sided invariant that drives every comparison and defines 𝒜_G. It handles zero-weight brackets | For abelian N it reduces to the EFW/Peng box volume; 𝒜_G generalizes Peng's root permutations and the Sol flip |
| 4 | I29: affinity criterion, "no folding + finite labels ⇒ affine" | N2 | Largest candidate Lean share: dominates 4.6% of the height core | Rademacher, chamber arguments, Hörmander. Neighbours: Cheeger–Kleiner monotone sets, EFW monotone geodesics |
| 5 | I24: inverse coupling with exactly the inverse slope | N2 | Needed to get P∘A = P | Shalom/Furman coupling symmetry |

## 8. Correctness concerns
- **The claim is extraordinary.** It would resolve a conjecture open since 2005–07. A quick search found no expert confirmation, and Grayevsky–Pallier (2025) still list it as open.
- **Order of limits in Prop 7.1.** The proof takes a diagonal over violating δ → 0 and extends convergence to the facet boundary (labels.tex:144-163). This is the most delicate step I read.
- **Pervasive o(r) envelope conventions** and order-of-choice requirements (Remarks 4.4 and 9.2). An informal proof is most likely to slip here, so the Lean build is decisive.
- **The paper's own uses are not certified by the Lean.** The Lean bypasses Cornulier–Tessera, Hörmander and KMN, so the paper's uses of those theorems are certified only through the Lean's alternative routes. The risk is low.
- **Trust base.** It includes the third-party `gromov` package (Aug 2026) and 262k lines of OAI Lean. If the build fails, everything reverts to an unrefereed paper.

**Checked by hand:**
- P is translation invariant, because a basis has total weight equal to the trace, which is 0.
- p is a norm (by the positive relation).
- 𝒜_G is finite.
- The Heisenberg example gives P = 2(b − a).
- The reflection step and the identity P(E′₁ ∪ E′₂) = 2P(E).
- The trace tests span W*.
- The amenable correction.
- The endgame logic.
- The comparator matches the paper.

## 9. Extraction friction
- Theorem numbers come from a single counter shared within each section, so they had to be reconstructed.
- Key definitions are inline: chart profiles, pure and mixed words, the uniform quasi-action.
- The Lean is enormous and fine-grained. Paper lemmas map to clusters of `Cartan*`, `Published*` and `Polar*` files.
- Cited theorems are encoded as Prop `*Input` definitions, so one must check which of them reach the final theorems.
- The extractor's ranking surfaces vocabulary and assembly declarations.
- The Lean reuses three other OAI dirs: Thompson, CyclicSeries and CriticalPercolation.

Sources from the quick literature check:
- [EFW 2007 (arXiv math/0511647)](https://arxiv.org/pdf/math/0511647)
- [Peng II (arXiv 1002.4451)](https://ar5iv.arxiv.org/html/1002.4451)
- [DFX (arXiv 2304.12498)](https://arxiv.org/pdf/2304.12498)
- [Le Boudec (arXiv 2510.24581)](https://www.arxiv.org/abs/2510.24581)
- [Grayevsky–Pallier (arXiv 2509.12823)](https://arxiv.org/pdf/2509.12823)
- [Cornulier, exponential radical](https://www.normalesup.org/~cornulier/gtexp.pdf)
