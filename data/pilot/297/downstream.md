# 297: Downstream targets for the selective bridge

**Item:** the paper's Thm na:bridge (bridge.tex:11-39), together with its analytic core: peak-transfer word decay, the peaking expectation and trace-null supports. The type is F3, an auxiliary construction inside a witness construction.

The construction adjoins a unitary v with v p_n¹ v\* = p_n² as Ueda's reduced HNN extension over D_i = C\*(p_n^i). The two peaking sequences (p_n¹), (p_n²) have matched traces strictly decreasing to 0. Three things then hold:
- every old pure state extends uniquely;
- exactly the two prescribed classes merge;
- the trace extends, and simplicity is kept.

**Method:** I read the Lean as text; it was not compiled. I traced the dependency chain by hand with grep. Web search worked for part of the session, but its index looks stale for Sep–Oct 2026.

## Part A: Is the item in the Lean?

**lean_status: formalized, different route.**

The bridge's construction and every one of its pure-state conclusions are proved:
- `PeakingPairData` (Peaking.lean:1046);
- `hnn_unique`, `hnn_join` and `hnn_no_unintended_join` (HNN.lean:1412/1416/1425);
- `hnn_simple` (HNN.lean:1778);
- `Endpoint.word_decay` (Peaking.lean:1823);
- `TracialStage.hnn` (Stages.lean:129).

**Gaps:**
- **Special case: simple bases only.** Every bridge theorem in Lean takes `IsSimpleCStar A`. The paper assumes only a faithful trace and no finite-dimensional irreps. Every use in 297 has a simple base, so the comparator is unaffected. Downstream uses with non-simple bases would need the Lean generalized.
- **Different model.** The amalgamated free product is built on a scalar ℓ² Fock space over atoms, not on Hilbert C\*-modules. Word decay is packaged through excision nets.
- **Amplified separation hypothesis.** `Separated` is stated for the M₂-amplified states. Lean derives it from the inequivalence of the original states.
- **The comparator is exact, and KOS is not a black box.** `main` matches Thm na:main verbatim, and KOS homogeneity is re-proved in Lean (Operators.lean:927).

**Comparator chain.**
- Successor-step branch: `main` → `fullTower_pure_reference_unconditional` → `recursiveTower_treated_unconditional` → `exists_joining_successor_unconditional` → `TracialStage.hnn` / `hnn_reference_join` → `hnn_join` + `hnn_unique` → `corner_unique` → `Endpoint.unique_matrix_extension` → `model_word_decay` → **`Endpoint.word_decay`**.
- Countable-determination branch: `literal_countable_determination` → `dependency_closed_pureUEP` → `omitted_endpoint_bridge` → `hnn_unique` / `hnn_no_unintended_join`.

The bridge is needed in both branches.

## Part B: Targets

### Speedup targets (known theorems)

| # | Target | How the bridge helps | Speedup | Lean |
|---|---|---|---|---|
| 1 | AW04 Cor. 3, tracial case: join two given states with unique extensions | Bridge + KOS gives it at once, with a stronger conclusion. Near-tautological, because this is the successor step | high | statable now |
| 2 | CH ⇒ a Naimark counterexample of density ℵ₁ (Tanaka 2026; CF22 Prop 8.3) | CF22 Prop 8.3 says a bridge-type class plus CH suffices, and the bridge supplies the class. This is same-problem reuse, and a corollary if Tanaka is in L | high (given Prop 8.3) | statable now (`Cardinal.continuum`) |
| 3 | AWW10 Thm 0.6: unique extension from C\*_r(F_S) to C\*_r(F_R) | The word-decay engine generalizes AWW's Lemma 0.2 | low-med | < 300 lines (define C\*_r) |
| 4 | Simplicity of reduced HNN extensions (Ueda 2008) | Already a clause of the bridge | low | statable now |

### Open or new problems

| Problem | Status | Match | Payoff / conf / difficulty | Lean |
|---|---|---|---|---|
| **In ZFC, a simple C\*-algebra with exactly m ≥ 2 irreducible representations** (CF22, under ◊^Cohen) | open in ZFC | Exactly the no-other-join clause. Inequivalence through limits is already in Lean (`pure_inequivalent_ordinal_chain`) | high / 0.5 / med | statable now; 297's Lean is the m=1 case |
| Vaccaro's trace simplices in ZFC (◊ in Vaccaro 2018/2020) | open in ZFC | The bridge keeps a faithful trace but prunes the trace space to θ-compatible traces | med-high / 0.3 / high | special cases statable now; general case < 300 lines |
| A nuclear Naimark counterexample in ZFC | open | The device is **expected to fail**: free-product structure kills nuclearity | high / 0.1 / high | needs major library |
| CF22 Q8.2: a global automorphism moving all pure states | open | The bridge sidesteps this question rather than answering it | low / 0.1 | statable now |
| Group analogue: a finitely presented infinite group with two conjugacy classes | open (not re-verified) | Same design, but nothing transfers back | none (listed as the design's origin) | statable now |

### Corollaries of the theorem (not reuse)

- Naimark's problem fails in ZFC (as Tanaka also shows).
- The AW04 and CF22 consistency results become consequences of the ZFC theorem.
- The counterexample has a faithful trace.

### Reuse in the release

- Inside 297, the bridge is used twice: in the successor step and inside T21.
- No other family uses it. There are no hits in CONTENTS.md and no Lean use outside `OAI/Analysis/Naimark`.
- Tanaka's route (outside the release) shares only the KOS-transported 2^{-n} projections.

### Negative controls

1. **Separable algebras or separably acting irreps** (Rosenberg; Glimm; CF22 Prop 7.2). Naimark's statement holds there, so no separable bridge iteration can reach a single class. This is a proved-false analogue.
2. **Density ℵ₁ under ¬CH.** It is independent of ZFC (AW04 Cor 7; Tanaka). A bridge recursion of length ω₁ must fail when 𝔠 > ℵ₁; this is why the recursion has length 𝔠⁺.
3. **Graph C\*-algebras.** Naimark's statement holds for them (Suri–Tomforde, arXiv:1708.04368).
4. **Nuclear targets** (e.g. Farah–Hirshberg-type constructions). Failure is expected here but not proved.

## Top 5 (Lean-usable first)

1. **Exactly m ≥ 2 irreducible representations, in ZFC.** This is a new witness built from the same design, which is the reuse that counts for a witness item. It uses exactly the bridge's new clause, and it is statable now.
2. **AW04 Cor. 3, tracial case.** Measurable, but near-tautological; use it to calibrate the harness.
3. **CH ⇒ density ℵ₁.** It tests whether the problem CF22 posed as Q8.1, plus the bridge, gives a short proof. This is same-problem reuse.
4. **Vaccaro's trace simplex in ZFC** (unique-trace or k-extreme-trace cases). This is where the design must genuinely stretch.
5. **AWW10 Thm 0.6.** It tests the word-decay core alone.

## Precedent

- **Same theorem:** Tanaka 2026 (2609.26930, 22 Sep, ChatGPT-developed) proves it by a different route with no HNN extension.
- **Earlier equivalent of the design — a downgrade, stated plainly:**
  - Higman–Neumann–Neumann (1949) iterate HNN extensions. Each step conjugates one prescribed pair and creates no other conjugacies (Britton/Collins), to make all elements of the same order conjugate. Osin (2010) has finitely generated groups with two conjugacy classes.
  - 297's recursion is the C\*-algebraic transcription of this template:
    - pure-state classes ↔ conjugacy classes;
    - `hnn_no_unintended_join` ↔ Collins' lemma.
  - Ueda's operator-algebraic HNN extension is the vehicle for the transfer, and Calderón–Farah Q8.1 had already asked for such an amalgamation. 297 does not cite HNN 1949.
  - **Effect on the grade:** under the strict rule, the design is transfer. What may remain new is the analytic core: unique extension of *every* old pure state via peak transfer, trace-null endpoints and the peaking expectation. The pressure on C1 is toward N2, and any N3 claim should be restricted to that core.
- **After 6 Oct 2026:** nothing found, but the search index looks stale.
