# Family 248: novelty analysis ("Thompson's group F is nonamenable")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`, which uses the 287 keys with `precedent_checks` as a list.

Inputs:
- `family.json`/`.md` from the paper and Lean analyst;
- the preprint source (`introduction.tex`, `finite-proof.tex`, `sources.bib`);
- spot checks of `lean/OAI/GroupTheory/Thompson/` (`partitionColor`, `exists_fixed_boundary`);
- a grep of every release preprint;
- web checks.

What was missing: no reasoning trace exists for 248, and no `f1_*` file was present when this was written.

**L** = Mathlib d13f23b plus 248's `sources.bib`. That file has 19 @-entries; family.json says 17. L includes Benyamini–Sternfeld 1983 and Moore 2013. **L⁻** drops Benyamini–Sternfeld and the two OpenAI companion preprints. It is used for Test 4.

## 1. Provenance verdict (first)

**Flag: PARTIAL, corollaries only. The main theorem has no model-produced precedent.**

- **Main theorem.** The core machinery cites only human work: Følner, Benyamini–Sternfeld (B–S), Cannon–Floyd–Parry and Moore. No AI-assisted or model-produced prior work on F's amenability turned up in searches pairing the problem with "ChatGPT", "GPT-5", "OpenAI" or "AI-assisted".
  - What the web shows is post-release coverage only:
    - Kalai's blog (10-07);
    - proofsandprompts (10-08), where Xiaolei Wu says earlier ChatGPT attempts failed;
    - vibemathed ("Candidate (review pending)");
    - kingy.ai and X posts.
  - No independent expert confirmation or refutation was found.
- **2025–2026 human citations.** Guba 2025 (arXiv:2210.12304, v1 2022) and Guba 2026 (arXiv:2304.04322, v1 2023) disclose no AI use. Both are background only, and neither contains any candidate item.
- **2025–2026 model-produced citations.** These are OpenAIUnitarizability2026 (family 251) and OpenAIPercolation2026 (family 214). Both are same-release, model-produced preprints, and both are used **only for the corollaries**.
  - A grep of the whole release finds no other preprint citing Sternfeld or using a recursive coloring.
  - So, unlike 287/Shlyakhtenko, there is **no same-vendor architectural precedent**.
- **Other 2026 preprints that surfaced** (Prellberg 2609.12290, on Cayley-graph density; Mandal 2609.25931, on Lipschitz group actions) disclose no AI use and are irrelevant to the candidates.

### History of claimed proofs (all checked on arXiv abstract pages)
| Claim | Direction | Method | Status | Candidate items present? |
|---|---|---|---|---|
| Akhmedov arXiv:0902.3849 (2009–13) | nonamenable | metric criteria | withdrawn (v3, v8) | absent |
| Shavgulidze arXiv:0906.0107 (2009) | amenable | averaging functional on Diff[0,1] | errors per Moore arXiv:1102.0747 ("do not seem to be repairable") | absent |
| Beklaryan arXiv:1112.1942 (2011–12) | nonamenable | projectively invariant measures | withdrawn, "crucial error in Theorem B*" | absent (not in 248's history paragraph) |
| Moore arXiv:1209.2063 (2012) | amenable | nonassociative Ramsey theory | withdrawn after Akhmedov found an error in Lemma 4.13 | scalar tree colorings only |
| Akhmedov arXiv:1310.4395 (v1 2013, v2 withdrawn, v3 2021) | nonamenable | height function, recursively built generalized binary trees | not accepted (Guba 2023 survey: open) | recursion present but scalar and combinatorial |
| Wajnryb–Witowicz arXiv:1408.2188 (2014–15) | nonamenable | not stated | withdrawn, "mistake which we cannot correct" | absent (not in 248's history paragraph) |

None of these uses a vector-valued invariant, a nonlinear self-map, or a fixed-point-free map.

## 2. Candidates and final grades

| # | Item | Nearest neighbours (verdict) | T2 | T3 | Final | F | conf |
|---|---|---|---|---|---|---|---|
| C1 | **Recursive Hilbert-ball coloring** p(T)=f(mean_j p(T_{I_j})) (I19, I23, I30) | Moore 2013 Thm 3.1, tree-coloring criterion (close *framework*, object absent); Moore Følner 2013 (scalar ∂ recursion, different); Akhmedov GBTs (different); Day/Lau/Gheysens–Monod/Schneider–Thom (affine or nonexpansive *actions*, different); Bartholdi–Kaimanovich–Nekrashevych self-similar fixed points (amenability direction, different); Aldous–Bandyopadhyay RDEs (form analogue only). **No near-equivalent found** | pass | pass (knockout) | **N3 (provisional; T4 pending)** | **F1** | 0.50 |
| C2 | Pair-exchangeability ⇒ concentration ⇒ approximate fixed point (I28, I31–I34; Lean `exists_fixed_boundary`) | finite de Finetti / Hilbert averaging (close variant) | fail (weak) | pass | **N2** | – | 0.70 |
| C3 | S fixed before A, one level after A, exact covariance (I25, I16) | Følner quantifier order; CFP tree pairs (equivalent) | fail | pass | **N1** (lowered from N2) | – | 0.75 |
| C4 | Nested pairs are a 1/D fraction (I33) | standard diagonal absorption | fail | pass | **N1** (lowered from N2) | – | 0.70 |
| C5 | Explicit B–S map on L²([0,1];ℝ²), δ=1/2 (I05, I38–I44) | B–S 1983 (equivalent); Kakutani, Lin–Sternfeld | fail | pass (replaceable by citation) | **N0** (transfer) | – | 0.90 |
| C6 | Lean-only Følner re-proof (Day + Namioka) | classical | fail | Lean only | **N0** | – | 0.95 |

**Test 3 note.**
- Lean's 20% DAG proxy fails here. `partitionColor` has about 0.05 dependents, because the B–S appendix (34%) and the dyadic plumbing (30%) do not depend on it.
- Load-bearing is therefore judged by knockout. Every step from the correlation comparison to the variance bound is about X_I = p(restriction), and the hinge X_{I_i} = f(z_i) is one unfolding of the recursion.

**Why C1 survives.**
- It occurs nowhere in the goal or in L. L contains each ingredient (tree restriction, the B–S map, Moore's scalar tree colorings, Følner) but not their composition.
- Its role is a *new bridge*. The classical fixed-point characterizations say that amenability gives fixed points for **affine or nonexpansive actions**. Here f is a single non-affine map with L>1 that is not an action at all. The recursion over F's self-similarity carries approximate invariance onto f.
- No use of Benyamini–Sternfeld, Kakutani or Lin–Sternfeld maps anywhere in amenability or group theory was found.

**Main risk to C1's N3.**
- Once the strategy is fixed ("approximate invariance ⇒ approximate fixed point of a map with none"), the recursion is close to forced. The same f must act at every scale so that parent and child pair-correlations share one value α.
- So the pivot distance is about 2 from L, and about 1 given the strategy sentence.
- A strategy-hidden hit rate above threshold would downgrade C1 to N2. So would an expert naming folklore for "self-similar recursion + no approximate fixed point ⇒ nonamenable".

**Compression.** The proof uses p only through one unfolding, so there is no PHP-style term blow-up. The Cook–Reckhow profile shows up in *search cost*: 47 years and at least six failed claims, against a roughly two-page core. A "confirmed eureka" verdict would need PLAN step 9, for example transfer of the C1 template to Lodha–Moore, Monod's H(A), or F_n Følner bounds.

## 3. Discoverability protocols (Test 4, not run)

The full specification is in `novelty.json → discoverability_protocols`.

**Model eligibility.**
- Training cutoff must be before **2026-09-23**.
- Each model must pass a canary probe: it says F's amenability is open, and it does not know the release.
- No tools are allowed.
- Excluded models: the unreleased OpenAI model, and any model trained on the openai/math repo, its Lean or its docs, vibemathed, Kalai 10-07, proofsandprompts 10-08, kingy.ai or the X posts.

**Arms for P-C1, the decisive protocol.**
- **Hide:** I19, I20, I23, I24, I28–I34, the proof of I27, I35, the intro's "Proof strategy" paragraph, and the corresponding Lean files.
- **Arm A** (pivot level, high hit rate expected): directed prompt plus L (B–S given).
- **Arm B** (decisive): open prompt plus L⁻.
- **Arm C** (measures leakage through the bibliography): open prompt plus L.

**Hit criterion.** A function of dyadic partitions or trees into a bounded convex set of an infinite-dimensional space, defined self-consistently across scales by a map with no approximate fixed point applied to averages of sub-restrictions, and paired with transport-invariant pair statistics.
- Partial credit, recorded but not counted: a recursive scalar coloring, or a vector-valued but non-recursive coloring.

**Sampling.** n = 256 per arm, reported as pass@k for k = 1…256.

**Controls.**
- Positive: Cook–Reckhow.
- Negative: C3, C4 and C6.

**P-C2.** C1 is given; pivot distance 1, chain depth 2.

## 4. Family verdict

**Axis D: D3 (provisional), confidence 0.45.**
- It rests on **C1** alone, with C2 as its payoff.
- It falls to **D2** if P-C1's arm B or C exceeds the threshold, or if an expert identifies a prior recursive or vector-valued nonlinear-map argument for nonamenability.
- The label is **void** if the proof fails. The proof is unrefereed, the Lean was not built, nanoda is off, and no external confirmation exists as of 2026-10-09.
- My own re-check of the core chain found no gap. The steps checked were: covariance, the translation inequality, the recursive identity, the three energy bounds, the cancellation of α (giving 4/D + 4(1−1/D)η), and the Jensen/Lipschitz step.

**Provenance flag: PARTIAL.** It applies to the corollaries only (model-produced companions 251 and 214). The main theorem has no model-produced precedent.

**Bridge novelty.**

| Import | Classification | Evidence |
|---|---|---|
| Nonlinear functional analysis → amenability (B–S map refutes amenability) | **New bridge**: the first connection found | Fixed-point/amenability links in the literature are all for affine or nonexpansive actions. No group-theoretic use of B–S was found |
| Moore's tree-coloring reformulation | **Known route** | Moore 2013 Thm 3.1 already makes "find a bad tree coloring" equivalent to nonamenability. 248's object is new; the route is not |
| CFP dyadic / tree-pair formalism, Følner | Known route | Used by every prior attempt |
| Exchangeability / L² averaging | Known route | C2 |

## 5. Open questions
1. Build the Lean (comparator plus nanoda) and get an expert reading.
2. Ask experts (Moore, Guba, Monod, Nekrashevych, Juschenko) whether "self-similar recursion ⇒ approximate fixed points" is folklore.
3. Proves-too-much at scale: lamplighter, Grigorchuk, Basilica, and IMG groups.
4. Downstream speedup on F-like groups.
5. Run zbMATH/MathSciNet citation searches on Benyamini–Sternfeld 1983 in MSC 20/43.
6. Merge with `f1_recursive_coloring.*` when it lands.

**Quote caveat.** Arxiv and blog quotes came through WebFetch's summarizer and are unverified. Moore 2013 was read from the PDF text.
