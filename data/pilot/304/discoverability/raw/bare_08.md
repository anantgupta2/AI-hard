# Proposal: the Haar-defect sheaf and the p-adic Euler class of a Z_p-orbit fibration

**Setting.** Suppose Z_p acts faithfully on M. Write π: M → X = M/Z_p. Let Λ = Z_p[[Z_p]] ≅ Z_p[[T]], with T = γ − 1 and γ = action of 1. Work first on the dense G_δ set of free points. Stabilisers are 0 or p^kZ_p, and each Fix(p^kZ_p) is closed and nowhere dense by Newman/Smith. Afterwards, extend by the usual stratification.

## The construction

1. **Orbit sheaf.** Let F := π_* Z_M. Because π is proper with totally disconnected fibres, Rπ_* = π_*. The stalk F_x = C^∞(Z_p·x, Z) is the module of locally constant functions on the orbit, and γ acts on it, so F is a sheaf of Z[γ^{±1}]-modules on X.

2. **Haar-defect sheaf.** Define Q := coker(γ − 1 : F → F). Then ker(γ − 1) = Z_X. At a free point, f ∈ C^∞(Z_p, Z) lies in the image of γ − 1 iff its sum over one period vanishes. The map f ↦ p^{−k} Σ_{a∈Z/p^k} f(a), for f constant on p^kZ_p-cosets, is well defined and gives
   **Q_x ≅ Z[1/p].**
   This is the integer shadow of the fact that Haar measure on Z_p is not Z-valued: μ(p^kZ_p) = p^{−k}. So Q is a locally constant sheaf of rank-1 Z[1/p]-modules.

3. **Self-duality (key lemma).** M is an n-manifold, so ω_M = Z_M[n]. Proper base change and Verdier duality give
   D_X(F) ≅ π_* ω_M = F[n],
   and under this γ is sent to γ^{−1}. Next, Z_X = RHom_{Z[γ]}(Z, F) = [F → F] in degrees 0 and 1. Dualising,
   **ω_X ≅ [F →(γ^{−1}−1) F][n+1].**
   So ω_X has exactly two cohomology sheaves: H^{−n−1}(ω_X) = Z_X and H^{−n}(ω_X) = Q.

   This recovers Yang and Bredon–Raymond–Williams. Ext^1(Z[1/p], Z) = Z_p/Z ≠ 0, and that term places non-finitely-generated cohomology in degree n+2, so dim_Z X = n+2.

4. **The invariant.** The truncation triangle Z_X[n+1] → ω_X → Q[n] → is classified by
   **e(M) ∈ Ext^2_X(Q, Z_X),**
   the *p-adic Euler class* of the action. It is the exact analogue of the Euler class in the Gysin sequence of a circle bundle, with the fibre behaving as if it had dimension −2. Locally on a small open set U, Q ≅ colim(Z →p Z →p ⋯), so
   Ext^2_U(Q, Z) ≅ lim_k H^2(U; Z) ⊕ lim^1_k H^1(U; Z), with both limits taken along multiplication by p.

## How it should give the contradiction

**(a) Rescaling lemma (formal).** Pass to the subgroup p^kZ_p and its quotient X_k = M/p^kZ_p → X, a free Z/p^k-quotient. The Haar defect of X_k is the pullback of Q, but the comparison map Q → Q_k is multiplication by p^k, because the period becomes p^k times shorter. Naturality of the truncation triangle then gives
e(M)|_{X_k} = p^k · e_k,
so the pullback of e is divisible by p^k on X_k for every k.

**(b) Newman lemma (geometric heart).** Take x ∈ M and a small ball B ∋ x. By Newman, for every k some p^kZ_p-orbit O ⊂ X_k leaves B. Alexander duality on B − O, where O is a Cantor set, gives H_{n−1}(B − O) ≅ C^∞(O, Z)/Z. The γ-period sum on this group defines an integral class
c_k ∈ H^{BM}_{n+1}(X_k; Q_k^∨),
the linking cycle of the escaping orbit. The claim to prove is
**⟨e_k, c_k⟩ = ±1.**
The sign is the local orientation of M at x. The value is independent of k because it is computed inside B, where the manifold structure forces local linking number 1 between an (n−1)-sphere and the escaping orbit.

**(c) Contradiction.** Pull c_k back to X_m for m ≥ k. By (a), the pairing ⟨e|_{X_m}, c_k⟩ ∈ Z is divisible by p^{m−k} for every m. By (b), the same pairing is ±1. Hence p^{m−k} divides 1 for all m, which is false. So no faithful action exists.

## Where the work lies

Steps 1–4 and (a) are formal sheaf theory and I expect them to hold as stated. The real content is (b): the pairing must land in Z, not in Z[1/p]. That requires pairing against BM-homology with coefficients in Q^∨ = RHom(Q, Z), and controlling the lim^1 term. That term is precisely where Yang's pathological degree-(n+2) cohomology lives. If the lim^1 contribution can be shown to pair trivially with linking cycles of Newman orbits (they are compactly supported in B), the argument closes. I would also test the device on the known cases: Lipschitz and Hölder actions (Repovš–Ščepin, Maleshich) and n = 3 (Pardon).
