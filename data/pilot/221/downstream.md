# Family 221: downstream targets for the shifted target tree S⁺ with charging of fresh splits

**Analysis mode.** Text level only. The Lean was not compiled (there is no local toolchain).
- `data/items/221_lean.json` is an older extraction that lacks dominated shares. I re-ran `scripts/extract_lean.py 221` into the scratchpad and left `data/items` untouched.
- No web queries ran for 221 because of a session limit. All external references are from memory and not re-verified.

## Part A: is the item in the Lean?

**Yes. lean_status: as in paper.** The item's location was previously unpinned; it is now found.

| Paper | Lean |
|---|---|
| S⁺ (every internal branching depth +1) | `ShiftedTree.lean`: `bottomUnary` :16 (old tree, depths kept), `doubled` :145, `shiftedTwinDepths` :147 (= branchingDepths + 2 inside the doubled tree), `NoAdjacentBranchDepths` :157 |
| "shifted depths are not old branching depths" | `shifted_twin_old_count` :160 |
| "2b target vertices must be fresh" | `shifted_twin_target_count` :173 |
| Lemma tree:charging (trees.tex:393) | `labeledHistory_charging_bound` (HistorySelector.lean:155), `prescribed_history_charging_bound` (ShapeCharging.lean:30), `chargeBound` (ActualCharging.lean:709) |
| relative bound after dividing by J = κ(S⁺)² | `shiftedCharge` (MatrixRoot.lean:30), `shiftedCharge_relative_bound` (RootMatrixTriple.lean:110), `node_frame_charge_uniform` (RegularNodeGeometry.lean:64) |

### Comparator chain

The device sits on the proof path of the comparator target `mezard_parisi`:
- `mezard_parisi` → `variationalValue_le_liminf_pressure` → `admissible_trial_lower` → `symmetric_trial_lower` → `bounded_symmetric_trial_lower` → … → `regular_node_pointwise`;
- then → … → `root_matrix_three_copy` → `matrix_three_copy_pointwise` → `projection_history_cost` → **`prescribed_history_charging_bound`** → `labeledHistory_charging_bound`.

The shift branches off from `regular_node_pointwise` in two places:
- `node_frame_charge_uniform` → … → **`shifted_twin_target_count`**;
- `scheduled_regular_old_count` → … → **`shifted_twin_old_count`**.

### Gaps

- **Encoding of the shift.** The Lean works with two aligned copies (`doubled`), so the charged set is "branching depths + 2".
- **General position.** The general-position hypothesis is an explicit predicate, `NoAdjacentBranchDepths`.
- **Constants and normalizer.**
  - The charging constant is a recursive `chargeBound`, where the paper uses k!/(k−b)!·(q+k)^b·(2(q+k))^{k−b}.
  - The normalizer is a full-to-protected-pair κ ratio rather than κ(S⁺)². Powers of L cancel exactly.
- **Wider scope than the paper.** The Lean lower bound `symmetric_trial_lower` holds for **any arity** with symmetric disorder. The paper fixes even p (model.tex:3).
- **Second in-family use (charging only).** The charging count, without the shift, is reused in `qExpect_grid_branching` (QTreeLaw.lean:112) for the Q_k regular-shapes bound.
- **Small declaration-level shares.** The novelty pass's 0.80/0.67 were file-import shares. At declaration level:
  - `prescribed_history_charging_bound`: 0.0014;
  - `node_frame_charge_uniform`: 0.0115;
  - `regular_node_pointwise`: 0.086.
- **formalization.yaml.** Family 221 is not listed there.

## Release reuse: a notable finding

The SATComputability formalization (lean/docs/235.md; paper *Computing the Random 3-SAT Threshold*, Sep 27 2026) depends on 221's lower bound.
- `SATVariational.lean` calls DilutedSpin's `symmetric_trial_lower` on `satModel : Model 3`, which has **odd arity**.
- The dependency path to the comparator is: Main → `threshold_program` → `satTrialSeparation` → `satTrialEvaluation_negative_witness`/`dense` → `exists_fully_rational_trial_near_pressure` → `symmetric_trial_lower` → … → charging.
- So a second comparator transitively uses the device.
- This is **theorem-level reuse**: the lower bound is applied to a new model. Under the brief's rules it is a corollary, not device reuse.
- The 221 paper's remark (consequences.tex:131-138) presents the 3-SAT work as using a different functional. That is true for its upper bound only.

The device itself (shift plus charging) is used nowhere outside DilutedSpin.

## Part B: targets

### Speedup targets

1. **Decorrelation step with vs without the shift lemmas** (`root_matrix_three_copy`, `node_frame_charge_uniform`). Statable now. Expected speedup high.
   - This is the item's own job, so it is a discoverability and calibration arm.
   - The trace's clause C10 gives a natural hint arm.
2. **Q_k regular-shapes lemma via `charging_final_shape`.** Statable now. Expected speedup low to medium (the paper's direct proof is one paragraph).
3. **Panchenko's finite-RSB MP structure theorem** (J. Stat. Phys. 2016, arXiv:1406.4702). Needs a major new library.
   - The obstruction is the same. The device helps the free-energy consequence, which is a corollary; it helps the structural theorem little.

No strong external speedup candidate was found. The device is tightly tied to the paper's tree calculus.

### Open problems

| Problem | Lean | Payoff / conf. |
|---|---|---|
| MP formula for the diluted antiferromagnetic Potts model / random-graph colouring (upper bound: Contucci–Dommers–Giardinà–Starr 2013) | < 300 lines | high / 0.3. The tree calculus is spin-agnostic; needs colour-valued marks |
| MP formula on random regular graphs (Concetti, arXiv:2508.17049, gives one inequality) | major library | high / 0.25 |
| One-sided MP lower bound for multi-species or bipartite diluted models | < 300 lines | med / 0.4. The device needs no positivity, but the open part is the upper bound |
| MP-type formula for diluted vector-spin (O(m)/XY) models (dense case: Panchenko, arXiv:1512.04441) | major library | med-high / 0.2 |
| Sparse inference with mismatched priors (Barbier–Panchenko, arXiv:2005.03115). Weak match: under Nishimori symmetry r = 0 and the device does nothing | major library | med / 0.15 |
| Odd-arity lower bound (soft 3-SAT) | statable now | already realized by the SATComputability formalization (corollary) |

### Corollaries and controls

- **Theorem corollaries:**
  - the SATComputability use above;
  - the Viana–Bray, diluted even-spin and soft even-K-SAT instances;
  - the zero-temperature ground-state formula;
  - the high-temperature RS case.
- **Negative controls:**
  - the Panchenko–Talagrand upper bound, already in the Lean without the device: an ideal control;
  - the SK Parisi formula;
  - the RS case r = 0 (b = 0, nothing to charge);
  - odd-arity upper bounds.

## Top 5 (Lean-usable first)

1. Decorrelation step, ablating the shift lemmas. Statable now.
2. Q_k regular shapes via the charging bound. Statable now.
3. One-sided MP lower bound for multi-species or bipartite models. Needs fewer than 300 lines.
4. MP formula for the diluted Potts antiferromagnet. Needs fewer than 300 lines.
5. Panchenko's finite-RSB structure theorem. Needs a major new library.

## Precedent

- **After 2026-10-06:** not searched on the web this session.
- **Earlier equivalent:** the novelty pass found none, among GG98, AC98, Barra–De Sanctis, Panchenko 2013–16 and Barbier–Panchenko. No downgrade on current evidence.
- **Main risk:** an expert may recognise the shift as folklore.
