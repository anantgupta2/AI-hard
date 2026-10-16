# Proposal: a sheet-transfer divisibility lemma for the averaged Witt degree

## The invariant

Write T_c for the compactly supported version of the test category, defined by localizing at a contractible open set as in tool 3. Since W = O x R^{d-n} is an oriented-up-to-sign topological d-manifold and d is odd, the shifted constant sheaf R_W[d] is Verdier self-dual. Fix a small closed chart ball D in W and let U be a contractible open set away from it. Then Rq_*(R_D[d]) gives a well-defined symmetric object of T(Y)/T(U); q is proper because G is compact. Call its class [W]_Y. By tool 3 we may view it as an element of E_d(Y). Define the **averaged Witt degree**

  delta(G, W) := a_*[W]_Y in E_d(S^d), with a the averaged pinch map from tool 4.

By tool 4, a∘q has degree 1 on the chart. Covariance and homotopy invariance (tool 1) then give delta = u_d + (torsion), so the rational image of delta is exactly u_d.

## Key lemma (sheet-transfer divisibility)

**Lemma.** For every k >= 1 there is an integer N_k, with v_p(N_k) <= c_d for a constant c_d that does not depend on k, such that

  N_k · delta(G, W) = p^k · x_k  for some x_k in E_d(S^d).

**Sketch.**
1. *Factor through the finite stages.* q = pi_k ∘ q_k, where q_k: W -> Y_k := W/p^kG and pi_k: Y_k -> Y. So [W]_Y = pi_{k*}[W]_{Y_k}.
2. *Localize to the sheeted region.* Take V from tool 5, so pi_k^{-1}V is p^k disjoint sheets S_1, ..., S_{p^k}. By tool 6, N_k·a ≃ h with h constant off V. Then N_k·delta = h_*[W]_Y, and that class only depends on [W]_Y|_V (excision in the Verdier quotient T(Y)/T(Y \ V)).
3. *Sheets are equivariantly identical.* The deck group Z/p^k = G/p^kG permutes the sheets transitively. The multiplier beta(gw) = zeta^g beta(w) trivializes this permutation compatibly with the self-duality forms: each translate g carries the symmetric form on R_{S_1}[d] to the form on R_{S_{g+1}}[d] with no sign or unit twist. Since R has no nontrivial p^k-th roots of unity for p odd, and for p = 2 the twist is absorbed into the 2-primary constant, the forms are isometric. Hence

  [W]_Y|_V = sum_g g_*(sigma_1) = p^k · sigma_1 in W_d(T(V)),

because h∘g = h on V. (The quotient map identifies the sheets, and h factors through Y.)
4. *Bound the multiple.* The homotopy in tool 6 comes from contracting Y \ V onto the basepoint after a d-fold suspension of the pinch. The obstruction to doing this with N = 1 lies in E_d of a contractible pair modulo T(U), and its denominators are controlled by the sphere lattice in tool 2. So N_k can be chosen to divide a fixed power of 2 times L_d. In particular v_p(N_k) <= c_d, uniformly in k.

## Contradiction with faithfulness

By tool 2, delta lies in L_d^{-1}Z·u_d modulo torsion, and its rational part is u_d. The Lemma gives N_k·u_d ∈ p^k·L_d^{-1}Z·u_d, so p^k divides N_k·L_d for all k. But v_p(N_k L_d) <= c_d + v_p(L_d), and this bound does not depend on k. Taking k > c_d + e_d contradicts this. So a faithful Z_p action cannot exist.

Where faithfulness enters:
- Through Newman (background), every open subgroup p^kG still acts nontrivially on any fixed chart. So for all k, V can be taken inside the region where tool 4's pinch is defined, and the sheets in step 3 are genuinely distinct. For a non-faithful action, Y_k -> Y would be a homeomorphism for large k, and step 3 would give a factor of 1, not p^k.
- Through Yang / Bredon–Raymond–Williams, cdim Y = n + 2. This is why one cannot simply compute in H^*(Y; Z) (the dimension jump destroys Poincaré duality). The Witt group of the test category is the replacement that still detects "degree".

## Proof analogy

This is a counting argument. A single bounded-denominator invariant (the averaged Witt degree) is forced to be divisible by p^k for every k, because at stage k it is a p^k-fold transfer. That is like a pigeonhole certificate whose size must grow with k while the lattice stays fixed. The substantive new device is step 3 plus the uniform bound in step 4. The rest is bookkeeping with tools 1–6.

**Main risk.** Step 4 (uniformity of v_p(N_k) in k) is the delicate point. If tool 6's multiple can only be bounded by a quantity depending on V, the fallback is to choose nested V_k and use homotopy invariance to transport a single homotopy N·a ≃ h_1 to all smaller V_k.
