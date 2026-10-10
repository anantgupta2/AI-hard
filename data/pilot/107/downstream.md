# Family 107: downstream targets for the separation device and the profile (ω ≤ 9/4)

**Analyst:** DOWNSTREAM-TARGET agent, 2026-10-10.
**Method:** Lean was read at text level only. No lake, lean or comparator run by me, because another build was running in the workspace. Per the environment note, the orchestrator's comparator run on the main `MatrixMultiplication` config passes.
**Literature:** WebSearch summaries only. WebFetch was not used because arxiv.org is blocked here.
**Cones:** Cone sizes come from `data/items/107_lean.json` plus my own breadth-first search over each target.

## Item
This is one device cluster with two entries.
- **C1 (N3, F3).** Lossless separation of a shared tensor leg by an auxiliary Fourier or group tensor, keeping a dot product.
  - Character form: λ(T) ≥ e^{p_X H(q)} ∏ λ(T_i)^{q_i} for every spectral point.
  - M2 states the same device in Behrend-sphere form.
- **C2 (N3, F1).** The symmetrized profile P(a,b) on polynomial-multiplication tensors, with concavity, shifted tripling and the growth lemma.

## Part A: is it in the Lean? `lean_status` = **as in paper**
C1 and C2 are formalized line by line from M1, and both lie inside the cone of `complex_omega_le_nine_quarters`.

**Main chain:**
`complex_omega_le_nine_quarters` → `AuxiliarySeparation.omega_le_nine_quarters` → `exactRankExponent_le_nine_quarters` → `Character.exponent_sum_le_nine_quarters` → `meanExponent_le_three_quarters` → `toScalarProfile` → `convolutionProfile_tripling` → `Sector.convolution_tripling_tag` → **`Character.sharedFirst_tag`** → `integral_type_comparison` → **`Character.finiteSeparation_bound`** → `value_separationTarget_le`.

**Side branches:**
- **Concavity:** `convolution_concavity_tag` → `sharedFirst_tag`. This makes C1 a cut vertex.
- **Profile:** `toScalarProfile` → `convolutionProfile` → `symmetrizedProfile` → `sixfoldProduct`.
- **Growth:** `ScalarProfile.exponent_le_three_quarters`.
- **Duality:** `exists_detecting_character`.

**Sizes (text level):**

| Cone | Declarations | Lines |
|---|---|---|
| 9/4 target | 836 | ~7.6k |
| `sharedFirst_tag` sub-cone | 216 | ~1.9k |
| `finiteSeparation_bound` sub-cone | 155 | ~1.2k |
| Generic growth lemma | 44 | ~0.5k |
| Duality | 238 | ~2.6k |

**Gaps:**
- The topological form `finiteSeparation_degeneratesTo` (Separation/Basic.lean:306) is **outside** the cone. The cone uses the algebraic polynomial-approximation form instead.
- The proof is over ℂ only, and it hard-codes `IsPrimitiveRoot ζ (5*M)`. A port to characteristic 5 therefore cannot reuse this step.
- Duality goes through App. A, which uses the external Brouwer package. `exists_detecting_character` is specialised to matrix multiplication. A version for an arbitrary tensor needs about 100–250 more lines.
- The M2 Behrend form (`Foundation.Separation.exists_modular_separation`) is a separate development. It sits in the α, rectangular and 2.267 cones (α cone: 1,239 decls / ~11.4k lines). The all-field 2.371 cone uses neither form.
- M2's elementary bound 9·log3/log75 ≈ 2.29011 from CW₁ is **not formalized**. Note that this is slightly above the "2.2901" quoted in family.md.

## Rules for building the arms
Every ω bound above 9/4 is a corollary of the headline. For such targets, remove these from **both** arms:
- the headline chain;
- `toScalarProfile` and the profile conclusion;
- the release's other ω results: the 2.267 bound, MatrixFields' 2.371, and the rectangular and α results whenever they imply the target.

The "with" arm then differs from the "without" arm only by the C1 declarations, and optionally C2. The full lists are in `lean_library_arms_common`.

## Speedup targets (known theorems)

| id | target | Lean statement | Baseline formal proof | speedup |
|---|---|---|---|---|
| S1 | CW bound from CW₁ via C1 | `Arithmetic.omega ℂ < 2376/1000` (variant: `< 22902/10000`) | MatrixFields laser proof (cone ~144k decl-lines); ℂ 2.267 M2-form proof (~7.3k) | high |
| S2 | α > 0.321334 (VXXZ 2024) via the M2 separator | `321334/1000000 < Arithmetic.complexAlpha` | OAI `alpha_gt` (0.465), ~11.4k decl-lines | med |
| S3 | R̃(cw₂) < 3.931 (Alman–Li, CCC 2026) | `∃ n ≥ 1, (exactRank (Tensor.power (smallCW 2) n) : ℝ) < (3931/1000)^n` | none | med |
| S4 | R̃(T) below d^{2ω/3} for all d×d×d tensors (Alman–Li) | as S3, quantified over T | none | low |

**Arms for S1.**
- *With item:* spectral infrastructure, the C1 declarations, and CW₁ (`ComplexCoppersmithWinograd.tensor`, border rank 3).
- *Without item:* the same library minus C1 and minus `Separation/*.lean`.

**Arms for S2.** α is **not** implied by ω ≤ 9/4, so the headline may stay in the library.
- *Remove from both arms:* `Duality/ExponentBound` and `ExponentConsumer`.
- *With item:* keep `Separation/*.lean`.
- *Without item:* remove `Separation/*.lean`.

**S3 and S4.**
- The statement needs a 15-line `smallCW` definition.
- The proof needs generalized detecting characters.
- **Caveat:** if Alman–Li plus ω ≤ 9/4 already implies the bound, then it is a corollary, and the headline must be removed from both arms.

## Open problems

| id | problem | Lean | payoff / conf |
|---|---|---|---|
| O1 | ω_F ≤ 9/4 for every field (char p) | statable now: `∀ F [Field F], MatrixAllFields…omega F ≤ 9/4` | high / med |
| O2 | ω < 9/4 with a new profile family | statable now | very high / low |
| O3 | α > 5/8 (past the CW-based 0.625 barrier, CLLZ 2025) | statable now | high / low |
| O4 | R̃(cw₂) < 3.5, toward q+1 | < 300 lines | high / low |
| O5 | Asymptotic rank conjecture for explicit tight tensors | < 300 lines | very high / low |

## Corollaries of the theorem (not reuse)
- All ω bounds above 9/4.
- ω ≤ 9/4 in characteristic 0.
- ω(1,2,1) ≤ 3.25, which beats Le Gall–Urrutia's 3.2516.
- R̃(T) ≤ d^{3/2}.
- Inversion and determinant in O(n^{9/4+ε}).
- ω_p ≤ 9/4+ε for all but finitely many p. This one is my own reasoning.

## Negative controls
1. **Alman 2019 universal-method barrier (2.16805).** Give the prover CW_q plus C1 only and ask for ω < 2.168. It must fail. M1 escapes this barrier only through C(a,b).
2. **Cap-set upper bound.** C1 can only lower-bound spectral points, and it works over ℂ, not 𝔽₃. Mathlib has no cap-set file.
3. **R(⟨2,2,2⟩) = 7.** Characters only see asymptotic quantities, so they cannot prove this exact rank.

The AFLG 2.3078 barrier is **not** a valid control, because C1 lies outside zeroing-out laser analyses.

## Top 5 (all Lean-usable)
1. **S1:** CW-level bound from CW₁ with C1 only. Two formal baselines exist.
2. **S2:** α > 0.3213 through the M2 form. The headline can stay in the library.
3. **O1:** every-field 9/4. The concrete obstacle is characteristic 5.
4. **S3:** cw₂ asymptotic rank < 3.931.
5. **O2/O3:** ω < 9/4 or α > 5/8 with a new profile.

## Precedent
- No earlier equivalent was found.
- The closest neighbour is Alman–Li 2026, "Strassen calculus".
- No use of the device after the release was found. Coverage is press only, plus one forum post saying the ℂ comparator passes.
