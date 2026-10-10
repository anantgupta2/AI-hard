# Family 197: novelty analysis ("A torsion-free group algebra that is not directly finite")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json` (same keys as 287, with `precedent_checks` as a list plus `bridge_novelty` and `sources`).

## Inputs and scope
- **Manuscripts.** The family has four. All of them were read directly, because only a trace analysis existed for this family:

  | Code | Manuscript | Date | Lean | Trace |
  |---|---|---|---|---|
  | **TF** | headline, torsion-free over F₂ | Oct 4 | **no** | **none** |
  | **CT** | characteristic 2 | Sep 23 | yes | traced (`trace.md`) |
  | **DT** | Determinant Conjecture | Sep 23 | yes | none |
  | **OD** | odd characteristic | Sep 26 | yes | none |

- **Family 196's paper** (*A Torsion-Free Group Algebra with Zero Divisors*, "ZD") was also read, because TF declares it as its method source.
- **L.** Mathlib d13f23b plus each manuscript's own bibliography.
  - L(TF) **includes** ZD and CT.
  - L(CT) includes Golowich–Lin and Dinur–Liu–Zhang.
- **L⁻** removes the OpenAI companions, for contamination control.
- **Lean.** I worked from the file-level structure only and did not compile anything. `OAI/RingTheory/DirectFiniteness` has 126 files and 13,310 lines, and none of them contains `sorry`.

## 1. Provenance verdict (first)

**Flag: YES for the family. The item that carries D3 has no model-produced precedent.**

1. **The headline TF strictly builds on a model-produced paper.** That paper is ZD (OpenAI, Sep 23, family 196), published 11 days before TF.
   - TF says it "develops the graph and cone construction" of ZD. In its words, ZD "supplies the parity mechanism for a zero product and the arrangement-exclusion strategy. We adapt those arguments" (introduction.tex:50–54).
   - Every TF item is a variant or a re-derivation of a ZD item:
     - the parity criterion;
     - the types (ZD uses 3 extra letters; TF uses 7 Fano letters);
     - the bounded-pattern estimate;
     - the planar separator extraction;
     - the cone surgery.
2. **DT uses CT (model-produced) as its sole existence input.** OD cites CT as context but says CT is not an input.
3. **The nonsoficity corollaries have a model-produced precedent that 197 does not cite.**
   - OpenAI's "Nonsofic Groups Exist" circulated on 2026-07-31 and was announced in August as an "Astra" result; one report credits GPT-5.6 Sol. It uses the unit group of the binary Leavitt algebra, Kun–Thom, and Thompson's V.
   - Separately, Fournier-Facio's human-authored arXiv:2608.02025 (Aug 3/14) already gives *torsion-free* nonsofic groups.
   - Thom has publicly alleged, and OpenAI has denied, that the August result drew on his private ChatGPT conversations. That dispute concerns expanders, not group rings.
4. **External 2024–26 sources disclose no AI use.** I fetched the abstract pages for:
   - Golowich–Lin 2410.14662;
   - Dinur–Liu–Zhang 2308.15563;
   - CSC–Coornaert–Phung 2310.09451 and 2405.18287;
   - Kammeyer 2609.15567.
5. **One transitive case.** Mian–Siddique 2609.22380, which is in ZD's bibliography only, says "Use of an LLM is disclosed in Section 10". It bears on no 197 item.
6. **Web searches.** I searched for ("Kaplansky direct finiteness" × OpenAI / ChatGPT / GPT / AI-assisted). Outside the release, I found no model-produced work on direct finiteness.

The quotes from news pages and arXiv pages came through WebFetch's summariser and are unverified.

## 2. Final grades

| # | Ms | Item | Nearest neighbour (verdict) | T2 | Final | F | conf |
|---|---|---|---|---|---|---|---|
| **C1** | CT | **Incidence criterion** (thm:criterion) | Elek–Szabó rank obstruction (the item defeats it); DHJ ULIE groups (different); lamplighter idempotents (different). **No near-equivalent found** | pass | **N3 (provisional)** | **F5** (F3 flavour) | **0.45** |
| C2 | CT | Glued subgroup averages → UT = I_m | Passman averaging; the model's own b4 (close variant) | fail (borderline) | N2 | – | 0.60 |
| C3 | CT | Punctured polynomial pairing (prop:pairing) | RM line duality (classical); GL/DLZ, named by the paper (close variant) | pass (weak) | N2 | – | 0.65 |
| C4 | CT | Regular girth-12 affine-line system (thm:hypergraph) | LLL/high-girth designs, trades (close variant) | fail | N2 | – | 0.60 |
| C5 | CT | Character packing + specialization certificate | HNN, character idempotents, rank (standard) | fail | N1 | – | 0.60 |
| C6 | CT | Planar Euler embedding (lem:embedding) | Gersten–Stallings/Haefliger; small-cancellation counts | fail | N1 | – | 0.75 |
| C7 | CT/OD | DJ finite-factor matrix units | Dykema–Juschenko Thm 2.2 (equivalent) | fail | N0 | – | 0.90 |
| C8 | CT | Linnik prime | Linnik/Xylouris | fail | N0 | – | 0.95 |
| C9 | CT/OD | CA transfer (Gottschalk) | Elek–Szabó §1; CSC–Coornaert | fail | N0 | – | 0.90 |
| T1 | **TF** | Parity criterion for ab = 1 (prop:parity) | **ZD** Prop 5.1 (close variant; model-produced); Mineyev 2024; Rips–Segev | fail (borderline) | N2 | – | 0.75 |
| T2 | TF | Fano-complement extra letters (prop:types) | ZD's types; the 2-(7,4,2) design | fail | N2 | – | 0.55 |
| T3 | TF | Word-weight decay + bounded patterns | ZD (same method) | fail | N1 | – | 0.70 |
| T4 | TF | Planar separator + cone-surgery asphericity | ZD (same); Ollivier/Gruber/Bereznyuk | fail | N1 | – | 0.70 |
| D1 | DT | DF failure in char 2 ⇒ det_FK < 1 (trace-gap projection, mod-q lift, shears) | Dicks–Schick (component, named); no prior implication found | pass (weak) | N2 (borderline N3) | – | 0.50 |
| O1 | OD | Triangular compression from a low-rank fit of a triangle-free graph | CT criterion (sibling, in L); Haviv/Golovnev–Haviv minrank | fail (borderline) | N2 | – | 0.60 |
| O2 | OD | Large modular idempotents with ordered annihilations | Jennings, Schwartz–Zippel (standard) | fail | N2 | – | 0.50 |

**Test 1 searches.** The full query list is in `novelty.json`. zbMATH, MathOverflow and Scholar were not queried directly, so absence claims mean "no neighbour found in WebSearch queries on X, Y, Z plus domain knowledge".

**Excluded from grading.**
- The PROVE→CEX switches, which are strategic rather than mathematical items.
- The off-route vertical-component theorem (a36).
- The nonsoficity and F∞ corollaries (N0; see the precedents above).
- The prescription bookkeeping.

**Overrides of the trace analyst.**
- EC4/PV7 (packing + certificate): N2 → **N1**. Every step is a standard tool in L.
- EC1 is kept at N3-provisional, but its confidence is lowered by the Elek–Szabó framing described below.

## 3. Why C1 survives, and how weakly

**The construction violates the sofic rank bound by design.** This is the analyst's own derivation, not a claim made in the paper.
- If the glued group N were sofic, a Sylvester rank function would give rk(P_v) = 1/κ.
- UT = I_m would then force m ≤ t/κ, that is, t ≥ mκ.
- CT's data has t ≤ m(D²/2 − 1) < mκ.
- So the criterion is a finite certificate that beats every rank function.
- It can exist only because Σ_f Σ_{v∈f} W_v = D·Σ_V W_v requires D = ℓ+1 = 0 in K. This is the trace's K23 ("Positive characteristic essential").
- A corollary of my own: if CT is right, **N itself is nonsofic**. N is a 2-dimensional amalgam of copies of F_ℓ² along lines with girth ≥ 12. That is a cheap sanity target, and it is listed as an open question.

**For N3.**
- No neighbour turned up in any field.
- The trace shows no retrieval for it.
- It turns the problem into finite incidence plus linear-algebra data (F5).
- It organizes the whole proof:
  - C3, C4 and C6 exist only to supply its hypotheses.
  - DT inherits it through Theorem 1.1.
  - OD's architecture is a sibling of it.

**Against N3.**
- Every component is standard: averaging idempotents, amalgams, HNN twists, specialization, and the DJ transfer.
- The trace reaches it at pivot distance 1 from its own early lessons (K11 and K12 at share 0.09; K19). The decisive clause K11 lay dormant from share 0.15 to 0.425.
- As in 287's C2, the eureka content lies in posing the data. Proving the criterion afterwards is routine.

**Where the proof budget goes.** It is spent on C4 (about 39% of the Lean lines) and C6 (about 34%), not on C1 (about 14%).
- That shape is Cook-like: a small certificate that organizes a large proof.
- But no compression check has been run.

## 4. Family verdict

**family_D: D3 (provisional), confidence 0.40.** It rests on C1 alone.
- **The headline manuscript TF on its own scores D2.** Its best items, T1 and T2, are adaptations of ZD, which is model-produced.
- **It falls to D2 if any of the following happens:**
  - Test 4 arm B hits for C1, which is plausible given the pivot distance of 1.
  - An expert names a prior finite "local cancellation / global identity" certificate against rank functions or stable finiteness.
  - OpenAI's August nonsofic manuscript turns out to contain a group-ring certificate of this kind. Press accounts say it does not.
- **Correctness caveat.** All four results are unrefereed and of the first rank. CT, DT and OD are Lean-formalized, but nothing was compiled here. TF is not formalized at all.

**provenance_flag: yes.**
- TF builds strictly on ZD (model-produced).
- DT builds strictly on CT (model-produced).
- The nonsofic corollary has a model-produced precedent (OpenAI, August).
- C1 itself has no model-produced precedent.

**bridge_novelty.**
- **New bridges** (first connection found):
  - RM line duality and coding products (Golowich–Lin, Dinur–Liu–Zhang) → group algebras (C3). This was retrieval-triggered in the trace.
  - TCS minrank and storage codes (Haviv, Golovnev–Haviv, Barg et al.) → DF in odd characteristic (O1).
  - Lamplighter projections + Fuglede–Kadison calculus → the implication "DF failure ⇒ Determinant Conjecture failure" (D1). The tools themselves are a known route.
- **Known routes:**
  - random graphical small cancellation → torsion-free group-ring identities (Rips–Segev, Steenbock, Mineyev 2024, ZD);
  - sofic/surjunctive corollaries;
  - complexes of groups / small cancellation for embeddings;
  - LLL for high-girth systems;
  - Linnik;
  - within the release, Lipton–Tarjan and projective-plane types (both from ZD).

**Methodological precedents.**
- **Gardam (2021).** He fixed a group (Promislow) and found an F₂ unit by SAT search. The SATURN project aims to do the same for direct finiteness and says success "will give the first example of a non-sofic group".
- **197 does no search.** It designs the group around a finite certificate (CT) or a parity count (TF), then proves the group is nondegenerate.
- **Nearest precedent for "build the group from the cancellation".** Dykema–Heister–Juschenko's ULIE groups do this, but they are built from support patterns rather than incidence data, so they are genuinely different.
- **Elek–Szabó** is the obstruction that C1 is built to defeat.

## 5. Discoverability (Test 4, not run)
The full specifications are in `novelty.json → discoverability_protocols`.

**Models.**
- Training cutoff strictly before **2026-07-31**, the first circulation of the OpenAI nonsofic paper.
- A canary probe excludes any model that:
  - knows a nonsofic group;
  - knows a claimed Kaplansky counterexample;
  - recognises the item names.
- No tools or browsing.
- The Astra / GPT-5.6 Sol lineage runs only as an uncontrolled reference arm.

**Library arms.**
- **L⁻** (main): the OpenAI companions removed.
- **L⁻⁻** (CT only): also removes Golowich–Lin and Dinur–Liu–Zhang, to measure the retrieval effect the trace shows for C3.
- **L**: adds ZD (for TF) or CT (for DT/OD), to measure how much the model-produced precedent raises hit rates.

**Prompt arms.** Open vs directed.

**Sampling.** n = 256 per arm; report pass@k for k = 1…256.

**Judging.** Two LLM judges plus a human group-ring expert. Lean targets where they exist:
- `AlgebraicCriterion.square_witnesses`;
- `PolynomialPairing.sum_complement_gram`.

**Item-level protocols.**
- **P-C1 (decisive).**
  - Hide thm:criterion and everything downstream.
  - Arm A gives a rank-function hint; arm B gives only the open problem.
  - A hit is a finite certificate that combines finite-subgroup idempotents, a rectangular identity UT = I_m with t < m·(inverse idempotent rank), and characteristic-dependent local cancellation.
  - Trace: pivot distance 1, chain depth 1.
- **P-C3.** Run L⁻ vs L⁻⁻. Trace: pivot distance 1 given GL/DLZ; chain depth 2.
- **P-T1.** Run with vs without ZD. Without ZD, it really tests family 196's parity mechanism. No trace exists.
- **P-D1.**
  - The trace shows the idea already at share ~0.05 (L101–105), as a conditional "lamp projection … negative logarithmic determinant" obstruction.
  - Pivot distance 1, chain depth 1.
- **P-O1.** Run with vs without CT.
- **Controls.**
  - Negative: C6, C7, C9.
  - Positive: Cook–Reckhow ER variables.

## 6. Open questions
1. Compile the Lean code and build a declaration-level DAG. The shares above come from a file-name heuristic.
2. Sanity-check the derived consequence that the glued group N is nonsofic. The trace raised Wise's polygons of finite groups at L858–864 and left the question unexplored.
3. Ask experts (Jaikin-Zapirain, Thom, Elek, Juschenko):
   - whether rank-violating finite certificates are known;
   - whether "DF failure over F_p ⇒ Determinant Conjecture failure" is known or folklore.
4. Read OpenAI's August nonsofic manuscript to confirm it contains no group-ring certificate.
5. Run a novelty pass for family 196. The parity mechanism originates there, and Mineyev 2024 is its nearest human precedent; I saw that preprint only through a search summary.
6. Spot-check all quotes that came through the WebFetch summariser.
