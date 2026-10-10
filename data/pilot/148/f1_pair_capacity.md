# F1 downstream-use report: pair capacity c_ℓ(ν) (family 148, item P14)

The structured version of this report is `f1_pair_capacity.json`.

**Bottom line.**
- **The definition.** The pair capacity is a clean, well-chosen interface, but it is **not a new object**. Varjú (JAMS 2019) takes, in the proof of his Prop. 21, a decomposition that maximizes the total mass of fair two-point submeasures at distances in [r/2, 2r]. That maximum is exactly the pair capacity for that single band. Read as an LP, it is a fractional b-matching or partial-self-coupling value. The analyst's grade **N2** stands, and N1 is arguable. There is no case for F1/N3.
- **The pair bound P15.** The separation-free pair bound is the real novelty. Kittle–Kogler (arXiv:2610.10511, posted 7 Oct 2026) reused its mechanism within a day, crediting a proof found by GPT-6 Astra. They **replaced c_ℓ by a linear multiscale variance energy** and got a better constant.
- **Downstream targets.** The plausible targets are all extensions within the same field: contracting-on-average measures, countable IFS, random IFS, commuting ℝ^d, and analytic IFS. None is a cross-field application.

## 1. The item

**Definition** (pairs.tex:13–27). Let ν be a finitely supported law on ℝ with support F.
- E_ℓ(F) is the set of unordered pairs {x, y} with 2^{-ℓ} ≤ |x−y| < 2^{1−ℓ}.
- c_ℓ(ν) is the maximum of Σ_e w_e subject to w_e ≥ 0 and ½ Σ_{e∋x} w_e ≤ ν({x}) for every x in F.
- In words, c_ℓ(ν) is the largest mass of fair two-point laws in band ℓ whose sum is a submeasure of ν. It lies in [0, 1], and the maximum is attained.

**Equivalent forms.** The first is in the source; the second and third are my own elementary derivations.
1. The fractional b-matching number of the distance-band graph, with b = 2ν.
2. The maximal mass of a sub-coupling π ≤ (ν, ν) supported on band pairs. This is how the proof feeds the capacity (pairs.tex:182–204; Lean `coupling_band_le_capacity`).
3. By max-flow min-cut on the bipartite double cover: c_ℓ(ν) = 1 − max_A [ν(A) − ν(N_ℓ(A))]. This is a defect-Hall / Strassen-type quantity.

**Role in the proof.** c_ℓ has two sides.
- **Deposit side.** The finite-law pair bound (Lemma 3.2) is k(H(ν) − H⁰_ρ(ν)) ≤ log|kF| + C_k Σ_{2^{-ℓ} ≤ 2ρ} c_ℓ(ν). Its random nested partitions produce symmetric in-cell couplings π_h, and these lower-bound c_ℓ band by band.
- **Withdrawal side.** In the conditional pair gain (windows.tex), an optimal packing attaining c_ℓ is fed, pair by pair, to the two-point gain lemma. This gives E[g_j − g_{j+n}] ≥ (δ/2)·c_{L−⌈σ_j⌉}.

**Obstruction dissolved.**
- With no separation, the entropy that ν hides below scale ρ may sit at arbitrarily fine scales. Baker and Bárány–Käenmäki give examples of super-exponential condensation.
- Hochman's argument needs that information to be visible in a bounded window of scales. Varjú's Prop. 21 converts entropy into pair mass only at a single scale, under a doubling hypothesis.
- What is needed is a currency with three properties:
  - it absorbs information from all finer scales without knowing where it sits;
  - it can be redeemed at each scale with a payoff that does not depend on the scale;
  - it is bounded in each band.
- c_ℓ meets all three because it is a maximum (any certificate lower-bounds it), it is attained (it can be cashed out pair by pair), and it is ≤ 1 in each band.
- **Caveat.** The non-obvious work is in P15/P17, not in the definition. Revealing the k-fold sum makes the per-level cost linear, so it sums geometrically over levels.

**Abstract mechanism (field-independent).**
- Quantify an obstruction by a scale-stratified packing LP: the maximum mass that can be packed into balanced two-element witnesses whose separation lies in a given dyadic band.
- Because it is a maximum, any coupling or averaging certificate lower-bounds it, band by band.
- Because it is attained, it can be redeemed witness by witness through a local gain lemma whose payoff does not depend on the band.
- Summing over bands turns information hidden at unknown, arbitrarily fine scales into a scale-free budget, which is then played against a bounded telescoping monovariant.

## 2. Candidate downstream problems

| # | Problem | Status | Match / adaptation | Payoff | Conf. | Diff. |
|---|---|---|---|---|---|---|
| C1 | Contracting-on-average self-similar measures on ℝ, no separation (Kittle–Kogler arXiv:2501.17795) | Proved only under weak all-scales separation | 1-D with commuting slopes, so types still fix the slope. Use stopping-time blocks; the pair bound applies verbatim | New theorem | med | med-high |
| C2 | ℝ^d with commuting linear parts: separation-free Hochman trichotomy (arXiv:1503.09043) | Open. KK 2610.10511 *claim* an extension for virtually solvable rotation groups | Capacities over annulus bands × direction sectors. Directional nonsaturation is the new issue | Independent proof | med (commuting) / low | high |
| C3 | Random / non-autonomous self-similar measures (GSSY; SSS arXiv:1709.05092) | Open without transversality or separation | Types machinery is native here. Jensen over the future environment | New quenched formulas | med | med |
| C4 | Real-analytic self-conformal IFS on ℝ (Rapaport arXiv:2412.16753; Käenmäki arXiv:2609.23743) | Open without ESC | Pair bound OK. P22 fails: derivative types do not identify maps up to translation | Partial | low-med | high |
| C5 | Projections of ergodic (Markov/Gibbs) measures (Jordan–Rapaport arXiv:1908.00271) | Open without ESC | Markov types replace Bernoulli types | New theorem (Markov case) | low-med | med-high |
| C6 | Furstenberg measures on SL₂(ℝ) (Hochman–Solomyak) | Open without ESC | Non-abelian, so type conditioning fails. KK name this obstruction too | — | low | very high |
| C7 | Planar self-affine measures (Hochman–Rapaport) | Open without ESC | Same non-commutativity problem | Partial | low | very high |
| C8 | L^q dimensions without separation (Shmerkin) | Open | The pair bound needs the Shannon chain rule, which has no Rényi analogue | — | low | very high |
| C9 | Countably infinite IFS on ℝ | Open | Truncate to finite laws; choose k after truncation | New theorem (routine) | med | med |
| C10 | DoF of interference channels (Stotz–Bölcskei arXiv:1404.7374) | Uses Hochman's theorem with an exceptional-parameter selection | Only indirect, through the main theorem | Simplifies | med / low for c_ℓ | low |
| C11 | Entropy loss under addition (KK Thm 1.3; Tao 2010) | **Done post-release by KK with variance energy** | The pair bound itself | Shows c_ℓ is replaceable | high / low value | low-med |
| C12 | Varjú survey Q8, Q9, Q11 (computing h_RW) | Open | **No match**: these are number theory of coincidences | none | — | — |
| C13 | Absolute continuity (Varjú, Kittle) | Open | **No match**: the c_ℓ argument is ineffective because B_n is uncontrolled | none | — | — |

## 3. Reuse within the release

- **None.** Only family 148 uses fair pairs or pair capacity. I grepped every preprint .tex for this.
- **Family 153** (Bernoulli convolution arithmetic classification) uses a different device: a common submeasure ξ ≤ μ₀, μ₁, plus single-scale counts of word pairs (classification.tex:223–300). c_ℓ would not help there.

## 4. Speedup targets (known theorems)

1. **Hochman 2014, Thm 1.3** (Annals, about 50 pp, with the inverse theorem about 20–25 pp). It is a corollary of 148, which takes about 15 pp. The Lean core that replaces the inverse theorem is about 1,580 lines (FairPairs, SumsetBound, GridCoupling, RandomGrid, FiniteRefinement).
2. **Varjú 2019** (Annals): dimension 1 for transcendental λ. Immediate from h_RW = log 2.
3. **Rapaport 2022** (ASENS, about 35 pp): algebraic contraction ratios. This is Cor 6.2.
4. **Rapaport–Varjú 2024** (Duke, about 60–70 pp): the three-map family. This is Cor 6.5, already formalized as `homogeneous_dimension_direct`.
5. **Feng–Feng 2025** (JLMS): algebraic translations.
6. **Varjú 2019 JAMS Prop 21** (about 5 pp). Its extremal decomposition *is* a pair capacity. This is the best Mathlib-scale test, but the saving is modest.
7. **Kittle–Kogler 2025 Thm 1.3, restricted to d = 1.**

Caveat for all of these: the savings come from the whole 148 pipeline. c_ℓ on its own buys almost nothing that can be measured separately.

## 5. Contamination and precedent

**Before the release.**
- Varjú, JAMS 2019 (arXiv:1602.00261), §4.2.3: "∥ν∥ is minimal among all such decompositions" into Bernoulli (equal-weight two-point) measures at distances in [r/2, 2r]. 1 − min∥ν∥ is the pair capacity for that ratio-4 band.
- Varjú then gets a gain from each pair over many scale ranges (Prop 20 / Lemma 22, §4.3). This is the same deposit/withdraw pattern, at single scales and under hypotheses.
- He also mentions an unpublished Lindenstrauss–Varjú variant.
- The LP and coupling forms of c_ℓ are classical combinatorial optimization.
- Kittle (2021) and Kittle–Kogler (2025) use linear scale-local currencies: detail, variance, and trace at scale r.

**After the release.**
- Kittle–Kogler, arXiv:2610.10511, was posted 7 Oct 2026. They state that GPT-6 Astra found their first proof, on 27 Sept 2026.
- They cite 148 as independent concurrent work. They call their Thm 1.3 "a quantitative version of Lemma 3.2" of 148, with C_m = 120m² instead of O(m³).
- Their currency is the **variance energy** ℰ(ρ) = ∫ V_ρ(r) dr/r. They use no fair pairs.
- So the *mechanism* transferred immediately and was independently discoverable by another model, while the *definition* did not survive.

**Verdict.** P14 is N2, bordering N1. It is not a confirmed eureka step, and the downstream evidence points to the pair *bound*, not the capacity.

## 6. Top 5 ranked

1. **C1, contracting on average.**
   - It is the closest structural match: 1-D, commuting slopes, and the pair bound applies verbatim.
   - The literature currently needs weak separation, so this would be a new theorem.
   - However, KK's variance energy is a ready-made competitor.
2. **C9, countable IFS.**
   - Truncation keeps the laws finite, so the transfer is likely routine.
   - That makes it a good low-cost test of transfer, but weak evidence of eureka value.
3. **C3, random / non-autonomous IFS.**
   - The GSSY types machinery is native to this setting; only the Jensen step changes.
   - The payoff would be quenched formulas.
4. **C2, ℝ^d with commuting linear parts.**
   - Capacities over direction sectors handle the pair-bound side; directional nonsaturation yields the saturation alternative.
   - KK claim the virtually solvable case, so this would likely be an independent proof rather than a first resolution.
5. **C4, analytic self-conformal IFS on ℝ.**
   - The pair bound transfers.
   - The step "types identify the map" (P22) fails, so c_ℓ would carry only half the argument.

## 7. Lean source (verbatim)

Source directory: `data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/`.
- There are no docstrings.
- Theorem statements are shown without proofs, cut at `:= by`.

### OAI.EntropyRateDimension.FairPairs.Law (structure)
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/FairPairs.lean:14`

```lean
structure Law where
  support : Finset ℝ
  prob : ℝ → ℝ
  prob_pos : ∀ x ∈ support, 0 < prob x
  prob_sum : ∑ x ∈ support, prob x = 1
```

### OAI.EntropyRateDimension.FairPairs.Law.edges (def)
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/FairPairs.lean:20`

```lean
noncomputable def Law.edges (ν : Law) (ℓ : ℤ) : Finset (ℝ × ℝ) := by
  classical
  exact (ν.support ×ˢ ν.support).filter fun e =>
    e.1 < e.2 ∧ (2 : ℝ) ^ (-ℓ) ≤ e.2 - e.1 ∧ e.2 - e.1 < (2 : ℝ) ^ (1 - ℓ)
```

### OAI.EntropyRateDimension.FairPairs.incident (def)
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/FairPairs.lean:25`

```lean
noncomputable def incident {ν : Law} {ℓ : ℤ} (w : ν.edges ℓ → ℝ) (x : ℝ) : ℝ := by
  classical
  exact ∑ e, ((if e.val.1 = x then w e / 2 else 0) +
      (if e.val.2 = x then w e / 2 else 0))
```

### OAI.EntropyRateDimension.FairPairs.Feasible (def)
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/FairPairs.lean:30`

```lean
def Feasible {ν : Law} {ℓ : ℤ} (w : ν.edges ℓ → ℝ) : Prop :=
  (∀ e, 0 ≤ w e) ∧ ∀ x ∈ ν.support, incident w x ≤ ν.prob x
```

### OAI.EntropyRateDimension.FairPairs.capacity (def)
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/FairPairs.lean:33`

```lean
noncomputable def capacity (ν : Law) (ℓ : ℤ) : ℝ :=
  sSup {t : ℝ | ∃ w : ν.edges ℓ → ℝ, Feasible w ∧ ∑ e, w e = t}
```

### OAI.EntropyRateDimension.FairPairs.capacity_le_one (theorem (statement only))
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/FairPairs.lean:88`

```lean
theorem capacity_le_one (ν : Law) (ℓ : ℤ) : capacity ν ℓ ≤ 1
```

### OAI.EntropyRateDimension.FairPairs.capacity_attained (theorem (statement only))
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/FairPairs.lean:131`

```lean
theorem capacity_attained (ν : Law) (ℓ : ℤ) :
    ∃ w : ν.edges ℓ → ℝ, Feasible w ∧ ∑ e, w e = capacity ν ℓ
```

### OAI.EntropyRateDimension.FairPairs.coupling_band_le_capacity (theorem (statement only))
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/FairPairs.lean:189`

```lean
theorem coupling_band_le_capacity {ν : Law} (ℓ : ℤ) (π : ℝ → ℝ → ℝ)
    (hπ : ∀ x ∈ ν.support, ∀ y ∈ ν.support, 0 ≤ π x y)
    (hsym : ∀ x ∈ ν.support, ∀ y ∈ ν.support, π x y = π y x)
    (hrow : ∀ x ∈ ν.support, ∑ y ∈ ν.support, π x y ≤ ν.prob x) :
    (∑ x ∈ ν.support, ∑ y ∈ ν.support,
      if (2 : ℝ) ^ (-ℓ) ≤ |y - x| ∧ |y - x| < (2 : ℝ) ^ (1 - ℓ)
      then π x y else 0) ≤ capacity ν ℓ
```

### OAI.EntropyRateDimension.FairPairs.Law.bandCost (def)
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/SumsetBound.lean:19`

```lean
noncomputable def Law.bandCost (ν : Law) (R : ℝ) : ℝ := by
  classical
  exact ∑ ℓ ∈ ν.bandSupport.filter (fun ℓ => (2 : ℝ)^(-ℓ) ≤ R),
    (2 : ℝ)^(1-ℓ)*capacity ν ℓ
```

### OAI.EntropyRateDimension.FairPairs.pair_bound (theorem (statement only))
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/SumsetBound.lean:329`

```lean
theorem pair_bound (ν : Law) (k : ℕ) (hk : 1 ≤ k) (ρ : ℝ) (hρ : 0 < ρ) :
    k*(ν.shannonEntropy-ν.gridEntropy ρ) ≤ Real.log (ν.sumset k).card / Real.log 2 +
      60000*k^4 * ∑ ℓ ∈ ν.bandSupport.filter (fun ℓ => (2 : ℝ)^(-ℓ) ≤ 2*ρ), capacity ν ℓ
```

### OAI.EntropyRateDimension.MeasureEntropy.finiteConv_mean_gain (theorem (statement only))
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/PairGain.lean:258`

```lean
theorem finiteConv_mean_gain {β : Type uβ} [Fintype β]
    (ν : FairPairs.Law) (a b : ℝ) (hb : b ≠ 0)
    (μ : Measure ℝ) [IsProbabilityMeasure μ] (hμ : CompactlyCarried μ)
    (τ : β → Measure ℝ) [∀ z, IsProbabilityMeasure (τ z)]
    (hτ : ∀ z, CompactlyCarried (τ z))
    (p : β → ℝ) (hp : ∀ z, 0 ≤ p z) (hp1 : ∑ z, p z=1)
    (hm : μ.map (fun x => b*x) = ∑ z, ENNReal.ofReal (p z) • τ z)
    {δ η s : ℝ} (hδ : ∀ v, 0 < v → δ ≤ deficit μ v) (hs : 0 < s)
    {N : ℕ} (hN : 0 < N) (ℓ : ℤ)
    (hv : ∀ e : ν.edges ℓ, s < |a*e.val.2-a*e.val.1| ∧ |a*e.val.2-a*e.val.1| < N*s)
    (herr : ∀ e : ν.edges ℓ,
      (s/|a*e.val.2-a*e.val.1|+|a*e.val.2-a*e.val.1|/(N*s))*Real.log 2 ≤ η) :
    (δ-η)*FairPairs.capacity ν ℓ ≤
      ∑ z, p z*(window (finiteConv ν a (τ z)) s (N*s)-window (τ z) s (N*s))
```

### OAI.EntropyRateDimension.Typed.conditional_gain (theorem (statement only))
`data/raw/openai-math/lean/OAI/MeasureTheory/SelfSimilar/ScaleGain.lean:82`

```lean
theorem conditional_gain (S : System α) (tag : α → β)
    (hr : ∀ a v, tag a=tag v → S.ratio a=S.ratio v)
    (μ : Measure ℝ) [IsProbabilityMeasure μ] (hμ : S.SelfSimilar μ)
    (hc : CompactlyCarried μ) {δ : ℝ}
    (hδ : ∀ v, 0 < v → δ ≤ deficit μ v) {M : ℕ} (hM : 4 < M)
    (he : 5/(M : ℝ)*Real.log 2 ≤ δ/2)
    {j n : ℕ} (u : Fin j → α) (w : Fin n → α) (t : ℕ) (L : ℤ) :
    δ/2*capacity (law S tag w) (L-⌈S.wordDepth u⌉) ≤
      ∑ z : Fin t → α, S.wordWeight z*
        (window (scaledTail S tag μ (S.completeMap u).1 (Fin.append w z))
          ((2 : ℝ)^(-L)/M) (((M*M : ℕ) : ℝ)*((2 : ℝ)^(-L)/M))-
        window (scaledTail S tag μ ((S.completeMap u).1*(S.completeMap w).1) z)
          ((2 : ℝ)^(-L)/M) (((M*M : ℕ) : ℝ)*((2 : ℝ)^(-L)/M)))
```

## 8. Sources and search log
The full lists are in the `sources` and `search_log` fields of `f1_pair_capacity.json`.

Key sources:
- arXiv:1602.00261 (Varjú, JAMS 2019)
- arXiv:2610.10511 (Kittle–Kogler, 7 Oct 2026)
- arXiv:2501.17795 (Kittle–Kogler, contracting on average)
- arXiv:2509.22042 (Varjú survey)
- arXiv:1503.09043, 1610.02641, 1904.09812, 1908.00271, 2412.16753, 2609.23743, 1609.07802 and 1404.7374
