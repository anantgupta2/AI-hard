# Family 197: reasoning-trace analysis ("Kaplansky direct finiteness in characteristic two")

Source: `data/traces/197.txt`, OpenAI's 23-page *summarized* chain of thought. It has two parts:
- **Part I** (secs 1–22, L60–864) is the direct-finiteness problem. Its body, without the prompt excerpt, is **9,104 words**.
- **Part II** (sec 23, L865–924, 708 words) is a separate prompt on Gottschalk surjunctivity. It takes the char-2 witnesses as input.

The family has four manuscripts. The trace corresponds to *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two* (Sep 23, 2026).
- The Determinant-Conjecture companion (same date) uses that paper's char-2 pair as input.
- The odd-characteristic paper (Sep 26) and the torsion-free headline paper (Oct 4) are **not covered by the trace**. The trace's construction uses odd-order torsion essentially.

Machine-readable coding is in `trace.json`, which uses the same schema as 287 plus documented extensions. L numbers refer to the .txt file.

**Read this first.** The trace is a curated summary in the summarizer's voice, with about 25 short VERBATIM excerpts. Everything below is about *what the summary reports*. Lengths measure how the summary allocates text, not compute. Compressed backtracks are invisible, so all counts are lower bounds.

**Computer-assisted? No.**
- The summary reports no search, code, SAT run, numerical experiment or tool use.
- Two calculations could be read either way, the "char-2 calculations with two copies of S3" (L263) and the "finite elimination" (L291). Both are presented as reasoning.
- The paper states that its terminating prescription "has not been executed". The finite search in the paper's §5 is a *definitional* device that makes the witnesses canonical; it is not a search that was run.
- Dykema–Heister–Juschenko [17] is a computer-search paper on ULIE groups, but the model only cites it.

## 1. The story of the search

**Secs 1–10 (L60–401, 42.5% of the body): rapid oscillation between proving direct finiteness (PROVE) and constructing a counterexample (CEX).** About 83% of this stretch is PROVE.

**PROVE routes.** Each needs a positivity, conservation or approximation principle that is unavailable for arbitrary groups:
- the sofic and surjunctive theorems (Elek–Szabó; Ceccherini-Silberstein–Coornaert–Phung);
- Witt-vector lifts;
- entropy on linear subshifts;
- random-priority pivot densities;
- skew group rings;
- spectral amplification and determinant obstructions, which are conditional on Lück's determinant conjecture;
- **char-2 sign lifting** to characteristic 0 via a central involution *z*, which is killed by odd-area spherical diagrams;
- random valuations;
- information indices (Gross–Nesme–Vogts–Werner);
- p-adic and integral lifting, which loses finite support;
- entropy-balance invariants for split circuits, refuted by the model's own free-group graph-state example;
- the Hattori trace;
- Gaussian channels with I–MMSE;
- "information from infinity", Brownian bridges and a spatial Poincaré inequality;
- lattice theta and Bombieri–Vaaler bounds;
- MTP pressure inequalities;
- a correct structure theorem confining any defect to a "vertical" component over finitely many primes (a36).

Five of the seven excitement markers in the trace sit on these PROVE routes: "full proof if", "Excellent", "This is huge", "Excellent! No support degree!" and "New promising". All of those routes fail.

**CEX routes.** These are short (642 words in total), but they contain the eventual mechanism.
- **C1, secs 2–3, share 0.07–0.11.**
  - Finite-subgroup averages reduce the problem to double-coset congruences.
  - Incidence designs collapse the presented group.
  - Jacobson/Leavitt-algebra constructions are killed by a rank count.
  - Then comes the key step: **averaging idempotents of odd-order finite subgroups (invertible in char 2) give a rectangular one-sided factorization**. That needs faithful subgroup embeddings and compatible character projections. "Dense identifications threatened collapse, while high-girth constructions exceeded the required size bound."
  - Cosets: "Cosets give much more flexibility!", under the budget Σ|K_i|⁻¹ ≤ 1.
- **C2/C3, sec 4.** Subgroup covering Σ K̂_i = 1 in 𝔽₂[N] by odd-order elementary abelian subgroups, then a cylinder-set relaxation. A de Bruijn–Erdős cost bound kills tree-like configurations.
- **C4, sec 7.** A 3-line S3×S3 corner, excluded.

**Sec 10 end – sec 12 (L402–488, 11.6%): the final route is constructed in a short burst.**
1. Rank-one matrix weights: Σ K̂_i W_i = I_m, with cross terms forcing full Gram cancellation (L402).
2. The **hypergraph formulation** (L410): rank-one x_v x_vᵀ vanishing on every hyperedge, total rank m, t ≤ m(D−1)², incidence girth ≥ 12 for embeddings.
3. A proposed rank inequality is refuted by polynomial evaluation examples (L415).
4. Golowich–Lin and Dinur–Liu–Zhang are recalled, which gives the **punctured affine space** (L422–439). Interpolation polynomials at holes O ⊂ 𝔽_q^n (q = 2^h) have products of degree ≤ q−2, so they sum to zero on every full line, and the retained points give Σ W_v = −I_m.
5. Radial-line trades plus a generic local lemma fail: "Need b<a−1 for rare. Generic LLL wanted b>a+4. Conflict!"
6. The fix is a punctured-plane tiling by an eigenvector-free J. This is exactly the paper's slab-partition lemma.
7. Plan: HNN character twists, a finite-group matrix corner, and Linnik.
8. Complete draft (sec 12). Haefliger developability is replaced by a planar Euler argument (the only insight backtrack). Then character packing with m < t ≤ mℓ², an augmentation rank certificate, and the DHJ finite-factor step.

**Secs 13–22 (L489–864, 45.9% of the body): ten audit passes.** The model:
- repairs the minimality scope of the embedding proof twice;
- makes the Euler counts explicit (B ≤ E/3, W ≤ E/2+½, F ≤ E/6+1 against B+W+F = E+2);
- discovers that the construction **cannot lift to characteristic 0**, because summing the line identities gives D·ΣW_v = 0 and D = 0 only in K: "Thus no lift. Positive characteristic essential.";
- tests the construction against Farrell–Jones, Bartels–Lück–Reich, DLMSY, Berlai, Wise, Ollivier–Wise, Slofstra, finite quotients and perfect matchings;
- tries twice to replace Linnik. One attempt fails. The other, Chebyshev plus a Rankin smooth-number bound, looks viable but is not adopted;
- explores girth 14 and hexagon exclusion (n = 10b → 12b) without adopting either.

The summary ends with the candidate "retained" and still under scrutiny.

**Part II (sec 23)** is linear and has no dead ends. T_c(x)(g) = Σ c_u x(gu), the order is checked, and T_aT_b = id. The delta configuration at h with (ba)_h ≠ 1_h lies outside the image. This becomes the paper's cellular-automata section.

## 2. Decisive pivots

| Pivot | Where | Trigger | Classification | Grade |
|---|---|---|---|---|
| PV1 PROVE→CEX (9 switches) | L113…L402 | accumulated conflicts; the first switch has no stated trigger | strategic | – |
| PV2 glued subgroup averages → rectangular factorization; embeddings, characters, size budget | L113–142, L174 | own reformulation b1; collapse lesson K9 | new bridge (known device, new use) | N2, F3 |
| **PV3 incidence criterion** (thm:criterion) | **L402–416** | **no visible trigger for the re-entry**; content follows from K11, K12 and K19 | **new concept** | **N3 candidate, F5/F3**; chain depth 1 |
| **PV4 punctured polynomial pairing** (prop:pairing) | **L422–439** | **retrieved** Golowich–Lin [22] and Dinur–Liu–Zhang [15], plus the inferred precursor K20 | **transfer** from coding theory (new bridge) | **N2, F3**; chain depth 2 |
| PV5 exact trades + eigenvector-free J tiling + LLL + Linnik | L427–462 | conflict ("Conflict!", K21) | known technique adapted | N1–N2 |
| PV6 planar Euler embedding replacing Haefliger | L469–473 | **insight** | known technique (small cancellation) | N1 |
| PV7 character packing + specialization rank certificate | L473–477 | K11, K12; K10 inferred | known techniques combined | N2, F5 |
| PV8 finite-group matrix units (DJ/DHJ) | L97, L147, L477 | retrieved | known | N0 |
| PV9 Linnik prime ℓ ≡ −1 mod q¹⁰⁰ | L448, L461 | retrieved | known | N0 |

**The decisive pivots are PV3 and PV4 together.**
- **PV3** is the constructed core. It is one step from the model's own early CEX lessons (K11 and K12, learned at shares 0.09–0.10 and last applied at 0.15). Those lessons then lay dormant until 0.425.
- **PV4** is a retrieval-triggered transfer that instantiates PV3. Characteristic two enters here: the regular degree ℓ+1 must vanish in K, which needs q | ℓ+1 and hence Linnik.

## 3. CDCL coding of the search

### Level-assignment rules (287's, plus documented extensions)
- **L0.** The posed problem. Part II is a separate tree (`part_II`) and is excluded from all metrics.
- **L1.** Strategy, meaning a commitment to the answer. PROVE plays the role of 287's NEG, and CEX the role of POS. A switch between them is a **restart**, and each re-entry gets a new node (P1–P5, C1–C5).
- **Extension 1.** Strategy-neutral reductions (ULIE presentations, the Dykema–Juschenko finite factor) are L2 tool nodes. They do not trigger restarts.
- **Extension 2.** Interjections that the summary marks as parallel ("Meanwhile", L185), or that last ≤ 3 lines (L263–265), are coded as restarts but flagged `interleaved`. This applies to 4 of the 9 restarts.
- **L2 and L3+.** Approach family, then refinement, exactly as in 287. In the final route, the audit sections form one L3 node (e1.4) with L4 children of three kinds:
  - **checks**: non-failing, so no backtrack;
  - **repairs**: `kept after repair`, which is a backtrack with `kept_branch_repair`, as for 287's d1.3.3;
  - **dropped optional strengthenings**: ordinary abandoned decisions.
- **Conflict, backtrack, distance and trigger.** Identical to 287: d = level(failing) − (level(next) − 1).
- **Length.** Words between *phrase anchors*, not lines, because several approaches share a line. Page headers and the prompt are excluded.

### Tree (condensed; 129 decision nodes in JSON)
```
ROOT  ab=1 ⇒ ba=1 in char-p group algebras?
├─ P1 PROVE (L60-113, 659 w)  a1 framing(K1) a2 Witt✗ a3 entropy✗ a4 ULIE(tool) a5 pivots✗ a6 skew✗ a7 spectral✗
│     a8 sign-lift ─ a8.1 odd spherical diagrams✗(K7) a8.2 Gardam✗ a8.3 ?   a9 DJ/ULIE(tool,K13)
│     a10 valuations✗ a11 Lück det.✗(K6) a12 parity✗ ─ a12.1 single-element lemma (partial)
│        ══ RESTART 1 (L113) ══
├─ C1 CEX (333 w)  b1 subgroup averages ─ b1.1 designs collapse✗(K9)   b2 Jacobson/Leavitt ─ b2.1✗ b2.2 rank-killed✗
│     b3 ODD-ORDER AVERAGES → RECTANGULAR U,T; need embeddings+characters ✗size(K11) ─ b3.1 Slofstra ? ─ b3.2 cosets Σ|K|⁻¹≤1 ✗(K12)
│        ══ RESTART 2 (L143) ══
├─ P2 PROVE (366 w)  a13 dimension✗ a14 DHJ matrix→scalar(tool) a15-a19 ✗ (p-adic: K16) a20 ? a21 ULIE finite models ─ ✗✗✗
│        ══ RESTART 3 (L174) ══   C2 CEX (58 w) b4 covering Σ K̂_i = 1 in F2[N] (conditional)
│        ══ RESTART 4 (L185, "Meanwhile") ══   P3 PROVE (47 w) a22 rational eigenvalue✗
│        ══ RESTART 5 (L188) ══   C3 CEX (190 w) b5 Arkhipov ? ─ b6 cylinder ─ b6.1✗ b6.2 de Bruijn–Erdős "Excellent"✗ b6.3 ?
│        ══ RESTART 6 (L204) ══
├─ P4 PROVE (642 w)  a23 ? a24 X≅Y×Z entropy✗ a25✗ a26 circuit W ✗graph-state(K15) a27✗ a28 shear-dilation✗
│     a29 sign-lift again ✗(K7 explicit) ─ a29.1✗ a29.2✗  a30 spectral✗ a31 Hattori trace✗(K17)
│        ══ RESTART 7 (L261, 3 lines) ══   C4 CEX (61 w) b7 S3×S3 corner✗
│        ══ RESTART 8 (L266) ══
├─ P5 PROVE (1513 w)  a32 ? a33 M=I+pC ─ OW✗ I-MMSE "full proof if"✗ … Bombieri–Vaaler✗
│     a34 info from infinity ─ "This is huge"✗ Poincaré✗ Bell✗ ?   a35 Gaussian/theta "Excellent!"✗ ✗ ✗
│     a36 vertical component (correct partial, K18)  a37✗ a38 telescoping✗ a39✗ a40 MTP "New promising"✗ a41✗
│        ══ RESTART 9 (L402) ══  ← no stated trigger
└─ C5 CEX final (5235 w, 57.5%)  e1 incidence criterion
    ├─ e1.1 Σ K̂_i W_i = I_m, cross terms (K19)
    ├─ e1.2 hypergraph + girth 12 ─ e1.2.1 rank ineq. refuted by polynomials✗(K20) ─ e1.2.2-5 ✗/?
    │     └─ e1.2.6 PUNCTURED AFFINE SPACE (GL, DLZ) ─ e1.2.6.1 trades+LLL "Conflict!"✗(K21) ─ e1.2.6.2 J-tiling ✓ ─ e1.2.6.3 plan ✓
    ├─ e1.3 complete draft ─ e1.3.1 Haefliger ──INSIGHT──▶ e1.3.2 planar Euler ✓ ─ e1.3.3 packing+rank certificate+DHJ ✓ ─ e1.3.4 ✓
    └─ e1.4 audits (secs 13-22, 4182 w, 45.9%): repairs ×3 (K24), Linnik replacement✗(K22), D·ΣW=0 ⇒ no char-0 lift (K23),
          girth-14 ?, hexagons ?, Chebyshev–Rankin ? (unused), 11 checks passed, hexagon correction 10b→12b (left)
```

### Metrics
| Metric | 197 | 287 |
|---|---|---|
| decisions / conflicts | 129 / 69 | 69 / 47 |
| backtracks: total / conflict / insight / unclear | **80 / 62 / 1 / 17** | 48 / 46 / 1 / 1 |
| distance histogram (all) | d=1: 63, d=2: 13, d=3: 4 | 40 / 7 / 1 |
| by trigger | conflict {1:51, 2:9, 3:2}; insight {1:1}; unclear {1:11, 2:4, 3:2} | conflict {1:39, 2:6, 3:1}; insight {2:1}; unclear {1:1} |
| max backtrack distance / max depth | 3 / 5 | 3 / 4 |
| restarts | **9** (5 excluding interleavings): P→C→P→C→P→C→P→C→P→C | 3 |
| propagations (rough) | 177 | 42 |
| learned clauses / reuse rate | 31 / **0.84** | 26 / 0.77 |
| share of body before final route | **0.425** (words), 0.431 (chars) | 0.774 / 0.777 |
| final route = construction + audit | 0.116 + 0.459 | 0.23 |
| abandoned-branch length, mean / median (words) | all 117 / 49; conflict 114 / 46 (73 / 44 excl. restarts); insight 36; unclear 133 / 65 | conflict 122 / 60 |
| length vs distance | Spearman 0.54, Pearson 0.51 (excluding restarts: 0.42 / 0.46). Mean length by distance: d=1 62 w, d=2 299 w, d=3 387 w | 0.62 / 0.40 |
| explicit time/compute markers | **none**; only "again", "returned", "repeatedly", "Finally"; four section titles say "Repeated audits/scrutiny" | none |

**Do long branches end in restarts?** Mechanically yes. The PROVE blocks P1, P2, P4 and P5 run to 659, 366, 642 and 1,513 words. At the leaf level, no: the last straws before restarts are ordinary leaves (median 55 words, against 36 for other leaves), and 4 of the 9 restarts are short interleavings. The correlation between length and distance is mostly this mechanical restart effect.

### Abandoned branches by length (top 20; full list in JSON)
| node | lvl | words | share | desc. | refs | outcome / obstruction |
|---|---|---|---|---|---|---|
| P5 | 1 | 1513 | .166 | 24 | 7 | restart; information from infinity, finite→infinite volume |
| P1 | 1 | 659 | .072 | 16 | 11 | restart; no positivity; sign lift dies |
| P4 | 1 | 642 | .071 | 12 | 9 | restart; entropy balance refuted, lifts lose support |
| a34 | 2 | 432 | .047 | 5 | 2 | info from infinity: children failed |
| a33 | 2 | 392 | .043 | 6 | 4 | M = I+pC spectral/info: children failed |
| P2 | 1 | 366 | .040 | 12 | 7 | restart |
| C1 | 1 | 333 | .037 | 8 | 2 | restart; **contains PV2 (K11, K12)** |
| a35 | 2 | 202 | .022 | 3 | 0 | Gaussian rank bounds |
| C3 | 1 | 190 | .021 | 5 | 3 | restart; cylinder sets |
| e1.4.9 | 4 | 166 | .018 | 0 | 6 | girth 14 (exploratory) |
| b3 | 2 | 162 | .018 | 2 | 2 | averages: collapse vs size (**kept as K11**) |
| a8 | 2 | 157 | .017 | 3 | 2 | sign lifting |
| b6 | 2 | 156 | .017 | 3 | 2 | cylinder relaxation |
| e1.4.21 | 4 | 143 | .016 | 0 | 3 | hexagon correction (left) |
| a36 | 2 | 128 | .014 | 0 | 0 | vertical component (partial, correct) |
| b2 | 2 | 127 | .014 | 2 | 0 | Jacobson/Leavitt |
| a26 | 2 | 121 | .013 | 1 | 0 | circuit W; graph-state counterexample |
| a40 | 2 | 116 | .013 | 0 | 1 | MTP / locally split encodings |
| a23 | 2 | 112 | .012 | 0 | 3 | compact-shift formulation (open) |
| a28 | 2 | 104 | .011 | 0 | 3 | integral lift; shear-dilation counterexample |

### Insight-driven steps
Only **one** backtrack is insight-driven: **e1.3.1 → e1.3.2, where Haefliger's developability theorem is replaced by a planar balanced-diagram Euler argument** (L469–473).
- **What was left.** No failure is stated, and the route looks valid: angles π/3 + π/2 + π/6 = π give a flat triangle of groups. It needs a complex of groups, link-girth checks at three vertex types (6, 4 and 12), and an imported theorem.
- **What replaced it.** A one-paragraph count on a minimal balanced planar graph. The count needed two later scope repairs (K24) and an explicit audit (L589–590).
- **Simplification.** This replaces an external dependency rather than shortening the text, roughly 1:1 in text. **Origin**: constructed from known small-cancellation counting. **Grade**: N1.

There is also a *reverse* insight, at e1.4.15 (L775–781). An elementary alternative to Linnik (Chebyshev plus Rankin) was "estimated" to survive, but the model **kept the old route**. It is coded `unclear`.

The decisive steps PV3 and PV4 are *not* insight backtracks. PV3 opens a new L1 after a PROVE conflict. PV4 follows a run of conflicts (e1.2.1–e1.2.5).

### Where the CDCL analogy breaks down
- **The strategy is not monotone.** In 287 the model committed to one answer for 62% of the text. Here it switches answer nine times in the first 43%, and the summary says sections "moved between" the two. The PROVE/CEX segmentation at sentence level is a judgement call.
- **Clauses are retained but not used.** The decisive clause K11 survives every restart (see `clauses_surviving_restarts`) but is not *applied* between L174 and L402. That pattern looks like phase saving plus restarts, not clause-driven propagation.
- **Relearning is heavy.** K3 (nonamenable entropy) is reapplied eight times and K6 (determinant) seven times.
- **The audit phase has no SAT counterpart.** Nearly half the body checks a candidate. It is closer to model-checking a found assignment.
- **Counts are lower bounds.** The summary compresses repeated audits into single paragraphs.

## 4. What the model learned (knowledge flow)

Ninety-three abandoned nodes carry a `lesson` object. Thirty-seven of them are abandoned L2 approach families, which is 287's granularity. Three more lessons sit on repaired-and-kept nodes. The 31 learned clauses fall into four groups.

**Necessary: the frame and most of the core of the proof.**

| Clause | Content | Where it lands in the paper |
|---|---|---|
| K9 | designs collapse unless girth is large | girth ≥ 12 |
| K11 | subgroup averages give a rectangular factorization; embeddings and characters are needed | the criterion's mechanism |
| K12 | size budget | m < t ≤ mκ |
| K19 | Gram cross terms | rank-one weights |
| K20 | polynomial evaluations (inferred) | the pairing |
| K21 | the LLL conflict | slab tiling and trades |
| K24 | minimality scope | lem:embedding |
| K13 | DJ finite factor | the scalar output |

The odd-order elementary abelian local groups from b4 also land in the paper (inferred).

**Enabling.**
- K1 (the group must be nonsofic and nonsurjunctive) is the consistency check.
- K7 (sign lifting dies) and K16 (lifting destroys support) are **inverted** in the audits. They become the observation that the final construction is intrinsically char 2: D·ΣW_v = 0 (K23), which matches the paper's prescription remark.
- K22 keeps Linnik.

**Inert.** All the PROVE-side analytic lessons: K3, K4, K6, K15, K17 and K28.

**Cross-family.** K6, "a DF counterexample would contradict the determinant conjecture" (a11, a30, e1.4.20 with its spectral atom −½), is the **contrapositive of the companion Determinant-Conjecture paper** in this family. The trace never considers that direction.

**Not learned.** The model obtained a correct theorem saying that any defect is intrinsically positive-characteristic (K18, at share 0.37). It did not turn this into a design principle such as "look for identities that hold only because an integer vanishes in K", which is exactly what the final construction does.

**The knowledge flow explains the frame and most of the core of the final proof. This differs from 287.** It does not explain two things:
- *timing*: nothing in the summary explains the re-entry at L402;
- *the choice of affine geometry over 𝔽_q*: that is explained only by the coding-theory retrieval.

## 5. What the trace tells us that the paper cannot
1. **Direction of search.** About 35% of the whole body, and 83% of the text before the final route, argues for the *opposite* answer. The paper reads as a direct construction.
2. **Early seed, late harvest.** The subgroup-average mechanism and the girth requirement appear at share 0.09. The construction is assembled only at 0.43–0.49, after five more strategy switches.
3. **Retrieval vs construction.**
   - The incidence criterion has no retrieved antecedent.
   - The polynomial pairing is triggered by Golowich–Lin and Dinur–Liu–Zhang. The paper credits them as inspiration only.
   - The slab tiling (eigenvector-free J) is constructed after a conflict.
   - The finite-factor step is retrieved (DHJ in the trace; Dykema–Juschenko in the paper).
4. **Provenance.**
   - 33 of the 42 trace references are absent from the paper.
   - The trace's latest reference is Manzoor (Aug 2025).
   - The paper adds two same-release companions, plus Erdős–Lovász, Moser–Tardos, Dyn–Floater and HNN.
   - Bridson–Haefliger is dropped along with the developability route.
5. **Verification status.**
   - About 10 self-built counterexamples or refutations.
   - About 4 circularity detections.
   - About 11 classes of checks on the final route.
   - Even so, the summary never claims a proof. It ends "retained the proposal and continued scrutinizing".
   - The finite presentation (relators of length ≤ 3) is paper-only.

## 6. Eureka candidates (trace level)

| ID | Item | Grade | For | Against |
|---|---|---|---|---|
| EC1 | **Incidence criterion** (PV3) | **N3 candidate**, F5/F3 | constructed; no antecedent; reduces an infinite group-algebra question to finite incidence plus linear-algebra data; load-bearing for the whole paper; reached only after 9 switches, with no trigger for the re-entry | pivot distance 1 from the model's own K11, K12 and K19; all components standard (averaging idempotents, triangles/amalgams of finite groups, DJ transfer); emerged incrementally |
| EC2 | Punctured polynomial pairing (PV4) | N2, F3 | the only instance of EC1; this is where char 2 enters | transfer from coding theory, invoked the sentence before; Reed–Muller-type line sums are classical; analytic once the identity is posed |
| EC3 | Glued subgroup averages → rectangular U,T (PV2) | N2, F3 | core mechanism; constructed early | standard device; dormant from share 0.15 to 0.425 |
| EC4 | Specialization rank certificate X^T X − I_t ≠ 0 (PV7) | N2, F5 | gives the rigorous certificate the prompt demands | standard; precursor K10 |
| EC5 | Planar Euler embedding (PV6) | N1 | self-contained (insight) | standard small-cancellation counting |
| EC6 | Vertical-component theorem (a36, off-route) | N1–N2 | correct, clean | unused; standard ingredients |

**Discoverability test.** Hide thm:criterion and everything downstream. Give a model the problem plus L: Mathlib, DJ, Elek–Szabó, CSCP, and **separately with and without GL/DLZ**. Score any proposal of the form "finite local-cancellation, global-nonzero Gram certificate with embedded finite subgroups".

## 7. Comparison with 287

| | 287 (free group factors) | 197 (char-2 direct finiteness) |
|---|---|---|
| Shape | one long NEG block (62%), then a flip to POS with one relapse | rapid PROVE/CEX oscillation in the first 43% (9 restarts, 4 of them interleaved) |
| Final route | last 22–23%, mostly construction | last 57.5%: 11.6% construction + **45.9% audit** |
| Decisive step | small-cocycle lemma: no trigger; recycled Fox calculus from a failed obstruction | incidence criterion: no trigger for the re-entry, but **pivot distance 1 from early CEX lessons**; instantiated by a retrieval-triggered transfer |
| Knowledge flow | explains the frame, not the core | explains the frame **and** most of the core; does not explain the timing or the 𝔽_q geometry |
| Lessons on the opposite side | mostly enabling (C14 motivates the restart) | mostly **inert**; two are inverted into an audit insight (no char-0 lift) |
| Insight backtracks | 1 (Arg(C), N2) | 1 (planar Euler, N1) |
| Reuse rate | 0.77 | 0.84 (but heavy relearning; K11 is dormant) |
| Excitement markers | "Aha!" on a dropped analogy | 5 of 7 on failed PROVE routes; none on PV3/PV4 |
| Computer-assisted | no | no |

**Recommendations for the remaining traces.**
- Keep the strategy-neutral and interleaved-restart extensions.
- Code audit phases as checks, repairs and dropped strengthenings.
- Report a "dormant clause" statistic: the longest gap in applications of a clause that becomes necessary. In 197, K11 is learned at 0.09, last applied at 0.15 (b4), and next applied at 0.425.
- Report the share of the final route spent on audit.
