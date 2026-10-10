# Family 221: reasoning-trace analysis ("The Mézard–Parisi formula for diluted spin glasses")

Source: `data/traces/221.txt` and the LaTeX source `data/raw/openai-math/reasoning_traces/mezard-parisi-formula.tex`. This is OpenAI's 5-page *summarized* chain of thought. The summary body has 3 sections and is **987 words** (7,260 characters), with prompt, headings and references excluded. It contains two VERBATIM excerpts. The final paper (`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/`) runs to about 14.9k words, and the family is formalized in Lean (`lean/OAI/Probability/DilutedSpin`, 405 files). Machine-readable coding is in `trace.json`. Line numbers (L) refer to the .txt file, and shares are fractions of summary words.

**Read this first.** Everything here concerns *what the summary reports*. The compression is extreme: about 1 summary word per 15 paper words. Lengths measure how the summarizer allocated text, not the model's compute. All counts are lower bounds.

## 1. The story of the search

**Sec. 1a–1b (L100–107, first 8%): framing, then a quick probe of the answer.**
- The model starts from the gap between the Panchenko–Talagrand interpolation upper bound [5] and the missing lower bound.
- Panchenko's finite-RSB analysis [4] is the natural template. But pair-overlap ultrametricity does not determine the **multioverlaps** that a diluted model needs (lesson C1).
- It probes for a counterexample at four hypothesis boundaries: a nonintegrable factorization constant, asymmetric fields, the positivity boundary, and divergent messages. None yields one.
- A constant-interaction case serves as a normalization check.
- Answer uncertainty ends here. After share 0.08 the trace never leaves the PROVE strategy.

**Sec. 1c–1d (L108–117, 0.08–0.20): two transfer attempts fail.**
- **Many-site cavity argument.** Condition on shared hierarchical randomness, then look for independent site messages. This fails because the shared randomness *adapts to the sampled sites*. A pointwise law of large numbers is not uniform, and pinning selects states with the wrong weights. The model writes the VERBATIM line "Aha recursive structure: overfitting shared variable can simulate original model at smaller scale".
- **Auxiliary hierarchies.** Enriched Gaussian fields [3] and the Hamilton–Jacobi viewpoint [2] suggest auxiliary hierarchies. Poisson perturbations, as in Barbier–Panchenko [1], are judged "more direct" (this is the only **insight** backtrack). But the Bayesian identities do not transfer: posterior-sampled observations and fractionally weighted observations have different laws (C8).

**Sec. 1e–2a (L118–134, 0.20–0.40): the final frame, then a run of failures inside it.**
- "Therefore", the model works *directly* with iterated power means and tilted path transitions. Marked perturbations specify where replicas branch, and the change of density gives signed coefficients for extending an old replica tree (PV3).
- The two-replica identity works.
- Higher products do not: signs alternate, dummy anchors cancel, and projections are not admissible tests (C9).
- The target is sharpened to *conditional decorrelation* of sitewise product vectors, followed by ordinary multioverlap concentration (PV4).
- Six failures follow:
  1. fresh subtrees with division by small exponent gaps;
  2. coarse partitions;
  3. equal-exponent refinements. All three hit "the same problem": continuity errors are too large after the division (C10).
  4. pinning again (C5 relearned);
  5. an exact purity claim, refuted by hidden Poisson–Dirichlet clustering inside an exponent jump (C11);
  6. factorial-polynomial expansions with a two-copy cancellation. This exposes squared covariances (C12, salvaged) but gives no estimate.

**Sec. 2b (L135–140, 0.40): the decisive pivot.**
- **Shift every internal branching depth of the target tree by one level.** The shifted splits avoid the old tree's branching depths, so each new branching vertex must be created by a fresh unary split. That split costs a factor −δ, which matches the δ per vertex in the shape's normalization.
- The model's VERBATIM reaction is "Great! Need carefully prove average error little with shifted depths not rare". It names both the breakthrough and the remaining obligation.

**Sec. 2c–2e (L141–162, 0.44–0.68): completing the proof.**
- An induction replaces descendant groups by conditional means, and an anchor identity gives a positive sum of squares.
- Bounded-martingale energy controls the shifts on average over depths (PV6).
- A marker anchor yields ordinary concentration (PV7). The order of limits is N first, then the hierarchy depth L.
- Further components:
  - the logarithmic expansion organized by adding paths (PV8);
  - the upper bound with all-plus normalization and the convexity remainder A^p − pAB^{p−1} + (p−1)B^p ≥ 0 (PV9);
  - sublinear marked Poisson perturbations, diagonal selection and polarization (PV10);
  - the arctanh encoding of a uniformly sampled site (PV11).

**Sec. 3 (L164–188, the last 31%): checking.**
- Ten checks of the final route.
- Two of them change a formulation:
  - the coefficient calculation is "reorganized as a positive squared-difference identity";
  - a concern that varying the insertion parameter "silently changes the background measure" is fixed by a fixed-background Palm formulation.
- Reduction to first moments.
- The summary ends hedged: "The final response claims that …".

## 2. Decisive pivots

| Pivot | Share | Trigger | Classification | Grade |
|---|---|---|---|---|
| PV1 multioverlaps as target; commit to PROVE | 0.02–0.08 | C1, C2 | known route (Panchenko 2013 viewpoint) | N0 |
| PV2 auxiliary finite hierarchy built into the construction | 0.13–0.17 | b1 failure + "Aha" + retrieved [3],[2] | **transfer** | N0–N1 |
| PV3 direct power-mean tree calculus + depth-selecting marks + signed extension coefficients | 0.20 | C8 (explicit "therefore") | known technique adapted (GG98/AC98/Barra–De Sanctis/Pan13 are named only in the paper) + new devices | **N2**, F3 flavour |
| PV4 conditional-decorrelation target (squared conditional covariance v_N(S,d)) | 0.28 | C9 | templated strengthened hypothesis | N2 (capped), F2 |
| **PV5 shift of branching depths + charging of fresh splits** | **0.40** | **C10, stated after 3 failures; plus C11, C12** | **new concept (constructed)** | **N3 candidate, F3 (F5 flavour)**; chain depth 2 |
| PV6 averaged depth continuity via martingale energy | 0.44 | need created by PV5 (VERBATIM) | known technique | N0–N1 |
| PV7 marker anchor | 0.50 | need: conditional → ordinary concentration | constructed small variant | N2, F3 |
| PV8 Q_k random-tree log expansion | 0.54 | none visible | known technique adapted (MP01, PT04) | N1–N2 |
| PV9–PV12 upper-bound normalization, selection/polarization/Palm, arctanh encoding, reduction | 0.56–0.94 | C3, C7, C14, C4 | known | N0–N1 |

**PV5 is the core of the proof.** It works only inside the tree calculus of PV3 and the induction of PV4. It is completed by PV6 (known) and PV7. Final-paper anchors:
- the "Shifted copies and their coefficients" paragraph of Sec. decorrelation (Fig. `decor:shift-figure`, J = κ(S⁺)², eq. `decor:relative-absolute-cost`);
- Lemma `tree:charging`;
- Lemma `decor:depth-continuity`;
- Lean: `ShiftedTree.lean` (`shiftedTwinDepths`), `ShapeCharging.lean` (`prescribed_history_charging_bound`), `SimultaneousShift.lean` (`averaged_simultaneous_shift_le`).

The paper's introduction singles it out ("Delaying each branching depth by one level permits an induction…").

## 3. CDCL coding of the search

### Level-assignment rules
The 287 rules are applied verbatim. L1 is the answer commitment, here PROVE vs REF. Four documented extensions (full text in JSON):
- **221-1.** A brief counterexample probe is an L1 REF node, so entering and leaving it counts as a restart. A stricter coding gives 0 restarts.
- **221-2.** Moving between *kept* proof components (upper bound, lower-bound frame, comparison, reduction) is a subgoal switch, not a backtrack.
- **221-3.** Checks in a later section are `node_kind: check` children of the node they check. A check that changes a formulation ("instead", "reorganized") is a conflict plus repair, as in 287's d1.3.3.
- **221-4.** Length is the sum of words of the sentences assigned to the subtree, because the checks interleave. A sentence that lists several attempts is split by word count.

### Search tree (42 nodes in JSON, including ROOT)
```
ROOT  lim F_N = inf_r Phi_r ?                                   987 w
├─ PROVE1 (L100-101, 47 w, 5%)  PT gap; Panchenko finite-RSB [4,5]
│   └─ a1 pair-overlap ultrametricity  ✗ insufficient           -> C1 (need all multioverlaps)
│        ══ RESTART 1 (L103, 0.05) ══
├─ REF1 (L103-107, 36 w, 4%)  counterexample probes; constant-interaction check ✓
│   ├─ r1 nonintegrable factorization const ✗  -> C3 (all-plus normalization, salvaged)
│   ├─ r2 asymmetric fields ✗     ├─ r3 near positivity boundary ✗     └─ r4 messages -> inf ✗
│        ══ RESTART 2 (L108, 0.08) ══
└─ PROVE2 (L108-188, 904 w, 92%)
    ├─ b1 many-site cavity, condition on shared randomness  ✗ adapts to sites (C4)
    │   ├─ b1.1 pointwise LLN ✗          └─ b1.2 pinning ✗ wrong weights (C5)
    │   "Aha recursive structure: overfitting shared variable can simulate original model..."
    │        ── backjump d=2 ──
    ├─ b2 enriched Gaussian fields / HJ [3,2]   ⇢ superseded  (INSIGHT, d=1): Poisson "more direct" (C7)
    ├─ b3 Barbier-Panchenko Bayesian identities [1]  ✗ no transport (C8)
    ├─ b4 FINAL FRAME (L118, 0.20): power means, tilted paths, marks, signed tree coefficients
    │   ├─ b4.1 two-replica child-replacement identity ✓
    │   ├─ b4.2 higher products directly ✗ signs/anchors/projections (C9)
    │   ├─ b4.3 target: conditional decorrelation -> multioverlap concentration
    │   │   ├─ b4.3.1 fresh subtrees ÷ small gaps ✗ (C10) ─ b4.3.2 coarse partitions ✗ ─ b4.3.3 equal-exp. refinements ✗
    │   │   ├─ b4.3.4 pinning again ✗ (C5 relearned)
    │   │   ├─ b4.3.5 exact purity ✗ hidden Poisson-Dirichlet clustering (C11)
    │   │   ├─ b4.3.6 factorial-polynomial + two-copy ✗ (salvage: squared covariances, C12)
    │   │   └─ b4.3.7 SHIFT every branching depth by one (L135, 0.40)  "Great!"  ✓
    │   │       ├─ b4.3.7.1 averaged error via martingale energy ✓ ── v4 check ✓
    │   │       ├─ b4.3.7.2 induction + anchor identity (squares) ✓ ── v1 ✓, v2a ✗→ v2b positive sq.-difference ✓
    │   │       ├─ b4.3.7.3 marker anchor ✓ ── v6 joint check ✓
    │   │       └─ v3 charging at coinciding depths ✓
    │   ├─ b4.4 log expansion by adding paths (telescoping, geometric tail) ✓
    │   └─ b4.5 sublinear marked Poisson + diagonal selection + polarization ✓
    │           └─ v5a background-measure concern ✗→ v5b fixed-background Palm ✓
    ├─ c1 upper bound: all-plus normalization + convexity remainder ✓
    ├─ c2 comparison: arctanh encoding of a uniformly sampled site ✓ ── v7 ✓
    └─ c3 reduction to first moments ✓
```

### Metrics
| Metric | 221 | 287 (reference) |
|---|---|---|
| summary words | 987 | 3,796 |
| decisions (excl. checks) / conflicts | 41 (32) / 18 | 69 / 47 |
| backtracks: total / conflict / insight / unclear | 18 / 17 / **1** / 0 (2 of the conflicts are repairs) | 48 / 46 / 1 / 1 |
| distance histogram (all) | d=1: 15, d=2: 3 | d=1: 40, d=2: 7, d=3: 1 |
| by trigger | conflict {1:14, 2:3}; insight {1:1} | conflict {1:39, 2:6, 3:1}; insight {2:1}; unclear {1:1} |
| max backtrack distance / max depth | 2 / 6 (5 excl. checks) | 3 / 4 |
| restarts | 2 (PROVE→REF→PROVE, both in the first 8%) | 3 |
| propagations (rough) | 37 | 42 |
| learned clauses / reuse rate | 14 / 0.93 | 26 / 0.77 |
| share before final route (chars / words) | 0.20 / 0.20 | 0.78 / 0.77 |
| share before decisive pivot (chars / words) | **0.39 / 0.40** | ~0.80 (PV4) |
| share spent checking the final route | 0.31 (sec 3) | — |
| abandoned-branch length, mean / median (words) | all 20.8 / 16.5; conflict 20.9 / 14 (excl. restarts 18.2 / 13); insight 19 | conflict 122 / 60; insight 285 |
| length vs distance | Pearson 0.83, Spearman 0.65 (excl. restarts 0.86 / 0.42). Mean: d=1 15 w, d=2 50 w | Spearman 0.62 |
| trace references / literature hit rate | 5 / 0.40 (2 shared with paper) | 54 / 0.09 |
| explicit time/compute markers | none. Sequence words only ("Initial", "Further", "repeatedly", "Finally", "The next stage", "Another concern"); 2 VERBATIM exclamations | none |

**Abandoned-branch lengths (all 18 backtracks).**
| from → to | d | trigger | branch | words |
|---|---|---|---|---|
| a1 → REF1 | 2 | conflict (restart) | PROVE1 | 47 |
| r1 → r2 | 1 | conflict | r1 | 7 |
| r2 → r3 | 1 | conflict | r2 | 7 |
| r3 → r4 | 1 | conflict | r3 | 6 |
| r4 → PROVE2 | 2 | conflict (restart) | REF1 | 36 |
| b1.1 → b1.2 | 1 | conflict | b1.1 | 10 |
| b1.2 → b2 | 2 | conflict | b1 | 67 |
| b2 → b3 | 1 | **insight** | b2 | 19 |
| b3 → b4 | 1 | conflict | b3 | 32 |
| b4.2 → b4.3 | 1 | conflict | b4.2 | 23 |
| b4.3.1 → b4.3.2 | 1 | conflict | b4.3.1 | 20 |
| b4.3.2 → b4.3.3 | 1 | conflict | b4.3.2 | 10 |
| b4.3.3 → b4.3.4 | 1 | conflict | b4.3.3 | 9 |
| b4.3.4 → b4.3.5 | 1 | conflict | b4.3.4 | 13 |
| b4.3.5 → b4.3.6 | 1 | conflict | b4.3.5 | 21 |
| b4.3.6 → b4.3.7 | 1 | conflict | b4.3.6 | 26 |
| v2a → v2b | 1 | conflict (repair) | v2a | 8 |
| v5a → v5b | 1 | conflict (repair) | v5a | 14 |

**Do long branches end in restarts?** No. Both restarts are at the very start and abandon short units (47 and 36 words). The longest abandoned branch is b1 (67 words, d=2), which is not a restart. The length–distance correlation only says that abandoning an L2 family costs more text than abandoning a leaf.

### The insight-driven step
**b2 → b3: Gaussian enrichment / HJ is bypassed for Poisson perturbations ("more direct tests").**
- *Origin:* retrieved, from Barbier–Panchenko [1].
- *Simplification:* not quantifiable. The bypassed branch had no stated subgoals, and the gain is by *avoidance*: transporting SK/HJ machinery to diluted models would be a research project in itself.
- *Grade:* N0 transfer, so it is not a novelty candidate.
- The Bayesian version then fails at once (b3). Only the idea of Poisson perturbations survives.

Every other backtrack is conflict-driven. The decisive PV5 is conflict-driven too: it follows a stated failure (b4.3.6) and answers a stated requirement (C10).

### Where the CDCL analogy breaks down
- The summary is about 1/15 the length of the paper. Single sentences hide whole searches ("Coarse partitions and equal-exponent refinements repeatedly encounter the same problem").
- The restart count depends on coding the 26-word counterexample probe as a strategy.
- The repairs v2a and v5a are inferred from wording ("reorganized", "instead").
- Unlike in 287, clause → decision links are often *explicit*:
  - C8 → b4 ("therefore");
  - C10 → b4.3.7 ("matching the small factor in the prescribed shape's normalization");
  - C10 → v3 ("This is the point of the shift").
  This is the closest of the traces seen so far to real conflict-driven learning. A summarizer that narrates in "because" form may also inflate that impression.

## 4. Dead ends and what was learned
Each dead end carries a full `lesson` object in the JSON (`dead_ends.detailed` and the nodes).

| Dead end | Obstruction | Lesson (form, generality) | Known? | Salvage / reuse |
|---|---|---|---|---|
| a1 structural finite-RSB route | pair overlaps don't fix multioverlaps | C1, sharpened target (general) | yes: Panchenko 2013 (cited in paper, not trace) | target of b4.3, comparison c2 |
| REF1 r1–r4 counterexample probes | none found | C2 commit; C3 normalize by all-plus (negative + salvaged tool, local) | partly (PT04) | C3 → c1, c3 (paper upper bound and reduction) |
| b1 shared-randomness cavity (+ LLN, pinning) | adaptivity; non-uniform; wrong weights | C4, C5 (negative + constraint, class-level) | pinning caveat known (Montanari 2008; Coja-Oghlan et al. 2018) | uniformly sampled site in comp:encoding |
| b2 Gaussian/HJ | superseded | C7 tool choice | yes (MP2020, M2022) | "auxiliary hierarchy" idea kept |
| b3 Bayesian identities | posterior-sampled vs fractionally weighted laws | C8 (negative + reformulation, class-level) | Nishimori specificity is known | Poisson perturbations kept; leads to b4 |
| b4.2 higher products | alternating signs, anchor cancellation, inadmissible tests | C9 constraint | partly (stochastic-stability folklore) | canceled-anchor expansion, old-tree tests, v1 |
| b4.3.1–3 small-gap division | errors not carrying the normalizer's δ | **C10** requirement (general within method) | not as a named obstacle | **specifies the shift** |
| b4.3.4 pinning again | observation law vs cavity | C5 relearned | — | none |
| b4.3.5 exact purity | PD clustering in an exponent jump | C11, counterexample → sharpened target | yes (Ruelle cascades) | averaging over depths; order of limits |
| b4.3.6 factorial-polynomial + two copies | still no covariance estimate | C12 salvaged tool | partly (three-copy tricks) | Lemma decor:contractions; squared-difference identity |
| v2a, v5a (repairs) | signed form; background measure | C13, C14 reformulations | Palm/Mecke known | decor:induction-identity; Lemmas pert:palm, pert:analytic |

**What was not learned or not recorded.**
- The trace never notes that the lower bound uses neither factorization nor positivity. The paper does (Cor. `comp:bounded-lower`), so these hypotheses matter only for the upper bound.
- The "Aha" line is ambiguous. It reads either as an obstruction or as the seed of PV2.
- Pinning was retried once despite C5. Retention is still far better than in 287.

## 5. Knowledge flow
- **Target.** C1 (multioverlaps) → b4.3 and c2.
- **Frame.** C7 + C8 → direct power-mean calculus with Poisson marks (explicit).
- **Constraints on the identities.** C9 → positive forms, old-tree tests, absolute-coefficient control.
- **Core.** C10 (stated three times) + C11 (only averaged concentration) + C12 (squares available) → **shift** → martingale averaging (requirement named VERBATIM) and the marker anchor.
- **Frame pieces from early probes.** C3 (from the counterexample probe) → upper-bound normalization and reduction. C4 → uniformly sampled site encoding.
- **Repairs.** C13 and C14 during checking.
- **Classification.** Necessary: C1, C3, C4, C8–C14, plus the two-replica identity. Enabling only: C2, C5, C7. Inert: C6.

**Contrast with 287.** There the knowledge flow explained the frame but not the core lemma. Here it explains the *specification* of the core step: C10 says exactly what the shift must achieve. But no clause contains the *means*, i.e. moving target splits off the old tree's branching depths so that each pays a fresh δ.

## 6. Eureka candidates (trace level)
| Id | Item | Grade | F | Main for | Main against |
|---|---|---|---|---|---|
| **E1** | shifted target tree S⁺ + charging fresh splits (relative absolute-cost bound) | **N3 candidate** | F3 (F5) | no precedent named in trace or paper; tiny change, qualitative budget drop (uncontrolled δ^{-2b} amplification → uniform constant); reached after 6 failures; only "Great!" | one step from clause C10 (general-position move); value is local to the model's own tree calculus (chain depth 2); generic "perturb parameters to avoid degeneracy" habit |
| E2 | marked-perturbation identities on prescribed colored trees | N2 | F3 | exact finite-tree identities with explicit γ_β, κ(S); depth-selecting marks | GG98/AC98/Barra–De Sanctis 2007/Pan13 are close neighbours named by the paper |
| E3 | conditional-decorrelation induction on v_N(S,d) | N2 (templated cap) | F2 | non-obvious inductive quantity enabling three-copy positivity | "carry an extra tracked quantity" + "all substructures" templates |
| E4 | marker anchor variance identity | N2 | F3 | same coefficient on both sides → Var(M) → 0 | one-line variant of the spin anchor |
| E5 | random-tree law Q_k for the log expansion | N1–N2 | F5 | elegant 1/k coefficients | reorganizes MP01/PT04 power-mean calculus |
| E6 | averaging over branching depths as the concentration notion | N2 | F2 | weakens the target to exactly what the cavity expansion consumes | GG/Talagrand parameter averaging; pinning-lemma pigeonhole |

**Suggested discovery test for E1.** Hide Lemma `tree:charging` and S⁺. Give the tree calculus and κ(S), with and without clause C10. The difference in hit rate measures how much the conflict clause predicts the construction. Lean anchors for the compression check (step 3b) are listed in `eureka_candidates[0].lean_anchors`.

## 7. What the trace tells us that the paper and Lean cannot
1. **Order of discovery.**
   - The paper presents the tree calculus, then the perturbations, then decorrelation.
   - The trace shows the reverse dependency: the decorrelation target came first (0.28), then six failures, then the shift (0.40).
   - The log expansion, upper bound and comparison were filled in afterwards (0.54–0.68).
   - Checking takes the last 31%.
2. **Retrieval vs construction.**
   - PV2 is a transfer, retrieved from Mourrat–Panchenko / Mourrat. Those papers are absent from the final paper.
   - PV3 is constructed. Its stochastic-stability antecedents (Ghirlanda–Guerra, Aizenman–Contucci, Barra–De Sanctis, Panchenko 2013) appear only in the paper, after the fact.
   - PV5 has no antecedent anywhere.
3. **Provenance.**
   - The latest trace reference is from 2022.
   - The paper adds 2025 works (BCS25, Concetti25) and cites the model-produced OpenAIThreeSAT2026, dated 27 Sep, after this paper's 23 Sep date. That citation is in a remark only, so it is not a dependency.
   - 3 of the 5 trace references are dead-end literature.
4. **Verification status.**
   - Self-refutation is real: exact purity is refuted, pinning is rejected twice, and a counterexample search is run.
   - The summary reports ten targeted checks and two repairs.
   - The ending is still hedged ("claims"). The paper's model corollaries (Viana–Bray, even-K SAT, ground states) never appear in the trace.

## 8. Comparison with 287
| | 287 (free group factors) | 221 (Mézard–Parisi) |
|---|---|---|
| answer uncertainty | 78% spent on the wrong answer (NEG) | about 4% (a probe); PROVE from 0.08 |
| shape of search | broad: ~38 invariant programmes, 3 restarts | narrow: one frame from 0.20, a run of 6 failures inside it |
| decisive step | PV4 small cocycle: N3 candidate, F3, chain depth 2, **no visible trigger** | PV5 shift: N3 candidate, F3, chain depth 2, **conflict-specified (C10)** |
| share before decisive step | ~0.80 | 0.40 |
| clause retention | poor (BDIP retried in 7 sections) | good (one relearning: pinning) |
| literature | 54 refs, 49 dead ends | 5 refs, 3 dead ends (the transfer branch) |
| insight backtracks | 1 (constructed, N2) | 1 (retrieved, N0) |
| checking | ~9 checks, hedged | 10 checks + 2 repairs over 31% of the text, hedged |

Both traces put the eureka-type step in a **constructed auxiliary object** (F3) that pays off only after two other new items are in place. In 221 the step sits one inference from an explicitly learned clause. This is the CDCL pattern "reached by propagating a learned clause", which PLAN.md reads as evidence of *reachability*, not hard discoverability. The step is still non-analytic: neither S⁺ nor the charging bound is a subterm of the goal or of anything the trace invoked.
