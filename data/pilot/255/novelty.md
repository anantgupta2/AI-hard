# Family 255: novelty analysis (QI recognition of virtually polycyclic groups)

Analyst role: novelty. Date: 2026-10-12. Machine-readable version: `novelty.json`.

**L** = Mathlib d13f23b plus 255's 28-entry bibliography (EFW, Peng I–II, Shalom, Cornulier–Tessera, Dymarz, DFX, Farb–Mosher, Guivarc'h, Gromov, Li, KMN, Bieri, Ganzburg, Grayevsky–Pallier, Le Boudec, ...). No reasoning trace was released. The release's Lean is trusted as published and was not built.

**Access caveat.** WebFetch could not reach arxiv.org, ar5iv, msp.org or math.uchicago.edu (DNS failure), and the proxy refused export.arxiv.org (403). All literature checks are therefore at WebSearch snippet level, and no abstract or PDF was read directly.

## 1. Verdicts first

**Provenance: no.**
- The cited 2025 works are human-authored, with no AI disclosure in the search summaries (unverified):
  - Grayevsky–Pallier, arXiv:2509.12823;
  - Le Boudec, arXiv:2510.24581;
  - DFX, arXiv:2304.12498.
- Searches pairing the conjecture with ChatGPT, GPT-5, OpenAI or "AI-assisted" found no model-produced precedent, and no expert commentary on 255 itself.
- The Lean reuses about 117 declarations from three other OAI dirs: Thompson (invariant means), CyclicSeries, and CriticalPercolation/Nilpotent. This is pure infrastructure and touches no candidate.

**Final grades**

| ID | Item | N | F | Conf. | Lean-backed |
|---|---|---|---|---|---|
| C1 | Reflection doubling for neighbouring labels (Prop 7.1 + tuple lifts) | **N3 (weak candidate)** | F3 (F4 flavour) | 0.35 | **yes**, on the chain of all 3 targets |
| C2 | Cone-quotient Haar trace tests / conditioned probes (Prop 8.3) | N2 (was N3 weak) | — | 0.55 | yes |
| C3 | Volume exponent P(E) + symmetry group 𝒜_G | N2 | — | 0.7 | yes |
| C4 | Affinity criterion (Lemma 6.6) + anti-folding inequality | N2 | — | 0.65 | yes |
| C5 | Inverse coupling (Lemma 5.5) | N1 (was N2) | — | 0.5 | yes |
| C6 | I23, I26, I33, I38 | N2 | — | 0.65 | yes |

**family_D: D3 (provisional, weak), confidence 0.35.**
- It rests on C1 alone.
- It falls to D2 under any of three conditions:
  - Peng II §4 ("Aligning the linear part of standard maps") turns out to be volume-based;
  - an expert calls cross-tile "unfolding doubles volume" folklore;
  - test P-C1 finds the device easy to discover once P is given.

## 2. Lean: are the N3 candidates load-bearing and on the comparator chain?

These figures come from `data/items/255_lean.json` (extractor v3, 7,308-declaration target DAG). The height core is the closure of `exists_uniform_height_intrinsic`, 3,970 declarations. Dominated share means the item is reachable from the targets only through that item, so a knockout disconnects it.

**Both candidates are on the dependency chain of all three comparator targets.** `group_recognition` and `lattice_recognition` both close over the height engine. The chain is:

`main_uniform_bounded_height → uniform_bounded_height → exists_uniform_height_intrinsic → … → exists_uniform_published_sublinear_height (Prop 9.4) → … → exists_uniform_identical_neighbor_profiles`

It then splits:
- into labels, `→ exists_uniform_neighbor_common_affinity → … → good_root_neighbor_labels_eq → affine_labels_eq_of_template_comparison → exists_reflection_templates → exists_reflected_direction_of_finite_labels`;
- into offsets, `→ exists_published_polar_offset_threshold → … → original_neighbor_offset_nonpos`.

| Cluster | Dominated decls | % DAG | % core |
|---|---|---|---|
| Prop 7.1 (`good_root_neighbor_labels_eq`) | 287 | 3.9 | 7.2 |
| … finite-dim reflection step (`exists_reflected_direction_of_finite_labels`) | 4 | 0.05 | 0.1 |
| … alternating-product volume bound (`path_alternating_product_exponent_le`) | 80 | 1.1 | 2.0 |
| Prop 8.3 (`exists_published_polar_offset_threshold`) | 447 | 6.1 | 11.3 |
| Neighbour stage, labels + offsets (`exists_uniform_identical_neighbor_profiles`) | 791 | 10.8 | 19.9 |
| Affinity criterion (`affine_profile_of_segment_inequalities`) | 181 | 2.5 | 4.6 |
| Inverse coupling | 72 | 1.0 | 1.8 |

**Correction to family.md.** Its figure of "<1% / 0.1% of the height core" applies only to the finite-dimensional reflection lemma. Measured by cluster, as the PLAN asks for distributed formalizations, Prop 7.1 dominates 7.2% of the core. That is below the 20% proxy, but it passes the knockout test.

## 3. Candidate notes

**C1, reflection doubling.**
- **Mechanism.** Co-location on the α_i facet forces A₁⁻¹A₂ to be the facet reflection. An inward segment E then has opposite target images, with P(E′₁∪E′₂) = 2P(E). Alternating switch bundles on the two sheets give target volume e^{2rP(E)}, while the source terminals are covered by e^{rP(E)} balls.
- **Neighbours:**
  - Peng 2011 II §4 aligns linear parts across tiles. It is the same sub-problem and a named precedent (intro:43-47), but its mechanism is unverified.
  - EFW and Ferragut use quadrilaterals, a different mechanism.
  - Internally, C1 is the cross-sheet mirror of the paper's own anti-folding inequality I28 and an application of its P-comparison (Lemma 5.4).
  - Ping-pong growth is genuinely different.
- **Tests:**
  - Test 2: passes.
  - Test 3: passes by knockout.
  - Test 4: protocol P-C1.
- **Grade.** It stays an N3 candidate only because no external work with this mechanism was found. The risk is high.

**C2, offset probes.** The Haar multiplier of a nilpotent quotient used as a height meter is the measure-scaling idea of Farb–Mosher, Dymarz, Dymarz–Xie and DFX; the paper's own §10 also uses it. The sub-problem is Peng II §5, "Patching". The exact-cancellation probe pair is engineering, so C2 is **N2**.

**C3, P and 𝒜_G.**
- For abelian N it reduces to the EFW/Peng box volume.
- The bracket "sum of separate maxima" is Guivarc'h's homogeneous-dimension mechanism with exponential weights.
- 𝒜_G generalizes Peng's root permutations and the Sol flip.
- It is essential vocabulary (used by 10% of the core), but **N2**.

**C4, the affinity criterion.** It reaches Peng I's local-affinity conclusion by a volume route, from classical moves (support-vs-variation equality, chambers). **N2.**

**C5, the inverse coupling.** This is Shalom's symmetric coupling specialized to the height cocycle. **N1**, on the N1/N2 boundary.

## 4. Bridge novelty
| Import | Status |
|---|---|
| Shalom couplings + reduced H¹ → height slopes | known route (Shalom, Sauer, Cornulier–Tessera) |
| Coarse differentiation / box volume | known route (EFW, Peng, Ferragut) |
| Guivarc'h bracket counting → P | known route (variant) |
| **Multivariate Remez inequality → keeping volume under restricted parameters** | **new bridge (tentative, 0.4)**: standard in homogeneous dynamics; no QI-rigidity use found |
| Haar multipliers on nilpotent quotients → height | known route (Farb–Mosher, Dymarz, DFX) |
| Hörmander hypoellipticity → affine limits (paper only) | known route (adjacent: Carnot regularity) |
| Gromov + Li/KMN/Bieri endgame | known route (Shalom, Sauer, Kropholler et al.) |
| Polyhedral-norm isometries / facet reflections | known route |

## 5. Discoverability protocols (not run)
**Common setup:**
- **Models:** cutoff before 2026-09-24, verified with a canary probe; the OpenAI release model is excluded from the main pool.
- **Arms:** two arms, open and directed. The directed arm includes §§2–6 verbatim.
- **Sampling:** n = 256 per arm; pass@k for k = 1…256.
- **Judging:** two judges plus a human check.
- **Controls:**
  - positive: Cook–Reckhow extension variables;
  - negative: C5, I23, and the finiteness of 𝒜_G.

**P-C1:**
- **Hide:**
  - `labels.tex`, plus everything downstream (§8–11);
  - in Lean, the 287-declaration cluster and the chain above it.
- **Hit:** a proposal must contain both:
  - (a) the facet-reflection structure of the label mismatch;
  - (b) a volume-exponent contradiction from paths alternating between the sheets, with target P = 2P(E) against source P(E).
- **Partial credit:** (a) alone, or an EFW-style quadrilateral argument.

**P-C2:** hide Prop 8.3. A hit means detecting cone-trace functionals of b₂−b₁ through Haar multipliers on cone quotients, in both directions.

**P-C3:** a calibration arm for P.

The trace's pivot distance and chain depth cannot be reported, because no trace was released.

## 6. Open questions
1. Read Peng II §4–5 in full. If it is volume-based, C1 falls to N2 and the family to D2. This is the single most important pending check.
2. Verify all snippet-level claims against the PDFs.
3. Ask experts (Peng, Dymarz, Xie, Pallier, Cornulier, Fisher) whether the alternation-doubling count is folklore.
4. Downstream: does the device shorten any *other* theorem (e.g. Heintze-type or Sol₅-like rigidity), as opposed to corollaries of Thm 1.4?
5. Confirm the Remez bridge.
