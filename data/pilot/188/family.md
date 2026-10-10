# Family 188: "The sharp terminal leave in random triangle removal" (family analyst, paper + Lean)

Sources at commit fd4aeeb:
- Paper: `preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/build/`. `paper.tex` inputs `introduction`, `prefix`, `queries`, `stability`, `coupling`, `witnesses` and `moments` (1,914 lines in all). The bibliography has 10 entries.
- Lean: `lean/OAI/Combinatorics/TriangleRemoval/` (287 files, 33,800 lines, 1,892 declarations), plus the comparator `lean/ComparatorChallenges/TriangleRemoval.{lean,json}`. It imports no other OAI directory.
- There is no reasoning trace for this family.
- The full item list is in `family.json`: 51 items, 43 from the paper and 8 Lean-only.

## 1. Main statement

**Thm main** (introduction.tex:36-48). For the uniform triangle-removal process started from K_n, E[(F_n/n^{3/2} − 1/(2√2))²] → 0. In particular F_n/n^{3/2} → 1/(2√2) in probability, and E F_n/n^{3/2} → 1/(2√2).

In words: delete uniformly random triangles until none are left. The number of surviving edges is then about 0.3536·n^{3/2}. Joos–Kühn's Conjecture 16.2 (arXiv 2412.15039v2, §16) predicts exactly this constant for the triangle case, but only in probability. The paper proves it in L². The paper does not claim the result for other starting graphs, for general F, or for fluctuations (introduction.tex:52-54).

**Lean comparator.** `OAI.SharpTerminalLeave.sharp_terminal_leave` is the conjunction of:
- the L² limit;
- the in-probability limit, for every ε > 0;
- the limit of the normalized mean.

It is stated over the following definitions:
- `Graph n := Finset (Finset (Fin n))`;
- `triangles` and `step`: delete a uniformly chosen triangle, or stay put when there is none;
- `terminalLaw n := evolve (completeGraph n) (n.choose 2)`.

**Match check: exact.** Running C(n,2) steps always reaches the absorbing state. The challenge definitions are textually identical to `Model.lean`.

**Formalized vs claimed.** All three parts of Thm main are formalized. The Lean does **not** formalize the paper's specialization of Joos–Kühn. It proves the prefix itself by a different, triangle-specific route (§5).

**Catalogue friction.** The comparator is missing from `lean/formalization.yaml`, although `OAI.lean:314` imports `Main` and `lean/docs/188.md` links it.

## 2. Trust surface

Grep over all 287 files:

| Pattern | Count |
|---|---|
| `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `set_option` | 0 each |
| `by decide` | 15 |
| bare `decide` tactic lines | 4 |

Every `decide` closes a literal side condition, such as `card (powersetCard 2 of a 3-set) = 3`, `2 ≠ 0`, or "the degree template is simple". About 100 further `decide`s are Bool coercions.

- Permitted axioms: propext, Classical.choice, Quot.sound.
- Imports: Mathlib only.
- **Not computer-assisted.**
- Caveat: Lean was not built here. The verdict comes from reading the text.

## 3. Labels

| Axis | Label | Evidence | Confidence |
|---|---|---|---|
| A | **A3** (sharp asymptotic constant; no explicit rate) | introduction.tex:39-40 | high |
| B | **B1** for the triangle case (it is B3 relative to the full JK Conjecture 16.2). Flag *full only with prior results* = **yes in the paper**: the JK prefix is a black box, "The only external proof input…" (introduction.tex:50-51). It is **no in Lean**. *Adds corollaries for other conjectures* = no. | introduction.tex:12-13, 31-33 | high |
| C | **C4 primary** (estimation chain: bootstrap, coupling, witness sums). Secondaries: **C5** (JK prefix, paper only), **C1** (auxiliary constructions: unfolding and formal witness graph, not the goal's witness), **C2** (induction in Lemma exact-paired-test; continuity bootstrap) | introduction.tex:116-117; queries.tex:95-96 | medium |
| C2 flags | ih_strengthened = **yes**, template **"strengthen to all substructures"**: the root statement is proved jointly with the pair-call statement. The bootstrap also carries I_{e,T} ≤ 1/2 ("carry an extra tracked quantity"). | queries.tex:85-86; stability.tex:69-74 | medium-low |
| Computer-assisted | **no** | | high |
| D | **D3 (provisional)**, resting on E1 and E2 below | introduction.tex:130-132 | low-medium |
| Provenance flag | **no**. All cited works are human-authored (1995–2025). The only 2025 entry is JK v2; its abstract page and full text contain no AI disclosure. | | high |

**E. Fields.**
- **Problem field:** Combinatorics (MSC 05C80, 05C70, 05B07, 60C05).
- **Lean-dir field:** Combinatorics.
- **Method fields:**
  - essential: probabilistic combinatorics (JK, priority representation); branching processes (Spencer); coupling and second moment; spectral graph theory (trace method); operator semigroups (Dyson–Phillips, Engel–Nagel); ODE bootstrap;
  - essential, Lean only: martingales (Freedman, re-proved), and the cavity-method naming;
  - background-cited: Penrose–Sudbury (adsorption), Bal–Bennett.
- **Cross-field essential count:** 5 (non-combinatorics).
- **Invoked without proof in the paper:** only JK (combinatorics). Everything else is re-proved in finite form.

## 4. Items: the highlights

There are 51 items in all (see the JSON). The key ones:

**Vocabulary, mostly N0–N1.**
- leave and F_n (I01);
- prefix trajectory and D = np² (I04);
- rooted templates, from JK (I05);
- the good-prefix proposition, cited from JK (I06);
- the priority scan, and its representation lemma (I08–I09).

**Query layer.**
- A *call* has a focus of one or two edges, a threshold and an omitted parent (I10). This is the recursive random-rank greedy oracle in the style of Nguyen–Onak / Spencer / Grable, specialized to pair foci. **N2.**
- The paired test with **one joint ordering and an expose-all rule** (I11) is "essential to the later visitation estimate". **N2.**
- Exactness lemma (I12): **N1.**

**Unfolding.**
- The *independent unfolding*, with fresh priorities per occurrence (I13): Spencer's branching process on the computation tree. **N1.**
- Factorial decay (I14): from Penrose–Sudbury. **N0.**
- q_e, q_{e,T}, I_{e,T} and the **product identities** (I15–I16): cavity/BP equations. **N1.** The Lean literally calls them `cavityOperator` and `cavityMessage`.

**Stability (Section 4).**
- Scalar law q(t) = (1+2Dt)^{−1/2}, from Spencer (I17). **N0.**
- Log time and z = log(q_e/q) (I18); edge-adjacency matrix A (I19); linearized error (I20). All **N1.**
- Link trace estimate from link-cycle counts (I21; Chung–Graham method). **N1.**
- Star approximation ‖M_u/D − 11ᵀ/N_u‖₂ small (I22). **N1.**
- **Star-average decomposition A/D = P + R**, with ‖R‖₂ = O(n^{−γ}) because each edge lies in exactly two stars (I23). **N2.**
- **P = UV, VU = I + W, ‖e^{−sP}‖_∞ ≤ 1 + 2s** (I24). **N2.**
- Finite Dyson expansion with mixed norms (I25), cited from Engel–Nagel. **N1.**
- **Prop semigroup: sup_{s≤log n} ‖e^{−sA/D}‖_∞ ≤ C(1+log n)^J** (I26). **Provisional N3, F5.**
- Prop unfolding, q_e = (1+o(1))q (I27). **N1.**

**Coupling and witnesses (Sections 5–6).**
- First-repetition coupling (I31). **N1.**
- Formal graph Γ, birth calls, properties (i)–(iv) (I32); ancestral paths and *extra-edge witness* (I33); witness lemma (I34). **N2.**
- Patterns (I35). **N1.**
- **Embedding bound with a last-L-births suffix template**, giving a length-independent D^{−B} (I36). **N2.**
- Off-pattern event O_x (I38). **N2.**
- **Visitation bound C_D³(2μ)^ℓ/(h!ℓ₁!ℓ₂!)** (I39). **N2.**
- **Prop collision: P(C_k) = O(D^{15−B} + 1/n) = o(1/D)** (I40). **Provisional N3, F3.**

**Moments (Section 7).** I41–I42 are standard: **N0.**

**Lean-only items.**
- L01 `ExposureTree` (free monad of exposures, with fresh and shared interpretations). **N1.**
- L02 discrete-grid priorities in Fin N, with N → ∞ error lemmas. **N1.**
- L03 cavity operator solved by Picard iteration in a BCF space. **N0**: transfer from the cavity method.
- L04–L05 a **moving star average** and mixed-norm stability on shrinking active edge sets. **N2.**
- **L06: a self-contained proof of the prefix.**
  - It tracks the centred codegree vector with drift −rate·(P + R) (`centered_edge_operator_drift`).
  - It closes an edge barrier by max-norm stability (`prefix_edge_barrier_improvement`), and gets degree/wheel tracking (hence link spectra), balanced-template tracking, and rooted upper bounds by moments from intact-survival probabilities.
  - It yields `UniformPrefixObligation` with failure ≤ exp(−(log n)^{4/3}), **without Joos–Kühn**.
  - Grade: **provisional N3, or N2 as a variant of E1.**
- L07 Freedman's inequality, re-proved. **N0.**
- L08 moment bound for rooted counts. **N1.**

## 5. Lean route differences

1. **The prefix is re-proved, not cited.** It has about 452 exclusive declarations and about 7.0k lines out of the 21.9k-line target DAG; `uniform_prefix_obligation` has a dominated share of 0.269. Its constants differ from the paper's: c = 1/80000, and polylog exponent 3·8001+2 instead of 2^{8002}−2.
2. **Grid priorities** in Fin N replace continuous uniforms, with explicit tie and grid errors.
3. **The product identities are solved analytically** (Picard / `cavityLimit`) instead of by an almost-surely finite random tree.
4. **Collision sum** is stated as C³(3·weight)^ℓ/ℓ!, a single factorial. The conclusion is the same o(1/D).
5. **The star-semigroup machinery is shared** between the continuation and the prefix: 171 shared declarations. `graph_star_semigroup_bound` is exactly ‖exp(−sP)‖ ≤ 1+2s.

**Dominated shares:**

| Branch | Share |
|---|---|
| survival moments | 0.588 |
| collision sum (E2) | 0.317 |
| prefix (E3/L06) | 0.269 |
| cavity relative (I27) | 0.077 |
| uniform semigroup (E1) | 0.035 |

## 6. Proof architecture
1. **Prefix.** Run the process to p = n^{−1/2+1/2000}. Degrees, codegrees, link j-cycle counts (j ≤ 8000) and rooted-extension bounds then hold with probability 1 − n^{−ω(1)}. The paper takes this from JK; Lean proves it (L06).
2. **Priority scan and exact paired recursive test** (joint ordering, expose all).
3. **Independent unfolding**, giving exact product identities.
4. **Stability.** In s = ½log(1+2Dt), z′ = −(A/D)z + small. Link traces give the star approximation, which gives P = UV with a controlled ℓ∞ semigroup. A mixed-norm Dyson expansion then gives a polylog bound on ‖e^{−sA/D}‖_∞, and the bootstrap closes: q_e ~ (1+2Dt)^{−1/2}.
5. **Coupling.** The finite and independent queries differ by at most P(a repeated exposed type). A repeat implies an extra-edge witness on two ancestral call paths.
6. **Witness sum.** Each step contributes pattern count 2 × b-factor 2 × 2D embeddings, i.e. 8D, against (μ^ℓ/ℓ!) visitation and a D^{−B} suffix gain. The total is O(D^{15−B}) = o(1/D).
7. **Moments.** First and second moments are 1+o(1). Then m·q(1)/n^{3/2} → 1/(2√2), giving L² convergence.

## 7. Eureka candidates (provisional)

| Rank | Candidate | Prov. N | F | For | Against |
|---|---|---|---|---|---|
| E1 | Max-norm semigroup via star averaging (I23–I26) | N3 | F5 | The paper names it as new; the naive bound loses e^{O(D)}; not a subterm of the goal or of L; Lean reuses it to prove the prefix | Ingredients are classical (trace method, line-graph incidence identity, push-through identity, Dyson expansion); dominated share 0.035 |
| E2 | o(1/D) collision bound (I32–I40) | N3 | F3 | Paper flags the sub-1/D precision as necessary; dominated share 0.317; off-pattern weighting turns D^ℓ into poly(D) | Decreasing-path 1/ℓ! (Nguyen–Onak, Penrose–Sudbury), cycle-in-exploration certificates and JK template bounds are all known |
| E3 | Lean-only prefix via moving-star codegree stability (L04–L06) | N3 / N2 | F2 | Replaces the 87-page JK black box with about 7k lines; BFL needed triangular extensions | No prose; within the family it is a variant of E1 |
| E4 | Paired-focus test with joint ordering (I10–I12) | N2 | – | "essential" per the paper | Nguyen–Onak oracle |
| E5 | Independent unfolding and cavity identities (I13–I16) | N1 | – | Load-bearing | Spencer 1995 / BP computation tree |

**Quick literature check** (WebSearch / WebFetch, 2026-10-09):
- **BFL 2015** (arXiv 1203.4223v3, full text read): no constant and no conjecture of one. The final phase appears only in the lower bound, through a uniform permutation of the triangles and local events (Sec. 6). Their method is scalar self-correcting martingales plus triangular extensions.
- **JK** (v2, full text read): §16 gives a Poisson/ODE heuristic and Conjecture 16.2. For triangles this gives n^{3/2}/(2√2).
- **Spencer**, "Real Time Asymptotic Packing" (1996/97): a modified greedy with growing D and an O(ND^{−1/k}ln^c D) leave. Not cited by the paper.
- **No 2025–2026 result** on the sharp constant was found, and no AI-assisted precedent.

## 8. Correctness concerns

**No gap found** on a line-by-line check (details in the JSON `checked` list). The following were verified by hand:
- the E₀ formula and the ‖E₀‖_∞ ≤ 1+2s bound;
- the exact z-equation;
- the short and long embedding cases;
- the visitation bookkeeping (fork factor, root factors);
- the exponent 15 = 3 + 12;
- the constant a_n → 1/(2√2);
- that the JK heuristic reproduces the same constant.

The Lean proves the identical comparator with no black box.

**Residual concerns:**
- The paper's mapping onto JK's conventions was not checked in detail; Lean bypasses it.
- The comparator is absent from `formalization.yaml`.
- L06 has no prose exposition.

## 9. Extraction friction
- Paper and Lean diverge on about a third of the DAG (the prefix).
- Lean uses cavity/message naming that the paper does not.
- Lean discretizes priorities, so paper lemmas map to grid lemmas plus N → ∞ limits.
- Many key "lemmas" are displays or paragraphs inside proofs.
- The new vocabulary is in inline `\emph` definitions.
- The extractor's definition ranking is uninformative: every definition has dominated share < 0.01.
- The catalogue marks the family as unformalized (it is absent from `formalization.yaml`).
