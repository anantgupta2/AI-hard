# Proposal: the tower Witt-degree and a transfer/self-similarity clash

## The invariant

Write G_k = p^k G, Y_k = W/G_k, and π_k : Y_k -> Y for the quotient map. π_k is proper, and it is generically a Z/p^k-cover (tool 5). Because Y_k is a quotient of the R-orientable odd-dimensional manifold W by a compact group, it is an R-homology d-manifold. So R_{Y_k}[d] carries a Verdier self-duality φ_k. It comes from the orientation of W, averaged with the Haar probability measure μ_k of G_k.

**Definition (tower Witt-degree).** Fix the moved test h : Y -> S^d (tool 6), constant off V. Set

  δ_k := h_* π_{k*} [R_{Y_k}[d], φ_k] ∈ E_d(S^d) ⊂ L_d^{-1} Z u_d.

Membership in T: R_{Y_k} is a hocolim of pushforwards from compact polyhedra. Approximate W/G_k by finite stages W/G_j and triangulate them semialgebraically (Hardt). Only the part over V matters (tool 3), and over V the object is a finite sum of constant sheaves on sheets. So the class lies in T(Y) after the localization of tool 3.

## Key lemma (two incompatible computations of δ_k)

**(A) Self-similarity.** δ_k = δ_0 for every k.

**(B) Transfer.** δ_k = p^k δ_0 for every k.

**(C) Non-vanishing.** δ_0 = N u_d with N ≥ 1, where N is the multiple from tool 6.

Together these give δ_0 = p^k δ_0 for k ≥ 1, so δ_0 = 0, which contradicts (C). Integrality matters here. All the δ_k lie in the fixed lattice L_d^{-1} Z u_d (tool 2), so the identities hold as statements about integers scaled by L_d^{-1}. No limit or completion can absorb the factor p^k. This holds for every p, including p = 2: N is fixed while the 2-adic valuation of p^k N is unbounded.

## Proof sketch

**(C).** By tool 4, a ∘ q has local degree 1 on a chart of W. For p^0, the Haar-averaged duality φ_0 is defined so that the Witt pushforward of [R_Y[d], φ_0] along a computes exactly this W-chart degree. Rationally, E_d(S^d) ⊗ Q = Q u_d, and the Witt class there is the signature. So a_*[Y] = u_d. Tool 6 replaces a by h ≃ N·a, which gives δ_0 = N u_d with N ≠ 0.

**(A).** G_k ≅ Z_p, and it acts on W as a faithful Z_p-action. The whole set-up of tools 1–6 is therefore available verbatim for (W, G_k). The test a is G-invariant, so it is G_k-invariant. Moreover a ∘ π_k ∘ q_k = a ∘ q still has local degree 1 on the same W-chart. The duality φ_k is normalized by the probability measure μ_k, so the argument of (C) applied to G_k computes h_*π_{k*}[Y_k] from the same W-chart data. The result is again N u_d. The point is that the normalized Witt degree is read off from W, not from the intermediate quotient.

**(B).** Decompose π_{k*} R_{Y_k} into isotypic pieces for the deck group Z/p^k:

  π_{k*} R_{Y_k} ≅ ⊕_{χ ∈ (Z/p^k)^} L_χ  (over C, then regroup conjugate pairs over R).

Each L_χ is a rank-one local system on the generic part of Y. Over V, the multiplier β from tool 5 satisfies β(g w) = ζ^g β(w), so β^χ is an explicit trivialization L_χ|_V ≅ R_V (or C_V). The duality φ_k decomposes orthogonally and pairs L_χ with L_{χ̄}. Under these trivializations it restricts on V to μ_0-normalized copies of the duality of R_V. The normalization matches because μ_k(G_k) = 1 = p^k · μ_0(G_k).

h is constant on Y \ V. Shrink a contractible neighbourhood U of the basepoint so that h^{-1}(U) ⊇ Y \ V. By tool 3, h_* factors through T(Y)/T(Y \ V), so every summand contributes only through its restriction to V. Therefore

  δ_k = Σ_χ h_*[L_χ] = p^k · h_*[R_Y|_V-extension] = p^k δ_0.

The real-structure bookkeeping (pairing χ with χ̄) changes no counts, because each conjugate pair gives a hyperbolic-free rank-2 real form of signature 2.

## Why this is the right pivot

The faithful action creates an infinite tower Y_k -> Y of sheet-counts p^k (tools 5 and 6). Witt classes with integral control (tool 2) on a degree-one test (tool 4) cannot be compatible with both:
- the self-similarity G_k ≅ G, which is invisible to W, and
- the transfer, which multiplies by the number of sheets.

The new device is the definition of δ_k with the μ_k-normalized duality, together with the observation that (A) and (B) are both forced. It plays the role of an extension variable. The object is tiny, but it converts the Newman-type "orbits do not shrink" data into a contradiction in a rigid integral invariant. Ordinary cohomology cannot do this, because Y has integral cohomological dimension n + 2 (Yang), so it cannot use Y's fundamental class directly.
