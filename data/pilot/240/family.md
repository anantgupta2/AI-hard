# Family 240: Shelah's eventual categoricity and the prescribed-threshold obstruction

This is a FAMILY analysis of both manuscripts and the Lean, done at text level. The agent did not build the Lean, because the checkout is shared; the orchestrator compiles the comparator.

- Corpus: `openai/math` at fd4aeeb.
- Machine-readable version: `family.json` (59 items).
- Extractor v3 dump: `data/items/240_lean.json`.
- There is no reasoning trace.

| | 240-CH | 240-EC |
|---|---|---|
| Title | A CH obstruction to a prescribed categoricity threshold | Eventual categoricity for abstract elementary classes |
| Source | `preprints/A-CH-Obstruction-…/build/`: 7 sections, 2,563 TeX lines | `preprints/Eventual-Categoricity-…/build/`: 14 sections, 9,549 TeX lines |
| Lean | **yes**: `OAI/ModelTheory/Categoricity`, 15 files, 5,089 lines | **none** |

**Numbering caveat.** `paper.tex` inputs the CH files in the order 00, 01, 02, 04, 03, 05, 06, so the PDF section numbers differ from the file prefixes. This report cites `file:line` and LaTeX labels instead.

## 1. Main statements

### 240-CH (`00-introduction.tex:87-100`)
**Theorem 1.1, under CH.** There is an AEC K in a countable relational language with:
- (i) LS(K) = ℵ₀;
- (ii) at least two nonisomorphic models of size ℶ_{ω₂} = H(K) = ℶ_{(2^{ℵ₀})⁺};
- (iii) categoricity in every μ ≥ Λ = ℶ_{(2^{ℵ₁})⁺}.

So downward transfer from Λ⁺ to H(K) fails. Corollary `cor:consistency` then gives Con(ZFC) ⇒ Con(ZFC + ¬prescribed-threshold), using Gödel's L.

**Comparator** (`ComparatorChallenges/CHObstruction.lean`, target `OAI.CHObstruction.main`):
- Statement: `CH → ∃ L countable, ∃ K, K.IsAEC ∧ K.HasLSNumber ℵ₀ ∧ endpoint = hanf ℵ₀ ∧ K.TwoModels endpoint ∧ ∀ μ ≥ tailThreshold, K.Categorical μ`.
- Permitted axioms: propext, Quot.sound and Classical.choice.

**Match check.**
- The comparator definitions are textually identical (`diff -w`) to `Model.lean`.
- The AEC axioms are standard: chains of every nonzero ordinal length with smoothness, coherence, LS with the language bound, and isomorphism invariance. Categoricity includes existence.
- The statement matches (i)–(iii) exactly, including the endpoint Λ. I found no loophole.

**Not formalized:**
- `cor:consistency`, the metamathematical relative-consistency statement;
- the failure of joint embedding and amalgamation;
- the dense-cosieve obstruction in `06-booleanization`.

The sibling theorem `prescribed_transfer_fails` (Main.lean:253) is formalized.

### 240-EC (`01-introduction.tex:45-78`)
**Theorem 1.2.** For every λ there is μ(λ) such that, for every AEC with LS ≤ λ, categoricity in some κ ≥ μ(λ) implies categoricity in every κ' ≥ μ(λ).

- This is Shelah's eventual categoricity conjecture, claimed in **ZFC** with no amalgamation, joint embedding, tameness, large-cardinal or WGCH hypotheses.
- The threshold is existential.
- Nothing in this manuscript is formalized.

**Priority.**
- Espíndola (arXiv 1906.09169 v7, 2022) already claims a ZFC proof. EC calls it a "separate public claim" and says it imports none of Espíndola's interfaces.
- Shelah–Vasey (JEMS 2024) prove the conjecture only under a proper class of strongly compact cardinals, or under WGCH plus amalgamation.

**Consistency between the two papers.** The CH class is categorical on a tail, so it is compatible with EC. The obstruction only says that H(K) cannot be the ZFC threshold.

## 2. Trust surface (text-level grep over all 15 Lean files)
- None of the following appear: `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, the `opaque` keyword, `ofReduceBool`, `partial def`, `maxHeartbeats`.
- There are about 25 `decide` uses. All are Bool coercions of `b ∈ u` inside the xor bit law (Arrays.lean:21-22).
- The only imports are Mathlib and the family's own files.
- **Compile status: pending (orchestrator).**

## 3. Labels

| Axis | Family label | 240-CH (formalized) | 240-EC (unformalized) | Conf. |
|---|---|---|---|---|
| A | **A2** | A2: an explicit counterexample AEC | A1: universal transfer, with an existential threshold that only indexes the witness | 0.85 |
| B | **B2** (conditional on CH) | B2: refutes the prescribed-threshold form under CH. One-sided independence; contradicts Espíndola2023Spectra Thm 4.1 | B1 claimed, with contested priority | 0.8 / 0.3 |
| C | **C1** | C1 primary: the class is built. Secondaries: C3 (the fixed-pattern contradiction via collapse) and C2 (end-homogeneous trees) | C2 primary: induction on dimension and on maximum piece cardinality. Secondaries: C3 (elimination, binary trees, Fodor) and C1 (EM presentations) | 0.8 / 0.6 |
| C2 flags | ih_strengthened = **yes**, templated | uniform version: partition estimate for all χ < Λ | add a parameter (an extra axis) and strengthen to all faces/shapes, with prescribed boundary isomorphisms. This is the Shelah 1983 template | 0.7 |
| Computer-assisted | **no** | | | 0.95 |
| D | **D3 (provisional)** | D2 | D3, from EC-I12 and EC-I25 | 0.35 |
| Provenance | no | no model-produced precedent | cites the companion CH paper for context only | 0.8 |

**Device reuse inside the family.** Both manuscripts use the same unbounded-colour pigeonhole: CH `cat:finite-patterns` and the colour choice d_n in EC `found:order-template`. Each picks finite partition colours without a common infinite homogeneous set.

**E: fields.**
- **Problem field:** Mathematical logic (MSC 03C48, 03C35, 03C45, 03E50, 03E35).
- **Lean dir:** ModelTheory.
- **Method fields:**
  - set theory, essential: Erdős–Rado, Mostowski collapse, canonical functions ω₁→ω₁, Fodor, beth arithmetic, CH coding;
  - Gödel's L: corollary-only;
  - ordered groups and order theory, essential in EC: Hahn-type ℚ^{(ℤ^{(δ)})}, balanced cuts;
  - F₂ finite-support torsors, essential in CH;
  - model theory, the home field: EM models, orbit counting, minimal types, pregeometry, excellence;
  - topos theory: corollary-only (CH `06-booleanization`).
- **Cross-field count:** 3. About 60% of the invoked external results are set theory rather than model theory, and nearly all of them are re-proved locally.

## 4. Proof architecture

### CH
1. **Diagrams and tests.** Every countable extensional relation with rank tags below ω₁ is coded as a colour in 2^ω/=*; CH is needed for the count. The full subsequence test T_k demands that all restrictions agree exactly.
2. **The AEC.** For every tuple from the index sort I, there are row and column torsors over a locally countable DLO base B, carrying a bit matrix with the translation law.
   - **Objects** may have countably many failing columns per tuple.
   - **Strong extensions** may have no failing columns at new base points.
   - All the axioms are verified and LS = ℵ₀. In the Lean, `AEC.isAEC` dominates 32% of the DAG; this is verification plumbing.
3. **Endpoint.** Take I = V_{ω₂} and B = ω₁×ℚ. The tags f_{rank(x)}(β) come from the canonical ω₂-chain in ω₁^{ω₁} modulo countable sets, which makes every tuple's diagram valid outside a countable F_X. A countable-base model of the same size completes the pair of models at ℶ_{ω₂}.
4. **Tail.**
   - A fixed colour pattern at every arity would give a coherent direct limit of size > |V_{ω₁}| that collapses into V_{ω₁}, which is impossible.
   - If B is uncountable and |I| ≥ Λ, the profile palette has size 2^{ℵ₁} = ξ < cf(Λ). The partition estimates below Λ then extract such a pattern at a coordinate outside countably many exceptional sets. Hence |I| < Λ. In the Lean, `index_lt` dominates 21%.
   - Models with countable base are classified by |I|, because a triangular split of the difference matrix lets finite row and column translations absorb it (`Matrix.decompose`).

### EC
1. The set-code reduction from the uniform to the qualitative form, then EM order presentations.
2. **Orders H(δ) = ℚ^{(ℤ^{(δ)})}.** Every cut is balanced, so orbits of short tuples are determined by their order diagram plus slot occupancies. This gives a uniform orbit bound 2^{2^{ℓ+θ}} at every categoricity cardinal, singular ones included.
3. **Eventual reversal (Thm `found:reversal`).** Profiles of orbit names are pigeonholed across P⁺ failing categoricity sizes. Alignment of small submodels then feeds a θ⁺-round elimination chain, which makes strong maps reversible on bounded tuples.
4. **Closed levels.**
   - Strong-map classes stabilize.
   - K is categorical at every countably cofinal closure point of t (`lev:closure-categoricity`).
   - Uniform testing and compact placement hold.
   - Amalgamation and type bounds follow at closed levels.
5. **The "working scheme" interface.** It supplies free lifts by majority of approximation sequences, products, local character, universal fresh strips with approximate retractions, and relative isolation. Fodor then gives all-dominated (prime-like) hulls.
6. **Marked systems.** Marked increments yield finite marked systems C_n. A return-tree split (`iter:boundary-completion`) gives amalgamated boundary completion, and from it exact boundary lifting. This is excellence at closed levels, without WGCH.
7. **Geometry.**
   - A minimal type gives a pregeometry.
   - There is no Vaughtian pair: coherent systems J_n give a colimit over [I]^{<ω} of size μ with only λ points, which contradicts pointed categoricity.
   - On the whole tail, |P(M)| = ‖M‖.
8. **Geometric systems and transfer.**
   - Geometric systems of every admissible shape satisfy classification by basis maps and exact boundary lifting at one common level. That level comes from Section 13's G_ω hierarchy of closure levels.
   - A cardinal induction on the maximum piece size, adding one axis per step, gives pointed categoricity on a tail, then categoricity on a tail, then the uniform threshold.

## 5. Items (summary; full list in JSON)
- **CH: 24 items**, CH-I01 to CH-I24.
  - N0: the colour quotient, size of a locally countable DLO, canonical functions, Mostowski collapse, Erdős–Rado, Gödel.
  - N1: diagrams, coding, tests, AEC verification, free realization, triangular absorption, tail assembly.
  - **N2:**
    - the torsor bit-matrix basic structure (Hart–Shelah named as predecessor);
    - the **object-vs-strong asymmetry** (CH-I08);
    - the endpoint construction;
    - the no-fixed-pattern lemma (the abstract Morley/Hanf argument);
    - the bound for uncountable bases;
    - the topos obstruction.
- **EC: 35 items**, EC-I01 to EC-I35.
  - N0/N1: EM presentation, Erdős–Rado, the set-code reduction, minimal type, pregeometry, the closure bookkeeping, the excellence cardinal induction.
  - N2: orbit theorem, stabilization, closure-point categoricity, testing and placement, working schemes, free extension, isolation, marked and geometric systems, no-growth, approximate retractions.
  - **N3 candidates:** EC-I12 (eventual reversal) and EC-I25 (return-tree split).

## 6. Eureka candidates
| Rank | Item | N | F | Lean? | For | Against |
|---|---|---|---|---|---|---|
| 1 | EC-I12: eventual reversal by profile pigeonhole, alignment and an elimination chain | N3 | F3/F2 | no | Removes the κ^θ = κ and cofinality hypotheses behind the Shelah Ch. IV gap noted by Boney–Vasey 2015. Every later section rests on it | Parts are classical: EM orbits over homogeneous orders (Shelah IV.5.1), pigeonhole over profiles. Unaudited |
| 2 | EC-I25: return-tree split, whose accumulator keeps only boundary maps | N3 | F3 | no | Replaces WGCH/weak-diamond non-structure (still needed in Shelah–Vasey 2024) with an orbit-count contradiction inside one model | It is the classical "binary tree ⇒ many types" stability argument; the novelty may be bookkeeping only |
| 3 | CH-I08: object-vs-strong asymmetry with coded rank diagrams | N2 | (F3) | **yes** | The key design. It is load-bearing in Lean: `Data` has a 53% share of the DAG, `index_lt` dominates 21% and `twoModels` 15% | The paper names Hart–Shelah and Kolesnikov–Lambie-Hanson as precedents, and the Morley-style Hanf-sharpness coding pattern is classical |
| 4 | EC-I14: categoricity at countably cofinal closure points | N2 | – | no | Avoids WGCH | It is a standard back-and-forth |
| 5 | EC-I21: approximate retractions from a fresh strip | N2 | (F3) | no | A neat device, used at limit stages and for descent | EM universality is classical |

- **Literature checks** (WebSearch, snippet level):
  - Shelah–Vasey 1805.06291 needs strongly compacts or WGCH.
  - Boney–Vasey 1508.03316 fixes the syntactic gap using model-theoretic forcing.
  - Espíndola 1906.09169 claims ZFC.
  - Kolesnikov–Lambie-Hanson 1409.2508 studies coloring classes and the Hanf number for amalgamation.
  - None of them shows EC-I12's elimination chain or EC-I25's boundary-only accumulator.
- **Shortlist consequence:** there is no Lean-eligible N3 item. The formalized CH tops out at N2. EC-I12 and EC-I25 belong on `data/eureka_informal.json` only.

## 7. Correctness concerns
- **CH:** checked line by line, and every step holds:
  - the count under CH;
  - well-definedness of the colours;
  - LS, by absorbing all E_t into a convex hull;
  - canonical functions;
  - validity of the endpoint diagrams;
  - tagged collapse;
  - the partition estimate with cf(Λ) = ξ⁺;
  - the palette 2^{ℵ₁};
  - triangular absorption.

  The trust burden then moves to the Lean compile, which is pending. `06-booleanization` (the claim about Espíndola's step) and `cor:consistency` are not formalized; the former was not checked against Espíndola's preprint.
- **EC: an extraordinary, unreviewed claim on a central open problem, with a competing prior claim.**
  - Read in full and coherent: sections 2–4, 10 and 14.
  - Read only at statement level plus selected proofs: sections 5–9 and 11–13.
  - **Highest-risk points:**
    - Section 13: one common level for all finite depths, which needs uniform definability and totalized bound requests, with the descriptor set fixed before the hypothetical Vaughtian pair is chosen.
    - The return-tree argument, which depends on lower-dimensional completion and on the orbit bound over parameters.
    - Chain closure of marked pairs.
  - There is no Lean to fall back on.

## 8. Extraction friction
- The family has two manuscripts and only one is formalized, so the headline is split.
- The CH section numbers are shifted by the `\input` order (see the caveat at the top).
- The Lean route uses a normal-form `Presentation` (array Data/Point/Map with row/column shifts) instead of the paper's abstract torsors. The joins are by topic, and the names are descriptive.
- EC is written against an abstract working-scheme interface. Many results hold only "at sufficiently closed levels", so mechanical extraction of dependencies is unreliable.
- The extractor's ranking of candidate definitions is dominated by the `Data`/`Map` structures. Its lemma ranking is informative.
