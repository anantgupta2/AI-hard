# Proposal: the local p-adic transfer class and a duality-based contradiction

## Setup
Let G = Z_p act faithfully on M, G_k = p^k Z_p, X_k = M/G_k, π_k : M → X_k, and q_k : X_{k+1} → X_k (deck group Z/p). Fix a compact ball B ⊂ M. Because the action map is continuous and B is compact, for every ε there is k with diam(G_k·x) < ε uniformly on B. Newman's theorem says this smallness cannot hold *everywhere for every finite quotient*. What remains is to turn "uniformly small but not trivial" into an algebraic obstruction.

## The invariant
Work in D^b(X_k; Z). Orbits of π_k are compact, so Rπ_{k!} = Rπ_{k*}, and Verdier duality commutes with it:

 D_{X_k}(Rπ_{k*} Z_M) ≅ Rπ_{k*} ω_M ≅ Rπ_{k*} or_M[n].

The stalk of Rπ_{k*} Z_M at a free orbit is C(G_k, Z) = colim_j Z[G_k/G_{k+j}], an induced smooth module. So the comparison map

 c_k : Z_{X_k} → R Γ_cts(G_k, Rπ_{k*} Z_M)

is an isomorphism, and the cone of the dual map is governed by continuous cohomology of Z_p with discrete coefficients. Since H^2_cts(Z_p; Z) = Q_p/Z_p, this is exactly where Yang's n+2 comes from. **Definition (local transfer class).** For x ∈ X_k and a small invariant neighbourhood W = G_k·U, set

 τ_k(x) ∈ H^{-n-1}(D_{X_k} Z_{X_k})_x ⊗ ... ≅ lim_W H^{n+2}_c(W/G_k; Z) ≅ Q_p/Z_p   (nonzero by Yang/BRW).

Functorially, q_k^* τ_k = p·τ_{k+1}. This holds because the transfer along a Z/p cover multiplies the degree-2 class of Z_p by the index. So the local classes form a p-divisible tower. Its inverse limit over the transfers is a nonzero Z_p-module of "rank one", with the generator 1/p^k ∈ Q_p/Z_p realised at level k.

## Key Lemma (bounded-complexity sandwich)
Let B ⊂ B' be concentric balls with G_k·B ⊂ B' and W = G_k·B. Then the composite

 H^{n+2}_c(W/G_k; Z) → (via transfer tr_k) H^{n+2}_c(W; Z)^{?} → H^{n+2}_c(B'; Z)

factors through the cohomology of a *finite* semialgebraic (polyhedral) approximation P_k of the inclusion W ⊂ B', and the complexity of P_k is independent of k.

*Sketch.* Triangulate B' once and for all. Use the uniform smallness of G_k-orbits to approximate the action of a topological generator g_k = p^k by maps simplicially close to the identity on a fixed subdivision. The Haar-averaged (Čech) nerve of the cover {g·σ} is then a semialgebraic set of complexity at most C(B'), with C independent of k. Milnor–Thom / Basu–Pollack–Roy bounds then cap the order of the torsion in its cohomology that can be hit from H^*_c(W/G_k) at some N = N(B').

## Contradiction
1. By Newman, for every k some point x_k ∈ B has a G_k-orbit not contained in the Newman ball U. Equivalently, the class τ_k(x_k) is not killed by restriction to W/G_k for W ⊂ B'. This is the "non-triviality on a fixed scale" input.
2. Using the tower relation q_k^*τ_k = p·τ_{k+1}, the element detected at level k has order exactly p^k in the image of the sandwich map.
3. The Key Lemma says that image has exponent at most N(B'). If p^k > N we get a contradiction. So G_k acts trivially on B for large k.
4. Faithfulness fails locally. Since M is connected, invariance of domain together with the fact that a fixed-point set is closed spreads triviality on a ball to triviality of G_k on M. So G_k is in the kernel, which contradicts faithfulness. ∎

## Where the difficulty sits
Step 1 to 2 is the honest gap. Newman gives non-smallness of *some* orbit, and that has to be converted into a lower bound on the order of τ_k in the sandwich image. The proposed bridge is to read Newman's theorem cohomologically. Its standard proof, via Smith theory and a degree-one map to a sphere, is exactly a statement that a Z/p-transfer of the fundamental class is nonzero. Applied along q_k, it shows that each transfer step multiplies the order by p rather than killing it.

The structural point is that the unboundedly divisible Q_p/Z_p in the orbit-space dualising complex is forced to land in a fixed, finitely complex piece of M. Uniform continuity gives that finite piece, and Newman forbids the class from vanishing there.

This argument is a sketch, not a complete proof. The factorisation in the Key Lemma needs the approximation to be equivariant up to a controlled homotopy. In dimension 3 this is roughly the role of Pardon's linking-form argument. In higher dimensions, controlled topology (Chapman–Ferry α-approximation) is the natural tool.
