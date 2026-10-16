# Proposed device: the p-primary Witt class of the quotient tower

## Setup
Assume Z_p acts faithfully on a connected n-manifold M. For p = 2, replace the group by 2Z_2 ≅ Z_2, so the action may be taken orientation-preserving. Write G_k = p^k Z_p, X_k = M/G_k, π_k : M → X_k, and f_k : X_{k+1} → X_k for the Z/p quotient maps. Let X_∞ = M/Z_p = lim X_k. Set R = Z_(p) and Q_p-free K = Q.

Facts used:
- Each X_k is the quotient of M by a finite group, so it is a Z[1/p]-homology n-manifold. Over Z[1/p], Verdier duality on X_k is "perfect".
- All the failure is p-primary. By Yang, dim_Z X_∞ = n+2, while dim_{Z[1/p]} X_∞ = n, because averaging with Haar measure is available once p is inverted.

## Construction (Witt class of the defect sheaf)
Let D_k = cone(Z_(p),X_k[n] → ω_{X_k} ⊗ Z_(p)) ∈ D^b_c(X_k; Z_(p)). It is the defect of duality on X_k. Verdier duality turns D_k into a **(−1)^n-symmetric torsion object**: it is supported in p-power torsion, and D(D_k) ≅ D_k[n+1] compatibly with the swap. Following Woolf (Witt groups of sheaves) and Balmer's triangular Witt groups, define

  τ_k := [D_k, φ_k] ∈ W^{n+1}_{tors}(X_k) := W^{n+1}(D^b_{p-tors}(X_k; Z_(p))).

The sheaf form of the Gersten–Witt / 12-term localization sequence is

  W^n(X_k; Z_(p)) → W^n(X_k; Q) → W^{n+1}_{tors}(X_k) → W^{n+1}(X_k; Z_(p)).

In it, τ_k is the boundary of the Q-symmetric class of X_k, and that rational class exists because X_k is a rational homology manifold. So **τ_k = 0 if and only if the integral symmetric structure on X_k lifts**, which is the condition for X_k to be a Z_(p)-homology manifold.

## Key Lemma (transfer divisibility)
For every k, the Witt classes satisfy (f_k)_* τ_{k+1} = p · τ_k + (Smith term). The Smith term is supported on the fixed set of the deck group Z/p, and by Smith theory it has F_p-rank bounded independently of k. The proof proceeds in steps:
1. Use proper base change for the finite map f_k.
2. Use the transfer f_{k*} f_k^* = multiplication by p on the trivial isotypic part.
3. Use that the nontrivial isotypic part over Z_(p)[ζ_p] has trace form divisible by (1−ζ_p)^{p−1} ~ p.

Push everything to X_∞ along q_k : X_k → X_∞ (a proper map with profinite fibres). Then the classes t_k = q_{k*} τ_k form an inverse system in W_tors(X_∞), and it satisfies t_k ≡ p · t_{k+1} modulo a bounded subgroup.

## Contradiction with faithfulness
(a) **Bounded exponent.** Fix a relatively compact chart U ⊂ M and its image V ⊂ X_∞, and localize the Witt classes to V. The stalk Witt groups of torsion linking forms over Z_(p) sit in W(F_p) ⊕ (forms on Z/p^j). By semialgebraic local triviality (Hardt), the local cohomology of a chart has finite type, so the image of t_k in W_tors(V) lies in a finitely generated subgroup Γ of bounded exponent p^e. Γ is independent of k because the torsion of H^*(M; Z) on U is fixed. Combined with the lemma, t_0 is p^k-divisible in Γ modulo a bounded error for every k, so **t_0 = 0** (and likewise every t_k).

(b) **Non-vanishing (Newman + Yang).** Newman's theorem says that for every k, the subgroup G_k has orbits that leave U. Hence V meets a non-free orbit stratum of each Z/p deck group. At such a point, the Smith term in the lemma is a nonzero linking form on H^{(n+1)/2}-type local torsion. Its nonvanishing comes from the Bredon–Raymond–Williams computation H^{n+2}_c(V; Z) ≠ 0, which is p-primary and is exactly the boundary of the rational fundamental class in the localization sequence. Yang's dim_Z X_∞ = n+2 therefore says **lim t_k ≠ 0** in the derived limit. More precisely, the class lives in lim^1, because it is a phantom at each finite stage. This is detected definably, in the sense of Bergfalk–Lupini–Panagiotopoulos, from the tower of Witt groups.

Statements (a) and (b) contradict each other. The tower has finitely generated, bounded-exponent terms, so it is Mittag-Leffler, and therefore lim^1 = 0, which contradicts (b). So the action is not faithful.

## Why this is the right invariant
- Cohomological dimension alone (Yang) carries no form, so it cannot see the transfer by p.
- The Witt class encodes the symmetric (Poincaré) structure. Because of that, the deck-group transfer acts on it by multiplication by p, which is a quadratic phenomenon and not just a rank count.
- Ranicki–Weiss (topological invariance of L-classes) guarantees that τ_k depends only on the topology, so no smoothness or Lipschitz hypothesis is needed. This is the step that the Lipschitz, Hölder and quasiconformal proofs could not avoid.

The hard step is making the "Smith term bounded / nonzero" dichotomy precise for wild actions. My suggestion is to do it with derived colimits over semialgebraic approximating neighbourhoods, then apply proper base change at each finite stage.
