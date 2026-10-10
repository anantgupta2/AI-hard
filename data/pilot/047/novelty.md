# Family 047: novelty analysis ("Zariski cancellation and affine fibrations over ℂ")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`, which uses the 287 keys with `precedent_checks` as a list.

Inputs:
- `family.json`/`.md` (paper and Lean analyst, with sympy checks);
- the preprint source (`build/main.tex`, sections 01–07, `references.tex`);
- the sources of sibling family 049;
- web checks (listed below).

Family 047 has **no reasoning trace and no F1 file**.

**L** = Mathlib d13f23b plus 047's 26 bibitems. No item in L is model-produced, so L⁻ = L.

## 1. Provenance verdict first

**Provenance flag: NO.** 047 builds on no model-produced result, and no model-produced precedent was found.

- **The only 2025–26 citation** is Gaifullin–Petrov, arXiv:2607.13593v1 (2026-07-15, human authors).
  - Its abstract page shows no AI disclosure.
  - It concerns *generalized* cancellation: maximal tori and the Makar-Limanov invariant of cylinders.
  - 047 cites it only to say that the char-0 problem is still listed as open.
  - It contains none of the candidate items.
- **Uncited 2025–26 neighbours** were also checked. None has an AI disclosure, and none contains a candidate item:
  - Dubouloz–Ghosh 2501.09613: Koras–Russell-type A¹-contractible varieties of dimension ≥ 4. Their ML is nontrivial, and their cylinders are *not* shown to be affine space; the authors call them only "potential counterexamples".
  - Wendt–Wittich 2607.17716: a rectifiability invariant for A¹ ⊂ A³.
  - van Dobben de Bruyn 2608.27341.
  - Venegas² 2512.15590 (survey).
- **Model-produced catalogues.** I extracted the text of both documents locally:
  - OpenAI's *Ten Advances* (updated 2026-08-06) contains no affine-geometry cancellation item.
  - Sra's "GPT, the Counterexample Machine" (2608.29595) lists ten AI-disproved 2026 conjectures, and none is ZCP, the Stable Coordinate Conjecture (SCC) or Dolgachev–Weisfeiler.
- **Adjacent model-assisted work, not flagged.**
  - Alpöge's degree-7 Keller map refuting the Jacobian conjecture in dimension 3 (July 2026; secondary reports attribute it to Claude Fable 5; there is an Isabelle AFP entry). It is in the same field, but it is a different problem, shares no item, and is not cited.
  - Sibling family **049** (OpenAI, 2026-10-05) is *downstream* of 047. It cites 047 as `Cancellation2026` and says it "adapts the construction in [Cancellation2026, Sections 2–6]". It uses the same quadric, the same SL₂ bundle, and v = a³b + a²u² − d².
- **Searches** for ZCP together with ChatGPT, GPT-5, OpenAI, AI-assisted or LLM found nothing before the 2026-10-06 release. The three withdrawn release preprints are not in this family.

**Access caveat.** arXiv abstract pages went through WebFetch's summarizer, so the "no AI disclosure" findings are unverified. The following were text-extracted locally, so their quotes are verbatim: Gupta's ICM survey, Sra's paper, OpenAI's ten-proofs PDF and Arzhantsev–Gaifullin.

## 2. Final grades

| # | Item | Nearest neighbour (T1) | T2 | T3 | Final N | F | conf |
|---|---|---|---|---|---|---|---|
| C1 | **Witness H** (I01 + design facets) | Asanuma's ring B = R[T][X,Y,Z,U,V]/(TᵈU−f, TᵈV−g) and the affine-fibration route in GuptaSurvey (in L): **close variant of the template, different object**. Also Gupta's char-p xᵐy=F, Danielewski-type pⁿu=Q, Russell cubic, Dubouloz–Ghosh, Vénéreau: all different | **pass** vs the posed problem; trivially analytic vs the formal goal | vacuous (down 0.87) | **N3 (provisional)** | F3 | 0.45 |
| C2 | Principalization through SL₂→SL₂/T plus the LND lift (I19–I22; Lean L07–L09) | Arzhantsev–Gaifullin 2010 Thm 5.1 (lift automorphisms to the Cox ring, where divisors become principal); ADHL *Cox Rings*; Brion (in L) | pass (weak) | knockout; lift dominated 0.20 | **N2** (borderline N1) | – | 0.75 |
| C3 | Extraction lemma: E²(v)=0, shift ≤ 0 (I24–I25; L11) | Freudenburg degree functions; Finston–Maubach L1.1; Kaliman–Zaidenberg LNDs on modifications | pass | knockout; 0.127 with rigidity | **N2** | – | 0.60 |
| C4 | Weighted rigidity: grading (0,3,−3,0,2), abc, −u³ nonsquare (I29–I33; L14) | Finston–Maubach §2 (named, in L); Crachiola–Maubach | pass | knockout; 0.073 | **N2** | – | 0.75 |
| C5 | Positive-degree invariant (I16; L05) | Gupta 2014, Derksen-invariant strategy (named, in L) | fail (borderline) | knockout; 0.133 | **N1** (↓ from N2) | – | 0.60 |
| C6 | Exact gr A = R[τ, I/τ²] = P/(H_top) (I13; L04) | Standard lemma: a prime top-weight form gives gr = P/(H_top) (Kaliman–Makar-Limanov, Gupta; in L) | fail (borderline) | knockout; carrier 0.229 | **N1** (↓ from N2) | – | 0.55 |

Not graded:
- The stabilization chain (I04–I07), which is an explicit instance of El Kahoui–Ouali, Edo–Vénéreau and Maubach (N0–N1).
- The textbook items.
- The corollaries (N0 given the main theorem).

**Special counterexample issue (Test 2 for C1).**
- H is literally in the comparator `MainStatement`. Against the formal goal, any witness is therefore analytic.
- Per the brief, I judged C1 against ZCP *as originally posed*: ∀A, A[w] ≅ ℂ^[n+1] ⇒ A ≅ ℂ^[n]. H is not a subterm of that statement or of anything in L, so C1 passes.
- What L *does* contain is the search specification:
  - El Kahoui–Ouali reduces the cylinder half to "find a residual coordinate over ℂ[p]";
  - GuptaSurvey displays Asanuma's template and says it is "very tempting to look for possible counterexamples to the affine fibration problem" to get char-0 ZCP counterexamples.
- So the strategy is N0. What is new is the specific design that makes non-polynomiality **provable**:
  - the Danielewski-type twist p³u = xy − z(z+1) of the SL₂/T quadric;
  - a non-principal A²-centre (x = s²+u³, z = sx);
  - a Cox/torsor pullback of that centre to a single v carrying the −u³ nonsquare.
  - No neighbour has any of these.

**Why C1's confidence is below 0.5.**
- The Asanuma template is a close architectural neighbour in L.
- Test 3 does not discriminate for witnesses.
- The claim is unrefereed, and the Lean comparator was not re-run here.

**Overrides of the analyst.**
- C5: N2 → N1. It is a specialization of Gupta's method, which is in L.
- C6: N2 → N1. It is an instance of the standard top-form lemma.
- C2 stays at N2 but becomes borderline N1, because Cox-ring principalization and lifting is a known technique.
- C1 stays at provisional N3, with confidence lowered because of the Asanuma/GuptaSurvey route.

## 3. Discoverability protocols (Test 4, not run)

The full spec is in `novelty.json → discoverability_protocols`.

**Models.**
- Training cutoff strictly before **2026-09-23**.
- Canary probes: the model must not know of a char-0 ZCP counterexample, must not complete H, and must not know 049's f.
- No tools.
- The OpenAI release model runs only as a reference arm.
- Stratify by whether the cutoff is after 2026-07-19 (the Jacobian counterexample), but do not exclude on that ground.

**Excluded sources:** the openai/math repository (047, 049 and the Lean files) and all coverage after 2026-10-06.

**Arms.**
- **O (open):** the problem plus L. n = 1024.
- **R (route):** also give the residual-coordinate route and an abstract obstruction pipeline, without S, R, I, v or the quadric. n = 256. **This arm decides the N3 grade.**
- **D (design):** also give S and R. n = 256. This is the pivot level, and a high hit rate is expected.

**Judging.**
- Two LLM judges, neither of them the proposer.
- CAS checks of the certificates proposals provide.
- An affine-geometry expert reviews all hits and 10% of misses.

**C1 hit criterion.**
- **Tier 1 (strict):** A′ ≅ A.
- **Tier 2 (family, the main metric):** a residual coordinate over ℂ[t] whose localization has the t⁻ᵏQ − tᵐu form over a smooth affine quadric surface, and whose induced modification has a non-principal divisorial centre, with any exponents. 047 and 049 both qualify.
- **Tier 3:** any other witness with an accepted proof, scored separately.
- Known candidates (Russell cubic, Koras–Russell, Asanuma's B over ℝ, Dubouloz–Ghosh, Vénéreau, Gupta's char-p threefolds) are **not** hits.

**k values:** 1…1024 for arm O; 1…256 for arms R and D.

**Distances.** No trace exists, so these are estimates from the paper:

| Item | Pivot distance | Chain depth |
|---|---|---|
| C1 | ≥ 3 from L (about 1 in arm D) | 1 to state, 4 to verify |
| C2 | 1 | 2 |
| C3 | 1 | 3 |
| C4 | 1 | 4 |
| C5 | 1 | 1 |
| C6 | 1 | 1 |

**Controls.** Positive: Cook–Reckhow ER variables. Negative: C5 and C6.

## 4. Family verdict

**family_D: D3 (provisional), confidence 0.45. It rests solely on C1, the witness H.**

It falls to **D2**, carried by C2–C4, if any of these happens:
- arm R (or O) of Test 4 exceeds the calibrated threshold;
- an expert finds a prior proposal of affine modifications of Danielewski twists of the SL₂/T quadric as ZCP or Dolgachev–Weisfeiler candidates;
- the methodology bars A2 witnesses (for which T3 is vacuous) from N3;
- the comparator check fails.

**Downstream note.** 049 reuses the whole C1–C4 package to refute SCC in four variables. That makes it a natural held-out theorem for the step-9 speedup test, and evidence against a one-off device.

**provenance_flag: no** (see §1).

**bridge_novelty.**

| Import | Verdict | Evidence |
|---|---|---|
| Residual-coordinate stabilization (El Kahoui–Ouali, Dutta–Lahiri, Edo–Vénéreau) | known route | GuptaSurvey's Asanuma/affine-fibration route |
| Filtered→graded LND method (Kaliman–Makar-Limanov, Gupta's Derksen strategy) | known route | Gupta's char-p ZCP proofs |
| SL₂ torus bundle / Cox torsor + Brion linearization to obstruct polynomiality | **new bridge (weak, 0.5)** | Lifting to Cox torsors is known in general, but no use in a cancellation obstruction was found. The Lean found an elementary alternative (slice + Bézout frame) |
| Mason–Stothers → LND rigidity | known route | Finston–Maubach |
| sl₂ highest weight (Lean only) | known tool, local use | — |
| Quillen–Suslin + Bass–Connell–Wright (corollary) | known route | standard in the affine-fibration literature |

## 5. Open questions
1. Re-run the Lean comparator for `OAI.ComplexCancellation.main`. Every grade is conditional on correctness.
2. Expert query to Gupta, Dubouloz, Kaliman, Freudenburg and Asanuma: was the quadric-twist / non-principal-centre construction proposed before? This is the main risk to C1.
3. Is A, after a change of variables, a saturated Asanuma-type ring S[I/p²]? Does the expert community treat it as the same template?
4. Methodology: tag A2 witnesses as "N3-witness", and require arm R to pass before D3 counts.
5. Ask OpenAI for the 047 search history; no trace was released.
6. Step 9: measure the speedup of C1–C4 on 049.
7. Verify Gaifullin–Petrov p. 1 and the Alpöge/Claude attribution from primary sources.
8. Run zbMATH/MathSciNet absence searches.
9. The corollaries (SCC in dimension 5, Dolgachev–Weisfeiler in relative dimension 3) are unformalized and should be checked independently.
