# Proposal: the Iwasawa–Witt class of the orbit map

## Construction

Let Λ = Z_p[[Z_p]] ≅ Z_p[[T]] (with T = γ − 1) be the Iwasawa algebra, carrying the involution ι(γ) = γ^{-1}. Λ is a regular local ring of Krull and global dimension 2, and its residue field is F_p. Suppose Z_p acts faithfully on M. For p = 2, first pass to 2Z_p. Then the action preserves orientation, because the orientation character factors through Z/2 and the group is pro-p. Let π: M → X = M/Z_p be the orbit map, which is proper because the orbits are compact. Define

  𝓕 := Rπ_* ω_M[−n]  (Borel–Moore chains along the fibres),

which is a complex of sheaves of Λ-modules on X. At an orbit with stabiliser p^jZ_p, the stalk is the measure module Z_p[[Z_p/p^jZ_p]] = Λ/((1+T)^{p^j} − 1). A free orbit therefore has stalk Λ.

**Lemma 1 (Λ-Poincaré duality).** Verdier duality on M and proper base change give a quasi-isomorphism

  D_X^{Λ}(𝓕) := RHom_Λ(𝓕, ω_X ⊗^L Λ) ≅ ι^*𝓕[n],

so (X, 𝓕) is an n-dimensional Λ-homology manifold with a Hermitian self-duality φ. *Sketch:* this is Verdier duality for π, with π_! = π_*. The stalk check is the identity RHom_Λ(Λ/f, Λ) = (Λ/f)[−1] for f = (1+T)^{p^j} − 1, combined with the shift coming from the orbit being 0-dimensional over Λ/f.

This explains Yang/Bredon–Raymond–Williams conceptually. Since gldim Λ = 2, forgetting to Z_p-coefficients raises the cohomological dimension to n + 2, and Ext²_Λ(F_p, Λ) = F_p accounts for the p-torsion in degree n + 2.

**Invariant.** The pair (𝓕, φ) defines a class

  w(M) ∈ W^n(X; Λ, ι)

in Woolf's Witt group of self-dual complexes of sheaves (Balmer's triangular Witt groups applied to D^b(Sh(X; Λ))).

## Key lemma (local Witt rigidity)

For an open U ⊂ X, let w_U ∈ W^n(U; Λ) be the restriction. Woolf's 12-term localisation sequence (Balmer) applied to a point y and its punctured neighbourhood gives a **local class** λ(y) ∈ W^{n}_{y}(Λ) ≅ W^{0 or 1}(Λ_y-modules of finite length, ι), the Witt class of the link.

**Lemma 2 (topological nilpotence kills the link class).** If y has a neighbourhood U such that 𝓕|_U ⊗_Λ Λ/(T^N) is quasi-isomorphic to 𝓕|_U ⊗_Λ Λ/(T^N, p^m) up to Witt-neutral terms for all N, then λ(y) lies in the image of the torsion-module Witt group W(Λ/(p) -tors) and has trivial p-adic signature.

The reason is that the Witt group of finite-length Λ-modules with ι splits by characteristic support. Here ι fixes the maximal ideal, and the only ι-stable height-one primes come from cyclotomic factors Φ_{p^j}(1+T) and from p. The Witt class therefore decomposes into a sum over j of components λ_j(y) ∈ W(Q_p(ζ_{p^j}), conj) plus a p-part.

## Contradiction with faithfulness

1. **Newman forces infinitely many components.** Fix y and a small invariant neighbourhood. For each k, Newman's theorem gives an orbit of p^kZ_p that leaves a fixed ball. Apply this to the Z/p deck group of X_{k+1} → X_k. The component of 𝓕 at the primitive character Φ_{p^{k+1}}(1+T) then has nonzero restriction to the link of y, with Witt class equal to the local Z/p-signature defect (ρ-invariant) of that deck action. A connectedness argument (the link is a Λ-homology sphere over Frac Λ) makes λ_{k+1}(y) ≠ 0 for infinitely many k.

2. **Finiteness forces finitely many.** Lemma 1 makes 𝓕 locally perfect over Λ, with stalks of bounded Λ-rank (at most dim H_*(ball) = 1). A perfect Λ-complex has a characteristic ideal char(𝓕_y) ∈ Λ. Its cyclotomic support is finite by Weierstrass preparation, since a nonzero element of Z_p[[T]] has only finitely many zeros in the open unit disc. Hence λ_j(y) = 0 for all but finitely many j.

Steps 1 and 2 contradict each other, so no faithful action exists.

## Where the jump is, and the gaps

The new device is to treat the whole tower M → X_k as one self-dual sheaf over the 2-dimensional regular ring Λ. That converts Newman's "infinitely many small subgroups with large orbits" into "infinitely many cyclotomic zeros of a characteristic power series", and Weierstrass preparation forbids that. This is the analogue of the Iwasawa μ/λ-invariant argument.

Gaps to check:
- **Perfectness of 𝓕 over Λ.** This needs the constructibility of Hardt-type local triviality, which is not available for wild actions. A substitute could be cohomological local connectedness, using Bergfalk–Lupini–Panagiotopoulos-style definable lim¹ control on the tower.
- **The nonvanishing step in (1).** It requires the ρ-invariant of a Z/p action that is effective near a point to be nonzero on the link. In the smooth setting this is Atiyah–Bott/Smith theory. Topologically, it needs Ranicki–Weiss sheaf-theoretic signatures.
