# Family 240: novelty analysis (eventual categoricity and the CH obstruction to a prescribed threshold)

- Analyst role: novelty. Date: 2026-10-12.
- Machine-readable version: `novelty.json`.
- Inputs: `family.json`/`.md`. There is no trace and no `f1_*` file.
- Sources read:
  - **CH:** sections 00, 05 and 06, plus the bib;
  - **EC:** sections 01, 03 (l.360–718) and 09 (l.300–560), plus the bib;
  - **Lean:** spot checks of `OAI/ModelTheory/Categoricity`.
- Lean is trusted as published, per the project rule; nothing was built.

**L** = Mathlib d13f23b, plus the CH bib (14 entries) and the EC bib (20 entries). For contamination control, L leaves out the intra-family companion `OpenAI2026CHThreshold`.

**Access caveat.** These checks are at snippet level only:
- WebFetch failed for every host (DNS errors for arxiv.org, ar5iv, hal.science and semanticscholar).
- Bash egress to export.arxiv.org was refused by the proxy (403).
- Every precedent check therefore rests on WebSearch snippets, the manuscripts' own statements and domain knowledge.

## 1. Verdicts first

**Provenance flag: no.**
- The only 2025–26 work cited is the companion 240-CH. It is model-produced and from the same release; EC cites it "for context only", and no EC lemma depends on it.
- The external precedents were all written by humans, years before model-produced research mathematics existed. Snippets show no AI disclosure, but this is unverified because the abstracts could not be fetched.
- Searching "eventual categoricity" together with ChatGPT, GPT-5, OpenAI or "AI-assisted" found no model-produced precedent.

**Family D: D2 (confidence 0.6)**, down from D3 (provisional, 0.35).
- No item survives as N3.
- The Lean-formalized manuscript, 240-CH (`OAI.CHObstruction.main`), tops out at N2 with CH-I08.
- Consequences:
  - The Lean shortlist gets nothing from this family.
  - The informal eureka list gets nothing either.

| Cand. | Item | Provisional | **Final** | Conf. | Lean-backed |
|---|---|---|---|---|---|
| C1 | EC-I12: eventual reversal by profile pigeonhole, two-size alignment and an omitting elimination chain | N3 | **N2** (borderline N3, F3 if upgraded) | 0.55 | no |
| C2 | EC-I25: return-tree split, whose accumulator keeps only boundary maps | N3 | **N2** | 0.6 | no |
| C3 | CH-I08: object-vs-strong asymmetry on coded rank diagrams | N2 | **N2** | 0.75 | **yes** (`Data.IsObject`, `Map.Strong`, `classData`) |
| C4 | EC-I14: categoricity at countably cofinal closure points | N2 | N2 (could be N1) | 0.55 | no |
| C5 | EC-I21: fresh strip and approximate retractions | N2 | N2 | 0.6 | no |
| — | CH-I06, CH-I14, CH-I16, CH-I19 | N2 | N2 | 0.6–0.8 | yes |
| — | CH-I24 (the topos obstruction) | N2 | N2 | 0.7 | no |
| — | EC-I07/09/11/13/16/18/20/22/23/24/26/30/31/32/33 | N2 | N2. I31–I33 are templated dimension-raising, capped at N2 | 0.55–0.7 | no |

## 2. What 240-CH contradicts in Espíndola

**What is contradicted.**
- The CH paper cites **Espíndola, arXiv:2301.13167 v1 (Jan 2023), Thm 4.1** as claiming categoricity transfer *at the prescribed bound* H(K) = ℶ_{(2^{LS})⁺} for arbitrary AECs (`00-introduction.tex:113-124`).
- Theorem 1.1, under CH, has the opposite conclusion at that bound. Its AEC has LS = ℵ₀, two models at ℶ_{ω₂} = H(K), and categoricity from Λ = ℶ_{(2^{ℵ₁})⁺} onward.
- With Gödel's L, where GCH and hence SCH also hold, it follows that Thm 4.1 cannot be a theorem of ZFC, or of ZFC + SCH, provided ZFC is consistent.

**The failing step (Section 7).**
- The cited proof starts from the full double-negation subtopos of presheaves on the countable internal-size site. It then asserts that a large categorical model gives a point of that subtopos.
- `Prop bool:obstruction` shows that this fails here. The canonical point p_H of any countable-base model, which includes every model of size ≥ Λ, does not factor through the subtopos.
- The reason: the cosieve R_A of maps that add a base point is dense, but it is not lifted inside H.
- The paper limits its claim. It does not classify the points of the Booleanization, and it does not rule out other constructions of points.

**What is not contradicted.**
- Espíndola's **1906.09169 v7** (2022) claims the *existential-threshold* conjecture in ZFC. The CH class is categorical on a tail, so it is consistent with that conclusion.
- Open question: does v7 use the same Booleanization step?

**Verification status.**
- Snippets confirm that 2301.13167 exists (30 Jan 2023; also on HAL as hal-04353204).
- Its abstract claims explicit thresholds and a ZFC classification of AEC categoricity spectra.
- The exact text of Thm 4.1 was **not** verified.

## 3. Candidates

### C1: EC-I12, eventual reversal (final N2, conf 0.55, no Lean)

**The device.**
1. **Profile pigeonhole.** Orbit-name profiles take at most 2^B values whatever κ is. So among P⁺ failing categoricity sizes, two of them, a < μ with a^θ ≤ μ, share a profile.
2. **Alignment.** Every subset of size ≤ a in the μ-model lies in a strong a-sized E(H(T)) whose θ-tuples have the same orbit names as in the big model.
3. **Elimination chain.** Run θ⁺ rounds of an increasing chain of μ-models. Each round enumerates the a^θ tuples of the current aligned small model and pushes every tuple whose orbit reaches p into r, where p → r but not r → p.
4. **Contradiction.** The union of the small models is a copy of C_a that omits p.

In the paper's words: "the small model supplies the alignment; the larger model accommodates the enumeration".

**Test 1, neighbours.**
- **Shelah 2009, Ch. IV (Claim IV.1.12 / IV.2.14).** On a tail, ≤_K = L_{∞,LS⁺}-elementarity. That implies reversal. This is the same target in a stronger claimed form, and it has a known gap.
- **Boney–Vasey 1508.03316 (Fact 1.4 / Claim 1.5).** They identify the gap and give valid variants under exponent or cofinality assumptions, using model-theoretic forcing and a proper-class Fodor. **Close variant of the statement, with a different mechanism.**
- **Classical omitting-types-by-chain arguments under categoricity**, from Morley and Shelah's EM proofs. **Close variant of the template.**
- **Pigeonholing a bounded invariant over many categoricity cardinals.** **Equivalent ingredient.**
- **Shelah IV.5.1** (homogeneous index orders) and **Vasey's work on universal classes.** **Ingredient.**
- **Espíndola's topos route.** **Genuinely different.**

**Test 2.**
- The statement fails: it is a hypothesis-free version of a statement already in L.
- The device (the two-size decoupling plus the omitting chain) is not a subterm of anything found.

**Test 3.** Passes by knockout. Every later EC section rests on symmetric strong-map classes.

**Verdict.**
- This is the most original element in the family and is N3-borderline.
- The statement is in L, and each of its three components is precedented.
- **Upgrade path:** an expert or the P-C1 judge finds no precedent for the two-size decoupling, and EC survives refereeing.

### C2: EC-I25, return-tree split (final N2, conf 0.6, no Lean)

**The device.** It is a binary tree of height ε, with ε the least cardinal such that 2^ε > χ, built from competing amalgams (Y⁻ / Y⁺ children).
- Full maps are kept only along branches.
- A shared accumulator keeps only boundary maps, identifying the two boundary copies of v.
- Completing the leaves gives more than χ orbits over at most χ parameters, which contradicts the orbit bound.

**Test 1, neighbours.**
- **Shelah's binary-tree "many types" argument.** It has exactly this cardinal bookkeeping: close variant (template).
- **Shelah 1983B (in L) and Shelah–Vasey JEMS 2024.** These use the same tree of competing amalgams but close it by counting models under WGCH or weak diamond: close variant.
- **Good-frame uniqueness under weak diamond:** different.
- **Tameness routes (Vasey, Grossberg–VanDieren, Boney):** different.

**Assessment.**
- The new part, the boundary-only accumulator, is bookkeeping that adapts a classical argument.
- It is **not** a new kind of object, so the grade is N2.
- Whether an in-model orbit count has been used before in place of weak diamond for multidimensional uniqueness is an open expert question.

### C3: CH-I08, object-vs-strong asymmetry (final N2, conf 0.75, **Lean-backed**)

**The design.**
- Objects allow countably many exceptional columns per tuple.
- Strong extensions allow none at new base points.

**What it buys.** LS = ℵ₀ and smoothness, while uncountable-base objects still store rank data up to ℶ_{ω₂}.

**Lean.**
- `Data.IsObject` is at Arrays.lean ~l.143 and `Map.Strong` at ArrayEmbeddings.lean ~l.91.
- It is load-bearing:
  - `Data` has a 53% share of the DAG;
  - `index_lt` dominates 21%;
  - `twoModels` dominates 15%.

**Test 1, neighbours.**
- **Hart–Shelah 1990 / Boney–Vasey 2018:** torsors, parity bits and 2^ω/fin colours. The paper names them "a close predecessor".
- **Kolesnikov–Lambie-Hanson 2016:** colour diagrams with ranks, and Hanf numbers for amalgamation. Also named by the paper.
- **Morley-style Hanf-sharpness coding**, a template.
- **AEC designs in which ≤_K constrains only new elements**, a template.

**Test 2.** Passes. The class is the witness, judged against the problem as posed.

**Verdict.** It does not pass Test 1, so the final grade is N2.

### Others
- **C4 (EC-I14):** a routine back-and-forth once stabilization is given.
- **C5 (EC-I21):** EM strip-shifting, which is classical.
- **CH-I24:** standard topos facts used as a concrete counterexample to one step of Espíndola's proof. It is corollary-only and not formalized.
- **EC-I31–I33:** templated cardinal or dimension induction, the Shelah 1983 template, capped at N2.
- **N0/N1 exclusions:** listed in the JSON.

## 4. Bridge novelty
Every cross-field import is a **known route**:
- **Set theory into AEC categoricity:** Morley, Shelah's book, Boney–Vasey's proper-class Fodor, KLH.
- **F₂ torsors into AEC counterexamples:** Hart–Shelah.
- **Hahn-type ordered groups as EM index orders:** Shelah IV.5.1.
- **Topos theory, corollary-only:** Espíndola, and the work of Lieberman, Rosický and Vasey.
- **Gödel's L.**

None of them is a new bridge.

## 5. Discoverability protocols (not run; full detail in the JSON)
**Common settings.**
- **Models:** training cutoff before 2026-09-24. Canary probes ask about both manuscripts; the OpenAI models that produced family 240 are excluded.
- **Sampling and context:** n = 256 samples per arm, k ∈ {1, …, 256}, context L without the companion paper.
- **Judging:** two LLM judges plus an AEC expert.
- **Controls:** Cook ER as the positive control; EC-I14 and CH-I19 as negative controls.

**Per candidate.**
- **P-C1 (EC-I12), informal.**
  - Hide EC-I09, I11 and I12 and everything downstream; give Sections 2–3 up to the orbit bound.
  - A **hit** needs both of these:
    - two categoricity sizes a < μ with a^θ ≤ μ that share an orbit invariant;
    - a chain whose union is a copy of the small model that omits a realized orbit.
  - The omitting chain together with κ^θ = κ is only partial credit, since that is the known route.
- **P-C2 (EC-I25), informal.**
  - Hide the return-tree proof.
  - Arms: "without WGCH" against a WGCH-allowed baseline.
  - A hit needs:
    - a height-ε tree;
    - a boundary-only accumulator;
    - an orbit count.
- **P-C3 (CH-I08), Lean-capable.**
  - Hide `IsObject`, `Map.Strong`, `classData` and everything downstream.
  - A hit is a proposal in which objects are "small exceptional set per tuple" while strong extensions are "exact at new base points".
  - Hits can be checked in Lean against `isAEC`, `twoModels` and `index_lt`.

There is no trace, so pivot distance is not available.

## 6. Open questions
1. Verify Espíndola 2301.13167 Thm 4.1 word for word: its threshold, its hypotheses, and the Booleanization step.
2. Does 1906.09169 v7 use the same step?
3. Ask experts (Vasey, Boney, Grossberg, Baldwin, Shelah) about EC-I12's two-size decoupling. It is the only route back to D3.
4. Is an orbit count known as a replacement for weak diamond in proving multidimensional uniqueness (EC-I25)?
5. Is any AEC already known that is categorical on a tail but not at H(K)? None was found. The searches found only Hanf-number lower bounds for amalgamation, JEP and stability (KLH, Baldwin–Boney, Leung).
6. Is 240-EC correct? Sections 5–9 and 11–13 were read only at statement level, and Section 13's common level is the highest-risk point.
7. Repeat all checks with full-text access.
