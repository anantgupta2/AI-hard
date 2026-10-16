# Proposal: the sheet-divisible Witt degree, plus a p-prime moving lemma

## The invariant
Fix the stabilized setting (tools 1-6): W = O x R^{d-n}, d odd, G = Z_p (already shrunk to H as in tool 4), q: W -> Y = W/G, and a: Y -> S^d the averaged degree-one test. Take a compact polyhedral chart ball B in W, with ∂B sent into a contractible open U ⊂ Y. Define the **orbit fundamental class**

  Φ := [Rq_* R_B, with its d-shifted duality relative to U] ∈ W_d(T(Y)/T(U)) ≅ E_d(Y)   (tool 3),

and for any map f: Y -> S^d (proper on the relevant support) set the **Witt degree** deg_E(f) := f_* Φ ∈ E_d(S^d). By tool 4, deg_E(a) = u_d. By tool 2, every Witt degree lies in the fixed lattice L_d^{-1} Z u_d.

## Lemma A (sheet divisibility)
Let V ⊂ Y \ {basepoint} be a sheet set at level k (tool 5, m = p^k). If f is constant on Y \ V, then

  deg_E(f) = m · f_*Φ^{(1)},   where Φ^{(1)} ∈ E_d(Y) is the contribution of one sheet,

so deg_E(f) ∈ p^k L_d^{-1} Z u_d.

*Sketch.* Classes supported on Y \ V are pushed by f to a point, and W_d(pt) = W_d(R) = 0 for odd d. So deg_E(f) depends only on Φ|_V. Over V, q factors as W -> W/p^kG -> Y, and the second map is m disjoint sheets. The multiplier β gives an explicit splitting of the pushforward, (π_* R)|_V = ⊕_{j ∈ μ_m} R·1_{β=j}, and this splitting is compatible with duality because each indicator is self-dual. G acts by β(gw) = ζ^g β(w), so it permutes the summands transitively. Since Φ is pulled back from Y, it is G-invariant, so all m summands carry the same Witt class. Each summand maps homeomorphically onto V, so its pushforward is a genuine element of E_d(S^d) and lies in L_d^{-1}Z u_d.

## Lemma B (p-prime moving; the new ingredient)
In tool 6, the multiple N with N·a ≃ h can be chosen **prime to p**. More precisely, N can be a power of 2 bounded by L_d · 2^{c(d)}, with c(d) independent of V and of k.

*Sketch.* The obstruction to compressing a off V is a class in the relative group E_d(Y, Y \ V). Its image in E_d(S^d) is detected after ⊗Q, because E_d(S^d) ⊗ Q = Q u_d. Two maps that agree there differ only by torsion in the Witt groups of T(·). That torsion is 2-primary: these are Witt groups of R-linear triangulated categories with duality, and Pfister's theorem says Witt torsion over R is 2-primary. This passes to triangulated Witt groups through Balmer's 12-term localization sequence and the Gersten-Witt spectral sequence. The rational part is handled by the homotopy in tool 6. Hence N kills only 2-primary torsion, of bounded exponent: L_d covers the sphere denominators, and 2^{c(d)} bounds the length of the d-step obstruction filtration.

## Contradiction
1. Choose k with p^k > 2^{c(d)} · L_d^2. Take V = V_k from tool 5, then h and N from Lemma B.
2. Homotopy invariance and linearity give N·u_d = N·deg_E(a) = deg_E(h).
3. By Lemma A, deg_E(h) ∈ p^k L_d^{-1} Z u_d. So N·L_d = p^k · j for some integer j ≠ 0.
4. For odd p, N·L_d is a power of 2 and so cannot be divisible by p^k. That is a contradiction.
5. For p = 2, the size bound N·L_d ≤ 2^{c(d)} L_d^2 < p^k ≤ p^k |j| gives the contradiction.

So no effective action of an open subgroup H ≤ Z_p exists. Since H ≅ Z_p, no faithful Z_p-action exists.

## Why this is the right pivot (proof-complexity reading)
The device is a **degree that can be computed sheet by sheet**. Witt classes play the role an extension variable plays in a proof system: they turn the global and uncomputable map Y -> S^d into a linear quantity that can be split over the m sheets. Lemma A is a counting argument: the degree is a multiple of p^k, for every k. Lemma B keeps the bookkeeping error away from the prime p. Together they reproduce Newman-style smallness ("orbits not uniformly small") at the level of an integer invariant, and the clash with the fixed lattice of tool 2 finishes the proof. This is where the integral cohomological dimension n+2 of Yang and Bredon-Raymond-Williams (where ordinary degree theory breaks) is bypassed: Witt groups of T(Y) see only compact polyhedral tests, never the wild cohomology of Y.

**The likely gap** is Lemma B: the claim that the torsion is 2-primary at the level of T(Y), with no p-primary torsion coming from Yang's Z_p-cohomology.
