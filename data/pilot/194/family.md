# Family 194: Lech's multiplicity conjecture

FAMILY analysis of the paper and the Lean, done at text level. Other agents share this checkout, so this agent did not run `lake build` or `comparator`; the orchestrator compiles the comparator. Corpus: `openai/math` at fd4aeeb. Manuscript: `preprints/Lechs-multiplicity-conjecture-September-23-2026/build/` (main.tex plus 6 sections, 3,220 TeX lines, 29 references). There is no reasoning trace. Machine-readable version: `family.json` (46 paper items and 3 Lean-only items).

## 1. Main statement
- **Paper** (`main.tex:80-88`): let (R,m) → (S,n) be a flat local homomorphism of nonzero Noetherian local rings. Then **e(R) ≤ e(S)**, with no restriction on dimension, residue fields or characteristic. This is Lech's 1960 conjecture in full.
- **Paraphrase of the proof:**
  1. Reduce to complete rings, a domain source, equal dimension and an algebraically closed target residue field.
  2. Factor R → T → S = T/J with e(T) = e(R) and J perfect, and form the IMW complex F = P ⊗ K(x;T).
  3. A new **uniform complex estimate** bounds λH₀(F) from below with coefficient 1 (§2).
  4. Positive characteristic: the estimate gives e_HK(J+(x),T) ≥ e(T), and Ma's identity turns this into e(S).
  5. Mixed characteristic: roots of parameters and Heitmann's Briançon–Skoda result make the entries deep, perfectoid normalized lengths give the lower bound, and a prime filtration gives the upper bound.
  6. Residue characteristic 0: Artin approximation and specialization reduce to the characteristic-p case.
- **Comparator** (`ComparatorChallenges/DuttaDomain.lean`, target `OAI.Lech.dutta_domain`, axioms propext/Quot.sound/Classical.choice):
  - Setting: D is a complete Noetherian local **domain** of characteristic p, and F is a short complex (finite free, degrees −d..0, finite-length homology, H⁰ ≠ 0).
  - Conclusions: all Frobenius-twisted homology has finite length; the Dutta sequence converges; and multiplicity D ≤ duttaMultiplicity.
- **Match check.** This is exactly Corollary 4.4 (`charp.tex:193-201`), i.e. IMW Conjecture 8.1 for complete char-p domains, plus existence of the limit.
  - The definitions match Def 4.3 up to cochain indexing.
  - The Tendsto clause blocks vacuous `limUnder` values.
  - I found no loophole.
- **Formalized vs claimed.**
  - **Lech's conjecture itself has no Lean statement**, in any characteristic.
  - The comparator nevertheless contains the whole new device: Theorem 2.1 for an abstract `TorsionLength` (`ComplexEstimate.lean:88`), instantiated with a char-p normalized length on the perfection that is built from scratch.
  - The solution lemma `dutta_complete_charp` (`DuttaDomain.lean:22`) **drops the domain hypothesis**. It therefore proves IMW Conj. 8.1 for *all* complete char-p local rings, which is stronger than both the comparator and the paper's stated corollary. The paper's own proof (`charp.tex:255-311`) already covers non-domains via a prime filtration.

## 2. Trust surface (text-level grep over all 278 files, 53,953 lines)
- None of the following appear: `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, the `opaque` keyword, `ofReduceBool`, `partial def`.
- There are no `set_option` lines at all (no raised heartbeats).
- There are 12 `decide` uses, all ComplexShape side conditions or Bool-valued definitions.
- Every file imports only Mathlib and its own directory.
- No file has a docstring, so the Lean is hard to audit but this is not a trust issue.
- **Compile status: pending (orchestrator).**

## 3. Labels
| Axis | Label | Conf. | Evidence |
|---|---|---|---|
| A | **A1**: a universal inequality over all flat local maps. The key lemma (Thm 2.1) is A3-style, with an explicit O_h(1/s) error | 0.85 | main.tex:80-88 |
| B | **B1**: confirms Lech fully. Flag *adds corollaries for other conjectures* is set: IMW Conj 8.1 for char p (domains in the paper, all complete rings in the Lean). Not "full only together with prior results" | 0.8 (as a claim) | main.tex:59-64, charp.tex:188-201 |
| C | Primary **C4** (estimation chain: Euler-characteristic positivity plus Riemann-sum error) | 0.6 | complex.tex:530-643 |
| D | **D3 (provisional)**: I08, the uniform complex estimate | 0.5 | main.tex:183-196 |

Notes on C and D:
- **C secondaries:**
  - C5: Cohen factorization, Ma's HK identity, CLMST, Heitmann, Roberts, Eisenbud–Schreyer and Artin, all cited without re-proof.
  - C1: auxiliary T, F, G, V and D.
  - C3: the char-0 contradiction.
  - A case for C5 as primary is defensible.
- **C flags:** computer-assisted no; ih_strengthened no (limits replace induction).
- **D flag:** *builds on prior model-produced result* = **no**. The paper cites one OpenAI preprint (SmallCM), but only as motivation (main.tex:147-153).

**E. Fields.**
- **Problem field:** Algebra (commutative algebra). MSC 13H15, 13A35, 13D22.
- **Lean-dir field:** RingTheory.
- **Method fields:**
  - Essential:
    - algebraic geometry (blowups, cohomology on Pⁿ, finite flat pushforward);
    - **Boij–Söderberg theory** (Eisenbud–Schreyer supernatural bundles and pairing positivity);
    - char-p methods (Frobenius, Hilbert–Kunz, Roberts, Dutta);
    - homological algebra;
    - field theory (trace duals);
    - real analysis (Rolle, Riemann sums).
  - Essential in mixed characteristic only: perfectoid/p-adic geometry (Bhatt–Scholze, CLMST, Faltings length) and plus closure (Heitmann).
  - Essential in characteristic 0 only: Artin approximation.
  - Background-cited: Ulrich methods (Hanes, Ma, IMW, Yhee).
- **Metrics:** cross-field count about 5. About 35% of invoked external results come from outside commutative algebra.

## 4. Proof architecture
1. **Reductions** (`reductions.tex:12-135`): Nagata localization at a fibre prime, prime-filtration additivity and residue-field extension. All N0.
2. **Uniform complex estimate (Thm 2.1, `complex.tex`).**
   - **Setting:** a possibly non-Noetherian ring C and I = (z₁..z_h). The length λ is additive and stable under sums and filtered colimits, with λ(C/(z^a)) = a^h μ and positive Koszul homology of length 0.
   - **Hypotheses on F:** finite free in degrees 0..h, contractible off V(I), alternating rank 0, entries in I^s.
   - **Conclusion:** λH₀(F) ≥ μ s^h (b₀ − A_h Σb_i / s).
   - **Mechanism:**
     - Pass to the blowup Y.
     - Divide the differentials by L^s, which gives G_i = O(−is)^{b_i}.
     - Tensor with the Eisenbud–Schreyer supernatural bundle V of rank (h−1)!, whose roots r_j ≈ s·ρ_j are rounded, where ρ_j are the critical points of H(x) = ∏_{i=1}^h (x+i).
     - Interlacing (−(j+1)s < r_j < −js) forces the hyperhomology of G⊗V into degree 0, so χ ≥ 0.
     - An Euler comparison (three towers, eventual images modulo length zero) gives χ(F_Y) = λH₀(F).
     - Each layer sum equals ∫_{−i}^0 H'/h = (H(0) − H(−i))/h = (h−1)!, so the alternating-rank identity isolates b₀ with coefficient 1.
3. **Length inputs** (`lengths.tex`):
   - Char p: the Faltings normalized length on D_perf gives λ(C/HC) = e_HK(H,D) and makes parameter Koszul homology negligible (Roberts).
   - Mixed char: CLMST perfectoid lengths give λ(C/HC) ≤ e(H,D), with equality on parameter ideals.
4. **Factorization** (Prop 3.3), following IMW Prop 8.3, AFH and Ma: T = R ⊗_A U with e(T) = e(R), J perfect, and F = P ⊗ K(x;T). Generic local rings of T are complete intersections, and regular in mixed characteristic.
5. **Char p** (Thm 4.2): Frobenius gives s = q − c on each component, so e_HK(HD,D) ≥ e(D). HK associativity then gives e_HK(J+(x),T) ≥ e(T), and Ma's Lemma 4.2 identifies e_HK(J+(x),T) with e(S).
   - Ma (2017) had already identified e(S) = e_HK(J+(x),T) and noted the lack of a lower bound. Thm 2.1 is precisely what was missing.
6. **Dutta corollary** (Cor 4.4): this is the Lean target.
7. **Mixed char** (Thm 5.3):
   - Set z = u^{1/q}. Heitmann's Briançon–Skoda theorem puts b·D inside (z)^{q−h}·D for a finite normal domain D of rank r.
   - Lower bound: λ/r ≥ e(B)(1−h/q)^h (1 − K/(q−h)).
   - Upper bound: a prime filtration plus Lemma 5.2, with N → ∞ taken first.
   - Then let q → ∞. The components are summed with coefficient 1 thanks to generic regularity.
8. **Residue char 0** (Thm 6.4):
   - A finite free reduction (Ma 5.1).
   - A polynomial certificate over Z[t]: minors and the reduction relation give e(R) ≥ r, and monic initial relations give e(S) ≤ e(S₀).
   - Artin approximation and spreading out to an algebraically closed field of characteristic p, which contradicts step 5.

## 5. Lean structure
- **Size:** 4,617 declarations (2,766 theorems, 1,172 defs). The proof DAG has 3,499 nodes, 688 of them plumbing.
- **Shares of the comparator DAG** (extractor v3):
  - `complex_estimate_basis` (Thm 2.1): upstream closure **76.6%**, dominated share 0.70. It is implemented with explicit Čech complexes on chart rings: ReesRoot 286, ProductSourceCover 246, RootInvariants 124, ProjectiveRoot 110, AlternatingCech 103, and so on. The Eisenbud–Schreyer bundle via (P¹)ⁿ → Pⁿ is rebuilt from scratch, which is transfer.
  - The char-p length construction (`exists_length_with_module_limit`): 19.6%.
  - The numerical root choice (`NumericalSupport`: H, ρ, roundedRoot, Riemann error): about **1.1%**.
- **Route differences from the paper:**
  - The domain hypothesis is dropped.
  - There is **no Cohen–Gabber**: the Lean works over the separable order {x ∈ D separable over K} (`FrobeniusIntermediatePowerMap.lean:153-273`).
  - **Roberts' theorem is re-proved** via a conductor bound (`RobertsSeparable.lean`).
  - The core estimate needs only DirectSumZero, not the filtered-colimit axiom.

## 6. Items (full list in family.json)
- **N0:**
  - Definitions: e, reduction, short complex, Dutta multiplicity, e_HK, normalized length, perfect ideal, blowup.
  - Cited results and lemmas: supernatural bundles (I16), conductor bound, CLMST inputs, reductions, Ma's HK identity, Ma 5.1, Artin approximation.
- **N1:**
  - Koszul acyclicity mod length zero, graded comparison, twist-map vanishing, the Riemann-sum step.
  - Length-input assembly; normalized-length limits; the finite-length module comparison.
  - Prop 3.3 bookkeeping and Lemma 5.2.
  - The case theorems once I08 is given.
  - Lean SeparableOrder.
- **N2:**
  - I05: the abstract stable-length interface.
  - I13: twisting by L^{-is} on the blowup.
  - I15: the non-Noetherian Euler comparison.
  - I17: root tuning.
  - I18: local pairing positivity.
  - I38/I40: the mixed-characteristic deep-extension scheme with two limits.
  - I43: the char-0 one-sided certificate.
- **N3 candidate:** I08 only.

## 7. Eureka candidates (provisional; full grading in the novelty phase)
1. **I08 uniform complex estimate (N3, F5 + F3).**
   - *For:*
     - It supplies the exact lower bound that Ma's 2017 approach lacked, with coefficient 1 in every dimension, uniform in the ring and the length theory.
     - It is load-bearing for all three characteristics and for the Dutta result, about 77% of the Lean DAG.
     - It is not in the goal or in L.
     - It has plausible reuse: IMW short-complex inequalities, Dutta-type positivity, local Boij–Söderberg.
   - *Against:*
     - It is assembled from known parts (Eisenbud–Schreyer pairing and bundles, blowup twisting, normalized lengths).
     - It can be read as a cross-field **transfer** of the ES functional to the blowup of a parameter ideal, and the paper itself names ES and Eisenbud–Erman as precedents.
   - *Nearest neighbours:* ES (JAMS 2009), Eisenbud–Erman (JEMS 2017), IMW 2022/2023/2025, Berkesch–Erman–Kummini–Sam.
   - *WebSearch:* found no local coefficient-1 analogue, and no 2026 human proof of Lech.
2. **I17 root tuning at the critical points of ∏(x+i) (N2, F3).**
   - It is tiny and decisive, which is the Cook-like shape.
   - But it is **forced**: equal layer sums require an antiderivative equal to c∏(x+i) + const, and the interval condition is the standard ES interlacing. Its pivot distance is about 1.
3. **I13+I18 blowup twist and local pairing positivity (N2, F5).**
   - The neighbours are standard strict-transform moves, IMW2025 (blowup/exceptional fibre) and ES positivity.
4. **I38+I40 mixed-characteristic scheme (N2).**
   - Every move is standard practice in mixed characteristic.
5. **I05 stable length interface (N2).**
   - It packages CLMST's properties of normalized length.

## 8. Correctness and trust concerns
- **Extraordinary and unreviewed.** WebSearch on 2026-10-12 found only the earlier partial results (Ma in dimension 3, Ma's graded case, Meng).
- **§2 checked by hand:**
  - the layer-sum identity;
  - Rolle interlacing;
  - the cohomological-degree counts for l ≥ 0 and l < 0;
  - the signs in eq. (complex-sum-estimate);
  - the alternating rank (1−1)^d = 0.

  The char-p instance is machine-checked once the comparator builds.
- **Top concern: the mixed-characteristic depth step.** It cites HeitmannMa Prop 2.8 to obtain genuine membership b·D ⊆ (z)^{q−h}·D in a finite extension.
  - Heitmann–Ma's headline results are stated for *extended plus closure*, which is an "almost" statement (c^{1/p^e}x ∈ (I,p^n)R⁺).
  - If Prop 2.8 is only of that form, Theorem 2.1 would need an almost-version. That is probably repairable via CLMST Prop 4.0.10, but the paper does not do it.
  - This has not been verified from the full text.
- **Other mixed-characteristic inputs:** e_perfd(H) ≤ e(H) for all primary H (CLMST 4.0.18), and Koszul almost-vanishing for every s.o.p. (4.0.4). Both are stated precisely but not checked.
- **Char-0 leg:** it follows Ma's Section 5. The one-sided certificate is new detail, and I checked it at the level of the (t)-adic tails and Hilbert-function domination.
- **Lean coverage:** only the Dutta corollary is formalized. The Lech assembly in char p (Cohen factorization plus Ma's identity) is short and credible given Thm 2.1. The mixed-char and char-0 legs depend on the paper alone.
- **Downstream test:** it should use `dutta_complete_charp` (all complete char-p local rings) and `complex_theorem` / `complex_estimate_allModule` as the device. A Lech-type or Dutta-type corollary does **not** count as device reuse.

## 9. Extraction friction
- The comparator targets a corollary (Dutta), not the headline (Lech).
- There are no Lean docstrings, so joins rely on namespaces.
- The extractor's def ranking is dominated by Čech plumbing, so lemma-level closure shares were used instead.
- The Lean solution is stronger than the comparator.
- Several cited results enter in precise numbered forms (CLMST 4.0.x, HeitmannMa 2.8, Ma 2.4/4.2/5.1) that need full texts to verify.
