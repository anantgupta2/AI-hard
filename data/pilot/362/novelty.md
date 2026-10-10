# Family 362: novelty analysis ("Global smoothness for relativistic Vlasov–Maxwell")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

**Inputs**
- `trace.json`/`.md`. These are the only prior analyses: 362 has no `family.json`, `paper.json`, `lean.json` or `f1_*` file.
- The preprint source, `build/sections/*.tex`, about 17.5k words. I extracted the key items myself.
- The Lean tree `lean/OAI/Analysis/VlasovMaxwell`: 207 files, about 90k lines.
  - grep finds no `sorry` and no `axiom`. I did not compile it.
  - The file-level import-DAG shares below come from my own script.
- Web checks on arXiv and elsewhere.

**L** = Mathlib d13f23b plus the paper's 29-entry bibliography.
- L **includes** Klainerman–Staffilani 2002, Pfaffelmoser 1992, Glassey–Strauss, Luk–Strain, Pallard 2005/2015, Lazarovici 2016, and Wang 2026 I and II.
- **L⁻** = L without Wang 2026 I/II, for contamination control.

## 1. Provenance verdict (first)

**Flag: NO.** No cited or close precedent is model-assisted.

| Work | AI disclosure | Bearing on 362 items |
|---|---|---|
| Wang 2026 I, arXiv:2203.01199 (v1 2022-03-02, v2 2026-07-16; in bib) | none found (abstract page; HTML read except its last ~38k chars). Acknowledgment thanks Deng, Yu and Zheng | **Close variant for C1/C2.** Bootstrap on velocity characteristics. §1.6.2 integrates the field along the receiver characteristic by parts *in receiver time*; the "Type I" term, where ∂_t hits V(t), is a receiver-acceleration field term. Its Fourier nonresonance factor plays the role of 362's D = 1−n·a. **Absent:** C3, C4, C5. Symmetry does their job |
| Wang 2026 II, arXiv:2607.14685 (v1 2026-07-16; in bib) | none found (first 100k of ~190k chars) | Localized Glassey–Strauss (GS) decomposition plus normal form; C3–C5 absent |
| Wang 2020 radial, arXiv:2003.14192 (not cited) | none | Same architecture as C1+C2 (velocity bootstrap, the KS "integration along the characteristic is smoother", loss from differentiating V), closed by spherical symmetry |
| Bigorgne 2025, arXiv:2208.08360 (in bib) | none | context only |
| Cheverry–Ibrahim, arXiv:2306.11812 / RMI 2025 (trace only) | none; full-text acknowledgments read | Signed (scalar energy) **momentum increment** representation, a close concept for C1. They *explicitly avoid* controlling directions Ξ/\|Ξ\| as "strongly oscillating", which is exactly what C3 counts |
| Patel 1607.07416; Hernandez–Patel–Salguero 2411.18610 | none | Absolute-value field integrals; 2D aspect-ratio direction control. No overlap |
| Ilin 2603.15929 (cs.AI) | **yes**, quoted: "A single mathematician supervised the process over 10 days at a cost of $200, writing zero lines of code" (Gemini DeepThink, Claude Code, Aristotle) | Vlasov–Maxwell–Landau equilibrium formalization; no 362 item |

**Searches for model-produced prior work.** I searched for the problem's name together with ChatGPT, GPT-5, OpenAI and AI-assisted. The only hit was the 362 release itself.

**Caveat.** Quotes passed through WebFetch's summarizer, so treat them as unverified. The Cheverry–Ibrahim text was extracted from its PDF locally.

## 2. Final grades

| # | Item | Nearest neighbour(s) | T2 | Final N | F | conf |
|---|---|---|---|---|---|---|
| C1 | Signed-increment bootstrap MP√I + A·I·P²L/w, with doubling gaps ≳ 1/log P | Wang 2020/2026 velocity bootstrap with signed time integration; Cheverry–Ibrahim increment; Pfaffelmoser–Schaeffer short-interval bound | weak pass | **N2** (templated cap) | – | 0.75 |
| C2 | Signed force identity (can:identity) and weighted formula | **Heaviside–Feynman formula, equivalent at a = 0 (hand-checked)**; KS 2002 / Wang §1.6.2 receiver-time integration by parts (in L) | borderline fail | **N2** | – | 0.75 |
| C3 | Direction-change count ≤ C(M,A)L⁶/δ (ang:direction) | generic greedy stopping-time / jump counting (rough paths, Lépingle); Pfaffelmoser frozen cells; Wang axis projections. **No near-equivalent found** | pass | **N3 (provisional; T4 pending)** | **F3** | 0.30 |
| C4 | Direction-based occupation via monotone crossing (ang:improved-hit) | Pfaffelmoser crossing on new cells | borderline fail | N2 | – | 0.65 |
| C5 | Summable selection + exponent contradiction (sel:exponents) | good/bad-bin bookkeeping; Wang uses symmetry instead | weak fail | N2 (borderline N1) | – | 0.55 |
| C6 | Cutoff-derivative cancellation | partition-of-unity identity | fail | N1 | – | 0.90 |
| C7 | Endpoint-ramp closure | standard bootstrap closure | fail | N1 | – | 0.80 |
| C8 | Pfaffelmoser occupation + joint energy budget | Pfaffelmoser / Schaeffer (in L) | fail | N1 (transfer) | – | 0.55 |
| C9 | Field localization for continuation | finite propagation | fail | N1 | – | 0.85 |
| C10 | Retarded label change / moving cone | Lazarovici, Pallard, Luk–Strain (credited) | fail | N0 | – | 0.90 |

### Key finding on C2

The trace analyst rated this item N2–N3. Set the receiver at rest: a ≡ 0, D = e = 1, q_X = 1. Then the identity reduces to

  ∫E dt = ∫ n/r² ds − [k0/(rd)], with k0 = u − n.

This is the **Heaviside–Feynman formula** E = n/(κr²) + ∂_t[(n−u)/(κr)] (κ = d) integrated in observer time and summed over sources. The transport kernel equals the Liénard–Wiechert velocity field times dt/ds.

The moving-receiver case adds two things:
- the Lorentz matrix Q = D·Id + n⊗a (because B = n×E);
- a product-rule term in the receiver acceleration a_t.

The PDE use of that term is the Klainerman–Staffilani / Wang move: integrate along the receiver, and the derivative falling on V produces a second field at an angle cost. Both of those sources are in L. The paper cites neither physics source.

### Test 3

The PLAN's 20% downstream proxy fails mechanically for top-of-chain items, as it did in 287. I report file-level downstream share and upstream cone, and judge load-bearing by knockout using the paper's dependency figure:

| File | Downstream | Upstream cone |
|---|---|---|
| IncrementBootstrap | 0.75 | – |
| SignedRemainder | 0.45 | – |
| DirectionCounts | 0.15 | 0.69 |
| SelectionWeight | 0.28 | – |

### Overrides of the trace analyst

| Item | Trace grade | Final grade | Reason |
|---|---|---|---|
| E2 (C2) | N2–N3 | **N2** | Heaviside–Feynman and KS/Wang |
| E1 (C1) | N2 | **N2** | Wang precedent confirms the cap |
| E3 (C3/C4) | N2–N3, F2/F3 | **C3: provisional N3, F3**; C4: N2 | only C3 survives T1 |
| E4 (C5) | N2 | N2 | kept, at lower confidence |

## 3. Discoverability protocols (Test 4, not run)

The full specification is in `novelty.json → discoverability_protocols`.

**Common settings.**
- **Models:** training cutoff before 2026-07-16 (Wang 2026 I v2/II). This also covers the 2026-09-23 manuscript and the 2026-10-06 release.
- **Canary probe:** the model must not know the 362 claim or 2607.14685.
- **Model exclusions:** exclude the OpenAI lineage that produced 362; run it only as a reference arm.
- **Unavoidable background:** KS 2002, Wang 2020/2022 v1, Cheverry–Ibrahim and Heaviside–Feynman cannot be excluded. They are the background the grades are judged against.
- **Arms:** L⁻ vs L, and open vs directed.
- **Sampling:** n = 256, T = 1, pass@k for k = 1…256.
- **Judging:** two LLM judges, plus a human kinetic theorist on all hits and 10% of misses.
- **Controls:** Cook–Reckhow (positive); C6, C9 and C10 (negative).

**P-C3 (decisive).**
- **Hide:** ang:direction and everything downstream.
- **Arm A:** give clause C4, "no uniform directional modulus". A high hit rate is expected (trace pivot distance 1).
- **Arm B (decisive):** withhold C4.
- **Hit criterion:** a count of δ-direction exits that is ≪ w/δ, derived from signed or projected force integrals.
- **Lean target:** `OAI.RVM.Admissible.direction_complete_count_cost_bound`.

**Trace distances and other protocols.**

| Item | Pivot distance | Chain depth | Hit criterion |
|---|---|---|---|
| C3 | 1 | 1 | as above |
| C2 | 1 | 0 | any physical-space total-derivative rewrite; a Fourier normal form gets partial credit |
| C1 | 1–2 | 2 | — |
| C5 | 1 | 2 | — |

## 4. Family verdict

**family_D: D3 (provisional), more likely D2. Confidence 0.30.**

- **What it rests on:** C3 alone, with C4 as its payoff. That piece lets the receiver-acceleration loss close **without symmetry**, which is the paper's real advance over Wang.
- **What would downgrade it to D2:**
  - P-C3 Arm A/B hit rates above threshold. The trace predicts this: the step is one propagation from a learned clause.
  - An expert finding a prior direction-exit count in Vlasov–Poisson or plasma work.

**Correctness caveat.** This is an extraordinary, unrefereed claim. The Lean formalization is very large, has no sorry or axiom per grep, and re-proves continuation rather than importing Luk–Strain. Compiling it should be the first follow-up. All grades are conditional on correctness.

**Bridge novelty.**

| Import | Status | Note |
|---|---|---|
| Pfaffelmoser (VP → RVM) | new bridge in execution | the direction itself is folklore |
| Heaviside–Feynman / KS (electrodynamics → kinetic identity) | known route | — |
| stopping-time / jump counting → momentum directions | new application of a generic device | — |
| finite propagation → continuation | known | — |

## 5. Open questions
1. Compile Lean and run the comparator `OAI.RVM.global_classical_solution`.
2. Check the C2 ↔ Heaviside–Feynman reduction symbolically, for a = 0 and for general a.
3. Read KS 2002 Facts 1–3 first-hand.
4. Expert query on direction-exit counts in kinetic theory. This is the main risk to C3.
5. Read the unread tails of the Wang 2026 HTML.
6. Build a declaration-level Lean DAG.
7. Ask OpenAI about earlier runs before the summarized one (trace L81).
