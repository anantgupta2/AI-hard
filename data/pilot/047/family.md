# Family 047: Zariski cancellation and affine fibrations over ℂ

Manuscript: *An explicit failure of complex affine-space cancellation* (OpenAI, 23 Sep 2026). Source is `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/` at commit fd4aeeb: `main.tex` plus seven sections and an inline bibliography of 26 entries.

Lean: `lean/OAI/Algebra/AffineCancellation` (55 files, 783 declarations). The comparator is `ComparatorChallenges/ComplexCancellation.{json,lean}`.

Full data: `family.json` (36 paper items, 15 Lean item groups). The sympy checks of every displayed identity are in `check047.py` and `check047b.py`.

Base library L = Mathlib d13f23b + the paper's 26 references.

## 1. Main statement

The witness is (01-introduction.tex:48-70):

- P = ℂ[p,s,u,F,J]
- x = s²+u³+p²F
- H = x²F − (1+2sx)J − p²J² − pu
- A = P/(H)

**Thm main.** A is an integral complex algebra of dimension 4, A[w] ≅ ℂ^[5], and A ≇ ℂ^[4]. So Zariski cancellation fails over ℂ in dimension 4.

Paraphrase: an explicit hypersurface X ⊂ 𝔸⁵ has X × 𝔸¹ ≅ 𝔸⁵ but X ≇ 𝔸⁴. This would be the first characteristic-zero counterexample in any dimension ≥ 3. A quick search finds only "potential" counterexamples in the literature (Dubouloz–Ghosh 2025).

The paper also claims two corollaries; neither is formalized:

- **Cor stable-coordinate:** H is a coordinate of P[w] but not of P, so the Stable Coordinate Conjecture fails in ambient dimension 5.
- **Cor affine-fibrations:** p: X → 𝔸¹ and (p,H): 𝔸⁵ → 𝔸² are smooth 𝔸³-fibrations, with every residue-field fiber 𝔸³, but are not Zariski-locally trivial. So Dolgachev–Weisfeiler fails in relative dimension 3.

**Comparator.** `MainStatement` is
`Algebra.FiniteType ℂ A ∧ IsDomain A ∧ ringKrullDim A = 4 ∧ Nonempty (Polynomial A ≃ₐ[ℂ] MvPolynomial (Fin 5) ℂ) ∧ ¬ Nonempty (A ≃ₐ[ℂ] MvPolynomial (Fin 4) ℂ)`.
It uses the same H, with p,s,u,F,J = X0..X4.

- **Match: exact.** All of Thm main is formalized. `lean/docs/047.md` states that the corollaries are excluded.
- **Trust surface: clean.**
  - 0 each of `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `set_option`.
  - 4 trivial `decide` uses on Nat literals.
  - `Classical.choose` appears only in standard noncomputable definitions.
  - A single `import Mathlib`.
  - The Lean was not built here; trust rests on the comparator pass.

## 2. Labels

| Axis | Label | Evidence | Confidence |
|---|---|---|---|
| A | **A2** (counterexample). The hard conjunct is A5-like (¬∃ iso) | "Consequently the Zariski cancellation problem ... has a negative answer in dimension four" (01:68-69) | high |
| B | **B2** (refutes). Flag *adds corollaries* (SCC, Dolgachev–Weisfeiler). *Full only with prior results*: no for Thm main; yes for the corollaries | 01:42-43 | high |
| C | **C1** primary (explicit witness and explicit cylinder iso). Secondaries: C3 (non-polynomiality by contradiction, ~82% of the Lean DAG), C5 (corollary-only: BCW, Suslin, Dutta–Lahiri), C4 (minor abc degree chain) | "We retain the explicit formulas so that the resulting isomorphism is available without an existence argument" (02:15-16) | high (C1 vs C3 is arguable) |
| computer-assisted | **no** | Every identity has a hand-checkable certificate. Lean closes them with `ring`/`linear_combination`, with no search | high |
| C2 flags | ih_strengthened **no**; template n/a | Only local well-founded descents: weight reduction (03:226) and LND order (05:192) | high |
| D | **D3, provisional** | Driven by the witness H (I01, N3/F3). Every proof lemma is N2 or below | low-medium |
| provenance | builds on a prior model-produced result: **no** | The only 2026 citation is Gaifullin–Petrov (human authors, cited for the open status) | medium-high |

**E (fields).**

- **Problem field:** Algebraic and complex geometry. MSC 14R10, 14R25, 14R20, 13B25.
- **Lean-dir field:** Algebra. The formalization is pure commutative algebra.

Method fields:

| Field | Tag |
|---|---|
| Commutative algebra: polynomial rings, residual coordinates | essential |
| LND / G_a-action theory | essential |
| Graded and filtered algebra, valuations, affine modifications | essential |
| Algebraic groups (SL₂ → SL₂/T) | essential |
| Picard groups and linearization (Traverso, Brion; re-proved) | essential in the paper only; the Lean bypasses it |
| Function-field abc (Mason–Stothers) | essential |
| sl₂ highest-weight theory | essential in the Lean only |
| K-theory (Quillen–Suslin, BCW) | corollary-only |
| Coordinate theory (Dutta–Lahiri, Edo–Vénéreau, Maubach) | corollary-only or alternative route |
| Characteristic-p cancellation (Asanuma, Gupta) | background-cited |

Cross-field essential count: 3 (4 counting the Lean's sl₂ argument).

## 3. Proof architecture

**Paper route:**
1. **Construction.** The identity xy − z(z+1) = p²(H+pu) gives A[p⁻¹] = ℂ[p^±,x,y,z]. A is a domain of dimension 4.
2. **Stabilization.** Δ = −p²∂/∂u is an LND of P with ΔH = p³.
   - exp(wΔ) gives A[w] ≅ P[w]/(H+p³w).
   - A determinant-1 change (L,M), a root L* mod p³ and the certificate e₀ then give T = ℂ[p,s,u,M,e].
   - This makes the El Kahoui–Ouali method explicit.
3. **Degeneration.** Take ord_p from S = ℂ[p,x,y,z,u]/(xy−z(z+1)−p³u). Then gr A = G = R[τ, I/τ²] = P/(H_top) exactly, where R is the quadric × 𝔸¹ and I = (f,g).
4. **Positive invariant.** If A = ℂ^[4], some coordinate has positive degree. ∂/∂q_i then gives a homogeneous LND D₀ on G that kills a positive-degree element.
5. **Principalization.** Pull back along SL₂ → SL₂/T, where R̃ = ℂ[a,d,b,c,u]/(ac−bd−1).
   - The certificate is f = C₁v, g = b²v, αC₁ + βb² = 1, so IR̃ = (v) with v = a³b − a²u³ − d².
   - Then G̃ = R̃[τ,V]/(τ²V−v), carrying a valuation degree and a fiber weight.
6. **Lift.** Pic(𝔸¹×X) = Pic(X) and the normalized linearization give a unique lift D̃. Conjugating by degree scaling shows D̃ is homogeneous.
7. **Extraction.** V divides the positive-degree invariant, so D̃V = 0. Splitting on whether D̃τ = 0 gives an LND E on R̃ with fiber shift q ≤ 0 and E²(v) = 0.
8. **Rigidity.**
   - Use the auxiliary grading (a,d,b,c,u) = (0,3,−3,0,2). Its top component E′ satisfies (E′)²(d²+a²u³) = 0.
   - Mason–Stothers on the orbit polynomials, plus the fact that −u³ is not a square in ℂ(a,d,b)(u), forces E′ to fix a, d and u.
   - Then h = cE′(b) − bE′(c) lies in ℂ[a,d,u] with fiber weight e−2 < 0, a contradiction.

**Lean route.** It differs from the paper in six places; the last two are minor:
- **Domain and dimension** come from the cylinder isomorphism itself.
- **Degeneration** uses the Rees algebra B ⊂ A[T^±] with B/qB ≅ G, not the valuation.
- **The positive invariant** comes with a *possibly non-homogeneous* LND on G.
- **The lift** avoids Picard groups entirely:
  - the rational slice theorem gives G ↪ F[t] with D ↦ d/dt;
  - a Bézout SL₂-frame over the Euclidean ring F[t] trivializes the torsor;
  - a replica cD clears denominators;
  - taking the highest valuation component on G̃ restores homogeneity.
- **The last step of rigidity** writes E′ = h·δ and uses that an sl₂ highest-weight vector of negative weight is zero.
- **Mason–Stothers** comes from Mathlib (`Polynomial.abc`).

Dominated shares of the target DAG:

| Lean declaration | Dominated share |
|---|---|
| nonpolynomiality | 0.82 |
| exists_equivariant_lift | 0.20 |
| positive_invariant_of_polynomial | 0.13 |
| no_positive_invariant | 0.13 |
| rigidity | 0.07 |
| cylinder iso | 0.055 |

The 20% dag_share proxy again selects only carriers: G, AffineModification.T, v, LocallyNilpotent and Torsor.Frame.

## 4. Eureka candidates

1. **I01, the witness polynomial H. Provisional N3, F3.**
   - *For:*
     - It settles a long-open characteristic-0 problem.
     - It is tiny, and it is not a subterm of the posed problem or of L.
     - It must satisfy two opposing constraints at once: it is a residual coordinate (so the cylinder is trivial), yet its degeneration principalizes to v with the −u³ nonsquare.
     - Once H is fixed, the rest is variants of known technique.
   - *Against:*
     - It is the witness of an A2 claim, so it appears in the formal goal; test 2 must be judged against the posed problem.
     - It may be templated: an Asanuma/Danielewski-type twist p³u = Q of the SL₂/T quadric, made into a residual coordinate.
   - *Nearest neighbours:*
     - Gupta's x^m y = F(x,z,t), which works in characteristic p only;
     - Vénéreau-type residual coordinates, whose coordinate status is open;
     - Dubouloz–Ghosh 2025, potential counterexamples only.
2. **I20, principalization through the SL₂ torus bundle (with the lift I22). Provisional N2, F5.** It turns the obstruction into a single-relation ring.
   - *Against:* torsor pullbacks and Brion linearization are known. The Lean also found an alternative elementary route.
3. **I25, the extraction lemma (E²v = 0, q ≤ 0). Provisional N2.** It is a new statement, but one step from I20/I24 by standard LND-order bookkeeping. The sign condition works like a tracked extra quantity.
4. **I29 + I31 + I33, weighted rigidity. Provisional N2, F3.** The auxiliary grading (0,3,−3,0,2) and the abc-plus-nonsquare argument. The paper names Finston–Maubach as precedent.
5. **I16, the positive-degree invariant obstruction. Provisional N2.** The paper names Gupta's Derksen-invariant strategy as its precedent.

## 5. Correctness and trust

- **Algebra re-checked.** Every displayed polynomial identity was re-verified with sympy:
  - the defining identity;
  - Δ and ΔH = p³;
  - the (L,M) inverse;
  - the H(L) expansion and C;
  - the root mod p³ and the e₀ certificate;
  - the principalization certificate and α C₁ + β b² = 1;
  - E₊ and the auxiliary degrees.
- **Logic.** The logical chain was read line by line, and no gap was found. One observation: the rigidity proposition actually holds for fiber shift e ≤ 1, which is stronger than the paper needs.
- **Main concern.** This is an extraordinary, unreviewed claim. The strongest evidence is the exact-match Lean proof with a clean trust surface, but the comparator was not re-run here.
- **Corollaries.** The SCC and Dolgachev–Weisfeiler corollaries are unformalized. They rest on cited theorems (Dutta–Lahiri Thm 3.4, Bass–Connell–Wright, Suslin) whose hypotheses appear to hold.
- **Section 4.** The paper's Picard/linearization section is compressed. The Lean does not depend on it.

## 6. Extraction friction

- **Hidden definitions.** Nearly all load-bearing objects are display-math definitions: x,y,z, Δ, L,M, C,Q₁,L*,e₀, S,R, f,g,I, R̃, v, α,β,C₁, G̃,V, N, E′, h. Only five inline `\emph` definitions exist.
- **Sub-lemmas inside proofs.** Some load-bearing facts sit inside proofs, such as the homogeneous pieces of G̃ and R̃ ∩ ℚ = ℂ[a,d,u].
- **Paper–Lean join.** The Lean route diverges in four substantive places, so a join by name or docstring fails. The join was done by hand (L04–L13).
- **Naming.** The namespace is `OAI.ComplexCancellation`, not the family id.
- **Load-bearing proxy.** The extractor's proxy over-weights carriers; the dominated share is more informative.
- **Bibliography.** There is no `references.bib`; the bibliography is inline.

## Quick literature-check sources
[Dubouloz–Ghosh 2501.09613](https://arxiv.org/pdf/2501.09613) · [Bell–Zhang survey 1601.04625](https://arxiv.org/pdf/1601.04625) · [A¹-contractibility survey 1903.07851](https://arxiv.org/pdf/1903.07851) · [Lewis, strongly residual coordinates 1304.1765](https://arxiv.org/pdf/1304.1765) · [Vénéreau-type polynomials](https://ar5iv.labs.arxiv.org/html/1007.2230) · [Finston–Maubach 0706.4184](https://ar5iv.arxiv.org/html/0706.4184) · [Brion, linearization 1312.6267](https://arxiv.org/pdf/1312.6267) · [Gaifullin–Petrov 2607.13593](https://arxiv.org/pdf/2607.13593) · [Gupta 1208.0483](https://arxiv.org/pdf/1208.0483) · [Gupta 1309.1368](https://arxiv.org/pdf/1309.1368)
