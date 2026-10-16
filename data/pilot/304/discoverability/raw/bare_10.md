# Proposal: an Iwasawa-module invariant of the quotient tower, made rigid by Verdier duality

**Status caveat.** As far as I know, the statement (Hilbert–Smith for Z_p) is open in general. It is proved for n ≤ 3 (n = 3 by Pardon, 2013) and for Lipschitz and Hölder actions with exponent > n/(n+2) (Repovš–Ščepin, Maleshich). What follows is a concrete device with one isolated hard lemma. It is not a complete proof.

## Construction

Let Λ = Z_p[[Z_p]] ≅ Z_p[[T]], with T = γ − 1 for a topological generator γ. Assume Z_p acts faithfully on M. By Newman's theorem we may shrink to a connected, Z_p-invariant, relatively compact open set U. Take U to be the saturation of a small ball, so that p^k Z_p acts faithfully on U for every k. Put X_k = U / p^k Z_p and π_k : U → X_k.

**Definition (tower module).** For each degree q, set

  𝓗^q(U) := lim_k H^q_c(X_k; Z_p) (the limit taken along transfers), with its natural Λ-module structure.

Define its Iwasawa invariants (μ_q, λ_q, r_q) = (μ, λ, Λ-rank) of the finitely generated torsion/free parts. Finite generation follows from the compactness of the closure of U and the constructibility of Rπ_{k*}Z_p below.

## Key lemma (the new input)

**Lemma (local duality on the tower).** Let D_k be the dualizing complex of X_k. There is a Λ-equivariant isomorphism

  R lim_k Rπ_{k*} D_U ≃ (R lim_k D_{X_k}) ⊗^L_Λ Λ[1],

where D_U = or_U[n]. The shift [1] is the cohomological dimension of Z_p, i.e. the Poincaré-duality group Z_p of dimension 1. Consequently the "virtual dimension" of the tower is n − 1 + 1 = n. That is, the complex lim D_{X_k}[−n] is a *Λ-invertible* sheaf on X_∞ = U/Z_p.

**Sketch of why it should hold.** Each X_{k+1} → X_k is a Z/p-branched cover (Yang, BRW). Verdier duality for finite group quotients gives π_*D = D_{X_k} ⊗ Z_p[Z/p^k]^∨. Passing to the limit replaces Z_p[Z/p^k] by Λ, and continuous duality for the profinite group adds the shift [1] (Λ-dual = Ext^1_Λ(·, Λ)). The genuinely hard step is the **Mittag-Leffler / no-phantom condition**: the lim^1 terms of the system H^q_c(X_k) must vanish. I would prove this by the quantitative Newman theorem. A non-vanishing lim^1 requires classes that survive arbitrarily deep in the tower while their supports shrink to orbits of diameter → 0. Newman's ε (uniform over all nontrivial finite cyclic actions on U) forbids such classes from being supported in ε-balls. Making this precise via a Čech-cover argument on X_k is the step I cannot fully certify.

## How it contradicts faithfulness

1. **Invertibility ⇒ manifold-like local cohomology.** If lim D_{X_k}[−n] is Λ-invertible, take stalks at x ∈ X_∞. Then H^q(lim D)_x is Λ-free of rank 1 for q = −n and 0 otherwise. Taking Λ-coinvariants (⊗_Λ Z_p, i.e. setting T = 0) recovers the local cohomology of X_∞. Hence X_∞ is a cohomology (n − 1 + 1)-manifold over Z_p, so dim_{Z} X_∞ = n.

2. **Contradiction with Yang / Bredon–Raymond–Williams.** These give dim_Z X_∞ = n + 2. The two extra degrees come exactly from H^2(Z_p; Z) = Q_p/Z_p ≠ 0, which is the Bockstein of the nontrivial characters Z_p → Q_p/Z_p. In the Λ-language this is a nonzero μ-type torsion class: the module Λ/p^∞ contributes in degree shifted by 2. Invertibility rules out Λ-torsion in the dualizing complex, so μ = λ = 0 in the relevant degree. That contradicts BRW's computation, which forces a nonzero torsion class in degree n + 2.

3. Therefore no faithful Z_p action exists on U, hence none on M. By Gleason–Montgomery–Zippin–Yamabe, Hilbert–Smith follows.

## Why this is the right invariant

- It turns "the cohomological dimension jumps by 2" into an algebraic statement: the tower module has Λ-torsion with nonzero μ. That statement is local and functorial, and it is compatible with Verdier duality.
- The only analytic input is a uniform lim^1-vanishing. Newman's theorem is exactly a uniform smallness obstruction, so it is the natural candidate for supplying it.
- For n ≤ 3, the needed lim^1-vanishing can be checked by hand from the classification of surfaces and 3-manifold topology. That recovers Pardon's result and is a sanity test. In the Lipschitz and Hölder cases it follows from the Hausdorff-dimension bounds, which recovers Repovš–Ščepin and Maleshich.

**Honest gap:** The Mittag-Leffler step (lim^1 = 0 for H^*_c(X_k; Z_p) via quantitative Newman) carries all the difficulty. Without it, the invariant still detects the n + 2 jump but does not contradict it.
