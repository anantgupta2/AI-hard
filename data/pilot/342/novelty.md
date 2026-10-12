# Family 342: novelty pass (Donaldson's tamed-to-compatible conjecture)

- **Analyst role:** novelty
- **Date:** 2026-10-12
- **Corpus:** `openai/math` at fd4aeeb
- **Inputs:** `family.json` and `family.md` (there is no trace and no f1 file), the Oct-6 preprint, family 341's §1 and §4 (for the reuse check only), Lean spot reads (not built), and `data/items/342_lean.json`
- **Machine-readable version:** `novelty.json`

## Verdict first

**Provenance flag: no (confidence 0.75).**
- 342 cites four works from 2025–2026:
  - LinZhou2025, arXiv 2503.15939;
  - WZZZ2025, arXiv 2412.18361;
  - LiNing2026, arXiv 2607.18778;
  - Kinnunen2026 lecture notes.
- Snippet-level summaries show no AI disclosure for any of them, and none contains C1–C5.
- The only model-produced work cited is the companion family 341, which is dated a day *later* and depends on 342. That makes it reuse, not precedent.
- Searches for the problem together with ChatGPT, GPT-5, OpenAI or "AI-assisted" found nothing.
- **Access caveat:** WebFetch could not resolve any host, and the proxy blocked arXiv for curl. All external evidence is therefore WebSearch snippets, and no quote is verified.

| ID | Item | Final | Conf. | Lean-backed |
|---|---|---|---|---|
| C1 | Thm 5.1, closedness of the positive-density part P_E = 1_{θ>0}P | **N2** (F3 if ever promoted) | 0.70 | **Partial.** The role is in Lean, the statement is not. |
| C2 | Residual pairing (Sec 7, Lemma 8.5) | N2 | 0.75 | Yes |
| C3 | Angular energy estimate (Q ∈ L², I_r ≤ Cr⁴) | N2 | 0.70 | Yes |
| C4 | Lean-only log-activation exceptional set (L02) / radial defect (L03) | N2 / N0 | 0.60 | Yes (Lean-only) |
| C5 | Quadratic mass growth (Prop 3.1) | N1 | 0.75 | Yes |

**family_D = D2 (confidence 0.7).**
- It rests on C1 at N2. There is no N3 item, so nothing joins the Lean shortlist.

## C1: Thm 5.1 stays N2

**The statement.**
- P is a positive superposition of unit complex-line bivectors, and Q ∈ L² is anti-invariant.
- Only P+Q is closed.
- Two bounds are assumed: μ(B_r) ≤ Cr² and the angular moment I_r ≤ Cr⁴.
- Conclusion: θ exists everywhere, and 1_{θ>0}P is closed.

**Nearest neighbours:**
- **Siu 1974 with Skoda / El Mir.** For a *closed* positive (1,1)-current, the positive-Lelong part is Σλ_j[C_j], which is closed. This is a close variant with the same conclusion.
- **TWZZ 2022, App. B.2, Lemma B.17 (in L).** It gives Siu-type level sets for *closed* positive (1,1)-currents on almost-Kähler / tamed 4-manifolds, the same manifold class as 342. This is the nearest neighbour inside L, and 342's remark under Thm 5.1 does not mention it.
- **Elkhadhra 2014, Lemma 1 (in L, and the paper's own contrast).** It gives 1_A T = m_A[A] for closed positive T and J-analytic A. Close variant.
- **Bellettini 2011/2014.** For positive-(1,1) normal *cycles* in any almost complex manifold, it gives almost-monotonicity, density everywhere and tangent cones. Close variant for Lemma 5.2; genuinely different for closedness.
- **Alessandrini–Bassanelli 1996, Bassanelli's cut-off theorem 1994, Dabbek–Elkhadhra–El Mir 2003, and arXiv 2606.29680** (June 2026, not cited: Siu's theorem for positive dd^c-closed currents).
  - Together they show that weakening closedness in Siu/Skoda statements is an established direction.
  - Their hypotheses differ (integrable J, dd^c conditions).
- **Ingredients:** Demailly 1992, plus GMT (Allard/Simon monotonicity, Preiss tangent measures, slicing).
  - For general normal currents the restriction is *not* closed: a segment plus a diffuse return flow is a counterexample.
  - So what the statement really uses is positivity on complex lines plus the angular bound.

**Why it is not N3.**
- The conclusion is a known theorem form, and its closed-current version for exactly this setting is in L.
- The item is a hypothesis weakening ("P closed" becomes "P+Q closed, Q ∈ L²") with a new proof.
- The original part is the balance r^{-3}·√I_r·√N_r = r^{-3}·O(r²)·o(r) = o(1). This is a Cauchy–Schwarz pairing of two moments the argument already controls. It is a sharp, short estimate, not a jump.
- The Lean reaches the same role by a second classical route (C4). That weakens a "hard to find" reading.

**What would promote it to N3:**
- an expert search that finds no closedness theorem for positive currents that are closed only modulo an L² correction. The places to look are Taubes's SW⇒Gr analysis, semicalibrated cycles, and TWZZ App. B and 2606.29680 read in full;
- and P-C1 staying below threshold.

**Lean backing.** `concentration_restriction_closed` together with `ConcentrationActivationData` proves closedness of the restriction to the *exceptional set of summable log-activations*.
- The angular × transverse balance itself is in Lean: `separating_current_angular_transverse_limit`.
- Not in Lean: θ, E = {θ>0}, tangent measures, and the weaker abstract hypotheses. Every Lean lemma also assumes `hann` (P annihilates closed invariant forms).
- A Lean speedup test would therefore use the exceptional-set form, which is specialised to separating currents.

**Test 3.**
- `concentrationActivationData_nonempty`: dominated share 0.084 (rank 2), closure 96%.
- `concentration_restriction_closed`: closure 10.9%.
- The analyst estimates the core at 10–20% of the 4,240-node DAG. On that basis the cluster is roughly 40–80% of the core, so it **passes**.

**Test 2: borderline.** The conclusion's form is in L (Elkhadhra 2014, TWZZ App. B); the hypothesis is not.

**Reuse by family 341: this is device reuse, not a corollary, and the evidence is weak.**
- 341 §4 re-proves "closed density weights", explicitly "shared with [342, Thm 5.1 and Sec 6]", for its own class separators.
- It then turns normalized positive-density thresholds into integral J-holomorphic cycles (Preiss + Rivière–Tian) to prove a curve criterion for taming classes. That criterion does not follow from 342's Thm 1.1.
- But it is the same model, the same release and the same setting. 341 also has no Lean, so this reuse cannot enter a Lean speedup test.

## Other candidates

- **C2 (N2).** This is the almost-complex, real-variable form of "the zero-Lelong (diffuse) part pairs non-negatively" (Demailly 1992), inside the Lamari/Buchdahl intersection argument.
  - It is what removes the h_J^- = b^+ − 1 restriction of TWZZ, WWZ and WZZZ.
  - The idea is the template's; the hard part is C1.
- **C3 (N2).** The Lamari/Buchdahl identity 0 = T·T, with Hodge-resolvent smoothing in place of Demailly regularization. The self-duality of anti-invariant forms (Draghici–Li–Zhang, TWZZ) is N0, and the angular identity is a single line of algebra.
- **C4.**
  - L02 is N2: summable log-cutoffs with a null exceptional set are a Borel–Cantelli / capacity trick.
  - L03 is N0: it is the Allard/Simon monotonicity excess.
- **C5 (N1).** Lelong-type monotonicity (Elkhadhra–Mimouni 2007 in L; Bellettini).
- **Excluded:**
  - N0 background: separation (Sullivan, Harvey–Lawson, Li–Zhang), Hodge resolvent, heat kernel;
  - the closed lift (N1, Lejmi);
  - the Sec 8 cones: the cone theorem I30 is N2, follows from C1+C2, and is not formalized.

## Bridge novelty

Every import is a **known route**:
- Pluripotential theory to almost-complex 4-manifolds: TWZZ, WWZ, Lin–Zhou, WZZZ, Elkhadhra.
- Cone duality: Sullivan, Harvey–Lawson, Li–Zhang.
- GMT to positive (1,1) currents: Bellettini, Rivière–Tian, Taubes.
- 4D self-duality: Draghici–Li–Zhang, TWZZ.
- Hodge-resolvent / heat-kernel regularization: classical smoothing of currents, and only a minor new use here.

No new bridge was found.

## Discoverability protocol (P-C1; not run)

- **What to hide:** Secs 5–8, the intro sketch from "To remove that error" (`01-introduction.tex:151-201`), and the Elkhadhra remark.
- **What to give:** Secs 2–4, plus the diagnosis that "the self-pairing only bounds ‖Q‖₂".
- **Context:** L⁻ = Mathlib digest + bibliography minus 341. It keeps Elkhadhra 2014 and TWZZ App. B, because they are in L.
- **Models:**
  - training cutoff before 2026-09-23 (the Sep-23 manuscript), with a canary probe;
  - the release's OpenAI model goes only in a reference arm;
  - an optional arm with cutoff before 2026-06-30 (2606.29680).
- **Sampling:** n = 256, pass@k for k = 1…256 in powers of 2.
- **Hit criterion:**
  - the proposal splits P by 2-density or concentration (E, or the Lean exceptional set);
  - **and** it claims closedness of the restriction when only P+Q is closed.
  - Partial credit, recorded but not counted: a split without the closedness claim, or closedness justified only by analytic structure.
  - A second score records whether the balance estimate appears.
- **Controls:**
  - positive: Cook–Reckhow (format), and the Siu step in Lamari/Buchdahl (in-domain);
  - negative: C5 and the closed lift.
- **Trace data:** no trace exists. Estimated pivot distance ≈ 1 from L; chain depth 2.

P-C2 and P-C3 are given in short form in the JSON.

## Open questions

1. Read TWZZ App. B.2 in full. This is the main risk to C1's grade, in either direction.
2. Read 2606.29680: authors, AI disclosure, method.
3. Check Taubes's SW⇒Gr analysis and the semicalibrated-cycle literature for a "closed modulo L²" restriction theorem.
4. Verify the snippet claims once arXiv is reachable.
5. Check whether `globalConcentration_current_control` needs `hann` essentially. If it does not, an abstract Lean Thm 5.1 (exceptional-set form) could be extracted.
6. Decide how same-model companion reuse (341) counts toward the PLAN's tally.
7. Correctness: the result is unrefereed, and the Lean is trusted as published, not built.
