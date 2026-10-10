# Family 271: downstream targets for the SPLICE (loop weight 2)

**Item.** The splice is the contraction "set x_q = y_q = t and take the coefficient of t". Applied to the stable law symbol E∏(x_i + y_π(i)), it gives a stable symbol of the next-pin law weighted by 2^{#pin-free cycles}:
- a fixed point gives x_q + y_q = 2t, so a factor 2;
- a path i→q→j gives (x_i + t)(t + y_j), whose t-coefficient is x_i + y_j, so the path is spliced.

This is lem:pin-splicing of *Spontaneous magnetization in the quantum Heisenberg ferromagnet* (Sep 24, 2026). The stable permutation symbol it acts on is N0 (Borcea–Brändén) and is **not** the item.

**Type:** F5. Machine-readable version: `downstream.json`, with 15 verbatim Lean declarations.

## Part A: Is it in the Lean?

**lean_status: `as in paper`.** The splice, its action on permutation symbols, the proof that it preserves stability, and the cycle-weight bookkeeping are all formalized. They lie on the comparator's proof DAG. I worked at text level; the Lean was not compiled.

### Key declarations
All are in `OAI/MathematicalPhysics/Heisenberg/`.

| Decl | File:line |
|---|---|
| `splice` = `eraseNone (pderiv none (rename spliceVariables p))` | PinSplicing.lean:27 |
| `spliceWeight π = if π none = none then 2 else 1` | PinSplicing.lean:164 |
| `splice_permutationSymbol_fixed`: splice (permutationSymbol π) = 2 * permutationSymbol (removeNone π) | PinSplicing.lean:69 |
| `splice_permutationSymbol_nonfixed`: no factor | PinSplicing.lean:110 |
| `stable_splice` (via `stable_pderiv` and `stable_boundarySection`) | PinSplicing.lean:138 |
| `stable_spliced_law` | PinSplicing.lean:203 |
| `cycle_weight_splice` (2^{missing} factorizes) | PinSplicing.lean:417 |
| `pinLaw` and `stable_pinLaw` (induction that deletes one non-pin at a time) | StablePinLaw.lean:183, 218 |

### Comparator chain
The comparator is `ComparatorChallenges/Heisenberg.json`. I found the chain with a BFS over the `extract_lean.py` DAG:

1. `spontaneous_magnetization`
2. `ordered_state_exists`
3. `field_ordered_cubes`
4. `physical_surface_bound`
5. `symmetrized_surface_bound`
6. `completed_surface_bound`
7. `mesh_matrix_surface`
8. `mesh_surface_tail`
9. `mesh_pin_bound`
10. `finite_pin_induction`
11. `finite_simultaneous_pin_test`
12. `pinned_input_return_bound`
13. `stable_pinDensity`
14. `stable_pinLaw`
15. `stable_spliced_law`, together with `cycle_weight_splice`
16. `splice_lawSymbol`
17. `splice_permutationSymbol`
18. `splice_permutationSymbol_fixed` / `splice_permutationSymbol_nonfixed`
19. `splice`

The dominated share is small (0.013), but the splice cannot be bypassed: every pin-test path runs through it.

### Gaps
- **One vertex at a time.** The Lean deletes one non-pin per step, by strong induction on |V|. The paper deletes all non-pins at once. The two are equivalent.
- **Finite mixtures only.** The Lean works with finite mixtures (Fintype Ω). Poisson laws are handled by Hurwitz limits elsewhere (`PolynomialLimits.lean`).
- **Output extraction lives elsewhere.** G_T is in `stable_outputSymbol` / `stable_pinDensity`, not in `PinSplicing`.
- **Only the half-plane splice (B+C) is formalized.** The spherical companion's disk / A+D contraction is not in the Lean, and neither are the Bloch or lattice-correction companions.
- No docstrings.

## Precedent check (Asano, Suzuki–Fisher)

**Asano (1970).** The contraction maps A + Bz₁ + Cz₂ + Dz₁z₂ to A + Dz. It preserves zero-freeness in the disk (Lee–Yang) setting.

**Suzuki–Fisher (1971).** They apply it, after a Trotter mapping, to this very model. Contracting the layers is a qubit trace, so every closed loop gets weight 2.

**The splice is the half-plane sister of that contraction:** A + Bx + Cy + Dxy ↦ B + C. It is a composite of standard stability-preserving operations: diagonalization, a derivative, and a real specialization (Borcea–Brändén; Wagner's survey, Lemma 2.4). The Lean proof uses exactly these.

**Verdict.**
- **Earlier equivalent of the mechanism:** "contraction = trace = weight 2 per loop" already exists, in the zero-freeness form.
- **Not found anywhere:** using the splice to make the 2^{cycles}-weighted next-pin law *stable*, and hence BBL negative dependent.
- So the item is a **new bridge, not a new object. Recommend N2** (agreeing with f1).
- **After Oct 6:** no use outside the release.

## Part B: targets

### Speedup targets

| # | Target | Splice used? | Lean score | Speedup |
|---|---|---|---|---|
| S1 | Suzuki–Fisher Lee–Yang for the quantum Heisenberg model (SF71, 10–12 pp) | yes, but the disk variant | < 300 lines | med |
| S2 | Liggett / BBL negative correlation for SEP from a deterministic start | **no** (control) | statable now | high, but none of it due to the splice |
| S3 | S_k-shuffle SR projection (Nestoridi–Priestley–Schmid 2023, Cor. 3.6) | **no** (control) | statable now | med, not due to the splice |
| S4 | Asano's proof of the Ising Lee–Yang theorem | sister contraction (A+D) | < 300 lines | low |
| S5 | In-family positive control: `finite_simultaneous_pin_test` | yes | statable now | by construction |

### Open problems

| # | Problem | Status | Lean score | Confidence |
|---|---|---|---|---|
| O1 | Ueltschi θ=2 model with u ∈ (½,1): easy-plane XXZ ferromagnet, d ≥ 3 | open | < 300 | medium-low |
| O2 | Heisenberg ferromagnet on small-degree trees, nonamenable graphs, long-range couplings | open | < 300 (finite volume) | medium |
| O3 | Zero-free strips and algorithms for quantum Heisenberg (HMS 2019; Bravyi–Gosset) | partly open | < 300 | low-medium |
| O4 | PD(2) cycle law in Tóth's model | open | major library (no Poisson–Dirichlet) | low |
| O5 | Néel order without reflection positivity (bipartite) | open | < 300 | low |
| O6 | Weight-2 Lorentz mirror model for d ≥ 2 (Ryan 2026) | open | < 300 | low |

### Theorem corollaries (not reuse)
- The magnetization theorem itself.
- The three Oct 5 companions: Bloch's law, its lattice correction, the spherical law.
- The pin test on arbitrary finite graphs. The Lean statement is already graph-agnostic, so these are instances.

### Negative controls
1. **θ ≠ 2.** The weighted contraction forces a = b, and the doubled symbol for θ = 4 is unstable.
2. **θ = 1 (Tóth conjecture for d = 3, 4).** No stability-preserving contraction gives weight 1.
3. **Permanental / spatial permutations.** Their symbols are not stable.

## Top 5 (Lean-usable first)
1. **S1, Suzuki–Fisher via the contraction.** This is the only known theorem the contraction itself could shorten. The risk is that it shows reach toward the precedent, not novelty, and it needs a disk variant.
2. **O1, easy-plane XXZ.** The obstruction matches exactly. The stability half extends (Brauer symbol); the presence inequality for pairings is open.
3. **S2, exclusion negative correlation (control).** Statable now. It isolates the BB-symbol contribution from the splice's.
4. **O2, other transient graphs.** The splice transfers verbatim, but it is the same model.
5. **S3, S_k shuffle (control).**
