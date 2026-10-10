# Family 242: novelty analysis ("Single-fold Diophantine representations")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

Inputs:
- `family.json`/`.md` (paper and Lean analyst). There is no reasoning trace for 242, so trace-based items (pivots, insight steps) do not apply.
- The preprint source (`main.tex`, `elliptic.tex`, `power.tex`, `references.bib`), plus spot checks of `HeightGrowth.lean`, `EllipticGrowth.lean` and `Power.lean`.
- Full texts read locally: Cantone–Cuzziol–Omodeo 2024, Cornelissen–Zahidi 2007, and the AIM problem list on extensions of Hilbert's tenth problem (H10).
- arXiv abstract/HTML pages: Poonen 2002, Shlapentokh 2009, Eisenträger–Everest, Mazur–Rubin, Koymans–Pagano, CCO 2023.

**L** = Mathlib d13f23b plus 242's 16-entry bibliography. L contains no 2025–2026 work. **L+** adds AIM Question 9, Shlapentokh 2009 and Eisenträger–Everest; it is used only as a Test-4 arm.

## 1. Provenance verdict first: **no**

- **Bibliography.** It has no 2025–2026 entries. The newest is cco2024 (*Le Matematiche* 79(2), received 2024-09-30). Its full text has no AI-assistance wording (a grep for ChatGPT/GPT/LLM/"language model"/"artificial" found nothing), and its authors are human with institutional funding.
- **Web searches.** I searched for "single-fold"/"singlefold" together with ChatGPT, GPT-5 or OpenAI. The only hits were:
  - press about *other* OpenAI results (GPT-5.6 Sol Ultra and the Cycle Double Cover conjecture, the-decoder, 2026-07-11);
  - third-party indexes of the 2026-10-06 release that list this family.
- **Result.** No model-produced earlier work on single-fold representations or on elliptic-height growth relations was found. The closest precedents are human and pre-LLM: Pheidas's AIM question (c. 2005), Poonen 2002, and CCO 2023/2024.

## 2. Final grades

| # | Item | Nearest neighbour (verdict) | T2 | T3 (dominated) | Final | F | conf |
|---|---|---|---|---|---|---|---|
| C1 | Elliptic-height single-fold growth function (I15–I20) | AIM Q9 (Pheidas) poses the bridge but gives no mechanism; Poonen 2002 Lemma 8 squares indices p-adically (different mechanism) | pass (moderate) | 0.49 (growth), knockout | **N3 (provisional)** | F3 (+F5) | **0.45** |
| C2 | Square-window lemma on its own (I19) | Quadratic-form second differences / parallelogram law (close variant) | fail (borderline) | 0.005 | N2 | – | 0.60 |
| C3 | Power from quasi-polynomial growth with a self-referential Pell scale (I22–I24) | Matiyasevich 1974 §4 = CCO 2024 Thm 5 (close variant) | fail (borderline) | 0.54 | N2 | – | 0.70 |
| C4 | Machine compiler: clock register, dyadic window, exact halt (I29–I32) | Matiyasevich 1974 Main Thm (same role); Jones–Matiyasevich; Chaitin | fail | 0.78, but replaceable | N2 (borderline N1) | – | 0.70 |
| C5 | Complete-witness hygiene (codes, gated cases, representatives) | CCO 2024 §2; mati1974 §3 | fail | carrier | N1 | – | 0.80 |
| C6 | Rank one and torsion of y² = x³ − 25x | Silverman X.4 (equivalent) | fail | 0.12 | N0 | – | 0.95 |
| C7 | Néron–Tate quadraticity and uniform comparison | Silverman VIII 9.1, 9.3 (equivalent) | fail | via C1 | N0 | – | 0.95 |
| C8 | Binary containment via Lucas mod 2 | Robinson 1952 §5; Jones–Matiyasevich (equivalent) | fail | knockout | N1 | – | 0.85 |

**Changes to the family analyst's provisional grades.**
- C1 stays N3, but its confidence drops, because of two precedents the analyst did not have.
- C4: the reduction it implements is already Matiyasevich 1974's Main Theorem.
- C3 stays N2, but its role is larger than the analyst recorded (see §3).

## 3. Precedent findings

**Target already posed (Robinson 1952; CCO 2024).**
- CCO 2024 §6 restates Davis's theorem: any Julia Robinson (JR)-growth relation can replace exponentiation. CCO note that **univocity is not preserved** there.
- CCO §7 states two open goals:
  1. a variant of Matiyasevich's univocal Theorem 5 with a relation M(u,v) in place of 2^u = v. CCO expect the requirements on M to be "probably stronger than exponential growth", citing Matiyasevich 2010's condition (‡);
  2. a concrete such M with a univocal polynomial specification.
- CCO §8 proposes eight candidates built from Davis-style quartics tied to Pell equations. There are **no elliptic curves or heights** anywhere in CCO 2023 or 2024.

**The bridge was posed about 21 years earlier (AIM problem list).** The list is "Problems related to Extensions of Hilbert's Tenth Problem" (moderated by Poonen and Scanlon, notes by Demeyer; undated, presumably from the AIM workshop of March 2005).
- Its Question 9 (Pheidas) asks whether the proof of H10 over ℤ can be redone with elliptic curves instead of Pell equations.
- It then asks: "Can this give a finite-fold Diophantine definition of all r.e. sets?"
- The question gives no mechanism. 242 does not cite it, and it is not in L.

**Squaring indices on rank-one curves already exists (Poonen 2002, in L).**
- Lemma 8 shows that den(x(P)) divides num((x(P)/x(mP) − m²)²). This extracts **m²** through the formal group, a p-adic congruence.
- Lemma 5 uses h(x(mP)) = m²ĥ(P) + O(1), but only for size control.
- Shlapentokh 2009 squares indices through divisibility of denominators.
- Eisenträger–Everest 2009 and Poonen 2003 model an index by real approximation: an error below 1/(10i), then rounding.
- Cornelissen–Zahidi 2007 multiply indices through Robinson's (ℤ, +, |).
- **None of them uses an archimedean height comparison to pin a nonlinear index relation. None builds a growth function, and none is single-fold.**
- Other works on elliptic curves and H10 (Denef 1980, Mazur–Rubin 2010, Koymans–Pagano 2024, Alpöge–Bhargava–Ho–Shnidman 2025) concern rank stability for rings of integers. Their abstracts mention no height-based definitions.

**C3 does more than adapt.**
- 242's Prop power is CCO Thm 5's system (L1–L7) with two changes:
  - the cutoff 2^u becomes g(u);
  - the scale becomes u = (c+1)^ℓ(n+1)(b+1) + u₀.
- Thm 5 already makes u a polynomial in the output. The new observation is that, because u > b^n already encodes n, a **quasi-polynomial** cutoff δ(log u)² < log g(u) < u log u suffices.
- This answers CCO §7's goal (1) with a requirement *weaker* than the (‡) condition CCO expected. It is also what makes C1's modest growth enough.
- It is still a close variant of a statement in L (N2). But it shifts where the difficulty lies: see the second open question in §7.

## 4. Why C1 survives, and how weakly

**For.**
- With Pell (linear log-growth in the index), a bounded multiplicative window can only test *linear* index relations.
- With heights on a rank-one curve (quadratic log-growth, bounded error), one fixed product L₀/D₀ = W_{2k}W_rW_1 / (W_k² W_{r+1}) tests r = k² exactly.
- Representatives and the neighbour-max bracket make every witness unique.
- This supplies the univocal M that CCO §7 asked for (via C3).
- Nothing in the goal or L states such a relation. In Lean, `growth` dominates 49% of the DAG, and `power` is literally `power_of_growth` applied to it.

**Against.**
- The bridge direction was posed (Pheidas Q9).
- The *aim* of squaring an index on a rank-one curve has a p-adic precedent in L (Poonen Lemma 8).
- Once quadratic log-growth with bounded error is in hand, the window itself (C2) is an exercise, and Lean states it for an arbitrary sequence.
- So the eureka content is narrow: the decision to use archimedean height comparisons as a single-fold growth device, plus the representative selection.

## 5. Discoverability protocols (Test 4, not run)

**Contamination control.**
- Models must have a training cutoff before **2026-09-24**, the preprint date. No earlier public source of C1 was found.
- Each model must pass a canary probe: it must not know of a claimed proof of the single-fold conjecture, or of an elliptic-height JR relation.
- Exclude the OpenAI lineage that produced the release; it may run only as a reference arm.
- No tools.

**Arms.**
- Library: L (main) vs L+ (adds Pheidas Q9, Shlapentokh and Eisenträger–Everest, to measure the effect of the posed bridge).
- Prompt: open vs directed.

**Sampling.** n = 256 at T = 1, reporting pass@k for k = 1…256. Two judges plus human review of all hits and 10% of misses.

**Controls.** Cook–Reckhow (positive); C6, C7, C8 and C2 (negative).

**P-C1 (decisive).**
- **Hide:** I14–I20 and everything downstream.
- **Arm A (pivot level):** give C3 (`power_of_growth`) and ask for any g that meets its hypothesis.
- **Arm B (decisive):** also hide C3; give only CCO Thm 5, §7 and (‡).
- **Hit:** a single-fold super-polynomial relation of growth at most u^u, built from both of:
  - (a) a family whose log-size is quadratic in a hidden index;
  - (b) a bounded-error comparison that pins a nonlinear index relation.
- **Partial credit (recorded, not counted):** "use elliptic curves instead of Pell" without (b).
- **Lean target:** `square_window` + `growth`.
- **Distances:** estimated pivot distance 2, chain depth 2 (no trace).

**P-C3.** Hit = using g as the cutoff with u polynomial in (c, b, n). Pivot distance 1.

**P-C2 and P-C4.** Expected near-negative. For P-C4, citing mati1974's Main Theorem counts as a hit.

## 6. Family verdict

**family_D: D3 (provisional), confidence 0.40.**
- It rests on C1 alone.
- **It falls to D2 if any of these happens:**
  - Arm B exceeds the calibrated threshold;
  - an expert (Pheidas, Poonen, Shlapentokh, Cornelissen, Zahidi, Matiyasevich) identifies an earlier archimedean height-window or height-based index squaring, for example in follow-ups to AIM Q9;
  - once C3's weakened target is known, a Pell-only single-fold quasi-polynomial growth function turns out to be easy. The key step would then be C3, which is N2.
- Grades are conditional on correctness of an unrefereed, extraordinary claim. The analyst found no gap and reports a clean Lean trust surface, but Lean was not compiled.

**provenance_flag: no.**

**bridge_novelty.**

| Bridge | Status | Evidence |
|---|---|---|
| Arithmetic geometry (rank-one curves, heights) → single-fold definability over ℕ | **Known route (posed), first execution with this mechanism** | Denef, Poonen, CPZ, Shlapentokh, Mazur–Rubin and Koymans–Pagano for rings of integers; Pheidas Q9 for ℤ and finite-fold |
| Pell → single-fold power | Known route | The C3 weakening is new inside it |
| Bit-masking / register machines | Known route | Jones–Matiyasevich; Chaitin; mati1974 |
| Lucas mod 2 | Known route | Robinson 1952; Jones–Matiyasevich |
| Minsky machines | Known route | Classical |

## 7. Open questions
1. Expert query: was an archimedean height-based index squaring discussed after AIM Q9? This is the main risk to C1.
2. Is a Pell-only quasi-polynomial single-fold growth function easy once C3 is known? A quick sketch suggests the index-transfer congruences bring back the cutoff problem, but this is not proved.
3. Read Matiyasevich 2010 p. 749 and 1974 §4 directly (mathnet.ru was unreachable). Did either note that a sub-exponential cutoff suffices?
4. Confirm the date of the AIM problem list.
5. Read Poonen 2003 (JAMS) and Denef 1980.
6. Re-run the absence searches on zbMATH, Google Scholar and MathOverflow.
7. Compile Lean.
8. Spot-check the summarised statements of Poonen Lemma 8 and Shlapentokh against the PDFs.
