# v2 A/B labels for the whole release (372 families)

231 families agreed on every field in two independent passes; 141 were adjudicated.

## Distributions

**A.matrix:** M1 property holds 66 (18%) · M3 counterexample 65 (17%) · M2 existence 49 (13%) · M9 exact value/sharp 41 (11%) · M8 one-sided bound 39 (10%) · M10 computational status 38 (10%) · M12 limit law 22 (6%) · M7 identity/isomorphism 14 (4%) · M4 non-existence 13 (3%) · M6 classification 13 (3%) · M5 equivalence 10 (3%) · M11 metamathematical 2 (1%)

**A.prefix, outermost quantifier:** ∀ 257 (69%) · ∃ 82 (22%) · none 27 (7%) · ℙ 6 (2%)

**A.prefix, full (top 12):** `∀` 143 · `∀∃` 53 · `∃` 53 · `none` 27 · `∃∀` 21 · `∀ℙ` 14 · `∀∃∀` 9 · `ℙ` 6 · `∀∞` 4 · `∀∃!` 4 · `∀∞∃` 4 · `∀∀∞` 3 · 31 distinct prefixes

**Quantifier alternations:** 0: 262 · 1: 91 · 2: 18 · 3: 1

**A.flags:** restricted_range 79 · asymptotic_only 49 · effective 37 · specific_instance 28 · probabilistic 27 · ineffective 24 · conditional_on 3 · finite_checkable 2

**B.problem:** P1 named conjecture 243 (65%) · P2 open question 94 (25%) · P4 record 17 (5%) · P3 problem list 14 (4%) · P5 nothing posed 4 (1%)

**B.outcome:** O1 settled yes 220 (59%) · O2 settled no 69 (19%) · O5 special case 62 (17%) · O7 record progress 7 (2%) · O8 extension 5 (1%) · O3 refute + replace 4 (1%) · O9 new proof 2 (1%) · O4 independent 2 (1%) · O6 conditional 1 (0%)

**B.flags:** adds_corollaries 221 · full_only_with_prior_results 43 · builds_on_model_output 16

**Lean vs headline:** same 176 (47%) · no_lean 130 (35%) · different 34 (9%) · weaker 32 (9%)

## Associations (Cramér's V, permutation p)

| pair | V | p |
|---|---|---|
| A_matrix × B_outcome | 0.51 | 0.000 |
| A_matrix × B_problem | 0.27 | 0.001 |
| A_outer × A_matrix | 0.51 | 0.000 |
| B_problem × B_outcome | 0.56 | 0.000 |
| A_matrix × subject | 0.39 | 0.000 |
| B_outcome × subject | 0.26 | 0.004 |
| A_outer × subject | 0.29 | 0.001 |
| A_matrix × lean | 0.30 | 0.000 |
| B_outcome × lean | 0.22 | 0.010 |
| lean_vs_headline × B_outcome | 0.16 | 0.517 |

## A.matrix × B.outcome (counts)

| A_matrix \ B_outcome | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 | O9 | n |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 | 42 | 1 | · | · | 22 | 1 | · | · | · | 66 |
| M10 | 25 | 5 | · | · | 1 | · | 3 | 4 | · | 38 |
| M11 | · | · | · | 2 | · | · | · | · | · | 2 |
| M12 | 15 | · | · | · | 6 | · | · | 1 | · | 22 |
| M2 | 37 | · | · | · | 12 | · | · | · | · | 49 |
| M3 | · | 61 | 1 | · | 1 | · | 1 | · | 1 | 65 |
| M4 | 9 | · | · | · | 3 | · | 1 | · | · | 13 |
| M5 | 9 | · | 1 | · | · | · | · | · | · | 10 |
| M6 | 11 | · | · | · | 2 | · | · | · | · | 13 |
| M7 | 11 | · | · | · | 3 | · | · | · | · | 14 |
| M8 | 28 | 2 | · | · | 7 | · | 2 | · | · | 39 |
| M9 | 33 | · | 2 | · | 5 | · | · | · | 1 | 41 |

## A.matrix by subject (row %)

| subject \ A_matrix | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Algebra | 33% | 17% | 44% | · | · | · | 6% | · | · | · | · | · | 18 |
| Algebraic and complex geometry | 31% | 19% | 22% | · | 3% | 3% | 11% | 6% | 6% | · | · | · | 36 |
| Combinatorics | 8% | 16% | 22% | 5% | 3% | · | · | 32% | 11% | 3% | · | · | 37 |
| Convex and metric geometry | 7% | · | 20% | · | · | · | · | 27% | 47% | · | · | · | 15 |
| Differential geometry | 10% | 17% | 24% | · | 10% | 14% | · | 10% | 14% | · | · | · | 29 |
| Dynamical systems and ergodic theory | 42% | 17% | 17% | · | 8% | · | · | 8% | 8% | · | · | · | 12 |
| Functional analysis | 9% | 18% | 36% | · | 9% | · | · | 9% | 9% | · | 9% | · | 11 |
| Group theory | 21% | 21% | 36% | 7% | 14% | · | · | · | · | · | · | · | 14 |
| Mathematical logic | 33% | 17% | · | 17% | · | · | · | · | · | 17% | 17% | · | 6 |
| Mathematical physics | 20% | 4% | 8% | 4% | · | · | · | 20% | 20% | 16% | · | 8% | 25 |
| Number theory | 13% | 16% | · | 13% | · | 3% | 13% | 10% | 16% | 3% | · | 13% | 31 |
| Operator algebras | 5% | 26% | 32% | · | 5% | 11% | 11% | 5% | 5% | · | · | · | 19 |
| Partial differential equations | 25% | 12% | 19% | 6% | · | 12% | · | · | 12% | 6% | · | 6% | 16 |
| Probability and statistical mechanics | 7% | 10% | · | 7% | · | · | · | · | 24% | · | · | 52% | 29 |
| Real and complex analysis | 69% | 12% | 6% | · | · | · | · | 12% | · | · | · | · | 16 |
| Theoretical computer science | · | 2% | 5% | · | · | · | 2% | 12% | 2% | 75% | · | · | 40 |
| Topology | 22% | 6% | 33% | 6% | · | 17% | 11% | · | 6% | · | · | · | 18 |

## B.outcome by subject (row %)

| subject \ B_outcome | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 | O9 | n |
|---|---|---|---|---|---|---|---|---|---|---|
| Algebra | 33% | 44% | · | · | 22% | · | · | · | · | 18 |
| Algebraic and complex geometry | 56% | 22% | · | · | 19% | 3% | · | · | · | 36 |
| Combinatorics | 62% | 19% | 3% | · | 8% | · | 8% | · | · | 37 |
| Convex and metric geometry | 73% | 20% | · | · | 7% | · | · | · | · | 15 |
| Differential geometry | 55% | 24% | · | · | 21% | · | · | · | · | 29 |
| Dynamical systems and ergodic theory | 67% | 17% | · | · | 17% | · | · | · | · | 12 |
| Functional analysis | 45% | 45% | · | 9% | · | · | · | · | · | 11 |
| Group theory | 64% | 36% | · | · | · | · | · | · | · | 14 |
| Mathematical logic | 83% | · | · | 17% | · | · | · | · | · | 6 |
| Mathematical physics | 56% | 8% | 4% | · | 28% | · | · | 4% | · | 25 |
| Number theory | 74% | 3% | · | · | 23% | · | · | · | · | 31 |
| Operator algebras | 53% | 26% | · | · | 16% | · | · | · | 5% | 19 |
| Partial differential equations | 50% | 19% | 6% | · | 12% | · | · | 12% | · | 16 |
| Probability and statistical mechanics | 62% | · | · | · | 34% | · | · | · | 3% | 29 |
| Real and complex analysis | 50% | 6% | · | · | 44% | · | · | · | · | 16 |
| Theoretical computer science | 65% | 18% | · | · | 2% | · | 10% | 5% | · | 40 |
| Topology | 56% | 28% | 6% | · | 11% | · | · | · | · | 18 |

## Outermost quantifier by A.matrix (counts)

| A_matrix \ A_outer | ∀ | ∃ | ℙ | none | n |
|---|---|---|---|---|---|
| M1 | 66 | · | · | · | 66 |
| M10 | 14 | 19 | · | 5 | 38 |
| M11 | · | · | · | 2 | 2 |
| M12 | 17 | · | 2 | 3 | 22 |
| M2 | 44 | 5 | · | · | 49 |
| M3 | 13 | 52 | · | · | 65 |
| M4 | 9 | · | · | 4 | 13 |
| M5 | 10 | · | · | · | 10 |
| M6 | 11 | · | · | 2 | 13 |
| M7 | 11 | · | · | 3 | 14 |
| M8 | 32 | 5 | · | 2 | 39 |
| M9 | 30 | 1 | 4 | 6 | 41 |

## Lean coverage of the headline (242 formalized families)

same 176 (73%) · different 34 (14%) · weaker 32 (13%)

## Reliability

| field | pass A vs pass B agreement | κ |
|---|---|---|
| A_matrix | 91% | 0.89 |
| A_prefix | 84% | 0.80 |
| B_problem | 94% | 0.88 |
| B_outcome | 94% | 0.89 |

Final labels vs the in-depth v1 labels through the v1 mapping (39 families): A 90%, B 79%.
