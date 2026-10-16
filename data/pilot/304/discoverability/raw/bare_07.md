# Proposal: the local Iwasawa (Λ-adic) homology sheaf and its Newman-controlled Euler class

**Caveat.** This statement is the Hilbert–Smith conjecture. Pardon settled n ≤ 3 (2013); n ≥ 4 is open. Below is one concrete device and a reduction showing exactly where a contradiction would have to come from. The final step is a conjectural lemma, not a theorem.

## Setup
Let Λ = Z_p[[Z_p]] ≅ Z_p[[T]] with T = γ − 1, where γ is a topological generator, and let ω_k = (1+T)^{p^k} − 1. Write M_k = M/p^kZ_p, X = M/Z_p, and π_k : M → M_k. Assume the action is free. This is the standard reduction: pass to a small invariant open set on which the stabilizers p^kZ_p are trivial. Smith theory together with Newman's theorem makes each fixed set Fix(p^kZ_p) nowhere dense.

## Construction (the Λ-homology sheaf)
For x ∈ X with orbit C_x ≅ Z_p, a Cantor set, define

  𝓛_x := H^{St}_n(M, M − C_x; Z_p)  (Steenrod homology).

Alexander–Steenrod duality on the n-manifold M gives H^{St}_n(M, M − C) ≅ H^{St}_0(C; Z_p) ≅ Meas(Z_p, Z_p) = Λ. In all other degrees the group vanishes. These stalks form a sheaf 𝓛 of Λ-modules on X that is **locally free of rank 1**: X is a "Λ-homology n-manifold". Its specialisations are

  𝓛 ⊗_Λ Λ/ω_k = local Z_p-homology of M_k (a Z_p[Z/p^k]-module),  𝓛 ⊗_Λ Z_p = local homology of X.

The comparison maps are isomorphisms only up to lim¹ terms. Those terms are exactly where Yang's jump n → n+2 for integral coefficients lives, through H²(BZ_p; Z) = Q_p/Z_p.

## Invariant: the Λ-Euler class
Let e ∈ Ȟ²(X; Z) be the Bockstein of the class of the principal Z_p-bundle M → X in Ȟ¹(X; Z_p). The class e is the obstruction to the bundle being trivial, and it appears in the Gysin-type sequence

  … → Ȟ^{i}(X) →(∪e) Ȟ^{i+2}(X) → Ȟ^{i+2}(M-type terms) → …

Yang's theorem says that e ∪ (local fundamental class) is **nonzero in local cohomology at every point**, H^{n+2}_x(X; Z) ≠ 0. This is the phenomenon that pushes cd_Z X to n+2.

## Key lemma (proposed)
**Lemma (Newman rigidity of e).** Let U be a Newman neighbourhood of x ∈ M with image V ⊂ X. Then for all k ≫ 0 the restriction of e to the level-k set V_k ⊂ M_k is **p^k-divisible by a class of uniformly bounded support**. Hence the local class

  e_x ∈ lim_k H²_{x}(V_k; Z/p^k)

dies in the inverse limit.

*Why it should hold.* Newman's theorem says that the orbit of each small subgroup p^kZ_p leaves U. Over a fixed compact K ⊂ V, the Z/p^k-cover V_k → V therefore has connected-fibre "sheets" that must leave π(U). The Bockstein of a Z/p^k-cover whose sheets leave a neighbourhood is supported on the boundary of π(U), not near x. Summed over k, this gives the divisibility, because the transfer M_{k+1} → M_k has degree p.

## Contradiction sketch
1. By the Λ-sheaf structure, local Z-cohomology at x is computed by R lim_k of 𝓛 ⊗^L Λ/ω_k. The only possible nonzero contribution in degree n+2 is lim¹ of the Bockstein tower, and that tower is exactly the local class e_x.
2. The lemma kills e_x in the limit and makes the lim¹ term Mittag-Leffler-trivial. Uniform support is what gives the Mittag-Leffler condition.
3. Therefore H^{n+2}_x(X; Z) = 0 for every x, which contradicts Bredon–Raymond–Williams/Yang (cd_Z X = n+2).
4. Hence there is no free action. Undoing the reduction, there is no faithful action at all.

## Where the gap is
Step "sheets leave π(U) ⇒ Bockstein supported away from x" is unproved. Raymond–Williams constructed faithful Z_p-actions on n-dimensional *compacta* with dim(orbit space) = n+2, so the lemma must use the manifold structure: local Λ-freeness of 𝓛, i.e. Poincaré duality at the level of measures on orbits. It cannot follow from Newman's property alone. In SAT terms, 𝓛 plays the role of an extension variable. It packages the infinite tower {M_k} into one rank-1 object over a 2-dimensional regular ring Λ. Krull dimension 2 is precisely the "+2", so the whole difficulty becomes one Mittag-Leffler (divisibility) statement for one cohomology class.
