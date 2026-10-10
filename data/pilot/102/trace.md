# Family 102: reasoning-trace analysis ("The Unique Games Conjecture and optimal approximation thresholds")

Source: `data/traces/102.txt`, OpenAI's 16-page *summarized* chain of thought (original: `reasoning_traces/basic-semidefinite-threshold-np-hardness.pdf`). The summary body (L94–560, prompt excerpts and references excluded) has **5,308 words** in 12 sections, with 10 short VERBATIM excerpts. Machine-readable coding is in `trace.json` (same keys as `data/pilot/287/trace.json`, plus the extensions listed in its `schema_extensions`). Line numbers (L) refer to the .txt file. Lengths are word-exact: each node is located by a text anchor.

**Read this first.** Everything below concerns *what the summary reports*. Lengths measure how the summary allocates text, not the model's compute. Backtracks that the summarizer compressed are invisible, so all counts are lower bounds.

## 0. The posed problem and which manuscript it leads to

**Prompt (L5–93).** Prove or refute, without the Unique Games Conjecture, ordinary NP-hardness of beating the BasicSDP ratio threshold α_Γ for *every* fixed finite Max-CSP. In other words: Raghavendra's optimality theorem made unconditional.

**The trace leads to exactly one of the five manuscripts: `The-Unique-Games-Theorem-September-23-2026`.**
- Its Theorem `thm:ugc` is UG hardness with completeness 1−ε, soundness δ, and translation constraints over F₂ˢ.
- Its Corollary `cor:raghavendra-consequence` is precisely the posed assertion. It is proved through Raghavendra's fixed-instance theorem with rational re-weighting.

The match is unambiguous. The trace contains the paper's specific objects:
- the quadratic seed Q(x) = (x₂x₃, x₁x₃, x₁x₂) over F_{2^d}³ (L307–308, L403, L476);
- the bound of "3r" alignments for generic rank-r character spaces, proved via square-root monomials and specialisation (L310, L369–376, L506);
- the harmonic rank potential with fresh orientations (L312, L538–541);
- row fibres and the row-fibre abundance repair (L336–341, L408–416);
- sparse projection with β = k^{−2/3} (L387, L550);
- Håstad parity with cloning (L383–385);
- alphabet-independent Rao / Dinur–Steurer repetition (L349–351);
- the Raghavendra transfer (L168–173, …, L555–557).

**Not led to:**
- **Direct Max-Cut.** That paper uses a tree code, vector-valued hashing and an affine 2-to-1 game. The trace mentions Max-Cut only as a Goemans–Williamson sanity check (L557–558).
- **Vertex Cover, Min-UnCut, DFVS.** None of these problems is mentioned in the trace.

These four are the family's "independent direct reductions". The trace shares only background with them (DKKMS, Håstad, Friedgut).

**Lean.** The comparator targets cover the UG gap reduction (and the four direct results). The BasicSDP corollary, which is what the prompt actually asked for, is **not** a comparator target.

## 1. The story of the search

**§1 (L94–136): the frame is fixed in the first 4% of the text.**
- **NEG1.** The model checks the conventions of the relaxation, Raghavendra [50] and the Thapper–Živný dichotomy [55]. It finds no cheap counterexample.
- **EQV (converse).** Raghavendra's dependence on UGC prompts a converse. A baseline gadget with three dummy labels keeps a Khot–Vishnoi gap. Then a VERBATIM "Wait insight": a gap with YES near 1 and NO bounded away from 1 already gives UGC by projection-game repetition (Rao). So the assertion is essentially *equivalent to UGC*:
  - proving it means proving UG hardness with near-perfect completeness;
  - refuting it means finding a UG algorithm.
- The model is aware that the KMS 2-to-2 theorem gives only completeness ≈ 1/2 (C3). From this point the *answer* never changes. The search alternates between POS (a UG-hardness gadget) and short NEG excursions (an alphabet-uniform algorithm for nearly satisfiable affine UG).
- **POS1** starts from the KMS/BKS shortcode framework with Håstad parity as the outer gap. Tensoring raises honest acceptance from 1/2 to 3/4, but it fails three ways:
  1. projected queries reveal the outer constraint (C8);
  2. sparse noise leaves duplications recognisable (VERBATIM cheater "independent of actual satisfiability!");
  3. dense noise kills completeness (C9).

**§2 (L137–186): the target is sharpened into a stability gap.**
- The requirement (C10): honest encodings must survive perturbations much better than arbitrary answers.
- Gaussian testers fail because smooth Lipschitz cheaters are just as stable. The model concludes it needs a linearity test via **rank-one** transformations (C12, VERBATIM).
- An "amplification insight" restates the goal as repeated noise with vanishing honest loss and constant dishonest loss (C14).
- A seed appears at L166: an abstract **equivariant decoder**, left open.
- The Raghavendra transfer is sketched (c10).
- A cyclic Z_M / winding-number idea dies against sphere-valued cheaters with correlated singularities (c11).

**§3 (L187–233): two NEG visits.** Nearly satisfiable affine UG over F₂^ℓ:
- KV gaps defeat equivariant SDP rounding;
- Goemans–Williamson per character leaves the errors unsynchronised;
- decomposition and collision potentials, alpha-expansion, the connection Laplacian, interleaved codes, Barto–Kozik, orthogonal separators, BKS rounding, hash-fibre conditioning and correlated sampling all fail.

Every attempt fails on *alphabet-uniformity* or *global consistency* (C16–C18). A one-sentence hardness aside (POS2: a "stable coloring") sits between the two visits.

**§4 (L234–283): the concept.**
- Rare-gate tensors give a soundness gap of only ε. VERBATIM: "Need ensure dummy axes themselves hard so no arbitrary gating" (C19).
- Rich pairings and smooth codes fail.
- Then **nonlinear equivariant decoders become the main alternative** (L251, share 0.34). The target is an unbounded separation between nonlinear stability and the best compatible linear decoding. The model makes it quantitative: p (nonlinear noise failure) against h(r) (the least noise cost of simultaneous linear lifts of r characters), with h(r)/p → ∞ (C22).
- Simplex mixing via symmetric injections is retained (C23).
- Two failures are written down as design requirements:
  - concatenation lets linear competitors split into scalar lifts (C21);
  - recursion with fixed branching collapses rank. VERBATIM: "Need increasing b or avoid collapse via mixing outer layers" (C24).

**§5 (L286–317): the construction.**
- Short POS4 / NEG6 asides come first.
- Then Croot–Lev–Pach / Lovett analytic rank is tried and is too weak (C25).
- In the next sentence (L307, share 0.46) the model writes down the gadget:
  - C(x, y) = y + (x₂x₃, x₁x₃, x₁x₂) on F_{2^d}³;
  - cubic monomials and specialisation bound exceptional cancellations by 3r;
  - concatenation runs through *all* binary-linear isomorphisms, which enforces a common parent lift;
  - a harmonic potential keeps h ≥ 1/4 while p → 0.

  The construction answers C21, C22 and C24 almost word for word.

**§§6–12 (L318–560, 45% of the text): assembly and audit of one construction.** Each section cycles through the same components:
- gadget;
- shared affine tables: exact identification by reduced keys, then folding;
- row-fibre advice, with the abundance repair (VERBATIM ×2);
- the outer game: Håstad, cloning, β = k^{−2/3}, clean coordinates, Dinur–Steurer repetition fixed before the alphabet;
- uniformity of the imported KMS/BKS constants, resolved by padding;
- the Raghavendra transfer (with a direct Lindeberg comparison that the paper drops);
- checks against CMM, KV, GW, KKL, expanders and a concrete counterstrategy.

The summary ends hedged: "its proposed affirmative argument".

## 2. Decisive pivots

| Pivot | Where | Trigger | Classification | Final paper | Eureka? |
|---|---|---|---|---|---|
| PV1 converse: assertion ⇒ UGC | L97–115, share 0.01–0.04 | retrieved (Raghavendra's UGC dependence) | **known route** | architecture only; the converse itself is dropped | no (N1) |
| PV2 POS via the 2-to-2 machinery | L123–136 | restart after NEG2 | known technique | Thm `thm:parity`, `thm:shortcode` | no (N0) |
| PV3 stability gap + rank-one linearity | L137–153 | conflicts c3.x, c4, c7 | known technique (sharpened target) | rank-one update test | no (N0–N1) |
| **PV4 nonlinear equivariant decoder, noise invisible to it** | seed L166, adopted L251, spec L265–271 | conflict lessons C9, C10, C12, C19, C22; no retrieval | **new concept** | **Lemma `lem:latent`** ("changes the noise using a nonlinear map") | **N3 candidate, F5+F3** |
| **PV5 explicit quadratic gadget** | L306–313 | conflict k3 (CLP/Lovett too weak); shaped by C21, C22, C24 | **new construction / new bridge** (char-2 algebra + polynomial identity + potential recursion) | §2: `lem:latent-block` … `prop:latent-full-lift-detection`, Def. *generic*, `lem:latent-generic` | **N3 candidate, F3 (+F4)**, chain depth 2 |
| PV6 shared affine tables, exact identification | L319–335 | C13 | known technique adapted (paper: Khot–Safra virtual tables, BGS folding; absent from trace) | §3 keys, folding | N1–N2 |
| PV7 row-fibre abundance | L336–341, L408–416 | self-detected gap (VERBATIM) | known technique adapted (KMS17 / MZ) | `lem:good-row-advice` | N2 |
| PV8 β = k^{−2/3}, clean coordinates, Dinur–Steurer repetition | L341–343, L383–393, L549–552 | C8, C27 | known technique | `prop:matrix-decoding`, §5 | N1 |
| PV9 Raghavendra transfer | L168–173 … L555–557 | C4 | known | `cor:raghavendra-consequence` | N0 |

**The decisive pivots are PV4 and PV5 together, with PV5 the core.**
- **PV4** is prepared by the model's own lessons. It has low pivot distance *from the trace state*, but no invoked literature supplies it. BKS §1.6 suggested higher-degree tests, which is a different route.
- **PV5** is the only step with no retrieved antecedent and no lesson predicting its specific form. The one possible remote antecedent is the Kasami–Tokura low-weight Reed–Muller search at L165.

## 3. CDCL coding of the search

### Level rules
The 287 rules apply verbatim, with four documented extensions (full text in `search_dynamics.level_assignment_rules`):
1. **REF node.** The answer-neutral reformulation EQV is an L1 node. Leaving it is not a backtrack, because it is retained.
2. **Component-tagged siblings.** In the final strategy the summary revisits the same components in every section, so each paragraph-level visit is an L2 sibling tagged GAD / TAB / ADV / OUT / SHC / TRN / CHK / ARCH / ALT.
3. **CHK nodes.** After commitment, attempts to refute the route's own lemmas are verification nodes, not NEG restarts.
4. **Micro restarts.** A restart into or out of an L1 node of fewer than 60 words is flagged as micro.

### Search tree (condensed; 146 decision nodes in JSON)
```
ROOT  NP-hardness at the BasicSDP threshold for every finite CSP (no UGC)?
├─ NEG1 (36 w)  a1 conventions / Thapper–Živný loophole ✗
│        ══ RESTART 1 (micro, L97) ══
├─ EQV [REF] (182 w)  converse: assertion ⇒ UGC
│   ├─ e1 CMM-constrained baseline ✗   ├─ e2 ratio ≠ completeness≈1 ✓(C3)
│   ├─ e3 GW + Raz odd cycle ✗          └─ e4 dummy labels + KV + "Wait insight" repetition ✓(C4,C5)
├─ NEG2 (93 w)  b1 SoS/ABS ✗  b2 certified SSE ✗  b3 Trevisan ?  b4 KKMO affine ?  b5 hashing ✗
│        ══ RESTART 2 (L123) ══
├─ POS1 (763 w, 14%)  UG gadget via KMS/BKS shortcode
│   ├─ c1 rich 2-to-1 ?   c2 DKKMS/MZ outer + Håstad ✓
│   ├─ c3 tensor test ─ c3.1 leak ✗ ─ c3.2 duplicates ✗ ─ c3.3 dense noise ✗        (d=2)
│   ├─ c4 low rank ✗  c5 flags ✗  c6 KM real code ?  c7 Gaussian tester ✗ (C12 rank-one)
│   ├─ c8 masked tensors ─ c8.1 consistency ✗ ─ c8.2 MZ+BLR ? ─ c8.3 Friedgut ✗        (d=2)
│   ├─ c9 amplification target ─ c9.1..c9.4 ✗/? ─ c9.5 equivariant decoder SEED ?   (d=2)
│   ├─ c10 transfer sketch (Raghavendra) ✓
│   └─ c11 Z_M winding ─ c11.1 ~ ─ c11.2 ~ ─ c11.3 smoothing ✗ ─ c11.4 sphere cheaters ✗
│        ══ RESTART 3 (L187, d=3) ══
├─ NEG3 (220 w)  d1 KV vs equivariant ✗ d2 GW/char ─ d2.1 squaring ✗ d3 ? d4 ✗ d5 ✗ d6 ✗
│        ══ RESTART 4 (micro) ══  POS2 (25 w) p1 stable coloring ?  ══ RESTART 5 (micro) ══
├─ NEG4 (307 w)  f1 ✗ f2 circular ✗ f3 ? f4 ✗ f5 ✗ f6 ✗ f7 hash fibres ─ f7.1 ✗ ─ f7.2 ✗  f8 coherence ✗
│        ══ RESTART 6 (L234) ══
├─ POS3 (550 w, 10%)
│   ├─ g1 rare gates ✗ (C19)  g2 KMS/DKKMS restudy ✓  g3 pairings ✗  g4 smooth codes ?
│   ├─ g5 NONLINEAR EQUIVARIANT DECODERS (PV4, share .34)
│   │    ├─ g5.1 aliasing ✗ g5.2 split lifts ✗(C21) g5.3 ? g5.4 ✗ g5.5 ✗ g5.6 ✗
│   │    ├─ g5.7 p vs h(r) target ✓(C22)   g5.8 simplex mixing ✓(C23)
│   │    └─ g5.9 rank collapse ✗(C24) g5.10 ✗ g5.11 ✗                               (d=2)
│   └─ g6 conditional fallback ✓
│        ══ RESTART 7 (micro, unclear) ══ NEG5 (21 w) h1 SSE ✗ ══ RESTART 8 (micro) ══
├─ POS4 (121 w)  i1 ✗ i2 ✗ i3 ✗ i4 Håstad+Rao ✓ i5 ?
│        ══ RESTART 9 (unclear) ══
├─ NEG6 (82 w)  j1 ✗ j2 ? j3 ✗ j4 ✗
│        ══ RESTART 10 (L303, share .454) ══
└─ POS5 FINAL (2900 w, 55%)
    ├─ k1 transpositions ✗  k2 Barrington ?  k3 CLP/Lovett ✗(C25)
    ├─ k4 QUADRATIC GADGET (PV5) ✓  k5 outer composition plan
    ├─ [GAD] k6 k14 k21 k28 k33 k38 k46 ✓     [TAB] k7 ✓
    ├─ [ADV] k8a ✗→k8b ✓ (repair)  k20  k22 ✗→k23 ✓ (repair)  k30  k35 ✓
    ├─ [OUT] k9 k10a ✗→k10b ✓ (repair) k17 k18 k24 k27 k34 k41 k48 k49 ✓
    ├─ [SHC] k16 (provisional)  k40 concern ✗→ padding (repair)  k47 ✓
    ├─ [TRN] k10 k19 k25 k32 k37 k44 k50 ✓   [CHK] k11 k13 k15 k26 k29 k36 k39 k43 ✓
    └─ [ALT] k31 ? k42 ✗ (several/summed perturbations unused)
```
(✗ = stated conflict, ? = left open (unclear), ~ = provisional, ✓ = kept.)

### Metrics
| Metric | 102 | 287 (for comparison) |
|---|---|---|
| decisions / conflicts | 146 / 58 | 69 / 47 |
| backtracks: total / conflict / insight / unclear | **73 / 56 / 0 / 17** (4 of the conflict ones are repairs) | 48 / 46 / 1 / 1 |
| distance histogram (all) | d=1: 57, d=2: 15, d=3: 1 | 40 / 7 / 1 |
| distance by trigger | conflict {1:44, 2:11, 3:1}; unclear {1:13, 2:4} | — |
| max backtrack distance, max depth | 3, 3 | 3, 4 |
| restarts | **10** (5 excluding micro), alternating NEG/POS | 3 |
| propagations (rough) | 158 | 42 |
| learned clauses / reuse rate | 39 / **0.87** | 26 / 0.77 |
| share of trace before the final route | **0.454** (words), 0.459 (chars) | 0.77 |
| text share by strategy | POS 82%, NEG 14%, EQV 3% | NEG ~78% |
| abandoned-branch length, mean / median (words) | all 61 / 26; conflict 61 / 29 (38 / 25 excl. restarts); unclear 64 / 20; restarts 222 / 107 | conflict 122 / 60 |
| length vs distance | Pearson 0.70, Spearman 0.60 (excluding restarts 0.66 / 0.48). Mean length by distance: d=1 26 w, d=2 147 w, d=3 763 w | Spearman 0.62 |
| non-restart leaf length | median 22 w (n=63) | 44 w |
| explicit time/compute markers | **none**; 32 revisit/retention words | none |

**Do long branches end in restarts?** Only mechanically:
- POS1 (763 words) and POS3 (550 words) are the long abandoned strategies.
- The last straws before restarts are ordinary leaves of 10–75 words, median 27.
- Half the restarts are micro (one-sentence asides).

As in 287, restarts follow accumulated conflicts or simple interleaving, not one long failed branch.

**Final-route composition (POS5, 2,900 words)** by component:

| Component | Share of final route |
|---|---|
| Outer game | 25% |
| Gadget | 24% |
| Checks | 16% |
| Advice | 14% |
| Transfer | 10% |
| Shortcode uniformity | 4% |
| Tables | 3% |

### Longest abandoned branches (top 15 of 89 abandoned or repaired nodes; full list in JSON)
| node | lvl | words | share | children | refs | outcome / obstruction |
|---|---|---|---|---|---|---|
| POS1 | 1 | 763 | .144 | 26 | 19 | restart; projection leakage, stability gap unmet |
| POS3 | 1 | 550 | .104 | 17 | 17 | restart (unclear); concept found, amplification unsolved |
| g5 | 2 | 330 | .062 | 11 | 5 | children mixed; target and simplex mixing retained |
| NEG4 | 1 | 307 | .058 | 10 | 6 | restart; global consistency |
| NEG3 | 1 | 220 | .041 | 7 | 13 | restart; no alphabet-uniform rounding |
| c11 | 2 | 171 | .032 | 4 | 1 | winding numbers: sphere-valued cheaters |
| POS4 | 1 | 121 | .023 | 5 | 8 | restart (unclear) |
| c3 | 2 | 120 | .023 | 3 | 2 | tensor shortcode test: leak / duplicates / completeness |
| c8 | 2 | 97 | .018 | 3 | 3 | masked tensors: consistency, juntas |
| NEG2 | 1 | 93 | .018 | 5 | 6 | restart; known algorithms insufficient |
| c9 | 2 | 91 | .017 | 5 | 2 | amplification walks fail (target kept) |
| NEG6 | 1 | 82 | .015 | 4 | 7 | restart; relearning |
| g1 | 2 | 80 | .015 | 0 | 0 | rare gates: soundness gap ≈ ε |
| f7 | 2 | 76 | .014 | 2 | 1 | hash-fibre conditioning: normalisation defect |
| c11.4 | 3 | 75 | .014 | 0 | 0 | sphere-valued correlated cheaters |

### Insight-driven steps
**There are no insight-driven backtracks.** Every abandonment is stated as a conflict or left unexplained.

The decisive construction (k4) follows a *stated failure* (k3, CLP/Lovett too weak). So it is a conflict-driven backtrack whose next node is constructed, flagged `novelty_candidate`.

Eight **insight events** that do not abandon a viable node are logged in `search_dynamics.insight_events`, and each is sent to novelty grading:

| Event | What happens | Grade |
|---|---|---|
| IE1 | "Wait insight" on the converse | N0–N1, known route |
| IE2 | amplification target | N1–N2 |
| IE3 | nonlinear equivariant decoders | **N3 candidate** |
| IE4 | quadratic gadget | **N3 candidate** |
| IE5 | exact table identification | N1–N2; paper credits Khot–Safra |
| IE6 | Lindeberg in place of MOO | N0; dropped from the paper |
| IE7 | "Aha!" average-scalar-cost reformulation inside a self-refutation attempt | N0–N1 |
| IE8 | "fresh outgoing randomness" for nongeneric spaces | N2; part of EC2 |

### Where the CDCL analogy breaks down
- **Levels are reconstructed.** The summary narrates §§2–12 as one continuous "proposed Unique Games route" with algorithmic asides. Five of the ten restarts are one-sentence interleavings.
- **The final route is narrated by component, not chronologically.** Each section re-states the gadget, tables, advice, outer game and transfer. That gives 53 L2 nodes in POS5, but only 9 backtracks there: 3 before the gadget, 4 repairs and 2 minor alternatives.
- **The clauses are informal lessons.** Unlike 287, many are phrased by the model as *specifications* ("Need increasing b or avoid collapse via mixing outer layers"; "need linearity test via rank-one transformations"). That is closer to clause learning than 287's repeated BDIP relapses.
- **Relearning still occurs:**
  - C7, coordinatewise errors: b5, then d2, then j1;
  - C9a, duplications: c3.2, then g5.6;
  - C20, scrambling: g3, then g5.11;
  - C6, algorithm barriers: across all six NEG visits.

## 4. What the model learned (knowledge flow)

Each of the 89 abandoned or repaired nodes carries a full `lesson` object in the JSON: obstruction, statement, VERBATIM excerpt, form, generality, known-in-literature, correctness, salvage, reused_at, influence, and what was not learned. The flow:

- **The architecture is fixed by early clauses.**
  - C3: completeness near 1 is *the* difficulty.
  - C3a: repetition can only shrink soundness.
  - C4: the assertion is equivalent to UGC.
  - C5: alphabet-independent projection-game repetition.

  All four are set in the first 4% of the text and are necessary for the final proof.
- **The gadget's specification is learned from failures before the gadget exists.**
  - C9: dense noise kills completeness.
  - C10: the stability gap.
  - C12: rank-one linearity, not Gaussian noise.
  - C19: no gating.
  - C21: a common parent lift.
  - C22: the h(r)/p target.
  - C24: no rank collapse; increase branching or mix layers.

  Then C25 (generic inverse-rank estimates too weak) points to an explicit construction, and k4 meets C21, C22 and C24.
- **Repairs in the assembly are conflict-driven.**
  - C26: existence → abundance of good row fibres.
  - C27 / C27b: alphabet-independent repetition and conditioning.
  - C28: decoding consistency.
  - C29: uniform imported constants. These are exactly the hypotheses of the paper's lemmas and quantifier order.
- **NEG dead ends are recycled as checks.** C2 (CMM), C7 (coordinatewise rounding), C16 (KV) and C18 (alphabet-dependent rounding) become verification checks on the final construction (k11, k13, k15, k26, k33, k36, k43). This use of failed refutation attempts did not appear in 287.
- **Inert:** C9a, C11, C13b, C15 (the topological route), C17a, C17b, C20, C30, C32.
- **Not learned.**
  - Barto–Kozik is set aside only for alphabet-dependent constants (f4). The stronger known reason, that linear equations lack bounded width, is not stated.
  - The trace never names the paper's closest precedents for the advice/decoding layer (Khot–Safra 2013, KMS 2017). It credits Minzer–Zheng instead.

**The knowledge flow explains the final route far better than in 287.** It explains everything except the specific algebraic object: the characteristic-2 quadratic map and its square-root-monomial genericity argument.

## 5. Eureka candidates (trace level)

| id | item | grade | F | for | against |
|---|---|---|---|---|---|
| **EC2** | quadratic gadget: Q over F_{2^d}³, generic spaces with ≤3r alignments (square-root monomials and specialisation), all-isomorphism recursion, harmonic potential with fresh orientations | **N3 candidate (strongest)** | F3 (+F4) | appears with no retrieval right after a failed retrieval; tiny and specific, in the spirit of Cook's extension variables; carries all the weight of EC1 | Q is a classical quadratic map; harmonic potentials are standard; its requirements were pre-specified by C21/C22/C24; the summary may compress search (Kasami–Tokura L165) |
| **EC1** | latent alphabet gadget (concept): nonlinear equivariant C with noise invisible to C but detected by every high-rank linear family | N3 candidate | F5 + F3 | the paper presents it as the new idea; non-analytic; sole source of near-1 completeness | built incrementally from the model's own lessons; changing test noise is a classical PCP move; needs a literature search (noise-resistant / latent encodings) |
| EC3 | row-fibre abundance | N2 | — | self-detected gap, repaired | KMS17 / MZ framework |
| EC4 | exact identification by reduced keys + folding | N1–N2 | — | stated reason for departing from approximate consistency | paper credits Khot–Safra, BGS |
| EC5 | β = k^{−2/3}, clean coordinates, Dinur–Steurer before the alphabet | N1 | — | — | parameter choice in a known framework |
| EC6 | converse via dummy labels | N1 | — | strategically decisive early | not in the paper; plausibly folklore |

For the discovery test, EC1 and EC2 should be hidden together, with chain depth 2. Contamination control must exclude Khot–Safra 2013, KMS 2017, BKS 2018 §1.6 and the OpenAI companion "Perfect completeness for 2-to-1 games".

## 6. What the trace tells us that the paper and Lean cannot

1. **Direction of search.**
   - The model fixed the correct answer and architecture at once, via the converse.
   - The NEG side (14% of the text) was explored in short excursions, and its lessons were later turned into *checks*.
   - The paper says nothing about the equivalence with the posed BasicSDP problem beyond the corollary.
2. **Concept before construction.**
   - The nonlinear-decoder concept took about 1,600 words of incremental lessons (L138 → L273).
   - The explicit construction took one sentence (L307).
3. **Provenance gaps.**
   - The paper's named precedents for the advice and decoding layer (Khot–Safra 2013, KMS 2017) and BGS folding are absent from the trace.
   - 36 of the 56 trace references never reach the paper; most are NEG and algorithmic literature.
   - The latest-dated references in the trace are Minzer–Zheng v4 (2026) and Ellis–Kindler–Lifshitz v2 (2026).
4. **Verification status.** The trace audits heavily: 16 checks on the final route, 3 self-refutation attempts against its own gadget or reduction, and 4 repair backtracks on 3 distinct issues. But it stays hedged ("proposed"). Several paper components are absent from the trace:
   - the explicit unweighted rounding and four-edge subdivision (paper §6);
   - the simple strong-left UG formulation needed for Raghavendra's fixed-instance theorem (paper Appendix);
   - deterministic computability of the gadget data;
   - one constant differs: the trace has h ≥ 1/4, the paper has detection ≥ 1/8.
5. **Dropped material.** The converse (assertion ⇒ UGC) and the direct Lindeberg comparison do not survive into the paper.

## 7. Comparison with 287

| | 287 (free group factors) | 102 (UGC / BasicSDP threshold) |
|---|---|---|
| Direction | ~78% on the wrong answer, then construction | correct answer fixed in the first 4%; only 14% on the opposite side |
| Share before the final route | 0.77 | 0.45 |
| Restarts | 3, long NEG programmes | 10 (5 micro), short interleaved NEG excursions |
| Backtracks (conflict / insight / unclear) | 46 / 1 / 1 | 56 / 0 / 17 |
| Distance histogram | 40 / 7 / 1 | 57 / 15 / 1 (same shape) |
| Clause reuse | 0.77, with heavy relearning (BDIP ×7) | 0.87; lessons phrased as specifications; NEG lessons recycled as checks |
| Final-route share | ~23% | ~55% (component-wise audits) |
| Core eureka candidate | small-cocycle lemma (new bridge, F3), no predicting lesson | latent gadget: concept predicted by lessons (F5/F3), construction unpredicted (F3/F4) |
| Common pattern | the concept is prepared by conflict lessons; the specific construction appears with no visible trigger, right after a failed or abandoned retrieval | same |

## 8. Caveats
- The summary is curated by OpenAI. It has no timing, token or branch information; parallel samples are invisible.
- Node levels, the micro-restart flag and several clause reuses (C17 → k33, C19 → latent detection, C23 → injections, C24 → k4) are the analyst's inference.
- "Known in literature" judgements in the lesson objects come from the analyst's knowledge, not a systematic search. EC1 and EC2 in particular need the N3 literature tests before any grading.
- I did not check whether the trace's proposed argument is correct. The final paper's proof was skimmed only to map items.
