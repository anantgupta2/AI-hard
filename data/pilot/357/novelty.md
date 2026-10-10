# Family 357: novelty analysis ("Bi-Lipschitz coordinates at every regular RCD point")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

Inputs:
- `family.json`/`family.md`, from phase 1 of this agent;
- the full preprint source.

The family has no trace, no F1 file and no Lean.

**L** = Mathlib d13f23b (no RCD content) plus the 30-entry bibliography. **L⁻** is L without HZ26, for contamination control. HZ26 holds no candidate, but it does state the conjecture.

## 1. Provenance verdict: **no**
- **HZ26** (Honda–Zhang, arXiv:2608.16021v1, 17 Aug 2026) is the paper's source for the conjecture.
  - I read the full text from the PDF.
  - Its acknowledgements (Simons Center, Bernoulli Center, M.-C. Lee, T. Fujioka) contain **no AI disclosure**.
  - It recalls the conjecture verbatim: "it is conjectured, for example in [CC97], that every regular point in the non-collapsed setting admits a bi-Lipschitz chart".
  - Its own bi-Lipschitz charts need positive injectivity radius.
  - It contains none of the candidates.
- **GV25** (arXiv:2406.13771) and **DPG18 v3** (2025 revision, "thank to Liming Yin") show no AI disclosure and contain no candidate.
- I searched for model-assisted or earlier proofs of the regular-point statement and found none.
- Naber's 2020 survey (arXiv:2010.10031) lists the related **Open Problem 2.2** as open. That listing is a summarizer's paraphrase, so the quote is unverified.

**Provenance flag: no.** The paper does not build on any model-produced result.

## 2. Final grades
| Cand. | Item | N | F | Conf. | Nearest neighbour |
|---|---|---|---|---|---|
| **C1** | Value-space renormalization h_{i+1}=h_i+(Dh_i)^{-T}v_i with the ℓ² diagonal recurrence (I41, I43, I47) | **N3 (provisional; Test 4 pending)** | F5 (F3) | 0.40 | Toro 1995 / David–Toro σ_k patch corrections: close in architecture, different in mechanism |
| C2 | Summable directional pinching (I34, with I31–I33) | N2 | – | 0.65 | CJN21 Thm 6.1 sharp splitting (linear Hessian² bound by pinching); Breiner–Park 2025 |
| C3 | Mass forms D_{i,y} on value space and cumulative comparison (I22) | N2 | – | 0.60 | CJN21 §8 heat-Gram telescoping; CN15/HH24/HZ26 normalization matrices |
| C4 | Non-commutative inverse increments (I20, I21) | N2 | – | 0.60 | CJN21 §8 |
| C5 | Radial transport lemma (I32) | N2 | – | 0.50 | weighted radial energy technique |
| C6 | Summable radial invariance, E_i (I30) | N2 | – | 0.60 | CJN21 §6 |
| C7 | Gevrey all-order jet bootstrap (I44–I46) | N1 | – | 0.70 | majorant method (templated IH) |
| C8 | Near-minimizing patch centres (I40) | N1 | – | 0.60 | generic selection trick |

These items are excluded as N0 or N1:
- the volume-telescoping Poisson defects (N0, Cheeger–Colding);
- the measure-data L¹ gradient bound (N0, Boccardo–Gallouët type);
- harmonic normalization and heat Gram (N1);
- the open-coordinates and limit-chart routines (N1).

## 3. family_D: **D3 (provisional), confidence 0.35**
The label rests on **C1 alone**.

**Why C1 survives Test 1.** I searched these fields:
- GMT (Toro, David–Toro);
- metric Reifenberg (GV25, Cheeger–Colding);
- Ricci-limit transformation theory (CN15, CJN21, HH24, HZ26 Thm 3.8);
- Nash-type iterations;
- 2D bi-Lipschitz parametrization (Bonk–Lang).

None of them builds **one map on the coordinate-value space** whose pullback metric increases by the localized Bochner mass forms. In that setting the first-order Gram drift is non-summable, and H_k may be unbounded. No neighbour pairs the update with an ℓ² recurrence on D²h(ξ,ξ) that sums errors with ΣE_i rather than Σ√E_i, and that is exactly what crosses the classical bi-Hölder barrier.

The nearest neighbour is the David–Toro construction σ_k = Id + Σψ_j(π_j − Id), which is cited as DT12. It shares the architecture of patchwise corrections summed over scales under a square-summable condition. Its mechanism is second-order (Pythagorean) distortion, whereas 357 has first-order, unbounded, positive metric growth compensated through J^{-T}.

**Test 2** passes: as posed, the problem suggests harmonic or distance coordinates, and those provably fail (Colding–Naber, Naber Ex. 2.3). **Test 3** passes by knockout: without Section 4 the paper yields only bi-Hölder charts. The down-share proxy (0.07–0.13) is low only because the chain is linear.

**What would downgrade D3 to D2:**
- Test 4 arm A (I22 and I34 given, value-space strategy stated) clears the threshold, which would mean a low pivot;
- a judge or expert reads C1 as David–Toro σ_k plus a Newton-type correction;
- an expert finds a prior value-space renormalization;
- a gap turns up in the proof.

**Correctness caveat.** This is an extraordinary, unrefereed claim with no Lean and no trace. The phase-1 audit found no gap in the steps traced, but the RCD technicalities and the uniformity of the compactness arguments are sketched.

There is also an implication the paper never states. Cor 1.2 would settle Naber's Open Problem 2.2 in local-chart form. It also predicts a non-harmonic bi-Lipschitz chart at the special point of the Colding–Naber example. That is a natural sanity test for experts.

The catalogue says the constant is "point-dependent", but the paper claims it depends only on n.

## 4. Bridge novelty
| Import | Status |
|---|---|
| "Square-summability suffices" (Toro/DT12, GMT) applied to intrinsic RCD charts | Partly a known route: GV25 does metric Reifenberg, but needs first-order summability. Using volume pinching through Bochner mass in value space is a **new bridge** in substance |
| Nash-type stagewise positive metric increments applied to RCD charts | **New bridge**, if counted as an import; the paper does not cite Nash |
| Gevrey/majorant control of derivative loss | Known route |
| CJN21 sharp splitting and heat-Gram telescoping | Known route, same field; named by the paper |
| Invariance of domain; PSD matrix analysis | Known route |

## 5. Discoverability protocols (not run)
**Common settings.**
- **Models:** training cutoff before **2026-09-25**. Use a canary probe on "regular-point bi-Lipschitz conjecture resolved?" and "value-space renormalization". Exclude the OpenAI release models, except as an uncontrolled reference.
- **Context:** L⁻ digest.
- **Arms:** open, directed, and L⁻.
- **Sampling:** 256 samples per arm; report pass@k for k = 1…256.
- **Judging:** two LLM judges plus a human geometric analyst. Lean equivalence is not possible.
- **Controls:** Cook–Reckhow PHP (positive); C7 and the volume telescoping (negative).

**P-C1.** Hide I41–I49.
- *Arm A* gives I22 and I34 and tests the pivot. Expect moderate to high hits.
- *Arm B*, the decisive arm, also hides I31–I34.
- *Hit:* a single value-space map, or an equivalent composition, whose pullback grows by positive increments matched to H_k, **plus** an error mechanism that sums E_i rather than √E_i.
- *Partial:* the iteration without the ℓ² mechanism, or a Toro-type scheme that needs Σ√E_i.
- Pivot about 1 (arm A) or about 2 (arm B); chain depth 2.

**P-C2.** Hide I31–I34 and everything downstream.
- *Hit:* the coordinate's Bochner mass in the direction u(x)−u(z) bounded by C r² times a summable defect at x and z.
- Pivot 1 from CJN21 Thm 6.1.

**P-C3.** Hide I20–I22.
- *Hit:* a two-sided comparison of H_k with Id plus the accumulated conjugated masses.

There is no trace, so the pivot distances are estimates from the paper.

## 6. Open questions
- Expert review of correctness, including whether L_n depends only on n.
- Whether experts see C1 as a variant of David–Toro, Semmes, Bonk–Lang or Bishop schemes.
- Run the Colding–Naber Example 2.3 sanity test.
- Repeat the searches in zbMATH, MathOverflow and Scholar.
- Confirm the Breiner–Park relation and check it for AI disclosure.
