# Family 107: ω ≤ 9/4 (novelty pass)

**Analyst:** NOVELTY agent, 2026-10-10. The Lean was read at text level only and was not compiled by me.
**Literature access:** WebFetch failed (DNS errors) on arxiv.org and alphaxiv.org. Every external claim below rests on WebSearch result summaries and is snippet-level. None of the external wording is quoted verbatim.

## Provenance verdict: **partial**
- **Within-family model precedent.** M1 (9/4, Oct 2) runs on the separation device first stated in the family's own M2 (Sept 24) as the "pairwise label separation" (GROUP) lemma. M1 uses a Fourier/square-weight form; M2 uses a Behrend-sphere form. M1 does not cite M2.
- **External AI-assisted work.** Dupont et al., arXiv 2608.16884 (AlphaEvolve-assisted, ω < 2.371177).
  - All three manuscripts cite it, but only as the numerical record.
  - M3 works inside the ADVXXZ v3 framework, whose table credits Dupont's parameters. M3's own mechanism is not taken from Dupont.
  - The candidates are absent from Dupont et al.
- **ChatGPT/GPT-5.** No ChatGPT- or GPT-5-assisted precedent for matrix multiplication was found.
- **OpenAI "Ten Advances" (Aug 1, 2026).** According to the search summaries, it contains no matrix-multiplication or tensor result.

## Final grades
| id | candidate | N | F | conf. |
|---|---|---|---|---|
| C1 | Lossless shared-leg separation via an auxiliary Fourier/group tensor, with a retained dot product (M1 Prop 3.1 / Cor 3.2; M2 GROUP lemma) | **N3** | **F3** | 0.55 |
| C2 | Symmetrized polynomial-multiplication profile P(a,b) and its discrete growth | **N3** | **F1** (F4 also defensible) | 0.50 |
| C3 | Discrete concavity via the Clebsch–Gordan determinant filtration | N2 | – | 0.5 |
| C4 | Shifted tripling via a three-sector degeneration | N2 | – | 0.5 |
| C5 | Viscosity-type comparison for attainable values (M2 square route; not in Lean) | N2 (new bridge) | – | 0.5 |
| C6 | Readable label trees and the conditional-entropy bound | N2 (templated) | – | 0.6 |
| C7 | Fixed-point proof of Strassen duality (detecting characters) | N1 | – | 0.6 |
| C8 | Cross-depth joint extraction and staggered lots (M3) | N2 | – | 0.7 |
| C9 | Completion operation on W-partitions | N2 | – | 0.5 |

**family_D = D3** (confidence 0.55). It rests on C1, with C2 as a second N3 at chain depth 2. Both are Lean-formalized and inside the 9/4 comparator cone, so both are eligible for the Lean shortlist.

**What would downgrade D3 to D2:**
- an expert finds the shared-leg entropy inequality for all spectral points, or an equivalent device, in prior work;
- the Lean fails to compile, or the proof breaks;
- protocol P-C1 shows easy discoverability.

## C1: the key device
**Statement.** Take T = Σ_h A_h with a shared X-leg and matched, disjoint Y and Z sectors. Then 5M copies of T degenerate to ⊕_h A_h ⊗ B_X(M):
- Fourier phases force u − v + 2(g − h) = 0;
- the weights g², hu − h², −hv then make the total weight (g − h)².

Consequently, λ(Σ T_i) ≥ e^{p_X H(q)} ∏ λ(T_i)^{q_i} for every spectral point.

**Test 1: neighbours.**

| Neighbour | Verdict |
|---|---|
| CW Salem–Spencer hashing and the combination-loss line (DWZ, VXXZ, ADVXXZ, Dupont) | Same problem, but solved with a loss: different |
| Cohn–Umans / CKSU group algebras | Shared ingredient, different use |
| Strassen's quadratic-weight degenerations | Component |
| Behrend spheres | Component |
| Support/quantum functionals | Their entropy formulas give the inequality only for those known spectral points |
| Alman–Li 2026 "Strassen calculus" | Different |
| Family M2 | Equivalent (model-produced) |

No external near-equivalent was found.

**Test 2: analytic check.** Pass. The device is not a subterm of the goal or of L, although every ingredient is in L.

**Test 3: load-bearing.** Pass.
- It is a cut vertex of the 9/4 Lean cone. Its sub-cone is 25% of all tokens, or about 41% of the mathematical core.
- Every M2 bound also passes through it.
- Budget-drop signature: from CW₁ alone it gives 2.2901 with a page of counting. That is below the AFLG 2.3078 limit for zeroing-out laser analyses, while the standard route took decades of heavy optimization to reach 2.371.

**How the barriers are evaded.**
- **AFLG** covers zeroing-out extraction from CW powers. C1 instead degenerates T^{⊗n} ⊗ A_G, with the auxiliary rank charged and then cancelled by the output multiplicity.
- **Alman / CVZ irreversibility.** For CW₁ I compute an irreversibility of ≈ 1.084, giving a barrier of ≈ 2.168. M2's 2.29 and 2.258 are consistent with it.
- **M1** works with C(a,a), whose irreversibility tends to 1, and its argument is dual. No known barrier applies.
- These barrier numbers are my own computations from Strassen's formula for tight tensors.

## C2: the profile
P(a,b) = (∏_{π∈S₃} λ_π(C(a,b)))^{1/(6t)}. Concavity and shifted tripling give P(a,a) ≥ a^{4/3}; comparing with the rank bound (2a−1)^{1/t} gives t ≤ 3/4.

**Neighbours.**
- Strassen's spectral program is a known route.
- Alman–Li 2026 is the closest methodological neighbour. It is not cited by M1 and contains no profile.
- Le Gall's symmetrization is a component.

**Tests.**
- Test 2 passes.
- Test 3 passes: the tripling and concavity sub-cones are 35% and 30% of the cone.
- Chain depth is 2, because it needs C1.

## Bridge novelty
| Import | Classification |
|---|---|
| Strassen duality → ω upper bound | Known route; first record bound by it, as far as searched |
| Abelian Fourier analysis → separator | Known route (Cohn–Umans), new purpose |
| SL₂ Clebsch–Gordan → degeneration of polynomial multiplication | New bridge |
| Viscosity PDE → laser-method values | New bridge |
| Behrend, method of types | Known routes |
| Fixed-point theorem → spectral points | New route to a known theorem |

## Discoverability (protocols only, not run)
**Eligible models.** Training cutoff before 2026-09-24. The OpenAI internal lineage is excluded from the main pool and run only as an uncontrolled reference arm. Canary probes check for knowledge of M1, M2 and the GROUP lemma.

**k values:** 1, 4, 16, 64, 256. Proposals are judged by Lean statement equivalence against `finiteSeparation_bound`, `sharedFirst_tag` and `symmetrizedProfile` where possible, otherwise by an LLM judge.

**P-C1.** Hide C1 and everything downstream. Three arms:
- open: improve ω;
- directed: separate a shared leg with minimal loss;
- hinted: as directed, with the hint "Fourier copies plus a quadratic weight".

A proposal is a hit only if a pairing on the two knowing legs is retained. Pure hashing is a miss.

**P-C2.** Three arms:
- conditional on C1 being revealed;
- directed with the hint "use C(a,b)";
- unconditional (C1 also hidden).

Hits are scored in two tiers: any scalar spectral growth argument that beats 2.371, and the strict P(a,b) profile with both inequalities.

## Correctness and trust
- I checked M1 by hand and found no error. I verified the separation identity numerically and checked the inequalities against the flattening-rank characters.
- Residual concerns:
  - the work is unreviewed, and I found no expert verification;
  - the Lean compile is pending (orchestrator);
  - the 9/4 proof trusts an external Brouwer package;
  - M1 is over ℂ only;
  - M1 cites neither M2 nor any barrier paper.

## Open questions
- Is the universal shared-leg inequality implicit in Strassen's 1988/1991 spectral laser theorems? The fetches failed, so I could not read them.
- Is there an equivalent quantum-information protocol, where a GHZ resource turns a label held by two parties into a direct sum plus an EPR pair?
