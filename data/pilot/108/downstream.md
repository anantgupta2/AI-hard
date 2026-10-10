# Family 108: downstream targets for the characteristic-2 spectral-curve bridge

Machine-readable version: `downstream.json`. Analysis is at text level only: there is no Lean toolchain here, so nothing was compiled.

**Item.** The bridge works over F̄₂ with D = diag(θ), the θᵢ distinct. Take G_D(X) = [sᵠtᵠ] per_k(X + sI + tD), which equals [sᵠtᵠ] det(X + sI + tD) in characteristic 2. Then:
- if ∇G_D(X) = 0, the adjugate zero scheme Z of the spectral curve C_X = V(det(sI + tD + uX)) has length at least T = C(q+2, 2);
- the conductor bound then gives δ(C_X) ≥ T;
- a Severi count plus a fibre count give dim{∇G_D = 0} ≤ k² + k − T.

The result is quadratic codimension for the critical locus of a linear-degree permanent projection. Type: F5.

## Part A: Is the item in the Lean?

**lean_status: "formalized, different route".**
- **First half, as in the paper.** `Selector.gradient_forces_normalization_defect` (Centralizers.lean:19) and `AdjugateAlgebra.critical_normalization_defect` (PencilSeparability.lean:182) show that ∇G = 0 forces a normalization defect of at least C(q+2, 2).
- **Second half, by a different route.** `SpectralDimension.spectral_effective_bound` (Main.lean:131) uses the char-2 Frobenius square form f = a² + xb² + yc² + xyd², a conductor bound, and a transcendence-degree count 18n + T ≤ 9(k+1)(k+2). The paper instead cites the CHT2023 Severi theorem and a Hilbert-scheme fibre bound. The Lean therefore does not depend on CHT2023.
- **Weaker intermediate statement.** `critical_dimension_effective` (Main.lean:214) gives ringKrullDim ≤ (k+1)² − ⌊C(q+2,2)/18⌋. That is a codimension of at least about T/18, against the paper's T − k. The final constant m³/(5529600e) is nevertheless identical to the paper's; I did not trace how the slack is absorbed.

**Comparator chain** (`PermanentCubic`; found by BFS):

`permanent_cubic_lower_bounds` → `permanent_border_cubic_lower_bound` → `exists_effective_critical_bound` → **`critical_dimension_effective`**, which then branches to:
- `gradient_forces_normalization_defect` → `critical_normalization_defect`;
- `spectral_effective_bound`.

The consumer is `HasBorderDeterminant.selector_lower_of_critical_dimension` (ConditionalBound.lean:393). It accepts the bound over any field and transfers it to ℂ through the integer family.

**The `SmoothInitialForm` comparator does NOT depend on the bridge.** It is the smooth-form branch, which follows the Sheshadri architecture.

Dominated shares of the DAG:

| Declaration | Share |
|---|---|
| `critical_dimension_effective` | 0.485 |
| `spectral_effective_bound` | 0.192 |
| `gradient_forces_normalization_defect` | 0.079 |

**Other gaps between the paper and the Lean:**
- **The spectral curve is affine in Lean.** It is the monic charpoly of X·diag(θ) + A, and δ is the length of the normalization quotient. The paper uses the projective curve C_X.
- **Different section dimension.** Lean uses ⌊C(q+2,2)/18⌋, about k²/324; the paper uses ⌊k²/100⌋.
- **Third-party build.** Guo rebuilt 12 declarations at commit adc7f12, not at fd4aeeb.

## Precedent check: the provenance claims, verified at source

| Claim | Source checked | Verdict |
|---|---|---|
| Builds on an LLM-assisted paper (Sheshadri, arXiv 2606.13628) | arXiv abstract page plus the **v2 PDF** (v1 11 Jun 2026; v2 7 Oct 2026) | The acknowledgement reads "The author used the assistance of large language models in all stages of the effort." It is in the v2 PDF but not on the abstract page; v1 was not checked. The paper treats Σxᵢⁿ, says **"No permanent claim"**, and has no characteristic 2 and no spectral curves. **True for 108's smooth-form branch (C3); irrelevant to the bridge.** |
| OpenAI's August "Ten Advances" used the same method | Ten Advances PDF (cdn.openai.com, 253 pp.), Ch. 5 "Circuit and Formula Lower Bounds for the Permanent"; also the ten-proofs repository | Ch. 5 uses an affine specialization of per, a critical locus of codimension k, a generic slice and Bézout/Baur–Strassen. Stage 3 bounds Crit(M_{t,s,d}) with power sums and Möbius inclusion–exclusion. It names the target "a degree-d specialization with d growing with n and with k = Θ(n²)". Characteristic 2 appears **only as background** ("the determinant and permanent coincide"). There are no spectral curves, δ, conductors or Severi varieties. **True at the architecture level, which pre-announces C1 (G_D). False for the bridge (C2).** 108 does not cite Ten Advances. |

**Further precedent findings:**
- **After Oct 6, 2026.** Guo, arXiv:2609.29568 **v2 (8 Oct 2026)**, reuses 12 machine-checked 108 declarations to get L_div(per_n) ≥ (n²/119790)·log₂(n/44) for n ≥ 1936. This is the first downstream use of the bridge's output.
- **Earlier equivalent of the bridge.** None found. zbMATH and MathOverflow were not reached because the web tools hit a session limit.
- **Effect on grades.** C2 keeps N3 (conf 0.40). The provenance flag stays "yes (partial)", applying to C1 and C3.

## Part B: Targets

### Speedup targets

| # | Target | How the bridge helps | Speedup | Lean |
|---|---|---|---|---|
| 1 | **Ten Advances Ch. 5 permanent circuit bound**, Ω(n² log log n) → Θ(n² log n) | Its output is exactly the degree-growing, Θ(n²)-codimension specialization that Stage 2 needs. It replaces the roughly 8k-line minor-sum block of ten-proofs `Permanent.lean` (27,563 lines in total). Guo v2 has done this on paper. | high | < 300 lines: port the circuit model. Formal baseline: ten-proofs. |
| 2 | **Mignon–Ressayre / LMR quadratic bound** | Via the singular-locus codimension of G_D. Expected to be longer and weaker than the Hessian proof. | low (calibration) | statable now |
| 3 | **Ten Advances Stage-3 target** | This is the bridge's direct output, so it counts as a corollary, not reuse. | n/a | statable now |

**Verdict.** The only strong target is the permanent circuit bound, which concerns the same polynomial in a different complexity measure. No known theorem about other polynomials was found that the bridge shortens.

### Open problems

1. **Cubic symmetric determinantal complexity sdc(per_m).**
   - The bridge applies unchanged.
   - What is missing is a symmetric smooth-form polar bound (Sheshadri proves the symmetric version only for Fermat).
   - Confidence medium.
2. **Hafnian vs Pfaffian.**
   - haf = Pf mod 2, mirroring per = det mod 2, and Pfaffian pencils have spectral curves.
   - This is the best test of whether the device generalises beyond the permanent.
   - Confidence low to medium.
3. **Super-cubic bdc(per).** The device saturates here: the polar bound with degree O(k) and at most k² section variables caps it at k³. Expected failure.
4. **Beyond Baur–Strassen for circuits.** The device already reaches N log d. Expected failure.
5. **dc(per) in odd characteristic.**
   - The codimension bound transfers via the ℤ[θ] family.
   - The polar count is a characteristic-0 argument.
   - Confidence low.
6. **A sharp characteristic-2 Severi-type bound for plane curves with δ ≥ T.**
   - This is the bridge's own second half; the Lean has an elementary version that is 18× weaker.

### Theorem corollaries
- exact dc cubic;
- the ABP cubic bounds (not formalized);
- the det-coefficient [sᵠtᵠ] det(X + sI + tD) inherits dc ≥ ck³;
- Ten Advances' Stage-3 target.

### Release reuse
- **Lean:** no other OAI directory imports Determinantal.
- **Other permanent families** (the four-row permanent inequality; char-p PIT) do not use the method.
- **External:** Guo v2, as above.

### Negative controls
1. **dc(per_m) over F̄₂.** Here per = det, so dc = m. This is a proved-false analogue of the cubic bound.
2. **det_k (q = 0, T = 1).** The critical locus has codimension 4, so the bridge gives only a trivial bound.
3. **The Ten Advances formula bound Ω(n⁴/log n).** It is proved by transcendence degree, not critical loci, so no speedup is expected.

## Top 5 (Lean-usable first)
1. **The permanent circuit bound, Ten Advances to Guo's n² log n.**
   - It has a formal baseline, and the bridge's output plugs straight into Stage 2.
   - It is reuse, but on the same polynomial.
2. **Cubic sdc(per).** It needs about 40 lines of definitions plus a symmetric smooth-form bound.
3. **The hafnian/Pfaffian analogue.** It needs about 100–200 lines of definitions. It would be genuine cross-problem reuse of the mechanism.
4. **A sharp characteristic-2 Severi-type bound.** It is statable with OAI's `normalizationDefect`.
5. **Mignon–Ressayre via the bridge**, as a calibration case where no compression is expected.

## Search log
- BFS chains for both comparators.
- Import grep across OAI.
- Sheshadri: abstract page plus the v2 PDF, text extracted.
- Ten Advances: the openai.com page returned 403. I read the PDF from the ten-proofs README link (253 pp.), grepped it for characteristic 2, spectral, Severi, conductor and adjugate, and read Ch. 5 Stages 2–3. I also read ten-proofs `Permanent.lean`.
- Guo: abstract page for v2.
- A session limit then blocked further web checks, including the literature status for hafnian and sdc.
