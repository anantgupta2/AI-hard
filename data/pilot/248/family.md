# Family 248: "Thompson's group F is nonamenable" (paper + Lean analyst)

Source: `preprints/Thompsons-group-F-is-nonamenable-September-23-2026/build/` (main.tex → introduction, finite-proof, consequences, appendix auxiliary, figure mixed-pairs) and `lean/OAI/GroupTheory/Thompson/` (68 files, 9457 lines) at commit fd4aeeb. Full item list: `family.json` (49 items: 44 from the paper, 5 Lean-only clusters). There is no reasoning trace for this family.

## 1. Main statement
**Thm main** (introduction.tex:37): *"Thompson's group F is not amenable."* Amenability means a positive, normalized, left-invariant mean on ℓ∞(F;ℝ) (introduction.tex:9-13). This confirms Geoghegan's 1979 conjecture.

The real content is **Prop avg:boundary** (finite-proof.tex:194). A finite set S ⊂ F, fixed in advance, satisfies, for every nonempty finite A,
max_{h∈S} |hA△A|/|A| ≥ (δ²/L² − 4/D)/(4(1−1/D)) > 0.
This is uniform failure of the Følner condition with an explicit constant.

**Comparator** (`ComparatorChallenges/ThompsonNonamenability.lean:78`, target `thompson_F_nonamenable_composition`): there is a `Group F` whose multiplication is composition, and `¬ Nonempty (InvariantMean F)`.
- `F` is the set of increasing self-homeomorphisms of [0,1] with finitely many dyadic knots and slopes 2^e.
- `InvariantMean` is a positive ℝ-linear map on `lp (fun _ => ℝ) ∞` with `M 1 = 1` and `M (f(h·)) = M f`.
- The challenge definitions are textually identical to `Model.lean` (checked by diff).
- `StandardCharacterization.lean` separately proves that the model equals the textbook finite-breakpoint definition.
- **Match: exact.** The composition clause pins down the group structure, so the existential over `Group F` is harmless.

What is formalized beyond the comparator:
- the explicit-constant proposition (`Main.lean:16`, `:38`, `:45`);
- a generic core theorem, `exists_fixed_boundary` (FiniteBoundary.lean:16), which works for any Hilbert space and any displacement map.

The two corollaries are not formalized.

**Route differences** between Lean and the paper:
- The paper *cites* the forward Følner criterion; Lean *re-proves* it, using Hahn–Banach separation (Day) and then a finite coarea/layer-cake argument (Namioka).
- Lean constructs the Benyamini–Sternfeld map completely, following the appendix.
- Lean places the parent intervals at depth 2D with index 2i+1, where the paper uses depth r with 2^r > 2D.

## 2. Trust surface
Over all 68 files:
- 0 each of `sorry`, `axiom`, `admit` (one grep hit is the English word in a docstring), `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque` and `set_option`.
- 14 `decide` lines, all on literals such as `0<2`.
- Imports are Mathlib only, with no other OAI directories and no external packages.
- The comparator's permitted axioms are propext, Quot.sound and Classical.choice. `Classical.choose` is used to pick the transports.

Caveats:
- I did not reproduce the build, since Lean is not installed.
- `enable_nanoda=false`, so no second kernel check is configured.

## 3. Labels
| Axis | Label | Evidence | Conf. |
|---|---|---|---|
| A | **A5** (impossibility), explicit-rate flag set | "F is not amenable" (intro:38); explicit constant (finite-proof:197) | high |
| B | **B1**. Full only with prior results: **no**. Adds corollaries: **yes** (Dixmier unitarizability for F; percolation p_c<p_u), both via OpenAI companion preprints | "We prove this conjecture." (intro:35) | high |
| C | **C1** primary (S and the constant are built explicitly). Secondaries: **C4** (inner-product estimation chain), **C3** (Følner contrapositive), **C5** (Følner cited without proof in the paper) | finite-proof:177-182, 298-305, 321-323 | medium (C1 vs C4) |
| C flags | computer-assisted: **no**. ih_strengthened: **no**, ih_template: none. The only induction is the well-founded *definition* of p by cell count | finite-proof:124 | high |
| D | **D3, provisional**: I19 (recursive coloring) is an N3 candidate | finite-proof:126-133 | medium |
| D flag | builds on a prior model-produced result: **no** for the theorem, **yes** for the two corollaries | consequences:22, 52 | high |

**E. Fields.**
- **Problem field:** group theory (MSC 20F65, 43A07, 20E08).
- **Lean-dir field:** GroupTheory.
- **Method fields:**
  - nonlinear functional analysis (Benyamini–Sternfeld, 46B20/47H10): *essential*, cited and re-proved;
  - amenability/Følner (43A07): *essential*, cited (re-proved in Lean);
  - elementary Hilbert geometry: *essential*;
  - dyadic partitions / PL combinatorics: *essential*;
  - curve/tube analysis: *essential*, appendix only;
  - Hahn–Banach convex analysis: *essential*, Lean only;
  - Ramsey theory (Moore), operator algebras (Haagerup–Olesen) and topology (Brown–Geoghegan): *background-cited*;
  - representation theory and percolation: *corollary-only*.
- **Cross-field share:** 1 of 4 invoked cited results (Benyamini–Sternfeld) comes from another field, and it is re-proved.

## 4. Proof architecture
1. **Setup.** Take a Lipschitz f on a Hilbert ball with ‖f(x)−x‖ ≥ δ. Explicitly: on L²([0,1];ℝ²), δ = 1/2. Choose D > 4L²/δ² and D separated internal dyadic parents I_1 < … < I_D.
2. **Recursive coloring** (the new object): p(T) = f(mean_j p(T_{I_j})) if the basic partition T respects every I_j, and 0 otherwise. Restrictions compose: (T_I)_J = T_{I·J}.
3. **Pull back to F:** X_I(g) = p((gT^(n))_I) for the D parents and D² descendants, with a zero extension. Then form the scalar correlations φ_{I,J} = ⟨X_I, X_J⟩.
4. **Compare correlations.** S consists of transports carrying each separated pair onto (I_1, I_2), and is fixed *before* A. One level n is then chosen for A∪SA. Exact covariance of normalized restrictions plus finite-average cancellation give: every separated-pair correlation average lies within η of a common α.
5. **Recursion step.** The recursion gives X_{I_i} = f(z_i). Because m is the mean of the f(z_i), Jensen and Lipschitz give δ² ≤ (L²/D) Σ‖z_i − m‖².
6. **Variance.** Nested (descendant–own-parent) pairs are only a 1/D fraction, and α cancels. So E‖z_i − m‖² ≤ 4/D + 4(1−1/D)η, which forces η ≥ (δ²/L² − 4/D)/(4(1−1/D)).
7. **Conclusion.** Uniform failure of Følner, hence F is nonamenable.

**Lean DAG share** (532 proof-DAG declarations):
- B–S map: 34%
- dyadic/PL plumbing: 30%
- the new core argument: 21%
- Følner re-proof: 10%
- model of F: 4%

`exists_fixed_boundary` dominates 51% of the DAG. The extractor's 20% proxy is uninformative here: `partitionColor` scores only 0.05, yet the proof cannot work without it.

## 5. Eureka candidates
**EC1. Recursive Hilbert-ball coloring p(T) (I19, pulled back as I23). Provisional N3, F1 (F3 flavour).**
- *For:*
  - It is a one-line definition found neither in the goal nor in L.
  - Once it is in place, a problem open for 47 years falls to about two pages of Hilbert-space algebra. That is the Cook–Reckhow profile: tiny, hard to find, and a huge drop in proof budget.
  - It turns approximate invariance of *scalar* averages into an approximate fixed point of a *nonlinear* map on an infinite-dimensional ball. The classical fixed-point characterizations of amenability (Day; Gheysens–Monod) concern affine actions.
  - It uses exactly what separates F from amenable affine or tree-automorphism groups: transports that change scale while placing two intervals independently.
  - Quick literature check, nearest neighbours: Moore 2013 (finite *scalar* tree colorings plus a convex Ramsey property), Akhmedov's height function, and Guba's diagram classes. None is recursive or vector-valued.
- *Against:*
  - Every ingredient is classical: B–S 1983, tree restriction, Følner. A judge may call it a clever combination (N2).
  - The pivot is about two steps from L: one needs both the recursion and the choice of a map with no approximate fixed point.

**EC2. Pair-exchangeability ⇒ concentration ⇒ approximate fixed point (I31 + I34; Lean `exists_fixed_boundary`). N2, or N3 only as a cluster with EC1.**
- *For:* the hinge is that m is both the parent mean and the mean of the f(z_i). The resulting Lean theorem is generic and reusable.
- *Against:* the computation is finite de Finetti / exchangeability style (Diaconis–Freedman) together with textbook Jensen.

**EC3. S fixed before A, a single level n chosen after A, and exact covariance (I25, I16, I28). N2.** This is standard Moore/tree-pair formalism, but it makes the comparisons exact.

**EC4. Nested pairs form a 1/D fraction (I33). N2.** This is elementary counting. It removes any need to control ancestor–descendant correlations.

**EC5. Explicit B–S map on L²([0,1];ℝ²) (I38–I44). N0 as a result, N1–N2 as a construction.** This is transfer, not eureka.

Taken together, EC1, EC2 and EC4 form one idea and should probably be scored as a single cluster, led by EC1.

## 6. Correctness audit (skeptical)
**Verdict:** I checked every step of §2 by hand and found **no gap**. The checks covered:
- covariance under hg = h∘g;
- the translation inequality with zero extension;
- the quantifier order (S before A, then n);
- well-foundedness of the recursion;
- the recursive identity;
- all separations;
- the three energy bounds and the cancellation of α (giving 4/D + 4(1−1/D)η);
- the Jensen/Lipschitz chain;
- the final constant;
- the worked example;
- the key appendix formula ‖γ'‖² = a'² + a²θ'²/3.

The Lean mirrors the paper step by step, is sorry-free, and has a faithful comparator. So, *if the build passes*, the result is machine-checked.

"Proves too much" tests, all passed:
- Amenable affine groups such as BS(1,2) cannot transport two intervals independently.
- Tree-automorphism groups (Grigorchuk, odometer full groups) cannot change depth.
- Finite-dimensional f is impossible by Brouwer, so the argument needs infinite dimension. This is consistent with the failure of scalar approaches.
- The argument implies that ⟨S⟩ is nonamenable for every choice of transports, which is consistent with the PL-subgroup structure theory.

Residual concerns:
- **The claim is extraordinary.** The problem has a history of failed or withdrawn proofs (Akhmedov 2013 v1, Shavgulidze 2009, Moore 2012), and this core argument is strikingly short. Expert review is still needed.
- The Lean build was not reproduced locally, and nanoda is off.
- A web search in Oct 2026 found no independent public confirmation or refutation.
- The corollaries rest on two unreviewed, model-produced companion preprints.

## 7. Extraction friction
- The decisive definition is a displayed recursion, not a Definition environment or an `\emph`. The core estimates are unnumbered paragraphs inside one proof.
- Only the headline is a theorem environment; the proposition carries the content.
- Joining paper and Lean by name fails: I_j in the paper versus `selectedInterval` (depth 2D) in Lean.
- The Følner re-proof exists only in Lean.
- DAG-share proxies over-weight the B–S appendix and under-weight the one-line coloring.
- Useful cue phrases:
  - "For completeness"
  - "The relevant covariance is exact"
  - "All choices so far, in particular S, are independent of the finite set to be tested"
  - "No condition is imposed on nested pairs"
