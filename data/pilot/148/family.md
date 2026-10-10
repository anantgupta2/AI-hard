# Family 148: The entropy-rate dimension formula for self-similar measures

- Manuscript: *The entropy-rate dimension formula for self-similar measures on the line* (OpenAI, Sept 24 2026), `preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/build/` (main.tex plus 6 sections, about 1,500 lines).
- Lean: `lean/OAI/MeasureTheory/SelfSimilar` (64 files, 12,093 lines, 890 declarations). There are 3 comparator targets across 2 challenge files.
- No reasoning trace. Not withdrawn or revised.
- L = Mathlib d13f23b plus the 23-entry bibliography.
- Structured data: `family.json` (37 items).

## 1. Main statement

**Verbatim** (introduction.tex:78-88):

> For every finite nonempty indexed family φ_i(x)=r_i x+t_i on ℝ with 0<|r_i|<1, and every strictly positive probability vector p, its self-similar measure satisfies dim_H μ_{Φ,p} = min{1, h_RW(Φ,p)/χ(Φ,p)}. No separation assumption is required; exact overlaps and repeated generators are allowed.

**Definitions used in the statement:**
- h_RW = lim H(G_n)/n = inf H(G_n)/n, where G_n is the *complete composed affine map* of n iid symbols. Coinciding maps are merged.
- χ = −Σ p_i log|r_i|.
- dim_H is the lower Hausdorff dimension of the measure.

**Paraphrase.** Dimension drops below the trivial bound exactly by the information lost to exact coincidences of composed maps.

**Status of the problem.** This is Conjecture 3 of Varjú's survey (arXiv 2509.22042v2). I extracted the survey's text: it calls the conjecture "folklore" and "wide open". Its no-exact-overlap case is the **exact overlaps conjecture** (Simon; Hochman).

Corollaries:
- **Cor 6.2:** the measure version, dim μ = min{1, H(p)/χ}.
- **Cor 6.3:** the set version, dim K = min{1, s_*}.
- **Cor 6.5:** the Rapaport–Varjú three-map family {λx, λx+1, λx+t}, for all parameters.

**Relative to known results.** The theorem subsumes all of the following:
- Hochman 2014: the formula under exponential separation.
- Rapaport 2022: algebraic contraction ratios.
- Breuillard–Varjú and Varjú 2019: all Bernoulli convolutions.
- Rapaport–Varjú 2024 Thm A.1: rational translations.
- Feng–Feng 2025: algebraic translations.

Notably, it **does not use Hochman's inverse theorem**. The only external dimension theorem the paper uses is Feng–Hu exact dimensionality. A quick web search found no other claimed resolution.

### Lean comparator statements and match check

| Target | File | Matches |
|---|---|---|
| `OAI.EntropyRateDimension.entropy_rate_dimension` | Main.lean:59 | Thm 1.1, exactly |
| `…Extensions.homogeneous_dimension_direct` | HomogeneousDimension.lean:97 | Cor 6.4, hence 6.5 |
| `OAI.CorSetReference.cor_set` | AttractorFormula.lean:32 | Cor 6.3 |

The comparator for the main theorem reads `lowerHausdorffDimension μ = ENNReal.ofReal (min 1 (S.entropyRate / S.lyapunov))`. It holds for every probability μ satisfying `μ = Σ p_i • μ.map (affine i)`.

Checks on the main comparator:
- `wordAffine (i::w)` = φ_i∘φ_w gives the full signed affine map.
- `entropyRate` is the infimum over n≥1 of the base-2 map entropy divided by n. The paper proves that this infimum equals the limit.
- `lowerHausdorffDimension` is the infimum of Mathlib's `dimH` over measurable sets of positive mass.
- Uniqueness of the invariant measure is proved in Lean (`selfSimilar_unique`). Quantifying over all solutions is therefore not a weakening.

Checks on the corollaries:
- `NoExactOverlaps` is injectivity of `wordAffine` on all lists, and `cor_set` compares nonempty words of any lengths. Both are equivalent to the paper's same-length convention by Lemma 6.1.

Further facts about the formalization:
- The challenge definitions are character-identical to Model.lean.
- No extra hypotheses are added.
- Cor 6.2 and Lemma 6.1 are formalized in the library but not compared.

**Verdict: faithful. The whole paper is formalized.** The Lean even re-proves the cited Feng–Hu theorem, in about 1,700 lines:
- Hopf maximal inequality, then the Birkhoff and Maker triangular ergodic averages;
- a maximal ball-ratio bound with an integrable log envelope;
- the information rate `infoRate`.

Route differences between the Lean and the paper:
- The pair bound uses shifted 4-adic grids on `AddCircle`, an existence-of-good-shift averaging, and induction on depth. The paper perturbs the cuts independently instead. The constant 60000k⁴ is kept.
- Block types are generalized to any slope-fixing `tag`.
- The window count uses a common horizon H divisible by all n_i.
- The homogeneous corollary has its own direct branch with the trivial tag.

## 2. Trust surface

I grepped all 64 files:
- **Zero** occurrences of `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `set_option` and `#eval`.
- The 3 uses of `decide` are Bool coercions in definitions.
- There are 2 explicit uses of `Classical.choice`, and 23 `local instance : MeasurableSpace ι := ⊤`.
- The only import is `Mathlib`.

The comparators permit `propext`, `Quot.sound` and `Classical.choice`, with `enable_nanoda: false`.

**Caveat:** Lean is not installed, so compilation and the comparator pass were not re-run. **Not computer-assisted.**

## 3. Labels

| Axis | Label | Evidence | Conf. |
|---|---|---|---|
| A | **A3**, an exact formula. The hard direction, the lower bound, is proved as an impossibility (A5-like). No explicit rate. | introduction.tex:83-84 | med-high |
| B | **B1**. full_only_with_prior_results = **no**: only Feng–Hu is cited, and Lean re-proves it. adds_corollaries = **yes**: exact overlaps conjecture (measures and sets), the RV three-map problem, and re-derivations of the Bernoulli-convolution and algebraic cases. | introduction.tex:90-91, 181-182 | high (as a claim) |
| C | Primary **C3**: contradiction from d<1, dχ<h. Secondaries: **C4** (entropy-inequality chain, C_k=60000k⁴), **C1** (auxiliary gadgets: random partitions, separated bands), **C5** (Feng–Hu and SLLN only). ih_strengthened = **no**, template = none: the only iteration is the diagonal choice of n_1<…<n_q. computer_assisted = **no**. | introduction.tex:254-260; pairs.tex:223; windows.tex:131 | high |
| D | **D3, provisional.** The top items are P15 (pair bound with pair capacity) and P28 (scale-free band counting). Both are borderline N2: see the caveat below. | | low-med |
| E | See below. | | medium |

**D caveat.** The paper names Varjú 2019 Prop. 21 as a "predecessor" of the pair-capacity approach. A strict reading of the rule "precedents the paper names itself → N2" would cap the family at D2.

**D provenance.** The provenance flag is **no**. All 23 references are human-authored, and I verified that the two 2025/26 arXiv items exist (Varjú survey; Bárány–Verma).

**E fields:**
- **Problem field:** Dynamical systems and ergodic theory. MSC 28A80, 37C45, 28A78, 11K55.
- **Lean-dir field:** MeasureTheory.
- **Method fields, essential:**
  - information theory (94A17);
  - fractal geometry and GMT;
  - ergodic theory (Feng–Hu; Birkhoff re-proved in Lean);
  - probability (LLN, Jensen over the environment);
  - Varjú/BV entropy methods;
  - random-IFS type classes (GSSY);
  - additive combinatorics (k-fold sumset counting);
  - combinatorial optimization (the fractional-matching LP defining pair capacity);
  - differential entropy and smoothing.
- **Method fields, background-cited:**
  - Wang's translation averaging;
  - Hochman's inverse theorem (cited, **not used**);
  - Pisot and Garsia number theory.

## 4. Items

There are 37 items in total: 35 from the paper and 2 Lean-only. The table shows the items that matter. Full fields, including Lean declarations and file:line, are in the JSON.

| id | item | cited/new | N |
|---|---|---|---|
| P01-P05 | IFS and self-similar measure, exact overlap, h_RW, χ, lower dim_H | classical | N0 |
| P06 | Feng–Hu exact dimensionality (cited in the paper; **re-proved in Lean**) | cited | N0 |
| P08 | Upper bound, via a map-alphabet regrouping and a covering argument | re-proved | N0 |
| P09-P11 | Averaged entropy calH_s, G_{s,t}, Δ_s; entropy calculus; entropy ≤ d log(1/s) | Varjú 2019, re-proved | N0 |
| P12 | Uniform nonsaturation, inf_v Δ_v(μ)>0 when d<1, for unequal signed ratios | adapted from BV Lemma 13 | N2 |
| P13 | Two-point gain, ≥ Δ_v − s/v − v/t | Varjú Prop 20 / Lemma 22 | N1 |
| **P14** | **Pair capacity c_ℓ(ν)**, an LP max of fair-pair mass in a dyadic distance band | new; Varjú Prop 21 named as predecessor | N2 (F1 if raised) |
| **P15** | **Finite-law pair bound:** k(H(ν)−H⁰_ρ(ν)) ≤ log\|kF\| + C_k Σ_{ℓ: 2^{-ℓ}≤2ρ} c_ℓ, independent of separation | new | **N3 cand.** (F3) |
| P16 | Randomized nested partitions with perturbed cuts | standard device | N1 |
| **P17** | Refinement after observing the sum Y: the cost is linear in exceptional probabilities | new; core of P15 | with P15 |
| P19-P21 | Block types (GSSY), conditional laws ν_{ω,n}, parameters | cited / plumbing | N0-N1 |
| P22 | Entropy retained by types: E H(ν_{ω,n}) ≥ n h_b, giving a linear deficit at scale 2^{-An} | adaptation | N2 |
| P23 | Digit-count sumset bound, \|kD_b\| ≤ (k+1)^{m^b} | elementary | N1 |
| P24 | Expected pair mass ≥ cn in a finite band [a_n, B_n], with B_n unbounded | assembly | N2 |
| P25-P26 | Suffix laws τ_j; monotone window entropy g_j | routine | N1 |
| P27 | Conditional pair gain: Jensen over the unobserved future types | new | N2 |
| **P28-P29** | **Separated-band counting:** adaptive n_i, disjoint retained windows at each physical scale, q ≤ 8D log M/(δc) | new | **N3 cand.** (F4) |
| P31-P35 | Overlap lengths; corollaries (measure, set, homogeneous, three-map) | known / consequences | N0 / n/a |
| L01-L02 | Lean-only: in-house finite-entropy library; generic slope-fixing `tag` | infrastructure | N0-N1 |

**Load-bearing proxy.** For each lemma, the share of the 749-declaration main-theorem DAG that lies below it:
- `no_strict_entropy_gap`: 73%
- `count_pair_budget_le`: 46%
- `conditional_gain`: 37%
- uniform nonsaturation: 27%
- exact dimensionality: 24%
- `two_point_gain`: 22%
- `pair_bound`: 19% of declarations, 22% of tokens
- `select_separated_bands`: 3%

The extractor's dependents ranking puts infrastructure on top (`FiniteEntropy.mass` 0.37, `System` 0.34).

## 5. Invoked external theorems

| Theorem | Treatment | Essential? |
|---|---|---|
| Feng–Hu Thm 2.8 (exact dimensionality) | Cited in the paper, re-proved in Lean | Yes |
| Varjú 2019 Lemmas 5, 6, 10 | Re-proved | Yes |
| Varjú 2019 Prop 20 / Lemma 22 | Adapted | Yes |
| Breuillard–Varjú Lemma 13 | Adapted | Yes |
| GSSY Lemma 6.6 / SSS / Käenmäki–Orponen (block types) | Re-proved in the needed form | Yes |
| SLLN / LLN | Standard | Yes |
| Hutchinson (invariant measure) | Cited; Lean proves uniqueness | Yes |
| Hochman fn. 3 | Re-proved | No |
| Varjú Prop 21 | Named predecessor, not used | No |
| Hochman's inverse theorem; Baker / Bárány–Käenmäki; Wang | Background only | No |

## 6. Proof architecture

1. **Upper bound.** Regroup into n-blocks whose alphabet is the distinct maps, then cover. It remains to rule out d<1 with dχ<h.
2. **Entropy between scales.** Uniform nonsaturation δ>0 holds at *every* scale, via stopped self-similarity. Each fair pair at distance v gains Δ_v.
3. **Pair bound.** For any finite law, k × (exact minus scale-ρ entropy) is at most log|kF| + C_k × (fair-pair capacity at finer bands). The bound does not depend on the minimal gap. In the proof, revealing the k-fold sum makes the per-level cost linear in mean deviations, so the costs sum geometrically.
4. **Linear pair mass.** Block types fix the signed slopes, so conditional translation entropy equals map entropy, at least n(bh − m log(b+1)). Under dimension loss this exceeds the entropy at scale 2^{-An} by εn. Sumsets are polynomial in k, so P15 gives expected pair capacity ≥ cn in a finite but **uncontrolled** band [a_n, B_n].
5. **Gains.** Fair pairs from block window [j, j+n), rescaled to physical scale 2^{-L}, each gain at least δ/2 in g_j − g_{j+n}. This holds after averaging the future types: Jensen applies because Δ is convex.
6. **Contradiction.** Choose q bands adaptively, each n_i after the earlier B_{n_h} are known. At each physical scale the retained windows are disjoint, so their gains telescope to at most 2 log M. Each band contributes δcT/(4D), so q is bounded, a contradiction.
7. **Corollaries.**

## 7. Eureka candidates

**1. P15 pair bound, together with P14 pair capacity and P17. Provisional N3, borderline N2; F3, with P14 as F1.**
- *For:*
  - It is the separation-free bridge from hidden fine-scale entropy to fair pairs at arbitrarily fine bands. Baker and Bárány–Käenmäki showed that such a bridge is necessary, and Hochman's fixed-window inverse theorem cannot supply it.
  - Nothing equivalent appears in the goal, Mathlib or the bibliography.
  - The sum-observation trick is non-obvious.
  - Sub-DAG share is about 20%.
- *Against:*
  - The paper names Varjú's Prop. 21 fair-pair decomposition as a predecessor.
  - Entropy–sumset inequalities and random grids are classical.
- *Quick literature check:* no precedent found. The nearest neighbours are Varjú JAMS 2019 Props 20-21 and Hochman's inverse theorem.

**2. P28-P29 scale-free separated-band counting. Provisional N3, borderline N2; F4, with monotone g_j as the monovariant.**
- *For:* it removes the last need for effective bounds. Each band's contribution does not depend on n_i, and the budget at each scale is shared.
- *Against:* telescoping of multiscale entropy and diagonal parameter choice are standard. Its Lean footprint is small.
- *Quick literature check:* no precedent found.

**3. P22 map entropy retained by types. N2.** Neighbours: GSSY types, Hochman Thm 1.4, Rapaport–Varjú A.1, Bárány–Verma.

**4. P12 uniform nonsaturation for signed unequal ratios. N2.** Neighbour: BV Lemma 13.

**5. P27 Jensen over unobserved future types. N2.**

## 8. Correctness concerns

I read every section line by line and checked the constants:
- 9k·k·1120k² = 10080k⁴, then ×2 and ×8/3 give 53760k⁴ ≤ 60000k⁴.
- Child lengths stay in [0.55, 1.45]ρ_{h+1}.
- The TV bound e_v ≤ √(2 ln2 Δ_v).
- The window-disjointness monotonicity.
- The exactly-once correspondence of targets: ⌈σ_j⌉ ≤ T/2 and B < T/2.

**I found no gap.**

Consistency checks passed:
- The formula predicts the known Pisot/Garsia drops.
- The argument is 1-D specific: nonsaturation uses d<1, matching the irreducibility caveats in ℝ^d.
- It uses no separation, consistent with the super-exponential condensation examples.
- The q-fold accumulation is multiscale gain at a fixed physical scale (budget 2 log M), not double counting of per-block entropy.

**Main concern:** this is an extraordinary, unreviewed claim. It is a short (~15 pp) elementary proof of a conjecture the leading survey calls wide open. The decisive support is the Lean formalization, which is complete with no escape hatches but was not compiled here.

Minor points:
- The paper's Lemma 2.2 measurability construction and its use of Feng–Hu are sketched. The Lean covers both.
- The result is ineffective: no rates, and nothing about absolute continuity.

## 9. Extraction friction

- Most load-bearing objects are in display math or unnumbered paragraphs, not environments:
  - calH_s, G_{s,t}, Δ_s;
  - types, environment, ν_{ω,n};
  - τ_j, g_j and the retention events;
  - the sum-observation lemma P17;
  - the band selection and the final count.

  Only "exact overlap" is an `\emph` definition.
- The Lean namespaces (`EntropyRateDimension`, `Typed`, `FairPairs`, `CorSetReference`, `ErgodicAux`) do not encode the FID. The 3 targets sit in 2 challenge files, and `DimensionCorollaries.lean` only re-imports.
- For this family the extractor's dependents ranking is uninformative. Closure (sub-DAG) share works better for lemmas.
- "Cited in the paper" ≠ "assumed in Lean": Feng–Hu is fully re-proved. Field tagging must record both.
- The Lean route differs from the paper in the pair bound (shifted grids) and in the window count (common horizon). Name-based joins need statement matching.
