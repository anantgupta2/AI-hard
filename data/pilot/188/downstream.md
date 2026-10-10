# Family 188: downstream targets for the max-norm semigroup via star averaging

**Analysis mode.** Text level only. The Lean was not compiled (there is no local toolchain). Dependency paths come from `data/items/188_lean.json` (extract_lean v2), checked by hand. Web access ended after three searches (session limit), so references not seen this session are flagged.

## Part A: is the item in the Lean?

**lean_status: as in paper.**

All four pieces are formalized and lie on the comparator's proof path:
- the factorization P = UV;
- the bound ‖e^{−sP}‖∞ ≤ 1+2s;
- the mixed-norm Dyson expansion;
- the uniform bound sup_{s≤log n} ‖e^{−sA/D}‖∞ ≤ C₁(1+log n)^J.

### Key declarations (verbatim statements are in `downstream.json` → `lean_source`)

| Declaration | File:line | Role |
|---|---|---|
| `starAverage`, `incidenceDegree` | Process/IncidenceDegree.lean:154, :151 | V = star average |
| `star_semigroup_bound` | Process/IncidenceDegree.lean:218 | abstract ‖exp(−s·U·V)‖ ≤ 1+2s (row sum 2 hard-coded) |
| `edgeIncidence`, `globalStarAverage_factorization` | Process/EdgeIncidence.lean:25, :48 | P = U·starAverage U |
| `graph_star_semigroup_bound` | Process/EdgeIncidence.lean:62 | paper eq. (average-semigroup) |
| `goodPrefix_semigroup_quantitative` | Spectral/GlobalLinkAdjacencyHermitian.lean:26 | P+R split + mixed-norm expansion |
| `goodPrefix_uniform_semigroup` | Process/GraphCardSqrt.lean:38 | paper Prop. semigroup |
| `graph_star_approximation` | Spectral/GraphStarApproximation.lean:26 | trace-method input (classical ingredient, not the device) |
| `movingStarMean`, `movingStarLift`, `movingStar_trajectory_representation`, `movingStarResponse_linf`, `movingStar_mixed_stability` | Spectral/MovingStarDegree.lean, Asymptotics/ActiveL2Map.lean:290, Stability/MovingResidualForcing.lean:115 | the device re-derived for the prefix |

### Comparator chain

The chain runs from `sharp_terminal_leave` (Main.lean:79) down to the device:
- `sharp_terminal_leave` → `sharp_terminal_leave_l2` → `main_l2_prefix_failure_bound` → … → `goodPrefix_survival_moments`;
- then → `goodPrefix_cavity_semigroup` → **`goodPrefix_uniform_semigroup`** → **`goodPrefix_semigroup_quantitative`** → **`graph_star_semigroup_bound`** → `star_semigroup_bound`.

There are two side branches:
- one reaches `graph_star_approximation`;
- one reaches `perturbation_mixed_norm_bound` (Volterra.lean:190).

The prefix branch is a second, independent use of the device:
- `sharp_terminal_leave_l2` → `uniform_prefix_obligation` → … → `prefix_edge_barrier_improvement` → `movingStar_mixed_stability`.

### The reuse signal, examined

The shortlist's reuse claim holds, with one qualification.
- **What the prefix does.** The Lean's self-contained prefix replaces the paper's Joos–Kühn black box. It writes the centred codegree vector's one-step drift as −a_k(P_k + R_k)x_k (`prefix_centered_edge_recurrence`, `centered_edge_operator_drift`), where P_k is a *moving* star average on the shrinking edge set. It then closes an ℓ∞ barrier with a discrete mixed-norm stability lemma.
- **The qualification.** The prefix **does not call** `graph_star_semigroup_bound`, `star_semigroup_bound` or `perturbation_mixed_norm_bound`. It re-derives the same device as fresh code:
  - the representation x = M − U b with a vertex trajectory b;
  - the bound (1 + 2Σa_k);
  - the absorption step.
- **What is shared.** The two uses share only `globalStarAverage`, `globalLinkAdjacency` and `graph_star_approximation`.

So this is a genuine second application of the *idea* to a different statement (the prefix cone has dominated share 0.269 and about 7k exclusive lines). It is not reuse of the lemma, and it comes from the same model on the same process.

### Gaps

- The paper proves 1+2s with the push-through identity. The Lean uses an abstract `rectangular_semigroup_bound` with ‖VU−1‖ ≤ 1. The content is the same.
- `star_semigroup_bound` hard-codes row sum 2, so it does not cover r-uniform incidence.
- The constants are explicit in the Lean: J = 2K+1 with K > 4/γ, cycle length 8000, c = 1/80000.
- The comparator is exact, but the device is internal: dominated share 0.035 for `goodPrefix_uniform_semigroup`.
- Family 188 is not in `formalization.yaml`.

## Part B: targets

### Speedup targets (Lean-usable first)

1. **Triangle-removal prefix** (`uniform_prefix_obligation`, `prefix_edge_barrier_improvement`). Statable now. Expected speedup high, confidence 0.6.
   - It replaces BFL's per-codegree self-correction plus triangular extensions, and JK's 87 pages, with one linear ℓ∞ stability step.
   - Size baseline: the OAI proof, about 7k exclusive lines; the device files themselves are about 940 lines.
   - Caveat: same family, so this is not a held-out test.
2. **Ablation of Prop. semigroup** without the star factorization. Statable now. Expected speedup high. This is a calibration arm only.
3. **Triangle-free process tracking** (Bohman 2009, arXiv:0806.4375; Bohman–Keevash 2021, arXiv:1302.5963; FGM 2020, arXiv:1302.6279). Needs fewer than 300 lines of new definitions. Expected speedup medium, confidence 0.3.
   - It helps only if the open-pair drift operator turns out to be star-averaged, which is unchecked.
4. **Random-STS process input** (Kwan, arXiv:1611.02246). Needs fewer than 300 lines. Expected speedup low to medium.
5. **Bennett–Bohman natural barrier** (arXiv:1210.3581). Needs fewer than 300 lines. Expected speedup low.
   - In k-uniform incidence ‖W‖∞ = k−1, so the one-line bound fails; this is only a partial match.

### Open problems

| Problem | Lean | Payoff / conf. |
|---|---|---|
| JK sharp-leave conjecture for K₄, C₅ (other strictly 2-balanced F) | < 300 lines | high / 0.3. For K₄, two edges of a copy can be disjoint, so A is not a sum of stars |
| Sharp leave for K_{r+1}^{(r)} packing (Steiner systems), r ≥ 3 | < 300 lines | high / 0.3. The star structure matches, but ‖W‖∞ = r−1, so the device must be nested |
| Fluctuations of F_n (excluded by the paper's scope; Erdős #1155 asks finer questions) | statable now | med-high / 0.4 |
| Triangle removal from quasirandom or G(n,p) starts | statable now | med / 0.5 |
| Final size of the H-free process (Bohman–Keevash conjecture; Warnke; Picollelli) | < 300 lines | med / 0.2 |
| R(3,k) constant via steered processes (arXiv:2505.13371; 2510.19718) | major library | high / 0.1 (superficial analogy) |

### Corollaries, reuse and controls

- **Theorem corollaries (not device reuse):**
  - BFL F_n = n^{3/2+o(1)};
  - the Bollobás–Erdős Θ(n^{3/2}) conjecture;
  - the mean question of Erdős #1155;
  - JK Conjecture 16.2 for K₃.
- **Release reuse:** none outside TriangleRemoval. A grep for star-average identifiers across `lean/OAI` found nothing.
- **Negative controls:**
  - bounded-degree greedy processes, where the naive e^{O(D)} bound is already O(1);
  - r ≥ 3 incidence, where the one-line bound is false-in-spirit;
  - the K₄-removal linearization, which is not a sum of stars;
  - any ℓ²-only argument.

## Top 5 (Lean-usable first)

1. Triangle-removal prefix, give vs withhold the `movingStar_*` lemmas. Statable now.
2. Ablation of the semigroup proposition. Statable now.
3. Removal from quasirandom starting graphs. Statable now.
4. Triangle-free process tracking. Needs fewer than 300 lines.
5. Fluctuations of F_n. Statable now.

## Precedent

- **After 2026-10-06:** nothing found (thin search).
- **Earlier equivalent:** none. The push-through and line-graph identities are classical, but we found no use of them for an ℓ∞ semigroup bound for a process. No downgrade.
- **Unverified references:** arXiv ids not re-checked this session are 0806.4375, 1302.5963, 1611.02246, 1210.3581, 0908.0429 and 1007.3037.
