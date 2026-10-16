# Proposal: an Iwasawa μ-invariant for the tower M/p^kZ_p

**Caveat first.** The statement is the full Hilbert–Smith conjecture. As far as I know it is open for n ≥ 4: Pardon proved n ≤ 3, and the Lipschitz and Hölder cases are known through Repovš–Ščepin and Maleshich. What follows is one construction and the strategy it supports. Step 3 is the crux, and I do not have a proof of it.

## Setup: reduce to a free action
Each stabilizer is either 0 or some p^kZ_p. By Newman's theorem, Fix(p^kZ_p) is nowhere dense, since a periodic homeomorphism fixing an open set is the identity. By Baire, W = M \ ∪_k Fix(p^kZ_p) is therefore open, dense and Z_p-invariant, and Z_p acts freely on it. Write X = W/Z_p and W_k = W/p^kZ_p. Then W_k → X is a regular Z/p^k-cover with W = lim W_k. Set Λ = F_p[[Z_p]] = F_p[[T]], where T = γ − 1. This ring is a DVR.

## The invariant
Take a compact, Z_p-invariant, codimension-0 submanifold-with-boundary N ⊂ W. One exists: saturate a closed ball B ⊂ W to Z_p·B, then thicken it equivariantly. Define the **Iwasawa cohomology**

  H^i_Iw(N) = lim_k H^i(N/p^kZ_p ; F_p), with corestriction (transfer) as the transition maps.

By Shapiro's lemma this equals H^i(N/Z_p ; 𝓛), where 𝓛 = (Rπ_*F_p)^∨ is the "Iwasawa local system" of Λ-modules. X has F_p-cohomological dimension n (Bredon) and N/Z_p is compact, so RΓ(N/Z_p; 𝓛) is a perfect complex over Λ. By the structure theorem over a DVR, each H^i_Iw is Λ^{r_i} ⊕ ⊕_j Λ/T^{e_{ij}}. Define

  μ_i(N) = r_i, so that dim_{F_p} H^i(N/p^kZ_p ; F_p) = r_i·p^k + O(1).

This is the exact analogue of Iwasawa's μ-invariant for a Z_p-tower of number fields. Here the "class groups" are mod-p cohomology of the finite quotients.

## Lemma A (duality forces μ = 0)
**Claim.** If N is a compact topological n-manifold, then r_i = 0 for every i.

*Sketch.* By continuity of Čech cohomology, H^i(N; F_p) = colim_k H^i(N/p^kZ_p; F_p) under restriction. In Λ-terms, this colimit is RΓ ⊗^L_Λ Λ^∨, where Λ^∨ = C(Z_p, F_p). A free summand Λ^r contributes (Λ^∨)^r, which is infinite-dimensional. But H^*(N; F_p) is finite because N is a compact manifold. So r_i = 0 and H^*_Iw is Λ-torsion.

The same holds for H_c and ∂N. Verdier duality on N, pushed down to the quotient, gives a Λ-linear Poincaré duality: Rπ_*ω_N ≅ D(π_!F_p). Under this duality the torsion exponents satisfy e_{ij} ↔ e_{n−i,j} up to the involution T ↦ (1+T)^{−1} − 1.

## Lemma B (Newman forces μ > 0; this is the crux)
**Claim.** For x ∈ W and N an invariant neighbourhood of the orbit Z_p·x that is small enough, μ_1(N) ≥ 1 or μ_{n−1}(N) ≥ 1.

*Heuristic.* Newman's theorem gives a uniform ε. Every p^kZ_p has an orbit of diameter ≥ ε inside N, so each level of the tower N/p^{k+1} → N/p^k is "non-trivial at scale ε". Pick a small ball V around x. Then Z_p·V has p^{m(V)} components, with m(V) → ∞ as V → x, because the orbit is a Cantor set. Each new level of components gives a non-trivial loop (an H_1 class) in N/p^kZ_p: it closes in the quotient but not upstairs. The proposed counting lemma is that these loops are independent modulo transfers from lower levels. If so, dim H_1(N/p^k) grows like a constant times p^k, so r_1 ≥ 1. Dually, r_{n−1} ≥ 1 via the linking spheres around the Cantor orbit, using Alexander duality H^n_O(W) ≅ Ȟ^0(O)^∨ = Λ.

## Contradiction
Lemma A gives μ(N) = 0 and Lemma B gives μ(N) ≥ 1, which contradicts faithfulness. Here faithfulness is what makes W non-empty.

## Why this is the right object, and where it can fail
- **It recovers known results.** Over Z_p[[T]], which has dimension 2 rather than the DVR F_p[[T]], the Tor-amplitude jumps by 2. That reproduces Yang's dim_Z X = n + 2. Under a Lipschitz or Hölder hypothesis, Hausdorff-dimension growth bounds dim H(N/p^k) by o(p^k), so μ = 0 comes for free and the problem moves entirely into Lemma B.
- **It matches Pardon's case.** For n = 3, Pardon's argument with incompressible surfaces and mapping-class finiteness is in effect a proof of Lemma B in degree 1.
- **The gap.** Lemma B is the hard step. A wild free action could make the new loops at each level die under transfer, giving μ = 0 with all the growth in the torsion exponents e_{ij}. The missing ingredient is a lower bound linking Newman's ε to the growth of λ or μ. In the number-field analogy, that is a "Ferrero–Washington theorem in reverse".

**Proof-complexity note.** The construction is a single extension-variable–style device: a cheap tower invariant that turns an unbounded family of local Newman witnesses into one module-rank inequality.
