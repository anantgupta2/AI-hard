# F1 downstream-use report: family 248, recursive Hilbert-ball colouring (`recursive_coloring`)

Machine-readable companion: `f1_recursive_coloring.json`. Analyst grade under test: I19 (and its pullback I23), provisional **N3, F1**.

## Verdict

**What holds up**
- No earlier equivalent of the device was found, so **N3 stands**.
- The device does transfer, but narrowly.
- Within group theory, every group whose structure the device needs seems to **contain F**. Brin's ubiquity criterion is met automatically by scale-changing pair transports.

**Where the payoff comes from**
- New *open-problem* payoff comes almost entirely from the **theorem**: T is C\*-simple, Moore's Ramsey statement fails, p_c<p_u, Dixmier for F, and so on. It does not come from reusing the **definition**.
- Reuse of the definition itself is strongest in three areas:
  1. explicit quantitative isoperimetric and spectral bounds for F;
  2. uniform elementary nonamenability proofs for Thompson-like and piecewise-projective groups;
  3. explicit finite witnesses: a Moore Ramsey counterexample and an explicit fixed-point-free convex compact F-space.
- I found no strong candidate *outside* group theory.
- The item is **not yet a confirmed eureka step**. The speedup tests S1–S4 below are the measurable next step.

## 1. The item

**Definition** (finite-proof.tex:124-138; Lean `partitionColor`, RecursiveColoring.lean:23):
- **Setting:** f is an L-Lipschitz self-map of the unit ball B of a Hilbert space with ‖f(x)−x‖ ≥ δ. Benyamini–Sternfeld; the paper builds one on L²([0,1];ℝ²) with δ=1/2.
- **Parameters:** D > 4L²/δ², and separated internal dyadic intervals I_1<…<I_D.
- **Recursion:** for a basic dyadic partition T,

  p(T) = f( (1/D) Σ_j p(T_{I_j}) ) if T respects every I_j, and 0 otherwise.

  Here T_I is the restriction renormalised to [0,1]. The recursion is well founded on the cell count.
- **Pullback to F:** X_I(g) = p((gT^(n))_I) over the parents I_i and descendants I_i·I_j. The level n is chosen *after* the test set A.
- **Two exact facts drive everything:**
  - (T_I)_J = T_{I·J}, which gives the recursive identity X_{I_i} = f(z_i), where z_i is the mean of the descendant colours;
  - covariance ((hg)T^(n))_{I'} = (gT^(n))_I when h maps I affinely onto I'.

**Obstruction dissolved.** Følner invariance controls only averages of *bounded* functions.
- The natural contradiction is unbounded: depth or cell count strictly drops under restriction, yet transports make restrictions at different scales equidistributed.
- Bounded scalar (indeed any finite-dimensional) recursions have fixed points (Brouwer), so they can stabilise. This is why Moore's scalar colourings, Akhmedov's heights and Moore's Følner-function recursion (tower bounds only) do not close the problem.
- The recursion is also nonlinear, so first moments say nothing.

The device fixes both problems:
- *bounded but non-stabilising* values, via a fixed-point-free Lipschitz f, which exists only in infinite dimension;
- *second-moment* control: approximately equal pair correlations make the child means z_i concentrate at the parent mean m (variance ≤ 4/D+4η). So m = mean f(z_i) ≈ f(m), a contradiction.

**Abstract mechanism.** *Recursively aggregate a vector-valued colouring of self-similar configurations through a Lipschitz map with no approximate fixed points; approximate invariance under a fixed finite set of scale-changing, pair-independent transports forces pair-exchangeability, hence concentration, hence an approximate fixed point.*

Applicability needs four conditions:
- (a) self-similar restriction (T_I)_J=T_{I·J};
- (b) a well-founded size that drops under restriction;
- (c) configurations that can be made **fine on any finite cell family** by refinement chosen after A;
- (d) a **fixed** finite set of **scale-changing** transports placing any separated pair onto a reference pair, with exact covariance.

Amenable examples fail these conditions:
- IETs and the release's own polygon-exchange group (family 253) are translation-only, so they fail (d);
- automaton groups preserve levels, so they fail (d);
- F acting on k-point configurations, whose stabilisers are co-amenable, fails (c).

This is a useful consistency ("proves too much") check.

## 2. Candidates (11; details, sketches and confidence in JSON)

| id | problem | status | kind | payoff | conf. |
|---|---|---|---|---|---|
| C1 | Explicit Følner constant for {x0,x1}; ‖x0+x0⁻¹+x1+x1⁻¹‖<4; cogrowth<16; Guba density<4 | open (only numerics / lower bounds) | device, quantitative | new bound, about δ⁴/L⁴, polynomial not tower | high |
| C2 | Uniform elementary nonamenability: F_n, Stein, F_τ, Lodha–Moore, Monod H(A), rearrangement / cloning / forest-skein groups | known or by containment of F | device, re-derivation | simplifies proofs (no Carrière–Ghys) | high |
| C3 | Moore's convex Ramsey statement for binary trees (equivalent to amenability of F) | now false, but no explicit witness | device, explicit witness | explicit counterexample | medium |
| C4 | Explicit fixed-point-free convex compact F-space (Monod's method "fails precisely for F"); nonlinear Day theorem | open (explicit construction) | device, structural | new construction | low-med |
| C5 | Co-amenability / Schreier-graph amenability in F, T, V | scattered | device, speculative | partial | low |
| C6 | Uniform non-amenability of F (ABLRSV) | open | device, speculative | likely negative | low |
| C7 | Brin–Sapir: subgroups of PL₊(I) are elementary amenable or contain F | open | **delineation**: the device cannot reach F-less groups | none | high (that it fails) |
| C8 | IET amenability; polygon exchanges (253); polynomial-activity automata | open | **negative control**: no scale change | none | high (that it fails) |
| C9 | Jones / Brothier tree-functor technology (exactness, weak amenability, forest-skein groups) | open | speculative cousin | conceptual | low |
| C10 | Theorem corollaries: T C\*-simple (Le Boudec–Matte Bon); non-Liouville for all measures; p_c<p_u (214); Dixmier (251); Moore Ramsey fails; groups containing F | resolved if the theorem holds | **theorem, not definition** | not counted | — |
| C11 | Abstract criterion "(a)-(d) ⇒ nonamenable" (the Lean core is already generic in G) | template | abstraction | reusable, but no known new example | medium/low |

**Release reuse.**
- No family uses the device. The grep over all .tex files finds Benyamini–Sternfeld only in 248.
- Families 214 and 251 consume the *theorem* (corollaries in consequences.tex).
- Family 253 is the mirror image. Almost-invariant random polygonal partitions exist there because its exchanges are translations. The device explains why the analogous construction must fail for F.
- Family 328 (Kirk's problem, nonexpansive maps) is compatible: B–S maps have L>1. There is no reuse.

## 3. Speedup targets (held-out)

| id | theorem | current proof | how the device helps |
|---|---|---|---|
| S1 | Monod's H(A) (A≠ℤ) and Γ_S are nonamenable | PNAS 2013, 4 pp. + Carrière–Ghys (deep ergodic theory); Monod 2023 elementary route about 8 pp.; none in Mathlib | F = H_Q(ℤ) ⊂ Γ_S gives a few lines; or run the device on Farey cells |
| S2 | Lodha–Moore G_0 is nonamenable | about 2 pp. + Monod + Carrière–Ghys | F ⊂ G_0, or run the device directly |
| S3 | F_n, F_{2,3}, F_τ are nonamenable | embeddings + the F proof | **Best Lean test:** port the 68 files to n-adic cells; the generic core (21%) and the B–S map (34%) transfer verbatim, only the plumbing (30%) is redone |
| S4 | Explicit Følner constant for {x0,x1} ⇒ Kesten norm <4 | none (new) | on top of `thompson_F_uniform_boundary` + caret-count word-length bounds |
| S5 | Negative controls: rational-rank ≤2 IET subgroups amenable; F_m (253) amenable; finite-set stabilisers co-amenable in F | 10–40 pp. each | the device must *not* apply; check that its hypotheses fail |
| S6 | T, V are nonamenable | about 1 p. (free subgroups) | no speedup expected (control) |

## 4. Precedent and contamination

**No earlier equivalent was found.** Nearest neighbours, and why none is equivalent:
- **Moore 2013:** finite *scalar* tree colourings with a convex Ramsey property. A reformulation, not a mechanism.
- **Moore, Følner function:** a scalar recursion giving tower bounds. The device is its bounded, non-stabilising upgrade.
- **Akhmedov:** unbounded integer height functions.
- **Monod 2013/2023:** *affine* fixed-point-free spaces, which fail for F.
- **Day / Gheysens–Monod / Barroso–Mbombo–Pestov:** affine fixed-point characterisations.
- **Benyamini–Sternfeld and Lin–Sternfeld:** the map only, with no group-theoretic use.
- **Jones / Brothier–Jones:** Pythagorean representations assign vectors recursively along trees, but through *linear isometries*, to build representations rather than contradictions.

**After 2026-10-06:** no use or reproduction found.
- VibeMathed lists the result as "candidate, review pending".
- Kalai's 2026-10-07 post mentions it without assessment.
- Neither the audit paper arXiv:2608.14673 nor the Lipschitz-action preprint arXiv:2609.25931 is related.

**Caveat:** the theorem itself is unreviewed, on a problem with a history of withdrawn claims. Everything downstream is conditional on it.

## 5. Top 5

1. **C1: explicit spectral and isoperimetric constants.**
   - This is the most direct reuse of the definition itself. The constant c0 is explicit, and the transports have O(D) carets.
   - So the Følner constant for {x0,x1} is roughly δ⁴/L⁴. That is polynomial, not tower-type.
   - This would give the first rigorous separations from 4 (Kesten norm) and 16 (cogrowth), where only numerics exist (Haagerup–Haagerup–Ramirez-Solano; Elvey Price–Guttmann; Guba).
   - It is formalisable on top of Main.lean.
2. **C2: uniform elementary nonamenability for Thompson-like and projective groups.**
   - This is the best held-out family for measuring speedup.
   - It removes Carrière–Ghys from the proofs for H(A) and Lodha–Moore.
   - The Lean core is already generic, so porting cost is measurable.
   - Caveat: novelty is modest, since containment of F already gives the qualitative statements.
3. **C3: explicit counterexample to Moore's convex Ramsey statement.**
   - The correlation functions φ_{I,J} are explicit bounded tree functions that witness failure.
   - Thresholding them should give concrete (m, n, colouring) data. This would be a new finite object coming from the definition.
4. **C4: explicit fixed-point-free convex compact F-space.**
   - Monod (2023) builds such spaces for every piecewise-projective group except F.
   - Lifting the nonlinear obstruction to an affine action on laws of colour families would give the first explicit Day witness for F. Compactness is the risk.
5. **C5: co-amenability inside Thompson groups.**
   - This is the only route by which the *device*, rather than the theorem, could reach new group-theoretic open problems.
   - It is consistent with the known co-amenability of finite-set stabilisers. Low confidence.

## 6. Exact Lean source (verbatim in JSON `lean_source`)

All files are under `data/raw/openai-math/lean/OAI/GroupTheory/Thompson/`.

**Definitions**
- `partitionColor`: def, RecursiveColoring.lean:23. This is the item. It has no declaration docstring; the module docstring at lines 6-11 explains the recursion.
- `partitionFamilyColor`: def, PartitionColorFamily.lean:29.
- `globalColor`: def, GlobalColors.lean:37.
- Support declarations: `UnitBall` (abbrev, UnitBall.lean:9) and `ballMean` (def, HilbertAverage.lean:79).

**Key lemmas** (statements only in the JSON)
- `partitionColor_restrict` (RecursiveColoring.lean:62): the recursive identity.
- `partitionFamilyColor_parent` (PartitionColorFamily.lean:57).
- `globalColor_covariance` (GlobalColors.lean:96): exact covariance.
- `displacement_le_mean_energy` (DisplacementEstimate.lean:23).
- `boundaryConstant_le_of_correlations` (FiniteCorrelationBoundary.lean:56): the generic core, stated for an arbitrary type G.
- `exists_fixed_boundary` (FiniteBoundary.lean:16).

The definition as formalised:

```lean
def partitionColor (I : Fin D → BasicInterval) (hI : ∀ i, (I i).Internal)
    (hD : 0 < D) (f : UnitBall E → UnitBall E) (T : BasicPartition) :
    UnitBall E := by
  classical
  exact if h : ∀ i, T.Respects (I i) then
    f (ballMean hD (fun i =>
      partitionColor I hI hD f (T.restrict (I i) (h i))))
  else unitBallZero E
termination_by T.cellCount
decreasing_by
  exact T.restrict_cellCount_lt _ _ (hI _)
```
