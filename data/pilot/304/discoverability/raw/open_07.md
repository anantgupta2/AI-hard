# Proposal: the Witt class of the orbit tower (a "p-adic signature" for the quotient)

## Setup
Let Z_p act faithfully on M^n, with X = M/Z_p and X_k = M/p^k Z_p. The maps q: M -> X and q_k: X_k -> X are proper because orbits are compact. Fix a coefficient field K = Q(zeta_{p^infty}) (or Q_l with l != p). For a continuous character chi: Z_p -> mu_{p^infty} of exact order p^k, set

  F_chi := ( R q_* K_M )_chi = the chi-isotypic summand of R q_{k*} K_{X_k} in D^b_c(X; K).

The summand is well defined because Z/p^k acts on X_k over X and |Z/p^k| is invertible in K. Also R q_* K_M = colim_k R q_{k*} K = (+)_chi F_chi, since locally constant functions on an orbit decompose into characters.

## Construction (Witt class of the tower)
1. Verdier duality on M gives D_M K_M = or_M[n], and proper pushforward commutes with D. Complex conjugation swaps chi and chi-bar. Together these give a canonical isomorphism

   phi_chi : F_chi --> D_X( F_chi-bar )[-n] (twisted by or),

   which is hermitian with respect to the conjugation on K. So (F_chi, phi_chi) is a hermitian object in Balmer's triangulated Witt group, and we can define

   w_chi := [F_chi, phi_chi] in W^n( D^b_c(X; K), D_X ).

   This is Woolf's Witt group of sheaves on X. It is defined even though X is not a manifold.
2. Restrict to a small open V in X, or more precisely to the pair (V, V minus a point). This gives local classes w_chi(x) in W^n of a point, i.e. W(K) or W^{-}(K). Each is a multisignature, i.e. an element of Z after a choice of embedding.

## Key lemma (vanishing versus Newman)
**Lemma.** Fix x in X and a basis of neighbourhoods V. Then:

(a) **(Continuity / averaging.)** Haar measure on Z_p gives the transfer. For chi of order p^k, the local multisignature equals a rho-type (G-signature defect) invariant of the Z/p^k-action on the link L_k(x) = boundary of q_k^{-1}(V). Summed over the p^{k-1}(p-1) primitive characters of order p^k, it equals sign(L_k / (Z/p^k)) minus sign(L_{k-1} / (Z/p^{k-1})). The quotient maps X_{k+1} -> X_k are Z/p-covers (Yang/BRW), so this is a difference of ordinary signatures of K-homology manifolds.

(b) **(Topological invariance.)** The local sum over all chi, sum_chi w_chi(x), is the local Witt class of K_M near the orbit q^{-1}(x). That class is the class of a compact family of (n-1)-sphere links, so it is bounded independently of k. By Ranicki–Weiss, the local L-class/signature data of a topological manifold is topologically invariant and locally trivial.

(c) **(Newman forces growth.)** Newman's theorem says p^k Z_p acts nontrivially with orbits that are not uniformly small, for every k. So for infinitely many k, the order-p^k characters contribute a nonzero local defect at some point of every V. The Z/p-cover structure of X_{k+1} -> X_k makes these contributions add, not cancel: by the Atiyah–Singer/Wall signature formula for prime-power covers, each nontrivial character class of order p^k contributes a defect of the same sign. Hence |sum_{ord chi <= p^k} w_chi(x)| grows without bound.

(b) and (c) contradict each other, so the action is not faithful.

## Why this should be the right invariant
- Yang's result that cd_Z(X) = n+2 says integral (or F_p) duality on X is shifted by 2. With coefficients K, where p is invertible, X is still an n-dimensional K-homology manifold. Its failure to be a manifold therefore lives entirely in the character decomposition. The Witt class w_chi is exactly the duality-compatible part of that decomposition. It is insensitive to the integral pathology but still remembers the cyclic coverings.
- Shifting a Witt class by 2 flips symmetric to skew (W^{n+2} = W^n_{-}). Balmer's 12-term localization sequence for the pair (X_k, fixed/singular strata) gives the exact sequence needed to localize w_chi at points (part a). It also identifies the boundary maps with linking forms of the covers L_k -> L_{k-1}.
- Semialgebraic local triviality (Hardt) plus the realisation of Witt classes by self-dual constructible complexes gives a model in which the link computations in (a) are finite and combinatorial.

## Status of the steps
- Parts (a) and (b) are formal: duality, transfer, and Ranicki–Weiss.
- The genuine content is (c). It requires that the defects attached to successive Z/p-covers do not cancel. My proposed mechanism is positivity of the defect for primitive characters, which is the analogue of the fact that the p-adic eta-function of a nontrivial lens-space tower is unbounded.
- If (c) fails, the same framework gives a weaker but useful statement: the Witt class defines a Z_p-valued measure on the character group. Faithfulness then forces this measure to be non-atomic, which is a concrete, checkable obstruction in low dimensions, where it recovers Pardon's n = 3 argument.
