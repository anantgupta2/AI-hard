# Family 358: "A three-manifold without conjugate points or nonpositive curvature" (paper + Lean)

Sources:
- Paper: `preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/build/`, commit fd4aeeb. It has 6 sections plus an appendix and about 70 KB of LaTeX.
- Lean: `lean/OAI/Geometry/ConjugatePoints`. It has 19 files, 24,974 lines and 2,179 declarations, with no docstrings.
- Comparator: `lean/ComparatorChallenges/ConjugatePoints.{json,lean}`.

Full data, including 34 paper items and 10 Lean-only items, is in `family.json`. There is no reasoning trace for this family.

## Main statement
**Thm main** (introduction.tex:27-29): there is a closed, connected, orientable smooth 3-manifold M with a C^∞ metric without conjugate points, such that M admits no C^∞ metric of nonpositive sectional curvature.

M is a two-piece graph manifold. Two copies of Σ₁,₁ × S¹ are glued by h₂ = h₁ + f₁ and f₂ = h₁; the gluing matrix [[1,1],[1,0]] has det −1. The result answers Ivanov–Kapovitch Q1.1/Q8.1 and Burns–Matveev Q4.1.2 negatively. The paper also claims three stronger facts:
- π₁(M) has no proper cocompact CAT(0) action.
- M has no locally CAT(0) length metric.
- Via IK Thm 7.1, M has no metric without focal points.

**Comparator** (`OAI.ThreeManifold.main_theorem`, `MainStatement`) asks for:
- ∃ M: compact, connected, T2, second countable, with E3 charts, C^∞, and an oriented atlas;
- ∧ ∃ g with `NoConjugatePoints g`;
- ∧ ¬∃ g with `NonpositiveSectionalCurvature g`.

How the comparator was checked:
- Its 18 definitions are textually identical to `Basic.lean`.
- I checked by hand that the coordinate curvature has the correct sign: g(R(u,v)v,u) ≤ 0.
- `NoConjugatePoints` covers every open interval, including constant and non-unit-speed geodesics.
- **The comparator matches Thm main exactly.**
- The general-CAT(0) theorem, the locally-CAT(0) corollary and the focal-point remark are *not* formalized; `lean/docs/358.md` says so.

**Trust surface:**
- 0 `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque` or `set_option`.
- 23 kernel `decide` calls. They cover fixed 2×2 integer-matrix identities, membership in SL(2,ℤ/2) and SL(2,ℤ/3), and ℕ side conditions. None of them is a search.
- The only import is `import Mathlib`.
- Lean was not built here.

## Labels
- **A2.** The headline is a counterexample (∃M), and one of its conjuncts is an impossibility (¬∃ NPC metric). Confidence high.
- **B2.** It refutes the implication "no conjugate points ⇒ some NPC metric", without relying on prior results.
  - Flag "adds corollaries": yes (CAT(0) actions, no-focal-points).
  - It does **not** settle IK's specific test case Q8.2 (|tr A| > 2). In natural conventions the paper's gluing has |trace| = 1.
- **C1** primary (construction of the metric). Secondaries:
  - C4: estimation chain ending in the choice of δ, turning.tex:293.
  - C3: the obstruction is proved by contradiction.
  - C5: flat torus theorem, BH II.6.8, metric Cartan–Hadamard, van Kampen/amalgams.
  - Not computer-assisted.
  - C2 is absent: there is no induction (ih_strengthened = false). The closest analogue is the strengthened local estimate, "arbitrary endpoint values, uniform over passages". If coded as a strengthening it fits the template "uniform/quantitative version".
- **D3, provisional, low confidence.** It rests on one weak N3 item (the returning-passage estimate). It drops to D2 if a judge calls that item N2.
  - Provenance flag: no. All 8 references are classical human works.
- **E.**
  - Problem field: Differential geometry (53C22, 53C20, 53C23, 57K30). Lean-dir field: Geometry.
  - Essential method fields: Riemannian index-form theory, CAT(0) metric geometry, graph-manifold topology, hyperbolic surfaces, matrix analysis (Loewner order), Sobolev/Hilbert duality, ODE, measure theory, and calculus of variations (joint convexity, implicit and uncited).
  - Corollary-only: IK Thm 7.1. Background-cited: Gulliver.
  - Lean-only fields: smooth Cartan–Hadamard and Rauch comparison, covering spaces and π₁, and congruence reductions in SL(2,ℤ).
  - Cross-field share of invoked cited theorems is about 2/3. Most of that material is re-proved inline.

## Proof architecture
1. **Obstruction (N0, Leeb Ex. 4.1, re-proved).** The flat torus theorem gives a common flat for the gluing ℤ². In each piece, h_i is a commutator in C(f_i), so its axis shift vanishes and Pythagoras forces v(h_i) ⊥ v(f_i). The gluing then gives 0 = ⟨u+v, u⟩ = |u|², a contradiction.
2. **Metric.**
   - The neck is g = dt² + dxᵀQ(t)dx with *concave cometric* P = Q⁻¹: P = d₁e₁e₁ᵀ + d₂HHᵀ, with diagonal variation of size δ and a shear of size δ² only on [5/12, 7/12].
   - The torus periods B₁ = δ²B₂ are chosen after δ, so the integral gluing becomes a coordinate swap plus a tiny shear.
   - Convex warped collars lead into hyperbolic cusps of punctured-torus cores. Curvature is ≤ 0 everywhere except the middle of the neck.
3. **Neck identities.** The momentum p is conserved and F = pᵀPp is concave. The intrinsic index is I = E − [⟨T, Γ(V,V)⟩]. Concavity makes the coordinate energy E ≥ 0, and the endpoint Christoffel term is (κ/2)z₁²∂_τ, which is ≥ 0 at every entry and exit.
4. **Easy passages.** The cases are J = ℝ, monotone passages, and returns that stay inside an end collar. A tangential gauge plus Cauchy–Schwarz with F < 1 handles them.
5. **Returning passages (the core).**
   - A gauge gives w(0) = w(L) = 0 with an affine tangential part, which leaves the target |pᵀX|² ≤ L(E + μ(eᵀX)²).
   - Cauchy–Schwarz in L²(Q) ⊕ H₀¹ gives |qᵀX|² ≤ S(q,q)E.
   - The boundary penalty and a Schur complement reduce the problem to S(p,p) − S(p,e)²/(S(e,e) + μ⁻¹) ≤ L.
   - Three bounds close it: S(p,p) ≤ L(1+v₀²), S(e,e) ≤ C_eL, and |S(p,e) − Lp₁| ≤ C_mδL|p₁|. A strict timing margin 4v₀ ≤ βκp₁²L with β = (1+e^{−9/26})/2 < 1 makes the bound uniform in L, v₀ and t\*.
6. **Assembly.** Countable additivity over passages, plus NPC on the complement, gives I_ℝ(V) ≥ 0. The index criterion then gives no conjugate points.

**The Lean proof follows a different route in four places:**
- *No flat torus theorem.* It re-proves smooth Cartan–Hadamard, the Gauss lemma and an NPC Jacobi lower bound. These give a proper CN-inequality metric on E3 on which deck isometries act. A new **cyclic shear obstruction** (Convexity.lean:696) then needs only common minimum points, axes and axis shifts.
- *No van Kampen.* The fibre classes are shown nontrivial because the fibres are closed geodesics of the constructed metric, which has no conjugate points (ThreeManifold.lean:36-70). So the non-NPC half depends on 97% of the DAG.
- *No H₀¹/Riesz.* The S(q,r) argument becomes an explicit pointwise quadratic plus integration by parts (`DirectTurning`, Returning.lean:267-487).
- *Compact windows.* Lean works inside a compact window around the field's support instead of on infinite passages, which adds "truncated returns".

The paper-style Euclidean orthogonality lemmas exist in Lean (Distance.lean:565-583) but are off the proof DAG.

DAG cone shares, as the fraction of the 1,753 target-DAG declarations each item depends on:

| Item | Cone share |
|---|---|
| no-conjugate-points half | 0.77 |
| returning estimate | 0.13 |
| cometric bounds | 0.07 |
| Cartan–Hadamard CN | 0.21 |
| cyclic shear | 0.035 |

## Eureka candidates
1. **P29, the returning-passage estimate (with P24–P28). N3 weak, F2.**
   - *For:* it is a free-endpoint normal-index nonnegativity for every returning geodesic segment through a positively curved neck, uniform in duration and incidence. Nothing like it is in L. It needs three coordinated insights: the boundary term controls only the e-component; S(p,e) must be accurate relative to |p₁|; and there is a strict timing margin.
   - *Against:* every step is elementary (Cauchy–Schwarz, Schur complement, convexity of v). It is a one-off device and will fail the downstream speedup test.
   - *Nearest neighbour:* Gulliver 1975 (radial comparison in a ball) and Riccati/Green-bundle methods. The quick search found no match.
2. **P19/P20, concave cometric ⇒ nonnegative coordinate second variation, with an engineered nonnegative boundary term. N2 leaning N3, F5.**
   - It is the conceptual core: measure the second variation along coordinate-linear variations, where it is a sum of squares.
   - *Against:* it is the classical fact that a Lagrangian jointly convex in (position, velocity) has nonnegative second variation. Partial Legendre duality makes "yᵀQ(t)y convex in (t,y)" the same as "pᵀP(t)p concave in t". This is uncited transfer.
3. **P31, localisation of the index form to neck passages with independent gauges. N2.** It is natural, and measure-theoretically trivial once it has been posed.
4. **P11/P05, the cometric path with δ/δ² scaling and the period trick B₁ = δ²B₂. N2, F3.** Necks between flat tori are standard (Leeb, Buyalo–Svetlov). The specific ordering, concave diagonal first and shear second, is new.
5. **(Lean only) L05/L03, the cyclic shear obstruction and fibre nontriviality via essential closed geodesics. N2.** These are lean re-routings of Kapovich–Leeb and Hadamard–Cartan.

Everything in the topological half is N0.

## Correctness
**I found no gap.** I re-derived:
- the end germs and frame change;
- the cutoff identities: a(0) = e^{−3/2}, a(1/8)/a(0) = e^{−9/26}, and a² ≤ −a';
- the coordinate-energy formula, via Q′ and Q″;
- the boundary Christoffel sign;
- the turning identity, chord and timing bounds;
- all three S-bounds and the final δ-choice (it matches Lean's `SmallParameter`);
- the orthogonality contradiction;
- the comparator's curvature sign.

Lean's `actual_loop_relations` encode exactly f₂ = h₁ and h₂ = h₁f₁. Consistency checks also pass: Green's scalar-curvature bound, IK centralizer splitting, Dibble's abelian-subgroup theorem, and the presence of focal points (forced by IK Thm 7.1).

Residual concerns:
- The intro's mention of IK's punctured-torus gluings could be read as resolving Q8.2, but the gluing here is not that test case (|tr A| > 2).
- The Lean build was not run.
- Burns–Matveev Q4.1.2 was not re-read.
- A quick search (2026-10-09) found no prior resolution. Tchuiaga 2025 is a rigidity preprint for closed Σ × S¹ and is unrelated.

## Extraction friction
- Lean has zero docstrings. Its namespaces are `ThreeManifold.*`.
- The load-bearing paper objects (E, S, Φ_q, D, μ, β, the gauge) appear only in display math. The only `\emph` definitions are "no conjugate points", "no focal points", "cometric" and "neck passage".
- The four route differences mean that paper Section 2 has almost no Lean counterpart by name.
- The extractor's `dominated_share` is uninformative here because the two halves are coupled. Cone share is more useful.
- The extractor's candidate_defs list is led by plumbing that pulls metrics back through charts.
- 426 declarations are off the DAG, including an abandoned paper-style route.
- Useful cue phrases:
  - "instance of Leeb's ... obstruction" (N0)
  - "We include the group-theoretic proof" (re-proved)
  - "This is what permits one metric to handle every complete geodesic" (candidate)

Sources (quick literature check): [Ivanov–Kapovitch, arXiv 1205.4455](https://ar5iv.arxiv.org/html/1205.4455); [Dibble, arXiv 1811.10095](https://arxiv.org/abs/1811.10095); [Gulliver 1975, TAMS](https://www.ams.org/journals/tran/1975-210-00/S0002-9947-1975-0383294-0/); [Tchuiaga, arXiv 2504.07616](https://arxiv.org/html/2504.07616v2); [Leeb, dg-ga/9410002](https://arxiv.org/abs/dg-ga/9410002).
