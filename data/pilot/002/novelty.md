# Family 002: novelty pass (BSD formula in Selmer coranks 0 and 1)

Novelty analyst, 2026-10-10, influential-problems pass. Inputs: `family.json` and `family.md` (this pass), the three manuscripts at `fd4aeeb` with their earlier editions, and the dependency on family 006. There is no reasoning trace and no F1 file.

> **Shortlist status.** Family 002 has **no Lean formalization**, so it is **excluded from the Lean eureka shortlist**. The reason is the missing Lean, not merit. The surviving N3 item (C3) goes on `data/eureka_informal.json`. All discoverability and speedup protocols below are at text level only (LLM judge plus expert), and can never confirm a eureka step unless the item is formalized.

## Provenance verdict: **yes (internal)**

- **Internal model-produced dependency.** The headline depends essentially on release-sibling **006**, which is model-produced (first edition Sep 23 2026):
  - M2 uses 006's 2-converse at p = 2.
  - M1 and M2 use 006's twist-density theorem to choose the auxiliary fields.
  - M1 also depends on the companions M2 and M3, which are model-produced too. M1 cites M2 lemma by lemma.
- **No external AI-assisted precedent found.** Three web searches combined BSD, p-converse, Sylvester or Goldfeld with ChatGPT, GPT-5, OpenAI or "AI-assisted". The only hit was a Gizmodo news item about the release.
- **2025–26 human works cited:** Smith 2025, BCS 2025, BSTW 2024, Keller–Yin 2024, BHTY 2026, Yin 2026, Burungale–Tian 2026. Search snippets show no AI disclosure for any of them. The abstract pages could not be fetched (arxiv.org DNS failure), so this absence is unverified.
- **Nearest uncited human precedents:**
  - for the ultralimit device: Sweeting (arXiv 2012.11771, ultrapatching) and Loeffler–Zerbes, *Ultra-Kolyvagin systems and non-ordinary Selmer groups* (arXiv 2511.08793, Nov 2025). The latter uses nonprincipal ultrafilters on auxiliary primes to avoid ordinarity.
  - for the U(3,1) machinery: Castella–Liu–Wan, which the paper names itself.

## Final grades

| id | Candidate | Test 1 | Test 2 | Test 3 | **Final** | conf. |
|---|---|---|---|---|---|---|
| C1 | Heisenberg-commutator Frobenius addressing: controls tame first-order obstructions (M2 strict case; M1 residual concentration and codimension two; M3 tame heights) | No equivalent found. The object is a Mazur–Tate / derived tame pairing; the move is Chebotarev in a Heisenberg (Massey) extension. Close variant by combination. | pass | pass (knockout in all three papers) | **N2** | 0.5 |
| C2 | Ultralimit tame deformation variables and admissible cochains (a p-unramified Iwasawa variable) | Close variants: Taylor–Wiles variables, ultrapatching, Sweeting, Loeffler–Zerbes | pass | pass | **N2** | 0.6 |
| C3 | Real-component detector Θ at 2: ψ(a)+ψ(a)⁻¹ weights on the real circles of X₀(n) under w_n∘c, giving a Hecke eigenfunctional | No neighbour found (Ogg, Snowden and Kriz–Li are genuinely different). Snippet-level only. | pass | borderline (knockout for the real-S₃ branch, ~5% share) | **N3, F3** | 0.25 |
| C4 | Codimension-two divisor removal by adjoining tame directions | Variant of pseudo-nullity / patching. The lemmas themselves are textbook. | pass | pass (knockout for M1's exact center) | **N2** | 0.55 |
| C5 | Tame-height route to Perrin-Riou's log² formula at every p and reduction type | Statement known (BDV, Venerucci, Büyükboduk). No tame route found. | partial | pass | **N2** (new bridge) | 0.5 |
| C6 | U(3,1) theta implication / theta-to-cusp congruence over k[t]/tᵇ | Close variant of Skinner–Urban and CLW (named by the paper) | pass | pass | **N2** | 0.7 |
| C7 | Conjugate Bockstein alternation at 2 | Poonen–Stoll / Flach technique | pass | pass | **N2** | 0.7 |
| C8 | Pfaffian cofactor lift with repeated factors | Pf(DBD) = det D · Pf B (textbook) | fail | pass (branch) | **N1** | 0.8 |

Excluded with reasons (see JSON):
- the pair-discrepancy sandwich, which is the **N0** template of JSW, Zhang and Skinner;
- the "two incompatible lengths" contradiction (Skinner–Urban template);
- finite models and switches (N1);
- integral Kato classes and BDP measures (N0/N1 transfer);
- the 2-descent graph models (N1);
- the Sylvester corollary (also claimed by Kriz 2022, Yin 2026, and arXiv 2609.14893);
- the unused M2 appendix.

## Family D

**D3 (provisional, weak), confidence 0.25.** It rests on C3 alone. The most likely final label is **D2**.

C3 would fall, and D would drop to D2, if any of the following happens:
- an expert finds a known Hecke-equivariant functional on real components (component-group theory of Mazur, Ribet or Edixhoven; real Heegner points);
- the project rules that a single-branch knockout fails Test 3;
- Test 4 shows easy rediscovery;
- the real-S₃ argument is wrong.

D3 would firm up if C1 were upgraded. C1 is the device actually reused across the whole family and the best target for informal speedup.

## What is genuinely new relative to prior BSD results

- **The statement.**
  - Full BSD for every E/Q of analytic rank ≤ 1, implicit in M1 Prop 10.x.
  - The p-converse at every p.
  - With 006 and Smith: full BSD for a density-one set of twists.

  Before this, the p-part was known only under hypotheses on p (≥ 3 or ≥ 5; good ordinary or supersingular; semistable), on E[p] (irreducibility plus ramification), or in CM / Eisenstein / multiplicative settings. The literature covers Skinner–Urban, Zhang, JSW, CGLS, Keller–Yin, BCS, BSTW, Castella, Burungale–Flach and LTYZ. The prime 2 was known only in families. If correct, the newly covered cases are:
  - **p = 2** in general;
  - **p = 3**;
  - **additive primes**, especially potentially supersingular ones;
  - primes dividing c_E or Tamagawa numbers;
  - residually reducible p with bad reduction;
  - CM rank 1 at odd p.
- **How the uniformity is obtained.**
  - The p-adic Iwasawa variable is replaced by a **p-unramified tame variable** (C2). The local condition at p is therefore only the Kummer line, with no ordinarity input.
  - Residual hypotheses are replaced by **residual concentration**, driven by C1.
  - The analytic side uses BDP measures on the ordinary locus of the *modular curve*, not ordinarity of E.
  - At p = 2, a four-way split by the image of E[2] is used, including the new detector C3.
- **Existing machinery, all transfer (N0–N2):**
  - Gross–Zagier, Kolyvagin, Kato and Burungale–Flach;
  - Rubin and Johnson-Leung–Kings;
  - the JSW / Zhang pair template;
  - the Skinner–Urban / CLW congruence method on U(3,1), with Labesse and BGHT for the Galois side;
  - BDP measures;
  - ultrapatching;
  - Poonen–Stoll alternation.
- **Not used:** Bhargava–Skinner–Zhang (66%), and Tamagawa-number-conjecture results beyond the Bloch–Kato determinant language.

## Bridge novelty

| Import | Status |
|---|---|
| Theta / Eisenstein congruences on unitary groups → Selmer lower bounds | known route (Skinner–Urban, CLW) |
| Ultrafilters → Galois cohomology | known route (ultrapatching, Sweeting, Loeffler–Zerbes) |
| TW-type tame variables → Iwasawa-style Selmer complexes with Greenberg conditions | **new bridge (candidate)** |
| Mazur–Tate tame heights → Perrin-Riou formula | **new bridge (candidate)** |
| Real components of modular curves → 2-adic Heegner primitivity | **new bridge (candidate)** |
| Determinantal codimension → main-conjecture units | known route (pseudo-nullity) |
| Twist-nonvanishing densities → auxiliary fields | known route |

## Discoverability (Test 4, not run; text-level protocols)

**Models.** Only models with a training cutoff before 2026-09-23, the first edition of 006. For C2, also split results at Nov 2025 (Loeffler–Zerbes). Contamination controls:
- run a canary probe on the contents of 002 and 006;
- no retrieval;
- keep the OpenAI release lineage only as a reference arm;
- use a judge from a different model family, with expert spot-checks.

**Design.** k ∈ {1, 4, 16, 64}, with two arms:
- Arm A (undirected): the problem, L⁻, and the paper up to the item;
- Arm B (directed): Arm A plus the item's sub-goal.

| Protocol | Hit criterion | Pivot | Chain depth |
|---|---|---|---|
| **P-C1** | The proposal uses u([g,g′]) = the alternating form on ker(G → GL V) to shift γ so that H_γ ≠ 0. | low, once H_γ is written down | needs C2 |
| **P-C2** | Moving-prime characters of growing p-power order are packaged into one limiting variable, with cohomology over k[t]/tᵇ. | low for models that know TW patching or ultrapatching | low |
| **P-C3** | A class-group-character-weighted, Hecke-equivariant mod-2 functional on the real components of the w_n∘c-twisted Jacobian, nonzero on the Heegner trace. | high | medium |
| **P-C4** | Enlarge the tame parameter space so that simultaneous jumps have codimension ≥ 2, then conclude a unit. | moderate | high |
| **P-C5** | Tame derivative of Kato classes = Mazur–Tate tame height, evaluated via a tame Gross–Zagier formula. | moderate | medium |

**Informal speedup targets** (JSON): for C1, the p-converse for higher-weight forms at non-ordinary p, Kolyvagin's conjecture at Eisenstein or additive primes, and Hilbert-modular residual concentration; for C3, 2-adic primitivity for other real-S₃ curves and RM abelian surfaces. Corollaries of the family's own theorems are negative controls.

## Correctness and trust (carried over)

- About 22k unrefereed lines, essential dependence on unreviewed 006, and no Lean, code or trace.
- The ultralimit cohomology framework is unconventional. Its uniform bounds are justified briefly (M1 03:121-129).
- The deep automorphic and Galois steps were read only at statement level.
- Editing artefacts:
  - the unused M2 appendix cites an undated weighted-fundamental-lemma draft;
  - M1's Oct-3 edition had a dangling `\cite{Dv}` to a "removed supporting manuscript";
  - the 2-converse is proved twice (006 and M3).

## Open questions

1. Is the proof correct? This needs expert reading of M2 Secs 4–9 and M1 Secs 7–9.
2. Does 006's 2-converse already use C1? If so, C1 is a cluster device dated Sep 23.
3. What was "Dv"?
4. Is there a component-group precedent for C3?
5. Is C1 in Zhang, Sweeting, Loeffler–Zerbes or Smith (full-text check needed)?
6. Verify the AI-disclosure status of the 2025–26 preprints.
