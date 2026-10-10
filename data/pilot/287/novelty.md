# Family 287: novelty analysis ("An isomorphism of the free group factors")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

Inputs:
- `paper.json`/`.md` and `trace.json`/`.md`;
- the preprint source;
- `lean.json`/`lean.md`, which arrived mid-analysis and are incorporated, plus spot checks of `lean/OAI/Analysis/FreeGroupFactor/`;
- web checks of arXiv:2609.11074.

**L** = Mathlib d13f23b plus 287's 17-entry bibliography. Note that L **includes** `shlyakhtenko2026fuchsian`. **L⁻** is L without it, for contamination control.

## 1. Shlyakhtenko check: verdict first

**The citation is real, correctly identified and accurately described. The preprint is itself model-assisted, by OpenAI's ChatGPT Pro.**

**Metadata.**
- arXiv:2609.11074v1, *On the II₁ Factors of Fuchsian Groups*, by Dimitri (Dima) Shlyakhtenko, sole author.
- Submitted 2026-09-10 04:31 UTC, 20 KB, math.OA, MSC 46L54. Only v1 exists; there is no comments field.
- Funded by ARO W911NF-25-1-0075 and NSF DMS-2348633.
- This matches 287's bib entry exactly (references.bib:147–155).
- It is not a family in the openai/math release.

**Access caveat.** I reached the paper through WebSearch and WebFetch of `/abs/…v1` and `/html/…`. Direct WebFetch of `/abs` and `/pdf` failed, and Bash has no network. The quotes below passed through WebFetch's summarizer, so spot-check them against the PDF.

**Claim.**
- **Main results.** L(π₁Σ_g) ≅ L(F_{2g−1}) for g ≥ 2. More generally, L(Γ) is a free group factor for every finitely generated, torsion-free, non-elementary discrete Γ < PSL₂(ℝ). This settles the torsion-free de la Harpe–Voiculescu conjecture.
- **Theorem 1**, as relayed: interpolated identifications L(Γ) ≅ L(F_r) with r = 2g−1+s+t+Σ(1−1/m_j) under stated conditions.
- **Groups with torsion:** only containments up to finite index are proved (Theorem 2). The author says he is unable to settle the conjecture in all cases.
- **Key technical result (Theorem 3):** for every η there is a Haar unitary v with ‖v−A‖₂ < η and L(F₂) = W\*(w) ∗ W\*(v), where w = ABA⁻¹B⁻¹.

**Architecture.**
1. **Prop 1, a Baire category argument.** Suppose that for every finite set x_i and every ε, η there is an automorphism θ that fixes w, moves A by less than η in L², and makes E_{θ(N)} approximate the x_i, where N = W\*(A,w). Then a free complement v exists, found as a Baire-generic point of the L²-closure of the orbit {θ(A)}.
2. **Prop 2.** It replaces E_N by radial contractions T_q, multiplication by q^{ℓ(g)} with Bass–Serre length relative to ⟨A,w⟩. Its proof telescopes with budgets ε/2J chosen backward.
3. **Explicit "finite" automorphisms:**
   - S_f: A ↦ A f(B);
   - R_m: B ↦ BA^m, a Nielsen transvection fixing ⟨A,w⟩;
   - Ψ = R₋ₘ S_f R_m, so that Ψ(A) = A f(BA⁻ᵐ) and Ψ(w) = w;
   - f_{m,t} = exp(i√(t/2m)(z+z̄)), which perturbs by √(t/m) at each step yet has an O(t) cumulative effect (Lemma 9).

**Item-by-item comparison with 287.**

| 287 item | In 2609.11074? | Evidence |
|---|---|---|
| One-step absorption (`prop:perturbation`, I31) | **Close variant**: the same role (a small automorphism that improves how well the perturbed subalgebra approximates targets). It keeps the rank fixed, uses the L² norm, fixes w, and uses a different mechanism | Lemma 1: "the map A↦Af(B), B↦B extends to a normal trace-preserving automorphism" |
| Small-cocycle lemma (I23, PV4) | **Absent**. There are no cocycles, Fox derivatives, prefix sums, free Poisson law or cutoff inverse. The only analog is the 1/√m-per-step, O(1)-cumulative scaling | f_{m,t}(z)=exp(i√(t/2m)(z+z̄)) |
| Cocycle-driven flow (I22, PV3) | **Absent from the final argument.** It appears only as the author's *abandoned* human approach, explored with ChatGPT Pro 5.6 | §1.1: "integrating a time-dependent divergence-free vector field" |
| S = Arg(C) | **Absent**. The only logarithm is scalar (§3.4) | — |
| Adaptive error budget (I34) + L² generation | **Close variant**: Baire category (Prop 1) plus backward telescoping budgets (Prop 2), with generation by L²-totality | §1.2: "v_n = (β₁∘⋯∘β_n)(A)" |
| Nielsen correction (γ: C ↦ CA_w) | **Close variant**: R_m is a Nielsen transvection fixing the protected subgroup, composed with a small automorphism | Lemma 2: "the map A↦A, B↦BA^m extends to a normal trace-preserving automorphism" |

**Provenance.**
- The abstract says: "This result was obtained using OpenAI's ChatGPT Pro 6.0."
- §1.1 ("How this result was obtained: use of AI") gives this account:
  - ChatGPT Pro 5.6 explored the author's transport approach, producing about 70 pages that never closed.
  - The newer model then "returned a 7-page proof that became the basis of this manuscript".
  - The work was "developed with substantial assistance from ChatGPT (OpenAI)", checked and rewritten by the author.
- There is no per-lemma attribution.
- **Citations between the two papers:** it cites no OpenAI work and not 287, which was not yet public. 287 cites it and says "No result from that preprint is used below". The comparison confirms that no lemma is imported.
- **Order:** Shlyakhtenko was public first, by 13 days (09-10 vs 09-23; the release was 10-06). Priority of *discovery* cannot be determined. The 287 trace is undated, never mentions the preprint, and its latest reference is arXiv:2608.15385 (August 2026).
- **Bearing on L(F₂) vs L(F₃):** none directly. Its ranks are r = 1−χ(Γ) and the free rank never changes, which is consistent with both branches of the Dykema–Rădulescu dichotomy. Its relevance is methodological: two weeks earlier, a model-assisted paper showed that small automorphisms plus a limiting generation argument can produce new free generating sets.

**Consequence.** 287's **outer architecture** has a model-produced precedent. Its **inner mechanism**, the cocycle flow and the small-cocycle lemma, does not. The one-step absorption (I31) falls from provisional N3 to N2.

## 2. Candidates and grades

All four tests are applied to each candidate in `novelty.json`. Two notes on the tests:
- **Test 1.** zbMATH and Google Scholar could not be queried directly in this session. Absence claims rest on WebSearch plus domain knowledge, and are phrased as "no neighbour found".
- **Test 3.** In the paper.json DAG (35 items on the path to the main theorem) the chain is linear. The PLAN's downstream-share proxy therefore fails mechanically for top-of-chain items (I31: 11%; I34: 9%). In Lean every novel item is below 5% of the DAG, because the classical interpolation branch dominates 66% (`lean.md`). I judged load-bearing by knockout ("on every path to the target") and report both the downstream share and the upstream-cone share. All ten candidates are knockout-essential.

| # | Item | T1 nearest neighbour | T2 | Final N | F | conf |
|---|---|---|---|---|---|---|
| C1 | One-step absorption (I31) | Shlyakhtenko Lemma 10/Prop 1 (close variant); Ornstein/Krieger perturb-then-limit | fail (borderline: the approximate form of the goal; hypothesis-form of a Prop 1 in L) | **N2** | – | 0.70 |
| C2 | Small cocycle with prescribed word value (I23 + I24/I27/I28) | Peterson–Thom 2011 (β₁⁽²⁾>0 ⇔ unbounded ℓ² cocycle: qualitative, no prescribed direction); Fox; free CLT; Shlyakhtenko Lemma 9 scaling. **No near-equivalent found** | pass | **N3 (provisional; T4 pending)** | **F3** | 0.40 |
| C3 | Cocycle-driven polynomial flow (I22) | Voiculescu cyclomorphy (in L); IPP free malleable deformation (the h=δ_e case); Sinclair / Peterson–Sinclair Gaussian cocycle deformations; Guionnet–Shlyakhtenko and Hartglass–Nelson transport | fail (borderline: an instance of cyclomorphy outside its literal hypotheses) | **N2** | – | 0.75 |
| C4 | Word derivative = cocycle value; exact displacement bound (I15) | Sinclair / Peterson–Sinclair (‖u_g displacement‖ controlled by b(g)); Peterson L²-rigidity | pass (weak) | **N2** | – | 0.65 |
| C5 | S = Arg(C) (I07; the trace's only insight backtrack) | IPP 2008: Borel f with exp(iπf(z)) = z, with time-1 map u ↦ uv. **Equivalent** | fail | **N0** | – | 0.80 |
| C6 | Adaptive budgets + L² generation (I34/I35) | Shlyakhtenko Props 1–2 (in L); Elliott intertwining; Ornstein/Krieger | fail | **N1** (borderline N2) | – | 0.65 |
| C7 | Nielsen correction (I32) | Aut(F_{n+1}) action; Shlyakhtenko R_m | fail | **N1** | – | 0.75 |
| C8 | First-variation trace identity (I16) | cyclomorphy criterion (in L) | fail | N2 | – | 0.70 |
| C9 | Free-sum realisation of ℓ²(F_n) inside M (I11) | free Bernoulli decomposition; free Gaussian functor | fail | N1 | – | 0.70 |
| C10 | 3π free-sum bound (I12) | Ricard–Xu (in L); Haagerup | fail | N0 | – | 0.90 |

Not graded: PV1, which is strategic, and PV2 (Cayley-tree root recovery), which is not in the final proof and is N0 transfer from Ornstein–Weiss / Bowen.

**Overrides of the other analysts.**
- I31: N3 → N2, because of the Shlyakhtenko precedent.
- Arg(C): N2 (trace) / N1 (paper) → N0, because IPP's device is identical, including its time-1 Nielsen property.
- I34: N2 → N1, because Shlyakhtenko's Prop 1 is in L. 287's own Lean proof even replaces the explicit iteration with a Baire lemma (`baire_local_approximation`), which is Shlyakhtenko's device.

**Why C2 alone survives, and how weakly.**
- C2 is the only item with no neighbour found and no retrieval trigger in the trace (PV4).
- It is where non-amenability enters. It fails for ℤ (Dirichlet kernel) and for property-(T) groups.
- Its statement occurs nowhere in L.
- But once `prop:flow`'s word-displacement bound is on the table, the coefficient problem is posed, and its solution is textbook: free CLT plus a spectral cutoff. The Lean formalization even proves it a *second* way, through an elementary alternating, Cesàro-averaged radial series (`Radial.averagedInverse` → `exists_small_prefix_inverse` → `smallCocycle`, SmallCocycle.lean:213). A separate rank-two version (`smallCocycleTwo`) gives the n = 2 step directly. Lean's compression estimate shows only additive growth, with no PHP-style signature.
- So the eureka content lies in **posing** the problem: ℓ² cocycles small on generators but δ_e-valued on a long word, coupled to absorption. The N3 grade really attaches to the cluster **C2 + C4**, with the flow C3 counted as known machinery.

## 3. Discoverability protocols (Test 4, not run)

The full spec is in `novelty.json → discoverability_protocols`.

**Common settings.**
- **Models:** training cutoff strictly before **2026-09-10**.
  - Each model passes a canary probe: it must not know arXiv:2609.11074, or that L(F₂)≅L(F₃) has been claimed.
  - No browsing or tools.
  - Exclude the OpenAI models that produced 287 or assisted 2609.11074 (ChatGPT Pro 5.6/6.0 lineage). They run only as an uncontrolled reference arm.
  - The judge must not be the proposer.
- **Arms.** Each axis has two settings:
  - library: **L⁻** (main) vs **L** (adds Shlyakhtenko, to measure the precedent's effect);
  - prompt: *open* (problem only) vs *directed* (absorption strategy plus all non-hidden upstream items).
- **Sampling:** n = 256 per arm at T = 1. Report pass@k for k ∈ {1, 2, 4, …, 256}.
- **Judging:** two LLM judges given 287's precedent remarks and this neighbour list. A human expert checks all hits and 10% of misses. Lean equivalence is used where it exists.
- **Controls:** Cook–Reckhow ER variables (positive); C5, C7 and C10 (negative).

**C2 (decisive).**
- **Hide:** I23–I29 and everything downstream (I31, I34–I37, I39, I41, I42).
- **Arm A (pivot level):** give I01–I22 and I32, including the displacement bound. A high hit rate is expected here.
- **Arm B (cluster level, decisive):** also hide I14–I22.
- **Hit criterion:** for every η, a word w and ℓ² coefficients with generator norm < η and cocycle value within η of δ_e, or of any fixed vector after normalization. In Arm B the proposal must also couple this to absorption. Lean target: `OAI.FreeGroupFactorMain.smallCocycle`.
- **Trace distances:** pivot distance ≥ 2 overall (about 1 in Arm A); chain depth 2.

**Other items.** The trace's pivot distances and chain depths, with one-line protocols:
- **C1:** pivot distance 1 given I22, I23 and I32; chain depth 3.
- **C3:** pivot distance 1 (the field was proposed first and matched to cyclomorphy afterwards); chain depth 2. Hide I14–I22; the hit criterion is a W\*(C)-fixing trace-preserving flow driven by Σh(g)A_gSA_g\*, plus the displacement bound scored as sub-criterion (b).
- **C5:** pivot distance 1, chain depth 2. Hide I07, replacing it with the semicircular-driver flow from trace branch d1.2; any S ∈ W\*(C) with e^{iS} = C counts as a hit.
- **C6:** pivot distance 1, chain depth 3+. Baire arguments count as hits.
- **C7:** pivot distance 1, chain depth 2. Any basis change c ↦ cw^{±1} counts as a hit.

## 4. Family label and flag

**Axis D: D3 (provisional), confidence 0.45.**
- It rests solely on C2 (with C4 as its coupling).
- It falls to **D2** if Arm B exceeds the calibrated threshold, or if an expert identifies a known prescribed-direction small-cocycle statement for groups with β₁⁽²⁾ > 0.
- It is not transfer: the ingredients are N0, and the candidate is their coupling.
- All grades are conditional on correctness. The claim is unrefereed and extraordinary.
- Per `lean.md`, the comparator `allInterpolatedIsomorphic` contains no sorry or extra axioms and imports only Mathlib. Lean was not run, though. Its route also differs from the paper's: a direct n = 2 step, Baire generation, a radial inverse, and a re-proved interpolation layer.
- Because no novel item shows multiplicative compression, a "confirmed eureka" verdict would have to come from the PLAN's downstream-speedup test (step 9).

**"Builds on prior model-produced result" flag: PARTIAL.**
- Strict "builds on": **no**. No result is imported and the trace never mentions the preprint.
- **Model-produced precedent: yes.** Arguably the closest precedent for 287's architecture is a ChatGPT Pro 6.0–assisted preprint, public 13 days before 287's date and from the same vendor's model family.
- Record this as "model-produced precedent (architecture)". It is the reason 2609.11074 and any post-2026-09-10 model are excluded from Test 4.

## 5. Open questions
1. Spot-check all 2609.11074 quotes against the PDF.
2. Ask OpenAI for the run dates of the 287 search, and whether it overlapped the ChatGPT Pro sessions behind 2609.11074.
3. Compression check: can I31 + I34 be replaced by a w-free version of Shlyakhtenko's Prop 1, with the I23-driven one-step as its hypothesis?
4. Expert query to Peterson, Thom, Gaboriau or Sinclair: is the prescribed-direction small-cocycle statement known or folklore? This is the main risk to the N3 grade.
5. Compile Lean and run the comparator: `smallCocycle`/`smallCocycleTwo` → `one_step` → `rankStep`/`rankTwo` → `allInterpolatedIsomorphic`.
6. Re-run the absence searches on zbMATH and Google Scholar.
7. Reconcile the trace's b1.4 lesson ("free generating tuples separated…") with the final norm-limit construction.
