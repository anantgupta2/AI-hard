# Family 304: novelty analysis ("The Hilbert–Smith conjecture in every dimension")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`, which uses the 287 keys with `precedent_checks` as a list.

**Inputs:**
- `family.json` / `family.md`;
- the preprint source (`build/main.tex`, six sections, appendix, `references.bib`; commit fd4aeeb);
- `f1_character_classes.json` / `.md`, which arrived mid-analysis and are incorporated;
- web checks.

There is **no Lean and no reasoning trace** for this family.

**L** = Mathlib d13f23b plus 304's 40-entry bibliography.
- L contains Woolf, Ranicki–Weiss, Balmer(–Walter), Hornbostel–Schlichting, Yang, Bredon–Raymond–Williams, Repovš–Ščepin, Dranishnikov–Ferry–Weinberger and Pardon.
- L does **not** contain Atiyah–Singer or any finite-group G-signature result.

## 1. Provenance verdict: flag NO

**No model-produced work precedes 304.**
- **Cited works.** There are no 2025–2026 preprints in the bib; the only 2026 entries are Stacks Project tags. All 40 entries are human literature. The arXiv-hosted ones I checked (Shelukhin 2403.07195, Pardon 1811.08748, Ranicki–Weiss 0901.0819) carry no AI disclosure.
- **Uncited 2025 neighbour.** Banagl–Leichtnam–Piazza, arXiv:2511.21586 (Nov 2025), "The G-signature theorem on Witt spaces". It covers compact Lie groups only and has no AI disclosure.
- **Web searches** for "Hilbert–Smith" with ChatGPT / GPT / OpenAI / AI-assisted found only **post-release** material:
  - **Dabrowski, `github.com/adbrw/HS_proof`, dated 2026-10-08.** Its author line is "A. Dabrowski's AI agents". It is a second claimed proof, with a route (per the Coppola audit) of an "integral tail in L-theory versus pZ". That is the same "integrality versus p-divisibility of a signature/Witt invariant" family as 304. It post-dates the 2026-10-06 release, so it is **not a precedent and possibly derivative**. It matters for contamination control in Test 4.
  - **Coppola, `github.com/ajjcoppola/hilberts-5th-oai`, 2026-10-07/08.** An AI-assisted audit ("Cursor(Opus 5.5/Grok), driven by: Alan Coppola"). It gives 304 no FAIL grades, and WEAK grades on dense doubling, the Balmer–Walter bridge, character coproducts and the equal-parts isometry. It reports no technical rebuttal so far.
  - **google-deepmind/formal-conjectures issue #6914, 2026-10-07.** Proposes marking Hilbert's 5th as solved and flags a second-countability mismatch. The author notes it was "prepared with AI assistance". No expert comments.
- **Quote caveat.** All quotes here come through WebFetch's summarizer and are unverified.
- **Discrepancy with the F1 agent.** The F1 agent reported "nothing found after Oct 6"; the three items above contradict that.

## 2. Final grades

| # | Item | Nearest neighbour (T1) | T2 | T3 (down / cone) | Final | conf |
|---|---|---|---|---|---|---|
| C1 | **I42 integral character classes** z_i(t) | Finite-group isotypic G-signature: Atiyah–Singer 1968, Gilmer 1981. Reflection-twist identity: Hirzebruch–Zagier 1974. Cappell–Shaneson–Weinberger 1991 (content unverified). **Close variant**; no profinite or localized version found | pass (template outside L) | knockout; 0.17 / 0.52 | **N2** (analyst: N3) | 0.55 |
| C2 | **I49 equal parts in a fixed lattice** (with I47, I26) | Free-action signature divisibility σ(M) = \|G\|σ(M/G). Rokhlin K-theory divisibility: Izumi; Gardella et al. (found by F1). Yang/BRW p-divisibility. Williams–Dranishnikov K-theory programme. **Close variant** | pass | knockout; prose strategy, cone 0.76 | **N2** (analyst: N3) | 0.50 |
| C3 | I46 equal parts via the sheet multiplier β | Trivialising a character local system on a trivial cover | pass (weak) | 0.07 / 0.57 | N1 | 0.65 |
| C4 | I32 averaged degree-one test | Bochner–Montgomery averaging; Repovš–Ščepin averaged metric (both in L) | pass (weak) | 0.10 / 0.10 | N2 | 0.60 |
| C5 | I37 move-test | DFW 2003 odd-sphere telescope, named by the paper | fail (borderline) | 0.07 / 0.19 | N1 (analyst: N2) | 0.60 |
| C6 | I07 test categories T(X) | Ranicki–Weiss 2010 ("close antecedent"); Woolf 2008 | fail (borderline) | 0.60 / 0.02 | N2 | 0.70 |
| C7 | I23 + I26 bounded comparison and fixed sphere lattice | Hornbostel–Schlichting cofinality; Woolf; Mayer–Vietoris template | pass (weak) | 0.07 / 0.48 | N2 (templated: uniform version) | 0.65 |
| C8 | I15 + I17 cutoff and germ description | Ranicki–Weiss cutoff; Kashiwara–Schapira | fail (borderline) | 0.38 / 0.05 | N1 | 0.60 |
| C9 | I45 homotopy invariance of the classes | Woolf cylinder | fail (borderline) | 0.07 / 0.57 | N1 (analyst: N2) | 0.60 |

**Excluded as N0 transfer:**
- I18 Balmer–Walter, I20 dense doubling (Hornbostel–Schlichting), I29 Newman/Pardon chart, I33 rational transfer, I34 Serre/DFW, I36 homotopy extension.
- I30 odd stabilization is an N1 design choice, folded into C1.

**Test 3 method.** There is no Lean, so I used the family.json LaTeX DAG. P is the 42 items in the cone of the headline. As in 287, the downstream proxy penalises items near the top of the chain, so load-bearing is judged by knockout, with both shares reported.

**Why C1 and C2 are downgraded from the analyst's provisional N3.** The family analyst noted isotypic G-signatures as the "against" case but did not name the decisive classical template:
- For a **free** finite action, sign(g, M) = 0 for g ≠ 1.
- So the isotypic parts of the signature are equal, and |G| divides σ(M).
- For an involution, [b] + [b∘σ] = 2[b restricted to V₊]. That is exactly 304's [A, α] + [A, α(2e−1)].

304 runs this template with |G| = p^k unbounded against a lattice L_d fixed in advance. It moves it from the manifold to a **test sphere**, reached from the wild orbit space by the averaged degree-one test.

The real new content is technical:
- the germ-localized projectors on the punctured target;
- the integral lift through a contractible quotient with d odd;
- the 2× summand, which avoids splitting idempotents;
- integral Witt bounds for non-constructible categories.

The F1 agent independently finds every component classical, finds no earlier equivalent of the composite, and calls N2 "a defensible alternative to N3".

## 3. Family verdict

**family_D: D2, confidence 0.55.**
- It rests on C1 and C2, both at N2.
- **It rises to D3** (C2 as F5, or C1 as F1) if both of these hold:
  - an expert judges that the profinite, germ-localized lift needs an idea absent from finite-group G-signature theory;
  - the Test 4 *template arm*, which supplies the finite-group divisibility fact explicitly, stays below the calibrated threshold.
- **D1 is unlikely.**
- **Correctness.** All grades assume the proof is correct. It is an unreviewed claim of a famous conjecture, with no Lean and no trace. Both the family analyst and the Coppola audit locate the risk in the Witt theory of the non-constructible categories T(X) and their Verdier quotients.

**provenance_flag: no.** Record "post-release AI-produced parallel claim (Dabrowski 2026-10-08)" for contamination control.

**bridge_novelty:**

| Import | Classification | Evidence |
|---|---|---|
| Sheaf Witt groups / signature integrality → Hilbert–Smith | **New bridge** (first connection found) | No prior signature, Witt or L-theory approach turned up on WebSearch or MathOverflow, in the bib, in Dranishnikov's 2016 survey of approaches, or in the McAuley, Pardon or Shelukhin methods. Coppola independently calls the route "not Yang dim-raising and not Pardon". Caveat: Weinberger's 2011 C⁰-Zimmer notes were not accessible |
| Finite-group isotypic signature divisibility → profinite Z_p | **New bridge for this problem**; known route for finite groups | The template itself is classical |
| Haar averaging → degree-one test | **Known route** | Repovš–Ščepin's Lipschitz Hilbert–Smith proof |
| Serre odd-sphere telescope | **Known technique, new application** | Used the same way in DFW 2003 |
| Newman + Pardon chart; GMZY reduction to Z_p | **Known route** | Lee 1997; Pardon 2013 |
| Hardt semialgebraic triviality | **Known technique** | |

## 4. Discoverability (Test 4, not run)

The full spec is in `novelty.json → discoverability_protocols`.

**Models.**
- Training cutoff before **2026-09-23**.
- A canary probe excludes any model that knows of a Hilbert–Smith resolution or of a Witt/signature approach to it.
- Exclude the OpenAI lineage that produced the release, plus the Dabrowski and Coppola material.
- No tools. The judge must differ from the proposer.

**Arms** for **P-C1C2** (decisive):
- **open:** the problem, plus the reduction and Newman;
- **template:** open, plus the finite-group statement "free action ⇒ equal isotypic signature parts ⇒ |G| divides σ";
- **pivot:** also gives T(X), the fixed sphere lattice, the averaged test, the move-test and the finite sheets.

**Protocol settings.**
- **Hide:** I39–I47, I49 and the intro prose 01:163–235. In the open and template arms, also hide I07–I37.
- **Hit criterion**, all three required:
  - (a) an integral invariant with a fixed denominator bound, attached to a test map out of the orbit space;
  - (b) a character-indexed splitting that preserves integrality;
  - (c) equal parts summing to a fixed class, giving p^k-divisibility against the lattice.
- An orbit-space-cohomology divisibility argument is the Yang/BRW route and does not count.
- **Sampling:** n = 256 per arm; report pass@k for k = 1…256.
- **N3 for C2 requires the template arm to stay below threshold.**

**Pivot distance and chain depth.** There is no trace, so these are estimated from the paper:
- C1: pivot 1 from the finite-group template, about 2 from L; chain depth 2.
- C2: pivot about 1–2 in the template arm, about 3 in the open arm; chain depth 3.

**Other protocols:** P-C4, P-C5 and P-C6C7, all at pivot 1.

## 5. Open questions
1. Expert query (e.g. Woolf, Schürmann, Weinberger, Pardon): is the profinite, localized character class a routine adaptation of finite-group isotypic signatures? This decides N2 vs N3.
2. Read Cappell–Shaneson–Weinberger, C. R. 313 (1991), and Weinberger's 2011 notes for any signature remark on Z_p actions.
3. Verify the Atiyah–Singer III and Gilmer locators.
4. Is the Dabrowski preprint independent of the 304 release?
5. Re-run the absence searches on zbMATH and MathSciNet.
6. A Lean comparator for `thm:main` would allow a real DAG share and a step-3b compression measurement.
7. The second-countability mismatch raised in formal-conjectures issue #6914.
