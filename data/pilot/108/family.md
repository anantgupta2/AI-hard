# Family 108: A cubic permanent–determinant lower bound

**Manuscript:** *A cubic lower bound for border determinantal complexity of the permanent* (OpenAI, dated 24 Sep 2026).
**Source:** `preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/build/source` (9 section files, read in full).
**Lean:** `lean/OAI/Algebra/Determinantal` has 57 files and 21,183 lines. There are two comparators: `PermanentCubic` and `SmoothInitialForm`.
**Analyst:** Phase 1, paper plus Lean, at text level. Lean was not run. The machine-readable version is `family.json`.

## 1. Main statement

> **Thm 1.1** (introduction.tex:41-49). There exist absolute constants c>0 and m₀ such that bdc(per_m) ≥ c·m³ for every m ≥ m₀. One may take c = 1/(5 529 600e) and m₀ = 1408.

**Paraphrase.** Over ℂ, take any sequence of n×n matrices of affine-linear forms whose determinants converge coefficientwise to per_m. The size n stays fixed along the sequence, and the coefficients are unbounded. Then n ≥ m³/(5.5·10⁶·e). The same bound follows for:
- exact dc;
- vertex and edge counts of affine ABPs, including fixed-budget limits.

The previous exponent was 2: Mignon–Ressayre for exact dc, Landsberg–Manivel–Ressayre for border dc.

**Supporting theorem (Thm 2.3, models.tex:104-111).** If G is a smooth nonzero form of degree r ≥ 2 in d ≥ 2 variables, then bdc(G) ≥ (r−1)(d−1)/(4e). Cor 9.3 extends this to smooth lowest-degree terms of nonhomogeneous polynomials.

**Lean comparators.** Both have exact matches:
- `permanent_cubic_lower_bounds` covers the border and exact versions of Thm 1.1, with identical constants.
- `smooth_initial_form_lower_bound` covers Cor 9.3. It contains Thm 2.3 as the case a = 0.

The challenge definitions are textually identical to `Model.lean:120-141`.

**Not formalized:**
- Prop 2.2 (the orbit-closure formulation);
- the ABP corollary (excluded in `lean/docs/108.md`).

The family is also absent from `formalization.yaml`.

## 2. Trust surface

Across all 57 files there are 0 hits for each of: `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `partial def` and `set_option`.

The 24 `decide` uses are literal side conditions (Fin disequalities and ContDiff orders). There are no custom axioms and no imported OAI dirs. Imports are `import Mathlib` only.

**Third-party build.** Guo (arXiv:2609.29568v2) rebuilt the frozen sources at openai/math commit adc7f12, with Lean 4.34.1 and Mathlib d13f23b. He checked 12 declarations from this dir, including `exists_effective_critical_bound` and `exists_selector_affine_projection`. For each, `#print axioms` reported only the three standard axioms.

**Verdict:** clean, pending a comparator run.

## 3. Labels

| Axis | Label | Evidence | Conf. |
|---|---|---|---|
| A | **A5** impossibility (no small representation), explicit rate | intro:41-49 | med-high (A3 arguable) |
| B | **B3** partial progress on per-vs-det; secondary B4, which raises the exponent of LMR/MR from 2 to 3. Adds corollaries (cubic ABP bound; a self-contained quadratic border bound for Σxᵢⁿ) | intro:105-108 | medium |
| C | **C4** primary: polar count vs multihomogeneous Bézout, plus dimension counts. Secondaries: C5 (per→G projection; char-2→ℂ transfer; CHT Severi theorem cited), C1 (explicit gadget), C3 (generic θ and generic slice) | models:123-127; intro:216-238 | medium |
| C flags | computer-assisted **no**; ih_strengthened **no**; ih_template none | | high |
| D | **D3 (provisional)**, resting on G_D (I06) and the char-2 bridge I29/I32/I35 | intro:156-158 | low-medium |
| D flag | builds on a prior model-produced result: **yes (partial)**. It cites the LLM-assisted Sheshadri 2606.13628 as the architecture source for the smooth-form bound. It does not cite OpenAI's *Ten Advances* Ch. 5, whose "critical locus of a permanent specialization plus linear slice" architecture it parallels | polar:9-13 | |
| E | Problem field: TCS (MSC 68Q17, 68Q15, 15A15). Lean dir: Algebra. Method fields: plane-curve AG (Severi, δ), commutative algebra (conductor), enumerative AG (polar degree, Bertini), numerical AG (multihomogeneous Bézout), scheme theory (specialization), complex analysis (IFT), matching gadgets, char-p algebra. AHH, Gałązka and GCT are background or corollary-only | | med-high |

## 4. Proof architecture

1. **Model.** bdc is monotone under fixed affine substitution (I10).
2. **Selector (I06, I17–I19).** Define G_D(X) = [sᵠtᵠ] per_k(X+sI+tD), with q = ⌊(k−1)/3⌋ and degree r = k−2q.
   - Two count gates and a signed 3×3 equality gadget realize (−2)^{2k}((k−q)!)⁴·G_D as a projection of per_{11k−2q}.
3. **Char-2 bridge (I25–I32).** Over F̄₂, per = det. Fix X and form the spectral curve C_X = V(det(sI+tD̄+uX)), which has a fixed reduced fibre at u = 0.
   - ∂F_X/∂X_ij = u·adj(M)_ji, so ∇G_D(X) = 0 means the coefficient [sᵠtᵠu^{r−1}] of every adjugate entry vanishes.
   - A cohomological generation lemma (I27) shows that adjugate entries span H⁰(I_Z(k−1)).
   - A complementary-monomial (catalecticant) trick (I28) then gives length Z ≥ T = C(q+2,2).
   - The conductor sits inside the adjugate ideal (I31, FGvS in char p), so length Z ≤ δ(C_X).
4. **Count (I33–I39).** Two dimension bounds combine:
   - Curves with δ ≥ T have dimension ≤ k(k+3)/2 − T (Severi dimension, CHT2023, cited).
   - Matrices over a fixed curve have dimension ≤ k(k−1)/2. The proof uses the row-adjugate subscheme, which determines X, together with dim Hilbᴺ(C) ≤ N.
   - Together: codim of the gradient locus ≥ T − k ≈ k²/18.
5. **Transfer and slice (I40–I43).** A proper family over Z[θ] gives an open set of complex θ for which the bound holds. Euler's identity identifies the gradient locus with Sing. Bertini then gives a smooth section of dimension d = ⌊k²/100⌋.
6. **Smooth-form bound (I13, I44–I48).**
   - A smooth form has r(r−1)^{d−2} simple polar points.
   - These persist in one nearby determinant by the IFT; no coefficient bounds are needed.
   - Each point lifts to right and left kernel lines. The Schur complement shows the lifts are simple.
   - The lifts are bounded by the multihomogeneous Bézout number 2^{d−2}·C(2n−1, d−1).
   - Hence n ≥ (r−1)(d−1)/(4e).
7. **Combine.** (r−1)(d−1)/(4e) ≥ k³/(3200e) with k = ⌊m/11⌋.

**Lean route differences.** Lean re-proves steps 4–5 by different means:
- A char-2 Frobenius decomposition f = a² + x b² + y c² + xy d² bounds δ ≤ 5·dim K[x,y]/(a,b,c,d) + #(ordinary singular points).
- A transcendence-degree parameter count (18n + T ≤ 9(k+1)(k+2)) replaces the CHT Severi theorem. It is about 18× weaker in T but enough for the same final constant.
- Krull dimension is bounded via field-valued points.
- Macaulay-matrix certificates replace the Stacks semicontinuity argument.

So the formal proof does **not** depend on CHT2023. None of this appears in the paper or in the Lean docs.

**Lean DAG** (upstream cone shares of the 1246-decl target cone):

| Branch | Cone share |
|---|---|
| char-2 critical-dimension branch | 52% |
| Severi substitute | 34% |
| smooth-form bound | 32% |
| fibre bound | 21% |
| selector | 13% |
| ∇=0 ⇒ δ≥T | 13% |
| transfer/slice | 5% |

The extractor's downstream `frac_dag_dependents` is below 8% for every decl and is uninformative here.

## 5. Items (summary; 51 paper items and 12 Lean items in JSON)

- **N0 (classical or cited):**
  - Definitions: per, dc, bdc, δ, polars, ABP.
  - The cited CHT Severi theorem, the conductor colength, the Hilbert-scheme bound, polar degree, multihomogeneous Bézout, characteristic transfer, Bertini.
  - per = det mod 2.
  - The ABP and exact corollaries.
- **N1:**
  - Count gate (the classical permanent identity for elementary symmetric functions).
  - Equality gadget.
  - Row-adjugate subscheme (spectral divisors, AHH).
  - Severi corollary, fibre bound, catalecticant trick (Gałązka).
  - Most Lean encodings.
- **N2:**
  - Selector as a whole (linear size).
  - Adjugate-generation lemma.
  - Conductor globalization.
  - Thm 2.3 / ambient polar bound (close variant of Sheshadri).
  - Lean-only Frobenius δ bound and Severi substitute.
- **N3 (provisional):**
  - **I06** G_D;
  - **I29** (∇G = 0 ⇒ length Z ≥ T);
  - **I35** (codim of gradient locus ≥ T − k).

## 6. Eureka candidates (quick literature check)

1. **G_D as a smooth-after-slicing, linear-size permanent projection** (provisional N3, F1/F3).
   - **For:** it creates quadratic singular codimension at linear degree, which the permanent itself lacks. Sheshadri explicitly makes "no permanent claim" for this reason. It is tiny, non-analytic and load-bearing.
   - **Against:** OpenAI *Ten Advances* (Aug 2026, model-produced, uncited) is a close precedent. Ch. 5 and `openai/ten-proofs/Permanent.lean` specialize the permanent to `minorSum t s d`, bound its critical locus and take finite gradient slices. Guo (arXiv:2609.29568, assisted by Codex GPT-5.6-Sol) even states that the target is "higher degree together with a quadratic-dimensional finite slice". Likely N2.
2. **Char-2 spectral-curve bridge, I29 + I32 + I35** (provisional N3, F5).
   - **For:** it turns critical points of a permanent coefficient into plane curves with large δ. No neighbour was found.
   - **Against:** every ingredient is classical (Beauville/AHH, FGvS, Gałązka, CHT), so it may be an assembly (N2).
3. **Smooth-form border bound I13/I46** (N2). Same constant 4e and same architecture as Sheshadri 2606.13628, whose acknowledgement says LLMs were used "in all stages". The new element is a cleaner IFT persistence argument.
4. **Lean-only Frobenius δ bound and Severi substitute L02/L03** (N2, F5). An elementary replacement for a deep cited theorem.
5. **Two-gate selector I17–I19** (N2). Valiant/DHMTW-type gadgets; Ten Advances uses a root-of-unity specialization instead.

## 7. Correctness and extraction notes

**Checked by hand:**
- the gadget arithmetic (per H = −2; the crossed 2×2 minors vanish);
- the size count 11k−2q;
- the gradient–adjugate identity;
- the catalecticant step;
- the fibre dimension N = k(k−1)/2, which matches the generic count;
- the Bézout coefficient and the final constants (1728·3200 = 5 529 600).

**Sanity check.** The det-analogue [sᵠtᵠ]det(X+sI+tD) is congruent to G_D mod 2. It would therefore inherit dc ≥ ck³, which is consistent with its trivial upper bound of about k³/18. No contradiction.

**Concerns:**
- CHT2023's characteristic-2 Severi dimension is cited, not proved. The Lean route avoids it.
- The paper is dated 24 Sep but cites Kumar–Volk dated 28 Sep 2026 (arXiv v1 confirmed). Either the text was revised after its date or the date is not the writing date.
- `SheshadriNoGo2026` is in the bib but never cited.
- The architecture source (Sheshadri) was described by Kumar–Volk as AI-written and unverifiable.
- The result is extraordinary: the first super-quadratic bound in this model. Lean has not been compiled here.

**Extraction friction:**
- No Lean docstrings.
- The Lean route diverges for about half of the DAG.
- The extractor's downstream share is uninformative.
- Names are reused across namespaces.
- The key candidates are inline constructions.
- Provenance sources lie outside the bib.
