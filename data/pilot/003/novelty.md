# Family 003: The quasi-Riemann hypothesis (novelty pass)

Date: 2026-10-10. Inputs:
- `family.json` and `family.md` (phase 1, same agent).
- No trace and no F1 files exist for this family.
- WebSearch summaries only. WebFetch and arXiv were unavailable, so every web claim below rests on a search snippet.
- Lean was read at text level. It was **not compiled**; the orchestrator does that.

## Provenance verdict: **partial** (no model-produced precedent)

- Q cites one model-produced release preprint, family 023 (*An unconditional first moment for cubic Gauss sums*), and states it is "not used here" (Q:124-127). A grep of 023 finds:
  - no sextic Möbius family;
  - no zero-free half-plane;
  - only classical zero-free regions (angular.tex:100-125).
  So it contains none of the candidates.
- A cites Q. S cites no model output.
- Web searches for the problem plus ChatGPT, GPT-5, OpenAI or AI-assisted return only press coverage of this release and arXiv 2608.12257. That preprint's snippet says no LLM-generated argument is used, and its method (Turán power sums) is different.
- **Downstream:** release family 029 (*Primitive roots for every admissible integer base*) **reuses the C1 device** over every cyclotomic field containing μ₁₂. Families 142 and 182 use the theorem only.

## Final grades

| Candidate | Items | N | F | Conf. |
|---|---|---|---|---|
| **C1** Sextic-twist Möbius ↔ cubic-theta duality | A03, A04, A07, A10–A14; Q16–Q18, Q31, Q33 | **N3** | **F5** | 0.45 |
| C2 β\* family bootstrap plus saturated two-witness zero detector | Q03, Q04, Q20, Q25 | N2 | – | 0.65 |
| C3 Compensated probe (11/12 → 7/8) | Q27, Q30 | N2 | – | 0.55 |
| C4 Sixth-power row replication (amplification) | A05, Q33 | N2 | – | 0.7 |
| C5 Strengthened recursive families (HB template) | A09, A11, A14; Q31, Q34 | N2 (templated cap) | – | 0.75 |
| C6 Weighted Frobenius interpolation determinant (Siegel) | S05, S06, S08, S09 | N2 | – | 0.5 |
| C7 Interpolation on a projected integer box | S03 | N2 | – | 0.65 |

**family_D = D3 (provisional), confidence 0.4. It rests on C1.**

It falls to D2 if any of these holds:
- Dunn–Radziwiłł's full text, or Heath-Brown/Patterson, already contains the "Möbius family → theta-coefficient dual" step, even in the reverse direction.
- Test 4 shows the sextic twist is readily proposed once HB00 eq (2) and Littlewood are given.
- The proof fails. This would happen if the A04 mean square is inconsistent with DR's sharpness of the cubic large sieve, or if the Lean compile fails.

## Why C1 survives and C6 does not

**C1.**
- **The device:** twist the Möbius sum by sextic residue symbols over ℤ[ω]. Poisson in the twist then produces sextic Gauss sums, which absorb μ(n) through γ₂(n)³ = μ(n)α(n) and become cubic Gauss sums, i.e. Kubota–Patterson theta coefficients.
- **What follows:** theta reflection gives a quadratic twist, the quadratic large sieve applies, and Heath-Brown recursion closes the estimate. The result is square-root cancellation on average, and p⁶ rows recover the target.
- **Nearest neighbours:**
  - DR 2024: same objects, the opposite direction (Gauss sums at primes), and it needs GRH.
  - HB00 and Hasse: the identity only.
  - Gao–Zhao, arXiv 2212.09241: the quadratic analogue, with no automorphic dual.
  - DFDS, arXiv 2410.03048: same toolbox, central values.
- **Result of the tests:**
  - No equivalent was found.
  - Non-analytic.
  - About 56% of the zeta Lean DAG lies in directories that carry the device (directory-share proxy; extractor dominated shares are diluted to ≤0.15).
- **F5:** it changes the representation of 1/L into theta-coefficient sums.
- **Caveat:** under the strict rule this N3 is fragile, because every ingredient is classical.

**C6.**
- The Frobenius congruence θ^p ≡ σ(θ) (mod p) makes an interpolation determinant divisible by p^{E_p}. This is the **Dobrowolski (1979) / Cantor–Straus (1982)** mechanism for Lehmer's problem (WebSearch summaries of arXiv 2308.16305 and 0908.4024). S does not cite these works.
- The weighted ordering α₁ + H(α₂+α₃) and the √2 adjunction are new design. The application to Siegel zeros is a **new bridge**.
- Grade: **N2** under the strict rule. Upgrade it to N3 (F3) if experts judge the weighted greedy determinant materially beyond Cantor–Straus.

## Bridge novelty

| Import | Classification |
|---|---|
| Cubic metaplectic theta → zero-free half-planes via sextic Möbius families | **New bridge** (moderate) |
| Interpolation determinants / Frobenius divisibility (transcendence, Lehmer's problem) → Siegel zeros | **New bridge** (moderate) |
| Quadratic large sieve after theta reflection | Known route (DR, HB) |
| Spectral theory of hyperbolic 3-space to build the theta function (Lean only) | Known route (Kubota, Patterson) |
| Local Bézout for multiplicity estimates (Lean S) | Known route |

## Discoverability protocols (not run)

**Model requirements.**
- Training cutoff before 2026-09-25.
- Exclude the openai/math families 003, 023, 029, 142 and 182, and all press after 2026-10-06.
- Canary probes check for the 7/8 claim, the A_u(D) family with p⁶ rows, and the biquadratic weighted rows.
- k ∈ {1, 4, 16, 64, 256}.

**P-C1.** Hide A03–A15 and Q16–Q18, Q31, Q33.
- Arms:
  - open: the problem plus L;
  - route: also give Littlewood's equivalence and HB00 eq (2).
- Hit criterion: the proposal embeds the target's Möbius sum (or 1/L) in a higher-order-twist family over ℤ[ω] whose Poisson dual is cubic-theta coefficients, **and** gives a way to recover the target.

**P-C6.** Hide S03–S09.
- Arms:
  - open: the problem plus L;
  - route: add Cantor–Straus as a positive control.
- Hit criterion: a determinant or resultant of conjugates, Frobenius divisibility at inert primes, and an archimedean comparison using the Siegel-zero prime bias.

**P-C2 and P-C3** are controls.

There is no trace, so pivot distances are estimates: C1 about 2 (chain depth 2) and C6 about 2 (chain depth 1).

## Trust notes (from phase 1)

- The zeta comparator is **exactly** the classical quasi-RH with Mathlib's `riemannZeta`, with no extra hypotheses. The Dirichlet comparator covers all characters.
- The Hecke comparator defines its own L-function. Its fidelity rests on library lemmas outside the comparator.
- The Siegel comparator is a trivial corollary of the Dirichlet one, but it is proved independently in Lean.
- The text grep finds 0 `sorry`, `axiom`, `native_decide`, `implemented_by`, `extern` and `unsafe`.
- PNT+ is patched with OpenAI-written Hadamard support files.
- There is no nanoda replay.
- The Lean 7/8 route seems to bypass the paper's 11/12 stage.

## Open questions
1. The orchestrator's compile result. This is decisive.
2. Read DR's full text and decide between C1 at N3 and C1 at N2.
3. Check A04's consistency with DR's GRH-conditional sharpness of the cubic large sieve.
4. Does Lean really skip Part I?
5. Expert opinion on C6 versus Cantor–Straus.
6. Family 029's reuse of the device as a downstream datum.
7. Fidelity of the Hecke comparator's definitions.
