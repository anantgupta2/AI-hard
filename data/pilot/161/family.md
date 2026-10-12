# Family 161: Counterexamples to Sidorenko's conjecture and the forcing conjecture

This is the FAMILY analysis of the paper and the Lean, done at text level. This agent did not build the Lean (no `lake build`, `lake env` or `comparator`, because the checkout is shared); the orchestrator compiles the comparator. The extractor did run: `scripts/extract_lean.py 161` (v3) wrote `data/items/161_lean.json`.

- **Corpus:** `openai/math` at fd4aeeb.
- **Manuscript:** `preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/build/`, with 8 sections and 2 figure files (3,920 TeX lines).
- **Reasoning trace:** none.
- **Machine-readable version:** `family.json` (43 items).
- **Counterexample rule:** the witness H appears in the formal goal, so per the codebook its novelty is judged against the problem *as originally posed* (Sidorenko 1986/1991: every bipartite H), before the witness was known.

## 1. Main statement
- **Paper** (`sections/introduction.tex:18-26`). Let H be the incidence graph of the 22 triples on 13 points in Table 1 (35 vertices, 66 edges). There is a finite simple G with an edge and **t(H,G) < p(G)^66**. Here t counts *all* homomorphisms, including noninjective ones. This refutes Sidorenko's conjecture.
- **Corollaries** (not formalized):
  - (i) t(H,F) < c·p(F)^66 for every c > 0, via categorical powers.
  - (ii) A fixed deficit in injective copies at one positive limiting density, via blow-ups. This contradicts the injective Erdős–Simonovits benchmark.
  - (iii) A nonconstant graphon W with t(K₂,W) = p and t(H,W) = p^66. So H is not p-forcing, which refutes the forcing conjecture (Skokan–Thoma; Conlon–Fox–Sudakov Conj. 2).
- **Comparator.** `ComparatorChallenges/SidorenkoCounterexample.lean` states `OAI.SidorenkoCounterexample.main : ∃ size, 0 < size ∧ ∃ host : SimpleGraph (Fin size), (∃ u v, host.Adj u v) ∧ homDensity H host < (edgeDensity host)^66`.
  - Solution module: `OAI.Combinatorics.Sidorenko.RandomHost`.
  - Permitted axioms: propext, Quot.sound, Classical.choice.
- **Match check: exact.**
  - The 22 `faces` agree with Table 1 row by row.
  - `homDensity` = Nat.card of all edge-preserving maps divided by n^35.
  - `edgeDensity` = 2|E|/n².
  - The challenge's local definitions are textually identical to `Sidorenko/Basic.lean:7-32` up to binder names. `definition_names` is empty, so the orchestrator should confirm that the comparator matches these constants.
  - H is bipartite by construction.
- **Explicitness.** H is explicit. G is only shown to exist: it is a random sample from a finite kernel whose parameters D, θ, ρ, ε and q are fixed by limits. In Lean the dimension threshold is `Classical.choose` with D₀ ≥ 1642. Calling the result "constructive" (as Wikipedia does) overstates it.

## 2. Trust surface (text-level grep over all 35 files, 23,761 lines, 2,280 declarations)
- None of the following appear: `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `ofReduceBool`, `partial def`. No `set_option` appears at all, so there are no heartbeat raises.
- The 2 "admit" hits and the 1 "axiom" hit are docstring English (Orbits.lean:496, Reduction.lean:276-277).
- `decide` is used 541 times, including 282 `decide +kernel` in Refinement.lean. All are kernel-checked finite certificates on the 35-vertex complex: pair tables, colour-refinement rounds, exposure orders, and `degree_choose_sum = 618`.
- The only imports are Mathlib and the family's own files, in a linear chain.
- **Compile status: pending (orchestrator).**

## 3. Labels
| Axis | Label | Conf. | Evidence |
|---|---|---|---|
| A | **A2**: existential counterexample (H explicit, G exists). No explicit rate | 0.95 | intro.tex:21-25 |
| B | **B2**: refutes Sidorenko. The flag *adds corollaries for other conjectures* is set: forcing conjecture, injective supersaturation benchmark, unbounded ratio. Not "full only with prior" | 0.9 (conditional on correctness) | intro.tex:11-16 |
| C | **C1** primary: kernel construction, then sampling. Secondaries: C4 (q-asymptotic estimation chain), C3 (G exists by sampling plus convexity; parameters fixed by limits), C2 (exposure orders and face-distance induction only) | 0.85 / 0.7 | intro.tex:28-31 |
| C2 flags | ih_strengthened = **no**. The only induction is on face-graph distance (tail.tex:409-422), with the hypothesis used as stated | 0.8 | |
| C5 | Not really used: every external tool is re-derived in the text | | |
| Computer-assisted | **no**. Only finite certificate checks, which are hand-checkable and which I re-verified in Python. The complex was very likely found by computer search, but the paper does not say so and no search is part of the proof | 0.85 | complex.tex:168-201 |
| D | **D3 (provisional)**. It rests on I07+I08, the rank-layer sign model (N3 candidate), and on I15, the activation gadget (N3 candidate) | 0.5 | intro.tex:84-89 |
| Provenance | **no**. Both 2026 citations are human-authored: imliliu2026 (CPC) and zhao2026 (arXiv:2606.15368, which discloses ChatGPT for language polishing only). Both are background-cited | 0.8 | |

**E. Fields.**
- **Problem field:** Combinatorics (MSC 05C35, 05C60, 05C80; graph limits).
- **Lean dir:** Combinatorics.
- **Method fields:**
  - quadratic forms over F_q and the symmetric-matrix association scheme (essential);
  - finite symplectic geometry: Lagrangian counts, reduction, triple orbits (essential);
  - character sums: quadratic Gauss sums, Fourier analysis on F_q^s (essential);
  - probability: sampling, total variation, planted change of measure (essential);
  - colour refinement / WL (essential, for pinning);
  - graph limits (home-field infrastructure);
  - elementary quadratic optimisation (routine);
  - graph norms, entropy, local Sidorenko (background-cited only).
- **Cross-field count:** 5. About 0.75 of the invoked external results come from outside combinatorics, and all are re-derived.
- **Unused neighbour:** the complex is a triangulated 2-sphere, but the paper never uses or says this.

## 4. Proof architecture
1. **The witness complex** (complex.tex):
   - Each of the 33 pairs lies in exactly two faces.
   - The face graph is connected.
   - Three bit positions define six classes of 11 faces each. Every class is a spanning growth sequence: each new face shares a pair with an earlier face and adds exactly one new point.
   - The separation is a_e ≥ 1/3 for every pair, and some pair has a_e > 1/3.
   - Colour refinement of H is discrete.
2. **The rank-layer lemma** (kernel.tex:31-49). Take the signed half-rank kernels K_ξ(Z) = 1{rank Z = r, sign Z = ξ}/P(·) on random symmetric D×D matrices over F_q. Products of these over the incidences converge to the sign model ∏_j ∏_{pairs ⊂ j}(1 + c₀η_eξξ), where the η_e are independent uniform signs. Averaging over η turns this into a parity test of the four incidence signs around each fully active pair.
3. **The typed activation kernel** W_q. Vertex types say which point or face a vertex is meant to represent, and there is one independent matrix coordinate per corner. Every first moment is forced to vanish. The coordinate expansion is then t(W_q) = 1 + Σ_types weight·C(a,b) + o(1), summed over all-nonempty labels only.
4. **The two-branch base law.** At each corner the law uses S = M_κ or S = Γ_κ, with opposite sign biases, and one corner sign is negative. Support forcing (∩_{κ∈U_g} M_κ = U_g) leaves the identity type assignment with a single term, equal to −(θ/2)^66.
5. **From one negative term to a finite host.**
   - Pinning: colour-refinement scores make the identity the unique maximizer, and Gibbs priors plus thinning with large ρ give t₀ < 0.
   - Dilution: the controlled orientation carries ε^13 and the uncontrolled transpose carries ε^22, so the negative term wins.
   - Crossed product: V((x,y),(x′,y′)) = W(x,y′)W(x′,y) gives a symmetric [0,1] kernel with t(H,U) < μ^66.
   - Sampling then gives a finite host.
6. **Transverse part of the rank-layer lemma.**
   - At half rank, a common center forces complementary images, so χ(det B) = c₀ξ₁ξ₂.
   - Centers are counted through maximal isotropic subspaces of L = B₀⁻¹ − B₁⁻¹.
   - Restriction signs concentrate at 1/2.
   - The 33 pair signs are asymptotically independent, by Schur complements and Gauss sums (D ≥ 12).
7. **Singular part, local.**
   - Symmetric matrices become graph Lagrangians, and rank defects become intersection dimensions.
   - Each ordered triple orbit has mass ≍ q^{−C}.
   - The planted-law density ratio bounds every face factor by q^g.
8. **Singular part, global.**
   - The profile cost comes from exposing the six bit classes and taking a geometric mean.
   - The total slack splits as Σ S_j plus the separation surplus.
   - Coercivity (Q ≥ (P²+T²+δ²)/342) bounds the pair dimensions. Propagation over the face graph, together with one pair with a_e > 1/3, makes the bound uniform.
   - Choosing D large forces c = 0 and h_e ∈ {0, 2}. Span counts then give strict decay (D > 1641).
9. **Corollaries:** tensor powers, blow-ups, and interpolation to an exact graphon equality.

## 5. Lean structure
**Size:** 35 files, 23,761 lines, 2,280 declarations (1,727 theorems, 442 defs). The extracted proof DAG has 1,600 declarations.

**Branch split by lines:**

| Branch | Lines | Share |
|---|---|---|
| Singular tail and Lagrangian geometry | 13.5k | 57% |
| Transverse part, joint signs, chart comparison | 6.4k | 27% |
| Combinatorial construction, pinning, symmetrization, host | 3.8k | 16% |

So the rank-layer lemma, the analytic engine, is about **84%** of the code. There is no implementation layer of the kind seen in 103 or 112.

**Dominated shares** (from the extractor):

| Declaration | Dominated share | Note |
|---|---|---|
| `exists_symmetric_kernel` | 0.94 | |
| `typedMatrixKernel_tendsto` | 0.44 | Rank-layer branch; under-estimate |
| `exists_negative_coefficient` | 0.33 | Includes `pinning_complex` at 0.21, mostly certificate tables |
| `configuration_bool_tendsto` | 0.28 | |
| `basePairLaw_identity` | 0.05 | Activation gadget |
| `identity_activeCoefficient` | 0.05 | Activation gadget |
| `corner_support` | 0.04 | Activation gadget |

The activation gadget is 8% of the lines.

**Extractor caveat.** The extractor misses `have h := lemma …` links made inside tactic proofs. For example, `tripleFaceDensity_tail_bound`, `directPairProfile_card_bound` and `indexed_strict_span` are all used, yet show in_proof_dag = False. As a result:
- Planted.lean, Exposure.lean, Spans.lean and Nullity.lean are badly under-counted.
- Singular-tail DAG shares are lower bounds.

**Route differences from the paper (minor):**
- Lean pinning combines refinement rounds by a small score perturbation, where the paper uses lexicographic weights L₀^{R−t}.
- Lean certifies refinement directly on H with 4 rounds of tables.
- Lean fixes the dimension as 2·(2r) with r = `singularTailThreshold` ≥ 1642.

## 6. Items (43; full list in family.json)

**N0 (standard or transfer):**
- I01: densities;
- I06: discriminant sign;
- I10: bipartite density;
- I20: crossed-product symmetrization;
- I21: finite-host sampling (Lovász–Szegedy);
- I22, I23, I29, I30: Grassmann, split-form and Lagrangian counts, and the graph-Lagrangian chart;
- I42: amplification.

**N1:**
- I05: finite certificates;
- I09: parity identity;
- I13–I14: coefficient and expansion;
- I18: Gibbs tilting;
- I24–I28: restriction signs, complementary images, local transverse limit, Gauss-sum joint signs;
- I31–I34: orbit masses, planted law, gains;
- I36, I37, I39–I41: slack, coercivity, spans, residual counts;
- I43: forcing corollary.

**N2:**
- I03: the witness;
- I04: bit labels and separation;
- I11–I12: typed kernel and zero-moment design;
- I16: support forcing;
- I17: colour-refinement pinning;
- I19: dilution asymmetry;
- I35: six-class exposure cost;
- I38: propagation and choice of D.

**N3 candidates:**
- I07+I08: the rank-layer kernel and sign model;
- I15: the two-branch activation law.

## 7. Eureka candidates (provisional; full grading belongs in novelty.md)

### 1. I07+I08 (+I25): the signed half-rank layer kernel and the rank-layer sign model. N3 candidate, F5/F3
- **For:**
  - It occurs neither in the goal nor in L.
  - It is the mechanism that makes the counterexample possible. A common center at half rank forces complementary images, so a 3-incidence face becomes a multiplicative constraint on three pair determinant signs, and those signs are asymptotically independent.
  - In effect it simulates the kind of 3-wise parity obstruction that breaks *hypergraph* Sidorenko (the loose triangle), but inside an ordinary bipartite homomorphism density.
  - It is syntactically tiny (an indicator of a rank/sign layer) and carries about 84% of the formal proof.
- **Against:**
  - The relation is a class of the Huo–Wan association scheme, which the paper cites.
  - The geometry is textbook (Taylor) and the independence is a Gauss-sum computation.
  - Quadratic-character hosts (Paley graphs, norm graphs) are classical in extremal graph theory.
  - A strict judge may call this a *new bridge* rather than a jump.
- **Literature check:** 4 WebSearch queries found no use of rank-layer or Lagrangian kernels for engineering signs in homomorphism densities (snippet level).

### 2. I15+I16: the two-branch activation law (M_κ vs Γ_κ) with support forcing. N3 candidate, F3
- **For:**
  - It cancels every first moment yet keeps one signed overlap moment.
  - This yields a unique global term −(θ/2)^66, the sole source of negativity in the proof.
- **Against:**
  - Mixing branches to kill first moments is a routine design move.
  - It is short (8% of the Lean) and specific to the complex, so it is likely a one-off device.
- **Nearest neighbours:** local Sidorenko second-order analysis (Lovász 2011); sign perturbations in work on common and step-Sidorenko graphs.

### 3. I03: the witness H. N2
- **What it is:** analyst observation, not stated in the paper. V − E + F = 13 − 33 + 22 = 2 and every vertex link is a cycle, so the complex is a 13-vertex triangulation of the 2-sphere. H is its Levi (vertex–face incidence) graph, which belongs to a classical class.
- **For:** judged against the problem as posed, the witness is not a subterm. No prior proposal of such candidates was found; the usual small open case is K_{5,5}∖C_10. It escapes every known positive criterion.
- **Against:** its properties are exactly the constraints the proof generates, so it was probably found by search downstream of candidates 1 and 2. A single witness cannot be reused downstream.

### 4. I17+I18: colour-refinement pinning with Gibbs tilting. N2
The paper itself says it "adapts" WL. The sum-of-squares round score is a neat touch.

### 5. I35+I36+I38: six-class exposure with geometric mean, separation surplus, and propagation. N2
This is Shearer- or Hölder-type fractional covering with a bespoke bit labelling.

## 8. Correctness and trust concerns
**What I checked.**
- Prop. complex, all four parts, in Python:
  - 33 pairs, each in exactly two faces;
  - connected face graph;
  - six classes, each with a growth order;
  - min a_e = 1/3, with 5 pairs above it;
  - colour refinement discrete after 4 rounds.
- The support identity and |M_κ| = 7, by computation.
- By hand:
  - base-law moments;
  - the per-corner factor in the expansion;
  - χ(det L) = η₁₂η₁₃η₂₃;
  - the Gauss-sum TV bound.
- With sympy:
  - the normalisation exponents;
  - the common-space gain g_C;
  - the full slack identity (eq:slack);
  - the coercivity endpoint values and the constant 1/342.
- The constants 618 and 1641.
- The comparator against the table and against Basic.lean.

**Concerns.**
- **This is an extraordinary, unreviewed claim.** It refutes a 1986/1991 conjecture. Searches on 2026-10-12 show only Wikipedia relaying OpenAI's claim.
- **The singular-tail exponent bookkeeping is intricate.** It is spot-checked, not fully audited by hand. The paper uses only necessary constraints on local maximizing tuples, which is valid for an upper bound.
- **Calling the counterexample "constructive" is inaccurate.** The host is not explicit and the dimension D is enormous.
- **The corollaries are not formalized.** They are short and standard.
- **Comparator constant matching.** `definition_names: []` means the orchestrator should check how the comparator matches the challenge-file definitions; they are textually identical to Basic.lean.
- **Bottom line:** if the Lean compiles with only the three permitted axioms, Theorem 1 is certified independently of the prose.

## 9. Extraction friction
- **Inline definitions.** Most definitions are inline `\emph`, and the key activation law is defined in a bulleted list, not a definition environment.
- **Unstated structure.** The paper never says the complex is a sphere triangulation.
- **Extractor gaps.** The extractor under-links tactic-internal uses, and 316 certificate lemmas inflate declaration counts. I therefore also report shares by file lines.
- **Easy join.** Lean names are descriptive and match paper sections, so joining paper items to Lean declarations was easy.
- **No trace.** There is no reasoning trace, so the search for the complex is invisible.
