# Proposal: the Iwasawa orbit sheaf and its generic-rank duality

## Construction (the invariant)

Let Λ = F_p[[Z_p]] ≅ F_p[[T]] (T = γ − 1, γ a topological generator). This is a complete DVR with fraction field K = F_p((T)). Let π: M → X = M/Z_p and π_k: M → X_k = M/p^kZ_p.

Define the **Iwasawa orbit sheaf** on X:

  𝓜 := π_* F_p = lim→_k π_{k*}... (equivalently π_! F_p, since π is proper).

Its stalk at x = π(m) is C(Z_p·m, F_p) = C(Z_p/S_m, F_p), where S_m is the stabilizer. That is a discrete Λ-module, and its Pontryagin dual is

  𝓜_x^∨ ≅ F_p[[Z_p/S_m]] = Λ (if S_m = 0), or Λ/(T^{p^j}) (if S_m = p^jZ_p).

So 𝓜^∨ := RHom_Λ(𝓜, Λ^∨) is a constructible-type complex of compact Λ-modules on X. The invariant is the **generic fibre** 𝓛 := 𝓜^∨ ⊗_Λ K, a sheaf of K-vector spaces. Its stalk is K (rank 1) exactly on the free locus X_free and 0 elsewhere. Faithfulness enters here: if the action were not faithful, some p^jZ_p would act trivially and 𝓛 would vanish identically.

## Key Lemma (Λ-linear Verdier self-duality)

For any Z_p-action on an n-manifold, with ω_M ≅ or_M[n] (or_M is the orientation sheaf, which is F_p-trivial after passing to an index-≤2 subgroup):

  D_X(𝓜) ≅ 𝓜 ⊗ or [n]  Λ-equivariantly, hence D_{X,K}(𝓛) ≅ 𝓛^∨[n]

where D_{X,K} is Verdier duality for K-sheaves.

*Sketch.* π is proper, so D_X Rπ_* = Rπ_* D_M. Verdier duality on M commutes with the Z_p-action, which is continuous on sections, so the Λ-module structures match. Tensoring with K is exact because K is flat over Λ, and it commutes with the duality functor up to the K-dual, using the finiteness in Step 1 below.

Consequence: (X, 𝓛) is a **K-cohomology n-manifold with coefficient system 𝓛**. For every x, H^i_x(X; 𝓛) is K for i = n and 0 otherwise when x ∈ closure(X_free), up to the twist.

## How it yields a contradiction

**Step 1 (finiteness).** For a small Z_p-invariant neighbourhood W of an orbit, take H^*_c(π(W); 𝓜^∨). This is the Iwasawa limit lim←_k H^*_c(W/p^kZ_p; F_p)^∨. It is a finitely generated Λ-module, because by Nakayama it suffices that its reduction mod T is finite, and that reduction is H^*_c(π(W); F_p), which is finite since cd_{F_p} X = n (Yang / Bredon–Raymond–Williams) and X is locally F_p-acyclic at small scales.

**Step 2 (density, via Newman).** Each fixed set F_j = Fix(p^jZ_p) is closed. Since p^jZ_p acts nontrivially, Newman's theorem gives F_j empty interior. Under faithfulness, Baire then makes X_free dense, so 𝓛 has generic rank 1 everywhere on X.

**Step 3 (specialization vs. Yang).** The Λ-lattice 𝓜^∨ inside 𝓛 has reduction mod T equal to F_p on X. Step 1 and the Key Lemma together say that H^*_x(X; 𝓜^∨) is a finitely generated Λ-module whose rank over Λ is concentrated in degree n with rank 1. Its torsion is bounded by the Λ-length of the local stalks Λ/(T^{p^j}).

Now compute integrally. The universal coefficient sequence for Λ → Z_p (the "p-adic Bockstein" T ↦ p is not a ring map, so instead compare via the tower M → X_k with deck groups Z/p) sends a Λ-rank-1 local class in degree n to a Z-class in degree n+2. Each of the two Ext-shifts comes from lim¹ and Ext¹(Q_p/Z_p, Z) = Z_p. This is the origin of Yang's dim_Z X = n+2.

The Key Lemma forces the Λ-torsion part of H^{n+1}_x and H^{n+2}_x to vanish. Concretely, the Λ-dual of a K-homology manifold is Λ-torsion-free in top degree. But Yang's theorem says H^{n+2}_x(X; Z) ≠ 0 at some point, and that group is computed exactly from this Λ-torsion (the Λ/(T^{p^j}) pieces glued along the F_j). So the torsion must be nonzero for infinitely many j. This contradicts the uniform bound from Step 1: a finitely generated torsion Λ-module has torsion killed by a fixed T^N, while Newman's theorem produces stalks Λ/(T^{p^j}) with j → ∞ at every scale near x.

**Conclusion.** Faithfulness gives generic rank 1 (Step 2). Duality forces top-degree torsion-freeness (Key Lemma). Newman forces unbounded T-torsion, and Yang forces that torsion to be nonzero in degree n+2. These are incompatible, so no faithful action exists.

## Where the real work is

The crux is the comparison in Step 3: identifying Yang's integral class in degree n+2 with the T-power-torsion of the Λ-lattice 𝓜^∨, uniformly in the tower. One would prove a "μ-invariant = 0, λ-invariant bounded" statement for the local Iwasawa modules H^*_x(X; 𝓜^∨), analogous to Ferrero–Washington, and show that Newman's theorem makes λ unbounded. In SAT terms, the Λ-module structure acts as the extension variable: it packages the whole tower p^kZ_p into one module, so that the contradiction becomes a single finiteness statement rather than an infinite family of mod-p Smith arguments.
