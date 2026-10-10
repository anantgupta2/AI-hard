# Family 367: The critical dimension for the one-phase Bernoulli problem

- **Manuscript:** *The critical dimension for one-phase Bernoulli minimizers* (OpenAI, Sept 24 2026).
  - Location: `preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/build/`.
  - Contents: `paper.tex` plus 7 sections, a 936-line coefficient appendix and a hand-written `thebibliography` with 20 entries (there is no .bib file).
  - It also has a `verification/` directory of Python exact-arithmetic checkers.
- **Lean:** `lean/OAI/Analysis/BernoulliCone`, with 91 files, 13,545 lines and 1,055 declarations. It imports only Mathlib.
  - There is one comparator, `OAI.Bernoulli.nonflat_in_seven`.
  - **It formalizes only the known De Silva–Jerison existence half.**
- There is no reasoning trace, and the family is not withdrawn or revised.
- L is Mathlib d13f23b plus the 20 cited references.
- Structured data is in `family.json`: 41 paper items and 7 Lean items.

## 1. Main statement

**Verbatim** (paper.tex:73-80):
> Every nonzero one-homogeneous global minimizer of (1.1) in ℝ^d, 1≤d≤6, is flat. There is a nonflat one-homogeneous global minimizer in ℝ^7. Consequently, d_*=7.

Here d_* is the least dimension with a nonzero, nonflat, one-homogeneous global minimizer. The energy is J = ∫|∇v|² + 1_{v>0}, and the competitors are arbitrary nonnegative H¹ functions on balls with the same trace.

**What is exactly claimed.** Before this paper, d_* ∈ {5,6,7}:
- Caffarelli–Jerison–Kenig 2004 gave d_* ≥ 4.
- Jerison–Savin 2015 gave d_* ≥ 5.
- De Silva–Jerison 2009 gave d_* ≤ 7.

The paper claims the **top value**, d_* = 7. Its own contribution is to exclude d = 5 and d = 6 (Thm 7.4, cutoffs.tex:315-351). The existence half in ℝ^7 is De Silva–Jerison's theorem, which is cited.

The paper "answers positively the critical-dimension question whether d_*=7" (history.tex:9-10).

**Corollary 1.2** (paper.tex:90-99) applies to local minimizers:
- the singular set is empty for n ≤ 6;
- it is locally finite for n = 7;
- its Hausdorff dimension is at most n−7;
- the bound is sharp, attained by the De Silva–Jerison cone × ℝ^{n−7}.

**An implicit consequence the paper does not state.** After the reductions in Sec 2, the paper uses only *stability* and a smooth link. The argument would therefore also prove the Caffarelli–Jerison–Kenig stability conjecture for cones with smooth cross-section in ℝ⁵ and ℝ⁶. This is the regime Jerison–Savin's method could not reach.

### Lean comparator and match check
| Target | Solution | Matches |
|---|---|---|
| `OAI.Bernoulli.nonflat_in_seven : ∃ u : Space 7 → ℝ, GlobalMinimizer u ∧ Nonzero u ∧ OneHomogeneous u ∧ ¬ Flat u` | Main.lean:10 := `DeSilvaJerison.exists_nonflat_dimension_seven` (GlobalMinimizer.lean:76) | The **second sentence** of Thm 1.1 only, which is De Silva–Jerison 2009 Thm 1.1 |

Checks on the comparator:
- The model definitions (Model.lean) are character-identical to the challenge file.
- They encode the paper's competitor class faithfully:
  - an H¹ function with a weak gradient;
  - H¹₀ as the H¹-closure of C_c^∞ tests;
  - every centre and radius;
  - the volume term included.
- `Flat` means a.e. equality with (x·e)_+.

`lean/docs/367.md` says this directly: the flatness classification and the singular-set bounds "are outside this selected statement". **None of the paper's new mathematics is formalized.**

The Lean proof is a formalization of the De Silva–Jerison cone.
- **The profile.** U = κ|x| p(x₇/|x|), where f solves (1−t²)f''−6tf'+6f=0 (an artanh closed form).
- **Upper comparison** (sub-DAG share 0.86 of declarations / 0.84 of tokens): a calibrated foliation by homothetic barriers with an explicit glued cap and exterior. The construction uses capAmplitude = −(10/17)f(3/5) and a rational τ=−2 Legendre solution.
- **Lower comparison** (0.34 / 0.33): the Picone ground-state inequality.
- The two comparisons are joined by the Sobolev lattice identity.
- About 2,000 lines build Sobolev calculus from scratch, because Mathlib has no H¹.

## 2. Trust surface
Scope: BernoulliCone/*.lean (91 files).

| Construct | Count |
|---|---|
| `sorry` | 0 |
| `axiom` | 0 |
| `admit` | 0 (the one hit is docstring prose) |
| `native_decide` | 0 |
| `implemented_by` | 0 |
| `extern` | 0 |
| `unsafe` | 0 |
| `opaque` | 0 |
| `set_option` | 0 |
| `decide` | 0 |

- There are 151 `nlinarith` and 270 `norm_num` uses.
- The comparator permits `propext`, `Quot.sound` and `Classical.choice`.
- Lean was not compiled here.

**Computer-assisted: YES, and essential for the new half.** It does not touch the Lean half.
- Proposition 4.1, the universal inequalities, is a machine-scale certificate:
  - 231 Table-I rows define f, U, K, M and P;
  - 21 Gram blocks have 557 rows in total;
  - the interior expansion has **1,714** nonzero scalar-graph keys;
  - the boundary expansion has 11 symmetric-monomial coefficients.
- It is verified by exact rational Python arithmetic. Two engines exist, and an independently authored interior engine matched 1714/1714 keys.
- The README disclaims that the checks "do not certify equivalence between mathematical formulas and code, or the analytic proof".
- How the coefficients were found (presumably an SDP or SOS search) is not disclosed.
- We did not execute the repository code (untrusted-code policy).

## 3. Labels

| Axis | Label | Evidence | Conf. |
|---|---|---|---|
| A | **A3** (sharp threshold). Hard direction A5/A1: no nonflat minimizing cone in d=5,6 | paper.tex:73-80 | medium. A1 is a defensible alternative if the existence half is treated as context |
| B | **B1** | history.tex:9-10 | high as a claim |
| C | **C3** primary; secondaries C1 (the test/flux gadget), C4 (estimation chain), C5 (Velichkov, DFS, Jerison–Savin and De Silva–Jerison invoked) | reductions.tex:229-233; history.tex:96-99, 119-121 | high |
| D | **D3, provisional**, resting on P21+P22 | history.tex:78-80 | low–medium |

**B flags.**
- *Full only together with prior results:* **yes**. It needs Jerison–Savin's d_* ≥ 5 and De Silva–Jerison's d_* ≤ 7.
- *Adds corollaries:* yes. These are the sharp singular-set bound and, implicitly, the CJK stability conjecture for smooth-link cones in dimensions 5 and 6.

**C2 flags.** ih_strengthened = **no**, and ih_template = none. There is only a first-dimension argument (reductions.tex:258): off-origin blowups live in dimension d−1 < d_* and are therefore flat.

**Computer-assisted:** yes, as described in §2.

**Provenance flag (builds on a prior model-produced result?): no, provisionally.**
- The cited 2025–26 preprints are Fernández-Real–Yu 2510.18330, Firester–Tsiamis–Wang 2601.16966 and 2601.18794, and Fernández-Real–Serra 2609.05669. All are cited as background.
- The arXiv abstract pages of 2601.16966 and 2609.05669 show no AI disclosure.
- The full check is deferred to the novelty pass.

**E. Fields.**
- **Problem field:** PDE (MSC 35R35, 49Q10, 35B65).
- **Lean-dir field:** Analysis.
- **Method fields:**

| Method field | Tag |
|---|---|
| Free-boundary regularity (Velichkov, De Silva–Ferrari–Salsa, Jerison–Savin, De Silva–Jerison) | essential |
| Spherical tensor calculus / Bochner–Simons identities | essential |
| Calculus of variations: second variation, sharp Hardy constant | essential |
| SOS / Gram-matrix polynomial certificates (Parrilo) | essential (the method itself; no theorem is invoked) |
| O(5) / S_r tensor representation theory (STF and hook projections) | essential |
| Elliptic PDE: Hopf lemma, maximum principle | essential |
| Exact computer arithmetic | essential |
| GMT dimension reduction | corollary-only |
| Minimal surfaces (Simons) | background-cited |

## 4. Proof architecture
1. **Setup.** 5 ≤ d_* ≤ 7 is known. Suppose d_* ∈ {5,6} and fix a nonflat cone.
2. **Smooth link.** Off-origin blowups are flat by minimality of d_*. So the link components are smooth, with Δg = −mg, g = 0 and ∇g = N on the boundary, and some component has T = ∇²g + g·Id ≢ 0.
3. **Suspension (d=5 only).** Pass to ℝ⁶; minimality is preserved. In both cases the working link is Ω ⊂ S⁵, with two singular tips in the suspended case.
4. **Geometry and stability.**
   - T is Codazzi and trace-free, ΔT = 5T, the Bochner identity holds, and Δs² = 2w².
   - s² < 1 inside; H > 0 and w > 0 on the boundary (Hopf).
   - The odd-normal boundary jets of B are given pointwise by V(A,p).
   - The second variation and the Hardy constant 4 give **∫_∂ H v² ≤ ∫ |∇v|² + 4v²**.
5. **Universal certificate (Prop 4.1).** This is a polynomial inequality in free normalized jet data (A, p, g, X, w, z, ℓ): I ≥ ε_*(z²+|ℓ|²) in the interior and S ≥ δ_* on the boundary.
6. **The flux pair.**
   - Define h = w^a√f(A,p,g) and Z = w^{2a}(G:X + wM + P), with G = δ⊗U + (K − K^{(12)}).
   - Fourth derivatives cancel through the Laplacian and skew contractions.
   - Completing the square in ℓ gives div Z ≥ |∇h|² + 4h² + ε_*w^{2a}.
   - Boundary reflection parity gives N·Z + Hh² = w^{2a+1}S ≥ 0.
7. **Exact verification.**
   - The Gram blocks are PSD, using the sym, hook and anti projections.
   - A graph calculus expands the interior into 1,714 keys, each with a graph bound L_t.
   - The resulting matrix D₀ ≤ D̄, and Young's inequality with ν leaves positive slacks.
   - The boundary reduces to 4 eigenvalues and 11 coefficients.
8. **Cutoffs and contradiction.**
   - The weighted Bochner estimate ∫w^{2a−2}|B|² < ∞ uses a ∈ (½, 1).
   - Product cutoffs remove the Hessian zeros and the tips; the tip errors are dominated by s_t^{21/25}D_o.
   - The positive mass ∫w^{2a} > 0 then contradicts stability.
9. **Corollary.** Weiss dimension reduction gives the singular-set statements; the De Silva–Jerison cone × ℝ^{n−7} gives sharpness.

## 5. Items (summary; full list in family.json)

| Grade | Items |
|---|---|
| **N0** | P01–P08 (energy, d_*, regularity theory, dimension reduction, smooth link); P12–P14, P17–P18 (identities, Hopf, stability, Hardy); P29 (Gram/SOS projections); P31 (tensor bounds); P40; Lean L02, L05, L06 |
| **N1** | P09, P10/P11 (suspension unification), P15–P16, P19, P27, P28, P30, P32–P38 (verification arithmetic, weighted Bochner, cutoffs); Lean L01, L03, L04, L07 |
| **N2** | P20 (normalized jet derivation D_l), P23 (fourth-derivative elimination), P24, P25 (boundary reflection parity), P26 |
| **N3 candidates** | **P21** (universal certificate f,U,K,M,P); **P22** (flux pair h, Z) |

Analytic check: P21 and P22 occur nowhere in the goal, in Mathlib or in the bibliography. They are the paper's only non-analytic load-bearing objects.

## 6. Eureka candidates
1. **P22+P21, the flux pair with a universal tensor SOS certificate.** N3 candidate, borderline N2; F3, with an F5 aspect from the jet representation.
   - **For:**
     - It overcomes precisely the obstruction Jerison–Savin identified (JS 2015 §3.2, read here). For 4 ≤ n ≤ 6, the interior and boundary windows for the power test w^α are optimized at different eigenvalue configurations.
     - A non-gradient flux Z decouples the interior estimate (div Z) from the boundary estimate (N·Z). The coefficients also depend on g and ∇g, not only on Hessian eigenvalues.
   - **Against:**
     - The paper names Jerison–Savin's "functions of the Hessian" and Simons as precedents, and Parrilo for Gram certificates.
     - Jerison–Savin's subsolution criterion is the special case Z = h∇h.
     - The certificate is machine-found. SOS and auxiliary-function certificates for PDE inequalities exist in control theory (e.g. arXiv 1703.06371).
   - **Quick literature check:** no geometric-analysis neighbour with a non-gradient flux or a tensor-polynomial certificate was found. The searches covered:
     - Firester–Tsiamis–Wang 2026 (symmetric cones only);
     - Fernández-Real–Serra 2026 (dimension 4);
     - Mazet's ℝ⁶ minimal-hypersurface work (a scalar quadratic form);
     - the Jerison–Savin text.
2. **P23, fourth-derivative elimination.** N2. Restricting the flux to the trace and commutator contractions is the key design constraint, but the identities themselves are classical.
3. **P25, boundary reflection parity.** N2. It kills the undetermined even-normal jets, but follows from making U and K even in p.
4. **P10/P11, suspension unifying d=5 and d=6 on S⁵.** N1. Product minimality is classical, and the budget effect is modest.
5. **P35, weighted Bochner integrability.** N1. This is a standard δ-regularization.

## 7. Correctness concerns
- **Extraordinary claim.** It settles an open problem (d_* ∈ {5,6,7}) and implicitly the smooth-link CJK conjecture in dimensions 5 and 6. The work is unreviewed.
- **What checks out.** Line-by-line reading of the analytic skeleton found no gap. I checked:
  - the suspension formulas;
  - the second variation and the Hardy constant;
  - the divergence identity coefficients (2a−1, 2a+1, 2a);
  - the square completion;
  - f ≥ ε_*;
  - the boundary identity;
  - the weighted Bochner absorption (4a − 2 = 8/25);
  - the tip integrability (21/25 > −1).
- **Arithmetic re-checked here from the printed integers.**
  - All ten D₀ ≤ 2Q²D̄ comparisons hold, but they are **tight** (ratios up to 0.99992).
  - The four slacks reproduce exactly.
  - The 11 boundary coefficients sum to 1,656,725,282, and 1/4 − that/Q² = δ_* exactly.
- **What rests on unverified code.** The 1,714-key expansion and the formula-to-code correspondence are not certified. Both engines implement the same written decoding, so a shared convention error would propagate. Tight margins make transcription errors potentially fatal.
- **The Lean gives zero assurance for the new half.**

## 8. Extraction friction
- The comparator targets the known half, so the Lean DAG measures De Silva–Jerison's construction, not the eureka items.
- The eureka objects exist only as digit-coded coefficient tables with a bespoke graph encoding.
- The key objects (h, Z, G, A, X, V) are defined inline in displays.
- There is no .bib file.
- `formalization.yaml`'s `Problem367` namespace is unrelated (a namespace collision), and the BernoulliCone dir is absent from the yaml.
- The verification directory exposes internal-process artifacts ("debate graphs", "submitted engine", "peer reports") but not the certificate search.
