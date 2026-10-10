# Family 330: "A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces"

Source: `preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026/build/` at commit fd4aeeb. The document root is `main.tex`; the catalog's `common.tex` is only the preamble. Lean: `lean/OAI/Analysis/LipschitzFree` (34 files, about 4,600 lines, 466 declarations). There is no reasoning trace for this family. The full item list (39 items, with Lean counterparts) is in `family.json`.

Base library L: Mathlib d13f23b plus the 17-entry inline bibliography.

## Main statement
**Thm main** (introduction.tex:39-43) says: *there is a countable, unbounded, nonproper pointed metric space with d(x,y) ≥ 1 for distinct points, such that F(M) has AP but fails λ-BAP for every finite λ ≥ 1.* This answers Kalton's question (Kalton 2004, p.185; Godefroy–Ozawa Q1; Godefroy survey Problem 6.2) negatively.

All the new mathematics is in **Thm blocks** (introduction.tex:92-105). For each p ≥ 1 there is a bounded, 1-separated, countably infinite block M_p, with diameter at most B_p = 300p²+150p+5, and a finite anchor set A_p. Every finite-rank operator of norm ≤ p moves some δ_a, a ∈ A_p, by at least 1/2.

The paper draws two corollaries:
- **Cor renorming:** real ℓ₁ has equivalent norms with 2B_p-BAP but not p-BAP. For p = 1 the norm fails MAP, which settles the open question of whether every renorming of ℓ₁ has MAP.
- **Nonlinear corollary:** F(M) is a separable space that is not approximable, which answers Kalton's Problem 1 negatively.

### Lean comparators and match
- **DiscreteLipschitzFree**, target `source_endpoints : BlockStatement ∧ MainStatement` (Main.lean:92).
  - It matches Thm main exactly.
  - It also matches Thm blocks for every p. The only gap is that "countably infinite" is stated as `Countable`, but infinitude follows from the obstruction.
- **RealL1Renorming**, target `real_l1_quantitative_renorming` (Renorming.lean:41).
  - It matches Cor renorming exactly.
  - The module structure is fixed, the norm is complete, and the BAP constants are explicit.
- Definitions check out:
  - `FreeSpace` is the closure of the span of the evaluations in the dual of `Lip0`, with the slope (Lipschitz-constant) norm.
  - `HasAP`/`HasBAP` use "∃η<ε with all errors ≤ η", which is equivalent on compact sets.
- **Not formalized:**
  - the nonlinear corollary, which rests on Kalton 2012 Thm 4.4;
  - the paper's random-graph local-limit lemma. Lean takes a different, deterministic route.

### Trust surface
Grep over all 34 files finds 0 each of `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe` and `opaque`, and no uses of `decide` at all. The only hit is the English word "admit" in a docstring. The permitted axioms are propext, Quot.sound and Classical.choice. Family 330 has no `formalization.yaml` entry. It is not computer-assisted.

## Labels
| Axis | Label | Evidence / note |
|---|---|---|
| A | **A2** (explicit-rate flag: yes) | Existence of a counterexample space. The blocks give explicit constants B_p (introduction.tex:40, 97-98). |
| B | **B2**. Flags: full-only-with-prior = no; adds corollaries = yes (ℓ₁ MAP renorming, formalized; Kalton approximability, not formalized) | "answering Kalton's question negatively" (main.tex:10). No cited theorem is needed for the headline. |
| C | **C1** primary; C3, C4, C5 secondary | C1: the block is built (blocks.tex:4). C3: proof by contradiction, and the graph sequence is obtained probabilistically. C4: a parameter budget ending in 2p > 11p (tests.tex:125). C5: Kalton's net theorem, used only for the nonlinear corollary. Not computer-assisted. ih_strengthened = no. |
| D | **D3, provisional** (low–medium confidence) | Max item: the edge-test complex I32 + I30 + I33. It drops to D2 if a judge treats it as forced once the record lemma is imported. Provenance flag: no (no model-produced source is cited). |
| E | Problem: Functional analysis (46B20, 46B28, 46B80). Lean dir: Analysis/LipschitzFree. Method fields, essential: Banach/free-space theory; random graphs and local weak limits; walk combinatorics; Lipschitz extension (McShane); free-group quotients (Lean only). Corollary-only: nonlinear Banach geometry (Kalton). Background-cited: quantum query complexity (Ben-David et al.) and descriptive set theory (Smith). | All cross-field material is re-proved inline. |

## Proof architecture
1. **Reduction** (reduction.tex).
   - Prop coefficients: a bounded, 1-separated N has F(N) ≅ ℓ₁ with 2B-BAP. This is cited to AACD20 and Cúth–Kalenda and re-proved.
   - The metric wedge of the blocks inherits each block's obstruction through contractive retractions, so it fails every λ-BAP.
   - Finite-block projections R_N then give AP.
2. **Block** (blocks.tex).
   - Take Δ-regular k-coloured multigraphs whose local statistics converge to those of the iid-coloured regular tree. The paper uses the permutation model. Lean uses large-girth Cayley quotients of the free group, crossed with *all* colourings.
   - Label each vertex by h_i = min(D, distance to colour class i).
   - Attach each vertex, at distance R, to the anchor of its label. Join the anchors by 2R + label distance.
   - Result: the block is bounded, labels are 1-Lipschitz, small balls stay inside one graph, and at most H label coordinates are uncapped.
3. **Operator to measures** (operators.tex).
   - Perturb the operator to one with finite support S and norm at most 2p.
   - Represent each Tδ_x by an affine signed measure μ_x with total variation at most V = 1+4pB.
   - Since the anchor a(x) is at distance R and the bump slope is L/K, ∫b_x dμ_x ≥ 3L/4.
4. **Rare matched walks** (walks.tex:50-110). Compatibility forces colours into sets of size ≤ H, and each state has ≤ Q possible successors. The bad fraction is therefore at most |S|(H/k)(ΔQH/k)^n.
5. **Records** (walks.tex:142-202). Record r_x(e,j) is the longest matched continuation through incidence e from state j. An incidence is exceptional when it is the strict argmax.
   - Lemma: across any edge, a compatible pair of states within distance 2L has one of its two directions exceptional.
6. **Edge tests and averaging** (tests.tex). Define f_e = b_x off E_e and −b_y off E_ē, then extend by McShane and clip.
   - Lower bound: the pairing with μ_x − μ_y is ≥ 3L/2 − 2L·(discarded variation).
   - Upper bound: it is ≤ 2p.
   - Averaging over incidences, the discarded variation is < 1/10, giving the contradiction 2p > 11p.

## Eureka candidates (provisional)
1. **I32 Lemma edge-test, with the exceptional sets and incidence averaging. Weak N3, F3.**
   - *For:* nothing like it is in the goal or in L. Each edge gets a 1-Lipschitz functional that is +bump(x) and −bump(y) on the operator's support, minus a combinatorially chosen discard set. This is where finite rank is played against the locally tree-like structure.
   - *For:* no analogue turned up in the Lipschitz-extension literature (Naor–Rabani; Naor's almost-extension; Godefroy–Ozawa; Brudnyi–Brudnyi).
   - *For:* Lean dominator shares put the downstream theorems at 0.37–0.39.
   - *Against:* the discard rule is imported from TCS. Once opposing bumps are chosen, the conflict on close cross pairs is forced, and edge-averaging against an error diluted by the degree is a familiar pattern.
2. **I18 Label-anchor block (labels I17, bumps I22). N2, leaning N3; F3 with an F5 flavour.**
   - *For:* one device makes the block bounded (so it is ℓ₁ with BAP) and gives every vertex an anchor lever. The Lean label definitions are the only non-carrier declarations passing the 20% proxy (0.21–0.23).
   - *Against:* the labels are truncated Fréchet/Bourgain random-subset coordinates, and coning to hubs is a generic move.
3. **I31 Continuation records / at most one exceptional direction. N2.** The precedent is named in the paper. I checked it against the arXiv text of Ben-David et al. (2006.12760, §6.1.2): FindParent takes the argmax of nonbacktracking continuation lengths, and Lemma 58 derives l_v > l_u and l_v < l_u. Same argument; here it is deterministic and indexed by state. This is cross-field transfer.
4. **I25/I26 Matched walks and their rarity. N2.**
   - The definition is new.
   - The rarity proof is a first-moment count. Lean replaces it with an exact count over colourings.
5. **I07 Per-operator finite anchor obstruction in bounded blocks. N1–N2.** This is a framing contrast with obstructions to projections with prescribed range.

The other items are N0/N1: the free-space basics, Prop coefficients, the wedge, the local limit (Friedman / Benjamini–Schramm), McShane, the parameter bookkeeping, and the Lean derandomization (free-group quotients I37 and the all-colourings count I38).

## Correctness
**No gap found.** I re-derived every inequality:
- B = 300p²+150p+5;
- (2pR+1)/K ≤ 1/5;
- the TV bound;
- the strict-inequality contradiction in the record lemma;
- the cross-pair argument in the edge test;
- the final 11p > 2p.

The Lean independently machine-checks Thm main, Thm blocks and Cor renorming by a partly different route.

Residual concerns:
- **Nonlinear corollary.** The non-approximability claim (Kalton's Problem 1) is not formalized. It depends on the exact form of Kalton 2012 Thm 4.4, which I did not verify.
- **Size of the claims.** Three long-standing questions are claimed at once, and the work is unreviewed. A web check (Oct 2026) found Kalton's question listed as open before this release. The closest prior work is Smith (arXiv 2509.00722): countable complete discrete spaces that are not uniformly discrete, obtained non-constructively.

## Extraction friction
- **Catalog:** main_tex points to the preamble, and the bibliography is inline.
- **Inline definitions:** core definitions are inline `\emph` or display math (anchor, compatible, matched, good/bad, exceptional, record, label, bump).
- **Comparator naming:** the comparator name `source_endpoints` is opaque and bundles two theorems.
- **Lean–paper join:** the Lean graph construction differs from the paper's, so joining by name fails. The paper's Remark abstract-obstruction (tests.tex:143-174) is the right interface to join on.
- **Load-bearing proxy:** the proxy flags carriers and labels but not the record/edge-test machinery (3–6%).
- **Dead code:** BlockPaths.lean appears to be dead code.
