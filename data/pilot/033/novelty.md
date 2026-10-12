# Family 033 novelty pass: Iitaka subadditivity, variation, and logarithmic additivity

Novelty analyst, 2026-10-12. Corpus `openai/math` @ `fd4aeeb`. Structured version: `novelty.json`. There is no trace and there are no `f1_*` files. Lean was not built or run; the release's Lean is trusted as published.

**Access caveat.** WebFetch failed with DNS errors for arxiv.org, adsabs and researchgate. Every external claim below therefore rests on WebSearch snippets plus domain knowledge, and none of the external papers was read in full.

## Verdicts up front

**Provenance: yes (within the release).**
- REV and VAR are built on the model-produced ORB:
  - REV's additivity uses ORB's log subadditivity.
  - VAR uses ORB's subadditivity, its adjoint comparison (C1) and its reduced-root refinement.
- VAR's projective C⁺ corollary also uses OpenAI's *Log abundance in characteristic zero* (family 034, Cor. 11.2).
- That 034 paper in turn uses ORB's ordinary subadditivity. This is a mutual citation with a date anomaly: 034 is dated 09-24 and ORB 09-26.
- No model-produced precedent outside the release was found. Searches for Iitaka / C_{n,m} together with ChatGPT, GPT-5, OpenAI or AI-assisted returned only the release itself (aggregator pages listing it as unreviewed) and a Manifold market.
- The device C1 originates inside this family (ORB/ORD/REV), not in earlier model output.

**Final grades**

| id | Item | N | F | conf | Lean-backed |
|---|---|---|---|---|---|
| C1 | Adjoint positivity of the entire highest Hodge line on the full-period quotient (M = p\*L, K_S+jL big) via strict rank loss on boundary and ramification divisors | **N3 (provisional)** | F3 + F5 | 0.40 | **no** → informal list |
| C2 | Adjoint-addition interpolation | N2 | – | 0.75 | no |
| C3 | Analytic birational-constancy criterion (VAR) | N2 | – | 0.65 | no |
| C4 | Marked periods, Higgs-tail line, period-twist removal (REV) | N2 | – | 0.70 | no |
| C5 | Section construction with retained zero + zero test (REV) | N2 | – | 0.75 | partial, off the comparator DAG |
| C6 | Tangential rank principle | N2 | – | 0.70 | no |
| C7 | Log-general-type addition in class C | N2 | – | 0.70 | no |
| C8 | Exact rank-one comparison / least-index root cover | N1 | – | 0.70 | no |
| C9 | Kähler b-semiampleness via product covers (BSA) | N2 | – | 0.70 | no |

**family_D: D3 (provisional), confidence 0.40, resting on C1 alone.**
- It is not Lean-backed. The comparator certifies only REV's trivial negative-fiber branch.
- C1 therefore goes on `data/eureka_informal.json`, not on the Lean shortlist. This agent did not edit that file.

## The decisive precedent check: BFMT 2025 (arXiv:2508.19215)

**What BFMT proves** (snippets):
- The Griffiths bundle extends amply to a Baily–Borel-type compactification of the period image, so it is semiample.
- The Hodge bundle of a Calabi–Yau VHS is semiample "under extra conditions". One snippet gives these as *integrable with torsion combinatorial monodromy*.
- From this, BFMT deduce the Prokhorov–Shokurov b-semiampleness conjecture, using Ambro and Kollár's minimal lc centres to verify those conditions.

**Does BFMT imply or contain C1? On current evidence it does neither.**
- Prokhorov–Shokurov, and Ambro's 2005 Thm 3.3 (M = h\*A with A nef and big), both assume the **boundary is effective over the generic point**.
- The Iitaka κ(F)=0 reduction produces a sub-boundary that is **negative on the generic fibre**.
- The papers say this explicitly. ORB `introduction.tex:295-297` and `reduced-root.tex:236-240` state that they use BFMT Thm 6.28, the Hodge = moduli identification, which permits negative coefficients. They do not use Thm 1.5 (semiampleness), which needs generic effectiveness.
- If BFMT's CY conditions could be verified for root-cover VHS, then M would be semiample and C1 would become a trivial corollary, because a big L makes K_S+jL big. No one claims this, including BFMT, who do not claim C_{n,m}.
- So BFMT supplies the *machinery*: the transcendental part (Def 2.9), Lemmas 2.16 and 5.6, Thm 6.28, and the picture in which boundary strata have lower dimension. It does not supply the *statement*.
- This is the main downgrade risk, and it needs an expert query.

**A side note on Ambro 2005.** Abundance would survive a generically finite base change, because κ and ν are invariant under it. So the family analyst's objection "breaks K_W" is not the real obstruction. The real obstruction is effectivity.

## C1 in detail

**Test 1 (neighbours).**
- BFMT: machinery, not the statement.
- Ambro 2005 / Fujino–Gongyo: the stronger conclusion, but only for an effective generic boundary.
- Brunebarbe–Cadorel: K_S + D big. This is an ingredient; C1 replaces D by jL.
- Brunebarbe 2020 (level covers increase positivity): related boundary absorption, but a different mechanism.
- Mumford 1977, Bakker–Tsimerman 2018, Kawamata's Siegel-space argument: the locally symmetric template. There L is big and the statement is easy. C1's content lies in the case ν(L) < dim S, which has no analogue there.
- Viehweg–Zuo, Popa–Schnell, Campana–Păun: these keep the log boundary and need maximal variation.
- Tsuji and Maehara: different methods, per the papers; their full texts were not read.
- No equivalent statement was found in any of the searches listed in the JSON.

**Test 2: borderline pass.**
- The need for positivity of M at κ=0 is analytic: it is the classical obstruction.
- The specific weakened target is not a subterm of L. That target is adjoint bigness on the *full* period image, rather than semiampleness or bigness of L, together with the rank-loss lemma.

**Test 3: pass (knockout).**
- C1 is the single new input on every route to C_{n,m}, the orbifold conjecture and Popa's conjectures. Four of the five papers depend on it.
- It has no Lean declarations (DAG share 0).
- It is a single point of failure: about 1,000 unverified lines.

**Test 4: not run; protocol P-C1.**
- Pivot distance is estimated at ≥2:
  1. Choosing S as the full period image.
  2. Formulating strict rank loss on N≠0 and finite-inertia divisors.
- Chain depth is 2–3 (C8 → C1 → C2 plus weak positivity plus KP).

**Reuse.** The device is reused across four manuscripts of the same family. Family 034 uses the *theorem*, not the device, so that is corollary-type reuse and does not count.

## Other candidates (short)

- **C2.** Follows Campana *Orbifolds* Prop 6.6 and Viehweg's addition over a general-type base. The paper names this itself (`adjoint-addition.tex:63-66`). Graded N2.
- **C3.** The paper names Cao–Guenancia–Păun 2023 Thm 1.2 (flat direct image ⇒ local triviality in the K-trivial klt case). VAR extends this to κ=0 fibres with zeros of the top form by contracting pole divisors. Graded N2.
- **C4 and C5.** Variants built on Viehweg–Zuo and Popa–Schnell.
- **C6.** The constant-rank theorem.
- **C7.** A setting extension of Kovács–Patakfalvi.
- **C8.** ORB says its cyclic extension *is* BFMT's Construction 6.23. Graded N1.
- **C9.** BFMT transferred to Kähler via MWWWZ.

## Bridge novelty

| Import | Status |
|---|---|
| VHS → Iitaka addition | known route (Kawamata, Viehweg–Zuo, Ambro, Popa–Schnell, BFMT) |
| o-minimality → moduli part | known route (BFMT is that bridge) |
| Period-image hyperbolicity (BC) → Viehweg-type addition, using the period image as a twisted general-type base | **new bridge (no precedent found)**, recorded separately; not a jump by itself |
| Andre normality / adjoint groups → rank loss | known route |
| L² / Bergman metrics → isotriviality | known route (CGP23, Păun–Takayama) |
| Galois/étale descent; integral-closure algebra | known route |
| MWWWZ product covers → Kähler b-semiampleness | new application, low significance |

## family_D: what would downgrade it

The label falls to **D2** if any of the following happens:
- (a) An expert verifies BFMT's CY-Hodge conditions for root-cover VHS with a negative generic sub-boundary, which would make C1 a corollary.
- (b) A K + jL boundary-absorption statement is found in BFMT §§5–6, in Brunebarbe 2020 or in arXiv:2608.22682. None of these was read in full.
- (c) P-C1 arm B hits at the calibrated rate.

If the rank-loss proof is wrong, the family's claims collapse altogether, not just the grade.

**Correctness caveat.** This is an extraordinary, unreviewed bundle of claims: C_{n,m}, C⁺_{n,m}, Campana and Popa. A Manifold market (search snapshot) puts the bundled log-abundance and Iitaka claims at about 34% "shown flawed before 2027".

## Discoverability protocol P-C1 (summary; full version in JSON)

- **Models:** training cutoff before 2026-09-10, with a canary probe; exclude the release's model.
- **Context L⁻:** the cited statements with every OpenAI preprint removed.
- **Arm A:** give the reduction plus the C1 statement and ask for a proof.
- **Arm B (decisive):** give the reduction plus "b-semiampleness unavailable (negative generic boundary); find a sufficient positivity statement for M and prove it". Mention neither period-image bases nor adjoint bigness.
- **Arm C:** the problem alone.
- **Hit:** M = p\*L with K_S + jL big, without assuming semiampleness or abundance, with the boundary removed by lower ν. Proposals that keep the log boundary or assume abundance are misses.
- **Sampling:** n = 256 per arm, pass@k for k = 1…256.
- **Judging:** two LLM judges plus an algebraic geometer.
- **Controls:** PHP-ER as the positive control; C2 and C8 as negative controls.

## Open questions
1. Put the BFMT expert query on the CY conditions for root-cover VHS (decisive).
2. Read BFMT v2, Brunebarbe 2020 and arXiv:2608.22682 in full.
3. Get an expert to read the rank-loss proof.
4. Settle ORB's class-C use of projective weak positivity.
5. Add C1 to `data/eureka_informal.json`.
