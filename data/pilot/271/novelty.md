# Family 271: novelty analysis ("Bloch's law, its lattice correction, and the spherical magnetization law")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

**Inputs.**
- `trace.json`/`.md`. The trace covers only the Sep 24 manuscript, *Spontaneous magnetization in the quantum Heisenberg ferromagnet*.
- There is no family, paper or Lean analysis, so I extracted the key items from that manuscript myself (`build/source/sections/00–07`).
- I read the three October 5 companions where they reuse those items.
- The Lean development at `lean/OAI/MathematicalPhysics/Heisenberg/` (128 files, 25,400 lines; target in `Main.lean`). I grepped it and computed import-DAG shares. I did not compile it.
- Web checks of arXiv pages and Wagner's survey (arXiv:0911.3569, Thm 3.4, Lemma 4.3 and Sec. 7, read from the extracted PDF).
- `f1_stable_permutation_symbol.*` was **not present** at writing time, so it is not used.

**L** = Mathlib d13f23b plus the 36-entry bib of the Sep 24 manuscript, which includes BBL 2009, Liggett 2009, DLM 2020 and Alon–Kozma 2013.
- Mathlib has no stable polynomials; the Lean development defines `Stable` itself.
- L does **not** contain Borcea–Brändén's symbol theorem (Invent. Math. 2009), Asano 1970, Suzuki–Fisher 1971 or Aizenman–Nachtergaele 1994.

## 1. Provenance verdict first: flag PARTIAL

**External: clean.** These are the 2025–2026 works cited anywhere in the family:

| Work | AI disclosure | Contains candidates? |
|---|---|---|
| Klippel, arXiv:2608.25506 (2026-08-26), cited in Sep 24 | none on abstract page | absent (d=2 free energy) |
| Björnberg–Ryan, arXiv:2506.22254 (2025; AHP 2026), cited in Bloch | none on abstract page | absent |
| Seiringer, OWR 7/2025 (2-page workshop note), cited in Sep 24 and the trace | not fetched; states the open problem | absent |

- Searches for "Heisenberg ferromagnet" plus ChatGPT, GPT-5, OpenAI or AI-assisted found **no model-produced prior work** on the problem.
- The nearest *uncited* 2026 neighbour is Wei, arXiv:2609.26802 (v1 09-13, v2 09-24). It covers BB symbols of stability-preserving semigroups, a disk kernel T∏(1+z_i w_i), and Suzuki–Fisher qubit Hamiltonians.
  - I found no AI disclosure in the parts I read: the abstract page and the first 100k of 226k characters of the HTML.
  - It contains no cycles, loop weights or negative dependence.

**In-family: builds on a model-produced result.** All three October companions import the Sep 24 manuscript, which is OpenAI-authored and model-produced:
- the spherical law cites "[Ord, Lemmas 3.2–3.6]" for the stable symbols and the presence bound;
- the lattice correction cites "[Ordering, Proposition 3.1 and Lemma 4.4]" for the simultaneous pin test, plus Thm 7.5, Prop 5.6 and Prop 6.2;
- the Bloch companion says the Sep 24 paper "provides the particular stable exchange symbols, presence inequality, local lattice inequality, and routed unit flows".

So the strict builds-on flag is **true for the companions** and false for the Sep 24 paper. The novelty grades below attach to the Sep 24 items.

## 2. Final grades

| # | Item | Nearest neighbour (verdict) | T2 | Final | F | conf |
|---|---|---|---|---|---|---|
| C1 | Stable exchange symbol E∏(x_i+y_π(i)) (`lem:pin-exchange-symbol`) | **Borcea–Brändén algebraic symbol** T(∏(x_i+y_i)) of the interchange/exclusion operator; its stability ⇔ BBL "SEP preserves stability" (Wagner Thm 3.4 / Lemma 4.3) (**equivalent**) | fail (borderline) | **N0** | – | 0.80 |
| C2 | **Splice** x_q=y_q=t, then the t-coefficient → E[2^{n_P}∏_{i∈P}(x_i+y_σ(i))]; stable next-pin output law under the θ=2 pin law (`lem:pin-splicing`) | Asano/Suzuki–Fisher contraction (trace → loop weight 2, but disk zero-freeness of partition functions); BBL/Liggett (θ=1 only); θ-weighted interchange (Tóth, Ueltschi, Björnberg; no stability); Lieb permanents, α-permanents, MCP (different); Wei 2609.26802 (different). **No near-equivalent found** | pass | **N3 (provisional)** | **F5** | 0.35 |
| C3 | Simultaneous pin test P_E(T⊆B_E) ≤ (2r)^m (`prop:pin-test`) | follows from C2 + BBL 4.9 + a 2^m weight comparison | pass (weak) | N2 | – | 0.60 |
| C4 | Presence product bound (`lem:pin-presence`) | BBL Thm 4.9 (**equivalent**) | fail | N0 | – | 0.95 |
| C5 | Exterior moments E∧^kΠ = ∧^kEΠ (`lem:exterior`) | DLM 2020 determinant-preserving property (**equivalent**); Alon–Kozma hook characters | fail | N0 | – | 0.85 |
| C6 | Conditional next-pin first moment: det(I−K_QQ), Schur kernel, arbitrary W (`prop:first-moment`) | Alon–Kozma Thm 1 (special case); Markov censoring (**close variant**) | pass (weak) | N2 | – | 0.55 |
| C7 | Downward induction over pin sets, sparse multi-point tests (`thm:pin-bootstrap`) | Sznitman decoupling; **templated strengthening** (all substructures + uniform) | pass | N2 (cap) | – | 0.60 |
| C8 | Return energy m(1−r) ≥ E⟨f,(I−U)f⟩, local Nash, routed flows, two-end leakage | Nash, Diaconis–Saloff-Coste, Doyle–Snell, Timár; percolation heat kernels (**close variant**) | fail (borderline) | N2 | – | 0.50 |
| C9 | Spin-S slot loop representation + pin law + factorial domination | Tóth, Nachtergaele, BFU 2020 (**equivalent**); Aizenman–Nachtergaele, Ueltschi | fail | N1 | – | 0.80 |
| C10 | Surface cost → field selection → KMS | Griffiths 1966 (**equivalent**) | fail | N0 | – | 0.80 |
| C11 | [Spherical] Disk symbol E∏(1+x_iy_π(i)), zero-free layered traces | Asano 1970, Suzuki–Fisher 1971, Ruelle; Wei 2609.26802 (**close variant**) | fail (borderline) | N1 | – | 0.50 |
| C12 | [Bloch] d_E(i)=r/(1+r); return comparison giving ζ(3/2)/(8π^{3/2}√det D) | Bloch/Dyson heuristics; Tóth, Conlon–Solovej, CGS techniques | pass (weak) | N2 | – | 0.40 |
| C13 | [Spherical] zero-sum exponential estimate; replica and harmonic pressure tangents | BFU 2020 (complete graph); Lanford–Robinson | pass (weak) | N2 | – | 0.35 |

**Override of the trace analyst.** The trace graded E1 (symbol + splice + pin test) as "N3, borderline N2" in a single bundle. I split it:
- The **symbol itself is N0**. E∏(x_i+y_π(i)) is exactly the Borcea–Brändén algebraic symbol of the random-permutation (exclusion) operator. BB's Thm 1.1 makes its stability equivalent to BBL's exclusion theorem, which is in L. Even the paper's word "symbol" matches. The trace shows no retrieval, but the object exists.
- The N3 candidacy survives **only for the splice (C2)**, with C3 as its consequence.

## 3. Why C2 survives, and how weakly

**For.**
- **No source found** links stability or strong Rayleigh to *cycle-weighted* (θ=2) interchange or loop measures. Searches covered BBL/SEP, θ-weighted permutations, the Heisenberg loop literature, permanents and α-permanents, Lee–Yang for Heisenberg, and 2026 stability-semigroup preprints.
- The splice makes the Heisenberg weight 2 appear "for free". A fixed point yields x_q+y_q = 2t. This removes exactly the obstruction the trace records as lesson C3 ("weight 2 must be handled natively").
- **Non-analytic:** the goal is a KMS state, and nothing in L mentions spliced or weighted symbols.
- **Load-bearing:** every step of the downward induction closes through `prop:pin-test`. In Lean, `PinSplicing.lean` has a file-level, line-weighted downstream share of **0.30** of the `Main` cone, above k=20%. The whole stable cluster is only **9.8%** of the lines: a tiny, pivotal object, Cook-like in shape.
- **In-family reuse across all three companions:**
  - Bloch re-derives C2 and runs a stronger bootstrap, β^{−9|T|/10};
  - the lattice correction imports C3 directly;
  - the spherical law builds the Lee–Yang disk symbol (C11) on C1.

**Against.**
- Every ingredient is N0: the BB symbol, the closure operations (diagonalization and differentiation), and BBL 4.9.
- The mechanism "contraction = qubit trace, so each closed loop has weight dim C² = 2" is classical Lee–Yang technology **for this very model** (Asano 1970; Suzuki–Fisher 1971). The spherical companion makes the identification explicit.
- For someone fluent in both literatures, C2 may be about 1 step from C1.
- The device seems θ=2-specific (trace L126), which is a risk for the downstream-speedup test.
- The trace is a curated summary, so a dropped BBL or BB retrieval at L53 cannot be excluded.

## 4. Discoverability protocols (Test 4, not run)

Full spec: `novelty.json → discoverability_protocols`.

**Common settings.**
- **Models:** training cutoff before **2026-09-24**.
  - A canary probe for family 271 and its vocabulary.
  - No tools.
  - The OpenAI release lineage runs only as an uncontrolled reference arm.
  - Excluded sources: the four 271 manuscripts, the openai/math repo and Lean files, and post-release commentary. The precedents (BBL, BB, Asano, Suzuki–Fisher) are old and allowed.
- **Arms:**
  - L vs L+ (L+ adds the BB symbol theorem, Wagner's survey, Asano and Suzuki–Fisher);
  - open vs directed (directed gives the representation, the pin law and the induction-step target).
- **Sampling:** n=256 per arm, k = 1…256.
- **Judging:** two judges, with an expert check on all hits; Lean targets `stable_spliced_law` and `finite_simultaneous_pin_test`.

**P-C2.**
- **Hide:** C1–C4 and everything downstream.
- **Hit:** the proposal must have all three of:
  - (a) a stable or zero-free multiaffine input/output encoding of the permutation law (any Cayley/Möbius equivalent counts);
  - (b) a stability-preserving contraction that splices cycles and weights closed pin-free cycles by 2;
  - (c) a product (negative-dependence) bound for the next-pin output set.
- θ=1-only proposals are misses.
- Arm A states lesson C9 ("signed minors fail; positivity needed"). Arm B, the decisive arm, does not.
- **Trace:** pivot distance 2 (about 1 in L+); chain depth 1.

**P-C6 and P-C7.**
- P-C6: pivot distance 1, chain depth 1. Hit = identifying E[Σ | every cycle meets J] with the Schur-complement hitting kernel.
- P-C7: pivot distance 1, chain depth 2. Hit = a downward induction over pin sets with a multi-point hypothesis.

## 5. Family verdict

**family_D: D3 (provisional), confidence 0.35.**
- It rests on **C2 alone**, with C3 as its consequence.
- It falls to **D2** in any of these cases:
  - P-C2 Arm B exceeds the calibrated threshold;
  - an expert locates θ=2 stability, negative dependence, or "BB-symbol contraction = cycle splicing" in the Lee–Yang or stable-polynomial literature;
  - a dropped retrieval is shown.
- Without C2, the best items are C6 and C7 (N2).

**Correctness caveat.**
- The claim is extraordinary and unrefereed: it would resolve Lieb's 1999 Problem A in the spontaneous-magnetization formulation.
- A sorry-free Lean development exists, but I did not compile it.
- `lean/docs/271.md` covers only the Sep 24 theorem.

**bridge_novelty.**

| Bridge | Status | Evidence |
|---|---|---|
| BBL negative dependence → θ=2 Heisenberg loops | **new bridge** | No precedent found. The adjacent Lee–Yang contraction route for this model is old but concerns zero-freeness, not negative dependence. |
| DLM 2020 (an ML paper) → next-pin kernel | known route, relabelled | Alon–Kozma's hook/exterior-power algebra for interchange cycles |
| Nash, flows, Timár → walks in the exposed environment | known route | Heat kernels on percolation clusters |
| Sznitman decoupling → sparse witnesses | known route | Standard multi-scale arguments |
| Asano–Ruelle contraction → zero-free strip (spherical) | known route | Asano 1970 and Suzuki–Fisher 1971 for this model |
| Griffiths field selection; Matsubara–Matsuda bosons | known route | Both in L |

## 6. Open questions
1. **Expert query, the main risk to N3.** Is θ=2 strong-Rayleigh behaviour of next-pin outputs, or splicing on BB symbols, known or folklore?
2. Does the splice give stability for θ ≠ 1, 2?
3. Finish reading Wei 2609.26802: 126k characters are unread. Look for permutation symbols and any AI disclosure.
4. Read Suzuki–Fisher and Asano in full for a half-plane analogue.
5. Compile the Lean development and get a proper `lean.json` DAG.
6. Merge with the F1 agent's file when it appears.
7. Run the step-3b compression check.
8. Companion items C11–C13 were graded from introductions and selected sections only.
