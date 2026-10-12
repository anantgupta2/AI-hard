# 161 Downstream: C1 rank-layer limit (I08 + I25)

**Item.** The signed half-rank kernel is K_ξ(Z) = 1{rank Z = r, sign Z = ξ}/P(·) on symmetric D×D matrices over F_q, with D = 2r. When a face center Y_j is integrated out, the product of these kernels over B converges to an exact pair-sign model, ∏(1 + c₀ η_e ξ_ij ξ_kj), in which the η_e are independent uniform signs. Averaging over η leaves one parity test of four incidence signs for each pair that lies in two faces. This reproduces a 3-wise (hypergraph) parity obstruction inside an ordinary bipartite density. The kernel object alone is N0 (a Huo–Wan scheme class). Novelty pass: provisional N3, F5.

**Type.** A witness/design item. Device reuse means the same design produces other witnesses or refutes other conjectures.

**Method.** Text-level only: no `lake build` or comparator run, because the checkout is shared. The dependency chain comes from `data/items/161_lean.json`, cross-checked by grep. arxiv.org was unreachable, so the literature rests on search summaries (unverified).

## Part A: Is it in the Lean?

**lean_status: `as in paper`.** `rankLayerLimit_proved` (Coefficients.lean:776) proves `RankLayerLimit` (Discriminant.lean:465), which is lem:rank-layer word for word. Like the paper, it is stated for the fixed 13 × 22 corner set. Its content is on the comparator path, but the packaged theorem itself is not.

### Correction to novelty.json
`rankLayerConvergence`, `rankLayerLimit_proved`, `RankLayerLimit`, `layerCorrelation` and `signModelCorrelation` have **0 dependents**. They are proved side theorems and are *not* on the path to `main`.

The comparator still uses the item's content, through this route:
- `main` → `main_proved` → `exists_symmetric_kernel` → `exists_oriented_kernel` → `typedMatrixKernel_tendsto` → `conditionalMatrixMoment_tendsto` → `configuration_even_rank_limit`.
- `configuration_even_rank_limit` uses only **D = 4r, so c₀ = 1**.
- It then branches into:
  - **Center limit:** `configuration_bool_tendsto`. This covers the transverse case, the singular tail, and the half-rank sign mechanism: `pairLocal_mismatch` → `signed_pair_compatibility` → `half_rank_projection` → `complementary_rank_iff` (I25).
  - **Independent η:** `pairBool_test_tendsto` → `pairSign_moment_tendsto`.

Dominated shares agree with the earlier "≈84% of lines prove I08" estimate: 0.28 / 0.38 / 0.43 along the chain.

### Gaps
- The c₀ = −1 branch (D ≡ 2 mod 4) is formalised off-path only.
- The reversed-difference clause is not stated separately. It is covered by `rankKernel_neg` and `activationMatrixKernel_symm`.
- Uniformity in B is implicit: the family is finite.
- D₀ is non-constructive, with D₀ ≥ 1642.
- There is no general-complex version:
  - 16 files (9,540 of 23,761 lines, with 543 `decide`) hard-code Fin 13/22/33.
  - 19 files (14,221 lines) are complex-agnostic and reusable as is.
- No `sorry`, `axiom` or `native_decide` was found.

Verbatim declarations, each tagged on-path or off-path, are in `downstream.json → lean_source` (18 entries).

## Part B: Where to try it

### Speedup targets (known theorems)
There is **no strong candidate.** The device creates deficits in *nonnegative* densities:
- Positive Sidorenko theorems cannot be shortened by it.
- Hypergraph and signed-kernel counterexamples are already one page long and need no center kernel.

Measurable but weak candidates:
- **S1:** the second template witness (also listed as OP1). This is the only one that would count as reuse.
- **S2:** the hypergraph loose-triangle and tight-cycle examples. The device only runs backwards here (low).
- **S3:** the MacWilliams / Huo–Wan layer counts. This would be reuse of the tooling, not of C1.
- **S4:** the quadratic-phase linear systems (Fox–Pham–Zhao). A cousin result only.

### Open or new problems (ranked; Lean-usable first)
| # | Target | Lean | Match | Conf. |
|---|---|---|---|---|
| 1 | **OP1:** Levi graph of the second 13-point template complex (plantri #49243) is non-Sidorenko | statable now | exact design | 0.55 |
| 2 | **OP2:** a template theorem for general complexes, giving an infinite family (n ≥ 14 sphere triangulations) | < 300 lines | full | 0.35 |
| 3 | **OP3:** a 2-colour uncommon bipartite graph (H or a template graph) | statable now | partial | 0.2 |
| 4 | **OP4:** an abelian Cayley-host counterexample for H | < 300 lines | kernel level is already Cayley on (S_D, +) | 0.25 |
| 5 | **OP5:** K₅,₅∖C₁₀ (Möbius strip) | statable now | weak; device should fail | 0.05 |
| – | **OP6:** edge-transitive non-Sidorenko graphs | statable now | pinning fails on symmetric graphs | 0.15 |
| – | **OP7:** KNRS for H; whether the 1-subdivision of H is Sidorenko | < 300 lines | reduces to OP4 | 0.15 |
| – | **OP8:** 4-uniform analogue (triple parity) | major library | no ternary analogue of I25 | 0.15 |

Notes on these targets:
- **OP1 is checked locally.** The second complex is a 13-point sphere triangulation: every pair lies in two faces, χ = 2, and colour refinement is discrete. Its degree sequence is 4⁴5⁴6⁵, against 4³5⁶6⁴ for the original, so the two Levi graphs are not isomorphic. Its tail needs a 20-cut mixture, whereas the Lean's Exposure/Coercivity assume 3 bit-partitions.
- **OP1 is the cleanest Lean speedup test.** Use the 14,221 agnostic lines plus a parametrised C1 as library L+, and compare against the original 23,761-line proof.
- **OP2 is the strongest reuse test.** A hit would give genuinely new witnesses from one device.

### Theorem corollaries (do not count as reuse)
- The forcing failure, amplification and injective Erdős–Simonovits benchmark from the paper. None of these is formalised.
- From external theorems (all unverified):
  - Turán exponent ex(n,H) ≥ n^{2−33/65+c}, via Conlon–Lee–Sidorenko.
  - A random-Turán bound, via Nie–Spiro.
  - H is not k-common for some k, via Kráľ–Noel–Norin–Volec–Wei.
  - Zhao's averaging hypothesis must fail for H, if his reduction holds as stated.

### Negative controls
- **NC1, Q₃.** Q₃ is the Levi graph of the tetrahedron boundary, where every pair lies in two faces. It is Sidorenko by Hatami. The device fails there as it should: colour refinement is not discrete, and the template enumeration has 0 survivors for n ≤ 8.
- **NC2, Lovász local Sidorenko.** No perturbative deficit is possible near the constant kernel.
- **NC3, abelian Cayley hosts and F₅,₃.** Even subdivisions satisfy Sidorenko on abelian Cayley hosts (Zhao). F₅,₃ has every pair in three faces, so averaging gives 1 + ab + ac + bc rather than a parity test, and it is weakly norming.
- **NC4, positive graphs.** With real-valued kernels the signs are free, so the device has nothing to do.

## Reuse and precedent
- **In the release:** none.
- **After the release:**
  - `rohanarun/sidorenko-template-refinements` (Codex, Oct 9–10 2026) reuses the design only inside its own template:
    - no template complex exists on ≤ 12 points;
    - exactly two classes exist at 13 points; the second is an unproved witness;
    - it lowers one tail constant, so that step needs only D ≥ 190 instead of 1642.
  - `artuskg` (a fork) was not read.
- **Earlier equivalent:** none found, so there is **no downgrade.** The hypergraph sign model is the target, not the device. Sidorenko's Levi-graph theorem only concerns signed kernels.
