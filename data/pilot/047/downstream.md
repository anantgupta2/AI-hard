# Family 047: downstream targets for the witness polynomial H

Analyst role: downstream targets (Lean shortlist). Date: 2026-10-09. Machine-readable version: `downstream.json`.

Item: the witness polynomial
H = x²F − (1+2sx)J − p²J² − pu, with x = s² + u³ + p²F, in ℂ[p,s,u,F,J].
A = P/(H) has A[w] ≅ ℂ^[5] but A ≇ ℂ^[4]. Item type: **witness (F3)**.

All Lean work was done at text level. Nothing was compiled, because there is no local toolchain.

## Part A. Is H in the Lean?

**lean_status: `as in paper`.**
H is literally the witness in the comparator: `ComparatorChallenges/ComplexCancellation.lean:17` is identical to `OAI/Algebra/AffineCancellation/Model.lean:17`. The whole headline theorem is the proved target. Only the route of the hard half differs from the paper.

### Key declarations
`downstream.json → lean_source` records each of these verbatim, with file and line.

| Declaration | File:line | Role |
|---|---|---|
| `P, p, s, u, F, J, x, H, A, MainStatement` | Model.lean:9–23 | the witness and the target statement |
| `Cylinder.Point`, `Point.equation` | CylinderShift.lean:12–23 | H as an identity on points of any ring |
| `Cylinder.Point.shift` | CylinderShift.lean:37 | the finite exp(wΔ) shift |
| `Cylinder.equivalence` | Cylinder.lean:181 | the explicit isomorphism A[w] ≃ ℂ^[5] |
| `Degeneration.relation`, `identity` | Degeneration.lean:10–14 | H_top = H + pu, and xy − z(z+1) = p²·H_top |
| `Determinant.v` | Determinant.lean:40 | v = a³b − a²u³ − d² on the SL₂ torsor |
| `Bundle.inclusion_f`, `inclusion_g`, `certificate` | Bundle.lean:76/79/82 | the principalization certificate, I·T = (v) |
| `Rees.positive_invariant_of_polynomial` | PositiveInvariant.lean:111 | if A ≅ ℂ⁴, an LND of gr A kills an element of positive degree |
| `PolynomialTorsor.exists_equivariant_lift` | EquivariantLift.lean:10 | the lift to the torsor |
| `Bundle.no_positive_invariant` | PositiveObstruction.lean:21 | the rigidity obstruction |
| `nonpolynomiality`, `main`, `stabilization` | Main.lean:9/31, Dimension.lean:42 | the targets |

### Comparator chain
- `main` = ⟨finiteType, domain, dimension, stabilization, nonpolynomiality⟩.
- **Stabilization:** stabilization → Cylinder.equivalence → decode/encode → Point.shift_equation → Point.equation (that is, H).
- **Non-polynomiality:** nonpolynomiality → Rees.positive_invariant_of_polynomial (on G = P/(H_top)) → exists_equivariant_lift → Bundle.pullback (certificate, v) → GradedLND.highest → no_positive_invariant → rigidity.
- **H is in the closure of the target signature.** Every branch above concerns H or its top-weight form.

### Gaps between the paper and the Lean
- **The obstruction takes a different route.**
  - It uses a Rees algebra in place of the ord_p valuation.
  - It works with a possibly non-homogeneous LND.
  - The lift to the torsor goes through a rational slice, a Bézout SL₂-frame and a replica, with no Picard groups.
  - The last step of rigidity uses sl₂ highest weight.
- **Domain and dimension** are read off the cylinder isomorphism.
- **The corollaries are not formalized:** the Stable Coordinate Conjecture (SCC) in ambient dimension 5, and Dolgachev–Weisfeiler.
- **H appears in the formal goal**, so Test 2 must be judged against the problem as originally posed.

## The in-release reuse in family 049: design, not theorem

Only **one** manuscript in the release reuses H: family 049's Oct-5 paper, *A stable coordinate that is not a coordinate in four variables*.
- The 049 Sep-24 paper uses an unrelated design: a cusp relation plus a critical-point obstruction.
- No other preprint cites 047.
- No other Lean directory imports `OAI.Algebra.AffineCancellation`.
- 049's Lean (118 files, 15,542 lines) re-formalizes everything from Mathlib alone. 047's Lean is 55 files and 5,573 lines.

What changed between 047 and 049:

| | 047 | 049 |
|---|---|---|
| x | s² + u³ + p²F | s² − u² + pF |
| H | x²F − (1+2sx)J − p²J² − **pu** | x²F − (1+2sx)J − **p**J² − **u** |
| quadric identity | xy − z(z+1) = p²(H + pu): twist p³u | xy − z(z+1) = p(H + u): twist pu |
| A = P/(H) | **not** ℂ^[4] (the point) | **is** ℂ^[4], via a new determinant-1 matrix change that needs the quadratic u-term |
| target | A itself | the distinguished element p: a 1-stable coordinate, not a coordinate |
| gr | R[τ, I/τ²] | B[τ, I/τ], with the same quadric xy = z(z+1) |
| torsor generator | v = a³b − a²u³ − d² | v = a³b + a²u² − d², on the same SL₂ ring ac − bd = 1 |
| rigidity | Mason–Stothers + "−u³ is not a square" | factorization (au − d)(au + d), with no abc |

**Verdict: this is design reuse, not theorem reuse.**
- 047's theorem gives SCC failure only in ambient dimension 5. 049's dimension-4 result does not follow from it, and 049's A is polynomial anyway.
- 049 says it "adapts the construction in [Cancellation2026, Sections 2–6]".
- What carries over:
  - the template: a Danielewski-type twist of the SL₂/T quadric, written as a residual coordinate in k[p,s,u,F,J];
  - the obstruction pipeline (novelty items C2–C4).

**Caveats.**
- The same producer made 049 twelve days later, citing 047. That shows the design transfers, not that it is easy to find.
- The transfer needed one new idea, the matrix change.
- What is reused is the whole package, never H verbatim.

## Part B. Targets

### Speedup targets (known theorems)

| # | Target | Lean | Speedup | Note |
|---|---|---|---|---|
| S1 | 049 `principal_package` (SCC in 4 variables) | statable now; formal baseline of 15,542 lines | high on paper; medium in Lean as-is, because 047's lemmas are not parametrized | **design reuse** |
| S2 | Russell cubic ≇ ℂ³ (Makar-Limanov 1996) | statable now; no formal proof exists | low–medium | only the generic LND infrastructure helps |
| S3 | Danielewski surfaces: equal cylinders, not isomorphic | statable now | low–medium | infrastructure |
| S4 | First Vénéreau polynomial is a 1-stable coordinate and a hyperplane | statable now (049's `IsOneStableCoordinate`) | medium, stabilization half only | sub-route |
| S5 | 047 over ℚ | statable now | trivial | a corollary; a harness sanity check only |

### Open problems (details, URLs and Lean feasibility are in the JSON)

| Problem | Status | Match | Confidence | Lean |
|---|---|---|---|---|
| **Parametric reach of the H-design** (m, j, φ) | new | exact design | 0.5 | statable now |
| ZCP over ℂ for n ≥ 5 (047's own remark: dimension 4 does not propagate upward) | open | design plus extra variables | 0.25 | statable now |
| **First Vénéreau polynomial a coordinate?** (Lewis 2013, arXiv:1007.2230) | open | exactly 049's situation | 0.15 | statable now |
| Makar-Limanov invariant of the 047 fourfold, and the dimension-4 ML characterization | open | same witness | 0.3 | < 300 lines (define ML) |
| Dubouloz–Ghosh cylinders ≅ A^{n+1}? (arXiv:2501.09613) | open | cylinder half | 0.15 | statable now |
| Koras–Russell cubic × A¹ ≅ A⁴? (arXiv:0807.4085) | open | cylinder half, weak | 0.05 | statable now |
| ZCP over ℂ in dimension 3 | open | design needs dim ≥ 4 | 0.05 | statable now |
| Abhyankar–Sathaye in A³ | open | weak (SCC is true in 3 variables) | 0.03 | statable now |
| Is X biholomorphic to ℂ⁴? | open | same witness | 0.15 | needs a major library |

**Theorem corollaries** (not counted as reuse):
- SCC in ambient dimension 5;
- Dolgachev–Weisfeiler in relative dimension 3 over A¹ and A²;
- the same result over ℚ or any field of characteristic 0.

**Negative controls.**
1. **049's own A_049 ≅ ℂ^[4]** (`polynomialPresentation`). This is the same template giving a polynomial ring, a proved-false analogue that is already formalized.
2. Cancellation for surfaces (Fujita; Miyanishi–Sugie).
3. Lewis: the second Vénéreau polynomial **is** a coordinate.
4. SCC in 3 variables is true.

## Top 5 (Lean-usable first)

1. **049 SCC in four variables.**
   - It is the only measured case where the design is known to transfer.
   - The comparator exists, and 049's own proof gives a baseline (15,542 lines with no shared code).
   - Run it with and without 047's library. This mirrors arm D vs arm O of the 047 Test 4.
2. **The parametric design family.**
   - This is the most direct test of whether the design produces further witnesses.
   - One known positive (047) and one known negative (049's A) are in hand.
3. **The first Vénéreau polynomial.**
   - It is the strongest external open target: a Vénéreau-shaped 1-stable coordinate, exactly the shape 049 resolved.
   - The odds are low. Pair it with Lewis's v₂ as a negative control.
4. **ZCP for n ≥ 5.**
   - Dimension 4 does not propagate upward, so this needs the design again.
   - It tests whether the design survives extra variables.
5. **Russell cubic and Danielewski surfaces.**
   - Known and statable, with no formal proofs anywhere.
   - Any speedup credits 047's generic LND infrastructure, not H, so these serve as contrast targets.

## Precedent
- **After 2026-10-06:** no use of the H-design found.
- **Earlier equivalent:** none found. The nearest ancestors are still Asanuma's ring and the affine-fibration route (route, not object), Danielewski twists, and Vénéreau residual coordinates. **No downgrade.**
- **Search limits:** web search was rate-limited for part of the session, and only about 6 queries ran. zbMATH was not queried.
