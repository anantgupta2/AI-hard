# Proposal: the character-split transfer and p^k-divisibility of the Witt degree

## The construction

Fix k and let V ⊂ Y be the sheeted open set from Fact 5, with m = p^k, the cover π_k: W/p^kG → Y, and the multiplier β: q^{-1}V → μ_m. Let

  x := q_*[t] ∈ E_d(Y),

where t ∈ T(W) is the Verdier self-dual (d-shifted) test object behind Fact 4: the Haar-averaged ball-pinch class on a chart. q is proper because G is compact, and E_d is covariant for proper maps, so x exists. Fact 4 gives

  a_*(x) = u_d in E_d(S^d) ⊗ Q.   (1)

**Character-split transfer.** Over V, (π_k)_* R splits as ⊕_{χ ∈ (Z/m)^∨} L_χ. Here L_χ is the rank-one local system on V obtained by twisting with χ∘β. Because β(gw) = ζ^g β(w), multiplication by β intertwines L_χ and L_{χ·ζ}. So multiplication by β is a G-equivariant isometry carrying each summand to the next, and the Verdier duality pairing respects it, since β has values in roots of unity and its inverse is its conjugate. Define

  τ_k : W_d(T(Y)/T(Y∖V)) → W_d(T(Y)/T(Y∖V)),  τ_k(z) = [z ⊗ L_triv],

the projection onto the trivial-character summand.

**Lemma (sheet divisibility).** In the localized Witt group W_d(T(Y)/T(Y∖V)),

  x ≡ m · τ_k(x) = p^k · τ_k(x).

*Sketch.* x factors as (π_k)_* x_k, where x_k is the test class on W/p^kG, because q = π_k ∘ (W → W/p^kG). Modulo T(Y∖V), (π_k)_* x_k = x_k ⊗ (⊕_χ L_χ) = ⊕_χ (x_k ⊗ L_χ). The cyclic isometry from β identifies every summand with the χ = 1 summand inside the quotient category. The quotient is triangulated and duality-stable, by the same argument as Fact 1, so the Witt classes of the summands are equal. Since there are m summands, x ≡ m·τ_k(x). β is only locally constant, so the identification is local on V. This is why we must localize away from Y∖V.

## How it gives the contradiction

1. **Push forward with a test map that sees only V.** By Fact 6 there are N ≥ 1 and h ≃ N·a with h constant on Y∖V. Every object of T(Y∖V) pushes forward under h to a point, and E_d(pt) = W_d(D^b(R)) = 0 for d odd (odd-shifted Witt groups of a field vanish). So h_* factors through W_d(T(Y)/T(Y∖V)). Homotopy invariance (Fact 1) and (1) then give

  N·u_d = h_*(x) = p^k · h_*(τ_k x).

2. **Integrality.** h_*(τ_k x) is the image of an integral class, so it lies in L_d^{-1} Z u_d by Fact 2. Hence N ∈ p^k L_d^{-1} Z, i.e.

  v_p(N) ≥ k − v_p(L_d).   (2)

3. **Uniformity of N (the remaining sublemma).** The multiple in Fact 6 is the order of the obstruction to deforming a, at the level of E_d and not of genuine homotopy, into a map constant off V. In Witt groups of R-linear duality categories, the torsion is 2-primary, because a hermitian form over a field in which 2 is invertible has order dividing a power of 2 in W. So N may be taken to be a power of 2, and L_d = 2^{e_d} is also a power of 2.
   - For **p odd**: v_p(N) = v_p(L_d) = 0, so (2) fails for every k ≥ 1. This contradicts faithfulness, which is what made Fact 5 available for k ≥ 1.
   - For **p = 2**: replace R by C-coefficients with hermitian duality. There the multiplier β (in μ_{2^k} ⊂ C^×) is a genuine unitary twist, and Witt torsion is still 2-primary. Instead, run the argument with k → ∞: N is bounded independently of k as soon as V is chosen once, inside the first V. By Fact 5 applied to the G-invariant open set q^{-1}V as a new O, each V_k can be chosen inside V. Then (2) fails for k > v_2(N) + e_d.

4. Either way, the assumption that Z_p acts faithfully gives sheets of every order p^k (Fact 5, Newman). The degree-one test a then has Witt degree u_d that is divisible by unboundedly large powers of p inside a fixed lattice. That is impossible, so no faithful continuous Z_p-action on M exists.

## Why this is the right pivot

Yang and Bredon–Raymond–Williams show that the integral cohomology of Y has p-torsion in degree n+2. So any argument in ordinary cohomology lets the p^k-divisibility be absorbed by that torsion. This is exactly why Fact 6's multiplier could hide powers of p. Witt groups of real (or hermitian) self-dual sheaves see only 2-primary torsion. The character-split transfer turns the p^k sheets into an exact p^k-fold multiple in a group whose p-part is rigid (Fact 2). The genuinely new device is the β-twisted isometry between character summands. The rest is formal from Facts 1 to 6.
