# Proposal: the local Iwasawa module of the orbit tower

**Caveat.** This statement is the Hilbert–Smith conjecture. It is open for n ≥ 4; Pardon proved n = 3. What follows is a concrete device with a reduction. One step (Lemma C) is not proved here, and I flag where.

## Construction

Let G = Z_p, G_k = p^k Z_p, X_k = M/G_k and X = X_0, with Λ = Z_p[[G]] ≅ Z_p[[T]]. Write ω_k = (1+T)^{p^k} − 1. Each q_k : X_{k+1} → X_k is a quotient by the finite group G_k/G_{k+1} ≅ Z/p, so it has a transfer tr_k on sheaf cohomology.

Free points: Newman's theorem says a nontrivial Z/p acting effectively on a connected manifold has a fixed set with empty interior. So M_free = {x : Stab(x) = 1} is a dense G_δ. Fix x ∈ M_free and let y_k be its image in X_k.

**Definition (local Iwasawa module).**
 L^i(x) := lim_{k, tr} H^i_{y_k}(X_k; Z_p),
the inverse limit, along transfers, of local cohomology at the image point. G/G_k acts on the k-th term. This makes L^*(x) a compact Λ-module, and L^* is a germ invariant of the action near the orbit Gx.

## Lemmas

**Lemma A (control).** RΓ_{y_k}(X_k; Z_p) ≅ RL(x) ⊗^L_Λ Λ/ω_k.

*Sketch.* Write π_k : M → X_k. Since G_k is compact, π_k is proper, so Rπ_{k*} = Rπ_{k!}. The sheaf π_{k*}Z_p is a constructible Λ/ω_k-module sheaf: its stalk at y_k is C(G_k x, Z_p) ≅ C(G_k, Z_p), the continuous functions on the fibre. The transfers form a Mittag-Leffler system of perfect Λ/ω_k-complexes. Base change for the tower then gives the formula, by the same argument as the Iwasawa control theorem for a Z_p-tower of spaces.

**Lemma B (where Yang's n+2 comes from).** Λ is a regular local ring of dimension 2, so every finitely generated Λ-module N has a dual filtration with layers Ext^j_Λ(N, Λ), j = 0, 1, 2. The j = 2 layer is the pseudo-null part (finite length, supported at (p, T)).

Combine three inputs:
- Verdier duality on M: M is a Z_p-homology n-manifold.
- Duality for proper pushforward: D Rπ_* = Rπ_* D.
- Lemma A.

Together they give RHom_Λ(RL(x), Λ) ≅ RL(x)[−n] up to a twist. Feeding this into the Bredon–Yang computation shows that cd_p X = n + 2 is equivalent to Ext^2_Λ(L^n(x), Λ) ≠ 0 for some free x. In words, **Yang's dimension jump is exactly a nonzero pseudo-null part of the local Iwasawa module.** If L^*(x) were Λ-free of rank 1 in degree n, Lemma A would make every X_k a Z_p-homology n-manifold near y_k. Then cd_p X = n, which contradicts Yang. So the conjecture is equivalent to:

**Lemma C (pseudo-null vanishing; the new input, unproved).** For x ∈ M_free, the pseudo-null submodule of L^n(x) is zero.

## Proposed proof of Lemma C

Suppose P ⊂ L^n(x) is pseudo-null and nonzero. Then P is finite, so ω_K P = 0 for some K. In other words, G_K acts trivially on P.

1. **Lift to a finite level.** By Lemma A, P injects into H^{n+2}_{y_k}(X_k; F_p) for all k ≥ K. G_K/G_{k} acts unipotently on the image, and this persists for all larger k.

2. **Smith theory at one step.** Apply Smith theory, with the Floyd and Borel inequalities on Σ dim H^*(·; F_p), to the Z/p-action of G_k/G_{k+1} on X_{k+1}. The fixed set is the image of points whose G_k-orbit is a single G_{k+1}-orbit. Near a free orbit that set is empty. For an action without fixed points, the Smith sequence makes the transfer tr_k injective on the invariants, multiplied by p. So tr_k ∘ q_k^* = p on P_k. Since P_k is p-torsion of bounded order, the transfers kill P_k after finitely many steps, and therefore P = lim P_k = 0.

3. **The gap.** Step 2 is the place where Newman's theorem must be used against "small orbits that are not uniformly small". The difficulty is that Smith theory applies to X_{k+1} only when it is finite-dimensional and locally p-acyclic, and X_{k+1} is not a manifold. The needed estimate is a **uniform** bound: Σ_i dim H^i_{y_k}(X_k; F_p) ≤ C(n), independent of k. That bound is what would make P finite and Mittag-Leffler at a single level.

A route to it:
- Use semialgebraic or sheaf-theoretic constructibility of π_{k*}F_p on a Čech nerve of mesh smaller than Newman's constant ε(M).
- Newman forces each G_k to move some point of every ε-ball by at least ε. This gives a Lusternik–Schnirelmann-type count of the nerve cells that a G_k-orbit must meet, bounded by the number of ε-balls, independently of k.
- That count bounds the local Betti numbers.

## Why this is the right invariant

It turns the global and quantitative statement "cd = n + 2" into the vanishing of a finite-length module at a point. That is a germ statement. Newman, a C^0 statement with uniform constants, is exactly the kind of input that can kill finite modules.

The analogy is Iwasawa theory, where "no finite submodules" is the standard bridge between control and duality. Here that is transfer of a known device (N0), not a jump. The new content would be the uniform local Betti bound in step 3.
