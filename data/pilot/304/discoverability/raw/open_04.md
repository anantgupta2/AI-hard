# Proposal: a Witt-valued character of the orbit tower ("p-adic equivariant sheaf signature")

## Setup
Let Z_p act faithfully on M^n. Assume M is oriented; otherwise pass to the orientation double cover, which Z_p preserves because Z_p is pro-p. Put X_k = M/p^kZ_p and X = M/Z_p = lim X_k, and let f: M -> X. Each X_k is the quotient of M by a finite group, so it is a **rational** homology n-manifold. Since f is proper (Z_p is compact), Rf_* = Rf_!, and Verdier duality gives

  D_X(Rf_* C_M) = Rf_* C_M[n].

Z_p acts on F = Rf_* C_M fibrewise by translation on the orbits, so F splits into isotypic pieces over the continuous characters chi: Z_p -> mu_{p^infty}:

  F = (direct sum over chi of F_chi), with F_1 = C_X, and D(F_chi) = conj(F_chi)[n].

So each F_chi is a Hermitian self-dual complex. It has a class

  w(chi) in W^n(Sh_c(X); C, conj)

in the Witt group of self-dual constructible-type complexes (Balmer's triangular Witt groups applied to Woolf's sheaf setting). By Ranicki–Weiss, it also has a local L-class L(F_chi) in H^{4*}(X; Q). The stalk rank of F_chi at x is 1 if chi kills Stab(x), and 0 otherwise. Faithfulness plus Newman's theorem make F_chi nonzero for characters of every order.

## Key lemma (small-subgroup Witt vanishing)
Let K be a compact saturated set, and suppose the subgroup p^mZ_p acts on a neighbourhood of K by maps homotopic to the identity through proper maps. Then for every chi of order greater than p^m,

  w(chi)|_K = 0 and L(F_chi)|_K = 0.

*Proof sketch.* The chi-component of the compactly supported intersection form on a saturated neighbourhood V is (1/p^k) Σ_{g in Z/p^k} chi(-g)·σ(g,V), where σ(g,V) is the g-twisted form (the G-signature construction, applied in Witt groups rather than to numbers). Write g = a + h with a in Z/p^m and h in p^mZ_p/p^k. Because h is homotopic to the identity, σ(a+h,V) = σ(a,V). The inner sum Σ_h chi(h) vanishes because chi is nontrivial on p^mZ_p. The same computation applies stalkwise over every open set, which gives the sheaf-level Witt class. ∎

By continuity of the action, for each compact K some m works.

## The contradiction
1. **Duality shift.** By Yang and Bredon–Raymond–Williams, integrally X has cohomological dimension n+2. The p-primary part of D_X(Z_X) therefore has a nonzero piece in degree -(n+2).
   - Model this with the solenoid Σ_p ⊃ Z_p: Y = M ×_{Z_p} Σ_p is an M-bundle over S^1, and X = Y/Σ_p.
   - The extra 2 comes from Ext(Z[1/p], Z) = Z_p/Z, a lim^1 ("phantom") term in the derived colimit over the tower X_k.
   - With Z_(p)-coefficients, F therefore carries a second, *shifted* self-duality D(F) ≅ F[n+2] on the phantom part.
   - Witt groups are 4-periodic and W^{n+2} = W^n with ε = -1. So the phantom part of F is both symmetric and skew-symmetric.
2. **Localization sequence.** Apply Balmer's 12-term localization sequence to the open set U = {x : |Stab x| ≤ p^m}, its closed complement Z, and the tower.
   - Over U the boundary map sends Σ_{ord chi > p^m} w(chi) into W^{n+1}(Z).
   - This class has two descriptions. One is the Witt class of the phantom term, read through the (n+2)-duality (step 1).
   - The other is the class that vanishes by the Lemma.
3. **Detection.** Reduce coefficients from Z_p[zeta_{p^k}] to the residue field F_p. W(F_p) detects rank mod 2 and the discriminant. The phantom term has stalk rank equal to the number of characters that are nontrivial on the stabilizer. Newman's theorem, read at a point where orbits are not uniformly small, makes this rank odd after the Galois-orbit normalisation (divide by p^{k-1}(p-1)). So the boundary class is nonzero. This contradicts the Lemma.

## Status / honest gap
- The Lemma is solid. It is a Witt-group upgrade of the G-signature averaging argument.
- The decisive unproved step is 1+3: that the lim^1 phantom part of Rf_*Z_(p) really carries an ε = -1 form, and that its class survives reduction to W(F_p).
- I expect the semialgebraic tools (Hardt triviality, Coste) to be needed only to put a stratification on X_k, so that the constructibility needed for Woolf's Witt groups holds.
- The new device is the **character-indexed Witt class w(chi) on the orbit space**, together with its small-subgroup vanishing. It converts Newman's "orbits are not uniformly small" into a nonvanishing Witt obstruction, and that obstruction must be killed by the duality shift n -> n+2.
