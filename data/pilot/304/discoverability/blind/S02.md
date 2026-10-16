# Proposal: a uniform Newman constant along the Iwasawa tower of orbit spaces

**Setup.** Suppose Γ = Z_p acts faithfully on M. Let Γ_k = p^kΓ, X_k = M/Γ_k, and π_k : M → X_k. Each map q_k : X_{k+1} → X_k is the quotient by the deck group Γ_k/Γ_{k+1} ≅ Z/p, and M = lim X_k. After restricting to an invariant relatively compact open set and passing to some Γ_m, we may assume the action is free on an invariant open W with compact closure. Stabilizers are open subgroups or trivial, and the non-free set is closed and handled the same way by Smith theory. Write Λ = F_p[[Γ]] ≅ F_p[[T]].

## Lemma A (F_p-local structure of the tower)

On W, each X_k is an **F_p-cohomology (n+1)-manifold**, and the deck Z/p acts freely on it.

*Sketch.* Take a free orbit C = Γ·x, which is a Cantor set. Duality gives H^j_C(M; F_p) = 0 for j ≠ n, and H^n_C(M; F_p) ≅ H_0(C; F_p) = Λ, a free module of rank 1. Since cd_p Γ_k = 1, the Hochschild–Serre spectral sequence has only the columns a = 0, 1. It gives
- H^{n+a}_{y}(X_k) = H^a(Γ_k; Λ) at y = π_k(x), restricted to one point of C/Γ_k;
- H^0 vanishes, because T^{p^k} is a non-zero-divisor;
- the coinvariants contribute one copy of F_p per point of C/Γ_k.

So the local cohomology of X_k is F_p in degree n+1 and zero elsewhere.

Integrally, the same computation gives H^2(Γ; Z) = Q_p/Z_p. This recovers the Yang/Bredon–Raymond–Williams dimension n+2 and serves as a consistency check. The same spectral sequence shows that χ_c vanishes for free actions with finite cohomology. That is a cheap sanity invariant, but it is not the contradiction.

## Key new invariant: the Newman modulus of a cohomology manifold

For an F_p-cohomology manifold Y and a compact K ⊂ Y, define the **homological local-connectivity modulus**

  φ_{Y,K}(ε) = sup{ δ ≤ ε : for all y ∈ K, the map H̃^*(B(y,ε); F_p) → H̃^*(B(y,δ); F_p) is zero }.

Dress's proof of Newman's theorem (Bredon, *Sheaf Theory*, Ch. V) is effective. It produces a constant ν > 0, depending **only** on the dimension and the function φ_{Y,K}, such that every free Z/p action on Y whose orbits meet K has some orbit of diameter ≥ ν.

## Lemma B (uniform modulus, the main lemma to prove)

Give M a Γ-invariant metric by Haar averaging, d(x,y) = ∫ d_0(gx, gy) dg, and give each X_k the quotient (Hausdorff) metric. Then the moduli φ_{X_k, π_k(K)} are bounded below by a function φ that does **not depend on k**.

*Why this is plausible and how to attack it.* The maps π_k are 1-Lipschitz, open and Γ_k-equivariant, and their fibres are Cantor sets, which are cohomologically trivial in positive degrees. By Vietoris–Begle with supports:
- a Čech class on a small ball B_{X_k}(y,δ) pulls back to a class on the invariant tube π_k^{-1}(B), which is the Γ_k-saturation of B_M(x,δ);
- the spectral sequence (only two columns) splits this into Γ_k-invariants and Γ_k-coinvariants of the cohomology of tubes in M;
- the column a = 0 is controlled directly by the local contractibility modulus of M;
- the column a = 1 (the "transfer" or Bockstein part) is controlled by the norm element N_k = Σ_{g ∈ Γ/Γ_k} g. On a tube of diameter < ε, Γ_k acts by maps ε-close to the identity, so for p^k ≫ 0 it acts unipotently and compatibly with restriction.

The technical core is to show that the vanishing radius δ for the a = 1 column can be chosen uniformly, using only the modulus of M and the uniform equicontinuity of the action. This is exactly where "small orbits" must turn into "small cohomology".

## Contradiction

Fix a compact K ⊂ W. By Lemmas A and B together with the effective Newman theorem, for every k the free deck action of Z/p on X_{k+1} has an orbit meeting π_{k+1}(K) of diameter ≥ ν, where ν > 0 is independent of k. Such a deck orbit is the image of a Γ_k-orbit in M, and π_{k+1} is 1-Lipschitz, so some Γ_k-orbit meeting K has diameter ≥ ν. But Γ_k → {0} in Γ, and the action is jointly continuous on the compact Γ × K, so sup_{x∈K} diam(Γ_k·x) → 0 as k → ∞. This is a contradiction, so the action is not faithful.

## Why this device

Newman's theorem cannot be applied to Z_p directly, because Z_p has no finite subgroups. The tower X_k turns the problem into infinitely many **finite** Z/p problems on (n+1)-dimensional F_p-cohomology manifolds. All the difficulty then sits in one checkable statement, the k-uniformity of the local-connectivity modulus (Lemma B). In the Lipschitz and Hölder cases, the metric bounds on Hausdorff dimension (Repovš–Ščepin, Maleshich) supply this uniformity, which suggests Lemma B is the right general replacement.
