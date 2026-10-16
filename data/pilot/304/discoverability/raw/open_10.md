# Proposal: the Iwasawa–Witt class of the orbit space

**Idea.** Rationally nothing goes wrong. X = M/Z_p is a Q-homology n-manifold, and the pathology (dim_Z X = n+2) is purely p-adic. So the invariant should combine the *whole tower* M -> X_k = M/p^kZ_p -> X into one self-dual sheaf over the Iwasawa algebra Λ = Z_p[[Z_p]] ≅ Z_p[[T]]. Its Witt class then has to satisfy two incompatible constraints: a "manifold" constraint coming from M, and a "Newman" constraint coming from continuity of the action.

## Construction

Let π: M -> X be the orbit map. It is proper, and its fibres are orbits, which are finite or Cantor sets. Set

  𝒜 := π_! (Z_p)_M ⊗ (Haar measures) = lim_k π_{k!} (Z_p)_{X_k},

a constructible complex on X of modules over Λ. The stalk of 𝒜 at an orbit with stabiliser p^jZ_p is Λ/ω_j, where ω_j = (1+T)^{p^j} − 1. At a free orbit the stalk is Λ.

**Lemma 1 (Λ-Poincaré duality).** There is an isomorphism

  D_X(𝒜) ≅ RHom_Λ(𝒜, Λ)^ι ⊗ or_M [n],

where ι is the involution of Λ induced by g ↦ g^{-1}. So 𝒜 is an ι-hermitian self-dual object of D^b_c(X; Λ), and it defines a class

  w(M) := [𝒜] ∈ W^n(X; Λ, ι),

in Woolf's Witt group of self-dual sheaves. This class restricts to open sets and is natural for invariant open embeddings.

*Sketch.* Apply Verdier duality on M, take proper base change along π_k, and pass to the limit. The Λ-structure comes from Z_p acting on fibres by translation. Since 𝒜 ⊗^L_Λ Z_p = Z_p,X and Λ has global dimension 2, the same computation also recovers Yang's dim X = n+2. This is a consistency check.

**Lemma 2 (specialisation).** For a character χ of order p^k, put O_k = Z_p[ζ_{p^k}]. The class χ_*w ∈ W^n(X; O_k, conj) is the class of the χ-isotypic summand 𝒜_χ of π_{k!}Z_p. Its stalk is O_k exactly where the orbit has at least p^k points, and 0 elsewhere.

## The key lemma (Newman–Witt inequality)

Fix x ∈ X and a small conic neighbourhood V ∋ x. Let L_x be the link. The local invariant

  w_x := ∂[𝒜|_{V∖x}] ∈ W^{n-1}(L_x; Λ)/(image from V),

is computed with the Balmer localization sequence for S = {ω_j}, Λ -> S^{-1}Λ. It satisfies two constraints.

(a) **Manifold side.** Because π^{-1}(V) is an open subset of the manifold M, w_x equals the image of the *regular* class ⟨1⟩_Λ ⊗ [S^{n-1}]. Here [S^{n-1}] is the Witt fundamental class of the local homology sphere. Under every specialisation χ this gives the rank-one hermitian form ⟨1⟩ over O_k ⊗ Q. Its discriminant is a unit and is not a norm from the subfield of index p.

(b) **Continuity side.** The action is continuous and p^kZ_p -> 0, so for k ≫ 0 every p^kZ_p-orbit over V lies in a set whose diameter is far smaller than V. On V, the sheaf 𝒜 ⊗_Λ Λ/ω_k = π_{k!}Z_p is then the *transfer* (induction) of a self-dual sheaf from X_k along the Z/p^k-cover X_k -> X. The extension group Z/p of X_{k+1} -> X_k acts as the deck group there. Induction of hermitian forms along the cyclic extension O_{k+1} ⊃ O_k multiplies discriminants by norms. So χ_*w_x is a norm for χ of order p^{k+1}.

These two constraints contradict each other for every primitive χ of order p^{k+1}, because a unit-discriminant non-norm form cannot be a norm. Therefore w_x is undefined, which means V is not a neighbourhood of a free orbit. Then the free locus is empty, so some p^kZ_p fixes an open set. By Newman's theorem applied to the finite group Z_p/p^kZ_p acting on X_k, this contradicts effectiveness. Hence no faithful action exists.

## Where the work lies

The difficult step is (b). One has to prove that "uniformly small p^k-orbits" upgrades to an *isomorphism of self-dual sheaves* 𝒜|_V ≅ Ind(𝒜_k|_V), and not only an isomorphism of underlying sheaves. Two tools seem right for this:

- **Semialgebraic local triviality (Hardt).** Approximate the action on a chart by semialgebraic maps so that the induced data is constructible, and so that the localization boundary can be computed cell by cell.
- **Locality of Witt classes (Ranicki–Weiss, Woolf).** This guarantees that w_x depends only on a germ, so the approximation does not change it.

## Relation to Newman

The classical Newman argument works because a finite group has an integral transfer. For Z_p, the Haar measure of p^kZ_p is p^{-k}, and that destroys the integral transfer. The Witt class replaces the integer-valued degree with a *norm-residue* obstruction, which survives the passage to the inverse limit over the tower. That replacement is the proposed eureka.
