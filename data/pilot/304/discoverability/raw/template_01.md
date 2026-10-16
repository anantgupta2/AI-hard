# Proposal: the character-graded Witt class of the orbit map (a "p-adic signature")

## Construction

Assume Z_p acts faithfully on M. First stabilize: replace M by M x (CP^2)^j with the trivial action on the second factor. The action stays faithful, and we can take n = dim M ≡ 0 (mod 4), n = 4m.

Let X = M/Z_p, X_k = M/p^k Z_p, and π: M → X. The map π is proper with compact fibres. Haar averaging decomposes the pushforward by characters χ ∈ Ẑ_p = Q_p/Z_p:

  Rπ_* C_M ≅ ⊕_χ F_χ,  where F_χ = (Rπ_* C_M)^χ is the χ-isotypic part.

Each F_χ is a sheaf on X (cohomological degree 0). Its stalks have dimension ≤ 1: the stalk at an orbit O ≅ Z_p/Stab is C when χ|_Stab = 1, and 0 otherwise. Proper base change together with Verdier duality on M (C_M[n] is self-dual, since M is oriented, after passing to the orientation cover if needed) gives

  D_X F_χ ≅ F_{χ̄}[n].

The hermitian pairing F_χ ⊗ conj(F_χ) → ω_X[-n] is induced by cup product followed by integration over fibres against Haar measure. So F_χ[2m] is a hermitian self-dual object, and it defines a class

  w_χ ∈ W_c(X; C, herm),

the Witt group of self-dual constructible-type complexes (Balmer; Woolf, *Witt groups of sheaves*). Composing with the "local signature" homomorphism W_c(X) → H_0^{lf}(X; W(C)) = H_0^{lf}(X; Z) yields an integer-valued local index σ_χ(x).

## Key lemma (graded signature rigidity)

**(a) Locality.** σ_χ is locally constant on the open dense set where χ is trivial on stabilizers. At such a point, F_χ looks locally like the constant sheaf on a homology n-manifold over Q, which X is: by Yang and Bredon–Raymond–Williams it fails to be a manifold only p-locally. So σ_χ(x) ∈ {0, ±1}. It equals 1 at every orbit whose stabilizer lies in ker χ, by the same computation that shows the local Witt class of C_M[n] is the generator of W(pt) = Z.

**(b) Galois and transfer invariance.** Gal(Q(ζ_{p^∞})/Q) ≅ Z_p^× permutes the characters of exact order p^k transitively. Because F_χ is defined over Q(ζ_{p^k}), the classes w_χ inside one Galois orbit have the same image under the trace to W(X; Q). Write w_k for that common image; it has rank φ(p^k) = p^{k-1}(p-1).

**(c) Finite-level identity.** For q_k: X_k → X with deck group Z/p^k, the G-signature splitting (the established finite-group fact, applied sheaf-theoretically over X, since the free part has full measure)

  [Rq_{k*} C_{X_k}] = Σ_{χ^{p^k} = 1} w_χ

combines with (b) to give, in H_0^{lf}(X; Z),

  σ(X_k) = 1 + Σ_{j=1}^{k} p^{j-1}(p-1)·σ_j,  where σ_j(x) = (1/φ(p^j))·σ(w_j)(x).

## Contradiction with faithfulness

Fix x ∈ M, and let U be a Newman neighbourhood of x (Newman 1931). For every k, faithfulness gives a point y_k ∈ U on which p^k Z_p acts nontrivially. A Baire argument over the closed sets Fix(p^k Z_p) shows that the set where p^k Z_p acts freely modulo its kernel is dense and open. On that set:

1. Each orbit of X_k → X is a finite set of p^k points. Equivalently, q_k is a p^k-sheeted branched cover over an open set V ⊂ X that meets π(U).
2. Applying (a) to X_k, which is also a Q-homology manifold, gives σ(X_k)|_V = p^k·σ(X)|_V. This is the "|G| divides the signature" statement, localized.
3. Comparing with (c), every σ_j|_V = 1 = σ(X)|_V, for every j. This holds only if all characters of order ≤ p^k are trivial on all stabilizers over V.

Now take the costalk at π(x), the point Newman's theorem controls. Since π is proper, the local Witt class of C_M[n] at the fibre O_x is a single generator. On the other hand, by (c) its pushforward is Σ_χ w_χ, and step 3 says that sum has infinitely many unit summands near π(x): one for every χ, of every order p^k. The class must be finite, because H^*_c of a small invariant ball is finite-dimensional (Hatcher / Kashiwara–Schapira finiteness for proper maps of manifolds). So the infinitely many nonzero graded pieces F_χ produce a non-finitely-generated element of H_0^{lf}(X; Z) near π(x). This contradicts the finiteness of H^*_c(π^{-1}(B); C) for a small invariant neighbourhood B.

So some p^k Z_p acts trivially, and the action is not faithful.

## Remarks on what is new and what remains

- The device is the **Witt class indexed by Q_p/Z_p**: one signature-type class per character, and the Galois/transfer identity (c). It turns Atiyah–Singer/Gilmer divisibility "p^k divides the signature" into a single sheaf-theoretic identity that stays finite in the limit k → ∞. Yang's n+2 dimension anomaly is invisible over C. The p-adic information lives entirely in the Galois-orbit ranks φ(p^k).
- The weakest step is (a) at non-free points. There one needs Woolf's localization sequence (Balmer's 12-term sequence) to show that the local signature homomorphism is well defined on the p-singular stratum of X.
