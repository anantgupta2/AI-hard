# Family 287: "An isomorphism of the free group factors" (paper analyst)

Source: `preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/build/` at commit fd4aeeb. Full item list: `paper.json` (43 items).

## Main statement and architecture
**Thm main** (main.tex:74): there exists a unital, normal, trace-preserving \*-isomorphism L(F₂) → L(F₃).

The constructive core is **Thm rank-step** (main.tex:64): L(F_n) ≅ L(F_{n+1}) for every n ≥ 3. The headline follows from N₃ ≅ N₄ ≅ N₅ by amplifying by √2 with Dykema's formula, which is cited and not re-proved. Rădulescu's dichotomy, also cited, then gives that all L(F_r), 1 < r ≤ ∞, are isomorphic, with fundamental group ℝ_{>0}. Transporting tuples answers Voiculescu's question negatively: none of δ, δ₀, δ\*, δ^⋆ is a W\*-invariant.

Labels:
- **A2**
- **B1**, flagged "full only with prior results" (Dykema, Rădulescu) and "adds corollaries"
- **C1** primary, with C2, C4 and C5 as secondaries
- not computer-assisted
- IH: "carry an extra tracked quantity" (the error budgets)
- **D3, provisional**

Proof chain, for M = L(F_{n+1}) = W\*(A₁…A_n, C):
1. Take S = arg C (bounded Borel logarithm). The conjugates S_g = A_g S A_g\*, g ∈ F_n, are free. The map s(k) = Σ k(g) S_g embeds ℓ²_ℝ(F_n) equivariantly, and ‖s(k)‖ ≤ 3π‖k‖₂ (Khintchine-type bound, re-proved).
2. **Cocycle flow.** Take the ODE A_j′ = i s_t(h_j) A_j. On the free formal algebra, τ∘ev₀∘δ = 0, proved by first variation plus freeness. Analyticity then gives moment invariance, so the flow consists of trace-preserving automorphisms β_t that fix S.
   - The word derivative is governed by the Fox cocycle: δa_g = iσ(D_g)a_g.
   - This gives the *exact* bound ‖β₁(A_w) − C A_w‖ ≤ 3π‖D_w − δ_e‖.
3. **Coefficient lemma.**
   - Build w_m = p_m x₁ from m free prefixes, so that D_{w_m} = T_m h with T_m = 1 + Σλ(p_j).
   - T_mT_m\*/m tends to the free Poisson law, which has no atom at 0.
   - A cutoff inverse then gives ‖h‖ < η and ‖D_w − δ_e‖ < η.
4. **Absorption.** Set α = γ⁻¹β₁, where γ is the Nielsen move C ↦ CA_w. Then α moves each A_j by less than ε, and α(A)_w is within ε of C.
5. Iterate with adaptive budgets. The A^{(k)} converge in norm to a free Haar n-tuple whose word algebra is L²-dense. The conditional expectation then shows that this tuple generates M.

## Strongest eureka-step candidates
**1. Prop. perturbation, the one-step absorption of a free generator (generation.tex:13). Provisional N3, F3 (with an F5 flavour).**
- *For:* a norm-small automorphism of L(F_{n+1}) under which a long word in the first n generators approximates the (n+1)-st is hard to imagine in advance. Nothing like it is in the goal or in L, and every stage of the limit depends on it. It turns the non-uniformity of deformations on long words, normally the *enemy* in Popa-style rigidity, into a constructive device.
- *Against:* the paper describes Shlyakhtenko's Sept 2026 preprint (arXiv 2609.11074) as using "finite automorphisms and a limiting generation argument". That preprint is after our knowledge cutoff and could not be checked. If it contains the same absorption idea, this item is N2.

**2. Small-cocycle lemma (cocycle.tex:31). Weak N3, F3.**
- *For:* this is where non-amenability enters. The lemma is impossible for ℤ (Dirichlet kernels) and for property-(T) groups (small cocycles are small coboundaries). It is the reduction of the absorption problem to a linear ℓ² problem in the group.
- *Against:* once the coefficient problem is posed, the solution is textbook: free CLT, Marchenko–Pastur and a spectral cutoff. The pivot is one step from L, and a judge may say N2.

**3. Cocycle-driven flow and word-displacement bound (Prop. flow, flow.tex:41). N2, leaning N3.**
- *For:* the bound is exact in operator norm, inside M, with no dilation. It avoids the naive product-of-exponentials error m·η² = O(1).
- *Against:* close neighbours exist:
  - Voiculescu's cyclomorphy (cited), for the exponentiation of trace-preserving fields.
  - Popa / Ioana–Peterson–Popa free malleable deformations, which use exactly C^t = e^{itS} for a free Haar C. This is the case h_j = δ_e.
  - Sinclair / Peterson–Sinclair Gaussian cocycle deformations α_t(u_g) = ω(t b(g)) u_g. The flow is their free, time-ordered analog.

  None of the last two is cited. This is a variant of a known tool, not a new one.

Also N2: the first-variation trace identity (flow.tex:116), a new proof of a cyclomorphy-type criterion, and the adaptive error-budget iteration (generation.tex:111), a standard diagonal construction whose named precedent is Shlyakhtenko 2026.

Free entropy, interpolated factors and Dykema–Rădulescu rescaling enter only as **cited transfer** (C5) or as corollaries. None is a eureka candidate. In the end, candidates 1–3 form a single idea: realize ℓ²(F_n) in M through the free complement, then use ℓ²-cohomology of F_n to absorb that complement. They should probably be scored as one cluster.

## Cross-field use
Problem field: operator algebras (46L10/46L36/46L54). Every cross-field ingredient is elementary and **re-proved inline**: Fox calculus and Nielsen moves, Catalan counts, moment determinacy, Picard iteration and analytic continuation, and free Khintchine bounds. The only invoked cited theorem from outside OA and free probability is the Borel functional calculus (Haase), so roughly 1/8 of the invoked citations are cross-field. L²-Betti numbers and free entropy are corollary-only. The essential role of β₁^{(2)}(F_n) > 0 is implicit and never stated. Model theory (Goldbring–Pi) and random matrices (the source of Rădulescu's dichotomy) are background or corollary-only.

## Correctness audit
I read every proof line by line and **found no gap**.

Checks passed: the cyclic rewrite in Lemma conjugates, the 3π constant, label preservation, the uniform analyticity radius, the exact displacement ODE, D_{w_m} = T_m h, the budget ordering and the √2 arithmetic. The most delicate point is that the formal algebra P has no relators. That is what lets the trace identity hold on all of P.

The argument also survives "proves too much" tests:
- **K-theory.** K₁(C\*_r F_n) = ℤⁿ distinguishes the reduced C\*-algebras. The flow lives on C\*(A, arg C), where C is null-homotopic, and generation happens only at the W\* level. The discontinuous logarithm is therefore *necessary*, and it is present.
- **Amenable and (T) groups.** For ℤ the coefficient lemma fails, and the same holds for (T) groups and for groups with relators.
- **Commutative Gaussian analog.** The Nielsen automorphism γ needs C to be free Haar. Otherwise the argument would contradict the absence of a Cartan subalgebra in L(F_n).

Residual concerns: the claim is extraordinary (it overturns the expected non-isomorphism and the W\*-invariance of δ₀); Shlyakhtenko 2026 cannot be verified here, including whether it is model-produced; the deformation/rigidity literature is uncited; δ₀ of semicirculars is sourced to an unusual 2023 paper; and δ\* = δ^⋆ for group generators needs checking against Mineyev–Shlyakhtenko Thm 4.1. Expert review and the Lean comparator status (other analyst) are needed before anything is treated as settled.

## Extraction friction
- The core machinery is defined in display math or prose, not in environments or `\emph`: s(k), D, the formal algebra P and derivation δ, the vector field V_j, w_m and T_m, the cutoff inverse R_m, the Nielsen move γ, and the budgets. The only `\emph` definitions are "normal", "free", "label" and "completion".
- Important sub-claims are unnumbered paragraphs inside proofs.
- The headline theorem is not the constructive theorem, so the comparator could target either.
- Useful cue phrases: "We prove the version needed here directly", "coefficient form of", "No result from that preprint is used".
- The provenance flag (prior model-produced work) cannot be resolved from the repo.
