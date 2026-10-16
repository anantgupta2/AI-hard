# Proposal: the "middle-layer Witt class" of the p-adic pushforward tower

## Set-up
Let Z_p act faithfully on M^n. For p = 2, pass to 2Z_2 so the action preserves orientation (for p odd it already does, since Hom(Z_p, Z/2) = 0). Write X_k = M/p^kZ_p, X = X_0, π_k : M → X_k and q_k : X_k → X. Fix a precompact invariant open set U = Z_p·B, where B is a small ball. Coefficients are in F_p.

**Construction.** Let S = Rπ_*F_M[n] on X. The map π is proper with profinite fibres, so S is a sheaf placed in degree -n, with stalk C(Z_p/Stab_x, F_p) (locally constant functions on the orbit). Write g for a topological generator of Z_p. The map g acts on S, and N = g - 1 is nilpotent on each piece S_k = Rq_{k*}F_{X_k}[n] ⊂ S, with N^{p^k} = 0 there. Since π is proper and M is an oriented n-manifold, Verdier duality gives a symmetric (or (-1)^n-symmetric) isomorphism φ : S → D S. Under φ, g is an isometry, so N* = -N g^{-1}.

So (S_k, φ, N) is a self-dual object with a nilpotent self-adjoint endomorphism (up to a unit) in D^b(X; F_p). This puts it in Balmer's triangular Witt group setting, and in Woolf's Witt groups of sheaves on X.

## Key lemma (Jacobson–Morozov dévissage for Witt classes)
Let (A, φ, N) be a self-dual object in a triangulated category with duality, where N is nilpotent, N* = -N·unit, and N^m = 0. The kernel–image (monodromy) filtration W_• of N is self-dual, and in W(·) we have

  [A, φ] = Σ_j (-1)^j [P_j, φ_j],

where P_j is the N-primitive part of gr^W_j and φ_j(x, y) = φ(x, N^j y). If A is "N-regular" (all Jordan blocks of the same length L), then [A] = [P_{L-1}, φ_{L-1}] is a single layer, the *middle-layer Witt class* μ(A).

*Proof sketch.* Metabolic sub-Lagrangians are given by ⊕_{i<(L-1)/2} N^i P. Each off-middle pair of layers is hyperbolic, so only the middle layer survives. Balmer's 12-term sequence makes this work in the triangulated, non-split setting.

**Local computation.** At an orbit O ≅ Z/p^m, the stalk of S is F_p[Z/p^m] with the trace form. This is a single Jordan block of length p^m, so μ_x = ⟨ε_m⟩ ∈ W(F_p), where ε_m = (-1)^{(p^m-1)/2}·c_m for an explicit unit c_m (a binomial-coefficient product modulo p). In particular μ_x ≠ 0. As m varies, μ_x takes at least two distinct values: for p ≡ 3 (mod 4), it alternates in the square class of -1.

## Contradiction with faithfulness
1. **Generic orbits are large.** Each Fix(p^kZ_p) is closed. By Newman's theorem it is nowhere dense, since an effective Z/p action cannot fix an open set. So orbits of size at least p^k are dense for every k. By semicontinuity of Stab_x, the orbit-size function is lower semicontinuous and unbounded on every open subset of U/Z_p.

2. **Rigidity.** The global class μ(U) := [RΓ_c(U/Z_p; S_k), φ] ∈ W(F_p) is computed in two ways:
   - **(a) Topologically.** It equals the Witt class of the Z/p^k-equivariant intersection form on H^*_c(U; F_p). U is a connected open n-manifold, and the equivariant Poincaré pairing on H^*_c(U) ⊗ H^*(U) splits off a hyperbolic part, so μ(U) depends only on the F_p[Z/p^k]-module H^n_c(U) = F_p. That module is trivial and has a 1-block, which gives μ(U) = ⟨1⟩ for every k.
   - **(b) Sheaf-theoretically.** By the lemma, μ(U) is the hypercohomology of the middle-layer sheaf P_mid(S_k). That sheaf is supported on the closed set Σ_k of orbits of size exactly p^k, and it carries the form ⟨ε_k⟩. Since cd(U/Z_p) = n + 2 (Yang, Bredon–Raymond–Williams), and the transfer for each Z/p deck step X_{k+1} → X_k is multiplication by p (an isomorphism on W(F_p) for p odd), one gets μ(U) = ⟨ε_k⟩·χ_c(Σ_k), where χ_c is the compactly supported mod-2 Euler characteristic.

3. **Contradiction.** Equating (a) and (b) gives ⟨1⟩ = ⟨ε_k⟩·χ_c(Σ_k) for all k. By step 1, Σ_k ≠ ∅ for infinitely many k. Choose two consecutive k with ε_k, ε_{k+1} in different square classes; this is possible for p ≡ 3 (mod 4), and for p ≡ 1 (mod 4) one uses c_k instead. The identities ⟨1⟩ = ⟨ε_k⟩·χ_c(Σ_k) and ⟨1⟩ = ⟨ε_{k+1}⟩·χ_c(Σ_{k+1}) are then incompatible in W(F_p), since χ_c can only change the result by sign or parity. Hence the action is not faithful.

## Status
The new device is the middle-layer Witt class μ of the Verdier-self-dual pushforward together with its monodromy filtration. It turns Yang's "excess dimension n + 2" from an obstacle into bookkeeping: integrally the pushforward is not a manifold sheaf, but its Witt class is still governed by one graded layer.

The weakest step is 2(b). It needs an additivity/excision formula for μ over the stratification by orbit type. That stratification is not constructible, and is likely only "definable" in the sense of Bergfalk–Lupini–Panagiotopoulos. Proving that formula, presumably via a Gersten–Witt spectral sequence on X with its finite cohomological dimension, is the real work. Step 2(a) and the local computation are routine.
