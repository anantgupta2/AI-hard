# Family 148: downstream targets for the finite-law pair bound

**Item.** The finite-law pair bound is Lemma `lem:pair-bound` in pairs.tex:37:

k(H(ν) − H⁰_ρ(ν)) ≤ log|kF| + C_k Σ_{2^{-ℓ} ≤ 2ρ} c_ℓ(ν)

- The bound is log-free.
- C_k does not depend on the minimal separation of F = supp ν, so the bound is separation-free.

**Type:** F3. The machine-readable version is `downstream.json`, which holds 10 verbatim Lean declarations. This report is brief, as instructed: Kittle–Kogler independently reached the same mechanism.

## Part A: Lean

**lean_status: `as in paper`.** `pair_bound_natural` (SumsetBound.lean:269) states the lemma with the paper's own constant C_k = 60000k⁴, in natural log. All three comparator theorems depend on it. I checked this at text level only; nothing was compiled.

**Comparator chain** (`entropy_rate_dimension`):
1. `entropy_rate_dimension`
2. `System.exponent_lower_bound`
3. `Typed.no_strict_entropy_gap`
4. `Typed.pair_bands_of_retained_loss`
5. `Typed.exists_band_pair_bound` (PairBands.lean:46)
6. `FairPairs.pair_bound_natural` (SumsetBound.lean:269)
7. `exists_fine_partition` (SumsetBound.lean:120)

`homogeneous_dimension_direct` reaches the same chain through `homogeneous_exponent_lower_direct`. `cor_set` reaches it through `no_exact_overlaps_dimension`.

**Gaps.**
- The shortlist points to `pair_bound` (:329). That declaration is only a **base-2 wrapper with zero dependents** and is not on any comparator DAG. The declaration that carries the load is `pair_bound_natural`.
- The paper's C_k is existential, with "one may take 60000k⁴". The Lean hard-codes that value.
- Dominated shares: `pair_bound_natural` 0.10, `exists_fine_partition` 0.076.

## Precedent

- **Before:** Varjú, JAMS 2019, Prop. 21. It works at a single scale, needs a doubling hypothesis, and loses a log. Pair capacity is equivalent to his extremal decomposition. No earlier log-free, all-scales version was found.
- **After Oct 6:** Kittle–Kogler, arXiv:2610.10511 (7 Oct 2026).
  - Same mechanism, but the currency is variance energy and the constant is C_m = 120m².
  - The first proof is credited to GPT-6 Astra (27 Sep).
  - They call their Thm 1.3 a quantitative version of 148's Lemma 3.2.
  - This is an independent rediscovery, so it is strong discoverability evidence against a jump.

## Part B

| # | Target | Kind | Lean score | Speedup / payoff |
|---|---|---|---|---|
| S1 | Varjú Prop. 21 (single scale) | known, a specialization | statable now | high but uninformative (control) |
| S2 | KK 2026 Thm 1.3, variance-energy form | known (post-release) | < 300 lines (variance energy) | med |
| S3 | KK 2025, contracting on average with weak separation | known | < 300 lines (System without `ratio_lt_one`) | med |
| O1 | Contracting on average with **no** separation | open | < 300 | new theorem; conf. medium |
| O2 | Countable IFS | open (routine) | < 300 | new theorem; conf. medium |
| O3 | Random / non-autonomous self-similar measures | open | < 300 | quenched formulas; conf. medium-low |
| O4 | ℝ^d with commuting linear parts | open; KK claim the virtually solvable case | major library | independent proof |
| O5 | Analytic self-conformal IFS on ℝ | open | major library | partial |

**Theorem corollaries (not reuse of the device):**
- Hochman 2014 Thm 1.3
- Varjú 2019 (transcendental parameters)
- Rapaport 2022
- Rapaport–Varjú 2024 (`homogeneous_dimension_direct`)
- Feng–Feng 2025
- the attractor formula (`cor_set`)

**Release reuse:** none. No other family uses fair pairs or the pair bound.

**Negative controls:**
1. L^q dimensions: there is no chain rule for Rényi entropy.
2. Absolute continuity: the argument is ineffective there.
3. Furstenberg measures and self-affine measures: non-commutativity breaks type conditioning.

## Top 5

1. **S2, the KK entropy-loss bound.** It is the device restated with a different currency. Only about 100 lines of new definitions are needed.
2. **O1, contracting on average without separation.** This is the best new-theorem target.
3. **O2, countable IFS.** A cheap transfer test.
4. **S3, KK 2025.** A known theorem in which the pair bound could replace the separation step.
5. **S1, Varjú Prop. 21.** A statable-now sanity control.

There is no cross-field target. Every target stays within the dimension theory of self-similar measures.
