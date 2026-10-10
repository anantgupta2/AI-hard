# Family 368: novelty analysis ("The three-dimensional Ball–Evans approximation problem")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

**Inputs**
- `family.json`/`.md`, written in this session. There is no trace, no `f1_*` file, and no Lean for this family.
- Both manuscripts, read in full:
  - **M1:** 1≤p≤2.
  - **M2:** p>2.
- Web checks.

**L** = Mathlib d13f23b plus the union of the two bibliographies (58 keys).

## 1. Provenance verdict: **no**

- **Recent citations.** The only 2025–2026 works cited are both human, and neither carries an AI statement on its arXiv page:
  - Hencl's survey (arXiv:2502.01336). It lists dimension 3 as open: Open Problem 1, and "any positive result … especially … n=3". That quote came from a summarizer and is unverified.
  - Campbell–D'Onofrio–Vítek (arXiv:2507.02854). It is used only as background for PL→smooth, which M1 re-proves.
- **Course notes.** McMullen 2023 and Hatcher are also cited; they are not 2025–2026 research papers.
- **The companions.** The two OpenAI manuscripts cite each other, but each states it uses no theorem of the other (M1:01-introduction.tex:121-124; M2:01-introduction.tex:57-58).
- **Model-produced prior work.** WebSearch for "Ball-Evans" together with ChatGPT, GPT-5, OpenAI or AI-assisted found no model-produced prior work and no prior 3D resolution.

## 2. Final grades

| ID | Item | Grade | F | Conf. | Reason |
|---|---|---|---|---|---|
| C1 | Guard-pinned topological wall realization: the approximant is P₀∘T∘h, and its energy depends only on two label slopes (M2 Sec 7; M2-31/34/36/37) | **N3** | F5 (F3 guards) | 0.40 | See below. |
| C2 | Immersed cubical skeleton cutoff (M2-08/09) | N2 | – | 0.55 | Close variant of Kirby's torus-trick lift. The new part is quantitative (Whitney-scaled energy summation). The paper does not cite the torus trick. |
| C3 | Tie budget + softmax simplex squeeze (M1-27/28/29) | N2 | – | 0.65 | Federer–Fleming/White dual counting, which the paper itself names. The new part is that it is realized by a target homeomorphism. |
| C4 | Convex product quantizer + Poisson contact exclusion (M2-17/19/20) | N2 | – | 0.60 | Moreau / power diagrams, which the paper names. |
| C5 | Finite PL libraries before resolution (M1-14) | N2 | – | 0.65 | Väisälä 1977 (Carleson's method), which the paper names. |
| C6 | Flattening via decomposability bundle + converse Rademacher (M2-03..06) | N2 | – | 0.60 | Graph-parametrized variant of Alberti–Marchese Lemma 7.5, plus transfer. |
| C7 | Kernel compression + near-sharp line/plane budgets (M1-17/32/39/40) | N2 | – | 0.55 | 3D analogue of Hencl–Pratelli's singular models, plus Morrey ε-conformal parametrization. |
| C8 | Diagonal routing, period conservation (M2-29/30) | N2 | – | 0.60 | Haken regular exchange with parameter-measure bookkeeping. |
| C9 | Canonical snapping (M2-46) | N1 | – | 0.50 | Finite-type bookkeeping. The family analyst's N2 is lowered here. |
| C10 | Radial blocks / star replacement / p=2 angular attenuation (M1-23/36/37) | N2 | – | 0.60 | 3D topological analogue of planar local replacements. |

**C1 in detail.**
- **Test 1 (no near-equivalent).** No near-equivalent found in: Hencl's survey; IKO 2011 (planar coordinatewise p-harmonic replacement); Ntalampekos arXiv:1911.06619 (planar monotone level sets); Hencl–Pratelli; targeted web searches. zbMATH was not queried.
- **Test 2 (non-analytic).** Passes. Guards and label walls occur in neither the goal nor L.
- **Test 3 (load-bearing).** Passes. About half of M2 depends on C1, and without it the rank-1/2 mean gradients cannot be controlled.
- **Cap.** No templated-strengthening cap applies.
- **Risk.** Every ingredient is classical: oscillation of W^{1,p} functions on 2-spheres for p>2, intersection numbers via H₂=0, and Haken exchange. A judge may call this assembly N2.

## 3. Family verdict

**family_D = D3, confidence 0.35.**
- **Rests on.** C1 alone.
- **Falls to D2 if:**
  - an expert finds prior use of topologically realized level sets pinned by a capacity or oscillation barrier, or judges C1 a routine assembly; or
  - discoverability protocol P-C1 returns a high hit rate.
- **Downstream speedup.** Unlikely to pass. C1 is problem-specific. C2 is the more plausible reusable lemma, but it is graded N2.
- **Transfer.** The transfers (C2's torus-trick mechanism, C4, C6) are N2 and cannot carry D3.

## 4. Bridge novelty

| Import | Into | Classification | Conf. |
|---|---|---|---|
| Alberti–Marchese bundle + De Philippis–Rindler | flattening (C6) | new bridge | 0.6 |
| Haken normal surfaces / regular exchange | label walls (C1, C8) | new bridge | 0.6 |
| Moreau / power diagrams | 2-complex quantizer (C4) | new bridge | 0.5 |
| Torus-trick immersion lift | energy cutoff (C2) | new bridge (uncited) | 0.5 |
| Federer–Fleming dual counts | trace budgets (C3) | new bridge (GMT precedent cited) | 0.5 |
| Moise/Bing/Hamilton, Schoenflies, Edwards–Kirby | qualitative topology | known route | 0.8 |
| Ahlfors–Bers / Morrey | p=2 disk estimate | known route | 0.7 |
| CHM inverse-BV/Lusin, Clarkson convexity | traces, energy-to-strong | known route | 0.85 |
| Lovász local lemma | mesh jitter | incidental | 0.5 |

## 5. Discoverability protocols (not run)

- **Models.** Training cutoff before 2026-09-24, with no exposure to the 2026-10-06 release. The producing OpenAI model may appear only as a reference arm. Use a canary probe, no retrieval, and a judge distinct from the proposer.
- **Context L.** The problem statement plus a digest of the 58-key bibliography.
- **Sampling.** n=256 per arm, k ∈ {1,4,16,64,256}.
- **Judging.** An LLM judge with a rubric (no Lean), a second judge on disagreements, and a 10% human spot-check.

| Protocol | Hide | Hit criterion | Arms |
|---|---|---|---|
| P-C1 | M2 Sec 7, plus the guard and capacity parts of Secs 8–9. Keep the carrier, quantizer and standard walls. | Energy carried only by label slopes, **and** realized labels pinned by a p>2 sphere/capacity barrier. | L, open, directed |
| P-C2 | Immersed-skeleton lemmas | Lift through an immersion at a common scale over Whitney layers, with the (ℓ/s)³ vs (s/ℓ)² count, and fillings excluded from the energy | L, L+ (add Kirby), open |
| P-C3 | Budget transfer | Dual-skeleton crossings plus an injective concentration map | L, L− (remove White) |
| P-C4 | Quantizer | Gradient of a Legendre conjugate / power diagram with contact control | L |
| P-C5 | Library construction | PL libraries fixed before resolution | L |
| P-C6 | Flattening | Use of the decomposability bundle | L |

There is no trace, so pivot distances are estimates. C1 has pivot ≈3–4 and chain depth 4: it needs C4, C2 and the wall machinery first.

## 6. Open questions

- Expert verification of correctness: about 15k unreviewed lines on an open problem. Is any analogue of C1 known?
- Is C2 reusable as a general quantitative 3D near-identity cutoff, making it a downstream-speedup candidate?
- A zbMATH search was not done.
- Could M1's budget method reach p>2? The answer would show whether C1 is essential.
