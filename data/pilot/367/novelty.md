# Family 367: novelty pass (one-phase Bernoulli critical dimension)

## Provenance verdict: **no**
The paper does not build on any prior model-produced result.

- **Three cited 2025–26 works show no AI disclosure** on their arXiv abstract pages:
  - Fernández-Real–Yu 2510.18330;
  - Firester–Tsiamis–Wang 2601.16966;
  - Firester–Tsiamis–Wang 2601.18794.
- **One cited work does disclose AI use: Fernández-Real–Serra 2609.05669** (4 Sep 2026, *stability conjecture in dimension four*).
  - It has a "Use of artificial intelligence" section, built around OpenAI Codex / GPT-5.5, with GPT-5.6 Sol and Claude Code.
  - The authors say they "fully designed all statements and proof strategies". This wording comes from a WebFetch summary and is unverified.
  - 367 cites it **only as background**. Its method (neck-linearization, a tangential Sternberg–Zumbrun inequality) shares nothing with 367's candidates.
  - It still treats cone classification in dimension 5 as open.
  - Recorded as `parallel_model_produced_work: true`.
- **Siclari 2609.12553** discloses "ChatGPT 5.6 Sol". It is uncited and unrelated.
- **Searches for model-produced prior work** on the problem name plus ChatGPT, GPT-5, OpenAI or AI-assisted found nothing on d_*. No posterior confirmation or refutation of 367 was found.
- **367's own verification directory** shows an internal multi-agent review: a "submitted engine", "peer reports", "debate graphs", and an independent engine frozen before access to the oracle. This is provenance of the *verification*, not prior literature.

## Final grades

| ID | Candidate | N | F | Conf. |
|---|---|---|---|---|
| **C1** | Flux pair h = w^a√f, Z = w^{2a}(G:X + wM + P), with the universal O(5)-equivariant tensor certificate f, U, K, M, P (Prop 4.1) | **N3** | F3 (+F5 aspect) | 0.40 |
| C2 | Fourth-derivative elimination: G = δ⊗U + skew part C | N2 | – | 0.60 |
| C3 | Boundary reflection parity, which kills the undetermined even-normal jets | N2 | – | 0.50 |
| C4 | Normalized jet derivation D_l (A = T/w, q = ∇log w, free X, w, z, ℓ) | N2 | – | 0.60 |
| C5 | Suspension, putting d=5 and d=6 on the same S⁵ | N1 | – | 0.70 |

Excluded at N0–N1:
- the weighted Bochner estimate;
- the V tensor (JS 2015 eq. 2.2);
- the Gram projections (Parrilo);
- the tensor bounds;
- stability and the Hardy constant (CJK; JS Prop 2.1);
- all Lean items. The Lean formalizes only De Silva–Jerison 2009.

**family_D = D3 (provisional), confidence 0.35, resting on C1 alone.** No templated-strengthening cap applies, because there is no induction.

## Candidate list
The family analysis lists P21 and P22 as provisional N3, and P20, P23, P24, P25 and P26 as N2. P24 and P26 are mechanical consequences of P21 and P22, so they are merged into C1.

Ranked candidates 4–5 from Phase 1 are C5 here and the excluded P35. There is no trace and no F1 file for 367.

## C1: the tests
**Test 1: nearest neighbours.** No near-equivalent was found.

| Neighbour | Relation | Verdict |
|---|---|---|
| Jerison–Savin 2015 Secs 2–4, named by the paper; I read the PDF pp. 1–10 | Scalar subsolution v = w^α, or w² = Σλ₊² + aΣλ₋², with the criterion λ ≥ (n−2)²/4 | Close in **role** only. JS uses no flux, depends only on Hessian eigenvalues, and is closed-form |
| JS Sec 3.2 (the obstruction) | The interior and boundary windows for α are optimal at different eigenvalue configurations, and L* = ∞ for n ≥ 5 | This is exactly what C1's non-gradient flux decouples |
| Simons 1968 | The minimal-cone template | Genuinely different |
| Pacati–Tortone–Velichkov 2025 | Convex curvature functions, capillary setting, n ≤ 4 | Genuinely different |
| Fernández-Real–Serra 2026, Firester–Tsiamis–Wang 2026 | Dimension-4 entire stable solutions; symmetric cones | Genuinely different |
| SOS auxiliary-function / Lyapunov certificates for PDE (Chernyshenko et al.; Goluskin–Fantuzzi; Valmorbida et al.) | The same **meta-method**, in fluids and control | Close variant of the method; the object is genuinely different |
| Calibrations / null Lagrangians | Generic divergence certificates | Ancestor of the idea only |

**Test 2: non-analytic. Pass.** The result is a nonexistence result, so the goal contains no witness.
- f, U, K, M, P and Z occur nowhere in the goal or in L.
- JS's subsolution is only the special case Z = h∇h, with f depending on eigenvalues alone.

**Test 3: load-bearing. Pass, by knockout.**
- The new half of the theorem is: N0 reductions + N0 stability + C1 + N1 cutoffs.
- Without C1, JS's method stops at n = 4.
- There is no Lean DAG to measure, because the new half is unformalized.

**Test 4: discoverability.** The test was not run; the protocol P-C1 is below.
- Pivot distance is about 2–3 from L, estimated (there is no trace). The chain runs: JS test → non-gradient flux → elimination-constrained polynomial ansatz → SDP.
- Chain depth is 2, because C2–C4 are design constraints of C1.

**Why N3 and not N2.**
- **For N3:** the specific ansatz has no neighbour. That ansatz is a non-gradient flux, dependence on g and ∇g, and elimination of the fourth-order and even-normal jets. It breaks a named obstruction that has stood for 11 years.
- **Downgrade risks:**
  - the paper names JS's Hessian-function tests as precedent;
  - the meta-method is imported;
  - the certificate is a search output;
  - correctness rests on code-verified arithmetic with tight margins.

## family_D
- **Rests on:** C1. C2–C4 are N2 design constraints.
- **What would push it to D2:**
  - a directed or tool-arm hit rate above threshold;
  - an expert-identified prior flux or SOS cone certificate (none was found);
  - a judge ruling that "JS generalized plus machine search" is a variant of a named precedent.
- **It is moot if the certificate is wrong.**
- **Not transfer:** the SOS import alone would only reach D1–D2. The claim rests on the geometric ansatz.
- **Correctness caveat:**
  - The new half has no Lean, and the README disclaims formula-to-code correspondence.
  - Two engines agree on 1714/1714 keys.
  - The D₀/D̄ ratios reach 0.99992.
  - The argument implicitly proves the smooth-link CJK conjecture in dimensions 5 and 6.

## Bridge novelty

| Import | Status | Evidence |
|---|---|---|
| SOS / SDP Gram certificates made exact | **New bridge** for free-boundary and minimal-cone stability, via a known method | No precedent found in JS, PTV, FR–Serra or FTW (all closed-form). The method itself is established in fluids, control and discrete geometry, so this is a transfer |
| O(5)/S_r tensor projections | Known route | Standard symmetry reduction |
| Bochner/Simons identities on the link | Known route | Simons → CJK → JS |
| Sharp Hardy constant | Known route | JS Prop 2.1 |
| Exact rational computer arithmetic | Known route in general | New for this problem |

## Discoverability protocols (not run)

**Common setup.**
- **Models:** training cutoff before **2026-09-24**. Use a canary on "is d_* = 7 known?" and on the content of openai/math paper 367. Exclude the lineage that produced 367. No browsing.
- **L:** a Mathlib digest, plus the 20 references, plus JS 2015 verbatim, plus 367 Secs 1–3 (all N0).
- **Arms:**
  - *open*;
  - *directed* (adds JS's Sec 3.2 obstruction);
  - *tool* (directed plus an SDP solver and an exact checker);
  - an uncontrolled reference arm.
- **Sampling:** n = 128 per arm (32 for the tool arm), pass@k for k = 1..128.

**P-C1.**
- **Hide** P19–P39.
- **Idea hit** requires all four of:
  - (a) a non-gradient Z with the pointwise interior and boundary inequalities;
  - (b) Z built from normalized jets;
  - (c) the undetermined fourth-order and even-normal jets eliminated by construction;
  - (d) a plan to certify by SOS.
- **Partial, not counted:** a better scalar F(eigenvalues).
- **Object hit:** an exact-verified certificate for m = 5.
- **Mandatory failing control:** the m = 6 case (Hardy constant 25/4) must be infeasible, because the De Silva–Jerison cone is stable in ℝ⁷.
- **Arms by role:** arm A gives the target flux form (this measures the ansatz design); arm B (open) decides N3.

**Sub-protocols P-C2, P-C3, P-C4:** hide P23, P25 and P20 respectively, with pivot distance 1.

**Controls.**
- Positive: Cook–Reckhow ER extension variables.
- Negative: C5, P35, and JS's w^α.

## Open questions
1. Recompute the 1,714-key expansion independently from the LaTeX, for example with a CAS in a sandbox. The margins are tight.
2. Is minimality used after Section 2? If not, the paper also settles the CJK smooth-link conjecture in dimensions 5 and 6. Seek expert opinion.
3. Run the m = 6 infeasibility check.
4. How was the certificate found, and does a much smaller one exist?
5. Read the rest of FR–Serra 2609.05669 for their "dimension five preliminary calculations".

Sources and full JSON are in `novelty.json`. The searches were standard WebSearch plus WebFetch of the arXiv abstract pages for 1410.7463 (and its PDF), 2609.05669 (and its HTML), 2601.16966, 2601.18794 and 2510.18330. zbMATH and MathOverflow were not queried directly.
