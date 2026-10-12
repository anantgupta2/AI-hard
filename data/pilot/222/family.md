# Family 222: Perceptron free energies and microscopic jamming exponents

**Commit:** fd4aeeb. **Analyst:** family agent, working at text level. Per the orchestrator, no `lake build`, `lake env` or comparator runs were made. The extractor was run: `scripts/extract_lean.py 222` writes `data/items/222_lean.json`.

**Base library L:** Mathlib d13f23b (which includes `Mathlib.Probability.BrownianMotion`) plus the four bibliographies. Full keys are in `family.json`.

## Manuscripts

| id | title | source | lines | Lean |
|---|---|---|---|---|
| I | The free energy of the Ising random perceptron | `build/main.tex` + 8 `sections/*.tex` + bib (32 entries) | 3.65k | finiteness clause only (`IsingFiniteness`) |
| S | The free energy of the spherical random perceptron | `build/paper.tex` + bib (24 entries) | 1.85k | **full headline** (`PerceptronFreeEnergy`) and the Spherical linear-field formula proposition (`SphericalField`) |
| B | The spherical perceptron with bi-orthogonally invariant disorder | `build/paper.tex` (inline bibliography) | 1.5k | none |
| J | Microscopic jamming in the negative spherical perceptron | single `build/main.tex` with an inline bibliography and a Python certificate listing | 10.4k | none |

## Main statements

- **I (Thm main, `sections/model.tex:88-99`).** Take Gaussian patterns, M = ⌊αN⌋, every α > 0 and every bounded Borel log-potential f. Then lim E p_N(f) = inf_q {α V_f(q) + S_I(q)}, and p_N(f) also converges in probability.
  - V_f is a Parisi-type Gaussian recursion.
  - S_I is the dual of the one-spin log cosh recursion.
  - Extensions: integrable activations, and random-sign patterns for f that is continuous off a Gaussian-null set.
- **S (Thm 1, `paper.tex:72-83`).** Same statement on the sphere ‖x‖² = N, for φ ∈ C_b, at every α, β > 0.
  - The formula is inf_m {α V_{βφ}(m) + S(m)}.
  - V is a Brownian stochastic-control value (Auffinger–Chen form).
  - S(m) = ½∫(1/D_m − 1/(1−t)) is the Crisanti–Sommers / Talagrand entropy.
- **B (Thm main, `paper.tex:92-113`).** Bi-orthogonally invariant A, with compact limiting singular-value law and no outliers.
  - The limit exists and is given by a radial sup over block-norm fractions of an angular pressure.
  - That angular pressure is defined through the nested limits λ→∞, B→∞, θ↓0 of a matrix-path Parisi functional with a "powered" witness integral.
- **J (Thm main, `main.tex:237-260`).** Margin −1 with quadratic penalty. The results:
  - a sharp SAT threshold α_c;
  - gap and force laws in the ordered limit N→∞, β→∞, α↓α_c, which are universal for small Gaussian scale mixtures;
  - G_J(u) = u^{1−γ+o(1)} and F_J(s) = s^{1+θ+o(1)}, with γ = 1/(2+θ), γ ∈ (0.4126930, 0.4126934) and θ ∈ (0.4231063, 0.4231088). These are certified by a Python interval-arithmetic certificate.
  - The exponents match the Franz–Parisi and CKPUZ physics values.

### Comparators

The challenge definitions were checked against the solution files with a whitespace-normalised diff, one declaration at a time. All three match **exactly**:
- `Perceptron/Model.lean`;
- `IsingPerceptron/VariationalDefs.lean`;
- `SphericalField/Model.lean`.

**`PerceptronFreeEnergy`** formalizes S Thm 1 in full: the variational value is real, E p_{N+1} converges to it, and so does p_{N+1} in probability.
- Brownian motion is Mathlib's `IsBrownianReal`.
- Controls are progressive with respect to the usual augmented filtration.
- No junk-value loophole was found:
  - `controlValue` is the sSup of a nonempty set bounded by ‖f‖.
  - The entropy integrand is ≥ 0, so the truncated ENNReal subtraction is harmless.
- `main` does not use the hypothesis β > 0 (`_hβ`).

**`SphericalField`** is S's spherical linear-field formula proposition (`paper.tex:669-691`), including its uniform clause at the stationary field 2h = A_q(q).

**`IsingFiniteness`** says only that the Ising variational value is a real number, for continuous bounded f and α ≥ 0. The paper gets this in two lines (`model.tex:101-107`). So the Ising headline is not formalized.

## Trust surface

The Lean side is 606 files and 130k lines, importing only Mathlib.

- Counts of `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `partial` and `set_option`: all **0**.
- There are 41 `decide` uses, all on trivial numerals or swaps.
- Explicit `Classical.choice` appears only in junk defaults.

The trust issue lies outside Lean, in J's certificate:
- It uses round-to-nearest binary64 with padding (|x|+1e-280)·2⁻⁴³ rather than directed rounding.
- The certificate file `certificate/original_certificate.py` and the reproducibility record cited at `main.tex:9464-9500` are not in the released directory. Only the appendix listing is.
- I did not run it.

## Labels

- **A3**, exact limit by a variational formula. J adds an A4-style sharp-threshold clause. Explicit rate: no. Confidence 0.75.
- **B1.** These are the first all-density, positive-temperature full-RSB formulas for perceptrons with arbitrary bounded potentials, and they confirm the Györgyi–Reimann and Montanari–Zhou predictions. Confidence 0.7.
  - B4 aspect: extends Talagrand and Bolthausen–Nakajima–Sun–Xu beyond small density.
  - Corollary flag: J rigorously confirms the jamming exponents.
  - Scope excludes hard constraints.
- **C4 primary**, a matched upper/lower estimation chain. Secondaries:
  - C3: the upper bound is a contradiction at a contact minimizer.
  - C5: Panchenko ultrametricity, Dovbysh–Sudakov, Lindeberg and Marchenko–Pastur are cited and not re-proved in S, B and J.
  - C2: cascade backward recursion and ASS telescoping.
  - C1: J's feasibility repair.

  IH strengthened: no. **Computer-assisted: yes, for J only** (a real interval enclosure of the spectral root a_*). I, S, B and the Lean are not computer-assisted. Confidence 0.55.
- **D2** (provisional, confidence 0.55). The best items are N2. Provenance flag: yes. I and B cite the OpenAI companion S for the two-pattern cavity strategy, while stating that no theorem from it is used.
- **E.** Problem field: probability and statistical mechanics (MSC 82B44, 60K35, 82D30). Lean-dir field: Probability. Method fields, all essential:
  - spin glasses (RPC, GG, ultrametricity, synchronization, ASS, Guerra);
  - Gaussian analysis;
  - Poisson/stable processes;
  - stochastic control (Boué–Dupuis, Auffinger–Chen);
  - Hamilton–Jacobi and parabolic PDE (Mourrat);
  - convex duality;
  - sphere geometry;
  - ODE (Wronskian);
  - random matrix theory (Haar/Stiefel frames, Marchenko–Pastur);
  - majorization (Hardy–Littlewood–Pólya);
  - Schrödinger spectral theory;
  - validated numerics.

  The physics replica predictions are background-cited.

## Proof architecture (I and S share it)

1. **Functional.** The pattern recursion V_f (equivalently a control value), plus the entropy: the Ising log cosh dual, or Crisanti–Sommers for the sphere.
2. **Order.** First variations through the tilted chain, and the **tail-integral order** (∫_s¹p ≥ ∫_s¹q ⇒ V_f(p) ≤ V_f(q), by summation by parts). Ising also has concavity of ℓ and a supporting inequality, credited to Chen–Issa–Mourrat and re-proved.
3. **Arrays.** GG ⇒ ultrametricity (re-proved by duplication in I), the RPC law, the marked cascade transform, a residual on every visit, and the fresh pattern evaluating to V_f(p).
4. **Upper bound.** Enrich with a cascade label, a hierarchical field and a Poissonized pattern count (the density acts as time). Then:
   - Assume a violation and take a penalized deterministic minimizer.
   - Get joint GG identities, then synchronization.
   - The field first-order condition gives tail(p) ≥ tail(q), so V_f(p) ≤ V_f(q).
   - The time first-order condition tends to −V_f(p)+V_f(q)+δ > 0. Contradiction.
5. **Bulk.** Remove **two patterns** and restore them as independent cascade marks. The first and second moments make the gradient covariance B = a(R) deterministic, with IBP balance c + a_d = ∫ r a dμ. For S, the **tangential divergence** on the sphere plus a **Wronskian** solve gives a = A_q = ∫D_q⁻², the Crisanti–Sommers stationary field, and support < 1.
6. **Cavity.** Add L coordinates, Taylor-expand and evaluate the increment. For I, coordinate exchangeability gives ρ_h = p, and concavity then gives attainment of the entropy dual. Telescope, then let L→∞.
7. **Finish.** Smoothness removal and concentration.

B repeats steps 4–6 for matrix paths on Stiefel columns. It reduces to them through a θ-powered witness integral and Haar-shell majorization.

J runs a different chain: row concavity, mixture universality, deletion and repair for the threshold, a convex martingale critical problem, endpoint scale estimates, then rigidity and contraction to select a_* (λ(a) = a), followed by the interval certificate.

## Lean structure

| | value |
|---|---|
| Lean files | 606 |
| Declarations | 8,664 (6,738 theorems, 1,624 defs) |
| Union proof DAG | 6,013 |
| Spherical `main` DAG | 4,213 decls / 54k lines |
| `SphericalField` DAG | 747 decls / 8.2k lines |
| Ising finiteness DAG | 1,107 decls / 12.4k lines |
| Declarations outside every DAG | 2,651 |

The Ising finiteness DAG is that large because ℓ ≤ 0 is proved through the enriched-model pressure at N = 1.

The orphans are an unfinished Ising upper-bound formalization, including a full formal GG ⇒ ultrametricity proof at `ArraySynchronization.lean:1416`, plus duplicated SphericalField copies.

Route differences from the paper:
- The Lean uses time-discretized control cells instead of Itô.
- The Lean **formally proves Panchenko ultrametricity** (`TripleIndex.lean:200`), which the paper only cites.

Shares within the spherical DAG, recomputed per target by me:

| declaration | role | share |
|---|---|---|
| `expectedPressure_lower_smooth` | lower bound | dominated 48% |
| `bulk_cavity_data` | cavity data | dominated 26.5% |
| `expectedPressure_upper_variational` | upper bound | dominated 11%, subtree 50% |
| `bulk_marked_self_consistency` | two-pattern restoration + Wronskian | subtree 50%, dominated 6.7% |
| `bulkMarkedArray_identification` | two-pattern restoration | subtree 43%, dominated 3.6% |
| `tangent_wronskian_ae` | Wronskian step | subtree 25 decls, dominated 0.4% |
| `sourceQuantile_control_tail_order` | tail order | dominated 2.6% |

## Items

`family.json` lists 74 items: I01–I35, S01–S12, B01–B11, J01–J13 and L01–L03.
- **N0 / transfer:** GG and ultrametricity, RPC and the marked transform, synchronization, ASS, Ising concavity (Chen–Issa–Mourrat / Ho), Lindeberg, the spherical entropy and the control representation.
- **N1:** the recursions, quantization, the fresh-pattern evaluation, the cavity comparison and the extensions.
- **N2:** the Ising entropy dual (I04), tail order (I07/S05), enrichment and contact (I21, I24, I26/S08), two-pattern restoration (I28/S09/B07), dual attainment by coordinate exchangeability (I31), the uniform spherical dual (S06, N1–N2), the tangent/Wronskian self-consistency (S10), the B devices (B03, B04, B08, B09) and the J devices (J03, J05, J06, J08–J10, J12).

## Eureka candidates (quick literature check only)

1. **Two-pattern removal and restoration (I28/S09/B07). N2, borderline N3; F3 if upgraded.**
   - For: it makes a non-Gaussian pattern Hamiltonian cavity-computable. It is reused across three manuscripts. In Lean it heads 43–50% of the spherical DAG.
   - Against: its ingredients are standard (exchangeability, marked cascades, zero variance from matching first and second moments). Its dominated share is low (3.6–6.7%). The paper frames it as a Chen–Mourrat-type critical identification.
   - Search: no identical construction found.
2. **Tangential divergence plus Wronskian self-consistency (S10). N2; F5 if upgraded.**
   - For: it bridges the perceptron gradient covariance and the Crisanti–Sommers stationarity condition.
   - Against: spherical integration by parts is classical, and the target equation is already in L. Its Lean footprint is tiny.
3. **Density-as-time contact comparison with tail order (I26/S08). N2.** This is Mourrat 2021 §4, which the paper names, adapted to this model. The tail order is one step from the standard derivative formula.
4. **B's θ-powered witnesses and Haar-shell majorization. N2.** The precedents are Monasson / Franz–Parisi and HLP. There is no Lean.
5. **J's rigidity selection of a_*. N2.** The scaling equations and the numbers come from physics (CKPUZ, FPSUZ, Parisi–Zamponi). The proof is computer-assisted, with no Lean.

Only items 1–3 can enter the Lean shortlist, and all are N2 at present. Device reuse within the release (items 1 and 3 appear in I, S and B) should go in the release-wide reuse count, as PLAN.md asks.

## Correctness concerns

- S is the best-certified claim: the full statement is a faithful comparator, and the Lean DAG is 54k lines with zero `sorry` or axioms. Compile status is pending the orchestrator.
- **The I headline rests on the paper alone.** Lean covers only the trivial finiteness clause, and the Ising-specific dual-attainment step (I31) has no Lean counterpart.
- **B's "explicit" formula is a triple nested limit.** Sections 3–7 were read at sketch level only.
- **J is 10k lines with no Lean.**
  - The exponent claim depends on a floating-point certificate whose file is not in the release.
  - ε₀ is not explicit.
  - The limits are taken in a fixed order.
  - Sections 6–9 were read at statement level only.
- The cited 2026 preprints (Chen–Issa–Mourrat, Ho, Shmalo, Parisi–Zamponi) were not verified. None of them is load-bearing for S, and I re-proves the cited concavity.

## Extraction friction

- The four manuscripts use three source layouts.
- The family spans three Lean dirs with many orphan and duplicate declarations, and the same short names appear in two namespaces.
- The extractor's definition ranking is uninformative here (maximum dominated share 0.001), so shares were recomputed per target.
- The Lean route differs from the paper's, as listed above.
- There is no reasoning trace for this family.
