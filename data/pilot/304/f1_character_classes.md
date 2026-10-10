# F1 downstream-use report: family 304, integral character classes z_i(t)

**Items:** I42 (character classes), used with I49 (equal parts in a fixed lattice).
**Analyst grade:** N3, F1/F5, provisional.
**Lean:** none. Family 304 has no formalization, so there is no Lean counterpart to quote.
**Machine-readable version:** `f1_character_classes.json`.

## 1. The item

### Definition
Source: `sections/06-character-classes.tex:225-235`.

**Setting.**
- G = Z_p acts faithfully on W = O × R^{d−n} ⊂ R^d and preserves orientation. Here O is an invariant chart subset and d > n is odd, with d ≥ 3.
- The maps are c: S^d → W⁺ (collapse), q: W⁺ → Y = W⁺/G, and t: Y → X, a compact test.
- The point b_t = t(q(∞)) has contractible neighbourhoods.
- A_t = R(tqc)_* C_{S^d}, where C is the real plane with form Re(z w̄).
- α_t is the pushed-forward orientation form. [A_t, α_t] lies in E_d(X) = W_d(T(X)).

**Character projectors.**
- Off b_t, A_t is the pushforward of the orbit sheaf. The orbit sheaf splits over the characters Λ = μ_{p^∞}.
- A finite partition Λ = D_0 ⊔ … ⊔ D_{m−1} gives self-adjoint orthogonal projectors on A_t restricted to X∖b_t.
- These projectors become endomorphisms e_i of A_t in the Verdier quotient Q_U(X) = T(X)/T(U), where U is a contractible neighbourhood of b_t.

**The class.**

> z_i(t) ∈ E_d(X) is the unique class with ℓ_U(z_i(t)) = [A_t, α_t] + [A_t, α_t∘(2e_i − 1)]. Here ℓ_U : E_d(X) ≅ W_d(Q_U(X)) is the integral localization isomorphism. It holds because U is contractible and d is odd (`04-lattice.tex:487-529`).

**Properties.**
- The image of e_i is never formed. If e_i did split, the right-hand side would be twice the class of that summand.
- Σ_i z_i(t) = 2[A_t, α_t] integrally, via the explicit isometry S = Σ_j E_j P_j.
- The classes are covariant in the test, and homotopy invariant.
- On a test concentrated over p^k labelled sheets, the sheet multiplier β cycles the parts, so all z_i are equal.

**The I49 contradiction.**
- Fix L_d first, with im E_d(S^d) ⊂ L_d⁻¹ ℤ u_d.
- Take m = p^k > 4L_d. The m classes z_i(a) are integral and have equal rational images summing to 4u_d.
- So each equals (4/m)u_d, which lies outside the lattice.

### Obstruction dissolved
A faithful Z_p-action ought to be ruled out by a "Haar fraction": one degree-one class spread equally over p^k character parts. Three things block this classically:
1. **Wild orbit spaces.** The orbit space has cohomological dimension n+2 (Yang), so transfer, Euler-characteristic and Smith counts give no integers.
2. **Splitting loses integrality.** Isotypic splitting needs complex coefficients or dividing by |G|, and then integrality is gone.
3. **The bad point.** The splitting fails at the bad point b, and the stalks there are infinite-dimensional, so "the e_i-part" is not an object.

The device removes all three:
- Real Witt groups keep integrality.
- The reflection twist α(2e−1) needs only a self-adjoint idempotent on the existing object.
- Localizing at a contractible U and lifting integrally removes b.

### Abstract mechanism
Suppose a self-dual object is split into many parts by a symmetry only generically (off a contractible bad locus). Assign each part an integral class without splitting it off:
1. Add the form to its reflection-twist by 2e − 1. This gives twice the part.
2. Do this in the category localized at the bad locus, then lift back through an integral localization isomorphism.

The parts sum to a fixed integral total, and a cyclic symmetry permutes them, so each part is total/m. A lattice fixed before m forbids this once m is large.

## 2. Candidate downstream problems

| # | Problem | Status | Match | Payoff | Conf. / diff. |
|---|---|---|---|---|---|
| C1 | Generalized Hilbert–Smith for ENR **Z-homology manifolds** (Yang/Bredon setting; Dranishnikov arXiv:1504.07277) | Open | Exact: Yang shows the same n+2 wild-orbit obstruction. Off b, z_i only needs Verdier duality with orientation sheaf. Newman via Smith theory. A_t ∈ T(X) because an ENR source is a retract of a polyhedron, and T is closed under summands. | Resolves | low–med / high |
| C2 | Mj's QI-group theorem (Thm 2.24/Cor 2.25, arXiv:0906.4243) and pattern rigidity **without** dim_Haus < dim_t + 2 | Open without the hypothesis | Mj's hypothesis exists only because his integral obstruction is a Hausdorff-dimension count. Character classes are metric-free. ∂G of a PD hyperbolic group is a homology manifold (Bestvina). | Resolves, conditional on C1 | low / high |
| C3 | Local (pseudogroup) Hilbert–Smith; cf. Goldbring's local H5 (arXiv:0708.3871) | Unverified as a named problem | The device is entirely local: one chart, a pinch ball, a sheet region V, a compact test. | Resolves, probably routinely | med (ports) / low–med |
| C4 | Weak HS / BDH → Ageev chain (CDT arXiv:1612.09567; Williams–Dranishnikov K-theory programme) | Open before Oct 2026 | Theorem-level only. K-theory "infinite products" are the earlier parallel integrality device. | Corollary | high (conditional) |
| C5 | Lie-hypothesis removals: Conner–Raymond for compact groups; Khan's G-manifolds III (arXiv:1905.09977), "limited by" HS | Open for non-Lie groups | Theorem-level only | Corollaries | high (conditional) |
| C6 | Symplectic HS (Shelukhin arXiv:2403.07195) without asphericity | Partially solved | Floer power operations correspond to the per-character integral invariant | Removes hypotheses / swaps technology | high (conditional) |
| C7 | Integral isotypic signatures in Z_p-towers: L²-signature approximation, Levine–Tristram/Casson–Gordon at μ_{p^∞} | Various | Superficial: parts already split in towers, and there is no bad point or wild quotient | None found | low |
| C8 | Strong Atiyah conjecture (bounded denominators) | Open | Analogy only (fractional parts vs lattice) | None | low (superficial) |
| C9 | Rokhlin-property K-theory divisibility for Z_p / compact actions (Izumi; Gardella et al. arXiv:1802.01462) | Known | Same equal-parts shape: a **precedent** for I49, not a target | None | n/a |
| C10 | Explicit Newman-type theorem from the lattice L_d | Known (Newman) | The finite-group version of the averaged test works, but Newman is already stronger | None | high that it is useless |

### C1 adaptation sketch
1. Keep the sphere lattice unchanged.
2. Replace the collapse S^d → W⁺, which needs W open in R^d, with a compact ENR homology-manifold source that is a homeomorphism over the test support. Boundary effects sit over b and die in Q_U(X).
3. Get the pinch from Hopf's theorem, then Haar-average it as in Lemma averaged-test.
4. Run the z_i, equal-parts and lattice steps unchanged.

**Steps to check:**
- [A_a, α_a] = 2(aqc)_* u_d holds rationally for a homology-manifold source.
- The rational transfer and odd-sphere telescope go through. They use no manifold input.

**Caveat.** Mj (p. 3–4) states that the topological analogue of his theorem is "false … on homology manifolds", citing Raymond–Williams 1963. The Raymond–Williams/Levin spaces are 2-dimensional inverse-limit compacta (arXiv:1909.12660), not visibly homology manifolds, so the remark probably concerns general compacta. Check it before investing.

## 3. Reuse within the release
I grepped `CONTENTS.md` and every preprint `.tex` for Hilbert–Smith, Witt group, Balmer–Walter, Verdier, Newman, Smith theory and signature. **No other family uses this device.**

- **Other hits, unrelated:**
  - A passing "Witt groups" in the Finite Congruence Lattices family.
  - Smith theory in family 314, which works in chromatic homotopy.
- **Families that could consume the theorem, not the device:**
  - 246 (Cannon): with S² boundary, HS applies directly to QI groups.
  - 207 (Bass/Kaplansky idempotent traces): a thematic cousin only.

## 4. Held-out speedup targets
The device sits inside heavy machinery (non-constructible sheaf Witt groups, Balmer–Walter localization, the sphere lattice), so **no known theorem gets dramatically shorter**. The measurable targets are:

| # | Theorem | Reference | Lean? | Current size | Expected speedup |
|---|---|---|---|---|---|
| S1 | Reflection-twist identity: [V,b] + [V,b(2e−1)] = 2[eV]; partition sum = 2[V,b] (the algebraic kernel of the device) | 06:236-291; Hirzebruch–Zagier 1974 | Yes. Mathlib has bilinear/quadratic forms and isometries, but no Witt group as far as checked | ~½ page; est. 150–300 Lean lines | Small; a good "does the model find the trick" probe |
| S2 | Isotypic signature of a finite cyclic isometry group without dividing by \|G\| | Atiyah–Singer III; Hirzebruch–Zagier | Yes (Hermitian matrices, eigenspaces) | ~1 page | Small–moderate |
| S3 | HS for n ≤ 2 | Pardon arXiv:1811.08748 | No | a few pages | None or negative |
| S4 | HS for n = 3 | Pardon, JAMS 2013 | No | ~15–20 pp (est.) | Uniform replacement, not shorter |
| S5 | Lipschitz / QC / Hölder cases; Mj Thm 2.24 | Repovš–Ščepin 1997; Martin 1999; Maleshich 1997 | No | 5–10 pp each, plus Yang | Become corollaries; no standalone speedup |
| S6 | Symplectic HS | Shelukhin 2024 | No | tens of pages plus Floer theory | Swaps technology; fewer conceptual inputs |

## 5. Contamination and precedent
**Nothing found after Oct 6, 2026.** Searches for Hilbert–Smith together with Witt, signature, L-theory, 2026 or OpenAI returned only the standard literature: McAuley 2001 (never accepted), Pardon, Dranishnikov, Shelukhin, Mj and Levin.

**No earlier equivalent of the composite device was found.** Each component has a precedent, though:
- **The algebraic identity is classical.** Involution signatures give sign(V^±) = (sign b ± sign(T, M))/2.
- **Isotypic G-signatures and equivariant Witt groups are classical for finite groups.**
- **Sheaf Witt groups and localization** come from Balmer, Balmer–Walter and Woolf, all cited in the paper.
- **The equal-parts-in-a-lattice shape (I49) is classical.** It appears in Smith/transfer divisibility and in Rokhlin K-theory divisibility (Izumi). The closest earlier attempt to beat the Haar fraction with an integral invariant is Williams' K-theory programme for BZ_p, in K-theory rather than Witt theory.

**What is new** is the germ-level projector in a Verdier quotient, lifted through the odd-degree contractible localization isomorphism, applied to a profinite character decomposition with infinite-dimensional stalks.

**Verdict:** no downgrade to N0. N2 ("profinite, localized isotypic Witt class") is a defensible alternative to N3. The downstream evidence so far is mostly corollaries of the theorem. Only C1/C2 (and perhaps C3) would be genuine reuse of the device.

## 6. Top 5
1. **C1: HS for ENR homology manifolds.** This is the only target where the device itself does new work. Every ingredient has a homology-manifold analogue, and the summand-closed T built from arbitrary continuous maps is exactly what lets ENR sources in. The risks are replacing the global source and Mj's caveat.
2. **C2: Mj's theorems without the dimension hypothesis.** The metric hypothesis exists only to make a Hausdorff-dimension count work, and the Witt integrality is metric-free. This depends on C1 plus ANR regularity of ∂G. For S² boundaries (family 246) the 304 theorem already applies.
3. **C3: local Hilbert–Smith.** The construction is local by design and should port almost verbatim. It is cheap but may be routine, and its status as a recognised problem is unverified.
4. **C6: Shelukhin's symplectic HS without asphericity.** Witt classes replace Floer power operations. It is a clean comparison of technologies, but the gain comes through the theorem.
5. **C4/C5: weak HS and Lie-hypothesis removals.** These are real consequences documented in the literature, but they are theorem corollaries and should not count as device reuse.

## 7. Lean source
None. `catalog_families.csv` row 304 has has_lean_doc=False and empty lean_dirs, and formalization.yaml has no entry.

## Sources
- Paper: `data/raw/openai-math/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/build/sections/0{1,3,4,5,6}-*.tex`
- Pilot analysis: `data/pilot/304/family.{md,json}`
- arXiv: 0906.4243, 1504.07277, 1811.08748, 1612.09567, 1905.09977, 2403.07195, 1909.12660, 1910.01476, 1909.12648, math/0103145, 0708.3871, 1802.01462, 1809.08791, 2002.01206

The full search log is in the JSON.
