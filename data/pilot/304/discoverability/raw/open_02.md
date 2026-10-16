# Proposal: the p-residue of the orbit-space Witt class, and a transfer-kills-it lemma

## Reductions
Replace M by M x CP^2 x R^j, with Z_p acting only on the first factor. The action stays faithful, and dim M = n = 4m. For p = 2, pass to the orientation cover. A pro-p group preserves orientation, so we may assume M is oriented. Localize to a Z_p-invariant open set with compact closure, where Newman's theorem bites. Set Y_k = M/p^kZ_p, with π_k : M -> Y_k and the degree-p deck quotient q_k : Y_{k+1} -> Y_k.

## Construction (the invariant)
π_k is proper, so Verdier duality commutes with pushforward: D Rπ_{k*} Q_M[2m] ≅ Rπ_{k*} Q_M[2m].

By proper base change, the stalk at y is the space of locally constant functions on the Cantor-set orbit. p^kZ_p acts on these stalks. Averaging with Haar measure splits off the invariant summand Q_{Y_k}[2m], and that summand is Verdier self-dual. So **Y_k is a rational homology n-manifold**, and it carries a symmetric class

  σ_k ∈ W^0(Y_k; Q)

in Woolf's Witt group of self-dual complexes of sheaves.

Over Z_(p) the averaging is unavailable, because it divides by p. This is exactly where Yang/BRW's integral dimension n+2 lives. Consider Balmer's localization sequence for the triangulated Witt groups of sheaves on Y_k:

  W(Y_k; Z_(p)) -> W(Y_k; Q) --∂_p--> W(Y_k; F_p-torsion sheaves) -> ...

**Invariant:** τ_k := ∂_p σ_k. This is the p-residue, a Witt class of a self-dual torsion linking complex L_k. L_k is the p-primary torsion of the cone of the duality map Z_{Y_k}[n] -> D Z_{Y_k}. It is supported where the integral duality fails.

## Lemma A (nonvanishing, from Newman + Yang)
τ_k ≠ 0 for every k. More precisely, on a nonempty open set, its local stalk class in W(F_p) is nonzero.

*Sketch.* Integral cd(Y_k) = n+2 > n means the integral duality map has a nonzero p-torsion cone. The linking form on that cone comes from Poincaré duality on M. Pushed forward, it is the Z/p-equivariant linking pairing on Čech cohomology of the Cantor orbits. Newman's theorem says the subgroups p^kZ_p never have uniformly small orbits. That makes the linking form nondegenerate on a nonzero piece near a point, instead of hyperbolic (metabolic). This is the step I expect to need real work: one must show that the torsion form is *anisotropic*, not merely nonzero.

## Lemma B (naturality and transfer)
(i) τ_{k+1} = q_k^* τ_k. q_k is a Z/p quotient, so restriction along it preserves the orientation and duality data. The equality is checked on stalks via proper base change and the derived colimit description of H^*(Y_k) = colim over the tower.

(ii) τ_k = q_{k*} τ_{k+1}. The integral duality on Y_k is the Z/p-invariant part of the duality on Y_{k+1}. Its torsion defect is the norm/transfer image.

(iii) q_{k*} q_k^* acts on W(-; F_p) as multiplication by the Witt class of the trace form of F_p[Z/p]. That form is Tr(g^a g^b) = p·[a+b ≡ 0] = 0 over F_p. It is identically zero, so **q_{k*} q_k^* = 0** on F_p-Witt classes.

## The contradiction
By Lemma B, τ_k = q_{k*} τ_{k+1} = q_{k*} q_k^* τ_k = 0. Lemma A says τ_k ≠ 0. So the action cannot be faithful.

Proof-complexity analogy: τ_k plays the role of a Cook–Reckhow extension variable. It is a tiny object, a single residue class, that turns Smith theory's divisibility counting into a one-line cancellation.

## Supporting tools
- **Ranicki–Weiss / semialgebraic local triviality (Hardt).** Use these to show σ_k determines local L-classes. Hardt gives finitely many local models for the linking forms, which yields the anisotropy needed in Lemma A.
- **lim^1 control (Bergfalk–Lupini–Panagiotopoulos).** The jump from n to n+2 is a lim^1/phantom phenomenon in the tower. Definability keeps the τ_k compatible in the inverse limit, so that Lemma B(i) is not spoiled by phantom classes.

## Honest status
Lemma B(iii) is formal. B(i) and (ii) are routine but delicate, because they need sign and shift conventions in Woolf's setup.

All the depth sits in Lemma A, i.e. in proving that the residue is not metabolic. If it were only "nonzero in the derived category", the argument would fail: a hyperbolic torsion form also has residue 0. The proposal therefore reduces Hilbert–Smith to one local statement: **the Newman/Yang torsion linking form of a p-adic orbit is anisotropic over F_p.**
