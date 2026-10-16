# Proposal: a Verdier-dual Witt-class tower on the orbit space, and a "p-adic signature" lemma

**Reductions.** By Newman, replace M by a small Z_p-invariant open set whose closure is compact. The connected component data is harmless. For p = 2, pass to 2Z_2 so the action preserves orientation (for odd p this is automatic). Coefficients are Q, or Z[1/2] where needed, so that Witt groups behave well. Write X_k = M/p^kZ_p, X = M/Z_p, and let π_k : X_k → X be the induced finite map. It is a branched Z/p^k-cover.

## Construction (the invariant)

1. Each X_k is the quotient of an oriented n-manifold by a finite orientation-preserving group. So X_k is an oriented **rational homology n-manifold**: D_{X_k} Q ≅ Q[n]. The map π_k is proper, so π_{k*} = π_{k!}. Hence
   F_k := Rπ_{k*} Q_{X_k}[n/2] (shift by n, made symmetric in the usual way)
   carries a nondegenerate symmetric duality F_k ≅ D_X F_k. That gives a class [F_k] in Woolf's Witt group W(D^b_c(X; Q)), with the shift set by n.
2. Z/p^k acts on F_k. Split F_k by characters. The summand G_k for the *primitive* characters of order p^k is a Q(ζ_{p^k})-module sheaf. Duality pairs χ with χ̄, so G_k carries a nondegenerate **hermitian** duality over Q(ζ_{p^k}) with its complex conjugation. Define
   w_k := [G_k] ∈ W^h(D^b_c(X; Q(ζ_{p^k}))),
   which gives [F_k] = Σ_{j≤k} tr_{Q(ζ_{p^j})/Q} w_j.
3. **Local invariant.** For y ∈ X, take the local Witt class at y. This is the image of w_k in the Witt group of the punctured costalk/stalk "link" at y, obtained from Balmer's 12-term localization sequence for {y} ⊂ U ⊂ X. Call it λ_k(y) ∈ W^h(Q(ζ_{p^k})) (shifted). Its multisignature gives an integer vector σ_k(y) ∈ Z^{φ(p^k)/2}.

## Key lemma (p-adic signature identity)

> For every y ∈ X and every small Z_p-invariant neighbourhood, Σ_{k≥0} Tr σ_k(y) = 1, where Tr is the trace over all complex embeddings. Moreover Tr σ_k(y) ≡ 0 mod p^{k-1}(p−1), and σ_k(y) is **constant on the free stratum** in a neighbourhood of y.

*Sketch.*
- The left side is the local signature of the constant sheaf on M at a manifold point. The pushforward of Q_M to X is colim_k F_k, because the fibres are Cantor sets whose Q-cohomology is the locally constant functions. Witt classes are additive under this splitting, and the local class of Q_M at a manifold point is ⟨1⟩, with signature 1.
- The congruence comes from the hermitian trace form. A rank-r hermitian form over Q(ζ_{p^k}) has trace-signature divisible by [Q(ζ_{p^k})^+ : Q]·(stuff). That quantity is divisible by p^{k−1}(p−1)/2, and by more after symmetrising over the conjugate embeddings.
- Constancy on the free stratum: there G_k is a rank-one Q(ζ_{p^k})-local system (the line bundle of the Z/p^k-torsor), and Witt classes of local systems are locally constant.

## Contradiction with faithfulness

Suppose the action is faithful. By Newman, for every k the subgroup p^kZ_p acts nontrivially inside every neighbourhood. So G_k ≠ 0 near every point, and λ_k(y) ≠ 0 for infinitely many k. That would give infinitely many nonzero terms of rapidly growing p-adic valuation in a finite sum equal to 1. This alone is consistent: the sum converges p-adically.

The real leverage comes from the **second constraint**. Each F_k is a constructible complex on X. By Yang and Bredon–Raymond–Williams, X has integral cohomological dimension n+2, while F_k lives in perverse degrees [−n, 0]. Apply Balmer–Walter (the Gersten–Witt spectral sequence) and the localization sequence to the closed set of non-free orbits of p^kZ_p. The class λ_k(y) is then forced to come from Witt groups of degree shift ≥ n+1. Those groups vanish for a hermitian form of rank 1 over a field (Witt groups of fields are 4-periodic and concentrated in shift 0 mod 4). Combined with the uniform-in-k local constancy, this gives λ_k(y) = 0 for all large k. That contradicts Newman's nontriviality: a nonzero primitive-character summand of a self-dual sheaf on a Q-homology manifold has nonzero local Witt class, by the multisignature detection of Ranicki–Weiss type local L-classes.

## Status and gaps

The main point is to replace Yang's *integral cohomology* obstruction by an obstruction in **Witt groups of sheaves with Verdier duality**, organised by character level. A Witt class (unlike cohomology) sees the self-duality, and through multisignatures it sees each character separately. The cohomological-dimension jump to n+2 only shows that the limit is not a manifold. The Witt tower should show that the *levels* cannot all carry nonzero local duality data.

The weakest step is the degree-shift vanishing in the last paragraph. It needs a precise statement that the n+2 dimensional defect is exactly the obstruction to Verdier self-duality of colim F_k. It also needs a proof that it pushes λ_k into vanishing Witt degrees uniformly in k. A semialgebraic/definable approximation (Hardt triviality) of the finite-level quotients X_k may be needed to control constructibility uniformly.
