# Family 312: downstream analysis of candidate C1

**Item C1:** index-n partial cylinders P_j, made contractible by descending induction at a fixed coskeletal cutoff q.
- Provisional grade N3, type F3+F2.
- Paper items I19, I25 and I27, with I28 and I34 as the payoff.

**Paper:** *The Grothendieck homotopy hypothesis via elementary expansions* (OpenAI, Sep 24 2026). Its comparator target is `OAI.Grothendieck.elementary_expansion`, which is Henry's pushout conjecture.

**Method.** Everything here was done at text level on fd4aeeb.
- No `lake build` or comparator was run, because the checkout is shared. The release Lean is trusted as published.
- The dependency chain comes from `data/items/312_lean.json` (fixed extractor), plus reading the Lean by hand.
- The item is not yet in `eureka_shortlist.json`, so there was no `lean_decls` hint.
- arxiv.org was blocked, so all external evidence is at snippet level.

## Part A: Is it really in the Lean?

**`lean_status`: formalized, different route.**

The device itself is in the Lean almost word for word:
- `cylinderNode` is `CylinderNode.stationary` for j < n, `CylinderNode.critical` (P_n = D_{n+1}) at n, and `completedCylinder` above n. The last is a small-object factorization against the upper I_k with k ≥ n+1.
- Its contractibility comes from the higher-index invariant: `cylinder_oneSided_contractible (hnq : n ≤ q) (H : ExpansionContraction hC q (n+1))`.
- It is load-bearing. `cylinderPathData` dominates **64.8%** of the comparator's 856-declaration proof DAG.

The route differs from the paper's in five places:
- **Different invariant.** The Lean inducts on `ExpansionContraction q r`: a J_{≥r}-cofibration from a cofibrant contractible object has a contractible target. The paper inducts on E(q,n): every J_n pushout is a weak equivalence. In the Lean, a weak equivalence appears only at the last step.
- **No W calculus.** Division, change of boundary and two-out-of-three are not formalized.
- **No trees.** Whiskers plus `free_hasFillers_of_top_homotopy` replace the tree contractibility argument.
- **Stronger joint lifting.** The Lean requires it for all J_k with k ≥ r, proved through `criticalJoint_retract`.
- **Per-object path data.** The Lean picks a non-functorial `CutoffPathData` for each object, with the operations interpreted through `Classical.choose`.

What is not formalized:
- Cor 5.1 (the semi-model structure).
- Cor 5.2 (the homotopy hypothesis itself).
- An instance of `IsCoherator`. None is built, so the library could in principle be vacuous.

### Comparator chain
```
elementary_expansion
 └ cutoff_elementary_exactBoundaryTest                    (dominated share 0.735)
    ├ expansionContraction_all  (strong induction on q−r; _top, _of_paths)
    │   └ cylinderPathData hC q r _ Hnext                  (CutoffExpansion.lean:79)
    └ cylinderPathData hC q n hnq (expansionContraction_all hC q (n+1))   (:99; share 0.648)
        ├ reflectedCylinder → fullCylinder → cylinderRealization/cylinderInterpretation → cylinderFrame
        │   └ cylinderNode → {CylinderNode.stationary, CylinderNode.critical, cylinderNext → completedCylinder → cylinderFactor}
        ├ reflectedCylinderEndpoint_lifts → fullCylinderEndpoint_liftsBoundary → cylinder_oneSided_split
        │   → cylinder_oneSided_split_high → cylinder_oneSided_contractible   (consumes H)
        └ reflectedCylinder_joint_cells → fullCylinder_joint
```
The verbatim declarations, with file and line, are in `downstream.json` under `lean_source` (15 entries).

## Part B: Targets

### Speedup targets on known theorems
I found no strong speedup target outside the corollary cone.

| # | Target | Expected speedup | Lean feasibility |
|---|---|---|---|
| S1 | Lanari 2020 (JPAA; 1805.00156) Thm 6.5: compositions, identities and inverses on globular cylinders | med | < 300 lines: Lanari's cylinder frame in the OAI `GlobularFrame` language |
| S2 | Nikolaus 2011: model structure on algebraic Kan complexes | low | < 300 lines: Mathlib `SSet`, `KanComplex`, `Coskeletal`; OAI Thomason `KanQuillenModel` |
| S3 | Henry 2016: semi-model structure and homotopy hypothesis for cylinder coherators | low | needs a major new library |
| S4 | Brown–Golasiński / Ara–Métayer: strict ω-groupoids (calibration) | low | needs a major new library |

**S1.** With the device, all of Lanari's operations come from one argument: contractible P(S) plus lifting (I28).
- It holds only at a fixed cutoff q.
- It counts as reuse only if Lanari's cylinder objects are made contractible by the descending bootstrap. If they are made contractible by Thm 1.1 instead, S1 is a corollary.

**S2 and S4.** Both have cheaper existing routes. Nikolaus uses transfer, and the strict case uses an explicit path object.

### Open and new problems
| # | Problem | Status | Match | Lean |
|---|---|---|---|---|
| O1 | Pushout conjecture or homotopy hypothesis for coherators **outside the Ara–Henry arity convention** (generating fillers with dim(S) > j) | open | exact: the convention is used only in the cutoff reflector R_q (02:51-53) | < 300 lines (drop `AdmissiblePair.height`) |
| O2 | Taylor's generalized pushout conjecture (2607.28540, Conj 5.7): monoidal, symmetric monoidal and Picard ∞-groupoids | open | same J-pushout statement; needs an arity-bounded free order | major |
| O3 | Homotopy hypothesis for Batanin–Leinster ω-groupoids | open (2016–18 sources) | via a comparison with coherators, likely O1 | major |
| O4 | Homotopy hypothesis for Brunerie / CaTT type-theoretic groupoids | open (Henry 2018) | whether the coherator meets the arity bound is unverified | major |
| O5 | Folk-type (semi-)model structure on weak ω-categories with ω-weak equivalences | apparently open | partial; 317 shows the device's last step fails when directed | major |
| O6 | Grothendieck–Maltsiniotis (∞,n)-categories | open (unverified) | the groupoidal part above n matches | major |
| O7 | A choice-free or internal pushout lemma | open | the small-object completions are the obstacle | statable now (`#print axioms`) |

### Theorem corollaries (do not count as reuse)
- **Pushout lemma for cutoff ((q+1)-coskeletal) models.** This is an internal lemma of the device. Combined with Henry–Lanari (TAC 39(26)), it should give the homotopy hypothesis for Grothendieck n-groupoids for every n, which includes Lanari's 3-dimensional semi-model structure.
- **A path object at finite cutoff.** This is `cylinderPathData hC q 0`, the device's own n = 0 instance.
- **Cor 5.1 and 5.2**, and coherator independence within the convention.
- **Taylor's Thm 5.8**, in the convention case.

### Release reuse
**Family 317** (Thomason model structures, Sep 25) is an **analogue, not a reuse**.
- It cites 312, and it uses strict right Gray cylinders that are stationary on the old sieve, glued through the pushout universal property. That is classical homotopy rel A.
- It has no contractibility bootstrap and no descending cutoff induction.
- It states: "No result of [OpenAI2026] is a premise of this proof".
- No OAI Lean outside `Globular/` imports the 312 library.

Device-reuse tally: **0**.

### Negative controls
1. **Two-out-of-three for W.** Statable now in the OAI library. The device should give zero speedup.
2. **Proved-false analogue.** The exact-boundary / single-joining-cell test does not detect Street weak equivalences: the inclusion of 0 into 0→1←2 is a counterexample (317 App.). The device's final step needs inverses.
3. **Strict ∞-groupoids.** The pushout lemma is true there, but the homotopy hypothesis is false (products of Eilenberg–Mac Lane spaces). So the device alone does not carry the homotopy hypothesis.

## Top 5 (Lean-usable first)
1. **O1: coherators outside the convention** (< 300 lines). This is the cleanest device-reuse test.
   - Only `exists_cutoff` (share about 0.06) has to change. The cylinders, the `ExpansionContraction` bootstrap and the retract argument are reused unchanged.
   - Measure how much of the DAG survives, and the prover budget with and without the cylinder files.
   - It also settles coherator independence in Maltsiniotis' generality.
2. **S1: Lanari's cylinder operations** (< 300 lines). This is a measurable proof-length reduction on a known partial theorem, compared against `cylinderInterpretation`.
3. **S2: Nikolaus's algebraic Kan complexes** (< 300 lines). A cross-model generality and discoverability test. The expected result is null.
4. **O2: Taylor's generalized pushout conjecture** (major library). It has the highest payoff, but it reduces to O1 unless the theories have an arity-bounded free order.
5. **O4: Brunerie / CaTT groupoids** (major library). A syntactic check of the arity bound decides between a corollary and an instance of O1.

## Precedent
- **Earlier equivalent.** None found at snippet level.
  - Two sources must be read in full before C1 can be upgraded: Lanari 2018 (1809.07923, a 3-dimensional "endofunctor that behaves like a path object") and Taylor, *A Tale of Two Paths* (2609.20860, 8 Sep 2026, a cylinder isomorphic to Lanari's).
  - Henry–Lanari supply only the cutoff ingredient.
  - Taylor 2604.09867 and 2510.22326 induct in the upward direction.
- **After the release.** No use of the device after Oct 6 was found.
- **Downgrade.** None for now.

**Bottom line.** C1 is real and load-bearing in the Lean, but it is tailored to this one conjecture. No downstream speedup has been shown, and the jump is not confirmed. The best experiment is O1.
