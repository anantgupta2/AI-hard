# Proposal: a Haar-defect Witt class on the orbit tower

## Setup
Suppose Z_p acts faithfully on M^n. Put G_k = p^k Z_p, X_k = M/G_k, X = M/Z_p, and let π_k : M → X_k and q_k : X_{k+1} → X_k (a Z/p branched cover) be the quotient maps. Each π_k is proper, and its fibres are Cantor sets (orbits).

## The construction: the Haar-defect sheaf
Let F = Rπ_* Z_M on X. By proper base change, its stalk at x is H^0(Z_p·y; Z) = C^∞(orbit, Z), the locally constant integer functions on the orbit. Z_p acts on F, and F^{Z_p} = Z_X. Verdier duality on M gives

  D_X F ≅ Rπ_* (or_M)[n],

so F is self-dual of dimension n, up to the orientation twist. Taking invariants does not commute with D. Instead, D_X(F^{Z_p}) ≅ (D_X F)_{hZ_p}, the homotopy coinvariants. The key observation is that the **coinvariants of C^∞(Z_p/H, Z) are Z[1/p] when H is infinite-index trivial**, because the Haar measure on Z_p takes values in Z[1/p]. Define

  E := cone( Z_X ⊗ or → (Rπ_* or_M)_{hZ_p} )  (the *Haar-defect complex*).

**Lemma A (Haar defect).** E ⊗ Z[1/p] = 0, and E is a torsion complex whose stalk at x is Z[1/p]/Z = Z/p^∞, concentrated in a single degree. It is supported exactly on the set of points whose stabiliser is not open. By Newman's theorem and faithfulness, this set is nonempty. Its existence recovers the Yang/BRW computation: Ext(Z/p^∞, Z) = Z_p raises dim_Z X to n+2, while X stays a Z[1/p]-homology n-manifold.

The lemma is a sketch; I make no claim to have proved it. It is the dual statement of "averaging over Z_p is integral only after inverting p."

## The invariant: a Witt class in the tower
Each X_k is a Z[1/p]-homology n-manifold, being a finite p-group quotient of M. Restrict to the case n = 4m (or take M × CP^2 products to reach it). Then intersection on H^{2m}_c gives a self-dual object of D^b(X_k; Z[1/p]), and so, in Woolf's sense, a **sheaf Witt class**

  w_k ∈ W(X_k; Z[1/p]),

a homotopy-functorial refinement of the Ranicki–Weiss L-class. The new ingredient is to keep track of the **integral** lattice. The integral pushforward Rπ_{k*}Z_M gives an integral pairing on X_k that is non-unimodular at the branch locus. Its discriminant form δ_k is a p-primary torsion linking form. Define

  **λ_k(U) ∈ W(Q/Z)_{(p)} = W(Z/p^∞-linking forms),**

the Witt class of the discriminant (linking) form on H^{2m}_c(U_k) for a small ball U ⊂ X with preimage U_k ⊂ X_k. Equivalently, λ_k(U) is the boundary in the localisation sequence 0 → W(Z) → W(Q) → W(Q/Z) (Balmer's 12-term sequence, applied in Woolf's sheaf setting) of the Z[1/p]-Witt class of the local self-dual sheaf.

**Lemma B (transfer).** q_{k*} induces a transfer on Witt classes with q_{k*} q_k^* = multiplication by p. Away from the branch locus, λ_{k+1} = q_k^* λ_k. Hence the "renormalised" classes p^{-k} λ_k form an inverse system. Their limit is precisely the Witt class of the Haar-defect complex E restricted to U.

## How the contradiction should go
1. **Bounded rank (uniformity).** Fix a Newman neighbourhood U. Pardon's 3-manifold argument, together with Hardt's semialgebraic local triviality, applies after replacing U by a tame model (a compact PL ball and a finite good cover). This bounds the rank of H^{2m}_c(U_k; Z) independently of k. The bound comes from the Smith-theory inequality for Z/p^k actions, which bounds mod-p Betti numbers of quotients by those of U. So λ_k(U) lies in a subgroup of W(Z/p^N) for a fixed N that does not depend on k.
2. **Divisibility.** By Lemma B, the image of λ_k(U) in the limit equals p^k λ_∞(U) up to boundary terms that vanish on shrinking U. So λ_∞(U) is divisible by p^k for every k in a group of exponent at most p^N. Hence λ_∞(U) = 0.
3. **Non-vanishing.** Lemma A identifies λ_∞(U) with the Witt class of E|_U, a linking form on Z/p^∞ of rank ≥ 1. Faithfulness and Newman put a non-open stabiliser in U. Such a form has nonzero class: its Ext-dual is Z_p, whose form has nonzero discriminant in W(Q_p)/W(Z_p) ≅ W(F_p) ≠ 0.

Steps 2 and 3 contradict each other, so the action is not faithful.

## Why this is the right object
The obstruction to Hilbert–Smith is invisible rationally, and invisible mod q for q ≠ p. It lives entirely in the failure of Haar averaging over Z. A Witt or L-class invariant is topologically invariant (Ranicki–Weiss) and transfer-compatible, which lets one compare p-power transfers against a uniform bound. Step 1 is the hard step and the likely gap: it needs uniform-in-k control of the integral cohomology of the quotients of a fixed small ball. Newman's theorem by itself gives only non-smallness of orbits, not rank bounds.
