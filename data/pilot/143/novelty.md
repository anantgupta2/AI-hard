# Family 143: novelty pass

**Problem.** Hilbert's sixteenth problem.
- **143a** claims uniform boundedness. It has no Lean.
- **143b** proves the degree-5 Lins–de Melo–Pugh case: at most 2 limit cycles, and the bound is sharp. It is Lean-backed, with comparator `OAI.QuinticLienard.main`.

**Analyst:** novelty, 2026-10-12.
**Base library L:** Mathlib d13f23b plus both bibliographies. L⁻ = L, because no cited work is model-produced.
**Network caveat:** WebFetch failed with DNS errors on every host tried, and curl to arXiv got a proxy 403. All literature claims therefore rest on search-engine summaries plus domain knowledge, and the quotes are unverified.

## Provenance verdict: **no**

| Work (2025–26) | AI disclosure | Contains candidates? | Role |
|---|---|---|---|
| CLZZ, arXiv:2608.19542 (Aug 2026), piecewise-linear Liénard | none in search summaries (unverified) | absent; it reports n = 5 as open | status citation |
| Hernández Rosales, ResearchGate preprint (Aug 2026) | unknown | absent; it is a 4-cycle example that 143b refutes | refuted claim |
| Yeung 2025 (arXiv 2402.12506) | none known | absent; it identifies a gap in Ilyashenko 1991 | 143a background |
| arXiv:2610.13080 (Oct 2026, slow–fast quintic), uncited | unknown | absent; it post-dates 143b | later work |

**Searches for model-produced prior work.** I searched "Hilbert 16", "quintic Liénard" and "LMP" together with ChatGPT, GPT-5, OpenAI, AI-assisted and AlphaEvolve.
- The only hits were the OpenAI release itself and the VibeMathed aggregator. VibeMathed attributes 143b to an unreleased internal OpenAI model.
- The two manuscripts do not cite each other.
- No other family in the release touches limit cycles.

## Final grades

| ID | Item | Lean | Grade | F | Conf. |
|---|---|---|---|---|---|
| **E1** | 143b quadratic-fit coordinates (H,P,Q,R,S,G; global fit Thm 3.6; transport Lemma 3.7) | **yes**: `QuadraticCoordinates.H`, `GlobalFit.fitK_spec`, `ActualFitTransport.fit_transport` | **N3 (provisional, borderline N2)** | F5 (+F1) | 0.40 |
| E2 | Model inequality (R/G)_r ≤ 0 via the Schwarzian of the endpoint correspondence | yes: `model_inequality`, `Cr_nonpos` | N2 | – | 0.60 |
| E3 | 143a packets + separation + absolute isolated-zero finiteness | **no** | N2 (upper N3; correctness unverified) | – | 0.45 |
| E4 | Shape comparisons: φ''' sign and ((φ'−d)/u)' sign | yes: `kappa_width_pos`, `intercept_negative` | N2 | – | 0.60 |
| E5 | Moving-cut matching systems + projection count | no | N2 (leans N1) | – | 0.60 |

**Changes from the provisional grades.**
- E3 moves from provisional N3 to **N2**. A packet is a multi-clock, parametric extension of Ilyashenko's superexact series combined with Écalle's lateral determinations, and the paper frames its own separation theorem inside that tradition (03-separation.tex:11-19). The difficulty lies in the proof, not in finding the object. E3 therefore does **not** go to `eureka_informal.json`.
- E1 keeps N3, with lower confidence.

## E1 in detail (the only N3)

**Test 1: no near-equivalent anywhere.**
- No Liénard or limit-cycle source found fits a model profile family to arc endpoint data (M, M_r).
- Nearest neighbours:
  - **Lagrange osculating elements / variation of parameters.** Lemma 3.7 is exactly this computation applied to the arc-data characteristic system: subtract the model's transport from the actual one, then solve a 2×2 system with determinant G. This is a template, not an instance.
  - Krylov–Bogoliubov equivalent linearization: data-space fitting, but heuristic only.
  - Massera's homothetic comparison.
  - Filippov plus F₁/F₂ branch comparisons (Zhang Zhifen, Coppel, Dumortier–Li, Li–Llibre): same coordinates, but no fit.
  - Villari–Zanolin.
  - Rychkov and Li–Lu (symmetric or slow–fast methods).

**Test 2: non-analytic. Pass.** H is defined implicitly through model-arc solutions and does not appear in the goal. One caveat: the model family is *suggested* by the goal's even part (introduction.tex:83-85). The data-space fit with exact transport is not suggested.

**Test 3: load-bearing. Pass.** H has 404 dependents, about 52% of the core, and cases 2–4 of `upper_bound` all go through `fit_transport`.

**Test 4: discoverability.** Pending; the protocol is P-E1 below.

**Downgrade risks.**
- The transport law is a 10-line osculating computation.
- The model choice is hinted at by the problem itself.
- The full texts of the Chinese-school Liénard literature were not readable here.

**Lean note for the downstream test.** The model layer is profile-independent. `fit_transport` and `kappa_width_pos`, however, are stated only for the quintic class (`a : Fin 6 → ℝ`), so reusing them for another degree first requires restating the actual-profile layer.

## Family verdict

**family_D = D3 (provisional), confidence 0.40.** It rests on E1 alone, which is Lean-backed.

It falls to D2 if any of the following happens:
- arm B of P-E1 hits at the calibrated rate;
- an expert finds a fitted-model or osculating comparison in the Liénard uniqueness literature;
- the osculating-elements template is judged a close variant.

The headline claim (143a, uniform boundedness) is unformalized and unconfirmed. D3 rests only on 143b.

## Bridge novelty
- **Osculating elements → Liénard half-arc comparison (E1):** *new bridge*. No precedent was found for this problem type, and the match is at template level only. This is recorded separately and is not automatically a jump.
- **Known routes:**
  - Schwarzian/Riccati → cycle bounds (Coll–Gasull–Prohens 1996, which the paper cites);
  - sign certificates;
  - averaging for sharpness (LMP 1977);
  - Écalle/Ilyashenko quasianalyticity → finiteness;
  - o-minimal/subanalytic geometry (KRS 2009, Speissegger program);
  - Khovanskii counting (Ilyashenko–Yakovenko, BNY);
  - Sard;
  - Duff rotated fields (the paper does not cite Duff).

## Discoverability protocol P-E1 (not run)

**What to hide:** Secs 3–6 of 143b (Q11–Q30 and everything downstream) and the Method paragraph of the introduction.

**Context given:** Sec 2 (arc data and matching), Q31, sharpness, and the bibliography as abstracts.

**Arms:**
- **Arm A:** adds the hint "quadratic profiles as comparison family".
- **Arm B (decisive):** no hint.
- **Arm C:** problem only.

**Hit criterion:** a map from endpoint data to the parameters of a 2-parameter model profile family, claimed invertible, with transport equations whose source is the actual-minus-model slope.

**Partial (recorded, not counted):** a Taylor-osculating parabola, or a fixed model with no fit.

**Sampling and judging:**
- k = 1…256, n = 256 per arm.
- Models must have a training cutoff before 2026-09-24, with a canary probe on degree-5 LMP. The OpenAI release models are excluded.
- Judging uses Lean equivalence against `QuadraticCoordinates.H`, `fitK_spec` and `fit_transport`.

**Other protocols:**
- **P-E2:** a calibration run for E2.
- **P-E3:** informal and optional.

**Pivot distance:** no trace exists for this family. Estimated pivot distance is ≥2 for arm B and about 1 for arm A; chain depth is 2.

## Open questions
1. Read Li–Llibre 2012, Dumortier–Li and Coppel 1989, plus the Ye Yanqian and Zhang Zhifen monographs, in full. This is the main risk to E1.
2. Re-fetch the arXiv abstracts to verify the AI-disclosure status.
3. Does arXiv:2610.13080 reuse the fit device?
4. Choose downstream targets for E1, e.g. generalized Liénard with nonlinear g.
5. Get an expert reading of 143a's correctness and of the novelty of the packet mechanism (the Speissegger/Kaiser/Rolin and Ilyashenko schools).
