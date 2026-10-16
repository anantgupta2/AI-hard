# Proposal: the character-twisted Witt signature of the orbit tower

## Setup
Suppose Z_p acts faithfully on M. Put G_k = p^k Z_p, X_k = M/G_k and π_k : M → X_k, which is proper with Cantor-set or finite fibres. Let R = Q(ζ_{p^∞}). All coefficients have p invertible.

**Fact A (Haar averaging).** With Z[1/p] coefficients, Haar averaging over G_k gives transfers. So each X_k is a Z[1/p]-homology n-manifold, even though its integral cohomological dimension is n+2 (Yang, Bredon–Raymond–Williams). In particular D_{X_k} Q ≅ or_{X_k}[n].

## The construction
Let F_k = π_{k*} R_M. Because the fibres are profinite, the higher direct images vanish, so F_k is a sheaf. Its stalk at x is the smooth induced module C^∞(Z_p/Stab, R). This module splits over the finite-order characters χ : Z_p → μ_{p^∞}:

  F_0 = ⊕_χ L_χ,

where L_χ = j_{χ!} (rank-one local system). Here j_χ is the inclusion of the open set U_χ = {x : Stab_x ⊂ ker χ}, and the monodromy is χ.

**Lemma 1 (twisted Verdier self-duality).** Proper base change for π_0 and Verdier duality on M (Kashiwara–Schapira) give D(L_χ) ≅ L_{χ̄}[n] ⊗ or. So for n = 4m (after the stabilisation below), the pairing L_χ ⊗ L_{χ̄} → or[n] makes L_χ a Hermitian self-dual object. It therefore defines a class

  w_χ = [L_χ] ∈ W_c(X_0; R, ε),

using Woolf's Witt group of self-dual complexes of sheaves with compact support. Its image in W(R) ⊗ Q is a signature σ_χ ∈ Z.

**Lemma 2 (equidistribution of twisted signatures).** σ_χ is independent of χ. The proof is the G-signature/Gilmer argument for the free Z/p^k action on the generic stratum, run sheaf-theoretically:
- Group the characters by their kernel G_k. Then ⊕_{ker χ ⊇ G_k} L_χ = R q_* F_k, where q : X_k → X_0 has deck group Z/p^k.
- The isotypic parts of a self-dual sheaf pushed forward along a Z/p^k quotient have equal Witt classes, up to the classes supported on the branch set. The branch set is where the stabiliser is G_j with j < k, and it has smaller codimension rank in the stratified Witt group.
- An induction on k, using Balmer's localization sequence for triangular Witt groups (open U_χ versus closed branch locus) to strip the branch terms, gives σ_χ = σ_1.

**Lemma 3 (finiteness).** Let N be a closed simply-connected 4-manifold with σ(N) = 1, such as CP². Replace M by M × N, where Z_p acts on the first factor; the action is still faithful. Restrict to V = Z_p·B, where B is a small ball about a point with non-small orbits (Newman), so V is an invariant open manifold. Work with the compactly supported invariant on V/Z_p × N. Then

  Σ_{ker χ ⊇ G_k} σ_χ = σ_c(X_k^V × N) = σ_c(V^{G_k} quotient) ≤ dim H^{2m}_c(V × N; Q),

since H^*_c(X_k; Q) = H^*_c(V × N; Q)^{G_k} injects into H^*_c(V × N; Q). The right-hand side is finite: shrinking V to a regular invariant neighbourhood makes H_c finite-dimensional. This step uses the Ranicki–Weiss topological invariance to make the signature on V × N well defined.

## Contradiction
By Lemma 2, the left-hand side is p^k σ_1. By the Künneth formula for Witt classes, σ_1 = σ_c(X_0^V) · σ(N), and we arrange σ_c(X_0^V) ≠ 0 by choosing B so that V carries an invariant Witt class of rank 1. For instance, take the boundary-relative fundamental class of the cone over a link; Lemma 1 makes this possible because X_0 is a Q-homology manifold.

So p^k |σ_1| ≤ dim H^{2m}_c(V × N; Q) < ∞ for every k, which is impossible. Faithfulness is used exactly once: for every k, G_k ≠ G_{k+1} acts nontrivially, so L_χ ≠ 0 for characters of every order. A non-faithful action factors through some Z/p^K, and then the sum over χ stops at k = K.

## Why this invariant
The tower X_{k+1} → X_k has deck group Z/p, but it is not a cover, so the classical |G| divides σ statement cannot be applied directly. The twisted Witt classes L_χ make it apply anyway:
- they live on the Q-homology manifold X_0, where duality holds;
- they turn branched Z/p-covers into an equal-signature statement in a localization sequence.

The p-adic tower then forces the signature to be divisible by every power of p while staying bounded.

## Main gap to close
Lemma 2 at the branch strata needs the Balmer–Walter / Gersten–Witt filtration to kill the branch terms in W(R) ⊗ Q. Semialgebraic local triviality (Hardt) is not available for topological actions, so this must come from the Q-homology-manifold structure (Fact A) and Pardon-style local acyclicity of the orbit map.
