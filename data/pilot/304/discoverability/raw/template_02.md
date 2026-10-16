# Proposal: the isotypic Witt tower of the orbit map

## Setup
Let Z_p act faithfully on M^n. Replacing M by M x CP^2 x ... (same action on the first factor), assume n = 4m. Replacing Z_p by the open subgroup p^{k_0}Z_p (still faithful), assume the action preserves orientation and acts trivially on the finitely generated groups H^*(M), H^*_c(M) of a chosen relatively compact invariant region. Write X_k = M/p^k Z_p and pi_k : M -> X_k. These maps are proper because Z_p is compact. The tower X_{k+1} -> X_k has deck group Z/p.

Take coefficients K = Q(mu_{p^infty}) with complex conjugation as involution. Set F = R pi_{0*} K_M on X = X_0. Two facts hold for F:

1. **Isotypic splitting.** Z_p acts on F through the finite quotients Z/p^k, stalkwise and continuously. Averaging with Haar measure is exact in characteristic 0. Hence F = colim_k (q_k)_* K_{X_k} = ⊕_chi F_chi, where chi ranges over the continuous characters Z_p -> mu_{p^infty}. Here F_1 = K_X.
2. **Equivariant Verdier self-duality.** D_X F = D_X R pi_* K_M = R pi_* D_M K_M = F[n], which is Z_p-equivariant up to the inversion gamma -> gamma^{-1}. Projecting onto isotypic parts gives D F_chi = F_{chi-bar}[n]. In particular D K_X = K_X[n], so X is a rational homology manifold. This matches Yang/BRW: the extra 2 dimensions of integral cohomological dimension are pure p-torsion.

## The invariant
By (2), each F_chi carries a Hermitian (-1)^m... more precisely a (+1)-Hermitian, since n = 4m, nondegenerate pairing F_chi x F_chi -> D_X[-n]. This defines a class in Woolf's Witt group of self-dual complexes of K-sheaves on X:

  w_chi(M) := [F_chi, phi_chi] in W^n(X; K, bar).

Its compactly supported pushforward to a point lands in W(K, bar). For K-Hermitian forms this group detects the signature: the class there is sigma_chi, the signature of the chi-isotypic part of the intersection form on H^{2m}_c(U; K) for an invariant open U. The **isotypic Witt tower** is the family (w_chi) over all chi, organised by order p^k.

## Key lemma (Witt equidistribution)
Let U be invariant, relatively compact and connected. Suppose chi has order p^k and p^{k-1}Z_p acts on U with no orbit inside a Newman neighbourhood. Then

  w_chi|_U = w_1|_U in W^n(pi(U); K).

The same holds for every Galois conjugate of chi.

*Proof sketch.* Restrict to the cover X_k -> X_0 with group G = Z/p^k. Write F^{(k)} = ⊕_{ord chi | p^k} F_chi. This equals (q_k)_* K_{X_k}, which is D-self-dual as a G-equivariant object. Apply Balmer's 12-term localization sequence to the open-closed pair (free part of the G-action on X_k, its complement Sigma_k). The G-signature argument, in Gilmer's sheaf-theoretic form, now runs inside W rather than on a manifold. On the free part the chi-parts are rank-one twisted local systems L_chi with D L_chi = L_{chi-bar}[n]. Twisting by a finite-order rank-one local system acts as the identity on W after K-linear trace transfer. This is the topological counterpart of "free action gives equal isotypic signatures". The error terms are supported on Sigma_k. A Z_p-action is free on X_k precisely away from the image of points whose stabiliser is open. Newman's theorem forces Sigma_k to be p-adically shrinking, so its Witt contribution vanishes in the colimit.

## Contradiction with faithfulness
- **Finiteness.** H^{2m}_c(U; K) has finite total dimension, being a finitely generated cohomology of a relatively compact region of a manifold. So sigma_chi(U) ≠ 0 for only finitely many chi.
- **Equidistribution.** For all chi of order p^k with k ≥ k_1, the lemma gives sigma_chi(U) = sigma_1(U).
- **Non-vanishing of sigma_1.** Choose U to contain a product region B x N with sign(N) = 1, which is available after the initial product with CP^2. Restricted to the trivial character, sigma_1(U) = sign(U/Z_p) = sign(B x N) relative boundary = 1. This uses the fact that X is a rational homology manifold, so its signature is defined and equals the signature of the invariant part.
- Together these give infinitely many nonzero sigma_chi, which contradicts finiteness. Hence no faithful action exists.

## Where the real work lies
The step that needs a genuine new idea is the vanishing of the Sigma_k error terms in the Witt group. Without it, the argument only reproves "Z_p cannot act freely on a closed manifold of nonzero signature." The intended mechanism has two parts:

- **Hardt/semialgebraic local triviality, used to make Sigma_k constructible in the limit.** Sigma_k is replaced by a definable model, using Bergfalk–Lupini–Panagiotopoulos-style definable homology to control the derived colimit over k.
- **The Gersten–Witt spectral sequence.** It bounds the localization term by Witt classes of strata of codimension ≥ 1. Newman's theorem shows these strata carry no stable class as k -> infinity, because the orbits of p^k Z_p stay large while their isotropy shrinks.

A Witt-group invariant fits here because, unlike plain cohomology, it is insensitive to the p-torsion that makes M/Z_p look (n+2)-dimensional. It still remembers the character decomposition coming from the Z_p-tower.
