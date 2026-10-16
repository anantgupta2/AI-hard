# Proposal: an isotypic Witt-class (local signature) of the orbit-space sheaf, with p-power divisibility

## Setup and reductions
- Replace M by M x R^j with Z_p acting trivially on R^j. Faithfulness is kept, so we may assume n = 4m. Work near a point.
- Write pi_k : M -> X_k = M/p^k Z_p and X = X_0 = M/Z_p. Every pi_k is proper, since the group is compact.
- By Newman and Baire, the free points are dense. Fix a free orbit O over xbar in X.

## Construction (the invariant)
Let F = R pi_* C_M on X. Its stalk at xbar is H^0(O; C) = C(O), the locally constant functions on O ≅ Z_p. The action of Z_p on F commutes with everything, so F splits over the finite-order characters chi in Q_p/Z_p:

  F = ⊕_chi L_chi,  where L_chi is the chi-isotypic summand, a sheaf in degree 0 with rank-one stalks.

Verdier duality and properness give D F = R pi_* D C_M = F ⊗ or[n]. Under this, D L_chi ≅ L_{chi-bar} ⊗ or[n]. Hence:
- L_1 = C_X is self-dual, so X is a C-homology n-manifold (consistent with Yang: the defect is integral, cd_Z = n+2).
- For chi ≠ 1, L_chi ⊕ L_{chi-bar} carries a symmetric (n = 4m) duality, hermitian after twisting.

So each block defines a class in Woolf's Witt group of self-dual complexes of sheaves, W(X; C). Apply the local-at-xbar functor, i.e. compactly supported hypercohomology over a small conic neighbourhood U of xbar relative to its link. This gives the **local isotypic signature**

  sigma_chi(xbar) = sign of the middle pairing on H^{2m}_c(U; L_chi) in W(C) ⊃ Z.

## Key lemma (p-power equidistribution)
For every k and every character chi of exact order dividing p^k, sigma_chi(xbar) = sigma_1(xbar). Consequently

  sigma_M(O) := local signature of C_M on pi^{-1}(U) = Σ_{chi in (Z/p^k)^dual} sigma_chi(xbar)

is p^k · sigma_1(xbar) on the level-k truncation, for every k.

*Sketch.* Over X_k, the map X_{k+1} -> X_k has deck group Z/p and is free over the free locus. Apply the finite-group fact (G-signature / Gilmer) in its sheaf-theoretic form. For a free Z/p^k action, the isotypic summands of a self-dual G-sheaf on the source have equal Witt classes. The reason is that they are all transfers of the same class along the free quotient: the pushed-forward pairing is the regular representation tensored with the form downstairs. The statement localizes over the conic neighbourhood U, which is legitimate because Woolf's Witt groups satisfy excision and the 12-term localization sequence (Balmer). Proper base change identifies the level-k pieces with the characters of Z/p^k factoring through Z_p. So the isotypic classes of F that factor through level k are permuted transitively by Galois action, and they are equal in W(C) ⊗ Q.

## Contradiction
1. **Normalisation.** Pick a small Euclidean chart V around a point y in O. Then sigma_M restricted to V is the local signature of R^n at a point, which is the generator 1 of L^0(pt) = Z (Ranicki–Weiss local L-orientation). Newman's theorem gives a neighbourhood U of xbar whose preimage contains, for each k, a p^k Z_p-orbit not contained in V. The preimage is a disjoint union of p^k translates of a fundamental domain W_k, and these are permuted freely by Z/p^k. By additivity of the Witt class under disjoint union, sigma_M(pi^{-1}U) = p^k · sigma(W_k).
2. **Integrality.** sigma_1(xbar) is the local signature of the self-dual sheaf C_X on a C-homology manifold. It is an integer, namely ±1 times the local degree of the C-orientation of X at xbar, so it is a fixed nonzero integer independent of k. The local L-class lifts because the Witt group of the stalk complex is W(C) ⊃ Z with no p-divisible part.
3. Combining step 1 with the lemma gives sigma_1(xbar) = sigma(W_k) for every k. Then sigma_M(pi^{-1}U) = p^k sigma_1(xbar) for every k, while the left side is a fixed finite integer computed in the compact window over U. Letting k -> infinity forces sigma_1(xbar) = 0. That contradicts step 2, since the local orientation class of the homology manifold X is nonzero. So no faithful action exists.

## Why this is the "most useful" device
It is a Witt class of R pi_* C_M taken character by character. It combines three things: rational homology-manifold duality on M/Z_p, which needs no integral manifold structure; the finite-group fact that free actions equidistribute signatures over isotypic parts; and an integral normalisation at a single point. Pardon's 3-manifold argument and Yang's n+2 dimension computation both show that the obstruction lives in an integral, p-local refinement. The isotypic Witt class is the natural carrier for it, and it is functorial under the tower X_{k+1} -> X_k.

**Main gap to close:** steps 2-3 need the local Witt class to be finitely generated and non-p-divisible at xbar. The proof relies on that integrality, so the integral-coefficients Witt group (Woolf, Hornbostel–Schlichting) must be used, not W(C).
