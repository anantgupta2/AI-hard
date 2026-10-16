# Proposal: a Witt-valued character tower of the orbit maps

## Setup
Let Z_p act faithfully on M. Replacing Z_p by p·Z_p (still ≅ Z_p, still faithful), we may assume the action preserves orientation (for p = 2 as well), so Q_M is Verdier self-dual: D(Q_M) ≅ Q_M[n]. Put G_k = Z/p^k, X_k = M/p^kZ_p, X = X_0 = M/Z_p, and let π_k : M → X_k and q_k : X_k → X be the quotient maps. Each q_k is a finite branched cover with deck group G_k. The map π : M → X is proper and has Cantor-set or finite fibres.

## Construction (Witt-valued character tower)
1. Proper base change gives F_k := q_{k*} π_{k*}-invariants. Concretely, F_k := (Rπ_* Q_M)^{p^kZ_p} is a constructible sheaf on X with a G_k-action. Verdier duality commutes with proper pushforward, so D F_k ≅ F_k[n] G_k-equivariantly. Haar averaging (finite here) makes taking invariants exact, and this is what makes the duality descend. The duality is symmetric when n ≡ 0 (mod 4) and skew in general. Cross with CP² or a torus to fix the parity: this changes neither faithfulness nor the conclusion.
2. Decompose F_k ⊗ Q(ζ_{p^k}) into χ-isotypic pieces F_{k,χ}. Duality pairs F_{k,χ} with F_{k,χ̄}, so each F_{k,χ} carries a Hermitian self-duality. This gives Woolf/Balmer Witt classes

   w_{k,χ} ∈ W^n(D^b_c(X); Q(ζ_{p^k}), conj).

   Let N_k ⊂ W be the sum of these classes over the *primitive* characters χ of order exactly p^k. It is Galois-invariant, so it descends to W^n(X; Q). These are the "new" parts of the tower.
3. **Witt-valued character:** Ψ(M, Z_p) := (N_k)_{k≥1}. Localise at a point x ∈ X to get Ψ_x = (N_{k,x}) in the local Witt groups W(X, X∖x).

## Key Lemma (multiplicativity and divisibility)
(a) *Transfer.* Use the localization sequence (Balmer 12-term; Woolf for sheaves) for the stratification of X by orbit type: the stratum where p^kZ_p acts freely versus its complement. On the free part, the Z/p-cover X_{k+1} → X_k is a genuine covering, and the Witt class satisfies p·N_{k,x} = tr(N_{k+1,x}). This is a Hirzebruch-type multiplicativity, and it holds rationally because the transfer is Witt-isometric up to the factor p.

(b) *Integrality and boundedness.* Use Ranicki–Weiss: topological invariance of the rational L-class, done sheaf-theoretically. Then N_{k,x} is the image of a class living in a finitely generated group. The group is the local L-theory of a small neighbourhood, and its rank is bounded independently of k, because X has finite cohomological dimension n+2 (Yang, Bredon–Raymond–Williams). Concretely, signature-type invariants in a neighbourhood U are bounded by ranks of H^*(U; Q). By Newman, these ranks are uniformly bounded in k once U is small.

(c) Combine (a) and (b). The sequence N_{k,x} is infinitely p-divisible in a finitely generated group, so N_{k,x} = 0 for all k. That holds at every x, hence N_k = 0 by the localization sequence.

## Contradiction with faithfulness
Faithfulness means that for every k the subgroup p^kZ_p acts nontrivially. Newman's theorem then gives, inside any small U, a point whose p^kZ_p-orbit leaves U. So F_{k,χ} ≠ 0 for every primitive χ of order p^k, near every point of the nonfree locus. The remaining step is to show that a *nonzero* isotypic piece has a *nonzero* Witt class. This is the analogue of the fact that a free Z/p action on a closed oriented manifold has a nonzero ρ-type invariant.

- Restrict to a regular neighbourhood of a linking sphere S ⊂ M of a small orbit, with S chosen invariant by Haar averaging of a tube.
- There F_{k,χ} computes the χ-eigenspace of H^*(S; Q(ζ)). The Hermitian intersection form on that eigenspace has signature equal to the Atiyah–Bott/G-signature defect at the χ-character.
- The defects of characters of exact order p^k cannot all vanish while the action is nontrivial. This follows from the nondegeneracy of the cyclotomic Fourier transform on Z/p^k: if all χ-signatures were zero, the g-signatures sign(g, S) would all vanish for g of order p^k. Smith theory says the fixed set of such g in S is a mod-p homology sphere, so some g-signature is nonzero.

Then N_k ≠ 0 for every k, contradicting (c). So no faithful action exists.

## Where the real difficulty sits
Step (b) carries the weight. One needs local L-theory/Witt groups of the *non-manifold* X, which has cohomological dimension n+2, to be finitely generated with ranks bounded uniformly in k. Proving this is where the semi-algebraic triviality machinery (Hardt) would enter: approximate the orbit-type stratification by a semialgebraic model to get constructibility. Steps (a) and (c) are formal consequences of Verdier duality and Balmer–Woolf localization. The non-vanishing step is classical G-signature/Smith theory. I regard the Witt-valued character tower Ψ, with its divisibility-versus-finiteness dichotomy, as the single new device. The proof is a sketch; (b) is not proved.
