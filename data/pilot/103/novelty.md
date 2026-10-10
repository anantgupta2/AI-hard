# Family 103: novelty pass (L = RL = BPL)

Date: 2026-10-10. Inputs: `family.json`/`.md`, the manuscript, the Lean dir, and `data/items/103_lean.json`. This family has no trace and no F1 files.

**How the evidence was gathered**
- WebFetch failed with DNS errors on arxiv.org and eccc.weizmann.ac.il, so every literature claim below rests on WebSearch summaries. No quote is verified.
- The Lean was not built by me; the orchestrator compiles the comparator.

## Provenance verdict: **no**
- **Cited 2025–26 works.** Three are cited: Chen–Cohen–Doron–Khaskelberg–Ta-Shma (APPROX/RANDOM 2026), Cheng–Wu (arXiv:2609.23603, posted 2026-09-20) and the Pyne–Tell survey (ECCC TR26-045).
  - Their listings are by human authors, and the search summaries mention no AI assistance. I could not fetch the pages themselves, so this is unverified.
  - None of the three contains the candidate items.
- **Model-produced prior work.** Searches for the problem together with "ChatGPT", "GPT-5", "OpenAI" or "AI-assisted" found none.
  - The only earlier OpenAI model-produced math release I found is the Aug-2026 "Ten Advances" (Astra). Its snippets mention no BPL result.

## Final grades
| ID | Candidate | N | F | Conf. |
|---|---|---|---|---|
| C1 | Correction-and-copy hierarchy, a shallow exact reward target (I06+I07+I09+I11+I12) | **N3** | F5 (copy-space embedding) + F4 (entry × support potential) | 0.5 |
| C2 | Slack-telescoped multilevel estimator in one shared O(log n)-bit environment (I20, I17, I19, I29) | **N2** | – | 0.5 |
| C3 | Allowance potential Φ = Aw + Dt, telescoping over the stack (I28) | N2 | – | 0.6 |
| C4 | Sampled column detectors and incoming gates (I09, I13) | N2 | – | 0.6 |
| C5 | Block-clean coupling for adaptive fingerprints (I22, I23); **not in the Lean** | N2 | – | 0.6 |
| C6 | Validated walk variants (I17) | N2 | – | 0.55 |
| C7 | Factorial truncation (I08) | N1 | – | 0.55 |
| C8 | Default-plus-exceptions compression (I21) | N2 | – | 0.55 |
| C9 | Catalytic restoring equality test (I24) | N0 | – | 0.9 |
| C10 | Affine spectral gap: property (T) in the paper, Fourier torus gap in the Lean (I16) | N0 | – | 0.9 |

**family_D = D3 (provisional), confidence 0.4.**
- It rests on C1 alone. In practice C1 has force only together with C2 and C3.
- It falls to D2 if either of these happens:
  - test-4 protocol P-C1 shows that pre-cutoff models find a copy/dilution hierarchy;
  - an expert identifies a precedent in Markov-chain state reduction or incomplete factorization.

## Candidate notes

### C1: the hierarchy
**What it is.** Each stage moves transition mass into a reward through the identity I−D = (I+E)(I−C):
- E is a detector-gated, soft-thresholded Neumann correction.
- The remaining large entries are split over D0 copies.
- The maximum entry falls by 2^H per stage, while the active vertex count at most doubles.

So after O(log n) stages, |p0 − W_L| ≤ |V0|·2^{-(H−1)L}.

**Test 1 (precedents).**
- The identity alone is classical left preconditioning ((I+S)-type, Richardson): equivalent, but **only for I06**.
- Genuinely different constructions:
  - CDRST21 and CDST23 (Richardson, "shift and truncate", precision alternation);
  - AKMPSV20 (cycle-lifted graphs);
  - Saks–Zhou and Hoza21;
  - ILUT (Saad, recalled from memory, not searched).
- I found no neighbour for the whole construction.

**Test 2 (analyticity): passes.** V_l, routing fractions and W_l occur nowhere in the goal or in L.

**Test 3 (load-bearing): passes.** In the Lean, `residual`, `substochastic` and `factorial` each have 912 dependents. That is 35% of the 5,166-declaration DAG, more than the whole 27% mathematical core.

**Against.**
- It is a combination of individually known moves.
- On its own it does not beat log² n.

### C2: the estimator
**What it is.** It averages the differences T_{b,m} − T_{b,m−1}, using expander walks whose length is proportional to the slack M−m. Frame space is then O(slack), and it telescopes to O(log n).

**Why N2, not N3.** Under the strict rule this is a close variant of two things:
- **Multilevel Monte Carlo** (Heinrich 2001, Giles 2008). Small differences between levels need little averaging; this is a transfer from numerical probability.
- **CDST23**. Its "precision-alternating recursive scheme" exists to avoid paying log n per level, the same goal (search snippet).

The coupling of these with space accounting looks like a **new bridge**: searches found no use of MLMC in space-bounded derandomization. Upgrade C2 to N3 only if P-C2 fails even with MLMC and CDST23 in context.

### C5: fingerprint coupling
I found no fingerprint, hash or collision declarations in the 43k Lean lines. `CatalyticComparison.lean` compares IDs exactly, digit by digit. The paper's Section 9 is therefore apparently not on the formal path, so C5 is ineligible for the Lean shortlist.

### Lean vs paper route
- The Lean uses s = 4, where the paper uses 8.
- It replaces Shalom's property (T) with an elementary Fourier "square torus gap" (AffineSampling.lean:723).
- It omits the fingerprints.

A successful build therefore certifies the theorem and C1–C3, not the paper's Sec. 6 (the property-(T) route) or Sec. 9 (fingerprints).

## Bridge novelty
- **Known routes:**
  - property (T) / expanders, and Riesz–Thorin;
  - preconditioning / Richardson (AKMPSV20, CDRST21, CDST23);
  - catalytic computing (Buhrman et al.; Cook–Mertz; the BPL ⊆ CL line);
  - hashing;
  - Cook–McKenzie contours.
- **New bridge:** MLMC-style telescoping applied to space-bounded recursion. This is implicit in the paper and not cited; the finding is snippet-level.

## Discoverability protocols (not run)
**Common setup.**
- k ∈ {1, 4, 16, 64, 256}.
- Models must have a training cutoff before 2026-09-23 and pass a canary probe.
- OpenAI's release-producing models (and Astra) are excluded from the main pool.
- Positive control: PHP ER extension variables. Negative controls: I02 and I24.

**P-C1.**
- Hide: Sec. 3 onward.
- Ask for: an O(log n)-stage representation of p0 with small entries.
- Judge accepts only if the proposal has all three of: (a) a mass-to-reward factorization; (b) splitting of large entries over vertex copies; (c) a support-vs-entry potential.

**P-C2.**
- Hide: Secs. 7–12.
- Ask for: a recursive estimator whose per-level space is below Θ(log n).
- Judge accepts if the proposal has budget telescoping plus averaging and frame length tied to the slack.

## Open questions
- **Comparator build.** Everything above is conditional on the comparator building. This is an unrefereed claim to resolve a famous open problem, and I found no expert reaction.
- **Fingerprints in the Lean.** Confirm by elaboration that the Lean route avoids fingerprints.
- **C1 precedent.** An expert check for precedents of the hierarchy in Markov-chain state reduction and incomplete factorization.
- **AI disclosure.** Fetch the abstract pages of the 2026 cited works to confirm there is no AI disclosure.
