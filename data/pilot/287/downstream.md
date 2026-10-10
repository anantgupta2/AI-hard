# 287: Downstream targets for the small cocycle with a prescribed word value

**Item:** the paper's lem:small-cocycle (cocycle.tex:31-46), formalized in Lean as `OAI.FreeGroupFactorMain.smallCocycle` (SmallCocycle.lean:213). It is a lemma of type F3. In words: for n ≥ 3 and η > 0 there are a word w in F_n and a finitely supported real vector h with ‖h‖₂ < η such that the cocycle D with D_{x₁} = h and D_{x_j} = 0 (j ≥ 2) satisfies ‖D_w − δ_e‖₂ < η.

**Method:** I read the Lean as text; it was not compiled. I traced the dependency chains by hand with grep. Web search worked for part of the session, but its index looks stale for Sep–Oct 2026, so the post-release precedent check is inconclusive.

## Part A: Is the item in the Lean?

**lean_status: formalized, different route.**

The statement of `smallCocycle` is exactly the paper's lemma, and the word construction is the paper's: p_j = (a b₁)…(a b_j), b_j = x₂^j x₃ x₂^{−j}, w = p_m a. Only the analytic core is proved differently:

| | Paper | Lean |
|---|---|---|
| Inverse problem T_m h ≈ δ_e | Catalan moments. μ_m tends to (1/2π)√((4−x)/x) on (0,4), with no atom at 0, then a spectral cutoff inverse | An explicit alternating series of normalized odd shells (`Radial.partialInverse`) and its Cesàro mean (`Radial.averagedInverse`). Exact identities give ‖h‖² ≤ (N+1)/m and residual² = (m−1)/(m(N+1)) |
| Freeness of the prefixes | Reduced words plus a Nielsen pair φ/ψ | A semidirect-product witness FreeGroup ℤ ⋊ ℤ with a telescoping left inverse (`prefixHom_injective`) |

**Gaps that matter for the tests:**

1. **The headline instance bypasses the item.** In Lean, L(F₂) ≅ L(F₃) does not use `smallCocycle`. `finiteRank_to_two 3` goes through `rankTwo`, then `one_step_two`, then `smallCocycleTwo` (RankTwoCoefficients.lean:543).
   - `smallCocycleTwo` is a Lean-only rank-two variant of about 1.8k lines, and it reuses the Radial shells.
   - `smallCocycle` itself feeds `rankStep` (n ≥ 3) and `rankThreeInfinite` (via `FiniteActive.one_step`). Through those it feeds every n ≥ 4, infinite and non-integer model of the comparator.
   - So the comparator theorem does depend on the item (knockout), but the r=2, s=3 instance does not.
   - **Any hide-the-item run must hide `smallCocycle`, `smallCocycleTwo` and RadialCoefficients.lean together.**
2. **The absorption step has a clean interface.** `one_step_of_coefficient_estimate` (FiniteRank.lean:15) takes the small-cocycle property as a hypothesis for any n. That makes a clean boundary between the device and its consequence.
3. **The comparator is stronger than the headline, with a trusted definition.** `allInterpolatedIsomorphic` covers all r, s in (1, ∞]. But non-integer L(F_r) is *defined* by Dykema's corner formula, which is trusted rather than proved. The fundamental-group result is proved but not compared.

**Comparator chain** (main path):
`allInterpolatedIsomorphic` → `Model.allIsomorphic` → `Model.toRankTwo` → `finiteRank_to_two` → `rankStep` → `rank_step` → `generating_haar_tuple` (Baire) → `orbit_step` → `one_step` → **`smallCocycle`** → `cocycle_push_prefix_inverse` / `prefixHom_injective` → `Radial.exists_small_prefix_inverse` → `averagedInverse`.

There is a second path, `rankThreeInfinite` → `FiniteActive.one_step` → `smallCocycle`. The full chain with file:line references is in the JSON.

## Which version to use in the speedup test: the Lean version

- **As a library statement, the two versions are the same.** `smallCocycle` is verbatim the paper's lemma, so adding the statement to L does not depend on the route.
- **To test reuse of the *construction*, only the Lean route works in Lean.**
  - `Radial.exists_small_prefix_inverse` is a self-contained, group-only lemma about ℓ²(F_m): δ_e has a small approximate preimage under 1 + Σᵢ λ(xᵢ), given by explicit shell vectors.
  - The paper's route needs free-probability limits of spectral measures and Borel cutoffs. Mathlib d13f23b has none of this, so it would need a major new library.
- **Lean's elementary proof locates the eureka content.** Once the problem is posed, Lean solves it in about 800 lines of combinatorics. So the eureka content is in *posing* the coupled problem: a small generator coefficient and a prescribed word value, fed into the absorption flow.
- **Use three arms:**
  - (A) baseline L;
  - (B) L + the `smallCocycle` statement;
  - (C) L + `smallCocycle` + `exists_small_prefix_inverse` + `prefixHom_injective` + `cocycle_push_prefix_inverse`.
- **Discoverability (test 4)** should accept either proof.

## Part B: Targets

### Speedup targets (known theorems)

| # | Target | Current size | How the item helps | Speedup | Lean |
|---|---|---|---|---|---|
| 1 | `smallCocycleTwo`: the same lemma for F₂ (in-family, Lean-only) | 1,808 Lean lines | n=3 prefixes don't exist in F₂, since x₁x₂^j is not free. The rank-two proof pushes the same shells through an almost-injective prefix map. With the item and the Radial file given, only the near-freeness counting remains | med | statable now; formal proof exists |
| 2 | L(Γ∗ℤ) ≅ L(Γ∗F₂) for Γ ⊇ F₂, e.g. SL(3,ℤ) | none (new) | Device reuse *beyond* the theorem: free products are functorial, so 287 gives Q∗L(F₂) ≅ Q∗L(F₃) but not Q∗L(ℤ) ≅ Q∗L(F₂). The whole device appears to transfer, using b_j = s^j t s^{−j} in Γ | high if true (conf 0.4) | statable now (Mathlib `Monoid.Coprod`); about 400–900 lines of generalization |
| 3 | Akemann–Ostrand lower bound ‖Σλ(xᵢ)‖ ≥ 2√(m−1) (Amer. J. Math. 1976) | a few pages; no Lean | `sumShift_shell_succ` gives a bidiagonal Jacobi matrix with entries √(m−1) | med | statable now. **Sub-device control:** it measures the N0 shell calculus, not the item |
| 4 | Family 296's perturbation proposition | about 4 pp; Lean in FactorGeneration | Its first-order term is a cocycle value along free prefixes. 296 needs only a correlation; its hard part, the nonlinear remainder, is untouched | low | statable now; formal proof exists |
| 5 | Shlyakhtenko 2609.11074, Thm 3/4 (surface groups) | about 20 pp; no Lean | Weak: the target B is not free from (A, [A,B]), so a relation-compatible cocycle is needed | low | statable now (`PresentedGroup`) |
| 6 | H¹(F_n, ℓ²F_n) ≠ 0 (ceiling check) | trivial via the tree cocycle | Implied in two lines, but so it is without the item | ≈0 | statable now |

### Open or new problems

| Problem | Status | Match | Payoff / conf / difficulty | Lean |
|---|---|---|---|---|
| L(Γ∗ℤ) ≅ L(Γ∗F₂); more generally, when is L(Γ) ≅ L(Γ∗ℤ)? | new; check Dykema–Rădulescu 2000 | exact obstruction (absorb a free Haar generator) | med-high / 0.4 / med | statable now |
| de la Harpe–Voiculescu conjecture for Fuchsian groups with torsion (e.g. triangle groups) | open beyond Shlyakhtenko's Thm 1 | β₁⁽²⁾ > 0, but relators kill the one-generator cocycle | high / 0.25 / high | statable now |
| Is L^∞(U_N^+) a free group factor? (Brannan–Vergnioux 2018 settle only O_N^+) | open | β₁⁽²⁾ = 1, and free complexification supplies a Haar unitary | high / 0.15 / very high | needs major library |
| q-Gaussians Γ_q(ℝ^N) ≅ L(F_N) for large \|q\| (Guionnet–Shlyakhtenko 2014 covers small \|q\|) | open | Fox derivative ↔ free difference quotient | med / 0.15 / very high | needs major library |
| Free Araki–Woods factors: is the multiplicity of the continuous part an invariant? | open (not re-verified) | type III version of absorption; trivial centralizer blocks the flow | med-high / 0.1 / very high | needs major library |

### Corollaries of the theorem (not device reuse)

- All L(F_r) are isomorphic, with fundamental group ℝ_{>0}.
- δ₀, δ\* and β₁⁽²⁾ are not W\*-invariants.
- Shlyakhtenko's and Dykema's identifications all collapse to L(F₂).
- L(F_n) is singly generated.
- L(F₃) ≅ L(F_∞). Lean proves this directly with the device, which is in-family use only.

### Reuse inside the release

- **Inside 287:**
  - `smallCocycle` is used twice: in `one_step` and in `FiniteActive.one_step`.
  - The Radial shells are reused by `smallCocycleTwo`.
- **Family 296 (same date):** an independent sibling of the *design*. It spreads a perturbation of size α/√ℓ over ℓ occurrences of a unitary in a long word, gets a first-order correlation, and then applies Baire.
  - It does not reuse the lemma or its code; it imports only `FreeGroupFactor.Operators`.
- No other OAI file uses `freeCocycle` or `exists_small_prefix_inverse`.

### Negative controls

1. **C\*_r(F₂) ≇ C\*_r(F₃)** (Pimsner–Voiculescu). This is a proved-false analogue: the device must use a Borel logarithm and leave the C\*-world.
2. **Orbit equivalence and Cartan pairs.** F₂ and F₃ actions are never orbit equivalent (Gaboriau's cost). This is also a proved-false analogue.
3. **Groups with β₁⁽²⁾ = 0** (F₂×F₂, BS(2,3), SL(3,ℤ); also ℤ via the Dirichlet kernel). There the small-cocycle property fails, and L(Γ) is strongly 1-bounded (Shlyakhtenko 2021).
4. **L^∞(O_N^+)**: β₁⁽²⁾ = 0, and it is strongly 1-bounded (Brannan–Vergnioux).

## Top 5 (Lean-usable first)

1. **L(Γ∗ℤ) ≅ L(Γ∗F₂).** This is the only target where the device does work the theorem cannot. It is statable now. Check the literature first.
2. **`smallCocycleTwo`.** This is the most measurable target, with an existing 1.8k-line proof. It is in-family, so it calibrates the harness rather than confirming a jump.
3. **Akemann–Ostrand lower bound.** It separates reuse of the item from reuse of the N0 shell library.
4. **Fuchsian groups with torsion.** An open problem with the same obstruction; a stretch target.
5. **296's perturbation proposition.** A release sibling; expect low speedup.

## Precedent

- **No exact earlier equivalent of the prescribed-value statement was found.**
- **Design-level neighbours exist:**
  - Shlyakhtenko 2609.11074 (10 Sep 2026, model-assisted) uses the 1/√m amplification but has no cocycle.
  - Family 296 (23 Sep 2026) uses the same amplification along free prefixes, in correlation form.
- **What this means for the grade:**
  - The principle appeared at least three times in model-produced work within two weeks. That weakens the case that it is hard to find.
  - It does not remove the novelty of the exact statement.
- **After 6 Oct 2026:** nothing found, but the search index looks stale, so this check is inconclusive.
