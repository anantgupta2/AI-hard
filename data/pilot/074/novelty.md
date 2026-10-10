# Family 074: Kakeya in three and four dimensions (novelty pass)

**Date:** 2026-10-10, influential-problems pass. The work is at text level only: there is no Lean and no reasoning trace.

> **Shortlist status.** 074 is **excluded from the Lean eureka shortlist because it has no Lean formalization, not on merit.** Its N3 item (C1) goes on `data/eureka_informal.json`, as PLAN decided on 2026-10-10.

## Provenance verdict: **partial**

- **M2 uses M1 as an input** (strict flag = yes). M2 (Hausdorff dimension in ℝ⁴, 24 Sept) cites the model-produced M1 (ℝ³ maximal, 23 Sept) as "Lemma 2.3", the weighted full-time plank estimate. M2 uses it in its reduction, its initial horizon bound and its scalar tools.
  - That lemma is only an N1 weighted wrapper of GWZ Thm 1.1, so no candidate inherits novelty from it.
  - The locator does not match M1's compiled numbering, where the lemma is 3.3.
- **Parallel model work:** M1 cites model-produced 077 (sphere restriction) as an "independent route". Sibling 079 (local smoothing) also implies M1's theorem. That makes three model routes to the same theorem in one release.
- **No AI disclosure found:** no 2025–2026 human reference shows one in search snippets. arXiv abstract pages could not be fetched (DNS/proxy), so every quote below is snippet-level and unverified.
- **No model-produced Kakeya work found outside the release.**

## Final grades

| ID | Candidate (paper items) | Final N | F | Conf. | Decisive reason |
|---|---|---|---|---|---|
| **C1** | M2 quadratic charts / true packets / known atlases + horizon H(E) (M2-04/05/06) | **N3** | **F1** | 0.30 | No equivalent object found; non-analytic; carries 100% of M2's core. Nearest is Guth's remark that WZ might extend with semialgebraic sets in place of convex sets. |
| C2 | Deformed critical inequality: profile F, cost Π_F, plank exponent A, h(p,z) (M1-05/06/07) | N2 | – | 0.65 | Templated IH strengthening (add a parameter + tracked quantity). WZ already runs two-parameter assertions D(σ,ω), E(σ,ω) (Lean-eval snippet). |
| C3 | Derivative capture at a BV differentiability point of h (M1-11/17) | N2 | – | 0.55 | Envelope-theorem logic (Milgrom–Segal 2002), so transfer. Recorded as a **new bridge**. |
| C4 | Degree restoration via the hidden coordinate, conic case (M2-15) | N2 | – | 0.50 | Terminal repair of the paper's own degree-2 class, so test 3 is borderline. The kernel lemma is classical apolarity. |
| C5 | Two-parameter coordinate-entropy function H(c,a) in moving frames + two-frame projection constraints (M1-24/26/27) | N2 | – | 0.65 | Self-named precedents: Hochman–Shmerkin; SW/OSW pinning. |
| C6 | Canonical profile β(κ−τ)₊ via minimum delay; flat delay (M1-21/23) | N2 | – | 0.65 | Stickiness / ε-linear profile paradigm. |
| C7 | Two-color matching for scalar sheets (M2-07/08/09) | N2 | – | 0.65 | Christ's method of refinements is named. |
| C8 | Horizontal (Heisenberg/SL₂) model + three-leg switch at 2k=1 (M2-18/19) | N2 | – | 0.60 | The model is the known Katz–Zahl / Katz–Wu–Zahl / Fässler–Orponen enemy. |
| C9 | Isotropic polynomial field and conservativity by switching (M2-13) | N2 | – | 0.55 | Polynomial method plus switching. |

**family_D = D3 (provisional, confidence 0.3).** It rests on C1 alone; every M1 item grades N2.

It falls to D2 if any of the following holds:
1. an expert judges the charts to be the semialgebraic-grain generalization Guth already suggested;
2. test 4 shows high hit rates in the directed arm;
3. M2 has a gap.

## What 074 adds beyond Wang–Zahl, and how much transfers

| | M1 (ℝ³ maximal) | M2 (ℝ⁴ dimension) |
|---|---|---|
| New result | The λ³ shading dependence that WZ left open (WZ have λ^{K(ε)}) | Full Hausdorff dimension in ℝ⁴. The previous best was 3.059 (Katz–Zahl) and 3.054 for the maximal form (Borges et al.). The ℝ⁴ maximal conjecture is not claimed. |
| WZ/GWZ used as | Black box: GWZ Thm 1.1 (N0) | Black box: the ℝ³ set theorem on projected lines (via M1, then GWZ); the WZ-sticky planar dot-product theorem (N0) |
| WZ template reused | Worst-case exponent and induction on scales (C2, C6: N2); KLT planiness and graininess re-derived (N0/N2) | Worst-case exponent (the horizon, critical paths: N2) |
| Sticky/planebrush/grains machinery re-run? | No | No. Planebrush, polynomial Wolff and HRZ are context only. |
| New devices | C2, C3, C5, C6, all N2 after grading | C1 (N3), plus C4, C7, C8, C9 (N2) |

## Precedent checks (summary)

- **GWZ 2601.14411 (Jan 2026)** is an essential input to both papers.
  - Trust caveat, snippet-level: Cohen's NYU notes say "There are some technical issues in Section 5".
  - Hua–Yang arXiv 2608.18870 v2 is titled "a Repair", and v3 "a Conditional Repair", of the streamlined ℝ³ reduction. The conditional fix depends on GWZ Lemma 9.1 plus an interface (I1)–(I4).
  - A Zenodo note (Zeraoulia) lists "technical corrections".
- **WZ 2502.17655** is the key human precedent. It caps C2 and C6 at N2.
- **079 (sibling, one day later):** it answers 079's open question. M1 does have a two-parameter entropy function, but **no** excess potential with zero boundary trace and no characteristic-path transport, so 079's C1 is not in 074 in the same form.
- **Unconfirmed:**
  - Wang–Zakharov arXiv 2609.22035, cited by M2, was not found in three searches.
  - The content of Hua–Yang 2608.18693, "Profile-Stable Buffered Multiplicity Factoring in Four Dimensions" (Aug 2026), could not be read. It could bear on C1.
- **Rios–Sawyer 2506.21315:** v1 claimed the ℝ³ maximal conjecture; v4 is retitled to an equivalence result. This is a caution, not a precedent.

## Test details for C1 (the only N3)

| Test | Result |
|---|---|
| Test 1 | Neighbours (none equivalent): Guth's semialgebraic remark (close in spirit); Guth–Zahl / Zahl-Severi quadric neighbourhoods (an obstruction, not a proof object); HRZ multiscale polynomial Wolff; WZ convex grains (convex, not quadric; no hidden coordinate); Wu regulus strips. |
| Test 2 | Pass. Nothing in the goal or in L. |
| Test 3 | Pass by architecture: every M2 section after Sec 2 and the final contradiction are statements about charts, atlases and horizons. |
| Test 4 | Not run; protocol P-C1. Pivot distance: unknown (no trace); about two steps from L. Chain depth: medium (pays off only with C7 and the critical paths). |

## Bridges

| Bridge | Status |
|---|---|
| Envelope / BV → worst-case exponent (C3) | **New bridge** |
| ODS multiplicative convolutions → Kakeya planar rigidity | New bridge (weak evidence) |
| Information theory → Kakeya | Known route |
| Furstenberg → Kakeya | Known route |
| Real algebraic geometry → Kakeya | Known route |
| BSG → Kakeya | Known route |
| Christ refinements → Kakeya | Known route |
| Heisenberg geometry → Kakeya | Known route |

## Discoverability protocol (text level; not run)

**Models:** training cutoff before 2026-09-23. Canary probe on 074/077/079 and on the Hua–Yang papers. The OpenAI lineage that produced the release is an uncontrolled reference arm only. No browsing.

**Context L:** the invoked theorems, as statements.

**Arms:**
- open;
- directed (framework sections up to the hidden item);
- reference.

**Sampling:** n=128, pass@k for k=1…128.

**Judging:**
- two LLM judges plus a human harmonic analyst;
- positive control: PHP extension variables;
- negative controls: the weighted GWZ lemma and the maximal reduction.

**C1 hit criterion:** the proposal must give a nested, mass-floored proof object made of line pieces on which one degree-≤2 polynomial in (t,y,w) is small, together with an extremal time-cost (horizon) whose positivity follows from a Hausdorff deficit. Semialgebraic grains without a hidden coordinate or a time cost count as a partial hit.

**Downstream speedup:** not testable in Lean. Informally: would charts give the ℝ⁴ maximal conjecture or ℝ⁵?

## Correctness and trust concerns

- Neither proof is refereed or formalized.
- My spot checks on M1 pass: validity at A=d−1, the λ^{p+1}→λ³ conversion, closure cases 1–2 by hand, and the BV critical-point logic.
- M2 was read only about 15% line by line. Its jump from 3.059 to 4 is extraordinary.
- Both papers inherit any GWZ issue. WZ 2502.17655 is a probable fallback for that input, but this was not verified.
