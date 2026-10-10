# Family 362: downstream targets for the direction-change count

**Item (Lemma `ang:direction`, direction.tex:22).**
- **Setting.** Assume the signed increment bootstrap. Take a supported characteristic with momentum size q ~ w on an interval of length at most (w/P)².
- **Stopping rule.** Stop whenever the direction ξ = V/|V| has moved chordal distance δ from its value at the previous stop.
- **Conclusion.** The number of intervals is at most C(M,A)·L⁶/δ, where L = log(2+P).
- **Hypotheses.** w ≥ P^{3/5} and w^{-3/5} ≤ δ ≤ w^{-1/10}.
- **Mechanism.**
  - Each complete interval forces |∫ψ wξ_t| ≥ wδ/2, where ψ is a ramp weight with total variation 2.
  - Summing these against the signed force identity bounds the count.
  - Only derivatives of the weights cost a factor N, and that factor is absorbed for large P.

**Type:** F3. The machine-readable version is `downstream.json`, with 8 verbatim Lean declarations.

## Part A: Lean

**lean_status: `as in paper`.** I worked at text level; nothing was compiled.

**Key declarations:**
- `WeightedDirectionPartition` (DirectionCounts.lean:451). This structure records the stopping times, the ramps, `direction_control`, `exit` (= δ), `signed_exit` (≥ wδ/2) and `variation` (= 2).
- `IncrementBootstrap.weighted_direction_partition` (:471) builds such a partition from the bootstrap.
- `complete_force_lower` (:560).
- `direction_complete_count_cost_bound` (:711).
- `direction_count_bound` (:1065): `D.count ≤ C*(log(2+P))^6/δ`, eventually in P.

**Comparator chain.** There are 21 steps from `global_classical_solution`:
1. population increment
2. signed increment
3. force bulk
4. unselected label/source
5. `representative_pure_occupation`
6. `direction_closedEulerian_improved`
7. `exists_bounded_direction_partition`
8. `direction_count_bound`
9. `direction_complete_count_real_bound`
10. `direction_complete_count_cost_bound`

The full list is in the JSON. `direction_count_bound` has a dominated share of 0.10.

**Gaps.**
- **Weaker δ bound.** The Lean only needs δ ≤ 1, where the paper needs δ ≤ w^{-1/10}. The Lean statement is therefore slightly more general.
- **Any partition, not just the greedy one.** The Lean bound applies to every `WeightedDirectionPartition`, not only to the greedy first-exit partition.
- **Context assumptions made explicit:** |V| ≥ w/16, and the bootstrap holds on a compact S ⊇ supp f₀.

## Precedent

- **Generic pattern: standard.** Counting first exits by a stopping time and summing against a budget is standard (Lépingle / p-variation jump counts; Pfaffelmoser cells).
- **Specific use: no near-equivalent found.** This is the combination of signed weighted exits, the signed Lorentz-force identity, and absorption of the weight-derivative cost.
- **Neighbouring work avoids the issue:**
  - Wang (2020/2026) closes the same loss by symmetry.
  - Cheverry–Ibrahim explicitly avoid controlling directions.
- **After Oct 6:** nothing found.
- **Novelty grade:** novelty.json gives N3 (provisional, 0.30), with D2 more likely.

## Part B

**Verdict: no strong external speedup candidate found.** The device is tailored to the receiver-acceleration loss in large-data 3D relativistic Vlasov–Maxwell (RVM). Known theorems in this area either follow from 362's main theorem or never face that loss.

| # | Target | Kind | Lean score | Payoff / speedup |
|---|---|---|---|---|
| S1 | 2.5D RVM global existence (Glassey–Schaeffer 1997/98) | known | < 300 (adapt Model.lean, 109 lines) | low |
| S2 | Nearly neutral multi-species 3D RVM (Glassey–Schaeffer 1988) | known | < 300 | low, likely none |
| S3 | `direction_count_bound` itself (positive control) | in-family | statable now | high, by construction |
| O1 | Multi-species 3D RVM with large data | open | < 300 | new theorem; conf. medium-low |
| O2 | 3D RVM with decaying, non-compact momentum data (cf. Wei–Yang 2020) | open | < 300 | new theorem; conf. low |
| O3 | 3D RVM on T³ | open, probably routine | < 300 | new theorem; conf. medium |
| O4 | Vlasov–Darwin with large data | open | < 300 | weak match; conf. low |
| O5 | RVM in a bounded domain | open | major library | partial |

**Theorem corollaries (not reuse):**
- Wang's large-data cylindrically symmetric global existence (arXiv:2203.01199).
- Continuation criteria (Glassey–Strauss, Luk–Strain) become vacuous.

**Release reuse:** none found.

**Negative controls:**
1. **3D Vlasov–Poisson.** It has no receiver-acceleration loss, and Pfaffelmoser's argument suffices without any direction count.
2. **1.5D RVM.** Momentum support is controlled directly by conservation laws, so there is nothing to count.
3. **Absolute-force control only (no signed bootstrap).** Here the count blows up to about w^{1/2}L/δ.

## Top 5

1. **S3, the positive control.** It is statable now and is the only place where the device is known to carry the proof.
2. **O1, multi-species RVM.** It faces the same obstruction on every characteristic.
3. **O3, the torus.** A cheap transfer test.
4. **S1, 2.5D RVM.** A low expected speedup.
5. **Vlasov–Poisson, as a negative control.** It should show no speedup.
