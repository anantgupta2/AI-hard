# Family 287: reasoning-trace analysis ("Isomorphism of the free group factors")

Source: `data/traces/287.txt`, OpenAI's 11-page *summarized* chain of thought. The summary body (references excluded) is about 3,800 words in 7 sections. Machine-readable coding is in `trace.json`. Line numbers (L) refer to the .txt file.

**Read this first.** The trace is a curated summary in the summarizer's voice, with five short VERBATIM excerpts. Everything below concerns *what the summary reports*. Lengths measure how the summary allocates text, not the model's compute. Backtracks that the summarizer compressed are invisible.

## 1. The story of the search

**Sections 1–5a (L16–220, about 59% of the text): the model tries to prove non-isomorphism.** It works through almost every known invariant and obstruction programme:
- the Dykema–Rădulescu dichotomy and absorption equivalence;
- the Boutonnet–Drimbe–Ioana–Popa (BDIP) nonseparable free-power invariant, tried in all 7 sections;
- deformation/rigidity and unique Cartan;
- strong 1-boundedness and 1-bounded entropy;
- microstate entropy, then width dimension, then equivariant encodings;
- Connes–Shlyakhtenko L²-homology, against Popa–Vaes vanishing;
- free-Jacobian rank;
- proper proximality and the Julg–Valette index;
- Gaboriau cost and ℓ²-Betti numbers;
- corner self-similarity;
- Fox-derivative closability;
- free dimension of embeddings;
- iterated hypothetical changes of generators;
- free Stein dimension.

Each attempt dies for one of three reasons:
1. the invariant is constant on the family;
2. the invariant depends on a presentation, and an abstract isomorphism need not preserve that presentation;
3. a needed estimate (closability, derivative control, continuity moduli) fails for rough, measurable changes of generators.

Two by-products survive. The first is a correct but circular reformulation, L(F₂)≅L(F₃) ⇔ 1/√2 ∈ 𝓕(L(F₂)), which brings the amplification calculus. The second is a toolkit met inside failures: Fox prefix calculus, Haar conjugates *b, cbc\**, Nielsen moves, and error recursions.

**Section 5b (L221–244): first constructive turn.** It is prompted by Ornstein–Weiss and Bowen, used as a classical analogy (the model writes "Aha!"). Free Haar vertex unitaries on the Cayley tree have free edge increments. A nonzero mean recovers the missing root, but exact freeness is lost. A spectral-gap argument then shows that free generating tuples cannot be reached by small perturbation of this construction.

**Section 6a (L245–259): relapse.** The model goes back to microstate invariants and writes "Same old."

**Sections 6b–7 (L260–342, the last 22%): the final route.**
1. Straight cocycle paths fail.
2. The model proposes a polynomial flow, dA_j/dt = i(Σ_g h_j(g) A_g S A_g\*) A_j, driven by conjugates of an auxiliary variable S.
3. Word displacement under this flow is governed by the Fox cocycle D_w. A word with many free prefixes, together with a spectral-cutoff inverse of P = 1+Σλ(p_r), makes ‖h‖₂ small while D_w ≈ δ_e. The limit has Catalan moments, a Marchenko–Pastur law and no atom at 0.
4. The semicircular S is replaced by the bounded Borel logarithm S = Arg(C).
5. A free-sum bound of 3π‖h‖₂.
6. The model corrects its own target from C to CA_w and inverts it with a Nielsen automorphism.
7. Adaptive diagonal iteration.
8. Generation is proved by L²-density.
9. Amplification transfers the rank-3/4 result to ranks 2/3.

The summary closes in hedged terms: the resolution is "proposed", and it "depends on" the flow and generation steps.

## 2. Decisive pivots

| Pivot | Trigger | Classification | Eureka? |
|---|---|---|---|
| PV1 NEG→POS (L201/221) | accumulated conflicts, no single trigger | strategic | no |
| PV2 Cayley-tree root recovery (L221–244) | retrieved Ornstein–Weiss [39] / Bowen [7] | **transfer** from ergodic theory along a folklore route; dropped | no |
| PV3 absorption by a polynomial trace-preserving flow (L260–271) | failed straight cocycle paths | known technique adapted (Voiculescu cyclomorphy [52], recalled *after* the field was proposed) | N2 |
| **PV4 small cocycle with prescribed word value** (L272–284) | no visible trigger; recycles Fox derivatives from the failed §3a | **new bridge**: Fox calculus + Haagerup + free Poisson spectral limit | **N3 candidate, F3**; chain depth 2 (needs PV3 and the free-sum bound) |
| PV5 S = Arg(C) + CA_w/Nielsen (L289–315) | its own C\*-algebra sanity check, then **insight** | known tools used for a change of representation | N2 (F5 flavour) |
| PV6 free-sum 3π bound | need created by PV5 | known (Ricard–Xu-type; cited in the paper, not in the trace) | N0–N1 |
| PV7 adaptive budgets + L² generation | §4 error-compounding lesson, inverted | known; named precedent Shlyakhtenko 2026 | N1–N2 |

**The decisive pivots are PV3 and PV4 together, with PV4 the core.** PV4 is the only step with no stated trigger and no matching retrieved item. Its pivot distance is at least 2 from anything invoked, although every ingredient is in L.

## 3. CDCL coding of the search

### Level-assignment rules (apply verbatim to the other traces)
- **L0** is the posed problem.
- **L1** is the strategy, meaning a commitment to the *answer* plus a proof architecture: NEG (non-isomorphism) or POS (construct an isomorphism). A switch between them is a **restart**, and each re-entry is a new L1 node.
- **L2** is an approach family, named by its central tool or invariant. A paragraph that changes the central tool opens a new L2 node. A revisit gets a new node that points to the earlier clause.
- **L3+** is a variant or sub-construction that the summary presents as a refinement ("then", "pursues", "replaced", "returning to").
- **Conflict** is recorded only for a *stated* failure. A parent whose children all failed has no conflict of its own. A node left without a stated reason has an `unclear` trigger.
- **Backtrack** happens when the next node is not a child of a failing node. Its distance is d = level(failing) − (level(next) − 1).
- **Trigger** is one of three values. `conflict` means a stated failure. `insight` means a viable branch was bypassed by a simpler idea (subsumption). `unclear` covers the rest.
- **Length** is the words from a node's first line to the next node outside its subtree, with page headers excluded and ±1 line of slack.

### Tree (condensed; 69 decision nodes in JSON)
```
ROOT  L(F2) ≅ L(F3)?
├─ NEG1 (L16-220, 2366 w, 62%)  find invariant / contradiction
│   ├─ a1 nonseparable BDIP ✗no-transport     ├─ a2 rigidity/Cartan ─ a2.1 ✗ a2.2 ✗
│   ├─ a3 trace-scaling flow ✗circular        ├─ a4 s1b / 1-bdd entropy ✗constant
│   ├─ a5 microstates ─ a5.1 Minkowski ✗ ─ a5.2 width ✗cex ─ a5.3 equivariance ✗cex
│   ├─ a6 L²-homology ✗constant  a7 ✗  a8 Jacobian rank ✗cex  a9 Julg–Valette ✗cex
│   ├─ a10..a16 absorption, Shen, cost, corners, ultralimit, Fock, gap-iteration ✗
│   ├─ a17 Fox closability ─ a17.1..a17.4 ✗   (salvage: prefix calculus C15)
│   ├─ a18 conditional absorption ─ a18.1 ok, a18.2..a18.4 ✗
│   ├─ a19 1/√2 ∈ F(N2) ✗circular (salvage: amplification C16)
│   └─ a20..a29 embeddings, witnesses, sweep, error recursion (C17), Baire, ... ✗
│        ══ RESTART 1 (L221) ══
├─ POS1 (252 w)  b1 Cayley tree ─ b1.1 "Aha!" freeness lost ✗ ─ b1.2 ✗ ─ b1.3 ok ─ b1.4 spectral gap ✗
│        ══ RESTART 2 (L245) ══
├─ NEG2 (171 w)  c1 "Same old" ✗ c2 ✗ c3 Urysohn/Borsuk–Ulam ✗ c4 ✗
│        ══ RESTART 3 (L260) ══
└─ POS2 (858 w, 23%)  d1 absorb a free generator
    ├─ d1.1 straight cocycle paths ✗
    ├─ d1.2 flow with semicircular S ─ d1.2.1 small cocycle ✓ ─ d1.2.2 iteration ✓ ─ d1.2.3 C*-check ✗
    │        ── INSIGHT backjump (d=2) ──
    └─ d1.3 S = Arg(C) ─ free-sum ✓ trace ✓ target fix (✗→✓) Nielsen ✓ L²-gen (✗→✓) checks ✓ amplification ✓
```

### Metrics
| Metric | Value |
|---|---|
| decisions / conflicts | 69 / 47 |
| backtracks: total / conflict / insight / unclear | 48 / 46 / **1** / 1 |
| distance histogram (all) | d=1: 40, d=2: 7, d=3: 1 |
| conflict / insight / unclear | conflict {1:39, 2:6, 3:1}; insight {2:1}; unclear {1:1} |
| max backtrack distance, max depth | 3, 4 |
| restarts | 3 (NEG→POS→NEG→POS) |
| propagations (rough) | 42 |
| learned clauses / reuse rate | 26 / 0.77 |
| share of trace before final route | 0.78 (chars), 0.77 (words) |
| abandoned-branch length, mean / median (words) | conflict 122 / 60 (66 / 55 excl. restarts); insight 285 (n=1); unclear 36 |
| length vs distance | Spearman 0.62, Pearson 0.40. Mean length: d=1 57 w, d=2 488 w, d=3 252 w |
| explicit time/compute markers | **none**. Only revisit words ("again", "returning", "revisited", "Same old", "Finally") |

Do long branches end in restarts? Mechanically yes, because a restart abandons a whole strategy. At the leaf level, no. The last straws before each restart are ordinary-length leaves: 132, 92 and 30 words, against a median leaf of 44. Restarts follow an *accumulation* of conflicts, not one long failure. The correlation is inflated by this mechanical effect.

### Abandoned branches by length (top 20 of 57; full list in JSON)
| node | lvl | words | share | children | refs | outcome / obstruction |
|---|---|---|---|---|---|---|
| NEG1 | 1 | 2366 | .623 | 42 | 44 | restart; all invariants blocked |
| d1.2 | 3 | 285 | .075 | 3 | 5 | **superseded (insight)** by Arg(C) |
| POS1 | 1 | 252 | .066 | 5 | 4 | restart; freeness lost |
| a5 | 2 | 199 | .052 | 3 | 2 | microstate/width: counterexamples |
| a18 | 2 | 176 | .046 | 4 | 5 | conditional absorption: missing compactness |
| NEG2 | 1 | 171 | .045 | 4 | 10 | restart; relearning |
| a23 | 2 | 132 | .035 | 0 | 14 | sweep blocked by old clauses |
| a29 | 2 | 132 | .035 | 0 | 4 | BDIP + Nielsen: no transport |
| a19 | 2 | 128 | .034 | 0 | 3 | circular reformulation (kept tool) |
| a17 | 2 | 125 | .033 | 4 | 5 | Fox closability (kept tool) |
| a1 | 2 | 121 | .032 | 0 | 4 | nonseparable: no transport |
| a22 | 2 | 100 | .026 | 0 | 1 | witnesses not preserved |
| a13 | 2 | 97 | .026 | 0 | 1 | corners: error magnification |
| a2 | 2 | 93 | .025 | 2 | 3 | rigidity: uncontrolled unitary |
| b1.4 | 3 | 92 | .024 | 0 | 1 | spectral-gap isolation |
| a5.2 | 3 | 88 | .023 | 0 | 0 | rounding counterexample |
| a10 | 2 | 86 | .023 | 0 | 3 | absorption + rigidity |
| a25 | 2 | 84 | .022 | 0 | 5 | Baire radius, etc. |
| b1.1 | 3 | 83 | .022 | 0 | 1 | freeness lost ("Aha!") |
| a24 | 2 | 78 | .021 | 0 | 1 | error compounding |

### Insight-driven steps
Only **one** backtrack is insight-driven: **d1.2 → d1.3, replacing the semicircular driver with S = Arg(C)**.
- **What was left open.** The semicircular branch was not refuted. It still had two hard open subgoals: a measurable Haar reparametrization of S, and whether a continuous Haar function can generate the semicircular algebra. It also depended on semicircular stability.
- **What the new route costs.** One line (e^{iS}=C, so the flow fixes C) plus one standard Khintchine-type lemma (3π). That is roughly 2–3 open subgoals traded for 1 standard lemma, or about 2:1 in text.
- **Origin.** Constructed: a known object put to a deliberate representational use.
- **Grading.** Novelty candidate, likely N2.
- **A trade-off the trace does not mention.** With semicircular S the free-sum bound is trivial. The switch costs a lemma.

Every other abandonment is presented as conflict-driven. Two readings are possible: the summarizer narrates failures more than shortcuts, or the model rarely abandons a viable line. The trace cannot tell these apart.

### Where the CDCL analogy breaks down
- **The levels are reconstructed.** The summary does not mark commitments.
- **The summary is curated.** Within-paragraph backtracks are compressed, so counts are lower bounds. The final route gets far more text per idea than the dead ends do.
- **The "clauses" are informal lessons.** There is no unit propagation, no clause database and no watched literals. "Reuse" is judged by reading, and 4 of the 9 load-bearing reuses are my inference.
- **Clause retention is poor.** BDIP is re-tried in every section, and the whole of NEG2 is relearning ("Same old"). That looks more like restarts with phase saving than like CDCL clause learning.

## 4. What the model learned (knowledge flow)

Each of the 57 abandoned or repaired nodes carries a `lesson` object in the JSON. The flow is:
- **Negative clauses enable the restarts but are not in the proof.** C1, C2, C4, C7 and above all **C14** ("an abstract isomorphism need not preserve the auxiliary structure you use") exhaust NEG and motivate construction.
- **Salvaged tools are in the proof:**
  - C15, the Fox prefix calculus from the failed closability attempt, becomes the cocycle rule and prefix sums;
  - C16, the amplification calculus from the circular reformulation, gives the final rank transfer;
  - C17, error compounding, is inverted into adaptive budgets (inferred);
  - the Haar-conjugate device b, cbc\* from a22 becomes S_g (inferred);
  - Nielsen substitutions from a29 become the inverse Nielsen step (inferred).
- **Constraints shape the design:**
  - C8, "small difference, huge derivative", leads to a design that never differentiates residuals;
  - C19, spectral-gap isolation, means generation comes only in the limit;
  - C20 forces a nonlinear flow;
  - C21, a C\*-algebra K-theory sanity check that mirrors the earlier Julg–Valette lesson C9, forces the Borel logarithm.
- **Doubtful lesson.** Read globally, b1.4 sits uneasily with the final result. That result produces a free generating n-tuple of L(F_{n+1}) as a norm limit of non-generating free tuples. It is plausible only as a local statement. The paper and Lean analysts should check it.
- **Not learned.** The model never treated the self-consistency of its conditional "affirmative" computations (a18), or the expected non-invariance of δ, as evidence for the affirmative answer. Fox derivatives sat in the toolkit for about 40% of the trace before being used constructively.

**The knowledge flow explains the frame of the proof but not its core.** The small-cocycle lemma has a salvaged ingredient but no predicting lesson.

## 5. What the trace tells us that the paper and Lean cannot
1. **Direction of search.** About 78% of the effort went to the *opposite* answer. The final paper reads as if construction were the obvious plan.
2. **Retrieval vs construction.** The flow was proposed and *then* matched to cyclomorphy. The small cocycle has no retrieved antecedent. Ornstein–Weiss was retrieved and dropped.
3. **Provenance gaps.** The paper's closest precedent, Shlyakhtenko arXiv:2609.11074 (10 Sep 2026, "finite automorphisms and a limiting generation argument"), is **absent from the trace**, even though the trace cites 2026 preprints up to August. Fox 1953 and Ricard–Xu are paper-side attributions added after the fact. 49 of the trace's 54 references are dead-end literature.
4. **Verification status.** The model runs real self-refutation: about 8 self-built counterexamples, about 3 circularity detections, and about 9 checks on the final route. But the summary ends in "proposed/intended" language. The paper's entropy-dimension corollary never appears in the trace.

## 6. Recommendations for the other 9 traces
- **Segmentation.** Code nodes with the level rules above. Record line spans, words, references and the trigger type for every backtrack.
- **Per-node fields.** Include the `lesson` fields: obstruction, form, generality, known-in-literature, correctness, salvage, influence, not-learned.
- **Pivot fields.** Record the trigger, classification (known / transfer / known route / new bridge / new concept), pivot distance, chain depth, and *retrieval-before-vs-after-construction*.
- **Corpus metrics.**
  - share before the final route;
  - restarts;
  - histogram of d by trigger;
  - clause reuse rate;
  - salvage rate (final-proof items first seen inside a failed branch);
  - literature hit rate (trace ∩ paper references / trace references);
  - the insight-backtrack rate. Every insight step goes to novelty grading.
- **Provenance.** List the paper's named precedents that are missing from the trace, and the latest-dated reference in the trace. Exclude both from the contamination-controlled discovery test.
- **Voice tagging.** Tag VERBATIM vs narration and code hedging verbs. Have two coders on levels and triggers, and target κ ≥ 0.6 before scaling.
