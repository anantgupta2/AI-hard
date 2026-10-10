# Family 148: novelty analysis ("The entropy-rate dimension formula for self-similar measures")

Analyst role: novelty. Date: 2026-10-09. The machine-readable version is `novelty.json`, which uses the 287 keys with `precedent_checks` as a list.

**Inputs.**
- `family.json`/`.md`. There is no reasoning trace for this family.
- `f1_pair_capacity.*`. These arrived during this analysis and are reconciled below.
- The preprint source and spot greps of `lean/OAI/MeasureTheory/SelfSimilar`.
- Full-text reads of Varjú JAMS 2019 and Varjú's survey. Both PDFs were saved by WebFetch and extracted locally, so their quotes are verbatim.
- Web checks, listed in `sources`.

**L** = Mathlib d13f23b plus 148's 23-entry bibliography. L **includes** Varjú 2019 and the Varjú survey. It does **not** include Kittle–Kogler 2025/2026 or Wu 2025.

## 1. Provenance verdict first

**Flag: NO.** 148 builds on no model-produced work, and there is no model-produced precedent. There **is** a posterior, parallel model-produced resolution that uses the same key mechanism.

**The 2025–26 items in the bibliography are all human**, with no AI disclosure on their arXiv abstract pages:
- **Varjú survey, 2509.22042.**
  - Versions: v1 26 Sep 2025; v2 22 Mar 2026, "minor revision based on referee's report", to appear in *Fractal Geometry and Stochastics 7*.
  - Its acknowledgements thank only Rapaport, Streck and the referee.
- **Bárány–Verma, 2507.05835.** v1 Jul 2025, v2 Jul 2026.
- **Feng–Feng, 2405.03124.** Posted 2024, published in JLMS 2025.

**The survey.**
- It states Conjecture 3 as a "folklore conjecture" that is "wide open".
- It contains **no strategy** for the conjecture, and none of pair capacity, the pair bound, block types or band counting.
- It cites Wu 2025 (arXiv:2503.21923), which 148 omits. Wu's is a transversality route, unrelated to the candidates.

**Parallel model-produced work (posterior).**
- Kittle–Kogler, *The Exact Overlaps Conjecture for Self-Similar Measures on the Real Line*, arXiv:2610.10511v1, posted 7 Oct 2026, one day after openai/math went public.
- **The machine contribution statement says:**
  - **GPT-6 Astra** found the first proof on **27 Sep 2026**, three days after 148's stated date of 24 Sep.
  - The model had first been asked, following a suggestion of Lindenstrauss, to simplify Hochman's and Varjú's proofs (about 2 h). It then proved the conjecture in about 2.5 h.
  - The supplementary repo states: "All documents written by GPT-6 Astra".
- **How it relates to 148:**
  - It cites 148 as "[20] OpenAIMath" and says a proof "was independently announced in [20] as paper number 148".
  - It calls its Theorem 1.3 a quantitative strengthening of **148's Lemma 3.2 (the pair bound)**. Theorem 1.3 states that the entropy lost under addition is at most C·m·Σ(variance energy).
  - Its mechanism is the same: random cuts revealed after observing the sum, with cost linear in E|X−X′|.
- Its quotes are summarizer-relayed and **unverified**, and its constants are relayed inconsistently.
- **Bearing:** it is not a precedent, so Test 1 is unaffected. It **is** strong external evidence on Test 4. Two model runs, three days apart, reached the same key inequality.

No ChatGPT-, GPT-5- or OpenAI-assisted work on this problem before 24 Sep 2026 was found.

## 2. Varjú Prop 21: what it actually says

I read the full text of arXiv:1602.00261v4, §4.

**Prop 21.**
- Hypothesis: µ is finitely supported, r > 0, and H(µ; r/2|r) ≤ 1.5·H(µ; r|2r).
- Conclusion: µ = ν + η₁ + … + η_N, where the η_i are Bernoulli (equal-weight two-point) measures at distances in [r/2, 2r], and Σ‖η_i‖ ≥ (1/128)·h/(log h⁻¹ + 1), with h = H(µ; r|2r).
- **Proof.** Take the decomposition with ‖ν‖ *minimal*, which is the same as maximal Bernoulli mass. The residual then has no pairs in the band, so Lemma 23 gives exact doubling. The Fano-type Lemma 26 costs 3‖η‖log‖η‖⁻¹, and **that is where the log loss comes from**.

**Lemma 27 and the proof of Thm 3.**
- Lemma 27 selects 2K-separated scales where Prop 21's hypothesis holds; between them, entropy decays geometrically.
- At each selected scale, Prop 20 gives a gain of α/3 per Bernoulli piece, and the gains are summed over the separated scales.

**Consequences for 148.**
- **P14, pair capacity, is Varjú's extremal quantity.** It is the maximal Bernoulli-decomposition mass, with one dyadic band where Varjú uses two.
- **P15, the pair bound, differs from Prop 21 in exactly one decisive respect.**
  - Analyst's sketch, unverified: Prop 21 plus Lemma 27 already give a single-copy (k = 1), separation-free bound with a **log loss**, ≲ Σ c_ℓ log(1/c_ℓ).
  - That loss is fatal when the band endpoints B_n are uncontrolled.
  - 148 removes it by observing the k-fold sum Y and paying log|kF|. The paper itself says this "is what makes [the bound] linear in the exceptional probabilities" (pairs.tex:158–160).
- **P28 (band counting) and P27 (conditional gain)** have Lemma 27 and Thm 3 as their in-L template.

## 3. Final grades

| # | Item | Nearest neighbour(s) | T2 | Final | F | conf |
|---|---|---|---|---|---|---|
| C1 | **Pair bound P15 + sum-observation refinement P17** (gadgets P16, P18) | Varjú Prop 21 + Lemma 27 (single-scale / log-lossy; close in role, different statement); Kittle–Kogler 2025 (single-scale, needs separation); KK 2026 Thm 1.3 (same mechanism, **posterior, model-produced**) | pass | **N3 (provisional; T4 pending, external evidence adverse)** | F3 | **0.30** |
| C2 | Pair capacity c_ℓ (P14) | Varjú Prop 21: maximal Bernoulli mass (**equivalent** up to band width); fractional b-matching | fail | **N1** | – | 0.75 |
| C3 | Separated-band counting (P28–P30) | Varjú Lemma 27 / Thm 3 (template); KK 2025 Props 4.9 and 5.4; KK 2026 (posterior) | pass (weak) | **N2** | – | 0.60 |
| C4 | Map entropy retained by types (P22) | Hochman Thm 1.4; GSSY/SSS/Käenmäki–Orponen types; Bárány–Verma Thm 3.5 | fail (borderline) | N2 | – | 0.65 |
| C5 | Uniform nonsaturation, signed and unequal ratios (P12) | Breuillard–Varjú Lemma 13 (named) | fail | N2 | – | 0.75 |
| C6 | Conditional gain via Jensen over future types (P27) | Varjú Prop 20 / Thm 3; environment averaging | fail (borderline) | N1 | – | 0.55 |
| C7 | Linear pair mass in an uncontrolled band (P24 + P23) | assembly of C1 and C4 | fail | N1 | – | 0.70 |

**Overrides of the family analyst.**
- **P14: N2 → N1.** It is Varjú's object, and Varjú 2019 is in L.
  - The F1 agent independently finds the same identity and grades P14 "N2, bordering N1".
  - The F1 agent also notes that KK 2026 *replaced* c_ℓ with a variance energy: the definition did not survive transfer, but the mechanism did.
- **P28: provisional N3 → N2.** Varjú's Lemma 27 is an in-L template.
- **P27 and P24: N2 → N1.**
- **P15 keeps provisional N3, at lower confidence (0.30).**

**Test 3 (Lean sub-DAG share of the 749-declaration main DAG).**

| Declaration | Share (declarations / tokens) |
|---|---|
| `pair_bound` | 0.19 / 0.22, which is at the 20% threshold; knockout-essential |
| `select_separated_bands` | 0.03 |
| `count_pair_budget_le` | 0.46 |
| `retained_loss_linear` | 0.20 |
| `conditional_gain` | 0.37 |
| `uniform_nonsaturation` | 0.27 |

**Why C1 alone survives, and how weakly.**
- **For:**
  - No prior statement has the log-free, multiscale, separation-free form, which is exactly what the uncontrolled endpoints B_n require.
  - Baker and Bárány–Käenmäki show that some separation-free bridge is necessary.
  - The delta over L is sharp: Prop 21 plus one device.
- **Against:**
  - It is a strengthening of a named predecessor in L by a single standard information-theoretic move, H(X) ≤ H(Y) + H(X|Y), with tensor-power-style amplification.
  - Another model run (GPT-6 Astra) produced the same mechanism within hours, three days later.
  - The PLAN puts named close precedents at N2. Whether Prop 21 is "close" enough is a judgment call. I judge it not equivalent, because the log loss is the whole difficulty, but an LLM judge could reasonably differ.

## 4. Discoverability protocols (Test 4, not run)

The full specification is in `novelty.json → discoverability_protocols`.

**Models.**
- Training cutoff before **2026-09-24**.
- A canary probe excludes any model that knows the conjecture is resolved, or knows 2610.10511 or openai/math #148.
- The 148-producing OpenAI model and the GPT-6 Astra lineage run only as the uncontrolled reference arm.
- No tools.

**Context.** L, with Varjú 2019 Props 20–21, Lemmas 22–27 and the proof of Thm 3 given verbatim, since they are the crux.

**Sampling.** n = 256 per arm, pass@k for k = 1…256.

**Judging.** Two judges plus an expert check. Lean target: `FairPairs.pair_bound` (SumsetBound.lean:329).

**Controls.**
- Positive: Cook–Reckhow ER extension variables.
- Negative: C2, which should hit almost always since it is in L; C4; C5.

**P-C1 (decisive).**
- **Hide:** P14–P18, P23, P24 and downstream (P27–P30).
- **Arm A (pivot):** give P22, P23 and the need ("linear pair mass over bands with uncontrolled endpoints").
- **Arm B (decisive):** also hide P22 and P23.
- **Hit:** a fine-scale entropy-deficit bound, or an entropy-loss-under-addition bound, that is *linear* in a multiscale pair or variance quantity, with a separation-independent constant. KK Thm 1.3 counts.
- **Partial, not counted:** single-scale, log-lossy or separation-dependent versions.
- **Distances:**
  - Pivot distance is about 2 from L (no trace; analyst estimate), or about 1 in Arm A.
  - Chain depth is 2.
  - External datapoint: a GPT-6 Astra hit in about 2.5 h, with human framing.

**P-C3.** Hide P28–P30. A hit is an adaptive diagonal choice against uncontrolled endpoints, plus per-scale disjointness or telescoping. Pivot distance is about 1; chain depth is 3.

## 5. Family label, flag and bridges

**family_D: D3 (provisional), confidence 0.30.**
- It rests on C1 alone.
- **It falls to D2 if any of the following happens:**
  - Test 4 for C1 hits above threshold. The GPT-6 Astra datapoint makes this plausible.
  - An expert (Varjú, Hochman, Shmerkin, Kittle) calls the log-free multiscale form folklore, or a routine consequence of Prop 21-type arguments.
  - Judges rule that a one-device strengthening of a named predecessor is N2.
- **Correctness** now has triple support, none of it verified here:
  - 148's Lean, which was not compiled here;
  - Kittle–Kogler's independent proof and its own roughly 47k-line Lean;
  - KK's description of 148's Lemma 3.2 as the weaker form of their Theorem 1.3.

**provenance_flag: no** (parallel posterior model-produced work: yes).

**bridge_novelty: every import is a known route for this problem type.**
- Information theory: the entropy-method lineage of Garsia, Hochman, BV and Varjú, plus entropic sumset theory.
- LP / fractional matching: cosmetic packaging of Varjú's object.
- Additive combinatorics: sumsets, already in Hochman's inverse-theorem route.
- Random grids: Wang 2011; Varjú's averaged entropy.
- Method of types and random environments: GSSY, SSS, Käenmäki–Orponen.
- Ergodic theory: Feng–Hu.

There is no new bridge. C1 is a new inequality inside known fields, not a cross-field import.

## 6. Open questions

1. Verify the KK quotes, dates and constants against the PDF of 2610.10511.
2. Establish GPT-6 Astra's vendor and lineage, and whether it had any access to the 148 run.
3. Check the analyst's sketch that Prop 21 plus Lemma 27 give a k = 1, log-lossy, separation-free bound. If a log-free version also follows from known arguments, C1 drops to N2.
4. Locate Lindenstrauss–Varjú's "work in progress" (2018), which Varjú cites for a decomposition similar to Prop 21.
5. Ask an expert whether the log-free multiscale bound is folklore.
6. Compile the Lean and run the comparator chain `pair_bound` → `pair_bands_of_retained_loss` → `count_pair_budget_le` → `no_strict_entropy_gap` → `entropy_rate_dimension`.
7. Repeat the absence searches on zbMATH, Google Scholar and MathOverflow. They were not queried directly; Bash has no network.
8. Settle the P14 convention (N1 here vs the F1 agent's N2 bordering N1).
