# Proposal: a p-adic tower signature (Witt class of the pushed-forward self-dual sheaf)

## Setup
Suppose Z_p acts faithfully on M. Replace M by M x T^a, with the trivial action on the torus, so that n = 4m. For p = 2, also replace Z_2 by 2Z_2 so that the action preserves orientation (Z_p has no nontrivial map to Z/2 for p odd). Write X_k = M/p^k Z_p and X = X_0. The maps X_{k+1} -> X_k are free Z/p-covers (Bredon–Raymond–Williams). Write f_k : M -> X_k for the quotient maps.

## Construction (the invariant)
F_k := R f_{k*} Q_M[n] is a Verdier self-dual complex on X_k. The reason is that f_k is proper with compact fibres, so D Rf_* = Rf_! D = Rf_* D, and D Q_M[n] = Q_M[n] by orientation. Its Z_p-invariant summand is Q_{X_k}[n]. So X_k is a **rational** homology n-manifold, even though its integral cohomological dimension is n+2. By Woolf, Q_{X_k}[n] defines a class in the Witt group of self-dual sheaves, W(X_k; Q).

For a Z_p-invariant open U ⊂ M with compact closure, define

  σ_k(U) := signature of the intersection form on Im( H^{2m}_c(U/p^kZ_p; Q) -> H^{2m}(U/p^kZ_p; Q) ).

In Witt-group terms this is the pushforward to a point of the Witt class [Q_{U_k}[n]] with compact supports. The form is nondegenerate on the image by Verdier duality.

## Lemma (p-adic tower lemma)
(a) **Multiplicativity:** σ_{k+1}(U) = p · σ_k(U), hence σ_k(U) = p^k σ_0(U).
(b) **Boundedness:** |σ_k(U)| ≤ dim Im( H^{2m}_c(U;Q) -> H^{2m}(U;Q) ) < ∞, uniformly in k.
(c) Therefore σ_0(U) = 0, and likewise every σ_k(U) = 0, for every invariant U.

### Proof sketch
(a) This is the sheaf-theoretic form of the free-action fact quoted in the prompt. Decompose F_k over X_{k-1}... More cleanly, push forward along the Z/p-cover q : X_{k+1} -> X_k:

  q_* Q = ⊕_{χ ∈ (Z/p)^} L_χ,

where each L_χ is a rank-one local system. The decomposition is orthogonal for the hermitian duality (L_χ dual to L_{χ̄}). Gilmer's topological proof of the free G-signature identity is local: it compares the χ-isotypic Witt classes through a bordism/transfer argument. Running it in Woolf's W(X_k) for rational homology manifolds gives σ(X_k; L_χ) = σ(X_k; Q) for all χ. Summing over χ gives σ_{k+1} = p σ_k.

(b) H^*(U; Q) = H^*(U_0; f_* Q) = colim_k H^*(U_k; Q). The colimit is continuous because the fibre Z_p is profinite and the stalks are locally constant functions. Each map H^*(U_k) -> H^*(U) is injective, since averaging over Z/p^k is a rational transfer. It is compatible with cup products up to the factor p^k, and that factor does not change signs. So the form on U_k embeds, up to a positive scalar, into the form on U. Its rank, and hence its signature, is bounded by a constant independent of k.

(c) An integer of the form p^k σ_0 that stays bounded for all k must be 0.

## Contradiction with faithfulness
The vanishing in (c) holds for every invariant U, and also for every twist. Apply the lemma to Q-coefficients replaced by any self-dual local system pulled back from X, and to products with closed manifolds N with trivial action, for which σ is multiplicative. By the Ranicki–Weiss and Novikov description of L-classes as signatures of transverse inverse images, the result is: **all rational L-classes of X_k vanish in local (compactly supported) cohomology, and the local Witt class of Q_{X_k}[n] at every point is trivial in every tower degree**.

Now use Newman's theorem together with Yang's theorem. Faithfulness gives, for every k, a nontrivial Z/p-cover X_{k+1} -> X_k whose deck orbits are not small. Yang's theorem says the integral cohomological dimension jumps to n+2. That jump is carried by a nonzero p-torsion class in H^{n+1}_c(V; Z) for arbitrarily small V ⊂ X. Its Bockstein-paired linking form on the tower is the Z_(p) refinement of σ_k. The refinement is a class in the p-local Witt group W(Q_p)/W(Z_p) ≅ W(F_p), and it is still governed by (a) and (b). The decisive step: it cannot vanish, because a nonzero linking class is exactly what witnesses dimension n+2 rather than n. Its image under the tower transfer equals p^k times itself, while staying bounded in a fixed finite-dimensional receptacle H^{n+1}_c(V; Z/p). For p odd, multiplication by p on the relevant 2-primary Witt group is an isomorphism, so the contradiction has to be taken at the level of the **rank** of the image of H_c -> H. That rank grows like p^k by the cover count, but it is bounded by (b). Hence no such faithful action exists.

## Honest assessment
The new device is the bounded-versus-multiplicative tension of a Verdier-self-dual Witt invariant along the p-adic tower X_k. Parts (a), (b) and (c) are solid modulo writing Gilmer's argument in Woolf's sheaf Witt groups. The weak link is the nonvanishing step: turning Yang's "dimension n+2" torsion into a nonzero tower invariant whose growth contradicts (b). Rationally the quotient looks like a manifold, so everything rational vanishes harmlessly. A complete proof needs an integral or p-local self-dual refinement on which faithfulness forces genuine growth.
