# Family 222: novelty pass (perceptron free energies and microscopic jamming exponents)

Date: 2026-10-12. Inputs:
- `family.json` / `family.md`. This family has no trace and no `f1_*` files.
- S `paper.tex`: intro and the full bulk section (lines 1075-1330).
- I: introduction and bulk-section greps.
- B: intro (line 68).
- J: intro (60-200), two-row deletion (2105-2135), selection section, bibliography.
- The Lean statement of `bulkMarkedArray_identification`.

Per PLAN (2026-10-12) the Lean is trusted as published. It was not built here.

**How the evidence was gathered**
- WebFetch failed with DNS errors on every host I tried: arxiv.org, ar5iv, mlr.press, talagrand.net and wikipedia. curl got a proxy 403.
- So every literature claim rests on WebSearch summaries plus my own domain knowledge. No quote is verified.
- The book text of Talagrand's perceptron chapters, which matters most for C1, could not be read.

## Provenance verdict: **partial** (model-produced precedent within the release; no external precedent for any candidate)

- **Within the release.** I and B take their architecture (the two-pattern cavity and the density-field contact comparison) from the OpenAI companion S. Both state that no theorem from S is used (I `introduction.tex:121-124`; B `paper.tex:68`).
  - J reuses the two-row deletion without citing S (J `main.tex:2116-2118`).
  - For I and B, the closest precedent of C1 and C3 is therefore model-produced. The family analyst recorded this as "yes".
  - For S itself, the only Lean-backed headline, I found no model-produced precedent.
- **Cited 2026 works that are AI-assisted but contain no candidate:**
  - **Shmalo, arXiv:2607.11010.** The acknowledgments, as summarised by search, say most of the work was done by Fable 5 (Anthropic) and Codex (OpenAI). It closes the capacity numerics and is only background in I.
  - **Parisi–Zamponi, arXiv:2606.03300.** It is Claude-assisted per press coverage, and is background in J. It proves the relation a+b=1 (γ=1/(2+θ)) *within* the physics scaling equations, so it is a close precedent for J's exponent relation only. It does not cover the selection of the microscopic limit.
- **Uncited:** Nakajima, arXiv:2512.23195, is GPT-5-assisted. It proves RS saddle-point uniqueness and contains no candidate.
- **Other cited 2025–26 works, with no AI disclosure in summaries:** Chen–Issa–Mourrat (2606.16636, 2508.06397) and Ho (2606.15432). These are precedents for C6 and J08 only.
- **Search for model-produced prior work.** Searches combining perceptron free energy with ChatGPT, GPT-5, OpenAI or "AI-assisted" found nothing for any candidate.

## Final grades

| ID | Candidate | Lean-backed | N | Conf. |
|---|---|---|---|---|
| C1 | Two-pattern removal and restoration, giving B = a(R) deterministic, plus the IBP balance (S09/I28/B07, and J) | **yes** (S: `bulkMarkedArray_identification`, `bulk_marked_self_consistency`) | **N2** | 0.70 |
| C2 | Tangential divergence on S_N plus a Wronskian solve, giving a = A_q = ∫D_q⁻² and supp μ ≤ B_* < 1 (S10) | yes (`tangent_wronskian_ae`) | N2 | 0.70 |
| C3 | Contact comparison with Poissonized density as HJ time, plus tail order (S08/S05, I26/I07) | yes (S upper bound) | N2 | 0.75 |
| C4 | B: θ-powered witness integral, Haar-flag projection witnesses, Haar-shell majorization | no | N2 | 0.60 |
| C5 | J: contraction rigidity selecting a_*, with an interval certificate | no | N2 | 0.60 |
| C6 | I: Ising entropy dual, attained via coordinate exchangeability (I04, I31) | no | N2 | 0.70 |
| C7 | J: row concavity, scale-mixture universality, deletion-and-repair threshold, martingale critical problem | no | N2 | 0.65 |

There are no N3 items. Nothing joins the Lean shortlist and no downstream file is needed.

**family_D = D2, confidence 0.7.** It rests on C1 as the best item.

### Why C1 stays N2 (the main question)
- **Test 1: close variants exist.**
  - **Talagrand's perceptron/Shcherbina–Tirozzi cavity.** This is AoP 2000, which is in L, and Mean Field Models vol. I ch. 2–3, "cavity in M", recalled from memory. Using symmetry among patterns and a cavity on patterns, it shows that the pattern-side overlap (1/N)Σ u′(S_k¹)u′(S_k²) concentrates on a constant r. That is the replica-symmetric ancestor of "B = a(R)". S's move is the full-RSB lift: the constant becomes a function on an RPC array, and the cavity becomes cascade restoration.
  - **Panchenko's multi-species synchronization** (in L) gives a conclusion of the same form: one species' overlap is a deterministic function of another's.
  - **Chen–Mourrat's critical-point identification** is the framework the paper names itself.
  - **The genuinely new step** is getting synchronization of the pattern-side overlap *without* a pattern-side perturbation. This is done by restoring two removed patterns as independent cascade marks, then closing with first and second moments.
- **Test 2: borderline.** The construction is not in L, but the identity it proves has the form of an L statement.
- **Test 3: passes on a single path.** Its subtree is 43–50% of the spherical DAG, but its dominated share is only 3.6–6.7%.
- **Reuse.** The device appears in all four manuscripts (I, S, B, J). That is reuse across variants of one problem type by the same model, not cross-problem reuse. Record it in the release-wide reuse count with that label.

### Other items
- **C2.** The target equation is the Crisanti–Sommers stationarity already in L. Spherical IBP is standard (Panchenko–Talagrand, Chen 2013, Bates–Sohn). It amounts to model-specific craft, with a dominated share of 0.4–1.1%.
- **C3.** This is Mourrat 2021 §4, named by the papers ("adapts", "implements"). Using the Poissonized constraint count as time is classical in diluted models (Franz–Leone, Panchenko–Talagrand). The tail order is one summation-by-parts step.
- **C4 and C5.** These are physics devices made rigorous: Monasson/Franz–Parisi θ-powers, and the CKPUZ/FPSUZ scaling plus Parisi–Zamponi. They have no Lean.
- **C6 and C7.** These follow precedents the papers name themselves (the Mourrat school's 2025–26 duality, Auffinger–Chen, Chatterjee and Nakajima–Sun).

### What would change family_D
D2 is the floor: C1–C3 are genuine adaptations, not abbreviations. Family_D rises to D3 only if all three of these hold:
1. The text of Talagrand's cavity-in-M is shown *not* to compute the pattern-side second moment via two patterns.
2. P-C1 arm B shows that contamination-controlled models rarely find restoration-based identification.
3. The device transfers beyond perceptron variants, for example to a Hopfield or GLM free energy.

## Bridge novelty
Most imports are **known routes**:
- the spin-glass RSB toolkit applied to the perceptron;
- stochastic control (Auffinger–Chen);
- RMT for structured disorder (Kabashima);
- validated numerics;
- the physics scaling theory.

Two are partly new:
- **Mourrat's HJ/contact method applied to the perceptron.** This is a known framework. Mourrat 2018 names the perceptron as a target, but I found no prior perceptron instance.
- **Majorization applied to Haar-shell volumes (B).** This is *possibly* a new bridge (low confidence, summary-level). Per CLAUDE.md it is recorded separately and is not a jump.

## Discoverability protocols (not run)
`novelty.json` gives the full protocols. They are written even though every item is N2.

**P-C1.**
- **What is hidden:** S's bulk section from line 1119 onward, plus the Lean `Cavity/Bulk*` files.
- **Arm A (pivot):** state that B converges to a deterministic function of R_12.
- **Arm B (decisive):** state only the obstacle, "identify the covariance of the field on new coordinates".
- **Arm C:** open problem.
- **Hit:** a two-pattern exchangeability argument, restoration on the reduced system's RPC, and the first-plus-second-moment zero-variance step.
- **Separate tally:** an alternative route through a pattern-side perturbation plus synchronization.
- **Sampling:** k ∈ {1, …, 256}, with models whose cutoff is before 2026-09-24. L⁻ drops the OAI companion and the 2026 preprints.

**P-C2 and P-C3** are N2 controls. P-C3 serves as a negative control, because the paper names its precedent.

## Open questions
- Read Talagrand vol. I ch. 2–3 and AoP 2000 to settle C1's Test 1. The text was unreachable here.
- Ask an expert (Panchenko, Mourrat, Chen or Sun) whether restoration-based synchronization is folklore.
- Verify the AI-disclosure wording of 2607.11010 and 2606.03300 against the PDFs.
- **J's provenance.** J uses S's device without citing it.
- **J's certificate.**
  - The certificate file is not in the release.
  - J records a driver run on October 4, 2026, which is after its stated date of September 24.
