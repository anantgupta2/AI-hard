# 287 — Isomorphism of the free group factors: Lean analysis

Lean text only. Lean was not run. Corpus `openai/math@fd4aeeb`; full data in `lean.json`.

## What is formalized and what is claimed

**Comparator target:** `Interpolation.allInterpolatedIsomorphic`. For all r, s ∈ (1, ∞] there is a σ-weakly bicontinuous, trace-preserving *-isomorphism L(F_r) ≅ L(F_s).

- Taking r = 2, s = 3 gives the headline L(F₂) ≅ L(F₃). Taking r = ⊤ covers L(F_∞).
- The only hypotheses are 1 < r and 1 < s.
- The challenge file re-declares 28 statement definitions (plus 12 instances and an unused alias). They are textually identical to `FreeGroupFactor/Model.lean`, and the improved extractor's statement closure recovers exactly these 28.

**Definitions behind the statement:**
- L(G) is the bicommutant λ(G)″, with trace ⟨Tδₑ, δₑ⟩. The ultraweak topology is hand-built.
- For non-integer r, L(F_r) is **defined** as the normalised corner p(L(F₂) ⊗̄ B(ℓ²))p, where Tr(p) = 1/√(r−1) and p is chosen by Hilbert's ε.
- So Dykema's amplification formula is built into the definition rather than proven. This choice is faithful to the paper, but only by Dykema 1994, Thm 2.4.

**What is outside the comparator:**
- The **fundamental-group claim** (= ℝ_{>0}) is proven in the library (`allInterpolatedFundamentalGroups`, with a standard definition of the fundamental group) but is not compared.
- The **free-entropy-dimension corollary** is not formalized.
- Family 287 has **no entry in `formalization.yaml`**, although it is built (`OAI.lean`) and documented (`docs/287.md`).

**Where Lean's route differs from the paper's:**
- **The n = 2 step.** Lean proves L(F₂) ≅ L(F₃) directly, using a rank-two coefficient construction of about 1.8k lines. The paper instead derives it from the n = 3, 4 steps plus Dykema's formula.
- **The interpolated family.** Lean **re-proves** a Rădulescu-type theorem (t ∈ (0,1] lies in the fundamental group of L(F_∞)) using a weighted-Fock / free-Gaussian model of about 18k lines. The paper cites the classical dichotomy instead.
- **The small-cocycle lemma.** Lean uses an explicit alternating, Cesàro-averaged radial series. The paper uses Catalan moments and a spectral truncated inverse.
- **The generation step.** Lean uses a Baire-category lemma. The paper uses an explicit iteration.

## Trust surface

I grepped both directories (77 files, 26.8k lines):

- **Zero hits** for `axiom`, `sorry`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `set_option` and `#eval`/`macro`/`elab`.
- **22 `decide`** uses, all trivial kernel-checked side conditions.
- **Choice:** 2 `Classical.epsilon` (one of them in `selectedProjection`, inside the statement) and 1 explicit `Classical.choice`.
- **Comparator settings:** the permitted axioms are `propext`, `Quot.sound` and `Classical.choice`; `definition_names` is empty.
- **Imports:** `import Mathlib` only, with no external packages. The `patches/` directory touches third-party packages only.
- **Residual trust:** the comparator run itself, and the Dykema identification above.

## Proof architecture

1. `Interpolation.lean`. `Model.allIsomorphic` / `Model.toRankTwo`: every valid model is ≅ L(F₂).
2. `NormalTransport.lean`. `finiteRank_to_two` gives L(F_n) ≅ L(F₂) by induction. It uses `rankTwo` (FiniteRank) and `rankStep` (n ≥ 3, Generation).
3. `Positive.lean`. `rankTwo_allPositiveScaling`: every corner of M∞(F₂) is ≅ L(F₂). This is transported from `Scaling.lean`'s `infinite_hasCornerScaling` along L(F₂) ≅ L(F₃) ≅ L(F_∞). It rests on the weighted-Fock recognition chain and corner-equivalence files.
4. `FreeGroupFactor/Main.lean`. `rankThreeInfinite`.
5. **Each rank step** has three layers:
   - Find a generic, freely generating Haar tuple (`baire_local_approximation`, `normalTracialIso_of_haar_total`).
   - That tuple comes from `one_step`: a trace-preserving automorphism that nearly fixes the generators and makes some word approximate the extra generator.
   - `one_step` combines three things:
     - the **cocycle-driven polynomial Hamiltonian flow**: `PolynomialFlow.field`, `laurent_flow_automorphisms`, and the trace identity, Taylor and ODE files;
     - the **free-sum displacement bounds**;
     - the **small-cocycle lemma**: `smallCocycle` ← `Radial.exists_small_prefix_inverse` for n ≥ 3, and `smallCocycleTwo` for n = 2.

**DAG sizes:** the target's DAG has 2,294 declarations and 255k tokens. The classical interpolation branch `rankTwo_allPositiveScaling` **dominates 66%** of it. The novel `rankTwo` branch dominates 8%.

## Eureka-step candidates by Lean evidence

| # | Candidate | DAG share | Cheap compression (step 3b) | My grade hint |
|---|---|---|---|---|
| 1 | `Radial.averagedInverse` → `exists_small_prefix_inverse` → `smallCocycle` | 2.5% (def), 1.8% (lemma) | Def has depth 0, 1 copy per use, +0.1%. Lemma is used twice: one extra copy of its subproof, tree +11%, DAG +0. Additive. | N2–N3 (F3). This is a Lean-only explicit construction. |
| 2 | `PolynomialFlow.hamiltonian`/`field` → `laurent_flow_automorphisms` | 4.4% | Defs have depth 1, +1.2%. `one_step_from_laurent` is used 3×: tree +59%. In `FiniteActive.one_step` the subproof's tree/DAG ratio is 7.2. Mild constant-factor growth. | N2–N3 (F1/F5) |
| 3 | `freeCocycle` (cocycle rule) | 3.4% | +0.1%, additive | N0 (Fox derivatives / 1-cocycles) |
| 4 | `RankTwo.prefixHom`, `smallCocycleTwo` | 2.2% | Single use, so inline growth is 0. Dominates 7.9% of DAG tokens. | N2 (variant of #1) |
| 5 | `Generation.orbit` + `baire_local_approximation` | 1.9% | +0.4%, additive | N0 (transfer: Baire) |

**Does the 20% proxy agree with the compression estimate?**

- **Among definitions:** they agree with each other (Spearman 0.51 over 595 definitions), but for the wrong reason. Both reward type-level carriers.
  - All 19 definitions over 20% are Fock-space, coordinate-projection or ℓ² aliases.
  - `FreeFock.Hilbert` has nesting depth 22 and tree growth ×290, but only 17% shared (DAG) growth.
- **Among theorems:** the agreement is weak (ρ = 0.25).
- **On the novel items, both fail.** None exceeds 4.4% globally. Even inside the novel sub-DAG of `rankTwo`, they reach only 4–14%, and only the goal concept `groupVonNeumann` passes 20%.
- **Whole-library compression:** inlining every family lemma inflates the target ×412 (as a tree). Almost all of that sits in the classical Fock-space machinery: subproof tree/DAG ratios are 110–164 there, against 3.6 for `rankTwo`.
- **No novel item shows the multiplicative, PHP-style signature.** The novelty here sits in single-use bottleneck lemmas with shallow definitions.

## Fixing `extract_lean.py`

**Already done (v2, backward-compatible):** follows `import OAI.*`; parses one-space-indented declarations (606 had been dropped); cuts signatures at bracket depth 0; resolves names Lean-style (namespaces, `open`s, declaration order, fields, a context pass for field notation); builds a target-only DAG; computes dominator-tree `dominated_share`; flags plumbing by name/shape; excludes the target-statement closure; emits lemma candidates. 287 runs in about 3 s, and all seven other families processed without errors. `data/items/287_lean.json` was not overwritten.

**Still needed:**
1. **Rank lemmas by dominated share and dominated subproof tokens**, not by closure share. Definitions rarely dominate anything.
2. **Detect transfer subtrees** before computing shares: a lemma that dominates ≥25% of the DAG, joined to the LaTeX citations (here Rădulescu). Then recompute shares on the remainder.
3. **Separate carrier definitions** (Type-, Set- or Subalgebra-valued) from object definitions (vectors, words, maps). Rank only the objects.
4. **Make plumbing detection structural**, beyond the new name rules: bundling chains (`restrict → linearMap → proj`) and duplicate definitions (`LaurentApprox.value` = `UnitaryEvaluation.laurentValue`).
5. **Drop the 20% DAG-share threshold for lemmas.** Use "on every path to the target and not already in the goal" instead, then the expensive prover test.
