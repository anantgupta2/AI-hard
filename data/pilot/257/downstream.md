# Family 257: downstream targets for the eureka item

**Item:** Doubled-Fano gadget with its all-CAT(0) finite obstruction (P03+P47), plus the uniform conditional test (P37), for a hyperbolic group without a geometric CAT(0) action (type F3 (gadget + finite obstruction, a witness design) / F5 (uniform conditional test, a lemma)).

*Text-level analysis; the Lean was not compiled. Web tools hit a session quota during this pass, so outside references marked [unverified] or [memory] need checking.*

**Bottom line.** The item is in the Lean and on the comparator path. The comparator gap is exactly two missing clauses: '2-dimensional' and 'no locally CAT(0) finite model'. Both are statement-level omissions that the existing Lean nearly proves (`simplex_card_le_three`; the CAT(−1) clause uses CAT(−1) only through `CATNegOne.catZero` inside `uniformLocalCATZero_of_compact`). No strong *speedup* target was found for the gadget's design. The measurable Lean targets reuse either the gadget itself (O1, O6) or the proof toolkit (S1, S2).

## Part A: is the item in the Lean?

**lean_status: formalized, different route.** All three parts of the item are in the Lean and on the comparator's dependency path (template carrier `Field`/`Edge`, `no_finite_obstruction`, `SamplingSequence.conditional`). The conditional test follows the paper, but the finite obstruction is proved by a shorter algebraic tangent-cone route without the paper's CAT(1) local-geodesic and parallel-set theorems. The comparator is weaker than the paper's Thm 1.1 at the statement level only, and both omitted clauses are within a few dozen lines of what the Lean already proves.

### Gaps between the paper and the Lean

- **Comparator omits '2-dimensional' (paper Thm 1.1: 'finite connected two-dimensional aspherical simplicial complex').** The Lean witness is `finalFiniteComplex m = elementaryFiniteComplex … = toFiniteComplex (elementaryPolygonData …).complex` (IndexedFillingValue.lean:5335, 2950). For the underlying polygon model the Lean already proves `FinitePolygonModel.Data.simplex_card_le_three` (FinitePolygonModel.lean:94): every face has at most 3 vertices, i.e. dimension at most 2. What is missing is only (a) transporting that bound through `toFiniteComplex`, which is a reindexing along `Fintype.equivFin` (IndexedFillingValue.lean:2887) and preserves face cardinalities, (b) one 3-vertex face to get dimension exactly 2 (any `collarFace` of a cell works), and (c) adding the clause to `MainStatement`. Text-level estimate: 20–40 new lines. So the omission is a statement-level choice, not a missing proof.
- **Comparator omits the locally CAT(0) model clause. It excludes only compatible locally CAT(−1) metrics (`CompatibleLocallyCATNegOne`), which is strictly weaker because a locally CAT(−1) metric is locally CAT(0).** The CAT(−1) clause is proved by `homotopy_incompatibleLocalCATNegOne` → `incompatibleLocalCATNegOne_of_noAction` → `not_noGeometricCATZeroAction_of_compact_localCATNegOne` (CompactLocalCATGeometric.lean). The only place CAT(−1) is used is `uniformLocalCATZero_of_compact` (IndexedFillingValue.lean:7037). It applies a Lebesgue number and then `(hc y).catZero` (`CATNegOne.catZero`, IndexedFillingValue.lean:6978) to get `UniformLocalCATZero r`. Everything downstream (the development, deck action, properness and CAT(0)-ness of the developed cover in DevelopmentDeck/DevelopmentProper/DevelopmentGeometricAction/LocalGeodesic) takes only `UniformLocalCATZero r`. A `CompatibleLocallyCATZero L` with `CATZero (ball x r)` in place of `CATNegOne` can therefore be excluded by copying three lemmas and deleting the `.catZero` call: about 30–50 lines. With that, the comparator would imply the paper's statement, since the CAT(−1) exclusion follows from the CAT(0) one.
- **Infinitude dropped from `MainStatement` (`exists_finite_aspherical_hyperbolic_noAction` proves `Infinite π₁`, and `main` discards it with `_`).** Harmless. A finite group acts geometrically on a one-point CAT(0) space, so `NoGeometricCATZeroAction` already forces π₁K to be infinite. This also rules out the trivial-group loophole in `WordHyperbolic`.
- **Different route for the finite obstruction (P47).** Paper Sec 6 uses tangent cones, flat rigidity, antipodality via the CAT(1) local-geodesic theorem, and a splitting of the parallel set of the M_C/M_D axis. The Lean (`no_finite_obstruction`, CATZeroFurther.lean:212) builds the completed tangent cone (`TangentCone.coneData`) and then argues purely algebraically. It uses `fan_identity`, `exceptional_identity`, `ConeData.exceptional_antipodes` ('in an algebraic form that avoids a local-to-global theorem in the completed space of directions', CATZero.lean:463) and `five_line_fans_contradiction`. Same conclusion, shorter proof, no parallel-set theorem.
- **Uniform conditional test: same statement, quantitative and limit forms are split.** Paper P37 (05-energy.tex:246-295) is a limsup statement uniform over actions chosen after the tables. The Lean splits it into the finite quantitative bound `ConeData.conditional_test` (FiniteLaw.lean:111), with explicit coupling errors B·√(1/(n+1)+2M²η)+2BMη, and the limit `SamplingSequence.conditional` (ConditionalStar.lean:147) via `conditional_test_eventually`. Uniformity is expressed structurally: `SamplingSequence` carries only combinatorial data, and `conditional` holds for every later sequence of `EnergyOrbit`s `O`. The displacement bound is M = 8 (paper: generic M). No weakening found.
- **Non-effective, as in the paper.** `finalFinite_noAction` is an `∀ᶠ m in atTop` statement, and `main` uses `.exists`, so no explicit K is produced (the paper says the same, 01:15).
- **Other Lean route differences (not affecting the item).** Asphericity is proved by an explicit contraction of the universal cover (paper: Hurewicz + Whitehead). Infinitude is proved by a six-cell rank count (paper: Euler characteristic). The Lean also proves its own Cartan–Hadamard development and its own 'linear filling ⇒ four-point hyperbolic' (family.md).

### Comparator chain

Main path, from the comparator theorem down to the item:

`OAI.HyperbolicObstruction.main` → `OAI.HyperbolicObstruction.IncidenceTemplate.exists_finite_aspherical_hyperbolic_noAction` → `OAI.HyperbolicObstruction.IncidenceTemplate.finalFinite_noAction` → `OAI.HyperbolicObstruction.IncidenceTemplate.finalDiagramStage_noAction` → `OAI.HyperbolicObstruction.IncidenceTemplate.SamplingStage.eventually_noAction` → `OAI.HyperbolicObstruction.MasterGraph.eventually_noAction` → `OAI.HyperbolicObstruction.MasterGraph.exists_noAction` → `OAI.HyperbolicObstruction.MasterGraph.impossible_sequence` → `OAI.HyperbolicObstruction.CoreGeometry.MetricCore.impossible` → `OAI.HyperbolicObstruction.CoreGeometry.MetricCore.toObstruction` → `OAI.HyperbolicObstruction.no_finite_obstruction` → `OAI.HyperbolicObstruction.ConeData.exceptional_antipodes` → `OAI.HyperbolicObstruction.ConeData.five_line_fans_contradiction`

Side branches that also reach the item:

- Metric core via the conditional test: `MasterGraph.impossible_sequence` → `MasterGraph.metricCore` (GraphLimit.lean:109) → `MasterGraph.path_lower` → `SamplingSequence.limit_path` (OrbitLimit.lean) → `SamplingSequence.word_lower` (ConditionalStar.lean:300) → `SamplingSequence.conditional` (ConditionalStar.lean:147, call at :324) → `ConeData.conditional_test` (FiniteLaw.lean:111) + `conditional_test_eventually` (FiniteLaw.lean:195).
- Exceptional ternary test via the conditional test: `MasterGraph.impossible_sequence` → `MasterGraph.exceptionalTest` (Exceptional.lean) → `SamplingSequence.limit_fractional` (OrbitLimit.lean:159) → `SamplingSequence.fractional_error` (ConditionalStar.lean:409) → `SamplingSequence.conditional` (call at :425).
- Template carrier: the sampling labels are indexed by `IncidenceTemplate.Field = Edge ⊕ (TwoPath × Fin 2)` (Template.lean:36), with `Edge` = all Fano incidences on 11 representatives (A–D doubled) minus (10,4) = Y_D–CD (Template.lean:15). The same omission appears in `CoreGeometry.Adjacent` (MetricHexagon.lean:114), which `MetricCore` and `toObstruction` use. The novelty pass found Edge/Field to be dependencies of 42.7%/40.5% of the patched DAG.
- CAT(−1) clause: `main` → `homotopy_incompatibleLocalCATNegOne` → `incompatibleLocalCATNegOne_of_noAction` → `not_noGeometricCATZeroAction_of_compact_localCATNegOne` → `uniformLocalCATZero_of_compact` + Cartan–Hadamard development. It reuses the no-action conclusion `hno` from the main path.

### Key Lean declarations (verbatim statements in `downstream.json`)

| Declaration | Kind | File:line |
|---|---|---|
| `OAI.HyperbolicObstruction.IncidenceTemplate.Edge` | abbrev | `lean/OAI/Geometry/HyperbolicGroups/Template.lean:15` |
| `OAI.HyperbolicObstruction.IncidenceTemplate.isLoose` | def | `lean/OAI/Geometry/HyperbolicGroups/Template.lean:17` |
| `OAI.HyperbolicObstruction.IncidenceTemplate.fan` | def | `lean/OAI/Geometry/HyperbolicGroups/Template.lean:21` |
| `OAI.HyperbolicObstruction.IncidenceTemplate.card_fan` | lemma | `lean/OAI/Geometry/HyperbolicGroups/Template.lean:26` |
| `OAI.HyperbolicObstruction.IncidenceTemplate.TwoPath` | abbrev | `lean/OAI/Geometry/HyperbolicGroups/Template.lean:31` |
| `OAI.HyperbolicObstruction.IncidenceTemplate.Field` | abbrev | `lean/OAI/Geometry/HyperbolicGroups/Template.lean:36` |
| `OAI.HyperbolicObstruction.IncidenceTemplate.card_fields` | lemma | `lean/OAI/Geometry/HyperbolicGroups/Template.lean:40` |
| `OAI.HyperbolicObstruction.IncidenceTemplate.vector` | def | `lean/OAI/Geometry/HyperbolicGroups/MetricHexagon.lean:96` |
| `OAI.HyperbolicObstruction.IncidenceTemplate.Incident` | def | `lean/OAI/Geometry/HyperbolicGroups/MetricHexagon.lean:100` |
| `OAI.HyperbolicObstruction.CoreGeometry.Adjacent` | def | `lean/OAI/Geometry/HyperbolicGroups/MetricHexagon.lean:114` |
| `OAI.HyperbolicObstruction.CoreGeometry.MetricCore` | structure | `lean/OAI/Geometry/HyperbolicGroups/MetricHexagon.lean:238` |
| `OAI.HyperbolicObstruction.CoreGeometry.ExceptionalTest` | def | `lean/OAI/Geometry/HyperbolicGroups/MetricHexagon.lean:367` |
| `OAI.HyperbolicObstruction.CoreGeometry.MetricCore.impossible` | theorem | `lean/OAI/Geometry/HyperbolicGroups/MetricHexagon.lean:409` |
| `OAI.HyperbolicObstruction.fullLines` | def | `lean/OAI/Geometry/HyperbolicGroups/CATZeroFurther.lean:182` |
| `OAI.HyperbolicObstruction.FiniteObstructionData` | structure | `lean/OAI/Geometry/HyperbolicGroups/CATZeroFurther.lean:189` |
| `OAI.HyperbolicObstruction.no_finite_obstruction` | theorem | `lean/OAI/Geometry/HyperbolicGroups/CATZeroFurther.lean:212` |
| `OAI.HyperbolicObstruction.TangentCone.fan_identity` | theorem | `lean/OAI/Geometry/HyperbolicGroups/CATZeroFurther.lean:57` |
| `OAI.HyperbolicObstruction.TangentCone.exceptional_identity` | theorem | `lean/OAI/Geometry/HyperbolicGroups/CATZeroFurther.lean:86` |
| `OAI.HyperbolicObstruction.ConeData.exceptional_antipodes` | theorem | `lean/OAI/Geometry/HyperbolicGroups/CATZero.lean:465` |
| `OAI.HyperbolicObstruction.ConeData.five_line_fans_contradiction` | theorem | `lean/OAI/Geometry/HyperbolicGroups/CATZero.lean:646` |
| `OAI.HyperbolicObstruction.ConditionalStar` | def | `lean/OAI/Geometry/HyperbolicGroups/ConditionalStar.lean:53` |
| `OAI.HyperbolicObstruction.SamplingSequence` | structure | `lean/OAI/Geometry/HyperbolicGroups/ConditionalStar.lean:73` |
| `OAI.HyperbolicObstruction.EnergyOrbit` | structure | `lean/OAI/Geometry/HyperbolicGroups/ConditionalStar.lean:88` |
| `OAI.HyperbolicObstruction.SamplingSequence.conditional` | theorem | `lean/OAI/Geometry/HyperbolicGroups/ConditionalStar.lean:147` |
| `OAI.HyperbolicObstruction.ConeData.conditional_test` | theorem | `lean/OAI/Geometry/HyperbolicGroups/FiniteLaw.lean:111` |
| `OAI.HyperbolicObstruction.conditional_test_eventually` | theorem | `lean/OAI/Geometry/HyperbolicGroups/FiniteLaw.lean:195` |
| `OAI.HyperbolicObstruction.IncidenceTemplate.exists_finite_aspherical_hyperbolic_noAction` | theorem | `lean/OAI/Geometry/HyperbolicGroups/IndexedFillingValue.lean:6747` |
| `OAI.HyperbolicObstruction.UniformLocalCATZero` | def | `lean/OAI/Geometry/HyperbolicGroups/IndexedFillingValue.lean:7034` |
| `OAI.HyperbolicObstruction.uniformLocalCATZero_of_compact` | lemma | `lean/OAI/Geometry/HyperbolicGroups/IndexedFillingValue.lean:7037` |
| `OAI.HyperbolicObstruction.FinitePolygonModel.Data.simplex_card_le_three` | lemma | `lean/OAI/Geometry/HyperbolicGroups/FinitePolygonModel.lean:94` |
| `OAI.HyperbolicObstruction.incompatibleLocalCATNegOne_of_noAction` | lemma | `lean/OAI/Geometry/HyperbolicGroups/CompactLocalCATGeometric.lean:38` |
| `OAI.HyperbolicObstruction.MainStatement` | def | `lean/OAI/Geometry/HyperbolicGroups/Basic.lean:145` |

## Part B: where to try the item

### Speedup targets (known theorems)

#### S1. Flat-triangle / CN-equality propagation in CAT(0) spaces (Bridson–Haefliger II.2.9 in CN form)
- **Statement:** In a CAT(0) space, if equality holds in the CN (comparison) inequality for a point z and the segment [x,y] at one interior parameter t₀ ∈ (0,1), then it holds for every t ∈ [0,1]. Equivalently, the comparison triangle of (z,x,y) is flat (BH II.2.9, Flat Triangle Lemma).
- **Reference:** Bridson–Haefliger, Metric Spaces of Non-positive Curvature (1999), Prop. II.2.9 (flat triangle lemma); BH II.2.11 for the flat quadrilateral version.
- **Status:** known (textbook)
- **Current proof size:** about 1 page in BH (via Alexandrov's lemma and angle comparison). No Mathlib formalization; Mathlib has no CAT(0) spaces. OAI has the cone-level ingredients: `TangentCone.cn_eq_of_log_dist` (CATZeroFurther.lean:44) and `log_dist_of_interior_equality` / `log_dist_of_midpoint_equality` (TangentCone/ConeData files).
- **How the item helps:** The obstruction proof's toolkit (`exceptional_identity`, `fan_identity`) does exactly this kind of propagation. From one CN equality it derives that `log` is isometric on the pair, and then CN equality along the whole segment (`cn_eq_of_log_dist`). With these in the library the target is a few lines. Caveat: this reuses the P47 proof toolkit, not the doubled-Fano design.
- **Expected speedup:** med in Lean (≈10–30 lines instead of a from-scratch angle theory); low on paper. Confidence: medium (the OAI lemma statements match closely; not compiled).
- **Lean feasibility:** score: **statable now**. Needs: OAI `HyperbolicObstruction.CATZero`, `CATZero.segment`, `CATZero.mid`; Mathlib `dist`, `Set.Icc`. Missing: none. Formal proof to compare: none in Mathlib; OAI's TangentCone lemmas are the nearest formal relatives.

#### S2. Flat quadrilateral theorem, unit-square case (BH II.2.11)
- **Statement:** If four points p,q,r,s of a CAT(0) space have squared sides 1 and squared diagonals 2, then the two diagonal midpoints coincide, and the geodesic quadrilateral spans an isometric copy of the Euclidean unit square (corner-preserving isometric embedding of [0,1]² extending the four points).
- **Reference:** Bridson–Haefliger (1999), Thm II.2.11 (flat quadrilateral theorem).
- **Status:** known (textbook)
- **Current proof size:** about 1 page in BH, using II.2.9 twice. OAI already proves the midpoint part as `CATZero.square_mid` (CATZeroFurther.lean:28; about 10 lines from `CATZero.quadrilateral`).
- **How the item helps:** `fan_identity` turns a metric square plus central flatness into cone-level identities (pairing −1/4, equal `add` sums). The cone `add`/`pairing` calculus (CATZero.lean:218-505) is what one needs to build the flat square from `log`-isometries. Again this is toolkit reuse.
- **Expected speedup:** low–med. Confidence: medium-low.
- **Lean feasibility:** score: **statable now**. Needs: OAI `CATZero`, `MetricSquare` (CATZeroFurther.lean:168); Mathlib `EuclideanSpace ℝ (Fin 2)`, `Isometry`. Missing: none for the corner-isometry form; a geodesic-convex-hull definition (~40 lines) if one wants BH's exact 'convex hull is flat' form. Formal proof to compare: OAI `CATZero.square_mid` (midpoint part only).

#### S3. Fixed points of graph-model random groups for one fixed cocompact CAT(0) target (Izeki–Kondo–Nayatani; Toyoda)
- **Statement:** For a fixed proper geodesically complete CAT(0) space X admitting a proper cocompact isometric action (so δ(X) < 1 by Toyoda), Gromov's graph-model random groups (with suitable expander sequences) have the fixed-point property for isometric actions on X with high probability.
- **Reference:** Izeki–Kondo–Nayatani, Groups Geom. Dyn. 6 (2012), via arXiv 1012.4147 Thm 2.2 (statement verified by subagent); Toyoda, arXiv 1102.0729 (δ<1 for cocompact geodesically complete X) [Kodai 2016 venue unverified]; Izeki–Nayatani, Geom. Dedicata 114 (2005) 147–188 [unverified page range].
- **Status:** known (2005–2016)
- **Current proof size:** Izeki–Nayatani ≈ 40 pp (combinatorial harmonic maps and the δ invariant), IKN ≈ 20–30 pp (random graph model), Toyoda ≈ 15 pp [page counts from memory, unverified]. No formalization anywhere.
- **How the item helps:** The uniform conditional test replaces the target-dependent spectral constant (1−δ(X))μ₁ with a TV-coupling + Sturm inductive-mean argument whose constants do not depend on X. Caveat: P37 as formalized needs an `EnergyOrbit` with an exact energy minimizer and a uniform displacement bound M, which come from cocompactness. IKN conclude fixed points for all isometric actions on X. So the item reaches only the weaker 'no geometric action on X' form unless it is combined with Gromov–Schoen-type scaling limits (an adaptation, not reuse).
- **Expected speedup:** low–med (for the weak 'no geometric action' form only). Confidence: low.
- **Lean feasibility:** score: **needs major new library**. Needs: OAI `CATZero`, `GeometricAction`; Mathlib `PresentedGroup`, `SimpleGraph`. Missing: Gromov graph model of random groups (labelled expander sequences, ~300+ lines), Izeki–Nayatani invariant δ (~150 lines), probabilistic 'with high probability' framework (~100 lines). Formal proof to compare: none.

#### S4. Family 254: an Artin group (116 generators) with no geometric CAT(0) action
- **Statement:** There is a finite-rank Artin group with no proper cocompact isometric action on a nonempty proper CAT(0) space (refutes Haettel's Conjecture 1.1 / Charney's problem).
- **Reference:** openai/math release family 254, preprint 'An Artin group with no geometric CAT(0) action' (2026-09-23); comparator `ArtinCAT0`.
- **Status:** known within the release (unrefereed)
- **Current proof size:** OAI/GroupTheory/ArtinCAT0: 20 files, ≈ 9,400 Lean lines.
- **How the item helps:** Probably not much. 254's obstruction is algebraic: stable translation lengths, braid subgroups, sectors. It uses no random presentation, tangent-cone configuration or energy minimizer. Only the shared CAT(0) basics (`CATZero`, segments, midpoints, geometric actions) would carry over. It is useful as a near-control on the same comparator style: a big speedup here would point to shared infrastructure, not to the gadget.
- **Expected speedup:** low. Confidence: medium.
- **Lean feasibility:** score: **statable now**. Needs: ComparatorChallenges/ArtinCAT0.lean (own `CAT0`, `GeometricAction` definitions). Missing: none (a bridge between ArtinCAT0.CAT0 and HyperbolicObstruction.CATZero, ~30 lines, if the 257 library is to be used). Formal proof to compare: OAI/GroupTheory/ArtinCAT0 (≈ 9.4k lines).

### Open or new problems

#### O1. Gromov's question: which finite metric spaces embed isometrically in a CAT(0) space? (≥ 6 points)
- **Statement:** Give an intrinsic characterization of finite metric spaces that admit an isometric embedding into some CAT(0) space. Known: ≤ 5 points iff every 4-point subset satisfies Gromov's ⊠-inequalities (Toyoda). Open for ≥ 6 points.
- **Reference:** Gromov, 'CAT(κ)-spaces: construction and concentration', Zap. Nauchn. Sem. POMI 280 (2001) [unverified]; Toyoda, 'An intrinsic characterization of five points in a CAT(0) space', Anal. Geom. Metr. Spaces 8 (2020), arXiv 1907.09074, https://arxiv.org/abs/1907.09074 [verified by subagent]; Lebedeva–Petrunin, '5-point CAT(0) spaces after Tetsu Toyoda', AGMS (2021), arXiv 2009.09522, https://arxiv.org/abs/2009.09522 [verified by subagent].
- **Status:** open for ≥ 6 points (per Toyoda 2020 / Lebedeva–Petrunin 2021; not re-checked for 2022–2026 progress)
- **Matching part of the obstruction:** The gadget is a finite configuration (points, plus midpoints and one fractional-geodesic inequality) that no CAT(0) space contains. `CoreGeometry.MetricCore` alone is a pure squared-distance pattern on 18 points: incidence = 1, two-step = 2, three-step ≥ 3. If the pure-distance core is already non-realizable, it is a new explicit obstruction certificate on 18 points.
- **How the item helps (adaptation sketch):** Step 1 (Lean-checkable): ask whether `MetricCore z` alone (without `ExceptionalTest`) is contradictory in every CAT(0) space. `no_finite_obstruction` currently consumes `loose`, `missing` and `fractional` too. If it is contradictory, check every ≤ 5-point sub-configuration against the ⊠ / cycle conditions. If all pass, the doubled-Fano core is a ≥ 6-point space that the 5-point criterion misses, which is genuinely new data for Gromov's question. If `MetricCore` alone is realizable, the fractional test is essential, which is itself informative.
- **Payoff:** med–high (new explicit data on a 20-year-old characterization problem). Confidence: low–medium (the pure-metric core may well be realizable, e.g. in a cube complex). Difficulty: medium.
- **Lean feasibility:** score: **statable now**. Needs: OAI `CATZero`, `CoreGeometry.Vertex`, `CoreGeometry.MetricCore`; statement `¬ ∃ (X : Type) (_ : MetricSpace X) (h : CATZero X) (z : Vertex → X), MetricCore z`. Missing: none (the ⊠-inequality family needs ~30 lines if the 5-point comparison is also wanted). Formal proof to compare: OAI `no_finite_obstruction` (with the extra exceptional fields).

#### O2. Are Gromov density random groups at 1/6 < d < 1/2 CAT(0)? (in particular 1/3 < d < 1/2, where property (T) rules out cube complexes)
- **Statement:** For Gromov's density model at density d ∈ (1/6, 1/2), does the random group act geometrically on a proper CAT(0) space with overwhelming probability, or not?
- **Reference:** Ollivier, 'A January 2005 invitation to random groups', Ensaios Mat. 10 (2005), open-problems chapter [wording unverified]; Ollivier–Wise, Trans. AMS (2011), cubulation at d < 1/6 [memory]; Mackay–Przytycki (d < 5/24) and Montée, arXiv 2106.14931, https://arxiv.org/abs/2106.14931 (d < 3/14): non-trivial actions on CAT(0) cube complexes [subagent-verified]; Ashcroft, arXiv 2104.14986 and 2206.14616 (property (T) thresholds) [titles verified by subagent].
- **Status:** open as far as found (only cube-complex actions are settled; general CAT(0) geometric actions are not) [status not re-verified on the web]
- **Matching part of the obstruction:** The uniform conditional test exists exactly to make a random presentation fail to act on every CAT(0) space at once. 257 uses a tailored nested model (fans at N^{2−α}, tops over selected fans, decorations just below 1/2) in which the template configuration is forced in the limit.
- **How the item helps (adaptation sketch):** Adaptation: (a) in the density model, find a sub-presentation pattern whose limit configuration after `conditional` + ultralimit contains a CAT(0)-impossible gadget; (b) reuse `SamplingSequence.conditional` verbatim, which only needs the `singleton` and `star` TV-coupling axioms of `SamplingSequence`; (c) verify those axioms for the density model at the given d. The hard part is (a): plain density-model presentations have no fan/top nesting.
- **Payoff:** high. Confidence: low. Difficulty: high.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `NoGeometricCATZeroAction`; Mathlib `FreeGroup`, `PresentedGroup`, `PMF`/finite uniform laws. Missing: density model: uniform random sets of (2m−1)^{dℓ} cyclically reduced words of length ℓ and 'with overwhelming probability' (~120–200 lines). Formal proof to compare: none.

#### O3. Expanders with respect to all Hadamard spaces / a finitely generated group with fixed points for every CAT(0) space via Gromov's graph model
- **Statement:** Is there a bounded-degree expander sequence that is an expander with respect to every Hadamard space (a uniform nonlinear spectral gap)? Equivalently, through Gromov's graphical random groups: is there a f.g. group with fixed points for isometric actions on all CAT(0) spaces built this way?
- **Reference:** Mendel–Naor, 'Expanders with respect to Hadamard spaces and random graphs', Duke Math. J. 164 (2015) [memory; question wording unverified]; Kondo, 'CAT(0) spaces and expanders', Math. Z. 271 (2012) (CAT(0) spaces with δ = 1) [memory]; Naor–Silberman, Compositio 147 (2011) [memory].
- **Status:** believed open [unverified; web quota exhausted]
- **Matching part of the obstruction:** The quantifier swap 'one object, all CAT(0) targets' is exactly what P37 delivers: a barycentric (Sturm inductive-mean) control whose constants do not depend on X. IKN/Kondo show that the δ-route must fail for some targets.
- **How the item helps (adaptation sketch):** Adaptation: the conditional test gives E⟨h_I, v_e⟩ ≤ o(1) for tests depending on 'past' labels. A nonlinear-spectral-gap statement needs a Poincaré inequality for all maps into X, not only energy-minimizing orbit maps. One would replace `EnergyOrbit.minimum` by an almost-minimizer from a Gromov–Schoen scaling limit and drop the uniform displacement bound `bound : … ≤ M`. The second step is the main obstacle.
- **Payoff:** high. Confidence: low. Difficulty: high.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `CATZero` + Mathlib `CompleteSpace`, `SimpleGraph`. Missing: nonlinear Poincaré constant γ(G, X) of a finite graph w.r.t. a metric space (~60 lines); expander sequence as a family (~40 lines). Formal proof to compare: none.

#### O4. Does every hyperbolic group act geometrically on a Busemann-convex space (or a space with a strongly convex bicombing)?
- **Statement:** Between CAT(0) (now refuted for hyperbolic groups by 257) and injective/Helly spaces (proved for all hyperbolic groups by Lang and by Chalopin–Chepoi–Genevois–Hirai–Osajda) sits Busemann convexity. Does every hyperbolic group act properly and cocompactly on a proper Busemann-convex geodesic space?
- **Reference:** Lang, 'Injective hulls of certain discrete metric spaces and groups', J. Topol. Anal. 5 (2013) [memory]; Descombes–Lang, convex geodesic bicombings (2015) [memory]; Chalopin–Chepoi–Genevois–Hirai–Osajda, 'Helly groups', arXiv 2002.06895 [memory]. I did not find a problem-list citation for the Busemann version in this pass.
- **Status:** believed open [unverified]
- **Matching part of the obstruction:** This is the natural boundary of the device. The conditional test needs CAT(0)-specific structure: inner-product-like tangent-cone pairings (`ConeData.pairing`), Sturm's variance inequality for inductive means, and CN-equality rigidity. All of these fail in general Busemann spaces.
- **How the item helps (adaptation sketch):** Adaptation sketch: replace barycenters by Busemann barycenters (Es-Sahib–Heinich / Navas) and the cone pairing by a first-variation inequality. The finite gadget would have to be re-derived from Busemann rigidity (strictly convex norms on tangent cones). The likely outcome is failure, which is still informative; see negative control N1.
- **Payoff:** high if it works; also a sharp test of the device's limits. Confidence: low. Difficulty: high.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `GeometricAction`, `WordHyperbolic`. Missing: Busemann convexity (~20 lines); a library of convex bicombings (~150 lines) if the proof route is pursued. Formal proof to compare: none.

#### O5. Proper (not necessarily cocompact) actions: does every hyperbolic group act properly on some complete CAT(0) space?
- **Statement:** Is there a hyperbolic group admitting no proper isometric action on any complete (possibly infinite-dimensional, non-proper) CAT(0) space?
- **Reference:** Status context: Duchesne–Simon, arXiv 2603.03863 (2026), cited by 257 for its 'Question W' (wording not read in this pass); Monod–Py on actions on infinite-dimensional hyperbolic space [memory]. Property (T) hyperbolic groups have no proper action on Hilbert space or on H^∞ [memory].
- **Status:** status unverified; possibly open in the CAT(0) generality
- **Matching part of the obstruction:** The uniform test kills geometric actions. Cocompactness enters through the energy minimizer and the displacement bound M (P35), and properness of X through the ultralimit.
- **How the item helps (adaptation sketch):** Adaptation: an almost-minimizer version of `EnergyOrbit` without `bound`, with rescaled ultralimits of non-proper spaces (OAI `OrbitLimit` already handles a sequence of spaces). The contradiction would then forbid all fixed-point-free actions, which would give a hyperbolic group with fixed points on every complete CAT(0) space. That is stronger than needed and may be false, so a 'proper but not cocompact' variant needs a different end-game.
- **Payoff:** high. Confidence: low. Difficulty: high.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `CATZero`, Mathlib `CompleteSpace`. Missing: proper isometric action without cocompactness (~20 lines, adapting `GeometricAction`). Formal proof to compare: none.

#### O6. Quantitative/effective version: an explicit hyperbolic group (explicit finite presentation) with no geometric CAT(0) action
- **Statement:** Exhibit a concrete finite presentation of a hyperbolic group with no geometric CAT(0) action, ideally with a checkable certificate.
- **Reference:** 257 itself: 'The proof is an existence argument and does not give an effective size for K' (01-introduction.tex:15).
- **Status:** open (new problem raised by the paper)
- **Matching part of the obstruction:** The gadget is finite and explicit. Only the sampling and ultralimit layers are non-effective.
- **How the item helps (adaptation sketch):** Make `SamplingSequence.conditional` quantitative: `ConeData.conditional_test` is already quantitative (explicit B√(1/(n+1)+2M²η)+2BMη). What is missing is a quantitative replacement for the ultralimit, i.e. a robust (ε-perturbed) version of `no_finite_obstruction`: all equalities replaced by ±ε, contradiction for ε < ε₀. That robust gadget lemma is a natural, Lean-statable sub-target.
- **Payoff:** med. Confidence: medium (a robust version of a finite algebraic contradiction usually exists; the work is in the constants). Difficulty: medium for the robust gadget; high for a full explicit presentation.
- **Lean feasibility:** score: **statable now**. Needs: OAI `FiniteObstructionData` with each `=` relaxed to `|· − ·| ≤ ε` (robust gadget). Missing: none for the robust-gadget sub-target. Formal proof to compare: OAI `no_finite_obstruction` (exact version).

## Theorem corollaries (reach, not reuse)

- **Gromov's realization question, CAT(0) and CAT(−1) versions (BMS Problem H11; Stark 2025 OP 2.15).** Answered negatively by the headline itself.
- **Full paper Thm 1.1 with '2-dimensional' and 'no locally CAT(0) finite model'.** A strengthening of the comparator reachable from the existing Lean in about 50–90 lines total (see lean_gaps). A good, cheap Lean exercise and a calibration task for the prover, but not reuse.
- **Infinite CAT(0)- and CAT(−1)-dimension for a hyperbolic group of geometric dimension 2.** Pushes Brady–Crisp (Comment. Math. Helv. 82, 2007 [memory]: geometric dimension 2 vs CAT(0) dimension 3) to the extreme. This is a corollary.
- **No finite-index subgroup of π₁K acts geometrically on a proper CAT(0) space.** Standard induction: a geometric action of a finite-index H on X induces one of G on X^{[G:H]}. A corollary, not in the Lean.
- **Single-target fixed-point statements (Toyoda/IKN type: for each X some hyperbolic group fails to act geometrically on X).** Trivial from the headline.
- **Linear isoperimetric inequality does not imply a nonpositively curved finite model.** Already stated by the paper as a consequence.

## Reuse inside the release

- **254 (Artin group with no geometric CAT(0) action, 2026-09-23).** Same headline type, different design: stable translation lengths, braid subgroups and sectors (introduction.tex). Grep of its build for Fano, tangent cone, barycent, Sturm, ultralimit, uniform conditional and energy found nothing. No reuse of the gadget or of the conditional test.
- **246 (Cannon's conjecture), 252 (non-residually-finite hyperbolic group).** Per the novelty pass, no shared machinery: no Fano template, Sturm means, ultralimits or Ollivier counting.
- **CAT0Fillings / IntegralFillings (sharp integral fillings in CAT(0) spaces).** Use their own CAT(0) definitions (`CAT0Fillings.IsCAT0`). Isoperimetry in CAT(0) spaces, unrelated to the gadget.
- **PolycyclicRecognition.** Has a `WordBallSamplingSequence`. This is a name collision only (Lie-group chart sampling), not the 257 `SamplingSequence`.
- **Verdict.** No family in the release reuses the doubled-Fano design or the uniform conditional test. The device is single-use inside the release.

## Negative controls

- **N1: Replace CAT(0) by injective metric spaces / Helly graphs (spaces with convex geodesic bicombings).** Expected: fails (proved-false analogue). Every hyperbolic group acts geometrically on a proper injective metric space (Lang 2013) and is Helly (Chalopin–Chepoi–Genevois–Hirai–Osajda) [memory]. So no version of the device can rule out geometric actions on these targets. The conditional test breaks there because tangent cones have no inner-product pairing and inductive means lack Sturm's variance bound. A prover that 'proves' no-action for injective targets has a bug.
- **N2: Gromov density random groups at d < 1/6.** Expected: fails (proved-false analogue). These are cubulated, hence act geometrically on CAT(0) cube complexes (Ollivier–Wise 2011) [memory]. Any transfer of the sampling/conditional-test pipeline must lose at low density. In 257 the decoration tables sit just below density 1/2, and the template only emerges there.
- **N3: Gadget with the exceptional data removed: `FiniteObstructionData` without `loose`, `missing`, `fractional` (equivalently, the undoubled template with all Fano incidences present).** Expected: the contradiction should not be derivable. In `no_finite_obstruction` the only route to `False` is `five_line_fans_contradiction`. Its antipodality hypothesis `hop` comes from `exceptional_antipodes`, which needs `hop` from `missing` (via `hmid`) and `hex` from `exceptional_identity` (needs `loose` and `fractional`). Without them the proof has no handle. Note that the residual data is NOT Euclidean-realizable: 5 or 6 line vectors with norm² 3/4 and pairwise pairing −1/4 have a Gram matrix I − J/4 that is not PSD. So realizability needs a genuinely non-Euclidean CAT(0) space (the novelty pass suggests cube-complex realizations). This is to be checked, not assumed.

## Top 5 (Lean-usable first)

1. **Pure-metric doubled-Fano core vs Gromov's CAT(0)-subset question** (O1). Statable now with existing OAI definitions (`MetricCore` + `CATZero`). It tests the gadget's design directly rather than its proof toolkit. One run decides whether the metric core alone is CAT(0)-impossible. If it is, and its ≤5-point subsets pass Toyoda's criterion, the gadget gives new data on an open 2001 question. This is the cleanest witness-reuse experiment available.

2. **Robust (ε-perturbed) doubled-Fano obstruction** (O6). Statable now by relaxing each field of `FiniteObstructionData` by ±ε. It is the first step toward an effective hyperbolic group and a natural test of whether a prover holding `no_finite_obstruction` reaches the robust version much faster than one without it. That makes it a measurable within-device speedup.

3. **Flat-triangle / CN-equality propagation** (S1). A textbook theorem (BH II.2.9) that is statable now. The OAI tangent-cone lemmas used by the obstruction proof are nearly the statement. It measures toolkit reuse, not the gadget, so a speedup here supports the infrastructure, not an N3 jump. It is still a clean, cheap Lean A/B test.

4. **Flat quadrilateral theorem (unit square)** (S2). Statable now, with the midpoint half already in OAI (`CATZero.square_mid`). Same caveat as S1. Expected speedup low–med.

5. **CAT(0)-ness of density random groups at 1/3 < d < 1/2** (O2). The only target where the uniform conditional test (P37) is the decisive ingredient, and the highest payoff. The statement needs about 150 lines of random-group definitions, and the adaptation (forcing a CAT(0)-impossible limit configuration in the plain density model) is the hard, uncertain part. Use it as a stretch target, not for the speedup measurement.

## Precedent check

**Earlier equivalent:** none found. No earlier construction of a finite configuration that is impossible in every CAT(0) space and built from a doubled Fano incidence graph was found. The Fano/Heawood graph usually appears in the opposite role, as the CAT(1) link of Ã₂ buildings. For the conditional test, the closest neighbours are target-dependent: IKN 2012 and Toyoda (constants through δ(X)), and Naor–Silberman / Mendel–Naor (nonlinear spectral gaps for classes of targets). An 'all CAT(0) targets' obstruction of a different kind exists: Eskenazis–Mendel–Naor, Invent. Math. 217 (2019), 'Nonpositive curvature is not coarsely universal' [memory], via metric cotype. It concerns coarse embeddings, not geometric actions, and does not downgrade the item. Nothing after 2026-10-06 using the device was found. The web search was cut short by a tool quota: two searches for a 2026 follow-up of 257 found none, and one 2026 search summary still called the realization question open, consistent with 257 not yet being absorbed.

- IKN 2012 / Toyoda: same purpose (random hyperbolic groups vs cocompact CAT(0) targets); target-dependent constants. Not equivalent.
- Eskenazis–Mendel–Naor 2019: uniform over all CAT(0) spaces, but for coarse embeddings via metric cotype. Not equivalent.
- Family 254 (Artin, 2026-09-23): the same 'no geometric CAT(0) action' conclusion by a different, algebraic mechanism. Not equivalent and not a downgrade.
- Post-2026-10-06: nothing found (search incomplete).

## Sources

- data/pilot/257/family.md, family.json, novelty.md, novelty.json; data/eureka_shortlist.json (rank 8 entry)
- data/raw/openai-math/lean/OAI/Geometry/HyperbolicGroups/{Main,Basic,Template,MetricHexagon,CATZero,CATZeroFurther,ConditionalStar,FiniteLaw,Exceptional,GraphLimit,OrbitLimit,Selection,SelectedPresentation,IndexedFillingValue,CompactLocalCATGeometric,FinitePolygonModel}.lean (read at text level)
- data/raw/openai-math/lean/ComparatorChallenges/HyperbolicObstruction.{json,lean}; lean/docs/257.md
- preprint A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/build/sections/01-introduction.tex, 07-completion.tex
- preprint An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/build/sections/introduction.tex; lean/ComparatorChallenges/ArtinCAT0.lean
- data/raw/openai-math/CONTENTS.md (release scan for CAT(0), hyperbolic, Fano)
- https://arxiv.org/abs/1907.09074 (Toyoda 2020) [via subagent]
- https://arxiv.org/abs/2009.09522 (Lebedeva–Petrunin) [via subagent]
- https://arxiv.org/abs/2106.14931 (Montée) [via subagent]
- https://arxiv.org/abs/1102.0729 (Toyoda) [via subagent]
- https://arxiv.org/abs/1012.4147 (IKN statement as quoted there) [via subagent]
- https://arxiv.org/abs/2603.03863 (Duchesne–Simon, abstract only) [via subagent]
- Memory-only, unverified: Ollivier 2005 survey; Ollivier–Wise 2011; Mendel–Naor 2015; Kondo 2012; Naor–Silberman 2011; Lang 2013; CCGHO Helly groups; Eskenazis–Mendel–Naor 2019; Brady–Crisp 2007; Bridson–Haefliger 1999

## Search log

- Local: grep of the Lean dir for the comparator chain (main → … → impossible_sequence → MetricCore.impossible → no_finite_obstruction; word_lower/fractional_error → conditional).
- Local: located `simplex_card_le_three` (2-dim bound) and `uniformLocalCATZero_of_compact` (the only CAT(−1)-specific step) to pin down the comparator gap.
- Local: CONTENTS.md scan; grep of family 254's preprint for Fano/tangent cone/Sturm/ultralimit/energy (no hits); grep of OAI for other uses of HyperbolicObstruction/SamplingSequence (only a PolycyclicRecognition name collision).
- Web (subagent, ~8 searches before quota): 'hyperbolic group not CAT(0) 2026 random presentation Fano' (no follow-up found); Toyoda five points CAT(0); Lebedeva–Petrunin; random groups density cubulation / property (T) (Montée, Ashcroft); IKN / Toyoda δ invariant; Duchesne–Simon abstract.
- Web (own): one search on Mendel–Naor 'Expanders with respect to Hadamard spaces' failed with the session quota; no further web checks were possible.
- Lean: not compiled; all Lean claims are text-level.
