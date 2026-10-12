# Family 262: Sharp one-dimensional Lieb–Thirring inequalities (scalar, matrix, equality cases)

FAMILY analysis of the papers and the Lean, done at text level. This agent did not build the Lean; the orchestrator compiles the comparator. Corpus: `openai/math` at fd4aeeb. There is no reasoning trace. Machine-readable version: `family.json` (34 items). Lean extractor output: `data/items/262_lean.json` (extractor v3).

| Id | Manuscript | Date | Lean |
|---|---|---|---|
| 262-S | *Sharp one-dimensional Lieb–Thirring constants* (scalar, 7 sections, about 1,670 TeX lines) | Sep 23, 2026 | **Formalized** (comparator `OAI.SharpLiebThirring.sharp_lieb_thirring`) |
| 262-M | *Sharp 1D LT inequalities for matrix potentials* (about 1,900 lines) | Oct 5, 2026 | Not formalized |
| 262-E | *Equality cases in the sharp 1D matrix LT inequality* (about 2,230 lines) | Oct 5, 2026 | Not formalized |

M cites S as "ScalarCompanion", and E cites M as "MLT". Both are model-produced, so the provenance flag is set.

## 1. Main statement
- **262-S, Thm 1.1** (`introduction.tex:37-48`): for 1/2<γ<3/2 and 0≤W∈L^{γ+1/2}(R),
  Tr(H_{−W})_−^γ ≤ 2((γ−½)/(γ+½))^{γ−½} L^cl_{γ,1} ∫W^{γ+½}.
  - The constant is optimal and equals the one-bound-state constant L^(1)_{γ,1}.
  - Equality holds at (r+1)sech²(rx), r=(γ−½)^{-1}.
  - This is the full open-interval case of the 1D Lieb–Thirring conjecture (Lieb–Thirring 1976). γ=1 was settled days earlier by Read–Schulz (arXiv:2609.10478, a human preprint, confirmed by search). The OpenAI proof is uniform in σ=γ−½∈(0,1), so it does not rely on Read–Schulz.
- **262-M**: the same constant holds for measurable Hermitian W≥0 of any finite size m, noncommuting and of any rank.
- **262-E**: equality holds iff W = U·diag(w_1..w_k,0..0)·U* in one constant unitary basis, with w_j=(r+1)a_j²sech²(ra_j(x−x_j)). The scales and centres are independent, and there are at most m eigenvalues.
- **Comparator** (`ComparatorChallenges/LiebThirring.lean`):
  - It proves `MainClaim`: for all γ∈(1/2,3/2), the bound holds for every admissible W, `optimalConstant = sharp`, `oneStateConstant = sharp`, and the equality potential attains it.
  - Permitted axioms are propext, Quot.sound and Classical.choice.
  - `H1` is a pair (val, grad) in L² with the weak-derivative identity.
  - The moment is a supremum over finite orthonormal families of weak eigenfunctions, taken in ℝ≥0∞ with no finiteness assumed.
  - The challenge definitions are **textually identical** to `Model.lean` (checked by diff).
- **Match check:** exact for S Thm 1.1.
  - The form-based moment is linked to the actual self-adjoint operator by the sibling theorem `OperatorProof.sharp_lieb_thirring_spectral` (`SpectralMain.lean`), which builds the operator unconditionally.
  - Bochner junk values cannot occur, since W|v|² is integrable for W∈L^p and v∈H¹.
- **Not formalized:**
  - S Cor 7.3 (signed potentials);
  - all of M and E;
  - the paper's Thm 2.1 in its H¹₀ form. It appears in Lean only as an *unproved* Prop `ActionClaim` (`MatrixOrder.lean:84`). The route proves `finite_action_upper_test` (`IntervalAction.lean:154`) for classical continuous amplitudes, which is enough.
- `lean/docs/262.md` covers the scalar result only. The catalog's family title describes the M and E content, which has no Lean.

## 2. Trust surface (text-level grep over 62 files, 15,944 lines, imports only Mathlib)
- No `sorry`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `partial def`, or heartbeat or instance-size options.
- The single `admit` hit is English in a docstring.
- There are 3 trivial `decide` uses: `2 ≠ 0` twice, plus one Bool coercion.
- **Compile status: pending (orchestrator).**

## 3. Labels
| Axis | Label | Conf. | Evidence |
|---|---|---|---|
| A | **A3**: a sharp constant with attainment. The explicit-rate flag is set. The hard direction is A1. (E is A4) | 0.85 | S intro.tex:37-48 |
| B | **B1**: the 1D LT conjecture on (1/2,3/2). M and E are B4 extensions. Not full-only-with-prior | 0.8 | S intro.tex:119-122 |
| C | **C4** primary: a sandwich of sup_C E_K(Cu) between the spectral sum and D_σ∫W^p. Secondaries: C1 (the calibration field M_δ, primitive J and path B), C3 (mod-2 continuation, compactness penalty), C5 (Teschl form theory invoked) | 0.55 (C1 is a close alternative) | S action-framework.tex:47-58 |
| C2 flags | No induction. Analogue: the target is strengthened to a potential-free action inequality that carries each scale k_i (template: carry an extra tracked quantity). E also carries a dimension-free defect Φ_K | 0.7 | S intro.tex:141-143 |
| Computer-assisted | **No** | 0.95 | |
| D | **D3 (provisional)**: the regularized matrix field M_δ with its rank-one comparison | 0.4 | S intro.tex:114-116 |
| Provenance | S: no model-produced precedent. M and E: **yes**, they build on S and M | 0.85 | M history.tex:8, 40-45 |

**E: fields.**
- Problem field: Mathematical physics (MSC 81Q10, 35P15, 34L15, 26D10/15A42).
- Lean dir: Analysis.
- Method fields, all essential unless noted:
  - matrix analysis (functional calculus, Daleckii–Krein, Stieltjes representations, Klein, trace Young);
  - probability (Bochner, Gamma–Gaussian mixtures);
  - differential topology (mod-2 degree; in Lean, PL topology);
  - equivariant topology (free row-sign actions);
  - ODE (Picard–Lindelöf, Gronwall, barriers);
  - spectral theory and forms (KLMN, min–max, Rellich);
  - convex duality and variational methods (Young duality, penalty);
  - special functions;
  - Weyl–Titchmarsh-type half-line boundary maps and log-det trace formulas (M and E only);
  - integrable systems: sech² solitons and the commutation method (background-cited in S, used in E).
- About 9 cross-field method fields. About 75% of the invoked results come from outside mathematical physics.

## 4. Items (abridged; see JSON for all 34)
**Scalar paper (Lean-formalized)**
- **I02/I03: the action E_K and Thm 2.1.** sup over lower-triangular C of E_K(Cu) ≥ Σ∫(k_i²−s²)^σ. It is potential-free and keeps the individual scales. Graded N3 only as the strengthened target (F2); its proof devices are what matter.
- **I04: triangularity ⇔ nested spectral spans.** The standard min–max flag. N1.
- **I05: regularized field** M_δ(B)=c·lim∫_{−R}^{R}(f(K²−2sB+s²)−f(s²))ds, with f'(y)=(y_++δ)^{β−1}.
  - It is designed from the identity k²−2sb+s²=(s−b)²+k²−b², whose affine dependence on B makes the field a trace gradient.
  - On commuting data it reproduces (K²−B²+δ)^σ−δ^σ.
  - **N3 candidate (F1/F3), borderline N2.**
- **I07/I08/I09: primitive J and scalar facts.** J(B)=−∫tr(BM(tB))dt; μ(z)=(z+δ)^σ−δ^σ; the directional Jensen bound; the diagonal rule; the boundary value; sign equivariance. N1 once I05 is given.
- **I10: resolvent tangent inequality** (operator concavity of a Stieltjes function, divided differences). N0.
- **I11: linearization point.** Y_s=(sI−B)²+dI with μ(d)=|a|². N2.
- **I12: integrated tangent map as a Schur multiplier** that equals an even Gamma–Gaussian average of e^{itB}·e^{−itB}. N2.
- **I13: Klein's inequality** applied to conjugates of the pencil, giving tr(MD) ≥ tr(MP(D)). N2.
- **I14: rank-one comparison.** M(B)=aaᵀ ⇒ aᵀ(K²−B²)a ≥ |a|^{2q}. **N3 jointly with I05** (F2).
- **I15: calibration identity.** (J(B)+aᵀBa)'=2a'ᵀBa−ε^{-1}‖M−aaᵀ‖², plus a completed square. N2: a matrix Benguria–Loss/Read–Schulz Riccati calibration.
- **I16: mod-2 continuation lemma.** N0 (Milnor).
- **I17: terminal matching modulo row signs** on lower-triangular C. There is one transverse orbit at θ=0, and zero rows are excluded by the fixed solution b_i≡k_i. N2.
- **I18: compact penalty.** N0.
- **I19–I22: spectral passage.** The Dirichlet estimate, KLMN, min–max exhaustion, the signed corollary and sech² sharpness. N0–N1.
- **I23 (Lean only): PL mod-2 degree.** Equivariant cubical barycentric flags plus an equivariant handshaking lemma (`FiniteParity.lean:413-622`, `Continuation.lean:303`) replace smooth Sard and transversality. This is background that Lean re-proves. N0.

**Matrix paper (no Lean)**
- **I25: integrated trace comparison.** Let N=c_σ∫t^β(t^{−1/2}−R(t))dt, with R(t)=π^{-1}∫((sI−B)²+V+t)^{-1}ds. If N≥0 then tr(NV) ≥ tr(N^q). The deficit is exactly c_σ∫t^β(tr(RZ²)+q‖R^{−1/2}−R^{1/2}(t+N^{1/σ})^{1/2}‖²)dt. **N3 candidate (F3/F5), informal list.**
- **I26: half-line boundary maps S,T.** They satisfy the Riccati identities, (S+T)/2=R^{-1}, the log-det integral F and the weighted balance. N2: a transfer of matrix Weyl–Titchmarsh theory.
- I27: field comparison via N=M_δ+δ^σ. N1.
- I28: realification. N0.
- I29: trace Young inequality. N0.

**Equality paper (no Lean)**
- **I31: dimension-free defect Φ_K** in a quantitative action estimate. N2.
- **I32: compactness with m columns.** The tail bound is ‖Q_hA_j‖² ≤ m(s_h+e_j)^{1/r}. N2.
- **I33/I34: constant channel spaces.** These lead to the matrix Riccati equation B_0'=r(B_0²−α²), whose solutions are tanh/sech² profiles. Attainment follows by factorization. N1/N0.

## 5. Proof architecture (S)
1. Reduce the problem to the potential-free action inequality (Thm 2.1).
2. Build the field M_δ and the primitive J, and compute their boundary values.
3. Prove the rank-one comparison: tangent inequality → Gaussian conjugation average → Klein.
4. Construct the connecting path K→−K with a lower-triangular C, by mod-2 continuation modulo row signs plus barriers.
5. Apply the action identity and penalty, letting ε→0 and then δ→0.
6. Spectral passage: ordered eigenfunctions, triangularity, Young duality, exhaustion, and the sech² sharpness example.

M replaces step 3 with I25 to handle densities of any rank. E adds defects, a compactness argument and Riccati rigidity.

## 6. Lean structure
- 1,208 declarations: 935 theorems, 225 defs, 29 instances, 12 abbrevs, 7 structures.
- The proof DAG has 944 declarations (10,192 lines). By block:

| Block | Declarations | Share of DAG |
|---|---|---|
| PL parity topology | 337 | 36% |
| Field + rank-one core | 301 | 32% |
| Sobolev/spectral background | 172 | 18% |
| Path ODE | 77 | 8% |
| Action/penalty | 31 | 3% |
| Spectral passage | 26 | 3% |

- Within the mathematical core (435 declarations), the field/rank-one block is **69%**, which clears the 20% bar of test 3.
- Measured on the whole DAG, `matrixField` has only a 0.05 share (0.16 for `regularizedPrimitive`), because of the independent PL block.
- Dominated shares:

| Declaration | Dominated share |
|---|---|
| `source_rankone_comparison` | 0.13 |
| `matrix_compact_penalty` | 0.13 |
| `equivariant_continuation` | 0.36 |
| `source_connecting_path` | 0.43 |
| `finite_action_upper_test` | 0.79 |
| `negativeMoment_bound` | 0.89 |

- **Route differences from the paper:**
  - PL parity replaces the smooth Sard argument.
  - The action theorem is proved for classical amplitudes; `ActionClaim` itself is unproved.
  - The rank-one comparison is proved first for complex Hermitian matrices, then complexification transfers it.
  - Lean uses weak eigenfunctions on the line with compact trial flags, not Dirichlet eigenfunctions on intervals.

## 7. Eureka candidates
1. **I05+I14: the regularized matrix field and its rank-one comparison.** N3, borderline N2; F1/F3.
   - *For:*
     - A tiny, non-analytic object that the whole proof revolves around.
     - It is a trace gradient, exact on commuting data, and satisfies the rank-one Young comparison.
     - Formalized and load-bearing.
     - It closes a roughly 50-year-old conjecture.
   - *Against:*
     - Read–Schulz 2026 (γ=1, posted ≤9 days earlier) extends Benguria–Loss's Riccati auxiliary function to orthonormal families via a "matrix correction". I could check only the snippet. If that correction is the σ=½ member of this family of fields, the grade drops to N2.
     - The tools around the field are classical.
     - Reuse outside LT-type problems is unclear.
   - *Lean-shortlist eligible.*
2. **I25: integrated trace comparison with exact deficit** (M, reused in E). N3 candidate, informal list.
   - *For:* a new scalar-tight matrix trace inequality, with an SOS remainder that powers the equality classification.
   - *Against:* it is assembled from classical Weyl–Titchmarsh m-function, spectral-factorization and log-det ingredients (Clark–Gesztesy), and it has no Lean.
3. **I12+I13: Gaussian-mixture conjugation average plus Klein.** N2. Close to positive-definite Schur multipliers as mixed-unitary averages.
4. **I17: row-sign continuation.** N2. A standard template: degree-theoretic shooting.
5. **I31: dimension-free equality defect.** N2. A stability template.

Literature check (WebSearch, 2026-10-12):
- the Read–Schulz abstract and snippet;
- the 2022 survey (arXiv:2203.06051), which lists the interval as open;
- the Schur-multiplier / mixed-unitary literature (e.g. arXiv:1807.06491);
- the Clark–Gesztesy matrix Weyl–Titchmarsh trace formulas (math/9905070, math/9905143).

No exact match was found for I05 or I25.

## 8. Correctness
- **262-S.** Every step was checked by hand with no gap found:
  - the sign of the action identity;
  - the Klein expansion;
  - the final rank-one step, m ≤ d^σ;
  - the θ=0 orbit count;
  - the constant identity.

  It is fully formalized with a clean trust surface. If the comparator compiles, the result is machine-checked.
- **262-M.** The only new ingredient, Thm 3.1, is unformalized. I re-derived its Riccati factorization and determinant algebra and they are correct. The half-line regularity and Fourier inversion steps were not checked.
- **262-E.** The most delicate step is Prop 5.1. It exhausts possibly infinitely many eigenfunctions, chooses B pointwise without a measurable selection, uses a rank-≤m tail bound, and extracts a.e. limits from L¹ errors. It is plausible but unreviewed.
- **No public expert reaction** was found.

## 9. Extraction friction
- The three manuscripts use different bibliography styles.
- M's `history.tex` is `\input` inside its introduction, which shifts the line numbers.
- Lean namespaces are thematic (MatrixProof, PLParity, CubeFlags…).
- The PL degree block (36% of the DAG) is absent from the paper and must be excluded from the core.
- The extractor's `candidate_defs` list is dominated by PL plumbing.
- The paper's Thm 2.1 appears in Lean only as an unproved Prop.
- The catalog's family title describes unformalized content.
