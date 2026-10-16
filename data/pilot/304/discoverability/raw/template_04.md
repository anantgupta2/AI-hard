# Proposal: the Smith–Witt class of the orbit tower

## Setup
Suppose Z_p acts faithfully on M. Then it acts faithfully on M x R^j as well, so we may assume n = 4m. Write X_k = M/p^k Z_p, π_k : M → X_k and f_k : X_{k+1} → X_k. Each π_k is proper because orbits are compact. Put F = Rπ_{0*} F_p,M [n] on X_0.

Proper pushforward commutes with Verdier duality, and the cup-product pairing on M is symmetric (n = 4m). So F is a self-dual complex of F_p-sheaves on X_0 and defines a class [F] ∈ W(X_0; F_p), the Witt group of self-dual complexes of sheaves in Woolf's sense. Z_p acts on F through the finite quotients Z/p^k. Write g for a topological generator.

## The invariant
For each k, F is a module over A_k = F_p[Z/p^k] = F_p[t]/t^{p^k} with t = g − 1. A_k is uniserial, and the duality pairs t^i F with ann(t^i).

Definition: the k-th Smith–Witt sheaf is S_k = t^{r} F_k / t^{r+1} F_k, where
- F_k = R(f_0 ∘ ... ∘ f_{k-1})_* F_p,X_k-equivariant part, i.e. the summand of F on which p^k Z_p acts trivially,
- r = (p^k − 1)/2 for p odd.

For p = 2, use the analogous half-filtration together with the form ⟨a, b⟩ = (coefficient of 1 in a · ḡ b).

## Lemma (Smith–Witt reduction)
For each k:
1. t^{r+1} F_k is a sublagrangian of F_k with orthogonal complement t^{r} F_k. In the derived sense this uses the Smith exact triangles t^i F → F → F/t^i F (Bredon's sheaf-theoretic Smith theory).
2. Therefore [F_k] = [S_k] in W(X_0; F_p).
3. Multiplication by t^r induces an isomorphism S_k ≅ ρ_k := Smith special sheaf σ_k F_k. Here σ_k is the norm 1 + g + ... + g^{p^k − 1}, and σ_k F_k is the image of the transfer from X_k. On the locus where the stabilizer is contained in p^k Z_p, S_k is the constant sheaf F_p,X_0 [n].
4. Compatibility: the inclusions F_k ⊂ F_{k+1} induce [S_{k+1}] = [S_k] + (a class supported on the branch locus B_k = {stabilizer ⊄ p^{k+1} Z_p}).

### Proof sketch
Parts (1) and (2) are the standard sublagrangian reduction in a triangulated Witt group (Balmer). In A_k, the ideal t^{r+1} A_k is isotropic for the trace form, and its orthogonal is t^r A_k. Sheafifying works because every map is A_k-linear and the duality is A_k-semilinear.

Part (3): t^{p^k − 1} = σ_k in characteristic p. The middle layer of the uniserial filtration is identified, by powers of t, with the socle, which is the image of the norm. For a point whose orbit is free modulo p^k, the stalk of F_k is F_p[Z/p^k] ⊗ (local orientation), and its socle is rank one.

## How it yields the contradiction
1. **Choose a good point.** By Newman's theorem and a Baire argument, Fix(p^j Z_p) is nowhere dense for every j, so the set of points with trivial stabilizer is dense. Pick y ∈ X_0 whose orbit is free.
2. **Stalk comparison.** Near y, part (3) of the Lemma gives that S_k agrees with F_p[n] on a neighbourhood V_k of y. The total class [F] is independent of k, because F_k → F is an isomorphism on the stalk at y after inverting nothing: the free part is the colimit. Hence the local Witt invariant of [F] at y, namely the rank parity of the local cohomology H^*_y in W(F_p), equals that of F_p[n], which is 1 ≠ 0.
3. **Dimension clash.** Parts (2) and (3) also identify ρ_k = σ_k F with a self-dual complex. Its costalks therefore satisfy D ρ_k ≅ ρ_k[−n]. So F_p,X_0 is Verdier self-dual in degree n on the dense free locus, and by part (4) every correction is supported on B_k.

   Because B_k decreases to the trivial-stabilizer complement as k → ∞, passing to the derived limit (Stacks: derived colimits commute with Rπ_*) gives D(F_p,X_0) ≅ F_p,X_0 [n] on all of X_0. Then X_0 is an F_p-homology n-manifold and has cohomological dimension n over F_p.
4. **Conclusion.** Yang and Bredon–Raymond–Williams show that the effective Z_p quotient has integral cohomological dimension n + 2. Their argument shows the F_p-dimension is n + 1: the extra class comes exactly from the Bockstein of the Z/p deck group of X_1 → X_0. This contradicts step 3, so the action cannot be faithful.

## Why this is the right device
- The p-group signature divisibility (|G| divides the signature for free actions) is the finite-level shadow: in W(F_p) it reads [F_k] = [S_k].
- Rationally, the invariants split off by Haar averaging, and X_0 is a rational homology manifold, so there is no contradiction. The obstruction lives only at p, which is why the Witt group must be taken with F_p coefficients and Smith filtrations rather than Q-isotypic signatures.
- The new construction is the sheafified middle layer S_k of the augmentation filtration together with its compatibility across the tower. It plays the role of an extension variable: it is small (rank one) but carries the global self-duality down to the orbit space.

## Main gap to verify
Part (4) of the Lemma, the control of the branch-locus corrections in the limit, is where all the difficulty sits. It needs a uniform estimate, presumably from Newman's theorem: the B_k cannot shrink to the stabilizer locus without forcing small orbits.
