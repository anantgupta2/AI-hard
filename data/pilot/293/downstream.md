# Downstream report (Lean shortlist): family 293, E1 backward intertwiner

This report has a machine-readable companion, `downstream.json`, which holds the full Lean statements, the verbatim `lean_source`, the sources and the search log.

The item is **E1**, the backward intertwiner across odometer fibers. It has three parts, B16–B18 in the BI paper:
- two-ended log-weights with opposite drift (B16);
- a drift lemma (B17);
- a normalized backward shift `V` in `{S}'` that moves fibers (B18).

Novelty grade: N3 candidate, F3, confidence 0.45.

**How this was checked.** All Lean work was done at **text level**. Comparator runs for 293 are in progress in another process, so I did not run lake, lean or the comparator: concurrent builds collide. Literature claims rest on WebSearch snippets only. WebFetch was not used, because arXiv is blocked.

## Part A: is the item in the Lean?

**lean_status: `as in paper`.** Each object of the paper's construction has a Lean counterpart:

| Paper object | Lean declaration |
|---|---|
| Weights | `residueCorrection` / `halfExponent` (ExplicitWeights.lean:14-17) |
| Opposite residues at the two ends | `plusResidue` / `minusResidue` |
| Drift lemma | `halfExponent_drift` (BackwardWeights.lean:75) |
| Closed-form solution of the recurrence | `rawBackward` |
| Two-ended decay | `rawBackward_decay` (:169) |
| Sup normalization | `backwardBound` / `backwardCoeff` |
| The operator `V` | `backwardOperator` (GlobalOperators.lean:374) |
| `SV = VS` | `forward_backward_commute` (:397) |

`V` is used exactly once on the comparator chain, at `forward_backward_scalar_transitive` (ErgodicTransitivity.lean:203, hypothesis `hV`).

**Comparator chain** (comparator BackwardIntertwiners, target `direct_algebra_corollary`):

```
direct_algebra_corollary → fullClaim_of_mainClaim (generic) ← direct_mainClaim ← forward_transitiveCommutant
  ← forward_backward_scalar_transitive (hV) ← forward_backward_commute ← backwardFiber_intertwines
       ← backwardCoeff_recurrence ← rawBackward_recurrence
  ← backwardOperator_power_nonzero ← backwardCoeff_ae_pos ← backwardBound_ge_one ← rawBackward_bddAbove
       ← rawBackward_decay ← halfExponent_drift ← residueCorrection / halfExponent   (THE ITEM)
  side: ergodic_late_intersection (inverse odometer), fiber_cyclic_orthogonal_order (Domar branch)
```

**Gaps** (the full list is in the JSON):
- **The run_cmd `auxLemmasExt` edits do not matter for E1 targets.**
  - They sit in `BrownMeasure/Model.lean:91` and `IrrationalRotation/Model/Product.lean:116`.
  - A text-level walk of the import closures puts them only in the closures of `IrrationalRotation.Main` and `BrownMeasure.Main`.
  - They are not in BI, which imports only Mathlib. They are also not in `Hyperinvariant.Main` (277 modules, 22,976 lines) or `FiniteFactor.Main` (271 modules, 22,601 lines).
- **The FiniteFactor comparator never says "hyperfinite."** It states a II_1 factor with separable predual and nothing more.
  - This does not matter for E1, because BI's operator is type I.
  - It does matter for the II_1 targets S3 and O3. A hyperfiniteness predicate would cost about 100–200 lines.
- **The drift lemma takes a different route.** Lean proves an eventually-exact drift of ±100 on `goodBase = Z_2 \ Z`. The paper instead uses Borel–Cantelli with an a.e.-finite constant C(x) that is not integrable. The estimates also differ: Lean uses 400√k where the paper uses 4Dk^{1/3}, and the decay rate is e^{-45n} versus e^{-90n}.
- **Lean consumes `V` differently from the paper.** In Lean, `V` enters the descent only through two facts:
  - b_j > 0 a.e.;
  - the coordinate shift `backwardOperator_power_nonzero`.

  The dense-tail-image lemmas (`backwardFiber_tail_closure`, `backwardFiber_denseRange`) are proved but are not on the comparator chain.
- **The baseline size needs care.** The BI chain is linear: 23 files, 5,802 lines. About 2.2k of those lines are structural side results that the comparator does not use.
  - Use the direct route, about 3.6k lines, as the baseline.
  - The E1-specific part is about 430 lines plus about 70 lines where it is used.

### With / without arms (for all BI-based targets)

- **With E1:** Mathlib d13f23b plus these BI files (3,235 lines): `ConvexEnvelope, ConvolutionBounds, CoefficientSupport, WeightSeparation, FiberTails, ExplicitWeights, HaarBase, FiberMaps, BackwardWeights, GlobalOperators, ErgodicTransitivity`.
- **Without E1:** the same files, minus the following:
  1. Delete `BackwardWeights.lean` (247 lines).
  2. Delete every `*backward*` declaration in GlobalOperators, plus `forward_backward_commute` (about 110 lines). Keep `inverseOdometer*` and `odometerMeasurableEquiv`.
  3. Delete these from ErgodicTransitivity (about 95 lines): `backwardOperator_power_nonzero`, `forward_backward_scalar_transitive`, `generated_transitive`, `explicitDirectModel*`, `direct_model`.
  4. Set `residueCorrection := 0` and delete the residue lemmas (76 lines) and `plus/minusResidue`.
- **Never include in either arm:** AlgebraCorollary and OperatorTransport. They contain the theorem itself.

## Part B: targets

### Speedup targets (all Lean-usable; exact statements are in the JSON)

| id | target | statable | expected | note |
|---|---|---|---|---|
| S1 | HSP witness over the **3-adic** odometer. The decomposable form over Z_3 is part of the statement, so BI cannot simply be transported. | now | high | **Calibration only.** It is a close variant. |
| S2 | HSP witness fibred over an **irrational rotation** (Mathlib `AddCircle.ergodic_add_right`). Drift comes from Rokhlin-tower levels with summable error. | now | med | Tests the design rather than the 2-adic bookkeeping. The tower sketch is mine and unverified. |
| S3 | `FiniteFactor.MainTarget` (II_1, no invariant projections) with BI in the library | now (exact challenge text) | low | Skeptical target, since BI is type I. Baseline: 22,601 lines. |
| S4 | Backward-type intertwiner between two bilateral shifts exists ⇔ the ratio sequence is bounded (Shields-type) | now | med | **Plumbing control.** It uses only the recurrence and normalization, with no drift. |

### Open problems

| id | problem | status | E1 match | confidence | Lean |
|---|---|---|---|---|---|
| O1 | **HSP on L^p(Z_2; l^p) ≅ L^p[0,1], 1<p<∞** | Open on reflexive spaces (JOT 2015 snippet) | Exact: E1 does not depend on the Hilbert structure. The fiber criterion and the duality step must be redone. | medium | statable now |
| O2 | HSP/ISP on l^p (atomic) | open | Partial only. The descent needs a non-atomic base (see N3). | low | now |
| O3 | Relative ISP in non-hyperfinite II_1 factors, point-mass Brown measure (Haagerup–Schultz) | open outside R | Architectural only | low | major library |
| O4 | HSP for multiplicity-one bilateral shifts (Atzmon–Sodin; Kérchy–Pearcy withdrawn) | open | E1 provably fails on one fiber (N1) | low | now |
| O5 | HSP for operator-weighted bilateral shifts of finite multiplicity (Hamid–Pearcy 2006) | open | Exact boundary of E1 (N3) | low | now |
| O6 | Bishop operators, Liouville α | open | Same base dynamics, but the fibers are rank one | low | <100 lines |
| O7 | Kérchy 2026: does a shift-type invariant subspace force a hyperinvariant subspace? | open | weak | low | <300 lines |
| O8 | Attainable hyperlattices | open | Non-ergodic base. Component swaps complicate this. | low | <300 lines |

### Negative controls
- **N1, single fiber (θ = id).** A bounded backward solution must be 0, because b grows like e^{10j}. Statable now; about 40–80 lines.
- **N2, unilateral fibers.** The equation at j = 0 forces b_1 = 0, and then V = 0. Statable now; about 30–60 lines.
- **N3, finite base / finite multiplicity.** V^N restricted to a fiber is a backward shift by N inside {S_x}'. It grows without bound and so must vanish. This is consistent with **Lomonosov**: over a finite base S is compact, and every fiber is compact (`forwardFiber_compact`).
  - Lomonosov and the Schauder fixed-point theorem are **not in Mathlib d13f23b** (checked by grep).
  - An atomic infinite base also fails, because there is no recurrence. BI's own `goodBase` removes exactly the integer orbit.
- **N4, quasinilpotent DT-operator.** It does have hyperinvariant subspaces (Dykema–Haagerup 2004). Any II_1 port of E1 must fail here.
- **ISP.** E1 can never produce an ISP counterexample, because S preserves every `L^2(X; K_{≥h})`.

## Theorem corollaries (not reuse)
- The transitive algebra problem is answered negatively.
- The Arveson / Douglas–Pearcy theorems are sharp: there is a transitive algebra that contains an abelian vN algebra of infinite multiplicity and is not dense.
- {S}' is not reflexive.
- The HSP fails for quasinilpotent operators and for C_00 contractions.
- The HSP fails on non-separable spaces too, via S ⊗ 1. This is my inference.
- The result conflicts with Garayev 2026 and Lee 2023.
- **Compression calibration:** the IP route needs a 22,976-line closure for the same FullClaim. With BI in the library, that comparator becomes a one-line corollary. This compression is not reuse.

## Release reuse
No other family uses the design.
- I searched CONTENTS.md, all preprint .tex files and the Lean sources.
- The only "odometer" hits outside BI are Turing-machine counters in `OAI/Computability`.
- Family 288 (hyperreflexivity of vN algebras) is a contrast only.
- Within the family, IP takes the II_1 route and shares no Lean with BI.

## Top 5 (Lean-usable first)
1. **O1, L^p HSP.** The cleanest test of reusing the device on a new theorem:
   - E1 ports unchanged;
   - the infrastructure that does not port is N0 and should be budgeted in both arms;
   - the missing vector-valued L^p duality costs about 0.5–1k lines.
2. **S2, rotation base.** Tests whether the design generalizes beyond residues. Only the tower lemma is new.
3. **S1, 3-adic re-run.** A cheap calibration that measures the size of the variant effect.
4. **S4 together with N1/N2.** Controls that separate plumbing from the opposite-drift idea.
5. **S3, FiniteFactor with BI.** Skeptical; I expect no gain.

## Precedent
No earlier equivalent or post-release use was found.
- **To read by hand:** Hamid–Pearcy 2006, "Hyperinvariant subspaces for some operator-weighted bilateral shifts." I saw only the bibliographic record. BI's S *is* an operator-weighted bilateral shift of infinite multiplicity, so that paper's hypotheses must exclude it.
- **Also seen:** arXiv:2605.23846 (adjacent cross-sections of the commutant). From the snippets, it uses a block-triangular method with no fibration.
