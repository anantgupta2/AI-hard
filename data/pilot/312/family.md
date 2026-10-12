# Family 312: The Grothendieck homotopy hypothesis

**Manuscript:** *The Grothendieck homotopy hypothesis via elementary expansions* (OpenAI, Sept 24 2026)

**Sources:**
- Paper: `preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/build`. Nine TeX files, about 2,000 lines.
- Lean: `lean/OAI/CategoryTheory/Globular`. 58 files, 12,753 lines, 1,034 declarations.
- Comparator: `GrothendieckElementaryExpansion`.

**Method:** text level only, at commit fd4aeeb. Nothing was built by this agent, so the orchestrator should run `lake build OAI.CategoryTheory.Globular.Main` and the comparator.

**JSON:** `family.json`, using the same keys as 103/287.

## 1. Main statement

**Theorem 1.1** (`sections/00-introduction.tex:50-69`) has four hypotheses:
- C is any Grothendieck coherator in the Ara–Henry convention;
- X is a cellular C-∞-groupoid;
- n ≥ 0;
- a: D_n → X is any cell.

The conclusion: the pushout i: X → X⁺ of the source inclusion s_n: D_n → D_{n+1} along a is a weak equivalence. A weak equivalence here means a bijection on π_0 and on every based π_r.

In words, this is **Henry's pushout conjecture** (Henry 2016, Conj. 5.3.3). Take a cellular weak globular ∞-groupoid and freely adjoin a new n-cell parallel to a chosen one, together with an (n+1)-cell joining them. This "elementary expansion" changes no homotopy invariant, even though the free algebraic construction creates many new composites and coherence cells.

Henry's reduction then gives two corollaries:
- Cor 5.1: the canonical left semi-model structure.
- Cor 5.2: a Quillen equivalence between Mod(C) and Spaces. This is the homotopy hypothesis in the title.

**Comparator:** `OAI.Grothendieck.elementary_expansion (C) (hC : C.IsCoherator) (X) (hX : X.IsCellular) (n) (a : disk C n ⟶ X) (Y) (i) (b) (square : IsPushout a (J C n) i b) : WeakEquivalence hC i`.
- The encoding is self-contained:
  - shapes are iterated pushouts of globes in presheaves on Globe;
  - a globular theory is a category on shapes with sum-preserving `base`;
  - `AdmissiblePair` has arity height ≤ n+1;
  - `IsFreeExtension`, `CellularPresentation` and `IsCoherator` follow the paper;
  - a model is a presheaf sending sums to pullbacks;
  - a cellular model is a transfinite composite of `BoundaryAttachment`s;
  - a weak equivalence is a bijection on components and on loops at the iterated chosen unit modulo `Joined`.
- **The match is exact** for Theorem 1.1. The solution's `Model.lean` contains every comparator declaration verbatim, up to namespace placement for the ten `Model.*` homotopy definitions.
- **Formalized:** Theorem 1.1 only. **Not formalized:** Cor 5.1, Cor 5.2 (the title claim), the division and change-of-boundary lemmas, Prop 2.4 (1)⇒(3), and two-out-of-three for W.

## 2. Trust surface
The scan covered all 58 files:
- `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `partial def`: 0 each.
- `decide`, `maxHeartbeats`, `autoImplicit`: 0 each.
- `Classical.choose`: 5. These cover the chosen unit, which is part of the statement, and chosen fillers.
- Imports: Mathlib only.

This is the cleanest trust surface the project has seen. One residual risk remains: no `IsCoherator` instance is ever constructed, so the comparator statement could in principle be vacuous. Mathematically a coherator exists (Θ_0 is initial and free extensions exist), so the risk is low.

## 3. Labels
| Axis | Label | Evidence | Conf. |
|---|---|---|---|
| A | **A1** (universal) | "the map i:X→X⁺ is a weak equivalence" (00:67-68). The corollary (homotopy hypothesis) is an equivalence of homotopy theories, but it is not the comparator target. | 0.9 |
| B | **B1** for Henry's conjecture. Flags: *full only with prior* (the homotopy hypothesis needs Henry 2016's reduction); *adds corollaries* (semi-model structure, homotopy hypothesis, coherator-independence; removes Taylor 2026's hypothesis in this setting) | "resolves Henry's pushout conjecture affirmatively" (00:75-76) | 0.8 |
| C | **C2** primary: descending induction on n at a fixed coskeletal cutoff q. Secondaries: C1 (partial-path functor), C5 (Henry 2016 for the corollaries; Ara 2013), weak C3 (retract and 2-out-of-3 arguments). Computer-assisted: **no**. | "We then hold q fixed and descend in the index n" (00:133-134) | 0.75 |
| C2 flags | ih_strengthened **yes**. Template: *add a parameter* (cutoff q), plus downward strong induction. The Lean IH weakens the conclusion to contractibility preservation but enlarges the class to all J_{≥r}-cofibrations (*strengthen to all substructures*). | 02:260-262 | |
| D | **D3, provisional**: the best item is the N3 candidate E1. | 00:106-110 | 0.45 |
| Provenance | No prior model-produced work found. Taylor 2026 (arXiv:2607.28540) appears human-authored (snippet-level check). | | |
| E | **Problem field:** Topology (MSC 55U35, 18N65, 55P15). **Lean dir:** CategoryTheory. **Method fields:** higher category theory (essential); homotopical algebra and the small-object argument (essential); universal algebra and sketches (essential); pasting-scheme combinatorics (essential); classical homotopy of spaces (corollary only); strict ∞-groupoids and type theory (background). | | |

The cross-field count is 1. About 10% of invoked results come from other fields. The problem field and the method field differ by formulation, not by transfer.

## 4. Proof architecture (paper)
1. **Algebraic setup.** The coherator is a tower built in free order, with arity height ≤ output dimension. Models are globular sets with interpretations of the operations. The paper fixes D_j, I_j, J_j and the cellular objects.
2. **Homotopy calculus**, following Ara 2013:
   - division with prescribed boundaries;
   - change of boundary;
   - the exact-boundary weak-equivalence test;
   - closure properties;
   - I-inj = W ∩ J-inj;
   - unit retractions of J_j.
3. **Cutoff reflector R_q** (Lemma 3.1). It is built in the coherator's free order and keeps all cells through q. Higher attachments preserve lower cells.
4. **Spines T_m(S)** and contractibility of free shapes, F(S) and F_q(S).
5. **Fixed q, descending induction on n.**
   - Top case E(q,q): a retraction plus unique fillers.
   - Upper-cell splitting and pushout (Lemma 3.6).
6. **Only the higher indices are used here.**
   - Tree diagrams are contractible: compare each tree with a string, then promote the edge homotopies through J_{n+1} "duplicates" (Prop 3.7).
   - Whiskered shapes H_ε(S) are contractible (Prop 3.8).
7. **Index-n partial cylinders P_j.**
   - Each P_j is stationary below n and is a single (n+1)-cell at n.
   - Above n, P_j is a small-object completion over the upper I_k.
   - An exact skeletal gluing from the whiskered shapes shows that all P_j, A_j^ε and P(S) are contractible (Lemma 4.1, Prop 4.2).
8. **Partial path functor 𝒫**, with (𝒫Y)_j = Hom(P_j, Y).
   - Every generator is interpreted in free order by extending A_j^{01} → P(S) over P_j, using the contractibility of P(S).
   - Each endpoint lifts every I_j.
   - The pair (p_0, p_1) lifts J_n through the four-vertex tree B (Prop 4.3).
9. **Retract argument.**
   - Let h be a section of p_0, and put u = p_1 h.
   - Joint lifting gives v = i u r ∈ W.
   - iu is a retract of v, so i ∈ W.
10. **Removing the cutoff.** An exact-boundary test in dimension k is detected in A_q for q ≥ max(n+1, k+1).
11. **Corollaries** follow through Henry 2016: the semi-model structure, then the Quillen equivalence with spaces.

## 5. Lean structure and route differences
The proof DAG has 856 declarations (451 theorems). Its share by file group:

| Group | Share of DAG |
|---|---|
| Statement and model infrastructure | 11% |
| Groupoid calculus and W-test | 15% |
| Cutoff reflector and colimit/realization plumbing | 28% |
| Small-object argument and lifting | 5% |
| Spines, whiskers, linear shapes | 15% |
| Cylinders and operation interpretation | 25% |
| Final assembly | 1% |

The mathematical core is about 46% of the DAG.

**Dominated shares**, computed with a patched extractor (see §9):
- `cutoff_elementary_exactBoundaryTest`: 0.735
- **`cylinderPathData`: 0.648**, the partial path object
- `cutoffFrame_whisker_hasFillers`: 0.272
- `whiskerFree_bounded_hasFillers`: 0.153
- `exists_cutoff(_reflection)`: about 0.06

**How the Lean route differs from the paper's:**
- **IH.** The Lean proves `ExpansionContraction q r` by strong induction on q−r: a J_{≥r}-cofibration from a cofibrant contractible object has a contractible target. It does not prove "J_n-pushouts are weak equivalences" at each step. A weak equivalence appears only in the final step, through `CutoffPathData`.
- **No W calculus.** The Lean has no division lemma, no change of boundary and no two-out-of-three. It uses only `ExactBoundaryTest`, `HasFillers` and the (3)⇒(1) direction of the test. The paper's §2.2 and most of the W calculus are therefore unnecessary for Theorem 1.1.
- **Trees.** Only whiskers and reverse whiskers are formalized. The J_{n+1}-duplication is replaced by `free_hasFillers_of_top_homotopy`: a small-object factorization, the IH for a contractible Z, and `lift_of_top_joined`, which shows F(S) is a retract of Z.
- **Joint lifting.** The Lean uses `criticalJoint_retract` instead of the tree B, and requires joint lifting for every J_k with k ≥ r.
- **Interpretation.** The Lean defines `cylinderTheory = representedTheory`, pairs of an operation with a cylinder map, and builds a section of `cylinderProjection` from the `CellularPresentation`.

## 6. Items
There are 34 items in the JSON: 32 from the paper and 2 Lean-only. Highlights:

| id | Item | N |
|---|---|---|
| I03 | Coherator convention (Ara–Henry) | N0 |
| I07–I13 | Ara's homotopy calculus, weak-equivalence test, closure, lifting tests, unit retraction | N0 |
| I15 | Cutoff reflector R_q, built in free order | N2 |
| I16, I20, I21 | Lower cells preserved, top case, upper-cell splitting | N1 |
| I17, I18 | Spines; free shapes are contractible (Lanari Prop 3.8) | N1 / N0 |
| I19 | E(q,n) with the cutoff parameter and descending order | N2 (part of E1) |
| I23, I24 | Tree and whisker contractibility via J_{n+1} promotion | N2 |
| **I25** | **Index-n partial cylinders P_j** | **N3 candidate (F3+F2)** |
| I26 | Exact skeletal gluing | N1 |
| **I27** | **Cylinder contractibility from the higher-index cases** | **N3 candidate (F2)** |
| I28 | Partial path functor; interpretation in free order | N2 |
| I29 | Endpoint-section retract argument | N1 |
| I31, I32 | Semi-model structure; homotopy hypothesis (via Henry) | N0 (corollaries) |
| I33 | Lean `ExpansionContraction` invariant | N2 |
| I34 | Lean `CutoffPathData` / `cylinderPathData` | N2 |

## 7. Eureka candidates
1. **E1: index-n partial cylinders bootstrapped by descending induction at a coskeletal cutoff** (I19 + I25 + I27, plus I28). Provisional **N3**, F3+F2.
   - *For.* Henry's conjecture has been open since 2016:
     - Lanari's full globular path object stopped short of interpreting all higher operations;
     - the work of Lanari and of Henry–Lanari only reached dimension 3;
     - Taylor 2026 still assumes a generalized form of the conjecture.

     The device is non-analytic: the cutoff, the "stationary below n" cylinders and the downward order appear neither in the goal nor in L. In Lean it dominates 65% of the DAG.
   - *Against.* Every part has a precedent:
     - cylinders (Métayer; Lafont–Métayer–Worytkiewicz; Lanari 2020, which the paper cites as its strategy);
     - coskeletal models (Henry–Lanari 2023, §2);
     - endomorphism-theory interpretation (Ara, Bourke 2016);
     - "path object with lifting ⇒ trivial cofibration" (folklore).

     The descending induction alone is an IH template. Novelty is the combination and the order. The device is tailored to the pushout lemma, so the speedup test should target related conjectures, for example (∞,n)-categories, other coherator conventions, or Taylor's controlled theories.
   - *Nearest neighbours:*
     - Lanari, arXiv:1805.00156;
     - Lanari 2018;
     - Henry–Lanari 2023;
     - Ara–Maltsiniotis on strict ∞-groupoids (Métayer cylinders);
     - arXiv:2604.09867, an upward inductive strategy that is conditional only.
2. **E2: promoting generator homotopies through already-covered J_{n+1} expansions** (I23, I24). Provisional **N2**. This is the classical cylinder/left-homotopy trick.
3. **E3: the Lean invariant `ExpansionContraction`** (I33). Provisional **N2**. It shows the paper's IH is stronger than needed and removes the W calculus from the proof.
4. **E4: the cutoff reflector in free order** (I15). Provisional **N2**. Coskeletal reflection is standard.
5. **E5: spines T_m(S)** (I17). Provisional **N1**.

**Literature check (2026-10-12).** Snippet-level searches still describe the pushout conjecture as open, and Taylor 2026 assumes it. No partial-cylinder or descending-cutoff argument turned up. WebFetch of arxiv.org failed with a DNS error, so no full texts were read.

## 8. Correctness concerns
- The headline **homotopy hypothesis is unformalized**. It relies on Henry 2016, an arXiv preprint: Thm 5.1.2(5), Prop 5.3.6–5.3.7 and Cor 5.3.12–5.3.13. It also relies on the paper's claim that a "typographical error" in Henry's Lemma 5.3.11 should be read as "acyclic fibration".
- **Convention dependence.** The bound "generator arity height ≤ output dimension" is load-bearing in two places: the cutoff (02:51-57) and the interpretation step (03:305-312). "Every Grothendieck coherator" means *in this convention*. Coherators in Maltsiniotis' or Taylor's sense are not covered.
- **Reading of Henry's definition.** The footnote at 01:113-118 reads Henry's Def 5.3.2, which prints n > 0, so as to include I_0. The theorem's n = 0 case depends on that reading.
- **Partial machine check.** The paper's tree argument for arbitrary orientations and its W-calculus are not machine-checked, because the Lean takes a leaner route. That route corroborates the core idea independently.
- **Vacuity.** The Lean never constructs an `IsCoherator` instance, so vacuity is not formally excluded. The risk is low.
- **Review status.** The work is unreviewed, and searches found no expert reaction.

## 9. Extraction friction
- **Extractor bug.** `scripts/extract_lean.py` v3 parses `theorem foo.{v}` as `foo.`. This affects 5 declarations, including the target, so the official `data/items/312_lean.json` reports 0/1 targets and an empty DAG.
  - The DAG figures above come from a scratch copy that strips the trailing `.`.
  - Suggested fix: in `DECL_RE`, stop the name before a `.{` universe suffix.
- **Inline definitions.** Key notions are defined in prose, not in definition environments: P_j, tree diagrams, whiskers, E(q,n) and coskeletal models.
- **Joining paper and Lean.** The two routes diverge, so items are joined by role rather than by name. The Lean names are descriptive, which helps.
- **Inflated closure shares.** About 28% of the Lean DAG is re-proved reflector, colimit and realization plumbing, which inflates closure shares. For example, `GlobularSet` reaches 80% of the DAG.
