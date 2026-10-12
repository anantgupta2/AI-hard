# Family 161: novelty pass (Sidorenko and forcing counterexamples)

Analyst role: novelty. Date: 2026-10-12. Machine-readable version: `novelty.json`.

Inputs:
- `family.json` / `family.md`. There is no trace and no `f1_*` file.
- The paper: introduction, the full kernel section, and excerpts of transverse and orbits.
- The bib.
- Lean, read at text level only. Per the user, the release's Lean is trusted as published.

**Access caveat.** WebFetch failed for every host (DNS), and curl to arxiv.org got a proxy 403. All literature evidence below comes from search-engine summaries plus domain knowledge, so the quotes are **unverified**.

## Provenance verdict: **no**
- **2026 citations.** The paper cites two 2026 works, and both are human mathematics:
  - Im–Li–Liu (CPC 2026; arXiv 2024).
  - Zhao, arXiv:2606.15368. It declares ChatGPT for *language polishing / readability only*.
- **Model-driven prior attempts on Sidorenko exist, but all are negative.** Each targeted K₅,₅∖C₁₀ and found no counterexample, and none contains any device of this paper:
  - AlphaEvolve, arXiv:2511.02864 (Nov 2025);
  - the multi-agent "Station", arXiv:2608.23691;
  - Duke Math+ 2025 (RL / AMCS search).
- **The only other AI activity post-dates the release:** Codex-assisted GitHub "template refinements" of 161 (Oct 2026).

## Final grades

| ID | Item | Provisional | **Final** | F | Conf. | Lean-backed |
|---|---|---|---|---|---|---|
| C1 | Rank-layer limit: signed half-rank kernel → limiting pair-sign model (I07+I08+I25) | N3 | **N3 (provisional)**; the object I07 alone is N0 | F5 | 0.40 | **yes** (`rankLayerConvergence`, `complementary_rank_iff`, `typedMatrixKernel_tendsto`), but specialised to this complex |
| C2 | Two-branch activation law + support forcing (I12, I15, I16) | N3 | **N2** | n/a | 0.55 | yes (`basePairLaw_identity`, `corner_support`, `cornerSigma`) |
| C3 | Witness H: Levi graph of a 13-vertex triangulated 2-sphere (I03) | N2 | **N2** | n/a | 0.70 | yes (`Basic.lean faces/H`) |
| C4 | WL pinning + Gibbs tilting (I17, I18) | N2 | **N2** | n/a | 0.75 | yes |
| C5 | Six-class exposure, slack, coercivity, propagation (I04, I35–I38) | N2 | **N2** | n/a | 0.70 | yes |
| C6 | Typed activation kernel + zero-first-moment design (I11, I12) | N2 | **N2** | n/a | 0.70 | yes |
| C7 | Dilution asymmetry ε¹³ vs ε²² + crossed product (I19, I20) | N2 | **N2** | n/a | 0.75 | yes |

**family_D = D3 (provisional), confidence 0.4.** It rests on C1 alone; C2 drops to N2.

## C1: why it survives, and why only narrowly
**What it is.** For half rank D = 2r, there is a nonnegative mean-one kernel K_ξ(Z) = 1{rank Z = r, sign Z = ξ}/P. Integrating out a face "center" Y_j turns the three incidences of a face into an *exact, full-strength* product of pair-sign factors (1 + c₀η_eξξ′). The pair signs η_e = χ(det(X_i − X_k)) are asymptotically independent.

**Why half rank.** A common center at half rank forces complementary images, so χ(det B) = c₀ξ₁ξ₂.

**What the device does:**
- It makes a bipartite incidence density behave like a **signed 3-uniform hypergraph model**.
- That model is exactly what the known hypergraph counterexamples have for free. These are Sidorenko 1993 (the loose triangle) and Conlon–Lee–Sidorenko 2023 (sign weights; even subgraphs weighted (−c)^{e(F)}).
- Lovász's local theorem and Fox–Wei show that a graph counterexample must achieve this far from the constant kernel. Naive common-neighbour moment kernels give only *positive* pair correlations.

**The four tests:**
- **Test 1.** No neighbour found that realises a signed hypergraph model inside a bipartite homomorphism density.
  - The closest work is the hypergraph *target* (close variant of the target, different realisation).
  - The arithmetic analogue is quadratic phases giving sub-random counts for linear systems (Gowers–Wolf, Fox–Pham–Zhao).
  - The method family is algebraic F_q hosts in Turán problems.
- **Test 2.**
  - **I07 alone fails.** It is a normalised class of the Huo–Wan/Schmidt association scheme, which is in L. That is N0 transfer.
  - **I08 passes.** It is judged against the problem as originally posed, since the witness is in the formal goal.
- **Test 3.** Maximal. About 84% of the Lean lines prove it, and it is the only analytic input.

**Downgrade risks:**
- A strict judge may call C1 a *new bridge* built from N0 parts (scheme class, complementary images, Gauss sums). That would make it N2.
- Once "use a common center to emulate the hypergraph parity target" is given, half rank may follow at pivot distance about 1.

## C2: downgraded
**For.** It is load-bearing: the sole source of the term −(θ/2)⁶⁶.

**Against:**
- Its logic is the Conlon–Lee–Sidorenko parity template: an odd total sign on a mod-2 closed structure, where every pair lies in exactly two faces.
- It is applied to C1's sign model, plus a routine opposite-bias mixture to cancel first moments.
- Support forcing is a short check specific to this complex.
- It is 8% of the Lean.

## C3: witness
I verified that V − E + F = 2 and that every vertex link is a cycle, so the complex is a triangulated 2-sphere. The paper never says so.

The object class is precedented: K₅,₅∖C₁₀, the canonical open case, is the Levi graph of the 5-triangle Möbius strip. So the witness is a close variant, judged against the problem as originally posed. It is single-use.

## Bridge novelty
| Import | Status |
|---|---|
| Symmetric-matrix association scheme over F_q → graph-density deficits | **New bridge** (first connection found) |
| Finite symplectic / Lagrangian geometry → singular-tail counting | New bridge, at tool level |
| Hypergraph parity obstruction → Levi graph | Known route conceptually (Sidorenko's Levi-graph positivity theorem; Möbius-strip K₅,₅∖C₁₀) |
| Gauss sums → independence of pair signs | Known route |
| WL → type pinning | Known route (WL ↔ homomorphism counts); new application |

The paper does **not** cite the hypergraph non-Sidorenko literature.

## Discoverability protocols (not run)
**Models.** Training cutoff before 2026-09-23, with a canary probe. AlphaEvolve and the Station contain no device, so models trained on them stay eligible. The producing OpenAI model is reference-only.

**Arms:**
- open;
- L (main);
- **L+hyper** (adds the loose triangle and the Conlon–Lee–Sidorenko criterion, to measure how much the hypergraph template lowers the jump);
- directed.

**Sampling:** n = 256 per arm; pass@k for k from 1 to 256.

**P-C1:**
- **Hide:** the rank-layer lemma and parity model, all of the transverse, orbits, planted and tail sections, and everything downstream.
- **Hit:** any nonnegative point–center kernel whose center integrals reproduce, at O(1) strength, a product of (1 + c·η_e·ξξ′) with asymptotically independent pair signs.

**P-C2:**
- **Give:** C1 and H.
- **Hit:** a per-corner coordinate and sign law with zero first moments, a signed overlap, an odd number of negative corners, and uniqueness of the identity labelling.
- **Expectation:** a high hit rate. A low rate would restore N3.

## Open questions
- **Expert check on C1 (the main risk).** Has a center or algebraic kernel been used before to emulate signed hypergraph correlations in graph densities?
- **Generality and reuse.** Does the lemma hold for any closed 3-uniform complex with every pair in two faces? Note:
  - K₅,₅∖C₁₀ is *not* covered, because the Möbius strip has boundary pairs.
  - Does the lemma need half rank exactly?
  - Lean states it only for Fin 13 × Fin 22, so a downstream Lean test needs a general restatement first.
- **Unverified quotes.** Verify every quoted passage against the PDFs (fetching was blocked in this session).
