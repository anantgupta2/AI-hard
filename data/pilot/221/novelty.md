# Family 221: novelty analysis ("The Mézard–Parisi formula for diluted spin glasses")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

**Inputs.**
- `trace.json`/`.md`. This is the only prior analysis: there is no family, paper, Lean or F1 file for 221.
- The preprint source (`build/main.tex` + 11 sections, about 14.9k words) and its 18-entry bib.
- A file-level import DAG of `lean/OAI/Probability/DilutedSpin` (405 files), which I computed.
- Web checks of the 2025–26 citations and the nearest literature.

**L** = Mathlib d13f23b, which has no spin-glass content, plus 221's bibliography. **L⁻** is L without `OpenAIThreeSAT2026`.

## 1. Provenance verdict: **no**

| Cited 2025–26 work | AI disclosure | Contains the candidates? |
|---|---|---|
| BCS25, Biswas–Chen–Sen, arXiv:2410.15599 (v1 Oct 2024) | none found in the abstract or metadata | absent. It covers RS regimes only |
| Concetti25, arXiv:2508.17049 (v1 Aug 2025) | none. The comments note only an overlap with the author's 1908.03820 | absent. It gives a full-RSB ≤ finite-RSB bound on random regular graphs; equality is conjectural there |
| OpenAIThreeSAT2026 (openai/math, dated 27 Sep 2026) | **model-produced** (same release) | absent. A grep for charging, fresh split, canceled anchor and branching depth is negative |

- **OpenAIThreeSAT2026.** It is cited only in a remark (`consequences.tex:131-138`). It is dated 4 days *after* 221 and uses a different trial functional, so it is not a dependency.
- **Web searches.** I searched "Mézard–Parisi" + diluted + ChatGPT / GPT-5 / OpenAI / AI-assisted. The only hits were the release itself and press coverage of it. No model-produced prior work exists on this problem.
- **Nearest human precedent.** Panchenko 2016 (arXiv:1406.4702, in L) proves the MP ansatz for *finite-RSB* asymptotic Gibbs measures after a small perturbation. It states that a description of general full-RSB measures is "still missing" (summarizer quote, unverified). 221 avoids that step by building finite auxiliary hierarchies into the construction.
- **Caveats.** The quotes came through WebFetch's summarizer. zbMATH, Google Scholar and MathOverflow were not queried.

Flag: **no** strict dependence and no model-produced precedent. There is one model-produced *citation*: a later-dated companion, used in a remark only.

## 2. Candidates and final grades

The candidate list merges three sources: the trace's E1–E6, the pivots PV2–PV8 and PV10–PV11, and items I extracted from the paper. All tests are in the JSON.

**Test 3 caveat.** The Lean shares come from file imports, not a declaration DAG, so they are inflated. Every item clears 20% except C10. Load-bearing status was therefore judged by knockout on the paper's architecture.

| # | Item | T1: nearest neighbour | T2 | Final | F | conf |
|---|---|---|---|---|---|---|
| **C1** | **Shift S→S⁺ + charging fresh splits** (Lemma `tree:charging`; "Shifted copies", J=κ(S⁺)²) | none found. Cousins: GG/AC stochastic stability, Barra–De Sanctis, Panchenko 2013/15/16, Barbier–Panchenko; the generic general-position habit | pass | **N3 (provisional; T4 pending)** | **F3** (F5 flavour) | 0.40 |
| C2 | Tree insertion calculus, canceled-anchor expansion, κ(S) | MP01 App. A, PT04 §5, RPC calculus (named by the paper) | fail (borderline) | N2 | – | 0.65 |
| C3 | Depth-selecting Rademacher marks → prescribed-tree identities | GG98, AC98, Barra–De Sanctis 2007, Pan13 (named) | pass (weak) | N2 | – | 0.60 |
| C4 | Conditional-covariance induction v_N(S,d) + three-copy bound | Barbier–Panchenko 2022 (induction on replicas) | pass (weak) | N2 (templated cap) | – | 0.70 |
| C5 | Marker anchor variance identity | the S₀=1 instance of the paper's own Thm `pert:tree-identity` | fail | N1 (trace said N2) | – | 0.60 |
| C6 | Q_k random-tree law for the log expansion | RPC replica-sampling law (nested PD/CRP; Q₂ matches exactly) | fail | N1 (N0 if k≥3 is verified) | – | 0.60 |
| C7 | Depth-averaged concentration + martingale-energy continuity | pinning lemma (Montanari; Coja-Oghlan et al.); parameter averaging (GG, Panchenko) | fail (borderline) | N2 | – | 0.55 |
| C8 | Cavity reservoir with built-in auxiliary hierarchy | ASS03, De Sanctis 04, Pan13, Mourrat–Panchenko | fail | N0 | – | 0.75 |
| C9 | Recursive law encoding + independent-message comparison | Panchenko 2016 Thm 2; Austin–Panchenko; COP19 | fail (borderline) | N1 | – | 0.55 |
| C10 | All-plus normalization upper bound; first-moment reduction | FL03, PT04 | fail | N1 | – | 0.70 |

Excluded from grading:
- PV1, which is strategic;
- the b2→b3 insight backtrack, which is retrieved (N0);
- Efron–Stein (N0);
- Cor. `comp:bounded-lower`, which is a by-product result rather than a device.

### Why C1 survives, and how weakly

**For N3.**
- C1 makes a syntactically tiny change: add one to every internal target depth. The shifted target vertices then cannot coincide with the old tree's branching depths, so each one must be paid for by a fresh unary split with coefficient −δ.
- That matches the δ per vertex in the normalizer κ(S⁺)² ~ δ^{2b}. Without the shift, errors are amplified by δ^{−2b} after division. With it, they are bounded by C_{k,η}.
- So C1 has a **qualitative error-budget signature**, which 287's C2 lacked.
- The paper names antecedents for everything around C1 (GG98, AC98, Barra–De Sanctis 2007, Pan13, MP01, PT04, ASS03) but none for the shift.
- I found no neighbour in the spin-glass, sparse-graph or Bayesian strong-RS literatures.
- **Test 3 (knockout).** C1 is knockout-essential for the entire lower bound. In Lean, ShapeCharging has a down-share of 0.80 and ShiftedTree 0.67.

**Against.**
- C1 sits **one inference from the trace's learned clause C10**: "errors after division do not carry the normalizer's δ". The trace states C10 three times before the shift.
- The trace reaches C1 by conflict-driven propagation, which PLAN.md reads as evidence of reachability.
- "Move to general position" is a generic habit.
- C1 pays off only inside the paper's own tree calculus (chain depth 2), so it may turn out to be a one-off device.

## 3. Discoverability protocols (Test 4, not run)

**Models and contamination control.**
- Training cutoff before **2026-09-23**. No precedent for C1 exists earlier, so the paper date is the binding constraint.
- **Excluded sources:** the whole openai/math release (including OpenAIThreeSAT2026), its Lean library, the 221 trace PDF, and press coverage of the release.
- Each model must pass a canary probe. The model that produced 221 runs only as a reference arm.

**P-C1 (decisive).**
- **Hide:**
  - Lemma `tree:charging`;
  - the worked delayed-split example at `trees.tex:316-330`, which leaks the idea;
  - the "Shifted copies" paragraph and its figure;
  - everything downstream: the k≥2 induction step, the concentration theorem, the comparison and the lower bound.
- **Give:** the tree calculus, Thm `pert:tree-identity`, v_N, the contractions lemma, the depth-continuity lemma and the one-leaf case.
- **Arm A:** also state clause C10. A high hit rate is expected, since the pivot distance is 1.
- **Arm B (decisive):** withhold C10.
- **Hit criterion:** any device that forces each target branching vertex to be created by a fresh unary split, with a relative absolute-cost bound uniform in L, plus a return to the original depths. Accepted forms include any fixed shift, depth choices disjoint from the old branching depths, or another general-position scheme.
- **Lean targets:** `prescribed_history_charging_bound`, `shifted_twin_target_count`.
- **Sampling:** k = 1…256.
- **Controls:** C5, C6 and C10 are the negative controls; Cook–Reckhow ER variables are the positive control.

The trace places C1 at pivot distance 1 from C10, ≥2 from L, with chain depth 2. P-C2 (tree calculus and marks) is specified in the JSON.

## 4. Family verdict

**family_D: D3 (provisional), confidence 0.40.** It rests on C1 alone.

It falls to **D2** if any of the following holds:
- Test 4 arm B clears the calibrated threshold;
- an expert identifies the shift/charging device as known in RPC or stochastic-stability computations;
- a compression check shows that the small-normalizer division can be avoided.

The result is unrefereed, and Lean was not compiled.

**Bridge novelty.** There is no new cross-field bridge. Every import is a known route within probability and statistical mechanics:
- the ASS cavity scheme carried to diluted models;
- RPC power-mean hierarchies;
- stochastic-stability identities, here with new devices;
- the pinning-lemma martingale pigeonhole.

The Bayesian strong-RS transfer was attempted in the trace and failed.

## 5. Open questions

1. Ask an expert (Panchenko, Talagrand, Chen, Mourrat or De Sanctis) whether the shift/charging device is folklore. This is the main risk to C1.
2. Verify that Q_k equals the RPC replica-tree law for k ≥ 3.
3. Compile the Lean, check the comparator, and build a declaration-level DAG.
4. Run the step-3b compression check on `prescribed_history_charging_bound`, and attempt a shift-free variant.
5. Re-run the absence searches on zbMATH, Google Scholar and MathOverflow, and check the WebFetch quotes against the PDFs.
6. Ask whether 221 and the 3-SAT companion came from the same run.
