# Family 046: novelty analysis ("Shafarevich counterexamples in dimension two and with large fundamental group")

Analyst role: novelty. Date: 2026-10-09. The machine-readable version is `novelty.json`, which uses the 287/047 keys.

Inputs:
- `family.json` and `family.md` (Phase 1, same agent; 80 items, S01–S38 and F01–F42);
- both manuscripts' sources;
- grep checks of sibling release families 057 and 058;
- web checks, listed under Sources.

There is **no reasoning trace, no Lean, and no F1 file**. Here **S** is the surface preprint (2026-09-23) and **F** is the fourfold preprint (2026-10-05).

## 1. Provenance verdict: PARTIAL
- **What S cites.** S cites two OpenAI release preprints, both model-produced. Both are used **only for corollaries**:
  - *Abelianity for special compact Kähler manifolds* (family 057) gives "the surface is not special";
  - *Semialgebraic universal covers* (family 058) gives "the cover is not semialgebraic".
- **They were developed together.**
  - 057 cites S back (`introduction.tex:162-165`).
  - 058 is dated a day *after* S but is cited by S.
  - Neither contains any candidate item. A grep finds no Golod, Nori, Stover or dihedral content in either.
- **What else is not cited.** F cites no model-produced work. S and F do not cite each other.
- **No model-produced precedent for the Shafarevich problem.**
  - Sra's *GPT, the Counterexample Machine* (2608.29595) was text-extracted locally: it has no Shafarevich, Katzarkov or Golod content.
  - Searches pairing Shafarevich with ChatGPT, GPT-5, OpenAI, AI-assisted or LLM found nothing.
- **Adjacent model-produced work** (method-level only):
  - the same release's weighted-GS group-theory families (201, 247, and the periodic-group preprint);
  - OpenAI's public May-2026 unit-distance result, which reportedly used GS class field towers (secondary reports, unverified).
- **Human 2025–26 citations** show no AI disclosure (all checks summarizer-mediated, so unverified): Eyssidieux–Funar 2112.06726, BBT 2408.16441, Deng–Yamanoi 2306.03070 and Llosa Isenrich–Py 2310.04073.

## 2. Final grades
| ID | Candidate | Final | F | Conf. | Decisive neighbour |
|---|---|---|---|---|---|
| C1 | Fourfold witness: coupled red/blue pencil arrangement + chart-local D_∞ translation labels (F14, F21, F23, F33) | **N3** | F3 | 0.45 | None equivalent. Toolkit: Stover–Toledo / Llosa Isenrich–Py ball-quotient covers |
| C2 | Surface witness: genus-0 48-marked Eisenstein family, torus-lifted, with pro-2 degree-raising monodromy (S13 cluster) | **N3** | F3 | 0.35 | Architecture named by the paper: Bogomolov–Katzarkov 1998. Eyssidieux–Funar show BK's own objects fail |
| C3 | Economical involution presentation, P=(1+t)G, via the acyclic Frattini differential (S25, S27) | **N2** | – | 0.60 | Koch–Venkov σ-group refinement of GS (σ-inverted relators lie deeper); Jennings bases |
| C4 | Local path criterion with projected-diameter edges (F07–F12, F26–F28, F38) | **N2** | – | 0.70 | Gromov / Delzant–Gromov Cartan–Hadamard; Coulon; DGO rotating families; electrification |
| C5 | Abelian-surface reduction and the C²/ℤ³ (T³×ℝ, H₃≠0) non-Stein obstruction (F03, F06) | **N2** | – | 0.55 | Andreotti–Frankel, toroidal groups, the Nori-string analogue. Test 2 is a borderline fail |
| C6 | Finite local detection and descent (S36) | N1 | – | 0.65 | Standard (negative control) |
| C7 | Relative Godeaux–Serre plus Atiyah-type ambient blowdown (F39, F40) | N1 | – | 0.60 | Serre 1958 / Totaro; Atiyah 1958 |

**family_D: D3 (provisional), confidence 0.40.**
- **What it rests on:** the two witnesses, which are counterexample designs judged against the problem as originally posed. Mainly C1, secondarily C2.
- **Everything else is N0–N2:** all the machinery (C3–C7) and every cited import.
- **What would downgrade it to D2:**
  - Test 4 shows that the C1 frame (pencil + D_∞ + coupling hyperplanes that collapse the red meridians), or the isogeny-lifted genus-0 BK family, is readily proposed once the route is given; or
  - an expert finds coupling-type arrangements or genus-0 BK families in the literature; or
  - a proof fails.

## 3. Test notes per candidate
- **C1.**
  - *Test 1:* none of the neighbours is equivalent:
    - Stover–Toledo and Llosa Isenrich–Py (ramified covers along totally geodesic divisors) are an ingredient and a route;
    - Eyssidieux 1611.09178 (Hirzebruch arrangement covers satisfy Shafarevich) reaches the opposite outcome;
    - BK 1998 is a strategy only;
    - Deligne–Mostow/Deraux arrangement orbifolds work by global uniformization.
  - *Test 2:* passes against the posed problem.
  - *Test 3:* about 75% of the F items depend on it.
  - The labels are deliberately *not* a global representation. By fixed-rank EKPR (Deng–Yamanoi confirm the fixed-N form), no bounded-rank linear representation can detect the generator's powers. So a local, chart-based invariant is the only option, and this is why the design is non-obvious.
- **C2.** The paper itself says it "follows the same broad passage" as BK. The pro-ℓ unipotence principle behind S19/S20 is folklore. The object (Eisenstein [4] family, 48→24 collisions, torus-lift comparison through p: K→Π) has no equivalent found. The grade is N3 at low confidence.
- **C3.** It is downgraded from the analyst's weak N3. Koch–Venkov (1975) beat GS for class field towers using exactly σ(r)=r⁻¹ relators that sit one filtration level deeper. S27's relators r_g = σ(g)g⁻¹ satisfy σ(r_g) = r_g⁻¹ and have degree w_g+1. What is new is the implementation: the p=2 permutation-module coinvariants, the d²=0 acyclic complex, and the shift-adapted weights. The Koch–Venkov details come from secondary summaries and are unverified.
- **C4.** The paper names Gromov's local-to-global viewpoint. The Delzant–Gromov / Coulon orbifold Cartan–Hadamard theorem (a locally hyperbolic space is developable, with hyperbolic universal cover) is essentially the content. Diameter edges amount to coning off bounded regions. The item is strategically central but is a variant of known machinery.
- **C5.** It is elementary given Andreotti–Frankel and toroidal groups. It is also analytic in the sense of test 2: it is the goal's own failure mode instantiated on the preimage of a subvariety.

## 4. Bridge novelty
| Import | Verdict |
|---|---|
| Weighted pro-2 Golod–Shafarevich → infinitude of a geometric π₁ quotient (S) | **New bridge**, moderate confidence. BK posed infinitude as open; EF used TQFT. No prior GS use was found, but BK's full text was not read |
| Koch–Venkov-type involution trick → monodromy coinvariants (C3) | Known in number theory; transplanted |
| Coarse Cartan–Hadamard → infinite order in an arrangement orbifold's π₁ (F) | Known route for BK-type infinitude questions (DGO); new bridge to ball-quotient charts |
| Stover–Toledo / arithmetic ball quotients → exotic projective varieties | Known route |
| Zarhin; Andreotti–Frankel; Godeaux–Serre / Hamm–Lê | Known routes |
| CM isogeny lift → controlled braid monodromy | Known technique, new use |

## 5. Discoverability protocols (not run)
- **Models:** training-data cutoff strictly before 2026-09-23, with no tools.
  - Exclude the openai/math repository, including 057/058, which cite S.
  - Canary probes check whether the model knows the disproof or can complete the arrangement or the identity P = (1+t)G.
  - Stratify by whether the cutoff is after May 2026 (OpenAI's GS unit-distance result).
- **Arms:**
  - O: the problem as posed;
  - R: also give the obstruction, and say that a representation-free infinitude proof is needed;
  - D: also give the surrounding machinery, at pivot level.
- **Sampling and judging:** k up to 512 for arm O and 256 for R and D. Two LLM judges plus an expert in Kähler groups.
- **Controls:** the positive control is Cook–Reckhow. The negative controls are C6 and C7. Witness negatives that must not count as hits are BK's genus ≥ 2 families, Hirzebruch covers and plain Stover–Toledo covers.
- **Hide sets, equivalence criteria and estimated pivot distances** are in `novelty.json` under P-C1 to P-C5. Estimated pivot distances: C1 about 2, C2 ≥ 2, C3 1–2, C4 1, C5 1. There is no trace, so none of these is measured.

## 6. Open questions
- **Correctness.** Have experts check F's Lemma app:true-relations, F's path lemma, and S's shift-basis propagation. Every grade is conditional on both proofs being correct, and both are unrefereed claims against a 1972 conjecture.
- **Precedent reading for C3.** Read Koch–Venkov and Ershov's GS survey directly. If C3 is a standard lemma, it drops to N1.
- **Precedent reading for C2.** Read BK §4.1 in full. If BK used genus-0 families or GS methods, C2 drops to N2 and the GS bridge becomes a known route.
- **Expert query for C1.** Ask Toledo, Stover, Py or Deraux whether coupling hyperplanes or chart-local D_∞ labels have appeared before. This is the main risk to C1's N3.
- **Missing consequences.** A referee should require the papers to state the consequences: no linear detection of e, and, if Treger's result holds, a non-residually-finite π₁.
- **Downstream speedup.** Test C3 and C4 on families 201 and 247, the periodic-group preprint, and the Kähler-group families.

## Sources
- arXiv: 2112.06726, 2408.16441, 2306.03070, 2607.07059, 2512.24458, 2608.29595 (local text), alg-geom/9703002, 1611.09178, 2310.04073, 1302.6933, 1111.7048, 1008.3003, 2608.17072, 1206.0490, 1008.3002, 1008.1745.
- Annals 176-3 p04 (EKPR).
- Local: 057 `introduction.tex:162-165`.
- The arXiv abstract checks went through WebFetch's summarizer, so the "no AI disclosure" findings are unverified.
