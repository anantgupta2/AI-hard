# Family 297: A ZFC counterexample to Naimark's problem

**Analyst:** family analyst (paper + Lean). No reasoning trace exists for this family.
**Sources:** `preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/build` (6 sections, 14 bib entries); `lean/OAI/Analysis/Naimark` (16 files, 25,931 lines, 2,104 declarations); comparator `lean/ComparatorChallenges/Naimark.{lean,json}`. Commit fd4aeeb.
**Base library L:** Mathlib d13f23b plus the 14 cited works. L includes one 2026 entry, **Tanaka2026** (arXiv:2609.26930). Tanaka2026 says its construction was developed predominantly by OpenAI ChatGPT.

## 1. Main statement

> There exists a unital infinite-dimensional simple complex C\*-algebra A with a faithful tracial state such that all its nonzero irreducible representations are unitarily equivalent. In particular, A is not isomorphic to K(H). (introduction.tex:10-15)

This answers Naimark's 1951 question negatively in ZFC. Akemann–Weaver (2004) needed ◊.

**Priority.** This is not the first ZFC answer. Tanaka2026 (22 Sep 2026, two days before this preprint) already gives a ZFC counterexample with a faithful trace. The paper concedes this: "the existence conclusion ... is already present there" (introduction.tex:49-50). It presents itself as an alternative proof by a different route.

**Lean.** The comparator target `OAI.NaimarkZFC.main` (Tracial.lean:243) matches Thm na:main exactly.
- The seven locked definitions in Basic.lean:11-43 are verbatim copies of the challenge file (checked with diff).
- `HasUniqueIrreducibleRepresentation` quantifies over Hilbert spaces in arbitrary universes.
- Everything the paper claims is formalized. That includes the cited Kishimoto–Ozawa–Sakai (KOS) theorem, which the Lean proves itself (`KOS.homogeneity`, Operators.lean:927).
- An earlier conditional `main_of_approxNearCentralRows` (Recursion.lean:2074) also survives. It assumed KOS as a hypothesis.
- **Catalog caveat:** `formalization.yaml` has no entry for this family, so the catalog shows `any_ms_formalized=False`. A complete formalization nonetheless exists, and `OAI.lean:159` imports it.

## 2. Trust surface
| check | count |
|---|---|
| sorry | 0 in solution (1 in the challenge stub) |
| axiom / admit / native_decide / implemented_by / extern / unsafe / opaque | 0 |
| set_option, #eval | 0 |
| plain `decide` | 8, all Bool/Fin trivia |
| imports | Mathlib only, plus the in-directory chain |

The permitted axioms are propext, Quot.sound and Classical.choice. Lean was not compiled here.

## 3. Labels
| Axis | Label | Evidence | Confidence |
|---|---|---|---|
| A | **A2** (existence of a counterexample) | introduction.tex:11 | high |
| B | **B2** (refutes the characterization). Flag: *not first resolution* (Tanaka2026). No prior partial result is used. | introduction.tex:7-8, 48-62 | high |
| C | **C1** primary. Secondaries: C2 (transfinite recursion and inductions), C4 (word-decay estimates), C5 (KOS, Kadison and Dini cited), C3 (minor). Computer-assisted: **no**. | construction.tex:43; iteration.tex:209-210; bridge.tex:113; construction.tex:18 | high |
| C2 flags | ih_strengthened = **yes**. Template: *carry an extra tracked quantity* (dependency sets I_j; the pair R_β ≅ H_j(O_β) / omitted-pair inequivalence). Secondary template: *strengthen to all substructures* ((U) for every dependency-closed sub-iteration). | iteration.tex:122-127, 191-219; Lean `ChronologicalHistory` | medium |
| D | **D3, provisional**, resting on T16 (the selective bridge) | bridge.tex:11-39 | medium-low (0.45) |
| Provenance | **partial**. Model-produced precedent (Tanaka2026, ChatGPT) for the existence result and for item I25. Nothing is imported. | introduction.tex:48-53 | high |

**E. Fields**
- **Problem field:** Operator algebras (46L05, 46L30; set-theoretic context 03E75).
- **Lean dir:** Analysis.
- **Method fields:**

| Method field | Tag |
|---|---|
| C\*-state theory (excision, unique extension) | essential |
| Free products and HNN extensions, Hilbert modules | essential |
| KOS homogeneity | essential; cited in the paper, re-proved in Lean |
| Kadison transitivity and GNS | essential |
| UHF/CAR algebras | essential |
| **Set theory** (c⁺, regular cardinals, bookkeeping) | essential |
| General topology (Dini) | essential, minor |
| Moment-norm formula | essential, minor |
| Prediction principles (◊, ◊_Cohen) | background-cited |
| Group-theoretic HNN | background-cited |
| Krylov/quasicentral averaging | essential in Lean only |

There are 3 essential cross-field imports outside operator algebras.

## 4. Proof architecture
1. **State tools.** Excision nets (AAP), projection excision, cross-excision (AW Lemma 1), trace-null supports (τ(r_h)=0), and the peaking expectation onto C(ℕ∪{∞}), with value h(a) at ∞.
2. **Reduced HNN adjunction (Ueda).** H(A) is built as the corner e₁(F \*_D G)e₁, with F=M₂(A), G=M₂(D₁), D=D₁⊕D₂. The section also proves an expectation onto A, uniqueness from reduced-word trace vanishing, and three closure properties: restriction, reordering (H_k H_j = H_j H_k) and limits.
3. **Selective bridge (T16).**
   - *Statement:* take two matched-trace peaking sequences for inequivalent f₁, f₂. Then every old pure state extends uniquely, and only [f₁] and [f₂] merge.
   - *Proof:* words decay under excision nets, via three ingredients:
     - the module bound ‖dP_G‖ ≤ ‖E(d\*d)‖^{1/2};
     - endpoint expectations, which vanish at the atoms (trace-null supports) and at ∞ (cross-excision), with Dini's theorem giving uniformity;
     - transfer of peaks through letters (P^ℓ b = b P^r), which exposes centered internal coefficients.
4. **Iteration.** The iteration starts from the CAR algebra and carries dependency sets I_j.
   - Dependency-closed sub-iterations are again bridge iterations.
   - **T21:** the inclusion A[S] ⊂ X_δ has (U). The proof postpones omitted steps (by reordering), and the bridge's no-other-join clause keeps omitted pairs apart.
5. **Countable determination (L22).** Every pure state is the unique extension of its pure restriction to a separable A[S]. Hence there are at most 𝔠 pure states at stages of size ≤ 𝔠.
6. **ZFC recursion of length 𝔠⁺.**
   - A fixed schedule σ assigns each pure state to a stage.
   - At each stage, KOS on the separable A[S] gives γ, and q_n = γ(p_n) has τ = 2^{-n}.
   - The bridge then joins the scheduled state to the reference class.
   - Regularity of 𝔠⁺ ensures every final pure state is caught.
7. **Conclusion.** There is one irreducible representation; A is simple, faithfully tracial, unital and infinite-dimensional, so A ≇ K(H).

## 5. Lean DAG and load
- **Lines by branch:**

  | Branch | Lines |
  |---|---|
  | State theory | 4.7k |
  | Amalgamation model | 4.5k |
  | Bridge decay (Peaking) | 2.4k |
  | HNN | 2.7k |
  | Reorder and limits | 1.7k |
  | Iteration, closed-subiteration, countable determination, recursion | 5.5k |
  | KOS re-proof and stages | 3.7k |
- **Dominated share** (substantive nodes):

  | Lean node | Item | Share |
  |---|---|---|
  | `countable_determination` | L22 | 0.153–0.156 |
  | `KOS.homogeneity` | Lean re-proof | 0.111 |
  | `dependency_closed_pureUEP` | T21 | 0.107 |
  | `omitted_endpoint_bridge` | T21 | 0.095 |
  | `word_decay` | I20 | 0.044 |

- The bridge's conclusions (`hnn_unique`, `hnn_join`) have share ≈ 0.001. They are used twice, in the successor step and in T21, so domination fails. Knockout is decisive here: removing T16 disconnects the whole recursion.
- **Lean route differences:**
  - The free product is built on a scalar ℓ² Fock space over atoms, not on Hilbert C\*-modules.
  - KOS is re-proved, using Krylov projection chains, near-central rows and an intertwining limit.
  - Faithfulness of the trace is derived from simplicity.

## 6. Items (45 total; full list in family.json)
| id | item | status | N |
|---|---|---|---|
| I05 | peaking sequence | new name, AAP-type notion | N1 |
| L07 | trace-null supports | folklore-level | N1 |
| L09 | peaking expectation onto C(ℕ∪∞) | new | N2 |
| P11/L12 | Ueda reduced HNN, amalgamated free product | cited, re-proved | N0 |
| P14 | reordering of adjunctions | new statement, corollary of multi-letter HNN | N1 |
| **T16 + I20** | **selective bridge + peak-transfer word decay** | new | **N3** (F3) |
| I14 | dependency sets / closure | new, Löwenheim–Skolem pattern | N1 |
| L20 | inherited sub-iterations | forcing analogue | N2 |
| **T21** | **closed-subiteration theorem** | new | **N2 (borderline N3)** |
| L22 | countable determination | AWW10 Prop 0.3 + T21 | N2 |
| I25 | q_n = γ(p_n) with matched traces | close variant in Tanaka2026 | N2 |
| T24 / I28 | KOS (cited) / Lean re-proof | known | N0 |
| T25 | c⁺ schedule recursion | bookkeeping | N2 |

## 7. Invoked external theorems
- **Cited, not re-proved:**
  - KOS03 Thm 1.1 (operator algebras; essential; re-proved in Lean);
  - Kadison 1957 transitivity (re-proved in Lean);
  - Dini's theorem (topology; proof recalled).
- **Cited and re-proved:** AAP86 Prop 2.2, AW04 Lemma 1, Ueda's HNN construction, Blanchard–Dykema.
- **Named as related but not used:** AWW10 Prop 2.3 / Remark 1, and CF22 Prop 7.2 (context only).

## 8. Eureka candidates (quick literature check)
1. **E1: selective bridge** (T16, I20, L09, L07). Provisional N3, F3.
   - *For:*
     - AW04 and FH17 join states with a crossed product by a global KOS automorphism. That needs separability and controls only the chosen states (AW04) or countably many (FH17).
     - CF22 Q8.2 (whether an automorphism can move every pure state off its class) is still open.
     - The bridge instead uses a partial isomorphism between two copies of C(ℕ∪∞). Its data are countable, so it works over nonseparable bases and gives (U) for all old pure states with a single join.
   - *Against:* CF22 §8 (in L) explicitly proposes an "amalgamation" / "partial crossed product" preserving unique extension (Q8.1). CF22 Prop 8.3 shows such a bridge suffices under CH. The direction was therefore posed. Ueda's HNN and AWW10's free-product unique-extension lemma are close ingredients.
   - *Searches:* none found that combine HNN or amalgamated free products with unique pure-state extension.
2. **E2: closed-subiteration theorem** (T21). Provisional N2, borderline N3.
   - *For:* no C\*-precedent was found.
   - *Against:* in set theory, sub-iterations over closed or adequate index sets are standard complete suborders (Judah–Shelah; Horowitz–Shelah 2302.08581). AWW10 Thm 0.6 covers the free-group special case. It is a strengthen-to-substructures template (cap N2).
3. **E3: countable determination plus the c⁺ schedule.** N2. Its pure-restriction half is AWW10 / AW04 Lemma 4.
4. **E4: peaking expectation.** N2.
5. **E5: q_n = γ(p_n).** N2. Tanaka2026 (model-produced) uses the same device.

## 9. Correctness and concerns
- **No gap found.** I checked all bridge cases (m=1, m=2 with two transfers, m≥3), the closed-subiteration bookkeeping (I_k ⊂ S∩k; no circular use) and the final catch argument.
- **Consistency with known results:**
  - AW04 Prop 6 (at least 2^ℵ₀ generators) is respected.
  - Rosenberg / CF22 Prop 7.2 is respected: the irreducible representation here is nonseparable.
  - The paper makes no density claim.
- **Residual concerns:**
  - Lean was not compiled here.
  - The paper relies on the cited KOS theorem (the Lean re-proves it).
  - There is a terminological tension in the literature. AW04 and CF22 say Rosenberg excludes "separably acting/represented" counterexamples, yet Tanaka2026 claims a "separably representable" one. The OpenAI paper reads Rosenberg as a statement about the irreducible representation. This bears on Tanaka2026, not on this theorem.

## 10. Extraction friction
- **No definition environments.** All twelve definitions are inline `\emph`. The bridge's core sits in `\emph`-titled paragraphs inside a proof.
- **Display-math objects.** Many objects are defined only in display math: P_G, ℓ(b)/r(b), O_β/R_β, I_j, σ.
- **Lean size and ranking.** At 25.9k lines this is the largest pilot so far. Dominated share ranks wrappers first and nearly zeroes the bridge, which is used twice.
- **Stale catalog flag.** `any_ms_formalized=False` is wrong for this family.
- **Unrelated name match.** An unrelated `OAI/InformationTheory/AmplitudeDamping/Naimark.lean` exists.
- **Lean naming history.** Suffixes such as `_unconditional` and `literal_` reflect development history.
