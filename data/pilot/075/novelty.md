# Family 075: novelty analysis ("The L log L Fourier-convergence conjecture")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`, which uses the 287 keys plus `precedent_checks`, `bridge_novelty` and `sources`.

**Inputs**
- `family.json` / `family.md` and `lean_layer_notes.md`.
- `f1_thermal_labels.{json,md}`. These arrived during this analysis and are incorporated.
- The preprint source (`build/main.tex` plus 10 section files, `references.bib`).
- Spot checks of `lean/OAI/Analysis/FourierLLogL/Thermal/`.
- Web checks.

No reasoning trace was released for 075, so pivot distances and chain depths are estimated from the paper.

**L** = Mathlib d13f23b plus 075's 23-entry bibliography. Every entry is human literature, so L⁻ = L. The `carleson` library is pinned in the manifest but not imported, so it is not counted in L.

## 1. Provenance verdict first: **no**

| Check | Result |
|---|---|
| 2025-2026 citations | Only Di Plinio–Fragkos, Trans. AMS 2025. It is arXiv:2204.08051, v1 from 2022-04-17, and the abstract page shows no AI disclosure (WebFetch summary, wording unverified). It is purely time-frequency (wave packets, weak-L^p ~ (p−1)⁻¹) and contains **none** of the candidates. |
| Paper-named precedents | Lee 2017 ("Related entropy-minimization arguments appear in"), Chang 2002, Ginibre 1970, Lie 2013 (good-set template), Petermichl/Hytönen. All human, all pre-2023. |
| Web: problem + ChatGPT / GPT-5 / OpenAI / AI-assisted | Only the October 2026 release coverage, which does not discuss 075 technically, plus human papers. |
| OpenAI "Ten Advances" collection | PDF CreationDate 2026-08-05, subject "A collection of research papers by an internal model at OpenAI". A keyword scan of the extracted text finds no Carleson, no L log L and no a.e. Fourier convergence. **Not a precedent.** It does show the internal model lineage was active by early August 2026. |
| F1 agent | No post-release use or discussion of the device. No other release family uses it. |

**Provenance flag: no.** The family neither builds on nor is anticipated by model-produced work. Unlike 287, there is no ChatGPT-assisted precedent. The paper itself is model-produced (author "OpenAI", dated 2026-09-23).

## 2. Final grades

| # | Item | Nearest neighbour(s) | T2 | T3 | Final | F | conf |
|---|---|---|---|---|---|---|---|
| C1 | **Thermal noisy labels** Z = Y+θ, θ ~ K_A = e^{F−A}, adaptively tightened (I26, I24) | Bohr-set localisation (Bourgain 1999, Sanders); stochastic localisation (Eldan; El Alaoui–Montanari 2109.00709); Tao entropy decrement; Russo–Zou information budget; generalised von Mises (noise law only). **No near-equivalent found**, confirmed independently by the F1 agent | pass | pass (Lean frac 0.26 / 0.21) | **N3 (provisional)** | **F1** | 0.35 |
| C2 | Two-law accounting + global Fisher sum (I10, I27) | Entropy chain rule + Pinsker (folklore); entropy decrement; L log L = relative entropy | fail (borderline: the budget is the goal's hypothesis read as entropy) | pass | N2 | – | 0.60 |
| C3 | Entropy compression lemma (I12 + I13–I17, I23) | Chang 2002, **Lee 2017 (paper-named)**, Impagliazzo–Moore–Russell, inverse Littlewood–Offord (Tao–Vu, Nguyen–Vu); pinning (I16) is equivalent to Montanari / Raghavendra–Tan | pass | pass (dom 0.15) | N2 | – | 0.60 |
| C4 | Two-visit-order refinement search (I22, I21) | Increment/telescoping templates; entropy decrement over block lengths | pass | pass | N2 | – | 0.50 |
| C5 | Gap potential F(A) − log\|B_A(r)\| (I29) | Log-slack of the Bohr-set uncertainty principle; Bohr-set size/rank tracking (Bourgain, Sanders) | pass | pass by knockout (Lean frac 0.06) | N2 | – | 0.55 |
| C6 | Spectral update, regular/cheap (I30, I28, I31) | Increment dichotomy; Bourgain regular-radius pigeonhole; Chang/Lee | pass | pass (dom 0.19) | N2 | – | 0.60 |
| C7 | Prop dyadic (I32) | Petermichl shift (in L); maximally modulated Haar multipliers (1506.00861 App. A; Zorin-Kranich); Walsh–Carleson; Lie 2013 | fail (borderline) | pass (dom 0.90) | N2 | – | 0.65 |
| C8 | Good-set + doubly exponential layers (I05, I07) | Lie 2013 Prop 3.1; Sjölin/Antonov layering | fail | pass | N1 | – | 0.60 |
| C9 | Procedure, plateaus, live budgets (I33–I35) | CZ / tree stopping times; **templated IH (extra tracked quantities)** | pass (weak) | pass | N2 (cap) | – | 0.65 |
| C10 | Capture / snapshots (I36) | Lee Riesz-product increment | pass (weak) | pass | N2 | – | 0.60 |
| C11 | Path estimates (I38, I40) | Burkholder, Nazarov–Treil–Volberg Bellman; **templated extra coordinate** | pass (weak) | pass | N2 (cap) | – | 0.65 |

Transfers excluded as N0: Griffiths–Ginibre (I25), the Chang/Lee sumset bound (I28), Petermichl–Hytönen and the Riesz projection (I43, I44), Stein (I08), and Ville (I37).

**Overrides of the family analyst.**
- C3, compression: N3 → N2. The paper names Lee 2017, and the lemma is a uniform-in-weight member of the Chang / inverse-Littlewood–Offord family.
- C4, search: N3 → N2. It is a scheduling fix that the paper itself derives from an identified obstruction.
- C5, gap potential: N3 → N2. Through the Bohr-set lens, K_A is a smooth Bohr set and B_A(r) is its dual ball. The gap is the slack in the uncertainty inequality |B_A(r)|·e^{−F(A)} ≤ C, which is exactly how the paper proves the gap is ≥ −C.
- C7, Prop dyadic: N3 → N2. As a statement it is the goal's per-layer estimate with Petermichl's shift substituted. Its novelty lives in its proof.
- C1 survives, but with confidence 0.35.

**Why C1 survives, and how weakly.**
- **For:** it is a new random variable, tiny to state and absent from the goal and from L. It replaces the loss in the number of frequencies (union bound, chaining, Bourgain multi-frequency) with a single O(d) information budget (F1 report). It is the only new object above the 20% Lean proxy: `Thermal.label` 0.255 and `Thermal.channel` 0.206, used in 18 and 22 files, and roughly 10k of 29.2k lines touch it. This is the profile of a Cook-style extension variable.
- **Against:**
  1. The noise law concentrates on a smooth Bohr set of the discovered frequencies. Conditioning on Z is therefore a *randomised* Bohr-set localisation, and a judge may call it a stochastic twist on Bourgain/Sanders density increment.
  2. "Progressively sharper noisy observation, paid by entropy" is the stochastic-localisation template.
  3. Chain depth 3: it pays off only together with C2, C3 and C5.

  Both this analysis and the F1 agent see a real N2 risk.

## 3. Bridge novelty

| Import | Status | Evidence |
|---|---|---|
| Information theory → Carleson-type maximal bounds | **new bridge** | No Shannon-entropy, Fisher-information or noisy-observation proof of any Carleson-type bound was found. The surveys (Lacey math/0307008, Demeter 1210.0886) list only tile proofs. In this literature "entropy" has meant level-set or metric entropy (Fefferman 1978; Bourgain). The route entropy → large spectrum is known (IMR, Lee), but not for pointwise convergence. |
| Statistical mechanics (Griffiths–Ginibre, XY Gibbs forms, free energy) → harmonic analysis | **new bridge** (the import itself is N0) | No prior use in this problem area was found. |
| Additive combinatorics (Chang, Riesz products, Bohr-type balls) → Carleson | partly known route | Lie (1902.03630 appendix; Polynomial Carleson) explicitly links additive combinatorics with time-frequency analysis. |
| Ville, change of measure, Bellman functions | known route | Standard in dyadic harmonic analysis. |
| Petermichl–Hytönen dyadic representation | known route | Standard. |

## 4. Discoverability protocols (Test 4, not run)

The full specification is in `novelty.json → discoverability_protocols`.

**Common settings.**
- **Model eligibility:**
  - Training cutoff **strictly before 2026-08-01**. The paper is dated 2026-09-23, but the internal lineage was producing results by 2026-08-05.
  - A canary probe: the model must not know that the L log L conjecture has been claimed, the openai/math repo, or the terms "thermal label" or "entropy compression lemma" in a Fourier context.
  - Excluded sources: openai/math (preprint 075, `FourierLLogL` Lean, `lean/docs/075.md`) and October 2026 press coverage.
  - The OpenAI internal model and its descendants are excluded; they run only as a reference arm.
  - No tools. The judge must not be the proposer.
- **Arms:** open, directed, and L+IT (which hints at de Bruijn and stochastic localisation).
- **Sampling:** n = 256 at T = 1, with pass@k for k = 1…256.
- **Judging:** two LLM judges plus a harmonic analyst. Lean equivalence is used where a target exists (`Thermal.channel`, `Compress.entropy_compression`, `Thermal.gap`, `Dyadic.GridBound`).
- **Controls:** Cook–Reckhow ER (positive); C8, C7 and I43 (negative).

**P-C1 (decisive).**
- **Hide:** I24, I26, I27, I29–I31, I33–I36 and I38–I42.
- **Arm A (pivot):** give Prop dyadic, the compression lemma and the two-law framing, with the directive "pay for frequency selection with information about the input point".
- **Arm B (decisive):** give Prop dyadic plus L only.
- **Hit criterion:**
  - (a) A noisy observation Z = Y + noise of the input point, whose law is adapted to the frequencies already found.
  - (b) Reading modulated coefficients through Z, charged to an O(d) entropy budget.
  - Deterministic Bohr-set restriction is recorded as a near miss.
- **Distances:** pivot distance ≥ 2 (estimated); chain depth 3.

**Other protocols.**
- **P-C3:** pivot distance 1 from Lee; depth 1. The hit must have uniformity over all weights on S′.
- **P-C4:** pivot distance 1; depth 2.
- **P-C5:** pivot distance 1 given C1; depth 2.
- **P-C7:** pivot distance 1; depth 0. This is control-like.

## 5. Family label

**family_D: D3 (provisional), confidence 0.35.**
- **Rests on:** C1 alone, the thermal noisy labels. Its N3 meaning attaches to the cluster C1 + C2 + C5, with C3 as the engine.
- **Falls to D2 if:**
  - P-C1 arm B exceeds the calibrated threshold; or
  - an expert identifies the label as a known randomised Bohr-set or stochastic-localisation device already used for maximal or Fourier-type estimates.
- **Not transfer:** the N0 imports (Ginibre, Chang/Lee, Petermichl, Ville, Stein) are coupled *by* C1, so the cross-field-transfer exclusion does not apply.
- **Correctness caveat:** all grades are conditional on correctness. The claim is extraordinary: it settles the L log L conjecture and gives a new proof of Carleson's theorem. It is unrefereed. The Lean was not built here. It formalises a different parametrisation, only the ε_j = r_{j+1} case of Prop dyadic, and a substitute for the simultaneous regular-evidence proposition.
- **Compression:** there is no step-3b measurement for 075. Inlining `Thermal.channel` is the natural test for an extension-variable signature.

## 6. Open questions
1. **Expert query** to an additive combinatorialist or harmonic analyst (e.g. Sanders, Bloom, Lie, Di Plinio, Thiele): is a Gibbs or Bohr-noise observation of the input point a known device? This is the main risk to C1.
2. **Run F1's most informative downstream test:** a finite model of Bourgain's multi-frequency lemma, (log N)² → log N.
3. **Build the Lean and run the comparator.** Confirm that the GridBound special case suffices and locate the substitute for the simultaneous-evidence statement.
4. **Step-3b inlining of the label channel.**
5. **"Proves too much" check:** which step fails at L√(log L)?
6. **Re-run absence searches** on zbMATH, MathSciNet and Scholar, which were not available in this session.
7. **Ask OpenAI for the 075 run dates** to set the contamination cutoff precisely.
8. **Konyagin is uncited:** get an expert to confirm there is no conflicting negative result.
