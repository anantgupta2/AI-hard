# 075 Lean layer map: open concerns

Source: helper agent spawned by the 075 family analyst. It mapped `lean/OAI/Analysis/FourierLLogL/{Procedure,Capture,Snapshot,Edges,Plateau,Paths,Assembly}` (75 files, about 13.7k lines). The analysis is at text level; the Lean was not built.

## Formal chain
`gridProof : GridBound` (Assembly/Endpoint.lean:18, constant C = 10^222) is built from:
- `plant` (Procedure/Tree.lean:58)
- `stage_shift` (Assembly/Cast.lean:138)
- `annual_valid` (Assembly/Gross.lean:35)
- `grossOur` / `grossDry` (Assembly/Weighted.lean:82/120)

The chain is closed within these directories, given Thermal/Compress. There are no sorry, axiom or native_decide uses, and no vacuous hypotheses were found. `decide` occurs only as Bool coercions or a trivial fact.

## Concerns to check downstream
1. **GridBound drops the ε_j multipliers.** `FinShift` uses the fixed sign `Gi = H_L − H_R`, whereas the paper's Prop dyadic quantifies over arbitrary F_{j+1}-measurable |ε_j| ≤ 1. GridBound is also a good-set statement (`finGood`, cutoff (j+1)³), not the paper's stopped sum with τ and e^{4h}. Both differences live in the Dyadic layer. Confirm that this special case suffices for the comparator theorem.
2. **The simultaneous regular-evidence statement is never formalised.** A multiplicative path-product score supermartingale (`rare`, Rare.lean:66) replaces it. That is logically sufficient for the assembly.
3. **`log_mass_budget` covers only the final state,** not the maximum over states as in the paper's X_*. It is still enough for `burn_rate`.
4. **Hypotheses the paper does not state:** `1000·2^J ≤ 2^M` appears in `grossOur`, `rating_bound`, `rare` and `stake_upper`.

## Route substitutions (Lean vs paper)
- Everything is finite: ZMod 2^M grids and finite laws. There is no MeasureTheory or martingale library; every supermartingale argument is a home-made finite-tree induction.
- Continuous noisy labels become a discrete heat-type kernel. Labels are integrated, not sampled.
- The scalar potential ψ becomes Huber + b·x². This gives a stronger √b bound.
- Relative entropy for snapshots becomes triangular discrimination.
- The count cap is not a transfer rule. Its validity is derived instead (`fund_est`).
- High-probability prefix statements become random parameters t = 2·log(score) with E[score] ≤ const.
