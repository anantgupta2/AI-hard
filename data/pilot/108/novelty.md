# Family 108: novelty pass

**Scope.** This is Phase 2, run in the same session as `family.json`. There is no trace and no f1 file. L = Mathlib d13f23b plus the 108 bibliography. Existence was judged against all the literature, including model-produced work outside L.

## Provenance verdict: YES (builds on prior model-produced results)

1. **Cited and built upon.** Sheshadri, arXiv:2606.13628 (June 2026), is the architecture source for the smooth-form border bound.
   - 108 says the kernel-incidence count and Schur reduction "build on" it (polar.tex:9-11).
   - Its acknowledgement, verified in the v2 PDF text: *"The author used the assistance of large language models in all stages of the effort."*
   - Kumar–Volk (arXiv:2609.34462) describe it as "AI-assisted and AI-written" and say they could not verify it.
   - It already states bdc(Σxᵢⁿ) ≥ (n−1)²/(4e) in v1, with the same constant 4e as 108's Thm 2.3.
2. **Uncited architectural precedent (model-produced).** OpenAI, *Ten Advances in Mathematics and TCS*, Ch. 5 (1 Aug 2026). Its abstract reads "results obtained by an internal OpenAI model". It proves a circuit bound for per_n using:
   - an affine specialization of the permanent (a sum of subpermanents M_{t,s,d}, realized by all-ones and roots-of-unity blocks);
   - a critical locus of codimension Θ(n²);
   - a generic linear slice;
   - a degree count.

   It states the next target explicitly: *"construct a degree-d specialization with d growing with n and with k = Θ(n²)"*. 108 hits exactly that target, with degree Θ(k), and swaps the circuit degree bound for a determinantal one. 108 does not cite Ten Advances.
3. **Downstream reuse.** Guo, arXiv:2609.29568v2 (8 Oct 2026; acknowledges Codex GPT-5.6-Sol), reuses 12 Lean declarations from 108 to improve the Ten Advances circuit bound from n² log log n to n² log n. He rebuilt them with only the standard axioms. This is evidence for PLAN step 9 (a held-out problem helped by the item) and partial third-party evidence that the Lean compiles.

## Final grades

| Cand | Item | Test 1 | Test 2 | Test 3 (down / cone) | Final |
|---|---|---|---|---|---|
| C1 | G_D = [sᵠtᵠ] per_k(X+sI+tD) as a linear-size, linear-degree permanent projection with quadratic critical codimension | close variant (Ten Advances M_{t,s,d}, model-produced) | pass vs L; the concept is pre-announced in Ten Advances | pass (0.64) | **N2**, conf 0.60 |
| C2 | char-2 spectral-curve bridge: ∇G_D = 0 ⇒ length Z ≥ T ⇒ δ(C_X) ≥ T ⇒ codim ≥ T−k | no near-equivalent (Ten Advances uses Möbius/power sums; ingredients FGvS, Beauville/AHH, Gałązka, CHT are N0) | pass | pass (0.52 / 0.52) | **N3, F5**, conf 0.40 |
| C3 | smooth-form bound bdc ≥ (r−1)(d−1)/(4e) | close variant (Sheshadri 2606.13628, LLM-assisted, in L) | fail (borderline) | pass (0.33) | **N2**, conf 0.75 |
| C4 | two-gate selector + signed 3×3 gadget | equivalent (Friedland–Levy count gate) / close (Valiant, DHMTW) | fail | borderline (0.13) | **N1**, conf 0.70 |
| C5 | Lean-only Frobenius square-form δ bound + transcendence-degree Severi substitute | proof route new; statement weaker than CHT2023 (in L) | fail (weakening of an L statement) | pass in Lean only (0.34) | **N2**, conf 0.45 |
| C6 | adjugate-generation lemma (H¹ of ker ψ vanishes) | probable spectral-sheaf folklore | pass (weak) | fail proxy (0.03) | **N2**, conf 0.50 |

No templated-strengthening cap applies, because there is no induction.

### Searches behind "no neighbour found" for C2

- Web and arXiv searches on: spectral curves of pencils; permanental singular loci; conductor and adjugate; Kumar/CKSV.
- Full-text greps of the Ten Advances PDF, Sheshadri 2606.13628 and Guo v1/v2.

zbMATH and MathOverflow were not queried directly.

## family_D: D3 (provisional), confidence 0.35

**Rests on C2 alone.** C2 is a new bridge: a permanent coefficient becomes, mod 2, a determinantal pencil, whose spectral plane curve must have δ ≥ C(q+2,2) at critical points. It carries 52% of the Lean target cone and has no alternative path.

**Not transfer.** Each imported tool is N0. The candidate is their coupling to the permanent.

**What would downgrade it to D2:**
- an expert finds a known spectral-curve treatment of critical loci of characteristic-polynomial or permanent coefficients;
- a judge scores C2 as an expert assembly of N0 tools;
- P-C2's directed arm (hint "reduce mod 2") exceeds the threshold.

**What would upgrade it.** C1 rises to N3 (F1) if models given Ten Advances (arm L+TA) still fail to find a linear-degree specialization.

## Bridge novelty

| Import | Classification |
|---|---|
| char 2 → spectral curves, δ-invariant, conductor, Severi → critical locus of a permanent coefficient | **new bridge** |
| polar degree / conormal plus multihomogeneous Bézout → border dc bounds | known route (LMR 2010; Sheshadri 2026, LLM-assisted; Kumar–Volk 2026) |
| critical-locus codimension of a permanent specialization plus generic slice → lower bounds | known route, model-produced (Ten Advances Ch. 5; antecedents ABV, CKSV, GGIL) |
| matching gadgets → coefficient extraction by projection | known route (Friedland–Levy 2006; Ten Advances Lemma 6.1) |
| Spec Z[θ] specialization from char 2 to char 0 | known route |
| Lean: Frobenius p-basis → elementary δ and Severi-type bound | new within formalization (low confidence) |

## Discoverability protocols (not run)

**Common setup:**
- **Models:** training cutoff before 2026-06-01, with canary probes for Sheshadri, Ten Advances and the cubic result. Exclude the OpenAI internal lineage and GPT-5.6-Sol/Codex from the main pool.
- **Library L−:** removes the three 2026 bib entries.
- **Arms:** L−, L+TA (adds Ten Advances), L+S (adds Sheshadri), directed.
- **Sampling:** n = 256 per arm, pass@k for k = 1…256.
- **Judging:** two LLM judges plus an expert.
- **Controls:** Cook–Reckhow ER as positive; C3 and C4 as negatives.

**Per candidate:**
- **P-C1.** Hide G_D and everything downstream; keep Thm smooth-border and the fact codim Sing(per_m) ≤ 2m.
  - Strict hit: a mixed coefficient of a permanent with ≥ 2 shifts, one diagonal shift generic, with a Θ(k²) codimension argument.
  - Loose hit: any linear-size permanent projection of degree Θ(k) with a correct proof of Θ(k²) critical codimension.
  - Pivot distance 1 from Ten Advances, ≥ 2 from L−. Chain depth 1.
- **P-C2.** Keep G_D and the selector; hide the char-2 branch. Arms: open, and directed ("reduce mod 2").
  - A hit needs all four of: char 2 / determinant; a plane-curve (spectral) model; a singularity measure ≥ Ω(k²); a dimension count over curves.
  - Pivot distance 2–3. Chain depth 1.
- **P-C3.** Control grade.

## Open questions

- Does the one-parameter [s^{k−r}] per(X+sI) already give quadratic critical codimension over ℂ?
- Verify CHT2023's characteristic-2 dimension statement for non-nodal curves (the Lean avoids it).
- Does Sheshadri's v1 PDF carry the LLM acknowledgement?
- Was 108 produced by the same model as Ten Advances?
- Why does a manuscript dated 24 Sep cite Kumar–Volk dated 28 Sep?
- Run the comparators at fd4aeeb (Guo built adc7f12).
- Extend the downstream speedup test beyond Guo's circuit corollary.
