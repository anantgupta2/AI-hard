# Proposal: the isotypic Witt class of the orbit pushforward, and a p-adic divisibility lemma

## Setup
Suppose Z_p acts faithfully on M (n-dimensional). After replacing M by M x CP^{2} as many times as needed (the product action is still faithful), we may assume n = 4m. Let X = M/Z_p, X_k = M/p^k Z_p, with q_k : X_k -> X, and pi : M -> X. Because Z_p is compact, pi is proper and its fibres are orbits, which are totally disconnected. By proper base change, Rpi_* Q_M = pi_* Q_M =: F is a sheaf (concentrated in degree 0) with stalk C^lc(orbit, Q). It carries a smooth Z_p-action, and F = colim_k F_k with F_k := q_{k*} Q_{X_k} = F^{p^k Z_p}.

**Verdier self-duality.** D_X F = pi_* D_M Q_M = pi_* or_M[n] ≅ F[n]. Fix an invariant orientation; it exists after passing to p^k Z_p, and a p-group cannot reverse it. Then F is a symmetric self-dual object of D^b_c(X) of degree n, i.e. a class [F] in Woolf's Witt group W^n(X). The same holds for each F_k, because it is a direct summand cut out by the averaging idempotent with respect to Haar measure.

## Invariant
Tensor with C. The finite group Z/p^k acts on F_k, so F_k ⊗ C = ⊕_χ F_χ over the characters χ of Z/p^k. The duality pairs F_χ with F_{χ̄}, so each F_χ is a Hermitian self-dual complex. Define

  w_k(χ) := [F_χ] ∈ W^n_herm(X; C),

the **isotypic Witt class**. Next fix a Z_p-invariant open U ⊂ M with compact closure. Every point has a basis of such neighbourhoods, since saturating a small ball by a compact group gives one. Compose with the "local signature" homomorphism

  λ_U : W^n(X) -> Z,  [G] ↦ signature of the Hermitian pairing on the image of H^{2m}_c(U/Z_p; G) -> H^{2m}(U/Z_p; G).

## Key lemma (isotypic equidistribution in the Witt group)
**Lemma.** For every k and every character χ of Z/p^k, w_k(χ) = w_k(1) in W^n_herm(X; C). Consequently [F_k ⊗ C] = p^k [F_0 ⊗ C], and λ_U(F_k) = p^k λ_U(F_0).

*Proof sketch.* This is the sheaf-theoretic, local replacement for the free-action G-signature fact quoted in the prompt. Over the open set X° of free orbits, F_k is the pushforward of the constant sheaf along a principal Z/p^k-cover, and F_χ is a rank-one Hermitian local system L_χ. Write χ = ψ^a with ψ of order p and a ∈ Z/p^{k-1}. The family {L_χ} is the restriction to the p^k-torsion of a continuous family of unitary rank-one systems along the circle-valued "transfer" of the Z/p-deck groups of X_{j+1} -> X_j. Witt classes of Hermitian complexes are locally constant in continuous families of unitary twisting (a Witt cobordism given by the path of local systems, à la Ranicki/Woolf). Hence w_k(χ) is constant in χ. Non-free orbits have stabilisers p^j Z_p, which are open, so the stratum of non-free orbits contributes isotypic summands induced from smaller quotients. By induction on k these summands are also equidistributed. The Balmer localization sequence for W(X°) -> W(X) glues the two pieces.

## Contradiction with faithfulness
1. **Independence of k.** H^*_c(U/Z_p; F_k) = H^*_c(U/p^k Z_p; Q). Its colimit is H^*_c(U; Q), and the Witt classes are compatible under the transfers X_{k+1} -> X_k (deck group Z/p). For the product with CP^{2} copies, take U = B x N with B an invariant neighbourhood and N closed. Then λ_U(F) is computed by H_c(U) and equals the signature σ(N) = 1 (Künneth), and this is reached at a finite stage. So λ_U(F_k) = 1 for all k ≥ k_0.
2. **Divisibility.** By the Lemma, λ_U(F_k) = p^k λ_U(F_0) ∈ p^k Z.
3. Hence p^k divides 1 for large k. This is a contradiction, so no faithful action exists.

## Where the real work is
- The Lemma must hold in the **Witt group of the singular quotient**, which has cd = n+2 (Yang, Bredon–Raymond–Williams). Integrally X is not a homology manifold, but over Q (and C) Verdier self-duality of F is formal. This is the reason to work with the pushforward of Q_M and not with Q_X, and it is exactly where the Yang dimension anomaly is evaded.
- Newman's theorem guarantees that the deck actions on X_{k+1} -> X_k are never "small". This prevents the eigen-local systems L_χ from becoming trivial on U/Z_p, which would otherwise allow λ_U(F_0) to absorb the divisibility.
- Semialgebraic or o-minimal local triviality (Hardt) is not available on X. Constructibility of F must instead come from the inverse-limit structure, M = lim X_k in the sense of sheaves (Stacks: derived colimits).

The new ingredient is the isotypic Witt class w_k(χ) together with its χ-independence. It turns the classical free-action divisibility "|G| divides σ" into a p^k-divisibility that holds for **every** k. The p-adic group then forces the invariant to vanish, while Poincaré duality on M fixes it at 1.
