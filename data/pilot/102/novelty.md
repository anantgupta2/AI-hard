# Family 102: novelty analysis ("The Unique Games Conjecture and optimal approximation thresholds")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

**Scope.** The trace leads only to the manuscript *The Unique Games Theorem* (2026-09-23). Grading covers that manuscript. The four direct-reduction manuscripts (Max-Cut, Vertex Cover, Min-UnCut, DFVS) are out of scope.

**Inputs.**
- This family has only `trace.json`/`.md`. There is no `family.json`, no Lean-analyst file and no `f1_*.json`.
- I extracted the candidates myself from the preprint source:
  - `00-introduction`, `01`, `02-latent` read in full;
  - the key statements of `03`–`07`.
- Sibling check: the same-release companion *Perfect completeness for 2-to-1 games*.
- Lean spot checks of `lean/OAI/Computability/UniqueGames/`.

**L** = Mathlib d13f23b plus the manuscript's 42-entry `references.bib`. That bib includes 3 OpenAI companion preprints. **L⁻** removes those 3, for contamination control.
- Khot–Moshkovitz 2016, Croot–Lev–Pach and Lovett appear in the trace's references, **not** in L.

**Quote caveat.** Web material came through WebFetch/WebSearch summarisers, so treat all web "quotes" as unverified paraphrase. Bash had no network. zbMATH, Google Scholar and MathOverflow were not queried directly. Absence claims read "no neighbour found".

## 1. Provenance verdict (first)

**Flag: PARTIAL. It does not build on a model result. It has a model-produced *sibling*, and no external model-produced precedent was found.**

**2025–2026 human preprints in the bibliography.** Neither discloses AI assistance on its arXiv abstract page.
- **Minzer–Zheng**, arXiv:2404.07441v4 (v4 2026-05-13, "STOC 2024, 106 pages"). It is the framework source for correlated advice.
- **Ellis–Kindler–Lifshitz**, arXiv:2209.04243v2 (v2 2026-01-22, "46 pages"). It is context only.
- Neither contains the latent gadget.
- KMS17 and DKKMS25 are the ToC 2025 journal versions of human STOC 2017/2018 work.

**Cited OpenAI companions.** All three are model-produced, from the same release.
- *Perfect completeness for 2-to-1 games*. The footnote says "It is not an input to this proof." It does, however, share C2's **architecture**:
  - a recursive tree whose internal spaces are spanned by products of pairs of child functions;
  - a random root-to-leaf path with fresh randomness ("recursive-product redesign", 02-construction.tex:436–440).
  - The object and purpose differ. Both papers are dated 09-23, and their relative order is unknown.
- *Uniform sparsest cut* and *Gaussian propeller*: separate applications, cited only in §7.

**Close human contemporaneous work: Fei–Minzer–Wang, ECCC TR26-179 (2026-09-14).**
- It covers 4-to-1 games with perfect completeness. Quadratic equations appear only in its outer PCP.
- It has no nonlinear decoder.
- Quanta (2026-10-07) reports it was posted early, after rumours of the OpenAI result reached Minzer on 2026-09-11.

**Web search** ("Unique Games" + ChatGPT / GPT-5 / OpenAI / AI-assisted).
- It turned up only coverage of the 2026-10-06 release: Quanta, Aaronson's "The Mathocalypse", and Fortnow's TCS list, which says the work was produced by an "unreleased internal model".
- One earlier **AI-first platform** page exists: ProofAtlas, "status checked 2026-08-06". It pursues an unfinished *tensor-rank-one* verifier programme for UGC. That is the BKS degree-3 route, which the trace also tried and dropped (POS1 c3). It contains no gadget.

## 2. Final grades

| # | Item | Nearest neighbour(s) | T1 | T2 | T3 | Final | F | conf |
|---|---|---|---|---|---|---|---|---|
| C1 | Latent separation concept (`lem:latent` as a statement, used as the rank-one test's noise) | Khot–Moshkovitz 2016 real-code noise test (named in the trace at L250, one sentence before adoption); BKS18 §1.6 higher-degree tests | close variant (strategy) | pass | pass (knockout) | **N2** | – | 0.55 |
| C2 | **Explicit quadratic gadget** (see the four components below) | Khot–Saket quadratic code; low-degree/short codes; Cremona map (object only); recursive-majority leaf decay; 2-to-1 companion (model-produced sibling, architecture only) | **no near-equivalent found** | pass | pass (knockout) | **N3 (provisional)** | **F3** | 0.45 |
| C3 | Generic spaces (≤3r alignments) via square-root monomials + Schwartz–Zippel | Schwartz–Zippel (in L); inseparable-extension independence | close variant | pass (weak) | inside C2 | N1 | – | 0.55 |
| C4 | Harmonic rank potential + fresh orientations | coupon-collector H_r potentials; random change of basis | equivalent device | fail (borderline) | inside C2 | N1 | – | 0.65 |
| C5 | Spectral comparison (Λ_g ≤ 7/8 → low-rank mass) | KMS Lemma 2.10 spectrum | close variant | fail | bridge | N1 | – | 0.70 |
| C6 | Exact reduced keys + folding | Khot–Safra 2013 virtual tables, BGS folding (paper: "adapts") | close variant | fail | pass | N1 | – | 0.75 |
| C7 | Row-fibre advice, erasure, witness transfer | KMS17 §§3.3–3.4, KS13 §3, Minzer–Zheng | close variant | fail | pass | N1 | – | 0.65 |
| C8 | β = k^{−2/3}, clean coordinates, repetition before alphabet | KMS17; Dinur–Steurer; Rao | close variant | fail | pass | N1 | – | 0.75 |
| C9 | Converse: assertion ⇒ UGC (dropped from the paper) | Rao / Khot survey | equivalent | fail | strategic | N0 | – | 0.70 |
| C10 | Inverse shortcode theorem | KMS Thm 1.12 + BKS chart | equivalent | fail | imported | N0 | – | 0.90 |
| C11 | Raghavendra transfer | Raghavendra 2008 | equivalent | fail | corollary | N0 | – | 0.90 |
| C12 | Stability-gap / amplification target | BKS §1.6; KM 2016 | close variant | fail | strategic | N1 | – | 0.60 |

C2's components:
- the block C_blk(x,y) = y + Q(x), with Q = (x₂x₃, x₁x₃, x₁x₂) on F_{2^d}³;
- the update spaces U_A;
- concatenation over all isomorphisms (A, J), with noise at a random leaf;
- quotient and injection enlargement.

**Override of the trace analyst.** The trace analyst gave PV4/EC1 (here C1) "no retrieval" and a provisional N3. I lower it to **N2**.
- Trace L250–251 reads: "Smooth-code alternatives prompted an analogy with Khot–Moshkovitz's Boolean noise test … Nonlinear equivariant decoders became the main alternative."
- So the concept had a retrieval trigger.
- BKS §1.6, which is in L, explicitly asks for a higher-completeness variant of the shortcode test.
- The concept statement amounts to a *specification* of what the KMS machinery needs. The hard part is realising it.

**Why C2 survives.** It is the sole realisation of C1, so it is the only route to completeness 1−ε. Without it, the uniform test keeps an evaluation with probability (1+2^{−ℓ})/2.
- **No neighbour found** in searches covering:
  - nonlinear/equivariant PCP decoders;
  - quadratic codes (Khot–Saket, Dinur–Guruswami, BGHMRS);
  - the Cremona map and quadratic-APN derivatives;
  - the 2-to-2/Grassmann literature;
  - FMW 2026.
- Where those works use quadratic structure, the honest table is linear in the code coordinates. Here the honest answer C(Pz) is **nonlinear in the table**.
- In the trace, the construction appears in one sentence (L307) right after a failed retrieval (Croot–Lev–Pach/Lovett too weak). This is the same pattern as 287.

**Against C2.**
1. Its requirements were spelled out in advance by the model's own lessons:
   - C21: a common parent lift;
   - C22: h(r)/p → ∞;
   - C24: increase branching or mix layers.
2. Each ingredient is standard:
   - Cremona-type map;
   - char-2 trace duality;
   - Schwartz–Zippel;
   - harmonic potential;
   - absorb-per-level recursion, as in recursive majority.
3. A same-day model-produced sibling uses the same recursive-quadratic-tree architecture. That suggests a house style rather than a one-off.
4. The summary may hide search. Trace L164–165 mentions a Kasami–Tokura-guided search for biased multilinear forms.

**Load-bearing evidence.** No paper/Lean DAG exists for 102.
- The Lean line-share proxy is 4.9%: Quadratic/ plus Gadgets/ come to 9,106 of about 186.5k lines.
- That share is depressed by Machines/ (polytime, 55.7k lines) and Inverse/, where KMS is re-proved (18.7k lines).
- Knockout is unambiguous.
- `Gadgets/Final.lean:19` `exists_actual_gadget` formalises the gadget. A grep found no `axiom`/`sorry`, but Lean was not compiled.

## 3. Discoverability protocols (Test 4, not run)

Full specification: `novelty.json → discoverability_protocols`.

**Models.**
- Training cutoff strictly before **2026-09-11**, the rumour date.
- Canary: the model must not know "latent alphabet gadget", the map (x₂x₃, x₁x₃, x₁x₂) in a UG context, or that UGC has been claimed proved.
- No tools.
- The producing OpenAI internal model runs only as an uncontrolled reference arm.
- **Excluded sources:** the openai/math release (including the 2-to-1 companion), Quanta and later coverage, and the ProofAtlas page.

**Context.** L⁻, with an L⁺ arm that adds Khot–Moshkovitz 2016 to measure the retrieval trigger's effect.

**Sampling and judging.**
- n = 256 per arm; pass@k for k = 1…256.
- Two LLM judges, plus a PCP expert who checks all hits and 10% of misses.

**Controls.**
- Positive: Cook–Reckhow extension-resolution variables.
- Negative: C6, C8 and C10.

**P-C1 (concept).**
- **Hide:** Sec. 2 and everything downstream.
- **Hit criterion:** a fixed-alphabet object with all three of:
  1. translation-equivariant nonlinear output;
  2. noise changing it with probability ≤ p;
  3. detection by every linear family of restriction rank ≥ r(p), with r independent of the alphabet.
- Raising the degree of the code (BKS §1.6) is a miss.

**P-C2 (construction).**
- **Arm A (pivot level):** give C1 plus the C21/C22/C24 specification. A high hit rate here would cap C2 at N2.
- **Arm B (cluster level, decisive):** hide C1 too.
- **Hit criterion:** any valid explicit construction meeting `lem:latent` with r* independent of ℓ. These sub-criteria are scored:
  - (a) a nonlinear block whose update spaces cancel the nonlinear term;
  - (b) per-level absorption with controlled rank loss;
  - (c) alphabet enlargement.
- **Trace distances:** pivot distance ≥ 2 from L, and about 1 given the specification; chain depth 2.

**C3/C4.** Scored as sub-criteria of P-C2 Arm A. Both have pivot distance 1 and chain depth 3.

**Trace distances for the other items.**
- C1: pivot distance about 1 from the trace state, ≥ 2 from L alone; chain depth 1.
- C5–C8 and C12: pivot distance 1.
- C9: retrieved converse.

## 4. Family verdict

**family_D: D3 (provisional), confidence 0.45.** It rests solely on **C2**, the explicit quadratic latent gadget.

**It falls to D2 if:**
- P-C2 Arm A or Arm B passes the calibrated threshold; or
- an expert (Khot, Minzer, Moshkovitz, Steurer or Kothari) identifies a known or folklore noise-absorbing equivariant gadget with linear-rank detection; or
- the recursive-quadratic architecture turns out to come from an earlier model-produced source.

**Caveats.**
- All grades are conditional on correctness. The claim is unrefereed and extraordinary.
- No compression estimate exists. C2 is a single-use bottleneck lemma, so a confirmed-eureka verdict would rest on the downstream-speedup test.

**provenance_flag: partial.** Strict builds-on: **no**. Model-produced sibling: **yes** (the 2-to-1 companion, which shares only the architecture).

**bridge_novelty.**

| Import | Verdict |
|---|---|
| Char-2 finite-field algebra (vector quadratic map, trace duality, Frobenius square roots, specialisation) used as a **noise-absorbing nonlinear decoder** in PCP test design | **New bridge** (algebraic codes in PCPs are a known route, but always linear in the table; no precedent found for this use) |
| KMS Grassmann expansion / BKS shortcode → UG soundness | Known route |
| KS13 / KMS17 / MZ outer machinery | Known route (named by the paper) |
| Rao / Dinur–Steurer repetition | Known route |
| Raghavendra transfer | Known route |
| Harmonic potential | Known technique |
| Croot–Lev–Pach / Lovett analytic rank | Considered in the trace, rejected, not used |

## 5. Open questions
1. Verify all web paraphrases (Quanta, ProofAtlas, ECCC, arXiv) against the originals.
2. Ask OpenAI for the run order of the UG and 2-to-1 searches, to settle which construction came first.
3. Put the expert folklore query (above) to Khot, Minzer, Moshkovitz, Steurer or Kothari. This is the main risk to C2.
4. Read Khot–Moshkovitz 2016 in full to see how close the real-code noise test is to C1.
5. Run a Lean-analyst pass on 102: DAG share, step-3b compression for Gadgets/ and Quadratic/, and compiling `theorem11`.
6. Search zbMATH, Google Scholar and MathOverflow.
7. Check whether the Kasami–Tokura search at trace L164–165 is a hidden antecedent of Q.
