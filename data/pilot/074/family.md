# Family 074: Kakeya in three and four dimensions (family analysis)

**Pass:** influential-problems pass, 2026-10-10. **Source:** `openai/math` @ `fd4aeeb`. **Analyst role:** family (paper) analyst. There is no Lean, so the Lean parts are skipped.

> **Shortlist status.** 074 is **excluded from the Lean eureka shortlist because it has no Lean formalization**: the catalog lean flag is False and there is no `lean/docs/074.md`. The exclusion is **not** a judgment on merit. Under PLAN (decided 2026-10-10), any N3 item from this family goes on the informal list `data/eureka_informal.json`.

| | M1 | M2 |
|---|---|---|
| Title | The Kakeya maximal conjecture in three dimensions | Every four-dimensional Kakeya set has full Hausdorff dimension |
| Date | 2026-09-23 | 2026-09-24 |
| Size | 7,446 lines in 11 sections; 24 bib entries | 14,184 lines in 11 sections; 34 bib entries |
| Read line-by-line | ~40%, plus every statement | ~15%, plus all 82 statements |

File/line references use the form `M1 <file>:<lines>`, which means `<manuscript dir>/build/sections/<file>`.

## 1. Main statements

**M1** (`introduction.tex:17-26`): for every ε>0, ‖K_δ f‖_{L³(S²)} ≤ C_ε δ^{-ε} ‖f‖_{L³(ℝ³)}. This is the full three-dimensional Kakeya maximal conjecture.

**M2** (`01-introduction.tex:8-15`): every K ⊂ ℝ⁴ that contains a unit segment in every direction has dim_H K = 4. No measurability or compactness is assumed.

### What 074 adds beyond Wang–Zahl

- **Wang–Zahl (2025), and the GWZ streamlined proof (2026),** proved the ℝ³ set conjecture for Hausdorff and Minkowski dimension. Their shading dependence is λ^{K(ε)}, and the λ³ dependence the maximal conjecture needs was left open. M1 says this explicitly (intro:59-64).
- **M1 adds the maximal form in ℝ³.**
  - It uses the GWZ union estimate (Thm 1.1: convex clustering ≤ δ^{-η}, density λ ≥ δ^η) as a **black box**.
  - All the low-density machinery is new to M1: the temporal deficit profile, the cost Π_F, the deformed critical exponent h(p,z), derivative capture, flat delay, the canonical profile, the moving-frame entropy rates, product-slope pinning, and the five-case closure.
  - Wang–Zahl's sticky reduction and grain decomposition are **not** re-run. KLT planiness and graininess are re-derived locally, from multilinear Kakeya plus GWZ. Stickiness survives only as the self-reproducing canonical profile, an N2 analogue.
- **M2 claims full dimension in ℝ⁴.** The previous bests were:
  - Hausdorff: 3.059 (Katz–Zahl planebrush, corrected v3);
  - maximal parameter: 3.0543 (Borges et al. 2511.22824);
  - polynomial Wolff: 3+1/40;
  - sticky sets: 13/4 (Rai Choudhuri).

  M2 does **not** prove the ℝ⁴ maximal conjecture. Its engine is new, and none of the planebrush, polynomial-Wolff or HRZ arguments is invoked. Its only Wang–Zahl-family inputs are:
  - the ℝ³ set theorem, through M1's weighted plank lemma applied to projected lines;
  - the planar dot-product theorem from the sticky paper.

## 2. Trust surface

- There is no Lean. A grep for sorry/axiom/admit/native_decide/extern/unsafe finds 0 hits.
- Neither paper is computer-assisted.
- There is no reasoning trace.
- Trust rests on 21.6k lines of unrefereed LaTeX.

## 3. Labels

- **A: A3 (M1), A1 (M2).** M1 is a sharp-up-to-ε quantitative inequality whose C_ε is not explicit. M2 is a universal qualitative statement.
- **B: B1 for both.**
  - Corollaries: Nikodym maximal estimates (ℝ³ and constant-curvature 3-manifolds), curved Kakeya, Minkowski/packing dimension in ℝ⁴, direction sets, and 4D Nikodym dimension. All come through cited transfers (GLX, Keleti–Máthé, Nadjimzadah).
  - The "full only with prior results" flag is false. GWZ is a tool here, not a partial case.
- **C: C3 primary.** Both papers argue by contradiction through extremal exponents.
  - Secondaries: C4 (rate and jet inequality chains), C5 (GWZ, Ren–Wang, BCT/Guth, Carbery–Valdimarsson, WZ-sticky dot products, ODS, BSG, AFP), C1 (gadgets) and C2 (induction on scales).
  - **ih_strengthened = yes.** The template is "add a parameter" plus "carry an extra tracked quantity": M1 proves a deformed family h(p,z) with a free plank exponent A and a tracked profile F, in order to get h(p,0)=0.
    - This coding departs from the 079 analyst's convention and is flagged in the JSON.
  - Computer-assisted: no.
- **D: D3, provisional and low confidence** (see §5). The flag "builds on a prior model-produced result" is **yes, within the family**: M2 cites M1 "Lemma 2.3" as an input.
- **E (fields):**
  - Problem field: Real and complex analysis (MSC 42B25, 28A75, 28A78).
  - Lean-dir field: none.
  - Essential method fields: Kakeya / multilinear Kakeya; projection theory and incidence geometry (Ren–Wang, SW/OSW); information theory; BV real analysis (AFP Thm 3.83); real algebraic geometry plus Bernstein–Remez; additive combinatorics (BSG, Plünnecke); Fourier decay of multiplicative convolutions (ODS); classical tensor and conic algebra.
  - Corollary-only: curved Kakeya / Riemannian.
  - Background-cited: OpenAISphere2026 (family 077).

## 4. Proof architecture

**M1**
1. Build an indexed weighted model of tubes, with time-bin shadings and full-time plank masses.
2. Deform the density target into critical inequalities m ≤exp N^{A+Π_F(1)} Δ_A. The temporal cost Π_F records how the shading deficit is spread over log-scales. The goal is h(p,0)=0 for p↓2, which gives the theorem through the maximal reduction.
3. If h(p,0)>0, the function h−z is separately monotone, hence BV. That gives a point of total differentiability with h>0 and h_z>0. Build hybrid and exact equality sequences there.
4. Local geometry of equality configurations:
   - a local mass bound;
   - planiness on short blocks (multilinear Kakeya);
   - plate density (Ren–Wang) plus the plate Nikodym L² bound give a **flat delay** τ>0;
   - saturated plates (GWZ) plus anisotropic rescaling give a positive deficit.
5. **Derivative capture** selects the saturated shapes. A **minimum-delay** argument with inner and outer cuts forces the canonical profile F=β(κ−τ)₊. The resulting stationary packets carry four coordinates (X,Y,U,V) in moving frames.
6. The entropy demand of the stationary masses is set against projection constraints from two frames on one index:
   - the shear matrix, whose mixed term Δt·Δϑ needs product-slope pinning;
   - mutual information between the actual joint law and the product law.

   A five-case closure then gives h(p,0)=0.

**M2**
1. From dim_H K<4, build a version-2 exact problem in the cap class C(d), d<1, with positive **horizon** H(E). This step uses the ℝ³ set theorem on projected lines.
2. Prove a scalar-sheet comparison (two-color matching, an alternating-path Jacobian argument; Christ's method of refinements is the named analogue). It gives terminal time extension and a critical time rate k>0. Optimize d_*, k and the narrowness ℓ into critical paths.
3. ℓ=0: isotropic improvement (polynomial field, conservativity, potential), plus **degree restoration** when the directions lie near a conic.
4. 0<ℓ<∞: scalar projection gives either wide intervals or a horizontal Heisenberg-type model Y′=−Z+tv. At 2k=1, a three-leg switch closes it. At 2k≠1, a bootstrap returns to wide intervals.
5. ℓ=∞: full-time localization plus scalar projection gives a horizon of 0, a contradiction.

## 5. Eureka candidates (provisional; the final grades are in novelty.md)

| Rank | Item | Prov. N | F | For | Against |
|---|---|---|---|---|---|
| 1 | M2-15 degree restoration through the hidden coordinate (seven-direction tensor kernels; the conic case) | N3 cand. | F5 | Defeats the quadric/conic configuration inside the isotropic branch. Nothing similar is in L. | Its kernel lemma is classical apolarity. It may be forced once charts are fixed at degree 2, which would make it a one-off device. |
| 2 | M1-06/11/17 deformed critical exponent h(p,z) with cost Π_F, and derivative capture at a BV differentiability point | N3 cand. (borderline N2) | F2 | This is what turns λ^{K(ε)} into λ³. No Kakeya precedent was found for differentiating a worst-case exponent. | Matches WZ's two-parameter assertions D(σ,ω)/E(σ,ω), the "add a parameter" template and the envelope theorem (transfer). |
| 3 | M2-04/05 quadratic charts and the horizon functional | N3 cand. (borderline N2) | F1 | The new extension object of M2. | Guth's outline of WZ suggests semialgebraic replacements for convex sets. Relatives: Guth–Zahl quadric obstruction; Wu regulus strips. |
| 4 | M1-26/27 two-parameter coordinate-entropy function in moving frames, and two-frame projection constraints | N2 (borderline N3) | – | The analogue of sibling 079's C1 (N3, 0.3). | The paper names Hochman–Shmerkin. Pinning is adapted from SW/OSW. x+tv slicing is classical. |
| 5 | M2-08 two-color matching | N2 | – | Used in every regime. | Christ's refinements are named. |

**Bridges** (detail in novelty.md):

| Bridge | Status |
|---|---|
| Information theory → Kakeya (entropy rates) | Known route |
| BV / envelope logic → induction on scales | New bridge, no precedent found |
| Real algebraic geometry → Kakeya | Known route (polynomial method) |
| Additive combinatorics → Kakeya | Known route (Bourgain, Katz–Tao) |

## 6. Correctness and trust concerns

1. **Spot checks on M1 pass.** I checked:
   - validity at A=d−1;
   - the conversion from density exponents to the maximal bound (λ^{p+1} → λ³, loss δ^{-(p-2)/3});
   - closure cases 1 and 2, by hand;
   - the logic of the BV critical-point lemma.

   The M2 reduction from Hausdorff covers is standard and plausible. About 9k lines of M2's three narrowness branches were read only at statement level.
2. **Dependence on GWZ 2601.14411 Thm 1.1 (both manuscripts).** Public signals of problems are snippet-level and unverified:
   - Cohen's NYU notes say "There are some technical issues in Section 5".
   - Hua–Yang (arXiv 2608.18870) changed title from "a Repair" to "a **Conditional** Repair of the Streamlined Three-Dimensional Kakeya Reduction".
   - A Zenodo note lists "technical corrections".

   The original Wang–Zahl 2502.17655 probably supplies the input, but its hypotheses were not matched against M1's convex-clustering form.
3. **Provenance:** M2 uses model-produced M1 as an input, through "Lemma 2.3", a thin wrapper of GWZ. In M1's compiled order that lemma is **3.3**, a locator mismatch that suggests the sections were reordered.
4. **Three model routes to the same ℝ³ maximal theorem** exist in one release: M1, 077 (restriction) and 079 (local smoothing). None is independently verified.
5. **Earlier human claim:** Rios–Sawyer 2506.21315 v1 claimed the ℝ³ maximal conjecture and was later retitled to an equivalence result.
6. **Unconfirmed citation:** M2 cites Wang–Zakharov arXiv 2609.22035 (18 Sept 2026), which no search confirmed.
7. **Size of the M2 jump:** M2 goes from 3.059 to 4 in one paper.

## 7. Extraction friction

- M1's section files are reordered: 10-critical is input before 05-inputs.
- Key objects are inline (Π_F, Δ_A, T, the X,Y,U,V forms, H(c,a), and M2's chart, true and horizon notions).
- Symbols are overloaded: H, d, k and η each carry more than one meaning.
- PDFs are absent, so compiled numbers were inferred from source order.
