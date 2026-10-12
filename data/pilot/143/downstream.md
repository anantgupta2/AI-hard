# Family 143: downstream analysis of E1 (quadratic-fit coordinates)

**Item.** E1 from 143b: the model midpoint `H(λ,κ,r)` of the quadratic profile `λu+κu²/2`, with `P=H_λ`, `Q=H_κ`, `R=P_r`, `S=Q_r`, `G=PS−QR`. It has three parts:
- the global fit, Thm 3.6: `(λ,κ,r) ↦ (H,H_r,r)` is a diffeomorphism onto `{|M|<r, |v|<1}`;
- the transport law, Lemma 3.7: `Pλ_r+Qκ_r=0`, `Dκ=−(R/G)(λ−k)`, `Dλ−κ=(S/G)(λ−k)`;
- the curvature comparison it relies on.

The novelty agent graded it N3 borderline N2, F5, confidence 0.4.

**Method.** This was a text-level analysis only. Other agents share the checkout, so I ran no `lake build` and no comparator. Dependency chains come from closures over the `uses` edges in `data/items/143_lean.json`.

## Part A: Is E1 in the Lean?

**lean_status: as in paper.**
- `H,P,Q,Hr,R,S,G` are defined verbatim in `QuadraticCoordinates.lean:20-26`.
- The global fit is general. It is spread over these declarations, with `P_pos` and `G_pos` (`RadiusSigns.lean:25`):
  - `fitK`/`fitD` (`GlobalFit.lean:82-85`)
  - `fit_spec` (92)
  - `fit_unique` (99)
  - `fitK_analytic`/`fitD_analytic` (109-132)
- The transport law is `QuinticFit.fit_transport` (`ActualFitTransport.lean:105`). Its proof is the paper's: subtract the model transport (`transport_H`, `transport_Hr`) from the actual one, then solve the 2×2 system with determinant G.

**Gaps:**
1. `fit_transport`, `kappa_width_pos` and the axis curvature bounds are stated only for the quintic profile family (`a : Fin 6 → ℝ`), not for a general smooth φ. The underlying arc layer (`PositiveTransport`, `PositiveFit`) is generic in an analytic Φ, so generalizing is a refactor of about 150 lines. It is not in the release.
2. Lean needs analytic profiles. The paper uses C^∞ profiles.
3. The "diffeomorphism" is not packaged as a single object. It is split over the fit lemmas.
4. The height-zero fit is a separate layer (`AxisFit.lean`, `joint_limits`).

**Comparator chain** (each step is a direct edge):
`main → upper_bound → upper_nonnegative → AxisFlow.matching_isolated_case2 → matchingDelta_zero_bound_of_third → axisKappa_monotone → kappa_monotone_height → QuinticFit.kappa_width_pos → ActualCharacteristic.w_pos → w_deriv → QuinticFit.w_transport → QuinticFit.fit_transport → QuinticFit.spec → QuadraticFit.fit_spec → QuadraticCoordinates.H`.

Cases 3 and 4 also go through H and `fitK_spec`. Case 1 and sharpness do not use E1.

## Part B: Downstream targets

### Key finding: the degree ≤ 4 Lins–de Melo–Pugh bound falls out of the library

Theorem 1.1 gives only ≤2 for degree ≤4. The sharp bound ≤1 (Li–Llibre, JDE 2012, 21 pp; LMP 1977 for n=3) still follows from the family's own lemmas in a few lines:
- When `a5=0`, the flip `F→−F` (`limitCycle_encard_neg`) makes `a3 ≥ 0`. That removes case 2 entirely.
- If `a1 ≥ 0`, case 1 applies (`no_periodic_case1`, or `no_isolated_matching_even`).
- If `a1 < 0`, case 3 applies (`matching_zeros_case3`), and it already bounds *all* zeros by 1.

The proof closure is 827 declarations and 7,746 lines, which is 65% of the main proof DAG. Of that, 165 declarations (1,438 lines) depend on H.

What it uses and does not use:
- **Uses:** E1's crossing lemma (`matchingDelta_zero_bound`: κ₊>κ₋ at zeros ⇒ Δ'>0, because `v̂_κ=G/P>0`) and the fitted-curvature range.
- **Does not use:** `fit_transport` or the model inequality (E2).

143b does not mention this consequence. It is a real reuse on an OTHER theorem, with two caveats:
- it stays in the same class of systems, so it is in-distribution;
- it exercises only the global-fit half of E1.

To attribute the speedup to E1, run an ablation:
- **Arm B:** remove AxisCases/UpperAssembly, so the prover must rebuild case 3 from E1.
- **Arm C:** remove the fit layer.

### Speedup targets

| # | Target | Lean | Expected speedup | Confidence |
|---|---|---|---|---|
| 1 | LMP n≤4: ≤1 cycle (Li–Llibre 2012; LMP 1977) | statable now; ~40–80 lines of glue | high (but half the device, in-distribution) | 0.8 |
| 2 | Zhang Zhifen uniqueness, g=x (F'(x)/x monotone ⇔ φ₊''≥0≥φ₋'') | statable now; deg≤5 proof ~100–200 lines; any degree needs de-quinticizing (46 files) | med | 0.6 |
| 3 | Rychkov-type two-cycle criteria (Zhang's generalization; Holst–Sundberg): the only target that uses the full device (transport + E2) | statable now; needs general-Φ `fit_transport`/`kappa_width_pos` (~300–600 lines) | med if hypotheses match, else low | 0.35 |
| 4 | van der Pol uniqueness for all μ | statable now; upper bound is an instance of #1; existence for small μ via the SharpCycles template | low | 0.8 (upper bound) |
| 5 | Generalized Liénard y'=−g(x): Zhang for general g; Dumortier–Li H(2,2)=1 | under 300 lines of new definitions; the plumbing is g=x-specific (major refactor) | med / low | 0.5 / 0.2 |

The Filippov change of variables `u=G(x)` gives the same arc equation `du/dy=φ(u)−y`. So H, the fit, the transport law and E2 carry over verbatim to target 5. Only the matching plumbing and the shape checks change.

### Open problems (all low confidence)

- **Odd-F LMP in degree 7 (≤3).** Status is open or contested; a claimed proof by "Chen and Chen" is unverified. This needs k-parameter polynomial-fit coordinates. It is the right test of whether E1 is a template.
- **H(6) for classical Liénard.** At least 4 cycles are known (DMD 2011). The common even part gains a u³ term, so a cubic fit would be needed.
- **Smale's 13th problem / polynomial growth of H(n).** This would need a sign-change-counting version of the device.
- **Generalized Liénard H(m,n) beyond the solved small cases.** Examples include a cubic restoring force with quintic F.
- **Multiplicity and hyperbolicity companion to the quintic bound.** This may be routine.
- **Piecewise-linear Liénard with n≥5 pieces (CLZZ 2026).** It would need a measure-valued curvature-range lemma. Lean requires analytic profiles, so this needs a major new library.
- **Uniqueness criteria for Gause-type predator–prey systems.** A "fitted-curvature separation" criterion might be weaker than Zhang's pointwise f/g monotonicity.

### Theorem corollaries (not counted as reuse)

- Rychkov 1975 (odd quintic F).
- The bound ≤2 for degree ≤4, which is weaker than the known ≤1.
- The Hernández Rosales refutation.
- The upper-bound halves of Odani 1996 Example 3 and of Gasull–Giacomini–Grau 2017.
- Li–Lu 2014 slow–fast cyclicity.
- The paper's own general-profile propositions, which are within-paper generalizations.

### Negative controls

- **Degree 6 and 7 (LMP is false there; DMD 2011, DPR 2007).** The shape hypotheses must fail on the explicit counterexample F. This is a concrete sanity check.
- **Abel equations and rigid systems (Lins Neto 1980: unboundedly many solutions).** They have no two-half-arc matching structure, so the device does not apply. No strong candidate was found.
- **Generalized Liénard with nonlinear g, above the Huzak–De Maesschalck lower bounds.** Any E1-based bound must stay above those known lower bounds.

### Release reuse

None. No other family deals with Liénard systems, limit cycles or planar vector fields, and no Lean file outside LienardCycles imports this code.

## Precedent

No earlier equivalent was found, so precedent gives no downgrade.
- The method template is still osculating elements / variation of parameters.
- Classical Filippov half-orbit comparisons (Zhang, Coppel, Dumortier–Li) do not fit models in data space.
- arXiv:2409.04024 compares divergence integrals over half-arcs, which is a different mechanism (seen only as a search snippet).
- I could not read Li–Llibre's method (ddd.uab.cat DNS failure).
- I found no post-Oct-6 use of the device; arXiv:2610.13080 did not appear in search.

All literature statements come from search snippets and are unverified: arxiv.org is blocked and WebFetch failed.
