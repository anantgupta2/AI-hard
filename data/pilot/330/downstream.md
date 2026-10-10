# Family 330: downstream targets for the eureka item

**Item:** Operator-adapted opposing edge tests with exceptional discard sets, plus incidence averaging (paper I32+I33, using the records lemma I30/I31), for Lipschitz-free spaces over uniformly discrete blocks (type F3 (lemma-level device inside a witness construction)).

*Text-level analysis; the Lean was not compiled. Web tools hit a session quota; references marked [subagent] were checked by a subagent against arXiv full texts or abstracts, and [memory] ones are unverified.*

**Bottom line.** The edge test and incidence averaging are in the Lean as in the paper, generic over port graphs, and on both comparators' paths. Only the surrounding graph supply is derandomised. No strong *speedup* target on a different known theorem was found. The device is tied to locally tree-like large-degree graphs and to a norm bound on finite-rank operators. The best Lean-usable experiments are portability (S1), the proper-space residue of Kalton's question (O1), and the cheap possible corollary for Godefroy–Ozawa Q3 (O2).

## Part A: is the item in the Lean?

**lean_status: as in paper.** `MetricBlock.edge_test` (ScalarTests.lean:119) is the paper's Lemma edge-test almost verbatim: a 1-Lipschitz f into [−L,L] equal to b_x off E_e and −b_y off E_ē, built by McShane extension and clipping from the record/exceptional-direction lemma. The averaging is `signed_incidence_obstruction` (SignedTests.lean:207), with the paper's constants (3L/2, 2L, 1/(20V), L = 10p). It sits on the comparator path of both DiscreteLipschitzFree and RealL1Renorming. Only the graph supply around the item takes a different route (deterministic, below).

### Gaps between the paper and the Lean

- **Different graph supply (outside the item).** Paper: Δ-regular k-coloured multigraphs from the permutation model whose coloured local statistics converge to the iid-coloured regular tree (local-limit lemma, Friedman / Benjamini–Schramm), then a first-moment bound for rare matched walks. Lean: Cayley quotients of free groups crossed with *all* colourings (`GraphProducer.sequenceGraph`, `allColoringsGraph`), and an exact colouring count `GraphProducer.exists_rare_component` (GraphSequence.lean:17) for the bad-vertex fraction 20·V·|bad| < |X|. The edge test and averaging do not depend on this choice: they are stated for an arbitrary `PortGraph`.
- **The paper's Remark abstract-obstruction (tests.tex:143-174) is not a standalone Lean theorem.** Its generic content is spread over `PortGraph`-generic lemmas (`matched_exceptional_endpoint`, `exceptional_endpoint`, `edge_test`, `opposing_pairing_lower`, `signed_incidence_obstruction`). The assembly `finite_support_impossible` is specialised to `BlockConstruction.Block p`. Packaging the remark as a reusable theorem over abstract (N, A, G_m, h) data would cost roughly 60–120 lines. That would make design-reuse tests cleaner.
- **Nonlinear corollary not formalized.** 'F(M) is separable and not approximable' (Kalton 2012 Problem 1, via Kalton's Thm 4.4) is not in the Lean or the comparators (family.md).
- **Comparator wording: 'countably infinite' becomes `Countable`.** In `BlockStatement` (DiscreteLipschitzFree.lean). Infinitude is proved separately (`BlockConstruction.infinite_block`) and is also forced by the obstruction, since F of a finite space is finite-dimensional and has 1-BAP.
- **Exceptional sets at bad vertices.** As in the paper: `exceptionSet` puts every state into E_e when x is not `Good` (ScalarTests.lean:59). The Lean compatibility threshold `K+2L+1` (`Compatible`) matches the paper's strict bound '< 1+K+2L' up to the ≤/< convention.

### Comparator chain

Main path, from the comparator theorem down to the item:

`OAI.DiscreteFree.source_endpoints` → `OAI.DiscreteFree.blocks_proved` → `OAI.DiscreteFree.BlockConstruction.obstruction` → `OAI.DiscreteFree.BlockConstruction.finite_support_impossible` → `OAI.DiscreteFree.MetricBlock.edge_test` → `OAI.DiscreteFree.MetricBlock.exceptional_endpoint` → `OAI.DiscreteFree.PortGraph.matched_exceptional_endpoint` → `OAI.DiscreteFree.exceptional_of_extensions`

Side branches that also reach the item:

- Averaging: `finite_support_impossible` → `signed_incidence_obstruction` (SignedTests.lean:207), fed by `opposing_pairing_lower` (:72), `bump_mass` (BlockObstruction.lean:76), `affine_difference_bound`, and `exceptional_unique_good` → `exceptional_unique` (SignedTests.lean:21).
- Scalar extension: `edge_test` → `opposing_scalar_extension` (SignedTests.lean:117) → `bounded_scalar_extension` (McShane plus clipping).
- Graph supply: `finite_support_impossible` → `GraphProducer.exists_rare_component` (GraphSequence.lean:17). This is the deterministic all-colourings count that replaces the paper's local-limit lemma.
- MainStatement half: `source_endpoints` → `main_proved` → `MainConstruction.noBAP` → `BlockConstruction.noBAP` (BlockBAP.lean:33) → `not_hasBAP_of_finite_obstruction` (BlockBAP.lean:15) → `BlockConstruction.obstruction` → … (as above).
- RealL1Renorming: `real_l1_quantitative_renorming` (Renorming.lean:41) → `BlockConstruction.noBAP p hp p le_rfl` → `obstruction` → `finite_support_impossible` → `edge_test`.
- The novelty pass gave dominator shares 0.37–0.39 for the obstruction subtree.

### Key Lean declarations (verbatim statements in `downstream.json`)

| Declaration | Kind | File:line |
|---|---|---|
| `OAI.DiscreteFree.PortGraph` | structure | `lean/OAI/Analysis/LipschitzFree/PortGraphs.lean:17` |
| `OAI.DiscreteFree.PortGraph.Matched` | def | `lean/OAI/Analysis/LipschitzFree/GraphWalks.lean:20` |
| `OAI.DiscreteFree.PortGraph.Good` | def | `lean/OAI/Analysis/LipschitzFree/GraphWalks.lean:42` |
| `OAI.DiscreteFree.PortGraph.RecordLength` | def | `lean/OAI/Analysis/LipschitzFree/GraphWalks.lean:54` |
| `OAI.DiscreteFree.PortGraph.record` | def | `lean/OAI/Analysis/LipschitzFree/GraphWalks.lean:58` |
| `OAI.DiscreteFree.Exceptional` | def | `lean/OAI/Analysis/LipschitzFree/SignedTests.lean:18` |
| `OAI.DiscreteFree.exceptional_unique` | theorem | `lean/OAI/Analysis/LipschitzFree/SignedTests.lean:21` |
| `OAI.DiscreteFree.PortGraph.matched_exceptional_endpoint` | theorem | `lean/OAI/Analysis/LipschitzFree/GraphWalks.lean:88` |
| `OAI.DiscreteFree.MetricBlock.Compatible` | def | `lean/OAI/Analysis/LipschitzFree/ScalarTests.lean:20` |
| `OAI.DiscreteFree.MetricBlock.Transition` | def | `lean/OAI/Analysis/LipschitzFree/ScalarTests.lean:23` |
| `OAI.DiscreteFree.MetricBlock.exceptionSet` | def | `lean/OAI/Analysis/LipschitzFree/ScalarTests.lean:59` |
| `OAI.DiscreteFree.MetricBlock.exceptional_endpoint` | theorem | `lean/OAI/Analysis/LipschitzFree/ScalarTests.lean:74` |
| `OAI.DiscreteFree.labelBump` | def | `lean/OAI/Analysis/LipschitzFree/LabelBumps.lean:17` |
| `OAI.DiscreteFree.opposing_scalar_extension` | theorem | `lean/OAI/Analysis/LipschitzFree/SignedTests.lean:117` |
| `OAI.DiscreteFree.MetricBlock.edge_test` | theorem | `lean/OAI/Analysis/LipschitzFree/ScalarTests.lean:119` |
| `OAI.DiscreteFree.opposing_pairing_lower` | theorem | `lean/OAI/Analysis/LipschitzFree/SignedTests.lean:72` |
| `OAI.DiscreteFree.signed_incidence_obstruction` | theorem | `lean/OAI/Analysis/LipschitzFree/SignedTests.lean:207` |
| `OAI.DiscreteFree.GraphProducer.exists_rare_component` | theorem | `lean/OAI/Analysis/LipschitzFree/GraphSequence.lean:17` |
| `OAI.DiscreteFree.BlockConstruction.finite_support_impossible` | theorem | `lean/OAI/Analysis/LipschitzFree/BlockObstruction.lean:102` |
| `OAI.DiscreteFree.BlockConstruction.obstruction` | theorem | `lean/OAI/Analysis/LipschitzFree/BlockObstruction.lean:176` |
| `OAI.DiscreteFree.not_hasBAP_of_finite_obstruction` | theorem | `lean/OAI/Analysis/LipschitzFree/BlockBAP.lean:15` |
| `OAI.DiscreteFree.BlockStatement (comparator)` | def | `lean/ComparatorChallenges/DiscreteLipschitzFree.lean:139` |
| `OAI.DiscreteFree.MainStatement (comparator)` | def | `lean/ComparatorChallenges/DiscreteLipschitzFree.lean:148` |
| `OAI.DiscreteFree.RealL1RenormingStatement (comparator)` | def | `lean/ComparatorChallenges/RealL1Renorming.lean:36` |

## Part B: where to try the item

### Speedup targets (known theorems)

#### S1. Thm blocks via the paper's own random-graph route (design reuse of the abstract obstruction)
- **Statement:** For each p ≥ 1 there is a bounded, 1-separated, countably infinite pointed metric space with a finite anchor set A such that every finite-rank T on F(M) with ‖T‖ ≤ p moves some δ_a by ≥ 1/2, where the graphs are random permutation-model Δ-regular graphs with iid colours (paper's Lemma local-limit + rare-walks), not Cayley quotients.
- **Reference:** 330 preprint, blocks.tex, walks.tex:50-110, tests.tex Remark abstract-obstruction.
- **Status:** known (the paper's own proof route; unrefereed)
- **Current proof size:** Paper: about 4 pages for walks + local limit. Lean: the deterministic route `GraphProducer`/`ColorCounting`/`GraphSequence` is about 300 lines. The item part (`ScalarTests` + `SignedTests` + `GraphWalks`) is about 570 lines.
- **How the item helps:** `edge_test`, `exceptional_endpoint`, `matched_exceptional_endpoint`, `opposing_pairing_lower` and `signed_incidence_obstruction` are generic in the `PortGraph`, so only the bad-fraction bound has to be re-proved for the new graph family. This measures how portable the device is. Caveat: it is the same theorem by a sibling route, not a different theorem.
- **Expected speedup:** high for the Lean (the item part is reused verbatim); not a jump signal on its own. Confidence: medium.
- **Lean feasibility:** score: **statable now**. Needs: `BlockStatement` (comparator) + Mathlib `Equiv.Perm` for the permutation model. Missing: permutation-model random graphs and their coloured local statistics (~200–300 lines, proof side only). Formal proof to compare: the OAI deterministic route (BlockObstruction/GraphSequence).

#### S2. Free spaces over diamond / Laakso graphs are not uniformly isomorphic to ℓ1ⁿ; projection constants of Lip0 over these graphs grow
- **Statement:** d_BM(F(D_n), ℓ1^{N_n}) → ∞ for diamond graphs D_n, and the relative projection constants of Lip0(Laakso graphs) are unbounded.
- **Reference:** Dilworth–Kutzarova–Ostrovskii, Canad. J. Math. 72(3) (2020) 774–804, arXiv 1807.03814, https://arxiv.org/abs/1807.03814; Positivity 25 (2021), arXiv 2007.07949 [subagent-verified bibliographic data].
- **Status:** known
- **Current proof size:** about 30 pp (CJM) + about 15 pp (Positivity). No formalization.
- **How the item helps:** Same shape of argument: one operator-norm bound, then averaging over a symmetric family. DKO average over cycle-preserving bijections (Grünbaum–Rudin), while 330 averages per-edge opposing tests over oriented incidences. An edge-test-style lower bound could replace the symmetrisation where the graphs lack a large automorphism group. Diamonds are not locally tree-like, though, so the records lemma has nothing to bite on. The analogy is loose.
- **Expected speedup:** low. Confidence: low.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean); Mathlib `SimpleGraph`, `lp`. Missing: diamond/Laakso graph sequences as metric spaces (~80 lines), Banach–Mazur distance or projection constant (~60 lines). Formal proof to compare: none.

#### S3. Lower estimates for the L1-distortion of transportation-cost spaces (planar grids, diamonds)
- **Statement:** The transportation-cost (free) space over the m×m planar grid has L1-distortion Ω(log m); similar sharp bounds hold for diamond graphs and for {1..m}^d uniformly in d.
- **Reference:** Gartland–Ostrovskii, 'Lower estimates for L1-distortion of transportation cost spaces', arXiv 2602.14852 (STOC 2026), https://arxiv.org/abs/2602.14852; Gartland–Ostrovskii–Rabani–Young, arXiv 2602.19434, https://arxiv.org/abs/2602.19434 [both subagent-verified].
- **Status:** known (2026)
- **Current proof size:** ≈ 20–30 pp; ≈ 15 pp. No formalization.
- **How the item helps:** Structurally the closest known method: systems of transportation problems on oriented edges (e⁺, e⁻) with ±1 sign matrices, averaged to force distortion for any linear map into ℓ1^m. The 330 edge test is also a signed per-oriented-edge test averaged over incidences, but adapted to the operator via discard sets. If the device helps anywhere outside BAP, this is the most plausible place. But planar grids are not locally tree-like and have no large degree to dilute over, so the records + degree-dilution part probably does not transfer.
- **Expected speedup:** low–med. Confidence: low.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean) (finite M); Mathlib `lp`. Missing: L1-distortion of a normed space (inf over linear embeddings into L1 / ℓ1^m; ~60–100 lines), grid metric (~30 lines). Formal proof to compare: none.

#### S4. Earthmover distance is not in L1 (planar; hypercube)
- **Statement:** Planar EMD over {0..n}² has L1-distortion Ω(√log n) (Naor–Schechtman); EMD over {0,1}^d has L1-distortion Ω(d) (Khot–Naor).
- **Reference:** Naor–Schechtman, SIAM J. Comput. 37 (2007) 804–826, arXiv cs/0509074; Khot–Naor, Math. Ann. 334 (2006) 821–852 [subagent-reported].
- **Status:** known
- **Current proof size:** ≈ 23 pp; ≈ 32 pp. No formalization.
- **How the item helps:** Weak. These are Fourier/Poincaré arguments about embeddings, not about finite-rank near-identity operators. Included because a prover holding the edge-test lemmas could try to recast them. Expect no gain; it doubles as a soft control.
- **Expected speedup:** low. Confidence: low.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean) (finite M). Missing: L1-distortion (~60–100 lines). Formal proof to compare: none.

### Open or new problems

#### O1. Kalton's question for proper / bounded-geometry uniformly discrete spaces
- **Statement:** Does F(M) have the BAP for every uniformly discrete M that is proper (closed balls finite), e.g. every locally finite graph of bounded degree, or every finitely generated group with a word metric?
- **Reference:** Kalton, Collect. Math. 55 (2004) 171–217, p. 185 (general question); Godefroy survey, Comment. Math. 55(2) (2015) 89–118, Problem 6.2, https://bibliotekanauki.pl/articles/746348.pdf; Hájek–Medina, arXiv 2112.03095, https://arxiv.org/abs/2112.03095 (reduction to nets; Schauder bases for nets in some spaces) [subagent-verified]. I found no explicit listing of the proper/bounded-geometry special case.
- **Status:** not found as a listed problem. 330 answers the general question with a non-proper space (the Lean proves `¬ ProperSpace M`), so the proper case becomes the natural residual question [status unverified].
- **Matching part of the obstruction:** Operator-adapted edge tests on locally tree-like coloured graphs of large degree; the records lemma; degree dilution.
- **How the item helps (adaptation sketch):** Direct transfer fails. The anchors attach infinitely many vertices at distance R, so each block is bounded but not proper. In a proper space a bounded block is finite, and then F is finite-dimensional with 1-BAP. Adaptation: replace one anchor per label by a finite hub tree of depth ~log, and let blocks be unbounded but uniformly locally finite. The averaging is already independent of |S|, but `bump_mass` uses d(x, a(x)) ≤ R with a fixed finite anchor set, so the 3L/4 bump bound breaks once anchors move to distance ~log|G|. This is a genuine obstacle. If it can be overcome, the payoff is large.
- **Payoff:** high. Confidence: low. Difficulty: high.
- **Lean feasibility:** score: **statable now**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean); Mathlib `ProperSpace`, `Countable`. Missing: none. Formal proof to compare: none.

#### O2. Godefroy–Ozawa Question 3 (generating compact convex Lipschitz retracts) and its 'mild form'
- **Statement:** Does every separable Banach space X contain a generating (closed span = X) compact convex Lipschitz retract? Hájek–Medina show that a mild form of this forces BAP.
- **Reference:** Godefroy–Ozawa, Proc. AMS 142(5) (2014) 1681–1687, arXiv 1201.0847, https://arxiv.org/abs/1201.0847; Hájek–Medina, arXiv 2202.08085, https://arxiv.org/abs/2202.08085 [subagent-verified; the exact 'mild form' not re-read here].
- **Status:** open (as of the subagent's reading)
- **Matching part of the obstruction:** 330 supplies a separable space failing BAP with AP (F(M), and the ℓ1 renormings at the isometric level).
- **How the item helps (adaptation sketch):** If the Hájek–Medina implication is '(mild form for X) ⇒ X has BAP', then X = F(M) from 330 violates the mild form, a possible negative answer as a corollary of the theorem rather than reuse of the device. To be checked against the exact HM statement. Recorded here because it is open and may fall immediately.
- **Payoff:** med–high. Confidence: low–medium (depends on the exact HM statement). Difficulty: low if the implication is as summarised.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean); Mathlib `IsCompact`, `Convex`, `LipschitzWith`, `Submodule.span`. Missing: Lipschitz retract definition (~20 lines); 'generating' (~10 lines). Formal proof to compare: none.

#### O3. Godefroy survey Problem 6.3: does Lipschitz approximability imply BAP?
- **Statement:** If a separable Banach space admits λ-Lipschitz maps with relatively compact range converging to the identity uniformly on compacts, must it have the BAP?
- **Reference:** Godefroy survey, Comment. Math. 55(2) (2015), Problem 6.3, https://bibliotekanauki.pl/articles/746348.pdf; Godefroy, CMUC 61 (2020) 187–193 may address it [subagent: not verified].
- **Status:** open in 2015; the 2020 status is unverified
- **Matching part of the obstruction:** The obstruction is linear (finite-rank operators of norm ≤ p against anchors). 330's F(M) fails BAP and, via Kalton 2012, is also not approximable, so it does not answer 6.3.
- **How the item helps (adaptation sketch):** Adaptation: a nonlinear edge test. For a Lipschitz map Φ: F(M) → F(M) with relatively compact range, compose with the per-edge 1-Lipschitz tests f_e. The measure representation μ_x (affine weights) is linear-specific, so one would need a barycentric replacement. Unclear.
- **Payoff:** high. Confidence: low. Difficulty: high.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean); Mathlib `LipschitzWith`, `IsCompact`. Missing: Lipschitz approximability property (~25 lines). Formal proof to compare: none.

#### O4. Does every Banach space with the BAP admit an equivalent norm with the MAP?
- **Statement:** Casazza's handbook problem (as cited by Godefroy–Ozawa, Problems 3.8/3.12): BAP ⇒ MAP after renorming?
- **Reference:** Casazza, 'Approximation properties', Handbook of the Geometry of Banach Spaces Vol. 1 (2001) [problem numbers via Godefroy–Ozawa 2014; wording unverified]; Godefroy–Lancien–Zizler, Rocky Mountain J. Math. 44 (2014), arXiv 1207.2958, Problem 18 [subagent-verified].
- **Status:** open as far as found [unverified]
- **Matching part of the obstruction:** 330's RealL1Renorming produces norms on ℓ1 failing MAP, i.e. the opposite direction (ℓ1 already has MAP in its usual norm).
- **How the item helps (adaptation sketch):** Mostly not. A counterexample needs an obstruction invariant under all renormings, but the anchor obstruction is p-quantitative and degrades by the renorming constant. Recorded as a direction where the device is expected not to help.
- **Payoff:** high. Confidence: very low. Difficulty: very high.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean) + the renorming encoding of RealL1Renorming (AddGroupNorm + compatible NormedSpace). Missing: general 'equivalent norm' quantifier over a Banach space (~40 lines). Formal proof to compare: none.

#### O5. Godefroy survey Problem 6.4: is the MAP (or a dimension-free BAP constant) available for F(M), M ⊂ ℝⁿ?
- **Statement:** For M ⊂ ℝⁿ, does F(M) have the MAP? Known: λ-BAP with λ ≤ C√n (Lancien–Pernecká). Is a bound independent of n possible?
- **Reference:** Godefroy survey (2015), Problem 6.4; Lancien–Pernecká, J. Funct. Anal. 264 (2013) [memory]; still called open in Hájek–Medina 2021 [subagent].
- **Status:** open
- **Matching part of the obstruction:** Opposite regime. The device needs exponentially growing locally tree-like structure at bounded scale, which doubling subsets of ℝⁿ cannot host. A lower bound λ_n → ∞ would need families in growing dimension.
- **How the item helps (adaptation sketch):** Probably not. Embedding the 330 blocks into ℝⁿ costs distortion that grows with the block size, and a bounded infinite 1-separated set cannot sit in ℝⁿ at all. Listed so the experiment can confirm the device's limits.
- **Payoff:** high. Confidence: very low. Difficulty: high.
- **Lean feasibility:** score: **statable now**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean); Mathlib `EuclideanSpace ℝ (Fin n)`. Missing: none. Formal proof to compare: none.

#### O6. Does F(N) have a Schauder basis whenever it has the BAP (N a net in a Banach space)?
- **Statement:** For nets N in separable Banach spaces, does BAP of F(N) imply a Schauder basis? Known for nets in finite-dimensional spaces, in spaces with a basis containing c0, and in separable L∞-spaces.
- **Reference:** Hájek–Medina, arXiv 2112.03095 and 2202.08032; Hájek–Novotný, arXiv 1606.03926; Aliaga–Medina, arXiv 2601.03131 (F(N_X) ≅ its ℓ1-sum) [subagent-verified]. No explicit problem listing found.
- **Status:** appears open (no explicit listing found)
- **Matching part of the obstruction:** Weak. The device obstructs BAP, not bases.
- **How the item helps (adaptation sketch):** Only indirectly: the wedge-of-blocks structure plus edge tests gives quantitative lower bounds on the norms of finite-rank near-identities on anchors, which bound basis constants from below. Expect no direct use.
- **Payoff:** med. Confidence: very low. Difficulty: high.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean); Mathlib Schauder basis API (subagent reports `Mathlib/Analysis/Normed/Module/Bases.lean`; presence at d13f23b not checked). Missing: net definition (~20 lines); Schauder basis, if absent at d13f23b (~80 lines). Formal proof to compare: none.

#### O7. L1-distortion of transportation-cost spaces vs stochastic tree-embedding distortion
- **Statement:** Is c₁(TC(X)) always comparable to the stochastic tree-embedding distortion of X? Related: Indyk's problem on the L1-distortion of EMD over n-point subsets of ℝ² (Matoušek–Naor open problems list, Problem 2.17).
- **Reference:** Gartland–Ostrovskii–Rabani–Young, arXiv 2602.19434 ('the most important question'); Gartland–Ostrovskii, arXiv 2602.14852 [subagent-verified]; Matoušek–Naor open problems list [memory].
- **Status:** open
- **Matching part of the obstruction:** Signed per-oriented-edge tests averaged over incidences (shared with S3); the operator-adapted discard part has no counterpart.
- **How the item helps (adaptation sketch):** A lower bound on distortion is a lower bound on norms of a linear map and its inverse. One could try opposing per-edge tests adapted to a given embedding T: F(X) → ℓ1^m, with records-based discard sets, on locally tree-like X. This is speculative.
- **Payoff:** high. Confidence: very low. Difficulty: high.
- **Lean feasibility:** score: **statable with < 300 lines of new definitions**. Needs: OAI `DiscreteFree.FreeSpace`, `delta`, `HasAP`, `HasBAP` (ComparatorChallenges/DiscreteLipschitzFree.lean) (finite M). Missing: L1-distortion (~60–100 lines); stochastic tree embeddings (~150 lines). Formal proof to compare: none.

## Theorem corollaries (reach, not reuse)

- **Kalton's question (uniformly discrete ⇒ BAP?) answered negatively.** Headline; formalized (DiscreteLipschitzFree).
- **Real ℓ1 has equivalent norms with 2B_p-BAP but not p-BAP; for p = 1 a renorming failing MAP.** Formalized (RealL1Renorming).
- **ℓ∞ with the dual norm is a dual space with BAP but not MAP (Godefroy–Lancien–Zizler Problem 18).** Via duality, per GLZ 2014 [subagent-verified that GLZ state this consequence]. Not in the Lean.
- **Any Banach space X ≅ ℓ1 ⊕ Y (e.g. L1[0,1]) has an equivalent norm failing MAP.** Renorm as (ℓ1, N₁) ⊕₁ Y. A 1-complemented subspace of a MAP space has MAP. Standard; my own remark, not in the paper or the Lean.
- **A uniformly discrete subset of c0 whose free space fails BAP.** Embed 330's M bi-Lipschitzly into c0 (Aharoni; Kalton–Lancien give distortion 2 [memory]); free spaces of bi-Lipschitz equivalent spaces are isomorphic. Corollary, not reuse.
- **A separable space with AP but not BAP (Figiel–Johnson 1973 phenomenon).** A one-line corollary of MainStatement. The same holds for F(M) explicitly.
- **F(M) is not approximable (Kalton 2012 Problem 1).** Paper's nonlinear corollary via Kalton's Thm 4.4; not formalized.

## Reuse inside the release

- **Whole release (preprint grep).** Phrases 'continuation record', 'matched walk', 'exceptional direction', 'opposing bump/test' occur outside 330 only generically: Falconer (an unrelated 'Exceptional directions' lemma), random 3-SAT ('pathwise continuation records' in a cascade argument), ball packings, Kuga–Satake, a projective fourfold, a random-environment zero-one law. No reuse of the edge-test design.
- **324/325 (Lipschitz equivalence; bi-Lipschitz absorption of c0), 332 (Markov cotype of ℓ1), PlanarL1, BoundedTreewidthL1, 098 (doubling Hilbert subset).** Same broad area (nonlinear Banach geometry, L1 embeddings). Their summaries show positive embedding/extension results or bi-Lipschitz constructions. None mentions finite-rank operator obstructions; not checked line by line.
- **OAI Lean.** A repo-wide grep of lean/OAI for `DiscreteFree` / `LipschitzFree` outside Analysis/LipschitzFree found no other file. Single-use device inside the release.

## Negative controls

- **N1: Doubling (e.g. Euclidean) uniformly discrete spaces, and nets in finite-dimensional spaces.** Expected: fails (proved-false analogue). F(M) has the BAP for doubling M (Lancien–Pernecká 2013 [memory]), and nets in ℝⁿ even give Schauder bases (Hájek–Pernecká; Hájek–Medina [subagent]). The device needs large-degree locally tree-like graphs at bounded scale (degree Δ > 20V with V = 1+4pB). Doubling spaces cannot host them, so any claimed obstruction there signals a bug.
- **N2: Renormings of ℓ_p (1 < p < ∞) and of c0.** Expected: fails (proved-false analogue). Every equivalent norm on these spaces has MAP: AP is an isomorphism invariant, and a space with AP that is reflexive, or whose dual is separable with AP, has MAP (Grothendieck; standard, e.g. Casazza's handbook chapter [memory]). So the RealL1Renorming pattern cannot transfer from ℓ1 to these spaces.
- **N3: Drop the operator-norm bound, or raise it to ≥ 2B_p on a single block.** Expected: fails (proved false inside the release). The same space has AP (`MainConstruction.hasAP`), and each bounded block has 2B_p-BAP (`bounded_separated_hasBAP`, used in Renorming.lean). So the edge-test contradiction (2p > 11p, which uses ‖T‖ ≤ 2p) cannot extend to unbounded or ≥ 2B_p-norm finite-rank operators. Good for checking that a prover does not over-apply `signed_incidence_obstruction`.

## Top 5 (Lean-usable first)

1. **Thm blocks via the random permutation-model graphs** (S1). Statable now (the comparator's `BlockStatement`). Everything item-specific is `PortGraph`-generic, so with the item in the library only the bad-fraction bound needs proving. It cleanly measures the item's portability across graph supplies, with a formal baseline (the OAI deterministic route). Not a different theorem, so a speedup here supports reusability, not a jump.

2. **Kalton's question for proper / bounded-geometry spaces** (O1). Statable now with the comparator's definitions. It is the residual open case after 330, and the place where the device's essential ingredients (degree dilution, locally tree-like coloured graphs) still make sense. The known obstacle (finite anchors at bounded distance) is precise, so a prover run will show quickly whether the device adapts.

3. **Godefroy–Ozawa Q3 via Hájek–Medina** (O2). Statable with < 50 new lines. It may fall as a corollary of 330's theorem (not of the device), so it is useful to check reach. Rank it above harder targets only because it is cheap.

4. **Gartland–Ostrovskii L1-distortion lower bounds** (S3). The structurally closest known method (signed per-oriented-edge transport tests), statable with ~100 lines. Expected speedup low–med. A hit would show that the opposing-test part of the device is the transferable kernel.

5. **Godefroy 6.4 (M ⊂ ℝⁿ) as a calibrated non-target** (O5). Statable now. The device is expected not to help (doubling geometry). Pairing it with N1 checks that the prover's use of the item is discriminating rather than blanket.

## Precedent check

**Earlier equivalent:** partial (the records sub-lemma only). The records / exceptional-direction lemma (I31) is a close variant of Ben-David–Childs–Gilyén–Kretschmer–Podder–Wang (arXiv 2006.12760, Lemma 58; checked in the novelty pass). This caps the sub-lemma at N2 but does not cover the operator-adapted opposing tests with discard sets or the incidence averaging. The structurally nearest 2026 work is Gartland–Ostrovskii (arXiv 2602.14852, STOC 2026): signed systems of transportation problems on oriented edges, averaged, to lower-bound L1-distortion. It is fixed (not operator-adapted), has no discard sets, and lives on grids and diamonds, so it is not an earlier equivalent. Its relation to I32/I33 deserves an expert look. Smith (arXiv 2509.00722) is a prior result, not a prior device: complete discrete, not uniformly discrete, via descriptive set theory. No Sept–Oct 2026 paper citing 330 or using an edge-test argument was found, but arXiv keyword search does not catch citations and the web quota cut the search short.

- Ben-David et al. 2020, Lemma 58: close variant of the records lemma (N2), already in L.
- Gartland–Ostrovskii 2026: closest technique in Banach/metric geometry. Signed oriented-edge tests, but not operator-adapted. Not an equivalent; flag for expert check.
- Dilworth–Kutzarova–Ostrovskii 2020: 'average over symmetries, then one operator norm bound'. Generic pattern, not equivalent.
- Smith 2025: prior partial answer to Kalton by a different method.
- Post-2026-10-06: nothing found (search incomplete).

## Sources

- data/pilot/330/family.md, family.json, novelty.md, novelty.json; data/eureka_shortlist.json (rank 11 entry)
- data/raw/openai-math/lean/OAI/Analysis/LipschitzFree/{Main,BlockObstruction,BlockBAP,ScalarTests,SignedTests,GraphWalks,GraphSequence,LabelBumps,MetricBlock,PortGraphs,Renorming}.lean (text level)
- data/raw/openai-math/lean/ComparatorChallenges/{DiscreteLipschitzFree,RealL1Renorming}.{json,lean}; lean/docs/330.md
- preprint Failure-of-Bounded-Approximation-…-September-26-2026/build/sections/tests.tex, introduction.tex
- data/raw/openai-math/CONTENTS.md (release scan)
- https://arxiv.org/abs/1201.0847 (Godefroy–Ozawa) [subagent]
- https://arxiv.org/abs/1207.2958 (Godefroy–Lancien–Zizler) [subagent]
- https://arxiv.org/abs/2509.00722 (Smith) [subagent]
- https://arxiv.org/abs/2604.01875 (Cúth–Kalenda) [subagent]
- https://arxiv.org/abs/2112.03095, https://arxiv.org/abs/2202.08032, https://arxiv.org/abs/2202.08085 (Hájek–Medina) [subagent]
- https://arxiv.org/abs/2601.03131 (Aliaga–Medina) [subagent]
- https://arxiv.org/abs/2602.14852 (Gartland–Ostrovskii) [subagent]
- https://arxiv.org/abs/2602.19434 (Gartland–Ostrovskii–Rabani–Young) [subagent]
- https://arxiv.org/abs/1807.03814 (Dilworth–Kutzarova–Ostrovskii) [subagent]
- https://arxiv.org/abs/2305.07591 (Talimdjioski; answers Godefroy 6.6) [subagent]
- https://arxiv.org/abs/cs/0509074 (Naor–Schechtman) [subagent]
- https://bibliotekanauki.pl/articles/746348.pdf (Godefroy 2015 survey) [subagent]
- Memory-only, unverified: Lancien–Pernecká 2013; Aharoni / Kalton–Lancien c0 embeddings; Casazza handbook chapter; Grothendieck AP ⇒ MAP for reflexive/separable duals; Matoušek–Naor open problems list

## Search log

- Local: traced `source_endpoints` → `blocks_proved` → `obstruction` → `finite_support_impossible` → `edge_test` / `signed_incidence_obstruction`; and `real_l1_quantitative_renorming` → `BlockConstruction.noBAP`.
- Local: compared `edge_test` against tests.tex Lemma edge-test and the averaging proof (constants 3L/2, 2L, V/Δ + Vβ < 1/10, 11p > 2p).
- Local: preprint-wide grep for 'continuation record | matched walk | exceptional direction | opposing bump/test' (only generic hits outside 330).
- Web (subagent, arXiv API + full texts after the WebSearch quota): Kalton question status (Cúth–Kalenda 2604.01875), Smith 2509.00722, Godefroy survey problems 6.1–6.7, Godefroy–Ozawa Q1–Q4, Hájek–Medina nets/bases/retracts, Aliaga–Medina 2601.03131, Gartland–Ostrovskii(-Rabani–Young) 2026, DKO 2020/2021, Talimdjioski 2305.07591; arXiv date-sorted searches for BAP/MAP/Kalton 2026 (no 330 follow-ups found).
- Lean: not compiled; all Lean claims are text-level.
