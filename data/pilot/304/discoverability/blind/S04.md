# Proposal: the local Iwasawa homology sheaf of the Z_p-tower and its torsion module

## Setup
Let Z_p act on M and suppose the action is faithful. Put M_k = M/p^k Z_p and X = M_0 = M/Z_p, with q_k : M_k -> X and the maps M_{k+1} -> M_k (deck group Z/p). Let Λ = F_p[[Z_p]] ≅ F_p[[T]], where T = γ - 1. This is a complete DVR.

## The invariant
Define a complex of sheaves of Λ-modules on X:

  𝓚 := R lim_k  R q_{k*} ω_{M_k},

where ω_{M_k} is the F_p-dualizing complex of M_k. Each R q_{k*} ω_{M_k} carries a Z/p^k = Z_p/p^k action, and the transition maps are traces. The limit is therefore a Λ-module complex. Its local homology at x ∈ X is

  H^Λ_i(x) := H^{-i}(i_x^! 𝓚),

a Λ-module. Call **τ(x)** the T-torsion submodule of H^Λ_{n+1}(x), and **μ(x)** := length of τ(x)/T. The proposed invariant is the function x ↦ τ(x), viewed as an Iwasawa module attached to the orbit over x.

## Lemma A (specialisation / Yang's dimension jump is T-torsion)
There is a derived Nakayama base change identity

  𝓚 ⊗^L_Λ F_p ≅ ω_X   (F_p coefficients).

*Sketch.* q_k is proper, so R q_{k*} = R q_{k!} commutes with Verdier duality. Taking coinvariants under Z_p/p^k recovers ω_X by Smith-type transfer: the norm map is an isomorphism away from p-torsion stabilisers, and the stabiliser contributions are handled stratum by stratum. Passing to the limit, Mittag-Leffler fails exactly by lim^1, and this produces Tor^Λ_1.

Consequently, the universal-coefficient sequence for Λ → F_p gives

  0 -> H^Λ_i(x)/T -> H_i(X, X-x; F_p) -> H^Λ_{i-1}(x)[T] -> 0.

By Yang / Bredon–Raymond–Williams, H_{n+2}(X, X-x; F_p) ≠ 0 for x in a dense set. The upstairs computation below forces H^Λ_{n+2}(x) = 0, so **τ(x) ≠ 0 there**. In other words, the non-manifold behaviour of X is exactly a nonzero torsion Iwasawa module in degree n+1.

## Lemma B (upstairs computation: H^Λ_*(x) is Λ-dual to the orbit's local homology)
Let C = π^{-1}(x) ⊂ M be the orbit. It is a point or a Cantor set ≅ Z_p/H. Then

  H^Λ_*(x) ≅ lim_U H_*(π^{-1}U, π^{-1}U − C; F_p),

with the Λ-structure coming from the Z_p-action. By Alexander duality in the manifold M, the inner groups are Čech groups Ȟ^{n-*}(C)^∨ for a closed set C. These are concentrated in degree n, where they equal F_p[[Z_p/H]], a cyclic Λ-module. The only way degree n+1 can appear is through the **non-stabilisation of the inverse system of invariant neighbourhoods**, i.e. through lim^1 over U. So τ(x) is a quotient of lim^1_U of the degree-n groups.

## Lemma C (the key new step: Newman forces lim^1 to be T-divisible, hence τ = 0)
Use Haar measure to build averaged neighbourhoods U_ε = Z_p·B_ε(y) for y ∈ C. Newman's theorem bounds the subgroups that can move points by less than ε: for small ε, p^{k(ε)}Z_p has an orbit of diameter > ε inside U_ε. On the degree-n groups this means that T^{p^{k}} = γ^{p^k} - 1 acts on the transition maps of the system {U_ε} as an **isomorphism up to an F_p-subspace of bounded rank**. Newman's constant depends only on the chart, so the bound is uniform in ε. The lim^1 of a tower of finitely generated Λ-modules on which a fixed power T^N acts surjectively up to bounded corank is a finite-length (pseudo-null) Λ-module. Since Λ is a DVR, a finite-length module killed by T^N with zero F_p-dimension growth vanishes. Hence τ(x) = 0.

## Contradiction
Lemma C gives τ(x) = 0 for every x. Lemma A gives τ(x) ≠ 0 on a dense set, as forced by Yang's cohomological dimension n+2. So no faithful action exists.

## Where the real work is
Lemma A is formal sheaf theory (proper base change, Verdier duality, Λ-adic limits à la Jannsen/Ekedahl). Lemma B is Alexander duality. The **load-bearing new ingredient is Lemma C**: a quantitative, Haar-averaged Newman estimate controlling the action of T on local homology towers. Its two delicate points are:
- uniformity of the bounded-corank constant in ε;
- the stabiliser strata where H ≠ 0.

For the strata, Smith theory gives that Fix(p^k Z_p) are F_p-homology manifolds of lower dimension, so an induction on dimension handles them. If the uniform estimate fails, one should still get τ(x) pseudo-null in a 2-variable refinement, using the tower in k and in ε together. That refinement would serve the same purpose.
