# Family 255, candidate C1: downstream analysis (reflection doubling for neighbouring labels)

- **Analyst role:** downstream.
- **Date:** 2026-10-12.
- **Machine-readable version:** `downstream.json`. It includes the verbatim Lean statements.
- **Scope of checks:**
  - **Lean:** read at text level only. It was not built (shared checkout) and is trusted as published.
  - **Literature:** WebSearch snippets only. arxiv is blocked, and ar5iv and projecteuclid failed DNS. Nothing below was read in full.

**Item C1 (Prop 7.1 + Lemma 7.2).** Suppose two sheets one generator step apart have different labels A₁ ≠ A₂ in 𝒜_G.
- Their limits agree on an α_i facet, so A₁⁻¹A₂ is the facet reflection.
- An inward segment E then has opposite images, with P(E′₁∪E′₂) = 2P(E).
- Alternating switch bundles on the two sheets reach about e^{2rP(E)} target terminals.
- The source terminals are covered by e^{rP(E)} balls. This is a contradiction.

## Part A: Lean status

**`lean_status`: as in paper.** The Lean follows the paper step for step:
1. facet agreement;
2. a reflection forced by the finite group;
3. the doubling identity;
4. the alternating-bundle exponent comparison.

The cluster is fully proved and lies on the dependency chain of all three comparator targets.

**Key declarations** (all under `lean/OAI/GroupTheory/PolycyclicRecognition/`):

| Decl | File:line | Role |
|---|---|---|
| `SupportDatum` (fields `weight`, `multiplicity`, `balanced`, …) | Analysis/SupportNorm.lean:27 | P data. `balanced` is unimodularity |
| `templateSupport` | Analysis/SupportTemplates.lean:31 | P(E) |
| `templateSymmetryGroup` | Algebra/TemplateSymmetries.lean:23 | 𝒜_G |
| `exists_reflected_direction_of_finite_labels` | Algebra/FiniteLabelReflection.lean:70 | finite group plus a fixed hyperplane gives C v = −A v |
| `SupportDatum.templateSupport_opposite_segments` | Analysis/ReflectedSegmentSupport.lean:67 | P(seg w ∪ seg −w) = 2·p(w) |
| `SupportDatum.reflected_segment_support` | Analysis/ReflectedSegmentSupport.lean:82 | the doubling identity |
| `exists_reflection_templates` | Algebra/FacetReflectionTemplates.lean:22 | equation (reflection-doubling) of labels.tex |
| `affine_labels_eq_of_template_comparison` | Algebra/FacetReflectionTemplates.lean:104 | the finite-dimensional contradiction |
| `CartanWordModel.path_alternating_product_exponent_le` | Geometry/CartanPathAlternatingComparison.lean:31 | alternating-bundle volume comparison |
| `tuple_lift_projection_volume` | Algebra/TupleLiftProjection.lean:28 | Lemma 7.2 piece |
| `CartanWordModel.good_root_neighbor_labels_eq` | Geometry/CartanGoodRootNeighborLabels.lean:38 | Prop 7.1 as used |

**Comparator chain.** `main_uniform_bounded_height` reaches `exists_reflected_direction_of_finite_labels` in 23 steps:

`main_uniform_bounded_height → uniform_bounded_height → exists_uniform_height_intrinsic → exists_uniform_cartan_height → exists_bounded_height_of_published_inputs → exists_uniform_published_bounded_height → exists_published_sublinear_height → exists_uniform_published_sublinear_height (Prop 9.4) → … → exists_uniform_published_chain_concentration → exists_uniform_identical_neighbor_profiles → exists_uniform_neighbor_common_affinity → exists_uniform_neighbor_label_threshold → eventually_root_neighbor_labels_eq → diagonal_root_neighbor_labels_eq → good_root_neighbor_labels_eq`

From there it splits:
- into `affine_labels_eq_of_template_comparison → exists_reflection_templates → exists_reflected_direction_of_finite_labels`;
- into `good_affine_templates_support_le → exists_coupled_profile_comparison_region → source_target_product_exponent_le → path_alternating_product_exponent_le`.

`group_recognition` (24 steps) and `lattice_recognition` (25 steps) join the same chain. Both call sites were checked in source.

**Where the weight sits (knockout / dominated sets):**

| Part | Decls | Lines |
|---|---|---|
| Whole Prop 7.1 cluster | 287 | 7,128 (121 files) |
| … coupled alternating comparison (`good_affine_templates_support_le`) | 264 | 6,364 |
| … `path_alternating_product_exponent_le` | 80 | 2,163 |
| Finite-dimensional reflection + doubling (`affine_labels_eq_of_template_comparison`) | 13 | 298 |
| … reflection lemma | 4 | 98 |
| … doubling identity | 3 | 30 |

**Gaps (all minor):**
1. **Packaging of Prop 7.1.** The paper states it for supports of limiting laws. The Lean uses good Haar sets with subexponentially decaying mass, plus a shrinking-δ diagonal. This is at least as strong.
2. **Invariant inner product.** The Lean pulls it back through a finite-orbit embedding inside the proof. The idea is the same.
3. **The doubling identity is elementary.** It is literally `balanced` (unimodularity) ⇒ p(−w) = p(w), a 13-line lemma.
4. **Lemma 7.2** is split across three declarations.
5. **Input Props** (Remez, exponential realization, Dynkin, Haar) are hypotheses of the cluster lemmas. They are proved elsewhere, and the targets carry none.
6. **The comparator says "some finite A"**, but the proof uses `templateSymmetryGroup`.

**Consequence for grading.** The two classical pieces carry no novelty:
- reflection lemma: N0;
- doubling identity: a trivial consequence of balance.

Any jump content sits entirely in the coupled alternating-bundle comparison, about 6k lines. **Suggested shortlist `lean_decls`:**
- `good_root_neighbor_labels_eq`
- `affine_labels_eq_of_template_comparison`
- `exists_reflection_templates`
- `reflected_segment_support`
- `good_affine_templates_support_le`
- `path_alternating_product_exponent_le`

## Part B: Where to try it

### Theorem corollaries (do NOT count as device reuse)
These follow from Thm 1.4 or Thm 1.1:
- Sol height-respecting and recognition (EFW).
- Peng I–II for nondegenerate unimodular split abelian-by-abelian groups. **Peng II Thm 4.1** (aligning linear parts across boxes) is moreover a special case of Prop 7.1 itself.
- Dymarz 2010, and DFX Thm 1.5 recognition, for unimodular SOL-like groups.
- Grayevsky–Pallier Thm C (Sol₅).
- Le Boudec Cor 3.7 (commable implies QI).
- The homomorphism H → 𝒜_G for uniform quasi-actions.

### Speedup targets (known theorems). Verdict: no strong candidate
| ID | Target | How C1 helps | Speedup | Lean |
|---|---|---|---|---|
| S1 | EFW: QIs of DL(n,n) / lamplighters are height-respecting | Rules out flip mismatches between adjacent tiles, using exact tree volumes n^{2r\|E\|} vs n^{r\|E\|}. Only a sub-step; coarse differentiation and quadrilaterals dominate | low–med | < 300 lines (trees with Busemann height, DL graph) |
| S2 | Ferragut 2026: horospherical products, swap consistency | Only for balanced products of isomorphic factors; the core uses quadrilaterals | low | major library |
| S3 | Rank-1 orientation agreement in Sol (EFW II, reused by Peng II §4) | C1 is uniform in rank, whereas Peng apparently needs a separate rank-1 EFW argument (unverified) | low; a special case, so it does not count | statable now (calibration only) |

### Open problems
| ID | Problem | Status | Match | Payoff / conf. / difficulty | Lean |
|---|---|---|---|---|---|
| O1 | Two-group bounded height: a QI G→G′ between unimodular real-triangulable groups induces L with P′∘L = P | Not in 255. A step toward Cornulier Conj. 19.113 (unverified) | Identical configuration | high / 0.45 / high | **statable now** |
| O2 | The same for non-unimodular groups whose 𝒜 contains reflections | Open (Cornulier program, pointed-sphere conjecture) | The mechanism survives; the doubling identity fails (no `balanced`) | high / 0.2 / very high | **statable now** (drop `huni`) |
| O3 | QI rigidity of DL_d(q), d ≥ 3, and higher-rank lamplighters | Open per BNW 2008 (unverified) | Strong: balanced W, 𝒜 = S_d, transpositions are facet reflections | high / 0.4 / high | < 300 lines |
| O4 | BNW Cayley-graph conjecture for DL(q₁,…,q_d) | Open (unverified) | Indirect, via O3 | med / 0.15 / high | < 300 lines |
| O5 | Horospherical products of ≥ 3 hyperbolic factors | Open beyond k = 2 | Factor permutations | med / 0.25 / high | major |
| O6 | Unimodular S-arithmetic Sol lattices, e.g. ℤ[1/p]² ⋊ ℤ | Unclear (unverified) | Mixed real/p-adic height with a flip | med / 0.15 / high | < 300 lines |
| O7 | Cross-field: facet agreement = rank-one connection (A₂−A₁ = A₁(R−I)), so C1 forbids "coarse laminates" (Ball–James analogue) | Speculative | Structural only | low–med / 0.1 | major |

### Negative controls
1. **H² = Aff⁺(ℝ) and H²×H² (non-unimodular): the Thm 1.4 analogue is false.**
   - Elliptic isometries move the height unboundedly.
   - `SupportDatum.balanced` cannot be instantiated, and P([−w,w]) = P([0,w]).
   - Any claimed reuse here is spurious.
2. **Trivial 𝒜 (BS(1,n), Sol(a,b) with a≠b, Heintze groups): the device is vacuous**, and the expected speedup is zero.
3. **Nilpotent groups (W = 0, P ≡ 0) and global flips.**
   - Here nothing is needed: neighbouring sheets are at bounded distance.
   - The Sol flip is an isometry. C1 must exclude only *mismatched neighbours*, never a global reflection.

### Top 5 (Lean-usable first)
1. **O1: two-group height (statable now).**
   - It is the cleanest reuse outside Thm 1.4.
   - The finite-dimensional half (298 lines) generalizes to two SupportData almost verbatim.
   - Every notion in the statement already exists in OAI: `SimplyConnectedSolvableLieModel`, `HeightSpace`, `MetricQuasiEquivalence`, `ModelIsUnimodular`.
   - Caveat: it reuses the same proof with two groups, so it is weak evidence of an independent speedup.
2. **O2: non-unimodular groups with reflections (statable now).** This test separates the *mechanism* (alternating bundles realize a union exponent) from the *identity* (balance).
3. **O3: DL_d(q), d ≥ 3 (< 300 lines).**
   - It is the strongest out-of-class structural match.
   - Exact tree volumes make the volume half elementary.
   - It still needs a higher-rank coarse differentiation for trees, which C1 does not supply.
4. **S1: EFW DL(n,n).** This is the only *known* out-of-class theorem where C1 competes with an existing proof. It is measurable, but the expected speedup is low.
5. **O6: S-arithmetic Sol lattices.** The statement is cheap to write in Mathlib (`Padic`, `SemidirectProduct`); the status is unverified.

## Precedent
- **After Oct 6, 2026:** nothing found that uses the device or comments on 255.
- **Peng II §4:** the same sub-problem; its mechanism is unverified. Snippets say:
  - for rank ≥ 2 the linear parts "have to be the same";
  - rank 1 "follows exactly the same proof as in [EFW2]".

  C1 is uniform in rank, which hints that the mechanisms differ. If Peng's rank ≥ 2 argument is a cross-tile volume count, C1 falls to N2. **Reading Peng II §4 in full remains the decisive pending check.**
- **EFW and Ferragut:** quadrilaterals, a different mechanism.
- **Classical pieces:** the reflection lemma is N0, and the doubling identity is elementary.

## Bottom line
Downstream evidence for a *confirmed* eureka step is weak.
- Inside Lie groups, every known theorem C1 touches is a corollary of 255.
- Outside Lie groups, the known targets use C1 only for a minor consistency step.
- The real tests are open problems O1, O2 and O3, of which O1 and O2 are statable in Lean now.

## Sources (snippet level, unverified unless local)
- arXiv 1002.4451 and 0802.2596 (Peng);
- math/0511647 and 0706.0940 (EFW);
- 2211.04093 / AGT 26:3 (Ferragut);
- 2509.12823 and 2410.05042 (Grayevsky–Pallier);
- 2510.24581 (Le Boudec);
- 2304.12498 (DFX);
- 0712.2214 (Dymarz);
- math/0601417 (BNW);
- NYJM 21 (2015) (Dymarz–Peng–Taback);
- the Cornulier Conj. 19.113 summary (emergentmind);
- local: labels.tex, introduction.tex, the 255 Lean tree, and `data/items/255_lean.json`.
