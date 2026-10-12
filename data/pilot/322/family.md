# Family 322: Tingley's sphere-isometry problem

**Manuscript:** *A positive solution to Tingley's problem* (OpenAI, Sept 23 2026). Source: `preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/build/main.tex` (544 lines) plus `references.tex` (24 bibitems).
**Lean:** `lean/OAI/Analysis/SphereIsometry`, 67 files, 9,273 lines, 747 declarations. Comparator: `TingleySphereIsometry`.
**Analyst mode:** text level only. Lean was **not built** by this agent because the checkout is shared; the orchestrator compiles the comparator. The extractor was run as `scripts/extract_lean.py 322` (v3), giving `data/items/322_lean.json`.
**L:** Mathlib d13f23b plus the 24 cited works. The JSON twin of this report is `family.json`.

---

## 1. Main statement

> Let X, Y be nonzero real Banach spaces and let f : S_X → S_Y be a surjective isometry. Then T(0)=0, T(x)=‖x‖ f(x/‖x‖) is a surjective real-linear isometry. It is the unique linear extension of f. (main.tex:51-57)

**Paraphrase.** Tingley's 1987 question has a full positive answer in every dimension. The metric of the unit sphere alone determines a real Banach space up to linear isometry. Equivalently, every real Banach space has the Mazur–Ulam property, so the Cheng–Dong question is answered too. The paper assumes nothing about separability, reflexivity, smoothness or strict convexity.

**Comparator.** The target is `OAI.Tingley.tingley_sphere_isometry_full`, with only the standard axioms permitted.
- **Hypotheses:** X and Y are `NormedSpace ℝ`, `CompleteSpace` and `Nontrivial`. `UnitSphere X` is the subtype `{x // ‖x‖ = 1}`. The map f satisfies `Isometry f` and `Surjective f`.
- **Conclusion:** `∃ T : X ≃ₗᵢ[ℝ] Y` such that T extends f, T 0 = 0, T x = ‖x‖ • f(normalize x) for x ≠ 0, T is surjective, and T is unique among **all** ℝ-linear maps that agree with f on the sphere.

**Match check: exact.** The uniqueness clause is even slightly stronger than the paper's, because it allows linear maps that are not assumed continuous. The challenge file's `UnitSphere` and `normalize` are textually identical to `Model.lean`.

**Formalized vs claimed.** Everything is formalized.
- Lean imports Mathlib's Hahn–Banach (`exists_dual_vector''`) and Mazur–Ulam (`toRealLinearIsometryEquivOfMapZero`), where the paper re-proves both.
- Lean re-proves ultrapowers, the Kuratowski measure, Darbo, Schauder, Brouwer for the simplex and Sperner. None of these are in Mathlib d13f23b.

## 2. Trust surface
I grepped all 67 files at word boundaries.

| Construct | Count |
|---|---|
| `sorry` / `admit` / `axiom` | 0 / 0 / 0 |
| `native_decide` / `implemented_by` / `extern` / `unsafe` | 0 / 0 / 0 / 0 |
| `opaque` / `partial def` | 0 / 0 |
| `decide` | 0 |
| any `set_option` | 0 |

The only hit is the English word "admit" in a docstring (`KuratowskiTotalBounded.lean:15`). The development imports only Mathlib and its own files. This is an unusually clean trust surface. The compile verdict is pending.

## 3. Labels

| Axis | Label | Evidence | Conf. |
|---|---|---|---|
| A | **A1** (universal). Formally ∀∃!, but the witness T is named in the statement, so the content is "the radial map is a linear isometry" | main.tex:52-56 | 0.75 |
| B | **B1**: confirms Tingley's problem fully. Flags: *adds corollaries* (Mazur–Ulam property for every real Banach space; subsumes all class-specific results). *Full only with prior*: no | main.tex:49 "We prove the full assertion." | 0.85 (label) |
| C | **C3** primary: the proof assumes M>0, takes an attained extremal configuration and derives a contradiction (main.tex:455). Secondaries: C1 (return map, invariant set and aligned chords built inside the contradiction), C4 (contraction and secant estimates), C2 (hull-growth induction, Darbo iteration, Sperner parity), weak C5 (all classical tools are re-proved in the paper; Lean invokes Mathlib Hahn–Banach and Mazur–Ulam) | | 0.85 / 0.7 |
| C flags | *computer-assisted*: **no** (zero `decide`). *ih_strengthened*: **yes**. The induction tracks the whole hull, conv{v₀..vₙ} ⊂ E, not just vₙ ∈ E (main.tex:259). *ih_template*: **"strengthen to all substructures"** | | |
| D | **D3 (provisional)**, from the return-map / self-supplied-contraction device (I10+I15). *Builds on prior model-produced result*: no | main.tex:110 | 0.5 |
| E | Problem field: functional analysis (MSC 46B04, 46B20). Lean dir: Analysis. Method fields, all essential: convex geometry and supports; **fixed-point theory** (Kuratowski, Darbo, Schauder; 47H08/47H10); **combinatorial topology** (Sperner and Brouwer, re-proved); Banach ultrapowers and ultrafilters; Mazur–Ulam; 1-D convexity. Background-cited only: operator-algebra facial results and class-specific Tingley papers. Cross-field count 2 (3 if ultrafilters are counted as logic). Share of invoked results from other fields ≈ 3/7 | | 0.7 |

## 4. Proof architecture
1. **Defect reduction** (main.tex:147-160). The defect is D_q(x,y)=‖f(x)−q f(y)‖−‖x−qy‖ and M = sup|D_q|. Its properties are D₀=D₁=0, 2-Lipschitz in q, and D^{f⁻¹} = −D. The theorem is equivalent to M=0.
2. **Attainment** (lem:attainment). If M>0, pass to completed ultrapowers. There a surjective sphere isometry has the global bound |D_q| ≤ M and attains D_t(x₀,y) = M exactly, with t ∈ [M/2, 1−M/2].
3. **Return map** (eq:return). Fix y, t and b=f(y). The map runs:
   - v ↦ x = ty+pv ∈ S_X;
   - x ↦ f(x) = tb+sw;
   - f(x) ↦ the opposite contact f(z) = tb−uw;
   - f(z) ↦ z, and then g(v) = (ty−z)/r.
4. **Extremal set** E = {s−p = M}. For v ∈ E, the two triangle inequalities are forced to equality: r = u+M and ‖pv+r g(v)‖ = p+r. So v and g(v) share a support. Moreover, **every unit l that shares a support with g(v) lies in E.**
5. **Invariant convex set.** Set v_{n+1} = g(aₙ), where aₙ is a strictly positive combination of v₀..vₙ. One common support then equals 1 on the whole hull, so the hull stays in E. A dense schedule of aₙ gives a closed convex C ⊂ E ⊂ S_X with g(C) ⊂ C.
6. **Contraction.** The estimate is ‖g(v)−g(v′)‖ ≤ (up/rs)‖v−v′‖ + scalar terms, where up/rs = (1−M/r)(1−M/s) ≤ (1−M/(1+t))² < 1. Binning the scalars p and u gives χ(gH) ≤ γχ(H). Darbo's theorem (re-proved through Schauder and Sperner) then gives a fixed point. The result is the **aligned chords** x=ty+pv, z=ty−rv, f(x)=tb+sw, f(z)=tb−uw, with s−p = r−u = M and p+r = s+u = d ≤ 2.
7. **Secant lemma.** The defects at radii t−sh and t+uh, weighted by u and s, cancel the unknown norm ‖w+hb‖ because sr−up = Md. The choice of h puts one radius at an endpoint, where its defect is 0. The result is ε/p ≤ φ(v) ≤ K ≤ {1−B or B}.
8. **Two regimes.**
   - Large (A>ε or B>ε): strict support signs follow, using the relabelled inverse configuration (p′,s′,r′,u′) = (u,r,s,p). A small radial perturbation then beats M.
   - Small: ε < 1/2 together with the ratio inequalities. Convexity of ‖y+λv‖ and ‖b+λw‖ contradicts ‖y−z‖ = ‖f(y)−f(z)‖. Lean replaces this step with two exact vector identities.
9. **Conclusion.** M = 0, so T is an onto isometry fixing 0. Mazur–Ulam makes T linear, and uniqueness follows from homogeneity.

## 5. Items (29; full list in JSON)

| id | item | N | note |
|---|---|---|---|
| I01–I04 | S_X, radial map T, Mazur–Ulam property, support | N0 | goal vocabulary or standard |
| I05 | lem:support (Hahn–Banach, common support) | N0 | Mathlib in Lean |
| I06 | lem:radial (radial contact) | N0 | Lean proves it Lipschitz |
| I07 | cross-radius defect D_q, M | N1 | **analytic**: the difference of the goal's two sides after unfolding T |
| I08 | antisymmetry, 2-Lipschitz | N1 | |
| I09 | ultrapower attainment | N1 | standard local-theory device, transferred |
| **I10** | **opposite-endpoint return map g** | **N3 cand.** (F3/F5) | core construction |
| I11 | extremal set E + common-support propagation | N2 | facial-method affinity (Tanaka, Cheng–Dong) |
| I12 | invariant convex set by hull growth | N2 | templated IH strengthening, capped at N2 |
| I13–I14 | Kuratowski χ, Darbo | N0 | **transfer** from fixed-point theory |
| **I15** | **return-map contraction χ(gH) ≤ (1−M/U)²χ(H)** | **N3 cand.** (F3) | the defect itself supplies the contraction margin |
| I16 | prop:alignment (composite) | N3 cand. | dominates 55% of the core DAG |
| I17, I20 | A, B, ε; inverse configuration | N1 | bookkeeping |
| I18 | secant lemma (weighted cancellation) | N2 | |
| I19, I21 | large and small regime contradictions | N1–N2 | |
| I22–I27 | Mazur–Ulam, χ lemmas, Brouwer via Sperner, Schauder, ultrafilters, ultrapower | N0 | all re-proved in the paper |
| I28–I29 | positive schedule, `AlignedConfiguration` record | N1 | plumbing |

## 6. Lean structure and load-bearing
The target DAG has 579 declarations. Split by file layer:

| Layer | Declarations | Share |
|---|---|---|
| Core Tingley argument | 247 | 43% |
| Re-proved fixed-point background (Sperner, barycentric subdivision, Brouwer, Schauder, Kuratowski, Darbo) | 227 | 39% (2.9k lines) |
| Ultrapower and completion | 73 | 13% |
| Supports and radial contact | 32 | 6% |

Dominated shares, as whole / core:
- `exists_alignedConfiguration`: 66% / 55%.
- `exists_return_invariant_convex`: 14% / 29%.
- `alignedConfiguration_impossible`: 11% / 23%.
- `exists_fixedPoint_of_kuratowski_contraction`: 37% / 0%. It is pure background.

As in 287 and 112, the key new layer falls below 20% of the whole DAG but clears it within the core.

The extractor's candidate-definition ranking puts ultrapower and subdivision plumbing on top (`unitClass`, `iterData`, `UltraSequence`), so I ignored it. Lean names are descriptive, so the paper-to-Lean joins were easy.

**Route differences:**
- The small-chord contradiction uses vector identities instead of the convex functions F and G.
- Lean uses Mathlib's Hahn–Banach and Mazur–Ulam.
- The return map is totalized to the ambient space for the Darbo step.

## 7. Eureka candidates
1. **Return map + self-supplied Kuratowski contraction → aligned chords (I10+I15→I16).** Provisional **N3**, F3/F5.
   - *For:* it turns "extremality propagates" into a dynamical system whose contraction margin is exactly the hypothetical defect M. It needs no compactness and no finite dimension, which is what every prior approach lacked. It is non-analytic, and it is the largest core component.
   - *Against:* every ingredient is classical (Darbo, radial contact, two triangle inequalities). It may be graded N2 if a folding or return-map argument exists in the Tingley or Mankiewicz literature. Reuse outside this problem is unclear, so it risks being a one-off device in the downstream test.
   - *Lit check:* 3 WebSearches found no source linking Darbo or measure-of-noncompactness arguments with sphere isometries.
2. **Extremal common-support propagation and the invariant face (I11+I12).** **N2**.
   - It is close to facial methods, as the paper itself says (main.tex:93-95: "geometric affinity with facial methods").
   - Its IH strengthening is templated.
3. **Secant cancellation lemma (I18).** **N2**: a clever but elementary choice of radii.
4. **Defect + ultrapower attainment (I07+I09).** **N1**: analytic reformulation plus a standard device.
5. **Chord contradiction (I19, I21).** **N1–N2**: elementary first variation and convexity.

## 8. Correctness audit
**Verdict.** This is an extraordinary claim: Tingley's problem has been open since 1987, and the general and dim ≥ 3 cases are described as open in every source I could reach. The paper is short, and I re-derived Sections 3–5 by hand:
- the defect identities and attainment;
- r = u+M and the propagation rule;
- the hull growth;
- the exact contraction constants;
- the secant identity uΔₓ+sΔ_z = MdK (sr−up = Md);
- the strict-sign argument and the inverse relabelling;
- the small-regime inequalities and the final convexity contradiction.

**I found no gap.** The Lean development is clean and its comparator matches the paper exactly.

**Residual concerns:**
- The result is unreviewed, and I found no expert reaction.
- I did not compile the Lean.
- Two places deserve a second look:
  - continuity of g on C as a map into X, which Lean handles through `returnAmbient`;
  - the step "sphere of the completion = completion of the sphere" (`SphereCompletion.lean`).
- The paper's Sperner proof sketch is terse, though Lean covers it in full.

## 9. Extraction friction
- There are 2 TeX files and 12 theorem environments. The key constructions are inline inside the proof of prop:alignment, so they must be split into four items by hand.
- 52% of the DAG is re-proved background, so shares relative to the core had to be recomputed by file layer.
- There is no reasoning trace for this family.
- All Lean statements here were read at text level only.

Sources (quick literature check): [Peralta survey arXiv:1801.02473](https://arxiv.org/pdf/1801.02473), [Kadets–Martín arXiv:1206.4839](https://arxiv.org/pdf/1206.4839), [Banakh arXiv:2103.09268](https://arxiv.org/pdf/2103.09268), [Banakh–Cabello Sánchez arXiv:2103.09266](https://arxiv.org/abs/2103.09266).
