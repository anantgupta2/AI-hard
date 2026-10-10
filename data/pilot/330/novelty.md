# Family 330: novelty analysis ("A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

Inputs:
- `family.json`/`.md` (paper and Lean analyst). There is no `trace.json` and no `f1_*.json` for 330, so there are no trace pivots to add.
- The preprint source, at `preprints/Failure-of-Bounded-Approximation-...-September-26-2026/build/sections/`.
- arXiv pages and full texts listed under Sources.

**L** = Mathlib d13f23b plus 330's 17-entry inline bibliography. No item in L is model-produced, so L⁻ = L.

## 1. Provenance verdict first: **no**

| Work | Role | AI disclosure | Contains 330's items? |
|---|---|---|---|
| Ben-David, Childs, Gilyén, Kretschmer, Podder, Wang, arXiv 2006.12760 (2020; SICOMP 2024) | Named precedent for the records | None (2020) | **C3: close variant.** I read the text directly. Algorithm 1 sets "u ← argmax_w ℓ(w)", with the comment "the longest path must go through the parent". The proof of Lemma 58 ends: "l_v > l_u. Since the situation is symmetric we can also deduce that l_v < l_u". C1, C2 and C4 are absent. |
| Smith, arXiv 2509.00722 (v1 2025-08-31 … v4 2026-02-23) | Closest prior result (complete discrete spaces, not uniformly discrete) | None. The pdftotext of v4 has no hits. | Absent. It uses descriptive set theory, and its v4 says the uniformly discrete case is "Kalton's problem". |
| Cúth–Kalenda, arXiv 2604.01875 (2026-04-02) | Coefficient bounds; records the question as open | None (abstract page and HTML, through the summarizer) | Only I09 (N0) |
| *Not cited:* Aliaga–Cúth–Vico, arXiv 2609.24392 (2026-09-21) | Same subfield, 5 days before 330 | **Yes.** "The main results in this document were obtained by OpenAI's GPT-5.6 Sol Pro and GPT-6 Pro" | **Absent.** The full text has 0 hits for Kalton, approximation, uniformly discrete, nonbacktracking or expander. It is about Weaver's unique-predual problem. |
| *Not cited:* 2505.19891, 2509.22328, 2607.28440, 2609.00970 | Other recent Lipschitz-free preprints | None | Absent |

Web searches pairing the problem with ChatGPT, GPT-5, OpenAI or "AI-assisted" returned only coverage of the openai/math release itself. They found no earlier model-produced attack on Kalton's question or on renormings of ℓ₁ that fail MAP.

The flag is **no**. One piece of context: OpenAI models were demonstrably being used on Lipschitz-free problems by experts in the field (Cúth among them) in September 2026, but that work does not overlap with 330.

## 2. Final grades

| ID | Item (paper refs) | Test 1 | Test 2 | Test 3 | Final |
|---|---|---|---|---|---|
| **C1** | Edge tests adapted to the operator, with exceptional discard sets and averaging over incidences (I32, I33, using I30) | No near-equivalent found | Pass | Pass (knockout; Lean obstruction dominated share 0.37–0.39) | **N3 provisional, F3, conf 0.40** |
| C2 | Label-anchor block: capped colour-distance labels, one anchor per label, bumps (I17, I18, I22) | Close variants for each part | Pass | Pass (labels 0.21–0.23 against the 20% proxy) | N2, conf 0.55 |
| C3 | Continuation records and the at-most-one-exceptional-direction lemma (I29–I31) | Close variant (Ben-David Lemma 58; Jordan's tree centre) | Pass vs the goal; borderline fail vs L (the precedent is cited) | Pass | N2, conf 0.75 |
| C4 | Matched walks and their rarity via colour restriction (I20, I24–I26, I28) | Close variant (first-moment bound for a finite tracker on an iid-coloured tree) | Pass | Pass | N2, conf 0.60 |
| C5 | Affine signed measures and the 3L/4 bump-mass bound (I23) | Close variant (Naor21, AACD20) | Weak pass | Pass | N1, conf 0.60. The analyst's N2 is downgraded. |
| C6 | Finite-anchor obstruction in bounded infinite blocks, the wedge, and the order of choices (I07, I34) | Close variant (Figiel–Johnson 1973 sums; Kalton's ℓ₁-sums; Enflo/Davie quantifier order) | Borderline fail | Pass | N1, conf 0.60 |

Excluded items (N0/N1):
- I01–I03, I08–I10, I12, I14–I16, I21, I36: free-space and AP basics, the wedge, coefficients, the local limit, McShane extension, the perturbation step;
- I13: the nonlinear corollary, a C5 transfer from Kalton 2012;
- I37–I39: the Lean-only derandomization.

### C1: why provisionally N3, and why only at 0.40

**The idea.** For each oriented edge x→y, the proof builds a 1-Lipschitz test that depends on T's finite support S:
- it equals +b_x on S∖E_e and −b_y on S∖E_ē;
- each support state is discarded in at most one of the Δ directions at a good vertex;
- so averaging over incidences divides the discarded variation by the degree, giving 2p > 11p.

**Neighbours checked, all genuinely different:**
- **Expander Poincaré inequalities** (Linial–London–Rabinovich; Matoušek; Khot–Naor; Naor–Schechtman; Dilworth–Kutzarova–Ostrovskii). These use fixed test functions and a spectral gap. 330 uses neither, only degree dilution and local tree structure.
- **AP counterexamples** (Enflo, Davie, Szankowski). Their averaged trace functionals are fixed and linear. Here the tests depend on T.
- **Finite obstructions to extension or projection** (Godefroy–Ozawa, Brudnyi–Brudnyi, Godefroy 2015, Naor 2021). These bound projections with a prescribed range or almost-extension operators, not arbitrary finite-rank operators.
- **Large-girth box spaces in uniform Roe algebras** (Willett–Yu; Higson–Lafforgue–Skandalis). A conceptual analogue only, though it is the same graph family that Lean uses.

**Why the confidence is only 0.40:**
- The hardest sub-step (C3) is transfer from TCS.
- The averaging is mass-transport-style counting (BLPS 1999; Aldous–Lyons 2007), a close template for I33.
- Once opposing bumps are chosen, the discard repair is natural.

So the N3 belongs to the **cluster C1+C3**. If Test 4 is decided at pivot level, with the records lemma given, expect N2.

### Test 2 note (counterexample family)
I judged Test 2 against Kalton's question as originally posed (Kalton 2004, p. 185: does F(M) have BAP for every uniformly discrete M?). That question mentions no graphs, labels, supports or tests. Testing T(δ_x−δ_y) against 1-Lipschitz functions is analytic, by Lip₀ = F\*. The T-dependent discard sets are not.

## 3. Family verdict
- **family_D: D3 (provisional), confidence 0.40.** It rests on C1, with its meaning attached to C1+C3.
  - **What would lower it to D2:** Test 4 arm B (records hidden, Ben-David kept in L) clears the calibrated threshold; or a specialist identifies a known operator-adapted edge-test or discard argument, most plausibly in the AP-counterexample literature, in uniform Roe algebras over box spaces, or in mass-transport non-amenability proofs.
- **provenance_flag: no.** Adjacent model-produced work (2609.24392) is recorded as context only.
- **bridge_novelty:**

| Import | Classification | Evidence |
|---|---|---|
| TCS property testing → Banach geometry (Ben-David records) | **New bridge**, carrying N2 content | No Lipschitz-free or BAP paper found using continuation records |
| Benjamini–Schramm local limits of iid-coloured random regular graphs → failure of BAP | **New bridge for BAP** | Expanders and high-girth graphs are a known route for embeddings and transportation-cost spaces, and random constructions are a known route to AP failure (Davie). No prior use against finite-rank operators on free spaces was found. |
| Fréchet/Bourgain distance-to-set labels | Known route | Standard in metric embedding theory |
| McShane extension, Godefroy–Kalton linearization, ℓ₁ coefficient identification | Known route (home field) | Cited and re-proved |
| Kalton 2012 nets → non-approximability | Known route | Kalton links Problem 1 to BAP for nets himself (checked only through secondary summaries) |
| Free-group large-girth quotients (Lean only) | Known route | Standard derandomization |

## 4. Discoverability protocols (not run)

**Common settings for all protocols:**
- **Models:**
  - Training cutoff must be before 2026-09-26, the 330 preprint date.
  - Canary probe: ask whether Kalton's uniformly-discrete BAP question is solved, and whether ℓ₁ has a renorming that fails MAP.
  - Exclude the OpenAI release lineage and GPT-5.6 Sol Pro / GPT-6 Pro, which were used for 2609.24392. These appear only in an uncontrolled reference arm.
- **Excluded sources:** the openai/math repo (preprint, Lean, CONTENTS, docs/330), coverage of the release, and this project's pilot files.
- **Context:** a Mathlib digest plus the 17 bibliography entries, including the Ben-David statements.
- **Arms:**
  - open;
  - directed;
  - directed minus Ben-David.
- **Sampling:** 256 samples per arm, with pass@k for k = 1…256 (powers of 2).
- **Judging:** two LLM judges plus a specialist check, with Lean equivalence against `edge_test` and `finite_support_impossible`.
- **Controls:** Cook–Reckhow as the positive control; C6, C5 and I21 as negative controls.
- **Redaction:** strip the parts of the paper that announce the hidden item:
  - introduction.tex lines 135–229;
  - the closing remark of walks.tex (lines 197–202);
  - the opening of tests.tex;
  - Remark abstract-obstruction.

**P-C1** (decisive):
- **Hide:** I30, I32, I33 and everything downstream.
- **Arm A (pivot):** give I01–I29, I31, the bounds on the measures and the bad fraction. Expected hit rate: moderate to high.
- **Arm B (cluster):** also hide I29–I31.
- **Hit:** T-dependent per-edge opposing tests, plus a discard rule with at most one discarded direction per state, plus degree-dilution averaging. Any tie-breaking rule that achieves this counts.
- **Partial credit:** opposing tests without the discard mechanism, or without the averaging.
- **Estimated distances:** pivot about 1 in arm A and ≥2 in arm B; chain depth 3. These are estimates, since no trace exists.

**P-C2** (optional; it would upgrade C2):
- **Hide:** I17–I19, I22 and everything downstream.
- **Hit:** a bounded block built by attaching vertices to finitely many hubs indexed by a 1-Lipschitz label map.

## 5. Open questions
- **Expert query.** Is an operator-adapted edge-test or discard argument known? This is the main risk to C1.
- **Downstream targets.** Thm blocks at p = 1 already gives a *bounded* uniformly discrete M₁ whose F(M₁) fails MAP. Candidate held-out targets for the speedup test are BAP for free spaces over nets in concrete Banach spaces, and the growth of BAP constants over hubbed random regular graphs.
- **Kalton 2012.** Verify Thm 4.4 and p. 1260 in the primary text.
- **Lean.** Compile it and run the comparator. Lean was not built in this pass.
- **zbMATH and Scholar** were not queried directly.
- **Cúth–Kalenda quote.** Spot-check it, since it came through the summarizer.

## Sources
- arXiv 2006.12760: abstract page, and §6.1.2 of the PDF read through pdftotext.
- arXiv 2509.00722: abstract page and v4 PDF.
- arXiv 2604.01875: abstract page and HTML.
- arXiv 2609.24392: abstract page and v1 PDF.
- arXiv 2609.00970, 2505.19891, 2509.22328, 2607.28440, 2009.11373: abstract pages.
- arXiv 1201.0847 (Godefroy–Ozawa).
- The emergentmind open-problem page for BAP over uniformly discrete spaces.
- kingy.ai coverage of the release.
- The WebSearch queries are listed in `novelty.json`.
