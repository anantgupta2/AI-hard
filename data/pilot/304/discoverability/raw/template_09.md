# Proposal: isotypic Witt classes of the orbit map (a sheaf-theoretic G-signature for Z_p)

## Setup
Suppose Z_p acts faithfully on M^n. Replace M by M x CP^2 x ... (trivial action on the factor) and then by a small invariant open neighbourhood, so that n = 4m. Let X = M/Z_p, let pi : M -> X be the (proper) orbit map, and let X_k = M/p^k Z_p. The fibres of pi are orbits Z_p/Stab, i.e. points or Cantor sets.

## The invariant
The constant sheaf C_M[n] is Verdier self-dual: D C_M[n] = or_M[n], and the orientation sheaf is trivial after the reduction. Since pi is proper, pi_* = pi_! commutes with D. So pi_* C_M[n] is a self-dual complex on X, with a hermitian duality, and Z_p acts on it. Its stalk at an orbit O is the space of locally constant functions on O. That stalk splits over the continuous characters chi : Z_p -> mu_{p^infinity}:

  pi_* C_M = (direct sum over chi) L_chi,   L_chi = the chi-isotypic summand.

Duality pairs L_chi with L_{chi-bar}. Hermitian (sesquilinear) duality therefore pairs L_chi with itself, so each L_chi is a hermitian self-dual object of D^b_c(X; C).

**Definition.** w_chi := [L_chi[n]] in W(X), the hermitian Witt group of self-dual sheaf complexes on X (Woolf; Balmer's triangulated Witt groups). For a relatively compact open V in X, set sigma_chi(V) := signature of the induced hermitian form on H^{2m}_c(V; L_chi) in W(C) = Z.

Summing over the characters that factor through Z/p^k gives

  (direct sum over chi^{p^k} = 1) L_chi = (r_k)_* C_{X_k},

so the sum of w_chi over chi^{p^k} = 1 is the pushforward of the class of X_k.

## Key lemma (equidistribution / sheaf G-signature)
For every k and every chi of exact order p^k, w_chi = w_1 in W(X)[1/p] modulo classes supported on the fixed-point strata F_j = Fix(p^j Z_p) for j < k.

*Sketch.* On the open set U_k = X \ F_{k-1}, the group Z/p^k = Z_p/p^k Z_p acts freely on the relevant quotient. There pi_* C splits as the regular representation tensored with a single self-dual sheaf, so all isotypic parts have the same Witt class. This is the sheaf-level form of the free G-signature fact; Gilmer's topological argument transfers because it only uses transfer and duality. Balmer's 12-term localization sequence W_F(X) -> W(X) -> W(X \ F) then pushes the discrepancy onto F. By Smith theory, F_j is a mod-p cohomology manifold of codimension >= 2 (Newman/Smith). Its contributions are p-primary torsion, or they vanish after inverting p, by the Gersten–Witt filtration argument (Balmer–Walter) applied to the stratification.

## Contradiction
1. **Finiteness.** For V small, the total sum of sigma_chi(V) over all chi is the local signature of pi^{-1}(V). It is finite and independent of k. Pick V so that pi^{-1}(V) contains a ball whose relative fundamental class gives local signature +-1. This is the 4m-dimensional local intersection form of C_M, which is unimodular of signature 1 on (B, boundary B) after the CP^2-stabilisation.
2. **Equidistribution.** By the lemma, for each k the phi(p^k) = p^{k-1}(p-1) characters of exact order p^k all contribute the same rational signature s_k = sigma_1(V) + (p-torsion). The characters of order dividing p^k contribute in total sigma(V; X_k), the signature of the k-th quotient, which has the form p^k s + (stratum terms).
3. **Newman forces non-vanishing.** Newman's theorem says that for every k, p^k Z_p moves some point of a fixed compact neighbourhood U by a definite amount. So L_chi restricted to V is nonzero for primitive chi of every order: the deck group Z/p of X_{k+1} -> X_k acts nontrivially over V.
4. Combining 1 to 3 gives 1 = sum over k of phi(p^k) s_k, with all but finitely many terms equal. Then s_k = 0 for large k. But then w_1 restricted to V is p^k-divisible in W(V)[1/p]-free torsion for all k, so w_1 = 0. This contradicts the fact that the trivial-character part (r_infinity)_* C_X carries the Yang / Bredon–Raymond–Williams class: X has cohomological dimension n+2, and the duality is nondegenerate on H^{2m}_c(V; L_1) because L_1 = C_X and X is a homology manifold away from F. So the signature is +-1, not divisible by p.

Hence the action has a nontrivial kernel, i.e. it is not faithful.

## Why this is the right device
The point of the construction is to make a free-action divisibility statement (|G| divides sigma) available for the non-free, infinite profinite action. It does this by (a) moving the computation to Witt groups of self-dual sheaves on the bad quotient X, where Verdier duality survives even though X is not a manifold, and (b) using Balmer localization to show that singular strata contribute only p-torsion. The crux to verify is the lemma's control of the stratum terms. Semialgebraic local triviality (Hardt) is the natural tool for making the strata constructible after approximation.
