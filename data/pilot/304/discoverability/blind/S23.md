# Proposal: the Iwasawa orientation module of the orbit space

## Setup
Let Γ = Z_p act faithfully on M^n. After passing to an open subgroup p^k Z_p (still ≅ Z_p, and still faithful), assume the action preserves orientation. Let π: M → X = M/Γ (a proper map), and let Λ = Z_p[[Γ]] ≅ Z_p[[T]], with γ = 1+T. Λ is a 2-dimensional regular local ring. Put ω_k = (1+T)^{p^k} − 1.

## Construction (the invariant)
Define the **Iwasawa sheaf** F = Rπ_* Z_p on X. Γ acts fibrewise, so F is a complex of sheaves of Λ-modules. At a point x with free orbit, the stalk is C(Γ, Z_p) ≅ Λ^∨ = Hom_cont(Λ, Z_p). Reducing mod ω_k gives the tower F ⊗^L_Λ Λ/ω_k ≅ Rπ_{k,*} Z_p for π_k: M → X_k = M/p^k Z_p. So the Yang/Bredon–Raymond–Williams tower X_{k+1} → X_k (deck group Z/p) is encoded by one Λ-object. The deck generator acts on F as multiplication by the unit γ^{p^k}, so it acts through the coefficients.

The **local orientation module** at x is O_x = H^{-n}(D_X F)_x, the costalk of the Verdier dual. Because π is proper, Verdier duality on M (ω_M = Z_p[n]) gives

  D_X(F) ≅ Rπ_* ω_M ≅ F[n],  Λ-linearly up to the involution γ ↦ γ^{-1}.

So O_x is a Λ-module. It equals Λ at a free orbit, and Λ/ω_k-type modules at orbits with stabilizer p^k Z_p.

## Key Lemma (dimension formula)
For every x ∈ X,

  cd_{Z_p}(X near x) = n + dim_Λ(O_x),

where dim_Λ is Krull dimension of the support. In particular, if O_x is Λ-torsion (dim ≤ 1) for all x, then cd X ≤ n+1.

*Sketch.* Locally, F is "an n-dimensional homology manifold with coefficients in Λ^∨". The self-duality above says F is a Λ-coefficient Poincaré complex of dimension n. The Čech/Leray spectral sequence for local cohomology of X with Z_p coefficients factors through RHom_Λ(Z_p, −) = derived Γ-invariants, which needs Λ-depth many extra degrees. Local duality over the regular local ring Λ adds exactly dim_Λ(O_x) to the top nonvanishing degree, because Ext^j_Λ(Z_p, Λ) is nonzero only for j = 2. This **recovers Yang's n+2 conceptually**: the "+2" is dim Λ = 2. Yang's theorem is then equivalent to: O_x has a rank-1 free (non-torsion) part somewhere.

## Contradiction strategy: the Λ-torsion lemma
**Lemma (needed).** For a continuous Z_p-action on a manifold, every O_x is Λ-torsion. More strongly, for each x there are a neighbourhood U and some k such that ω_k annihilates the image of H^n_c(π^{-1}U) → O_x.

Given this lemma, the Key Lemma gives cd X ≤ n+1, which contradicts Yang/BRW. So no faithful action exists.

*Proposed proof of the torsion lemma (Newman with Λ-coefficients).* Newman's argument for Z/p uses the fact that a cyclic group acting near x through small orbits must fix the local fundamental class. Then the transfer forces p·[M,x] = Σ g·[M,x] to be realised by a chain supported in an orbit-thin set, which is impossible. With Λ-coefficients:
1. Γ-equivariant Haar averaging yields arbitrarily small Γ-invariant neighbourhoods W = π^{-1}U. Use the semialgebraic/tame structure of a chart to make them finite CW-type modulo Γ-translates.
2. H^n_c(W; F_p) ⊗_Λ Λ/(p, ω_k) is finite for each k. Continuity of the action on this finite group forces p^{k'}Z_p to act trivially for some k' ≥ k.
3. Nakayama over the complete local ring Λ lifts "trivial mod (p, ω_k)" on the generators of O_x to "ω_{k'} · O_x ⊂ m·ω_k O_x", and hence to ω_{k'}-torsion of the image.

Newman's theorem is the obstruction to doing this naively: orbits of p^kZ_p are not uniformly small. The Λ-formalism avoids pointwise smallness. It only needs smallness in the m_Λ-adic topology, and continuity of the action gives that automatically, since γ^{p^k} → 1 in Λ.

## Why this is the right object
- It turns the infinite tower of non-manifold quotients into a **single finite-type duality statement** over a 2-dimensional regular ring.
- It isolates the whole conjecture in one algebraic dichotomy: the local orientation module is either *free of rank 1* (Yang) or *torsion* (Newman plus continuity).
- It is formalizable piece by piece. Verdier duality for proper maps, Iwasawa-module structure theory, and Krull dimension all exist in a Mathlib-style library.

**Honest caveat.** Step 3 is exactly where all previous approaches stall. It is the Λ-module version of the gap between Newman's theorem (finite groups) and Hilbert–Smith. I expect it to need a genuinely new input, such as a Λ-adic Smith inequality relating dim_{F_p} H^*(X_k) growth (in Iwasawa λ/μ-style form) to the local orientation module.
