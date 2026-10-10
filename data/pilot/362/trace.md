# Family 362: reasoning-trace analysis ("Global smoothness for relativistic Vlasov–Maxwell")

**Sources**
- Trace: `data/traces/362.txt`, OpenAI's 6-page *summarized* chain of thought. The summary body is L65–211 with page headers excluded: **1,671 words**, 11,688 characters, in 5 sections.
- Coding: machine-readable in `trace.json`, which uses the same keys as 287 plus a few extensions.
- Final paper: `preprints/Global-classical-solutions-…-September-23-2026/build/main.tex` and its `sections/*.tex`, about 17,500 words.
- Line numbers (L) refer to the .txt file.

**Read this first.**
- The summary is in the summarizer's voice. It has **one** VERBATIM excerpt (L165–167) and hedges heavily: "proposed" 17 times, "intended" 6 times, "conditional on" 5 times.
- Everything below concerns *what the summary reports*. The compression is extreme: a 1,671-word summary of an argument whose paper runs to about 17,500 words.
- One phrase, "The present attempt instead pursued…" (L81), hints that earlier attempts or parallel lines exist and are not shown.

## 1. The story of the search

**Section 1 (L65–94, the first 22%): choose the route, build almost all of it.**
- The model never questions the answer. From the first sentence it looks for a finite-interval **momentum bound**, to feed the Glassey–Strauss bounded-momentum continuation criterion in its Luk–Strain formulation [2, 3]. Its scoping menu (null-slab energy, direction freezing, residence times) already contains the final route's ingredients.
- **Continuation subgoal.** The stated data class (C_b^∞ ∩ L², i.e. finite energy with all derivatives bounded) is not inside H⁵, the criterion's field hypothesis. The model proposes a repair at once: keep the Coulomb field, localize the divergence-free remainders through vector potentials, and restore the difference as a vacuum Maxwell field, which finite propagation keeps away from the particles. This survives verbatim in the paper's Section "Local theory and continuation".
- **Alternatives considered but not pursued:**
  - Cheverry–Ibrahim's momentum-spreading representation [1];
  - Wang's frequency-localized resonance and smoothing, extended beyond cylindrical symmetry [6];
  - Serre's positive-stress compensated integrability [5], set against the *indefinite* Maxwell stress (an implicit failure).
- **Commitment at L75 (share 0.07):** a *Pfaffelmoser-type residence-time strategy*. In the very next sentence the model derives the **signed integration-by-parts cancellation** between the source-acceleration and transport kernels. That is the core of the paper (Lemma can:identity). The cancellation removes the source-angle singularity but leaves:
  - endpoint terms;
  - cutoff derivatives;
  - a **receiver-acceleration coefficient** that can only be controlled with absolute force bounds.
- **Direction freezing fails.** A uniform directional modulus is blocked by derivatives of moving cutoffs (L78–79).
- **Replacement: counting direction changes.** The model counts "substantial angular changes within speed-stable windows" (L81–83). This explicitly avoids "a stronger uniform directional modulus" and becomes Lemma ang:direction.
- **The target sharpens** into the two-term **signed momentum-increment bootstrap**, |ΔV| ≤ MP√I + (linear in I). A weight is revised after failing on very short intervals. A coefficient argument conditional on the event counts and "endpoint averaging" (the paper's closure) are planned.

**Section 2 (L97–122): repairs.**
- The bootstrap gets its final shape: |ΔV| ≤ MP√I + A·I·P² log P / w.
- Cheverry–Ibrahim's retarded work kernel leaves a near-cone power loss, so it is abandoned.
- The signed integration by parts is made **selective**: it is applied only in a narrow angular sector. The sector boundary is set at a fixed small ratio of angular scales (θ < κφ in the paper) to avoid an extra logarithm.
- **Self-detected error:** the counting windows are too long for the bootstrap's linear term to preserve speed. They are shortened by a factor of about M² + A log P.
- A dependency-order audit (bootstrap → direction variation → improved occupation → improvement) becomes the paper's Figure fig:dependencies.
- The momentum-doubling argument appears: doubling times of about 1/log P have a divergent sum.

**Sections 3–5 (L123–211, the last 58%): stress-testing the same route.** The localization is revisited 6 times and the bootstrap restated 4 times. New items:
- particle labels are held fixed, matching the paper's Lemma ret:phase-change (credited there to Lazarovici, who is not in the trace);
- source *and* receiver direction counts;
- an occupation bound in a restricted window (high momenta, intermediate angles);
- the **exponent contradiction**: with w = Pᶻ and h = P^(−H), H < 0.41z versus H > 0.496z. These are *exactly* the numbers in the paper's Lemma sel:exponents;
- cancellation of differentiated cutoffs;
- the f/(4π) normalization for Luk–Strain;
- the VERBATIM sanity check, "Is there a conservation law obstructing? Think physical…".

Section 5 first states that absolute force bounds "lost a factor √w" (L194), although the narrow-sector fix that answers it was already in place at L108. The model "ended by asserting global smooth continuation". The summarizer adds that the assertion rests on unverified occupation, direction-count and cutoff estimates.

**In one line:** the route was chosen and its core constructed within the first 13% of the summary. The rest is local repair and audit. No restarts, no reversal of the answer, no backtrack beyond one level.

## 2. Search tree

Key: ✓ kept · ✗ conflict · ? left without a reason (unclear) · (L) = light decision · [M]/[C] = momentum or continuation subgoal · word counts are subtree lengths.
```
ROOT  T_max = ∞ for all smooth admissible data?                         (prompt)
└─ POS  affirmative: momentum bound + Glassey–Strauss continuation      1671 w  (single L1; 0 restarts)
   ├─ a1 [M] scoping: null-slab energy, direction freezing, residence    19 w  → absorbed into a5
   ├─ k0 [C] reduce to GS criterion (Luk–Strain Thm 1.1)               356 w  21%
   │   ├─ k0.1 apply directly           ✗ data not in H⁵                  14 w
   │   ├─ k0.2 Coulomb + truncated potentials + vacuum Maxwell  ✓       300 w  (re-audited 6×)
   │   └─ k1 (L) plane-projection criterion  ?                           11 w
   ├─ a2 (L) Cheverry–Ibrahim momentum spreading  ? (3 consults)          40 w
   ├─ a3 (L) Wang beyond cylindrical symmetry      ?                      14 w
   ├─ a4 (L) Serre positive stress  ✗ (implicit: Maxwell stress indefinite) 14 w
   ├─ a5 [M] Pfaffelmoser residence time + signed impulse  ✓ FINAL      1162 w  70%
   │   ├─ a5.1 signed IBP identity (accel.+transport)  ✓ partial ✗→C3    122 w
   │   ├─ a5.2 uniform directional modulus  ✗ moving-cutoff derivatives  14 w
   │   ├─ a5.3 (L) receiver smoothing + magnetic estimate  ?             14 w
   │   ├─ a5.4 count δ-exits of direction  ✓                            190 w
   │   │   ├─ a5.4.1 windows too long  ✗  →  a5.4.2 shorten by M²+A log P ✓  23 / 55 w
   │   │   ├─ a5.4.3 source + receiver counts  ✓                         18 w
   │   │   └─ a5.4.4 occupation in restricted angular window  ✓          34 w
   │   ├─ a5.5 signed bootstrap MP√I + A·I·P²L/w  ✓                      390 w
   │   │   ├─ a5.5.1 first weight ✗ short intervals → a5.5.2 revised ✓   16 / 0 w
   │   │   ├─ a5.5.3 receiver coefficient: H<.41z vs H>.496z  ✓           75 w
   │   │   ├─ a5.5.4 endpoint averaging  ✓                                 4 w
   │   │   └─ a5.5.5 doubling times ~1/log P, divergent sum  ✓            73 w
   │   ├─ a5.6 direct absolute bounds  ✓ baseline, partial ✗ (√w loss → C8) 43 w
   │   ├─ a5.7 Cheverry–Ibrahim retarded work kernel  ✗ power loss         20 w
   │   └─ a5.8 selective IBP in narrow angular sector  ✓ (partial ✗ extra log → C9) 111 w
   │       ├─ a5.8.1 θ<κφ, near/far balance ✓   ├─ a5.8.2 labels fixed ✓
   │       └─ a5.8.3 differentiated-cutoff cancellation ✓
   └─ a6 (L) Pallard characteristic-integral comparison  ?               22 w
```
Abandoned text totals 202 words (12% of the summary). The other 88% is the final route and its audits.

## 3. Metrics (CDCL coding)

| Metric | 362 | 287 (for reference) |
|---|---|---|
| summary words | 1,671 | 3,796 |
| decisions (excluding light) | 31 (25) | 69 |
| conflicts | 9 (6 abandoning + 3 partial, on kept nodes) | 47 |
| backtracks: total / conflict / insight / unclear | **11 / 6 / 0 / 5** (5 / 5 / 0 / 0 excluding light) | 48 / 46 / 1 / 1 |
| of which in-place repairs (kept_branch_repair) | 3 (k0.1, a5.4.1, a5.5.1) | — |
| distance histogram | **d=1: 11** (conflict {1: 6}; unclear {1: 5}) | d=1: 40, d=2: 7, d=3: 1 |
| max backtrack distance / max depth | 1 / 4 | 3 / 4 |
| restarts | **0** | 3 |
| subgoal switches M↔C (not backtracks) | 19 | — |
| propagations (rough) | 45 | 42 |
| learned clauses / reuse rate | 10 / **0.80** (0.60 explicit only) | 26 / 0.77 |
| share before final route (words / chars) | **0.071 / 0.078** | 0.774 / 0.777 |
| abandoned-branch length, mean / median (words) | all 18.4 / 14; conflict 16.8 / 15; unclear 20.2 / 14 | conflict 122 / 60 |
| length vs distance | undefined (all d=1) | Spearman 0.62 |
| literature: trace refs / shared with paper | 6 / 4 (hit rate 0.67) | 54 / 5 (0.09) |
| explicit time/compute markers | none; only sequencing and revisit words ("repeatedly", "Repeated audits", "returned to") | none |

Do long branches end in restarts? Not applicable: there are no restarts. No abandoned branch is longer than 22 words.

### Rule extensions used (documented in `trace.json` → `level_assignment_rules`)
- **R1, AND-subgoals.** The single strategy needs both M (a momentum bound) and C (continuation for the stated data). Moving between them is a *subgoal switch*, not a backtrack. There are 19 such switches; the summary interleaves the two.
- **R2, resumption.** An abandoned light node followed by text that continues an open kept branch counts as d = 1.
- **R3, revisits of kept nodes.** Re-audits of a kept node do not create new decision nodes. They are logged as `revisit_lines`. 287 created new nodes only when revisiting *failed* families.
- **R4, light decisions.** An alternative mentioned in at most two sentences and not pursued is flagged `light_decision`. Metrics are reported with and without light decisions.
- **R5, partial conflicts.** A stated shortfall of a kept node, handled by refinement, counts as a conflict and yields a learned clause, but is not a backtrack.
- **R6, length.** Length is computed by sentence-level segment attribution, because kept nodes are interleaved.

### Insight-driven steps
**None.** Every abandonment is either conflict-driven or unexplained.
- The closest candidate is a5.3 → a5.4. The summary says "A different possible approach smoothed receiver velocity… The present attempt instead pursued counts". That could be a bypass of a viable line or a contrast between separate attempts, so it is coded *unclear*.
- The core identity PV4 is not an insight backtrack either. Nothing was abandoned for it: it was the first move on the chosen route.

### Where the CDCL analogy breaks down
- The search looks less like CDCL than like **local repair of one fixed assignment**, in the style of WalkSAT:
  - one strategy;
  - every backtrack has d = 1;
  - three abandonments are in-place repairs;
  - most of the text re-checks the same assignment.
- The clauses are mostly *constraints on a route that is already chosen*, not reasons to leave it. Contrast 287, where they mainly justified restarts.
- The summary is audit-shaped. Sections 2–5 have the titles "Repairing and auditing", "Stress-testing", "Testing a candidate…" and "…under repeated scrutiny". Failures inside these passes are probably under-reported.

## 4. Decisive pivots

| Pivot | Trigger | Classification | Final paper | Grade |
|---|---|---|---|---|
| PV1 affirmative answer + GS continuation (L65–71) | none (initial) | known route | Thm thm:global, Section setup | — |
| PV2 field localization (L67–70, refined L90–94) | conflict C1 (data not in H⁵) | known technique, combined | Lemma cont:vacuum, eq cont:modified-data | N1 |
| PV3 Pfaffelmoser residence time (L75) | chosen among alternatives | **transfer** (VP → RVM). The paper calls it "methodological inspiration" | Section occ | N0/N1 |
| **PV4 signed impulse + signed force identity** (L76–77, L83–85) | **no visible trigger.** Derived at once; rationalised later by C6/C8 | **new concept + new bridge** on the GS representation | Prop. prop:increment; Lemma can:identity | **N2–N3 candidate** (F2 / F3) |
| **PV5 direction-change counting** (L81–83) | **conflict C4** (no uniform directional modulus) | **new bridge** (stopping-time count + signed identity + monotone crossing) | Lemmas ang:direction, ang:improved-hit | **N2–N3 candidate** (F2) |
| PV6 selective sector + exponent contradiction (L108–111, L171–174) | C3 + C6/C8 | known technique applied constructively | Section sel, Lemma sel:exponents | N2 (F3) |
| PV7 shortened windows (L112–113) | conflict C7 | known (parameter retuning) | ℓ in ang:direction; occ:lambda | N1 |
| PV8 endpoint averaging + doubling (L88, L119–121) | the need to close the bootstrap | known route (continuity; Osgood-type divergence) | Section closure; Section setup | N1 |

- **PV4 is the core and PV5 the decisive conflict-driven move. PV6 closes the loop.**
- PV4 resembles 287's core lemma in that **no lesson predicts it**. It differs in timing: it arrives at share 0.075, *before* any failure on the momentum route, rather than after a long failed search.
- PV5 is one propagation step from a learned clause, which counts as evidence of reachability.

## 5. Knowledge flow

- **C1** (the data class is not H⁵) leads to the localization, and through it to all of the paper's Section cont. *Necessary.*
- **C3**, from the identity's residue (receiver coefficient, endpoint and cutoff terms), sets the agenda for the rest of the proof:
  - counting, explicitly "to make that coefficient small" (L141);
  - the exponent contradiction;
  - endpoint averaging;
  - cutoff cancellation.
  *Necessary.*
- **C4** (no uniform directional modulus) leads to direction counting (explicit at L82–83). *Necessary.*
- **C6 + C8** (absolute bounds lose a power, namely √w, near the cone) lead to selective narrow-sector integration by parts. *Necessary.* C8 is *stated* only at L194 but is used from L108.
- **C7** (shorten the windows), **C9** (θ < κφ), **C5** (weight revision, inferred) and **C10** (non-circular order; constants independent of M, A) are technical constraints, all present in the paper.
- **Inert:** Cheverry–Ibrahim's representation, Wang beyond symmetry, receiver smoothing, the Luk–Strain plane-projection criterion. Serre (C2) is at most enabling.

**Contrast with 287.** There, the negative lessons justified restarts and the core lemma had a salvaged ingredient but no predicting lesson. Here, almost every lesson lands in the proof, because there is only one route. The core identity still has no predicting lesson.

**What was not learned.**
- The summary never explains why the √w loss and the w^(−1/2) coefficient must match exactly: substituting V_X′ = K makes the receiver term proportional to the receiver force.
- The plane-projection criterion and Wang's 2026 versions are never weighed.
- No negative-answer scenario (blow-up) is ever examined.

## 6. Eureka candidates (trace-level shortlist)

| ID | Item | For | Against | Suggested |
|---|---|---|---|---|
| E1 | Signed-increment bootstrap MP√I + A·I·P²L/w, with doubling gaps ≥ c/log P | Not a subterm of the goal. A tuned two-term form. Load-bearing everywhere | A templated "uniform/quantitative" strengthening of the standard momentum-support bootstrap (capped at N2); taking the norm after integration is natural | N2 (maybe N3), F2 |
| E2 | Signed force identity (transport + acceleration kernels = total s-derivative + R + A) | The paper names precedents for its ingredients only (GS, Luk–Strain, Pallard 2015, Lazarovici), none for the identity. Used twice. Removes the √w loss | GS-style integration by parts along characteristics is classical; the identity is a computation once one integrates in s. Derived at once, with no visible search; a physical (Liénard–Wiechert) reading suggests retrievability | **N2–N3 borderline**, F3 |
| E3 | Direction-change count C(M,A)L⁶/δ, then improved occupation at intermediate angles | Replaces an unattainable uniform modulus by a countable quantity. A clever second use of the identity (perpendicular projection) | Stopping-time counting is standard; one step from clause C4 | **N2–N3**, F2/F3 |
| E4 | Selection threshold + exponent contradiction (H < .41z vs H > .496z) | Improved occupation needs to hold only in a window | Routine exponent bookkeeping; chain depth 2 | N2, F3 |
| E5 | Field localization (negative control) | Closes a real hypothesis gap | Standard finite-propagation technique; no compression | N1 |

The trace makes E2 and E3 look *reachable* for the model: E2 has no search, and E3 is one step from a clause. Whether they are hard to discover must be settled by the hidden-item discovery test. This trace is too compressed to settle it.

## 7. Verification behaviour and self-assessment

**Self-refutation.**
- A weight fails at short intervals (L86).
- The counting windows are too long (L112).
- Absolute bounds lose √w (L194).
- The Cheverry–Ibrahim kernel leaves a power loss (L106).

**Circularity checks.**
- Dependency order (L114–115).
- No double charging of force integrals (L142).
- Constants independent of the bootstrap constants (L178).

**Checks on the final route.**
- Repeated reconstruction of the Glassey–Strauss decomposition (L134).
- Retarded Jacobians, cone-tip integrability and boundary-crossing cells (L176–177).
- Luk–Strain normalization and H⁵ hypotheses (L179–180).
- The VERBATIM conservation-law check (L165–167). It is the only visible self-doubt about the mechanism, and it is answered by physical intuition, not a proof.

**Absent.**
- Any exploration of the negative answer.
- Numerical experiments.
- Consistency checks against known special cases: small data, Wang's cylindrical case, 2½-D results.
- The summarizer's closing hedge (L209–211) explicitly separates "asserting" from establishing.

## 8. What the trace tells us that the paper cannot

1. **Direction of search.** There was none to speak of: the affirmative route was chosen at once. The paper's "Proof strategy" reads as the plan the model actually followed from L75. This is the opposite of 287.
2. **Order of discovery.** The core identity (share 0.075) and the direction counting (0.11) came *before* the √w loss was even stated (0.86). The paper presents the √w loss as the motivation. The trace shows the motivation was rationalised afterwards, or else the summarizer reordered.
3. **Exact numerical continuity.** The trace's exponents H < 0.41z and H > 0.496z, the window factor M² + A log P and the count log(2+P)^C/δ all survive into the paper: Lemma sel:exponents exactly, ℓ and λ, and L⁶/δ. The route the trace reports is the route in the paper, not a sketch later replaced.
4. **Provenance.**
   - Wang's July 2026 papers (arXiv:2203.01199v2, "to appear in Annals", and arXiv:2607.14685), which the paper discusses, are absent from the trace; it cites only the 2022 v1.
   - Lazarovici 2016 (the label change) and Pallard 2015 (acceleration-kernel orthogonality) are paper-side attributions. The trace uses the label device without citing it.
   - The latest-dated trace reference is from 2025.
   - The discovery test must exclude Wang 2026 I and II.
5. **Possible hidden search.** "The present attempt" (L81) suggests that earlier attempts, not shown, may exist.

## 9. Comparison with 287

| | 287 (free group factors) | 362 (relativistic Vlasov–Maxwell) |
|---|---|---|
| shape | search-dominated: about 38 abandoned approaches across *both answers* | audit-dominated: one route, 5 passes of repair and stress-testing |
| restarts / max distance | 3 / 3 | 0 / 1 |
| share before final route | 0.77 | 0.07 |
| insight backtracks | 1 (semicircular S → Arg C) | 0 |
| literature hit rate | 0.09 (49 of 54 references are dead ends) | 0.67 (only Cheverry–Ibrahim and Serre are dead ends) |
| learned-clause role | mostly enabling restarts; salvaged tools in the proof | almost all are constraints that land in the proof |
| core step | small cocycle (PV4): no trigger, after a long failed search, chain depth 2 | signed identity (PV4): no trigger, *at the start*, chain depth 0, then conflict-driven counting (PV5) |
| eureka shortlist | PV4 N3 candidate (F3) | E2 and E3, N2–N3 borderline (F3, F2) |

Both traces share one pattern: **the core constructed step has no predicting lesson.** They differ in when it comes. In 287 it comes after exhaustion. In 362 it comes immediately. On the trace evidence alone, then, 362's key ideas look easier for the model to reach than 287's. This conclusion is weakened by the extreme compression (about 1,700 words for a 17,500-word proof) and by the hint of unshown prior attempts.

## 10. Notes for the remaining traces

- **Apply extensions R1–R6** wherever a trace commits early and spends most of its text auditing:
  - AND-subgoals;
  - resumption;
  - revisits of kept nodes;
  - light decisions;
  - partial conflicts;
  - segment-based length.
- **Report an "audit share"** (here 0.78: sections 2–5) alongside the share before the final route.
- **Report the ordering anomaly.** When the summary *states* a motivation (here the √w loss) after the remedy is already in use, record both positions.
