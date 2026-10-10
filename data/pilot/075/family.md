# Family 075: "The L log L Fourier-convergence conjecture" (family analyst: paper + Lean)

Source: `preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/` at commit fd4aeeb. The `main.tex` file `\input`s 10 section files and 2 TikZ figures; file:line references below are per section file. Lean: `lean/OAI/Analysis/FourierLLogL` (156 files, ~29.2k lines) plus `OAI/Analysis/Fourier/HeightLayers.lean`. All Lean analysis is at the text level; Lean was not built. Full structured output is in `family.json`: 44 paper items, 29+ Lean items, labels, invoked theorems, architecture, eureka candidates, audit.

## 1. Main statement

**Thm main** (`01-introduction.tex:94-103`): for every complex-valued f ∈ L log L(𝕋), there is a measurable null set N_f such that S_N f(x) → f(x) off N_f, along the full sequence N = 0, 1, 2, …. Here L log L = {∫|f| log(2+|f|) dμ < ∞} and μ = dx/2π.

*Paraphrase:* the classical L log L sufficiency conjecture for a.e. convergence of Fourier series, in full.

**Corollary** (`11-fourier.tex:357-392`): with the Luxemburg norm for Φ(t) = t log(2+t),

  sup_λ λ·μ{S\*f > λ} ≤ C‖f‖_Φ.

This is proved via Stein's 1961 continuity principle. It is exactly Lie's **Conjecture 1** (JEMS 2017, "L log L is a C-space"). I verified the wording against arXiv 1408.4783v2, where it appears as "Definition 1 / Conjecture 1".

**Relation to known results.** The claim sits strictly inside the open gap.
- Positive side, previously known: Sjölin (L log L log log L), Antonov (L log L log log log L), Arias de Reyna (QA), Carro–Mastyło–Rodríguez-Piazza, Lie 2013, Di Plinio–Fragkos 2025.
- Negative side: Konyagin 2000 constructs everywhere-divergent Fourier series in φ(L) whenever φ(u) = o(u√(log u/log log u)). That does not reach u log u, so there is no contradiction.
- Konyagin is **not cited**. Nor is Lie's heuristic that the maximal Lorentz C-space might be L√(log L).
- Because L² ⊂ L log L and the proof never invokes Carleson, Hunt or time-frequency analysis, the paper also contains a **new, independent proof of Carleson's theorem**. The Lean imports only Mathlib, not the `carleson` library pinned in the manifest.

**Comparator** (`ComparatorChallenges/FourierLLogL.{json,lean}`; formalization.yaml:1237-1239). Target `OAI.FourierLLogL.paperMain`; permitted axioms propext, Quot.sound, Classical.choice; nanoda off.
- The statement uses AddCircle(2π) with `haarAddCircle`, `AEStronglyMeasurable f`, `Integrable (‖f x‖·log(2+‖f x‖))`, and a measurable null E. Off E, the sum over `Icc (-N) N` of `fourierCoeff f k * fourier k x` tends to f x.
- **Exact match** with Thm main: normalized measure, symmetric sums, full sequence, limit f itself, complex-valued.
- The solution is `PaperMain.lean:8-19` → `Main.lean:25` (`almost_everywhere_fourier_convergence := main_of_grid Dyadic.gridProof`).
- Formalized but not compared:
  - `weak_L1_maximal_bound` (Main.lean:36), proved by a re-proved Stein-type argument rather than via Stein's theorem;
  - `maximal_good_sets : GoodBound`;
  - `Dyadic.GridBound`.
- Claimed but not formalized as stated:
  - Prop dyadic in full generality (arbitrary multipliers ε_j, arbitrary d, stopping time at e^{4h}). The Lean proves only the case actually used.
  - The paper's specific parameter choices.

## 2. Trust surface

grep over FourierLLogL, HeightLayers and the challenge:
- `sorry` 0 (except the challenge stub), `axiom` 0, `native_decide` 0, `implemented_by` 0, `extern` 0, `unsafe` 0, `opaque` 0.
- `admit`: only two false positives (the lemma name `scale_admit`).
- `set_option`: 7 × `linter.unusedSectionVars false` and 1 × `maxHeartbeats 600000` (Compress/Search.lean:8).
- `decide`: about 29 uses, all Bool coercions or numeral checks, so there is no search.
- Classical choice is used only for decidability and to pick a `PieceLaw` (Procedure/Play.lean:27).

**Not computer-assisted.** Clean at the text level. Compilation and the comparator run are not verified by us.

## 3. Labels

| Axis | Label | Evidence | Conf. |
|---|---|---|---|
| A | **A1** (∀f ∈ L log L, a.e. convergence). The headline is qualitative; the key estimates are quantitative (Cd per layer; Lean C = 10^222). | 01:96-97 | high |
| B | **B1**. Not "full only with prior results": Stein is used for the corollary only, and the Lean re-proves it. **Adds corollaries**: Lie's Conjecture 1, and a new proof of Carleson. | 01:131-132; 01:129-130 | high (as a claim) |
| C | Primary **C4** (one long estimation chain: entropy, Fisher and likelihood budgets → Cd). Secondaries: **C1** (constructed devices: procedure, labels, lists), **C2** (iterated procedure with inductive caps; refinement search), **C5** (Stein, corollary only). | 06:41-45; 06:277; 11:384 | med-high |
| C flags | computer-assisted **no**; **ih_strengthened yes**, template **"carry an extra tracked quantity"**: each branch carries form A, count n, charge Q, radius r and gap potential (06:83-91). The Lean `Fund.Ok` bundles 8 tracked invariants (Procedure/Capital.lean:31-40). | | med-high |
| D | **D3, provisional** (cluster I26/I27 + I12/I22 + I29/I30). Provenance flag: **false**; all 23 references are human literature. | | medium |
| E | See below | | |

**E. Fields.**
- **Problem field:** Real and complex analysis (overview.tex:224); MSC 42A20, 42A50, 42B25, 42A24.
- **Lean-dir field:** Analysis.
- **Method fields:**

| Method field | Tag | What it supplies |
|---|---|---|
| Harmonic analysis | essential | dyadic Haar shifts, Petermichl–Hytönen averaging, Dirichlet/Hilbert kernels, maximal function |
| Information theory | essential | entropy, KL, mutual information, chain rules, Pinsker |
| Probability | essential | supermartingales, Ville, change of measure, exchangeability/pinning |
| Statistical mechanics | essential | Griffiths–Ginibre, free energy, Gibbs variational principle |
| Additive combinatorics | essential | Chang/Lee dissociated spectra, sumsets, Riesz products, Bohr-type balls |
| Convex analysis | essential | finite duality; Hahn–Banach in the Lean |
| Functional analysis | corollary-only | Stein's principle, Orlicz spaces |
| Extrapolation / time-frequency | background-cited | context only |

This gives 5 essential non-harmonic-analysis fields. 5 of the 8 invoked citations come from outside harmonic analysis, and all except Stein are re-proved.

## 4. Proof architecture

1. **Layers** (11:279-353). Split f into layers e^{2^j} ≤ |f| < e^{2^{j+1}} and normalize to ρ_j ≤ e^{d_j}. Then Σ m_j d_j < ∞ ⇔ L log L. On the good sets G_j = {Mρ_j ≤ (log d_j)^4}, Borel–Cantelli applies because Σ(log d_j)^{-4} < ∞. Everything reduces to **Thm good-set**: ∫_{G_ρ} sup_N |S_N ρ| ≤ C·d.
2. **Fourier transfer** (11:42-227).
   - Write S_N via the Riesz projection and modulated Hilbert transforms.
   - The truncated cot-kernel equals (1/πc) times the translation+scale average of a **delayed Haar shift**, up to bounded error and an inner window bounded by M ρ ≤ (log d)^4. Here c = −1/8.
   - So Thm good-set follows from **Prop dyadic** (06:10-49): a stopped, modulated, delayed Haar shift satisfies ∫ max_u |…| ≤ Cd uniformly in depth and number of frequencies.
3. **Entropy compression** (Secs 3-4). From a uniform bound on noisy 2T-fold frequency sums, get a subset S′ (log-size loss d²/(E h²)) and a centre x₀ whose phase defects are small on one common region, **for every weight on S′**. The steps:
   1. Gibbs-dual noisy-sum law;
   2. pinning to nearly i.i.d. blocks;
   3. thinning;
   4. a **two-visit-order refinement search** with entropy cost O(h^{-2});
   5. phase extraction.
4. **Thermal labels and spectral update** (Sec 5).
   - The input point Y carries a noisy label Z = Y + θ, with θ ∝ e^{−A} and A a ferromagnetic cosine form (Griffiths–Ginibre).
   - Separated high label-weighted frequencies lead either to a *regular* test, paid later by likelihood evidence e^{−t/8}, or to a *cheap* update.
   - A cheap update lowers the **gap potential** F(A) − log|B_A(r)| by k_b/2.
5. **Procedure and budgets** (Sec 6). Membership splits produce live and static plateaus. Per branch, Σk_b + Σt ≤ Cd and n ≤ Ch. Membership surprisal is O(h) in L², plateau weights are O(h), transfer has probability O(h^{-10}), and the **global label Fisher sum is O(d)**. This is where information charged under the true input law becomes an output-path bound.
6. **Capture and snapshots** (Sec 7): signed-span frequency lists via Riesz-product entropy increments, edge charges, snapshot refresh by relative entropy, and one miss block.
7. **Paths** (Sec 8):
   - predictable-sign (Ville) inequality;
   - scalar Bellman-type potential ψ;
   - a delayed vector estimate whose Fisher-sum coefficient is **absolute** (concavity of |(W, f, λM)|);
   - checkpoints, and simultaneous bounds over representatives and dyadic caps.
8. **Assembly** (Sec 9): O(d/h) per live plateau × O(h) total live weight + static/transfer O(d) = O(d).

**Lean route** (top chain). GridBound → UnitTreeBound → AffineTreeBound → RealGoodBound → GoodBound → `main_bound_consequence` → `paperMain`. Differences from the paper:
- finite grid ZMod(2^M), with a good-set majorant W shared by all u instead of the stopping time;
- d = 2^j only, threshold (j+1)^3;
- **no Hilbert transform**: a direct Dirichlet-kernel comparison, `Fourier/Good.lean:59`;
- frequency rounding when rescaling tops (`Affine.lean:121`);
- trigonometric-polynomial approximation instead of Fejér means;
- padded layer masses (the log⁻ lemmas in HeightLayers are dead code);
- a Stein-type corollary re-proved.

In the Compress and Thermal layers:
- compression is proved over an arbitrary finite abelian group, with Hahn–Banach replacing explicit Gibbs duality;
- finite information theory is home-built (`Finite/`), with no Mathlib KL;
- parameters differ: h ≈ log j/1000, L = d·2^{2^h}, k_b linear, search schedule 2^{16h};
- the constants are explicit: 300000·D², 10^16, 10^222.

The procedure is an inductive tree `Play` (rest / freeze / ticket / jump / attempt) over `Scene` states (Procedure/Play.lean:90). Its existence is `plant` (Procedure/Tree.lean:58).

## 5. Eureka candidates (provisional; quick literature checks only)

**1. Thermal noisy labels + two-law Fisher-sum identity (I26, I27, I10). N3, F1 (F5 flavour).**
- *For:*
  - A new random variable Z = Y + θ that appears nowhere in the goal or in L. Its Fisher information along uniform output paths is globally O(d) by the entropy chain rule.
  - The decoding identity ∫χ_n 𝔞^s = c_A(n)c^{s+n} recovers each modulation.
  - This is the closest thing in the corpus so far to a literal extension variable.
  - Searches found no information-theoretic or noisy-observation proof of Carleson-type bounds. Every known proof (Carleson, Fefferman, Lacey–Thiele, Lie, Di Plinio) is time-frequency combinatorics.
- *Against:*
  - Noise smoothing plus Fisher information is standard information theory (de Bruijn identity, stochastic localization), so a judge could call it transfer (N2).
  - It pays off only together with the rest of the cluster (chain depth > 1).

**2. Entropy compression lemma + two-order refinement search (I12, I22). N3, F3 (I22: F4).**
- *For:*
  - The conclusion is uniform over all weights on S′, which allows choosing the weight later.
  - The cardinality loss is calibrated to the endpoint.
  - The search buys an O(h^{-2}) entropy cost.
  - The Lean isolates the search as a reusable abstract `Arena` (Compress/Search.lean).
- *Against:*
  - It belongs to the Chang's-lemma family. The paper names Lee 2017's entropy-maximization argument as related.
  - Its pinning step is a known lemma (Montanari 2008; Raghavendra–Tan 2012) and is uncited.
  - A judge may say "entropy variant of Chang", i.e. N2.

**3. Gap potential F(A) − log|B_A(r)| + regular/cheap spectral update (I29, I30). N3, F4/F3.**
- *For:* a monovariant mixing free energy with the packing entropy of a Bohr-type ball. It charges cheap updates to regular ones and closes the k_b and count budgets.
- *Against:* density/energy-increment potentials on Bohr sets are a known template (Bourgain, Sanders, Bloom), and the monotonicity is Griffiths–Ginibre transfer, so this could be N2.

**4. Prop dyadic as a statement (I32). N3/N2, F5.**
- *For:* the right finite target. Every difficulty flows through it (GridBound in Lean).
- *Against:* it is essentially "the conjecture on a dyadic tree"; Walsh/dyadic models of the Carleson operator are standard.

**5. Delayed vector norm estimate with absolute Fisher coefficient (I40). N2.**
- This is a Bellman/concave-potential argument (Burkholder; Nazarov–Treil–Volberg).
- Adding the λM coordinate is a templated "track an extra quantity" move.

**Transfer and N0 items.** Griffiths–Ginibre (I25), the Chang/Lee sumset bound (I28), Petermichl–Hytönen averaging (I43), Ville (I37), Stein (I08) and the layer decomposition (I07) are all N0 or N1 transfer. The candidates form one cluster: *read frequency structure through a noisy observation of the input point and pay for it in information*. They should probably be scored together.

## 6. Correctness

I read every section. The reduction layers check out:
- layer summation;
- bounded inputs;
- the kernel constant c = −1/8 (which the Lean's `kappa_integral` reproduces independently);
- the cot/Hilbert comparison;
- the Stein corollary.

Spot checks in Sections 3-4 also pass: the duality formula, the telescoping of prefix entropy deficits, thinning error ≤ 3ε, and search cost O(h^{-2}). The claim is consistent with Konyagin's lower bound and with single-layer examples (S\* ~ d on a large set). **No gap found**, but most of Sections 5-9 is bookkeeping we could not verify line by line.

Residual concerns:
1. **The claim is extraordinary and unreviewed.** It resolves a 60-year problem and re-proves Carleson.
2. **The Lean is the strongest evidence for correctness**: sorry-free, Mathlib-only, exact comparator match. But it was not built here, and it formalizes a different parametrization, so it certifies the theorem rather than each paper lemma as written.
3. **Regular evidence.** The paper's Prop regular evidence asserts a *simultaneous* true-law statement. The Lean Thermal layer proves per-attempt bounds only; see `lean_procedure_notes` in the JSON for where the union step lives.
4. **Missing negative-side context.** Konyagin is not cited, and there is no discussion of why the method stops at L log L. Our reading is that every budget is O(d) and Σ m_j 2^j is exactly ∫|f| log|f|, so the method is calibrated to L log L and does not "prove too much".
5. **Prop dyadic in full generality** (arbitrary ε_j) is not formalized.

## 7. Extraction friction

- The core objects are not in definition environments or `\emph`: the labels, the gap potential, plateaus, J_p and snapshots appear in display math or prose.
- Lean names are whimsical: Scene, Play, Fund (`wage`, `mood`, `bank`), Festival, Gross, Troupe, Frost, Lamp, Wire, Pulse, `annual`, `yieldA`.
- The Lean proves a different sufficient finite statement with different constants, so paper and Lean items do not join one-to-one.
- `OAI.Release075.main` belongs to a different family (hyperbolic groups).
- The extractor's candidate_defs list is dominated by plumbing.
- The proof never cites Carleson, so a citation-based field extractor would mislabel the dependence.
