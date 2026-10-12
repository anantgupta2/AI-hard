# Family 262: downstream analysis of C1 (regularized matrix field M_δ and rank-one comparison)

This is the downstream pass, dated 2026-10-12. Machine-readable version: `downstream.json`. The Lean was read at text level only; no `lake build` or comparator run was done, per the orchestrator. The dependency chain comes from `data/items/262_lean.json` (extractor v3). arxiv.org was unreachable, so every external paper below is known only from WebSearch summaries and is **unverified**.

**Item.** The item is defined as follows:
- The field: M_δ(B) = c·lim_R ∫_{−R}^{R} (f(K² − 2sB + s²) − f(s²)) ds on symmetric B.
- Its primitive: J, with dJ = −tr(M dB).
- The rank-one comparison: M(B) = aaᵀ ⇒ aᵀ(K² − B²)a ≥ |a|^{2q}.

It comes from 262-S, Sections 3–4. Its classification is F1 (secondary F3): provisional N3, borderline N2.

## Part A: Is the item in the Lean?

**`lean_status`: as in paper.** The field, primitive, values on commuting data, boundary values and rank-one comparison are Lean declarations with the paper's formulas (`MatrixOrder.lean:16-56`). The comparator depends on them, and the Lean is, if anything, more general than the paper.

**Defining declarations** (verbatim in the JSON). All are in `lean/OAI/Analysis/LiebThirring/`:

| Declaration | File:line |
|---|---|
| `regularizedPrimitive` | MatrixOrder.lean:17 |
| `fieldNormalization` | MatrixOrder.lean:20 |
| `scalarMu` | MatrixOrder.lean:23 |
| `matrixX` | MatrixOrder.lean:30 |
| `truncatedField` | MatrixOrder.lean:36 |
| `matrixField` | MatrixOrder.lean:43 |
| `fieldPrimitive` | MatrixOrder.lean:47 |
| `RankOneClaim` | MatrixOrder.lean:51 |
| `quadraticMatrix` (s² + C − 2sB) | FieldLimit.lean:313 |
| `hermitianField` | FieldLimit.lean:433 |

**Key lemmas:**

| Lemma | What it gives | File:line |
|---|---|---|
| `hermitianField_cutoff_limit` | the limit exists | FieldLimit.lean:462 |
| `hermitianPotential_hasFDerivAt` | trace gradient, for any Hermitian C | FieldPrimitive.lean:185 |
| `fieldPrimitive_path_derivative` | dJ along paths | BoundaryValues.lean:235 |
| `matrixField_diagonal` | value on commuting data, μ(k²−b²) | BoundaryValues.lean:89 |
| `fieldPrimitive_endpoint_limit` | boundary values | BoundaryValues.lean:162 |
| `hermitianField_state_jensen` | state Jensen inequality | RankOne.lean:26 |
| `rankone_hermitian_comparison` | rank-one comparison | RankOne.lean:460 |
| `source_rankone_comparison` | rank-one comparison | RankOne.lean:601 |

**Comparator chain.** The comparator is `ComparatorChallenges/LiebThirring.json`, with solution module `OAI.Analysis.LiebThirring.Main`. The chain runs:
1. `sharp_lieb_thirring`
2. `negativeMoment_bound`
3. `finite_complex_eigenfamily_bound`
4. `SpectralProof.real_family_bound`
5. `real_family_action_bound`
6. `real_family_bound_sorted`
7. `compact_trial_bound`
8. `finite_spectral_trial`
9. `ActionProof.finite_action_upper_test`
10. `regularized_action_upper_test`
11. `matrix_compact_penalty`
12. `MatrixProof.source_rankone_comparison`
13. `rankone_hermitian_comparison`
14. `hermitianField`

Side branches:
- `penalized_action_integral` uses `matrixField`, `fieldPrimitive_hasFDerivAt` and `fieldPrimitive_path_derivative`.
- `finite_action_upper_test` uses `fieldPrimitive_endpoint_limit`.
- `source_connecting_path` uses `scalarMu`, `matrixField_isolated_coordinate`, `hermitianField_state_jensen` and `matrixField_diagonal`.

Dominated shares are 0.128 for `source_rankone_comparison`, 0.125 for `rankone_hermitian_comparison` and 0.039 for `fieldPrimitive_hasFDerivAt`. The field and rank-one block makes up 69% of the mathematical core.

**Gaps:**
- **Generalization, not weakening.**
  - Lean proves the field and the rank-one comparison for an arbitrary complex Hermitian C (in place of K²) and complex Hermitian B.
  - It transfers them to the real case with C = K² by complexification.
- **Different gradient proof.** Lean uses an explicit potential (`hermitianPotential`, built from `secondPrimitive`) instead of the paper's closed-curve argument.
- **Unused wrapper.** The Prop wrapper `RankOneClaim` / `rankOneClaim` is **not** in the comparator DAG; the DAG calls `source_rankone_comparison` directly.
- **Surrounding theorem only partly proved.** The paper's Thm 2.1 (`ActionClaim`, H¹₀) is unproved in Lean. The field is consumed by `finite_action_upper_test` for continuous amplitudes, which is enough for the comparator.
- **Matrix paper not formalized.** 262-M's reuse of the field is not formalized.
- **Range of σ.** Every lemma assumes 0 < σ < 1. For σ ≥ 1, `fieldNormalization` evaluates to 0, since the Bochner integral of a non-integrable function is 0.

## Part B: Where the device might be reused

**Bottom line: no strong device-reuse speedup target on a known theorem was found.**
- Everything the item reaches among known theorems, it reaches through its **theorem** or the same-family extension 262-M, not through the device. That includes:
  - Read–Schulz at γ=1;
  - the endpoints γ=1/2 and γ=3/2;
  - the matrix versions;
  - the Neumann half-line;
  - even star graphs;
  - higher-dimensional constants.
- The device is tied to second-order 1D problems with 0 < σ < 1:
  - it degenerates at both endpoints;
  - at σ = 1 the naive K² − B² is already a gradient;
  - there is no evident discrete, higher-order or d-dimensional analogue of the gauge shift k² − 2sb + s² = (s−b)² + k² − b².

### Speedup targets (known theorems)

| Id | Target | Reuse class | Expected speedup | Lean |
|---|---|---|---|---|
| S1 | Finite-matrix sharp LT, γ=1 (Read–Schulz) and (1/2,3/2) (262-M) | extension of own theorem, does not count | med | < 300 lines (matrix Model.lean) |
| S2 | Keller one-bound-state (N = 1) | special case; control | none | statable now |
| S3 | Even-edge star graphs (Demirel–Frank) | corollary via reduction | low | < 300 lines |
| S4 | Matrix γ = 3/2 (Laptev–Weidl, Benguria–Loss) | limit corollary; device unnecessary at σ = 1 | none | < 300 lines |

### Open problems where the obstruction recurs

| Id | Problem | Match | Confidence | Lean |
|---|---|---|---|---|
| O1 | Half-line LT with a Hermitian Robin matrix S, or Dirichlet, for 1/2<γ<3/2 (Exner–Laptev–Usman 2014; Schimmer 2022) | Strong: the calibration's boundary term a(0)ᵀB(0)a(0) equals the Robin term when B(0) = S; the field and J already exist at any Hermitian B | low-med | < 300 lines |
| O2 | Odd-edge Kirchhoff star graphs, general potentials (Demirel–Frank) | vector-valued half-line problem with a noncommuting vertex condition | low | < 300 lines |
| O3 | Sharp Jacobi-matrix LT for 1/2<γ<3/2 (Hundertmark–Simon; Schimmer) | weak: no discrete gauge shift | low | statable now (finite sections) |
| O4 | LT constants in d ≥ 2 | only through the theorem (corollary below) | low | needs major library |
| O5 | Sharp Hardy–LT on the half-line | singular Riccati endpoint | low | < 300 lines |
| O6 | Higher-order or fractional 1D LT | symbol not affine in B; likely failure | very low | < 300 lines |

### Theorem corollaries (show reach, but do not count)
- **γ = 1 instance.** Read–Schulz's L_{1,1} = 4/(3√3π) is MainClaim at γ = 1.
- **Same-family papers.** 262-M and 262-E are extensions of the theorem.
- **Endpoint limits.** The cases γ → 1/2 and γ → 3/2 follow as limits, for both the scalar and the matrix versions.
- **Neumann half-line.** The sharp constant is 2·L^(1)_{γ,1}, by even reflection. The soliton optimizer is even, so the constant is sharp.
- **Even star graphs.** They get the explicit constant L^(1)_{γ,1}.
- **Higher dimensions (new, not stated in the release; plausible, unchecked).** R_{γ,d} ≤ 2((γ−½)/(γ+½))^{γ−½} for 1 ≤ γ < 3/2 and every d.
  - Route: an operator-valued extension of 262-M, then Laptev–Weidl lifting.
  - This strictly improves Read–Schulz's 2/√3 on (1, 3/2); for example, the bound is about 1.059 at γ = 5/4.
- **Orthonormal ground states.** In the dual problem, ground states made of several orthonormal functions do not exist in the conjugate range. This follows from the dual form plus E's equality classification.

### Negative controls
- **N1: γ < 1/2 in d = 1 (proved false).** No finite LT constant exists, by weak-coupling scaling. The device fails because σ < 0. Statable now as `optimalConstant γ = ⊤`.
- **N2: γ > 3/2 (proved false).** The one-bound-state constant is too small, since L_{γ,1} = L^cl > L^(1) (Lieb–Thirring 1976; Frank–Gontier–Lewin 2021). In Lean the field is identically 0 there. Statable now.
- **N3: Complex potentials (Bögli et al.).** Hermitian functional calculus and trace gradients are unavailable. Needs a major library.

### Top 5 (Lean-usable first)
1. **O1: Robin half-line problem.** This is the only good structural match where the device itself, not the theorem, would be reused. The risks:
   - the continuation must be redone for a fixed initial value;
   - the sharp form is not known.
2. **S1: matrix LT at γ = 1 and on (1/2, 3/2).** This is the cleanest experiment for measuring how much the library is worth, since the field is reused verbatim. It is an extension of the item's own theorem, so it does not count toward a jump.
3. **O2: odd star graphs.** The device's noncommutative content is genuinely needed here. It may reduce to O1.
4. **O3: Jacobi matrices.** Cheap to state, but expected to fail.
5. **Controls N1/N2/S2/S4.** These bracket the device's domain of validity.

## Precedent
- **After Oct 6, 2026.** No use of the device was found.
- **Earlier equivalents.** None beyond those already in `novelty.json`:
  - Read–Schulz's cumulative-mass A(x), which is a different object;
  - Laptev–Weidl's phase-space integral, which lacks the B-shift.
- **Release reuse.** None outside 262-M and 262-E.
- **Grade.** No downgrade from this pass. The open risk remains that an expert identifies M_δ as a known gauge-shifted local Weyl density used as a calibration.
