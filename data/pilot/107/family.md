# Family 107: Matrix multiplication with exponent at most 9/4 (family analysis)

**Analyst:** FAMILY agent (paper + Lean, text level), 2026-10-10, influential-problems pass.
**Corpus:** `openai/math` @ fd4aeeb. **L:** Mathlib d13f23b plus the three bibliographies.
**Lean was not compiled by this agent.** The orchestrator compiles the comparators.

## Manuscripts
| id | title | date | role |
|---|---|---|---|
| M1 | An Upper Bound of 9/4 for the Matrix Multiplication Exponent | Oct 2 | **Headline.** ω(ℂ) ≤ 9/4 via Strassen's spectral route on polynomial-multiplication tensors. 15 pp., no numerics |
| M2 | Complex Matrix Multiplication Below 2.258 and Rectangular Bounds | Sep 24 | Laser-type method on CW₁, using an auxiliary group-tensor separator (GROUP). ω < 2.258, α > 0.465, ω(1,0.709,1) < 2.092 |
| M3 | Staggered extraction for exact matrix multiplication over every field | Sep 24 | Asymmetric laser method in the ADVXXZ framework. ω_F < 2.371054886006746 for every field |

## Main statement and comparator
- **M1, Thm 1.1** (paper.tex:45-49). For every ε > 0, two n×n complex matrices can be multiplied with O_ε(n^{9/4+ε}) arithmetic operations.
- **Comparators.**
  - `MatrixMultiplication.json` has three targets:
    - `Arithmetic.omega ℂ ≤ 9/4`;
    - `93/200 < complexAlpha`;
    - `rectangularOmega ℂ 0.709 < 523/250`.
  - `MatrixFields.json` has one target: `∀ F field, omega F < 2.371054886006746`.
- **Model.** Straight-line programs over +, −, ×, with free constants and no division. Cost ≤ C·n^{τ+ε} for all n.
- **Match check.** The comparator matches the paper's model.
  - The sInf/sSup junk values cannot be exploited: the admissible set is nonempty and bounded below by 0.
  - The α target needs rectangularOmega = 2 exactly, so a formal lower bound is also needed. `Arithmetic/LowerBound.lean` exists.
- **Not in Lean.**
  - M2's ω < 2.258 route (viscosity comparison plus an 18 MB GMP certificate). It is implied by the formalized 9/4.
  - M2's characteristic-transfer corollaries.
- `lean/docs/107.md` links M2 and M3 but not M1, although the 9/4 Lean development follows M1 line by line.

## Trust surface (text level)
The grep covers MatrixMultiplication (83k lines) and MatrixFields (182k lines).
- **Absent:** sorry, axiom, native_decide, implemented_by, extern, unsafe, opaque, set_option, #eval and custom elab/macro all return 0. The single `admit` hit is prose in a docstring.
- **Kernel `decide`:**
  - 2 trivial uses in the 9/4 subtree;
  - about 18.4k in the MatrixFields numerical certificates (computer-assisted but kernel-checked).
- **External dependency:** the 9/4 proof imports `FixedPointTheorems.brouwer` from the harfe/fixed-point-theorems-lean4 package. It is used to prove a Schauder–Tychonoff-type fixed point by finite approximation.
- **Permitted axioms:** propext, Quot.sound, Classical.choice.

## Labels
| Axis | Label | Notes |
|---|---|---|
| A | **A3**, explicit rate | Quantitative bound on an infimum. Inside: ∀ε ∃C ∀n ∃ a program. The algorithms are not explicit |
| B | **B3** | The posed problem (ω = 2?) stays open. Flags: adds corollaries (rectangular/dual exponents; det/inverse in O(n^c), c < 2.258; every-field bound). Not "full only with prior results" |
| C | **C3** primary (spectral duality) | Secondaries: C1 (explicit degenerations: the real core), C4 (discrete growth), C2 (induction on H_a), C5 (fixed-point theorem). Computer-assisted: headline no; M2/M3 yes. ih_strengthened = yes, template "carry an extra tracked quantity" (the slope bound H_a). App. A strengthens the target to all s (Strassen-standard) |
| D | **D3 (provisional)** | Rests on the separation device and the profile method. Provenance flag: **partial**. M1 reuses M2's GROUP lemma (model-produced, same release) without citing it. Dupont et al. (AlphaEvolve-assisted) is cited only as the record |
| E | Problem: TCS (68Q17, 68Q25, 15A69). Lean dir: LinearAlgebra | Essential method fields: Strassen spectrum; laser method/ASI; finite abelian Fourier; SL₂ Clebsch–Gordan; method of types; fixed-point/convexity; Behrend (M2); viscosity PDE (M2 square); validated numerics (M2, M3). Corollary-only: Nullstellensatz |

## Proof architecture of M1 (the headline)
1. **Spectral reduction.** ν ≤ 9/4 holds iff every tensor character has p_X + p_Y + p_Z ≤ 9/4.
   - This uses λ(T_m) = m^{3t} and Strassen's detecting characters.
   - App. A re-proves Strassen's theorem by a new route: Schauder–Tychonoff with frozen slices, plus a catalytic obstruction.
2. **Finite separation (Prop 3.1).** Take A = Σ A_h, sharing the X-leg, with matched disjoint Y/Z sectors.
   - Then 5M copies of A degenerate to ⊕_h A_h ⊗ B_X(M).
   - Fourier phases force u − v + 2(g − h) = 0. The weights g², hu − h², −hv then give total weight (g − h)².
3. **Shared-leg entropy inequality (Cor 3.2).** λ(T) ≥ e^{p_X H(q)} ∏ λ(T_i)^{q_i}, for every character.
4. **Profile.** P(a,b) = (∏_{π∈S₃} λ_π(C(a,b)))^{1/(6t)} over the polynomial-multiplication tensors C(a,b).
   - Basic properties: P(1,b) = b, P(a,b) = P(b,a), P ≤ (a+b−1)^{1/t}.
5. **Discrete concavity.** Comes from C(a,b) ⊗ B_X(2): the Clebsch–Gordan determinant filtration gives a block-triangular structure, and weights ±1 give a degeneration.
   - **Shifted tripling** P(a, 3h+a−1) ≥ 3P(a,h) comes from a three-sector monomial degeneration.
6. **Diagonal growth.** P(a,a) ≥ a^{4/3}. Comparing with (2a−1)^{1/t} forces t ≤ 3/4, so ω ≤ 9/4.

**Lean cone of `omega_le_nine_quarters`:** 835 declarations, 93k tokens.

| Part of the cone | Share |
|---|---|
| Spectrum + Convex (background re-proof) | ≈20% |
| Arithmetic-model plumbing | ≈18% |
| Separation tag inequality (sub-cone) | 25% |
| Concavity (sub-cone) | 30% |
| Tripling (sub-cone) | 35% |

The separation lemma is a **cut vertex**: it lies in the up-cone of both concavity and tripling.

## Items
The full list (49 paper items and 11 Lean items) is in family.json. Highlights:

| id | item | prov. N | F |
|---|---|---|---|
| I10 / J03 / L02 / L10 | Finite separation (M1) = GROUP lemma (M2, Behrend-sphere form): lossless separation of a shared leg with a retained dot product | **N3** | F3 |
| I11 / L03 | Shared-leg entropy inequality for all characters | N2 (graded with I10) | |
| I14 / L04 | Symmetrized polynomial-multiplication profile P(a,b) | **N3** | F1 |
| I17, I18 | Discrete concavity; shifted tripling | N2 (graded with I14) | |
| I19 | Diagonal-growth lemma | N1 | |
| I22 | Fixed-point proof of multiplicativity (alternative route to Strassen duality) | N2 | |
| J13 | Viscosity-type comparison for attainable values (M2, not in Lean) | N2 (new bridge) | |
| J15 | Readable label trees, conditional entropy bound | N2 | |
| K03, K06 | Cross-depth joint extraction; staggered lots (M3) | N2 | |
| I05, I09, I12, I16, J01, J02 | Strassen duality, Bini interpolation, C(a,b) rank, Clebsch–Gordan, ASI, CW border rank | N0 | |

## Eureka candidates (ranked)
1. **Separation device (I10 + I11; J03).** Provisional N3, F3.
   - It replaces lossy Salem–Spencer zeroing-out with lossless separation plus a gain factor.
   - From CW₁ alone it gives 2.2901 in a page, which is below the AFLG 2.3078 limit for laser variants.
   - Against: its ingredients are classical (Cohn–Umans group algebras, Strassen's quadratic-weight degenerations, Behrend). It also has a within-family model precedent (M2).
2. **Polynomial-multiplication profile (I14 + I17 + I18).** Provisional N3, F1.
   - It converts Strassen's dual route into a scalar growth problem.
   - Against: it depends on candidate 1. The closest method neighbour is Alman–Li 2026 "Strassen calculus" (not cited).
3. **Viscosity comparison for value functions (J13).** N2. A bridge built from transfer, and not in Lean.
4. **Label-tree entropy bound (J15).** N2, templated.
5. **Cross-depth joint extraction and staggering (K03/K06).** N2. ADVXXZ Thm 6.4 is the named precedent.

## Correctness
I checked M1 line by line and found no error.
- I verified the separation identity numerically (M = 1..4).
- I sanity-checked concavity, tripling and the final bound with the flattening-rank characters, for which P = √(ab(a+b−1)) and t = 2/3.

**Barriers.**
- **AFLG (2.3078)** covers zeroing-out laser analyses of CW powers. GROUP uses an auxiliary group tensor degeneration and lies outside that framework.
- **Alman / CVZ irreversibility (2.168 for CW_q).** My estimate for CW₁ is irreversibility ≈ 1.084, which gives a barrier of ≈ 2.168. M2's 2.29 and 2.258 respect it.
- **M1** uses C(a,a), whose irreversibility tends to 1 (estimate Q̃ = a), and its argument is dual (spectral). No known barrier applies.
- These barrier numbers are my own calculations, not quotes from the barrier papers.

**Residual concerns.**
- The jump is enormous and the work is unreviewed. Only press coverage was found (OfficeChai).
- The Lean was not compiled by me, and the 9/4 proof relies on an external Brouwer package.
- M1 does not cite M2 or any barrier paper.
- M1 is over ℂ only. M2's exceptional primes are not computed.

## Extraction friction
- The 90 MB extractor dump is dominated by MatrixFields certificate plumbing, so cones had to be computed per target.
- The same device appears under two names and in two forms (M1 and M2).
- M1 is missing from `lean/docs/107.md`.
- WebFetch was unavailable, so the literature checks are search-snippet level.
