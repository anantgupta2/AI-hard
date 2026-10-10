# Family 357: "Bi-Lipschitz coordinates at every regular RCD point" (family analyst)

Source: `preprints/Bi-Lipschitz-Coordinates-at-Regular-Points-of-Noncollapsed-RCD-Spaces-September-25-2026/build/source/` at commit fd4aeeb. The paper has five files (paper.tex, introduction, coordinates, pinching, renormalization), 3,468 lines in all, and every line was read. Machine-readable version: `family.json`, with 49 items and a paper DAG.

**No Lean formalization and no reasoning trace exist**, so the Lean sections of the brief are skipped and there is no trust surface. The whole weight rests on the unrefereed LaTeX.

## Main statement
**Thm 1.1** (introduction.tex:17–32). For every n ≥ 2 there is a constant L_n with the following property. Let X be a noncollapsed RCD(K,n) space (measure exactly Hⁿ), and let p ∈ X be a point where every pointed GH tangent is ℝⁿ. Then some open U ∋ p admits a homeomorphism F onto an open V ⊂ ℝⁿ with L_n⁻¹d ≤ |F(x)−F(z)| ≤ L_n d, where d is the **ambient** distance. L_n depends only on n; U depends on X and p.

**Cor 1.2.** There is an open set of full measure containing every regular point, with a countable L_n-bi-Lipschitz atlas.

**Catalogue mismatch.** CONTENTS.md:8665 and overview.tex:812 say the chart has "a point-dependent finite constant". The paper claims a constant that depends only on n. The catalogue's version is weaker.

## Labels
| Axis | Label | Evidence |
|---|---|---|
| A | **A2** (∀p regular ∃U,F). L_n depends only on n but is not explicit; no explicit rate | introduction.tex:23–25 |
| B | **B1**. Resolves the conjecture recalled in HZ26 §1.2, which goes back to CC97 Rem 5.15. Not "full only with prior results". The paper claims no other corollaries (see the note below) | paper.tex:44–45; introduction.tex:93–95 |
| C | **C1** primary (F = lim hᵢ∘u). Secondaries: C2 (scale iteration), C4 (estimation chain), C3 (compactness and contradiction), C5 (cited RCD toolkit). **Not computer-assisted** | introduction.tex:215 |
| C2 flags | **ih_strengthened = yes**, template **"carry an extra tracked quantity"**: all-order Gevrey jet bounds and the diagonal quantity bᵢ, also a "uniform/quantitative version" | renormalization.tex:339–350 |
| D | **D3, provisional, low–medium confidence.** It rests on the value-space renormalization (I43 + I47) | introduction.tex:204–206 |
| Provenance | **no.** HZ26 (arXiv 2608.16021), GV25 and DPG18-v3 disclose no AI assistance, and no model-produced precedent turned up | see novelty.md |

**E. Fields.**
- **Problem field:** Differential geometry (MSC 53C23, 53C21, 51F30, 30L05).
- **Lean-dir field:** none.
- **Method fields, all essential:**
  - RCD / metric-measure geometry;
  - nonsmooth calculus (Gigli18, HK00);
  - elliptic PDE and potential theory on metric-measure spaces (Kell13, Jiang14, AH18);
  - heat kernels (JLZ16);
  - matrix analysis, re-proved;
  - Gevrey/majorant real analysis, re-proved;
  - Euclidean harmonic functions, re-proved;
  - invariance of domain (Hatcher).
- **Method fields, background-cited:**
  - Reifenberg/GMT (DT12, GV25);
  - optimal-transport foundations;
  - Ricci-limit structure theory (CJN21, CN15 and others, named as antecedents).
- **Invoked cited theorems from outside geometric analysis:** 2 of 13 strictly (HK00, Hatcher), or 5 of 13 if the heat-kernel and Poisson-regularity papers count as PDE.
- CM20 is in the bib but is never cited.

**Unclaimed implication (analyst note).** The singular set of a noncollapsed space has codimension ≥ 2. Cor 1.2 would therefore answer **Naber's Open Problem 2.2** (arXiv 2010.10031, "bi-Lipschitz to a manifold away from codimension two?") in local-chart form. It would also give a (non-harmonic) bi-Lipschitz chart at the special point of the Colding–Naber example (Naber Ex. 2.3), where harmonic and distance coordinates provably fail. The paper does not mention either.

## Proof architecture
1. **Rescale at p.** Bishop–Gromov together with density ≤ 1 makes every ball near p, at every small scale, δ-Euclidean. Take harmonic coordinates u.
2. **Normalize at every centre and scale.** Use R_i(y)^{-1/2}. The mean Gram matrices vary slowly (2^{2a|i−j|}) but **may degenerate** as i → ∞, and the normalized Bochner mass is o(1). u is an open homeomorphism.
3. **Heat Gram matrices.** Q_i = P_{r_i²}(χG) + λr_i² is monotone, and H_i = Q_i⁻¹ increases, possibly without bound. A non-commutative cumulative comparison gives Id + ΣZ_i ≍ H_k ≍ Id + ΣS_i for the **mass forms** D_{i,y} = R⁻¹[r^{2−n}M(B_{Lr}(y))]R⁻¹ (I20–I22).
4. **Summable defects.** Poisson replacements of d²/2 have defects P_i whose sum telescopes *exactly* to ω_n − A(16S) = o(1). Smoothing them gives E_i, and radial invariance holds with error √E_i.
5. **Directional pinching** (I34): D_{i,y}[u(x)−u(z)] ≤ C r_i²(E_i(x)+E_i(z)). It is proved from three lemmas:
   - a two-centre commutator: f^z − f^x is harmonic, approximately affine, with coefficient ≈ U(x)−U(z);
   - radial transport, which keeps the defect squared;
   - a sharp projection, linear in s, proved by compactness and the rigidity of the Euler operator X·∇ − 1.
6. **Field in value space.** v_i = Σ φ_{i,y} D_{i,y}(P − c_{i,y}), with patch centres chosen to nearly minimize E_i (I40, I41). Its value is O(√(εE) r), its derivative is S_i + e, and its diagonal error is √(ZE).
7. **Iteration** h_{i+1} = h_i + (Dh_i)^{-T} v_i.
   - The inverse transpose turns Dv into a positive metric increment 2S_i. The only first-order error is ⟨D²h(ξ,ξ), J^{-T}v⟩.
   - The ℓ² recurrence b_{i+1} ≤ b_i/2 + C(√Z[ξ] + √E q_i) gives Σb_i² ≲ H_k[ξ]. Cauchy–Schwarz then sums the errors with ΣE_i alone, never with Σ√E_i.
   - Gevrey jet bounds in all orders absorb the derivative lost at each step.
   - Result: |J_kξ|² ≍ H_k[ξ].
8. **Conclude.** F = lim h_i∘u converges with tail τr_i. For a pair at distance t, take r_i ≈ Dt and apply Taylor's formula inside the central ellipsoid, plus separation; this gives bi-Lipschitz with L_n = 4√A(n). Invariance of domain makes the image open.

Paper DAG: 46 items lie on the path to the theorem. Down/cone shares are: I47 0.07/0.91, I43 0.13/0.65, I34 0.17/0.61, I22 0.30/0.37, I20 0.35/0.33. The chain is linear, so the down-share proxy penalizes the decisive late items, as it did for 287.

## Eureka candidates (quick literature check only)
1. **Value-space renormalization (I43 + I47, with I41). Provisional N3, F5 (F3 secondary).**
   - *For:* the iteration converts a first-order Gram drift that need not be summable into a metric realized by a single map. The ℓ² diagonal recurrence is exactly where the classical bi-Hölder barrier (Σ√E_i = ∞) is crossed. Nothing like it appears in the goal or in L.
   - *Against:* Toro 1995 and David–Toro (cited) already show that square-summable errors suffice, extrinsically. Nash's iterations add positive metric increments step by step while controlling derivative loss. The J^{-T} update is a natural gradient/Newton step. Gevrey majorants are classical.
2. **Directional pinching (I34, with I31–I33). N2.** It is a close variant of the sharp splitting in CJN21 Thm 6.1 / Prop 6.4, where the L² Hessian of a splitting map is bounded *linearly* by pinching at spanning points. A Breiner–Park 2025 analogue also exists, and the paper names CJN21 and CC96 itself.
3. **The mass forms D_{i,y} and their cumulative comparison (I22). N2, F1.** D_{i,y} is the normalized Bochner energy of the normalized coordinates, re-read on the value space (CJN21, CN15, HZ26 Thm 3.8).
4. **Non-commutative inverse increments (I20). N2.** This is CJN21 §8 telescoping without commutativity.
5. **Radial transport lemma (I32). Weak N2.** It is a weighted radial energy estimate.

The remaining items are N0 or N1:
- the summable Poisson defects come from classical volume telescoping (N0);
- the measure-data L¹ gradient bound is Boccardo–Gallouët-type (N0);
- the Gevrey inverse majorant is N0;
- the transformation-type normalization is N1.

## Correctness audit
**I found no gap in the parts I traced.** These were Sections 3.3–3.4 and 5 line by line, and the structure of 2, 3.1–3.2 and 4.2–4.4.

Checks passed:
- uniform flatness near p;
- exact telescoping of P_i;
- the sign condition for the radial-transport cutoff;
- the Euler-operator rigidity in the sharp projection;
- the inverse-increment identity;
- both metric-step identities;
- the diagonal recurrence, including its homogeneity, and the error sums;
- the jet step;
- δ_m → 0;
- the final Taylor/tail/separation arithmetic.

"Proves too much" checks also pass:
- The chart is non-harmonic. This is consistent with Honda–Sire/Otsu–Shioya and with the Colding–Naber Example 2.3, where harmonic charts fail.
- The paper claims no regularity of the metric tensor, consistent with CN13 Thm 1.2.
- Noncollapsing is used essentially, through density ≤ 1 and volume telescoping. This is consistent with the collapsed counterexamples of HNW25.

Residual concerns:
- **This is an extraordinary claim**: it resolves a question going back to CC97 and, without saying so, Naber's Open Problem 2.2. It is unrefereed and has no Lean.
- RCD technicalities are delegated to citations with sketch-level justification: capacity representatives against singular Bochner measures, and the measure Laplacian of d² at the centre.
- Many uniform constants come from compactness arguments over infinitely many scales.
- The claim "L_n depends only on n" is asserted rather than re-derived, and the catalogue disagrees with it.
- The symbol γ is reused with different values in §3 (1/2) and §4 (1/8).

## Extraction friction
- Every core object is a bare display: R, Q, H, N, F, D, Z, S, P, E, v, h and b.
- Only one `\emph` is a definition.
- Symbols are heavily overloaded: E, D, A, a, γ, s and L.
- The `co:` labels span §2–3.
- Key identities are buried in proofs.
- There is no Lean or trace, so load-bearing shares come from a hand-built DAG.
