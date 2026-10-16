# Proposal: the character-isotypic Witt class of the orbit-space pushforward ("p-adic signature sheaf")

## Setup
Suppose Z_p acts faithfully on M. After crossing with a closed simply connected manifold carrying the trivial action (e.g. CP^2 powers, so the signature is multiplied by 1), we may assume n = 4m and M is oriented. Faithfulness and orientation are preserved. Let X_k = M/p^kZ_p, X = M/Z_p = lim X_k, and pi: M -> X. Over C, decompose by characters chi: Z_p -> mu_{p^infty}. Since pi is proper with finite-type fibres (Z_p-orbits), the complex

  A := R pi_* C_M[4m]  (Čech, continuous-cohomology version)

splits as a colimit A = colim_k (pi_k^* side) = ⊕_chi A_chi. Here A_chi is the chi-isotypic part for the residual Z_p-action on pushforwards to X. Verdier duality on M (orientation gives D C_M[4m] ≅ C_M[4m]) and proper base change give a perfect pairing A_chi ⊗ A_{chī} -> D_X. This is a **Hermitian self-duality on A_chi**, the same pairing that underlies the isotypic splitting in the G-signature theorem quoted in the prompt.

**Invariant.** For each open V ⊂ X with pi^{-1}(V) a compact 4m-manifold with boundary (or open with finite-dimensional H_c), set

  w_chi(V) := [A_chi|_V] ∈ W(V; C, Hermitian)   (Woolf's Witt group of self-dual sheaf complexes),
  sigma_chi(V) := its signature image ∈ Z, i.e. the signature of the chi-twisted intersection form on H^{2m}_c(pi^{-1}V; C)_chi.

## Key lemma (Galois equidistribution plus finite level)
(a) *Galois invariance.* For a prime to p, sigma_{chi^a}(V) = sigma_chi(V). The form is defined over Q(mu_{p^k}), and Galois conjugation preserves signature of the Hermitian form after the standard identification of each conjugate's real embedding. This is the infinite-group replacement for the "equal signatures" clause of the finite-group fact.

(b) *Finite level.* H^*_c(pi^{-1}V; C) is finite-dimensional and Z_p acts continuously on it. So the action factors through Z/p^K, and sigma_chi(V) = 0 (indeed A_chi|_V is acyclic on global sections) for ord(chi) > p^K.

(c) *Local nonvanishing (where the content lies).* Take a point x and Newman's neighbourhood U. For every k there is a small invariant V_k ⊂ pi(U) such that the subgroup p^kZ_p acts on pi^{-1}(V_k) without being trivial on cohomology of the link pair. By Smith theory for the Z/p-quotients X_{k+1} -> X_k, the non-free stratum is a proper F_p-homology submanifold. The Yang/BRW dimension jump (dim_Z X = n+2 while dim_Q X = n) says the p-torsion in the local cohomology of X near pi(x) is unbounded in k. Feed this into the Gersten–Witt/Balmer localization sequence for the pair (V_k, non-free stratum) to obtain a characteristic of order exactly p^{k+1} with **w_chi(V_k) ≠ 0 in the Witt group of the punctured link**. Equivalently, the residue of A_chi along the stratum is nonzero.

## How the contradiction follows
Fix a compact invariant V ⊃ pi(U) with finite-type preimage and apply the localization exact sequence

  W(V) -> W(V \ S) --∂--> W_S(V)

to each A_chi. By (c), the boundary classes ∂w_chi are nonzero for characters of order p^{k+1} for infinitely many k. They are realised inside V, because V ⊃ V_k. Additivity of Witt classes under the decomposition V = V_k ∪ (V \ V_k) shows these local residues must be cancelled by global classes in W(V)_chi. By (a), the cancellation has to happen uniformly over each Galois orbit of chi, so in a group of size phi(p^{k+1}). The total signature therefore satisfies

  sigma(pi^{-1}V) = sigma_1(V) + Σ_k phi(p^{k+1}) s_k(V),  with s_k(V) ≠ 0 for infinitely many k,

which contradicts the finite-level statement (b): s_k(V) = 0 for k ≥ K. So the action is not faithful.

## Comments
- **Why this device.** It upgrades the finite-group "|G| divides signature" mechanism into a sheaf-theoretic Witt class on the *non-manifold* orbit space. Witt groups of sheaves (Woolf) and the localization sequence (Balmer) are exactly what makes sense on X, even though X is not a manifold and has dim_Z X = n+2.
- **Remaining gap.** Step (c) is the hard step: converting the Yang/BRW p-torsion growth into nonzero Witt residues. Over C, torsion is invisible. A real proof probably needs Z[1/p]- or Z_(l)-coefficient Witt groups (l ≠ p), or the semialgebraic local triviality (Hardt) to make A_chi constructible on a model of V_k. Pardon's 3-manifold argument handles the analogous step by hand in dimension 3, using linking-form torsion in place of a Witt class. The proposal is to make that linking-form step functorial via W(V).
