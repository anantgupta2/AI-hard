# Family 079 novelty pass: Local smoothing in three dimensions

## Provenance verdict: **partial**
- **Model-produced work the paper cites.** 079 cites one model-produced work, OpenAIBochnerRiesz2026 (= family 078, same day). It does so only in Sec. 10, for comparison, and says that "That article is not an input to the deduction above" (10:138-141).
- **Uncited sibling with the same architecture.** 079 does **not** cite sibling **074** (*Kakeya maximal conjecture in three dimensions*, Sept 23, one day earlier). 074 uses the same architecture:
  - a critical exponent and equality configurations;
  - a "canonical temporal profile";
  - coordinate entropy rates constrained by Ren–Wang;
  - product-slope pinning adapted from Shmerkin–Wang / OSW.
- **Shared toolkit across the cluster.** 078 and 077 share the toolkit and cite 079 back. The method is a house method of the release cluster 074/077/078/079.
- **No AI disclosure in the human references.** None of the human 2025–2026 references discloses AI assistance (Gan–He–Li–Wu 2502.05973v2, Rozendaal–Schippa 2608.01440, Ren–Wang 2308.08819).
- **No outside claim.** No claimed resolution of 3+1 local smoothing outside the release was found.
- **Flag fields.** `builds_on_prior_model_result_strict = false`; model-produced precedent = yes (074, uncited); parallel model work = yes.

## Final grades

| Cand. | Item | N | F | Conf. |
|---|---|---|---|---|
| C1 | **Entropy-excess potential** E(a,v) ≥ 0 with zero boundary trace, transport inequalities (∂_a − k∂_v)E ≥ 2Γ, and a path contradiction (P54, P68, P72; round P86, P88) | **N3** | F4 | 0.30 |
| C2 | Lexicographic extremal reduction (minimal p, then shear costs c, c₁, giving affine profiles) | N2 | – | 0.60 |
| C3 | Canonical name 𝒞(a,v) (record with a moving shear frame) | N2 (paper-named precedent: Hochman–Shmerkin) | – | 0.65 |
| C4 | Hybrid classical/quantum cylinder model + conformal flattening of null hyperquadrics | N2 | – | 0.60 |
| C5 | Outgoing entropy via transverse pins + Ramsey | N2 | – | 0.55 |
| C6 | Rarity transport (Sp) | N2 | – | 0.50 |

**family_D: D3 (provisional), confidence 0.30.** It rests on C1 alone.

D3 falls to D2 in any of these cases:
- an expert judges the two-parameter extension of branching-function / entropy-growth arguments to be routine;
- the directed arm of Test 4 hits;
- the project counts the one-day-earlier sibling 074 as model-produced precedent;
- a gap is found in Secs 4–6 or 8.

## Test summary for C1
- **Test 1: no human near-equivalent found.**
  - **Nearest neighbours, all one-parameter:**
    - Orponen–Shmerkin / OSW branching functions with ε-linear intervals;
    - Lutz–Stull Kolmogorov-complexity profiles (from memory, unverified);
    - Hochman–Shmerkin local entropy averages.
  - **One-parameter version in this paper.** P50 (D′(a) ≥ 1+3d vs D(1) ≤ 1+3d−2Γ) is itself of the standard one-parameter type.
  - **What is new.** The two-parameter excess, with a boundary trace and directional transport.
  - **Siblings 074/078.** They contain close variants but are parallel model output, so they are recorded for provenance and contamination and not as precedent.
  - **Searches.** Listed in `novelty.json`. zbMATH and MathOverflow were not queried.
- **Test 2: pass.** The goal is an L³ Sobolev inequality, and nothing in it or in L mentions names, entropies or excess functions.
- **Test 3: pass by architecture.** C1 closes every positive-cost cylinder case and the whole round wave case, which is about half the paper by length. There is no Lean DAG.
- **Test 4: not run.** The protocol is P-C1.
  - Hide Secs 4.3–6 and 8.3–8.5.
  - **Arms.** The open arm gets the problem plus L. The directed arm also gets Secs 1–3 and 7.
  - **Hit criterion.** A proposal hits if it builds a nonnegative entropy deficit in ≥2 scale parameters that vanishes on a label-recoverable boundary and is contradicted by directional differential inequalities. A one-parameter version is a partial hit.
  - **Sampling.** k = 1…128.
  - **Contamination control.** Use models with a training cutoff before 2026-09-23, run a canary for papers 074/077/078/079, and keep the OpenAI lineage only as a reference arm.
  - There is no trace, so pivot distance is unknown and chain depth is high.

## Bridge novelty
- **GWZ (2+1) as an input to 3+1:** known route.
- **Ren–Wang Furstenberg into local smoothing / restriction:** known route (Wang–Wu two-ends Furstenberg; GHLW incidences).
- **Shannon entropy of wave-packet records:** a **new bridge**, with no human precedent found. It is shared with the sibling papers.
- **Bateman conformal covariance:** known route (Lorentz rescaling).
- **Ramsey and analytic sets:** incidental.

## Caveats
- **Correctness.** Everything is conditional on the correctness of an unrefereed, unformalised 12.6k-line proof. That proof would also settle Bochner–Riesz, sphere restriction and Kakeya maximal in ℝ³.
- **Reading depth.** Only Secs 0–2, 9–10 and the closing proofs were read line by line.
- **Cross-paper reuse.** The device's reuse across 074/077/078 hints at downstream speedup, but every reuse comes from the same model lineage, so it is not independent evidence.
