# Family 242: "Single-fold Diophantine representations" (family analyst, paper + Lean)

Sources at commit fd4aeeb:
- Paper: `preprints/Single-fold-Diophantine-representations-September-24-2026/build/`. `main.tex` inputs `elliptic`, `power`, `computation`, `consequences`, `rank-one-proof` and `witness-ledger`; the bibliography has 16 entries.
- Lean: `lean/OAI/NumberTheory/SingleFold/` (28 files, 7,598 lines, 836 declarations) and the comparator `lean/ComparatorChallenges/SingleFold.{lean,json}`.
- There is no reasoning trace for this family.
- The full item list (49 items: 40 from the paper, 9 Lean-only) is in `family.json`.
- Base library L: Mathlib d13f23b plus the paper's bibliography.

## 1. Main statement
**Thm main** (main.tex:62-73): for every n ≥ 1 and every r.e. set S ⊆ ℕⁿ there are m ≥ 1 and P ∈ ℤ[A₁..Aₙ, W₁..W_m] such that #{w ∈ ℕ^m : P(a,w) = 0} is 1 if a ∈ S and 0 otherwise.

In words, this is Matiyasevich's 1974 **single-fold conjecture** over ℕ. The finite-fold conjecture follows immediately.

**Corollary** (main.tex:116-127): there are fixed m and D such that no algorithm decides solvability over ℕ of degree-≤D polynomials in m variables, even under the promise of at most one solution. The corollary is **not formalized**.

**Lean comparator.** The target is `OAI.SingleFold.main : MainStatement`, with standard axioms only.
- Statement: for all n ≥ 1 and all S with `REPred (· ∈ S)`, there exist m ≥ 1 and P : MvPolynomial (Fin n ⊕ Fin m) ℤ with `Represents P S`.
- `Represents P S` means: ∀ a, (a ∈ S ↔ ∃ w, evalNat P a w = 0), and any two zeros w, v of P(a,·) are equal.
- The challenge file's definitions are textually identical to `Model.lean`.
- **Match: exact.** The quantifier order, witnesses over ℕ, coefficients in ℤ, existence-iff-membership and uniqueness for every input are all the same as in the paper.
- The library also proves every proposition of the paper (growth, power, subset, compiler, rank one), but these are not compared.
- `formalization.yaml:1597-1599` lists the family.

## 2. Trust surface
Grep over all 28 files found none of the following: `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `set_option`.

The only notable item is **one kernel-checked finite enumeration**. `Duplication.bounded_points` (Duplication.lean:125) runs `decide +kernel` over 13·19·20 = 4,940 small rationals to find every point of naive height < 185. Torsion = E[2] is then proved from strict height growth under doubling. This replaces the paper's Nagell–Lutz argument. Other `decide` calls are on literals or on ZMod 5.

Imports are `Mathlib` only. The family relies on Mathlib's recent height API: `Height.logHeight`, `Northcott`, `WeierstrassCurve.addSubMap` and its log-height bound. `lean/patches` touches other packages, not Mathlib. I did not build Lean here.

## 3. Labels
- **A2.** The headline is ∀S ∃P with an exact-count property. One could argue A3, because the count is sharp. The corollary is A5. Confidence medium-high.
- **B1.** Evidence: "This proves the single-fold conjecture" (main.tex:33).
  - Flag *adds corollaries*: yes. It gives the finite-fold conjecture and promise-undecidability of Hilbert's tenth problem (H10). As a by-product it gives a new elliptic-curve Julia Robinson (JR) relation, which is an alternative route to the growth step of the Matiyasevich–Robinson–Davis–Putnam theorem (MRDP).
  - Flag *full only with prior results*: no. Every reduction is re-proved, and the cited theorems are standard background.
- **C1 primary.** The polynomial system is built explicitly.
  - C5 is secondary: the paper invokes Néron–Tate, Mordell–Weil, the isogeny theorem and Nagell–Lutz without proof.
  - C4 is secondary: height error bands, Pell ratio bounds and the quotient error.
  - C2 is secondary: routine inductions only.
  - `ih_strengthened` = false; `ih_template` = none.
  - **Computer-assisted: false.** The paper computes nothing; it does not even give the constants. The only computation is the Lean-only side enumeration above.
- **D3, provisional.** The top item is the elliptic-height square window and growth function (I19/I20).
  - Provenance flag (builds on prior model-produced work): **no**. All cited works are by human authors.
- **E fields.**
  - Problem field: Mathematical logic (03D35, 11U05, 03D25).
  - Lean-dir field: Number theory.
  - Essential method fields:
    - arithmetic geometry (elliptic curves, descent);
    - Néron–Tate heights;
    - Pell equations;
    - binomial parity (Lucas's theorem);
    - counter machines;
    - Diophantine definability, the home field.
  - Background-cited: Poonen and Miller–Shlapentokh (other rings), Chaitin.
  - 4 essential method fields are outside logic.
  - Theorems invoked without proof: 4 of 4 are from arithmetic geometry. Every logic and computability ingredient is re-proved.

## 4. Proof architecture
1. **Single-fold calculus** (main.tex §2): unique slacks and sign codes; conjunction, composition and disjoint cases, where every case-local variable is forced to zero; a sum of squares at the end.
2. **Arithmetic on E: y² = x³ − 25x.**
   - E(ℚ) = ℤP ⊕ E[2], proved by 2-isogeny descent in the appendix.
   - Rationals are coded uniquely by six naturals (p, n, d, t, s, q), using a shifted modular inverse.
   - Points are coded with an identity flag. Addition (7 gated cases) and fixed scalar multiples are single-fold.
3. **Heights.**
   - Define W(Q) = H(x([m_*]Q)), where H is the larger of |numerator| and denominator.
   - m_* is even, so it kills the torsion, and W depends only on j = |index|.
   - log W_j = a_E j² + O(c_E). Enlarging m_* makes a_E as large as needed while keeping c_E fixed.
   - A "representative" (largest x in its torsion coset, y ≥ 0) gives exactly one point per j.
4. **Growth function** (Prop growth).
   - The *bracket* W(Q) ≤ u + W₁ < max W(Q ± P) pins the index k at the scale of the input u.
   - The *square window* L₀ = W(2Q)·W(R)·W₁ versus D₀ = W(Q)²·max W(R ± P) satisfies log(L₀/D₀) = 2a_E(k² − r) + O(6c_E). So κ⁻¹ ≤ L₀/D₀ ≤ κ holds exactly when r = k².
   - The output is g(u) = W_{k²}, with δ(log u)² < log g(u) < u log u. This is a **single-fold Julia Robinson-type relation**.
5. **Power** (Prop power). Two Pell equations, with parameters bu and u:
   - the cutoff 0 < F, H < g(u) pins both indices below u;
   - residues ≡ n+1 then fix both indices at n+1;
   - the quotient F = cH + r gives c = bⁿ.
   - The scale u = (c+1)^ℓ(n+1)(b+1) + u₀ is a fixed polynomial in the output c, so no free parameter remains.
6. **Binary containment** (Prop subset): extract the digit binom(y,x) of (B+1)^y in base B = 2^{y+1}, and test its parity with Lucas's theorem mod 2.
7. **Machine compiler.**
   - A Minsky machine accepts S. Its run is encoded in base B = 2^w using state, branch and counter masks.
   - A clock register forces B ∈ (2(C+T), 4(C+T)], an interval that contains exactly one power of two. Summing the state equations gives B·I_h = H, so the halt happens exactly at the last time step.
   - The result is exactly one complete tuple for each halting input, which proves Thm main.

**Lean route differences.**
- Point addition: 5 cases with a slope-free "Line" relation.
- Rank: a full 2-descent through the Kummer map instead of a 2-isogeny descent. The generator is G = (25/4, 75/8) = (−4,6) + (0,0), and G is shown nontorsion by a 2-adic valuation argument.
- Torsion: proved by height growth under doubling plus the enumeration, not by Nagell–Lutz.
- Mordell–Weil and the canonical height: proved in-house (height descent; Tate limit), where the paper cites them.
- Universality: Mathlib's `PartrecToTM2` plus a base-5 macro counter machine.
- Case splits: Lean uses `Semi` (both R and ¬R are single-fold) to build guarded cases.

## 5. Eureka candidates (provisional)
| # | Candidate | N | F |
|---|---|---|---|
| E1 | Elliptic-height square window producing a single-fold growth function (I19, I20, I16, I15) | **N3** | F3 (F5 flavour) |
| E2 | Square-window lemma on its own (`HeightWindow.square_window`) | N3 inside E1; N2 alone | F3 |
| E3 | Self-referential Pell scale u = poly(c, b, n) with cutoff g (I24) | N2 | — |
| E4 | Clock register with a dyadic base window, plus the exact halt mask (I31) | N2 | — |
| E5 | Complete-witness hygiene: shifted-inverse codes, zeroed inactive cases, representatives | N1 | — |

**E1: for.**
- It supplies exactly the missing object: a single-fold Diophantine relation that grows faster than every polynomial but slower than u^u. Pell and Fibonacci relations cannot provide it because their solution sets are periodic.
- The trick is syntactically tiny. Heights grow *quadratically* in the hidden index, with bounded error. So one fixed product of heights tests the quadratic relation r = k², using the identity (2k)² − 2k² − ((r+1)² − r²) + 1 = 2(k² − r).
- With linear log-growth (Pell), no bounded multiplicative test can square an index.
- Nothing in the goal or in L mentions heights. A quick search found no JR relation built from canonical heights.
- In Lean, `growth` dominates 49% of the proof DAG.

**E1: against.**
- Rank-one curves and height or denominator growth are standard tools in Diophantine definability (Poonen 2002, which the paper cites; Denef; Shlapentokh; Eisenträger–Everest).
- The *target* was already identified in the literature. Robinson 1952 reduces exponentiation to any growth relation, and Cantone–Cuzziol–Omodeo 2024 propose replacing exponentiation by any exponential-growth relation.
- The Pell-to-power step is an adaptation that the paper names (Matiyasevich 1974 §4; Cantone–Cuzziol–Omodeo 2024 Lemma 6.1/Thm 5).
- The pivot from L may therefore be short.

E3 and E4 have named precedents (Matiyasevich 1974 and Cantone–Cuzziol–Omodeo 2024; Chaitin 1987 and Jones–Matiyasevich). Néron–Tate, Mordell–Weil and the descent are **N0 transfer**.

## 6. Load-bearing (Lean DAG)
The proof DAG has 756 declarations. Dominated share is the fraction of the DAG reachable only through an item.

| Item | Dominated share |
|---|---|
| `halts_sf` | 0.78 |
| `power` | 0.54 |
| `growth` | 0.49 |
| `graph_sf` | 0.20 |
| `growth_model` | 0.15 |
| `exists_counter` | 0.14 |
| `rank_one` | 0.12 |
| `square_window` | 0.005 |

The 20% "dependents" proxy selects only carriers (`Representation`, `SF`, `RationalCode`, `Counter.Witness`). This repeats the 287 finding that the proxy does not track eureka-ness.

`HeightDescent.finitely_generated` shows a share of 0 because it is used only through an `instance`, which the extractor cannot see.

Lines per branch:

| Branch | Lines |
|---|---|
| Elliptic arithmetic geometry | 1,947 |
| Growth | 779 |
| Coding / compiler | 1,442 |
| Pell / power / binary | 787 |
| Machine | 2,589 |

## 7. Correctness
**Verdict: no gap found.**

I checked every inequality and identity, including:
- the six-term height error and the κ constraints;
- the bracket's neighbour maximum;
- the index cutoff u^u < (2u−1)^{u−1};
- index pinning modulo u−1 and bu−1;
- the bound 2u − 1 − n − cn ≥ cn + 2c + n + 9;
- the existence cutoff ℓ > 3/(δ log 2);
- the no-carry decoding;
- the halt identity and the clock window;
- the ledger counts;
- the appendix arithmetic: 36 ∤ 62500, and the mod-5 exclusion of [2].

Lean proves the comparator statement verbatim with a clean trust surface. Its route through the arithmetic geometry is independent of the paper's, so the cited theorems are not a single point of failure.

Residual concerns:
- This is an extraordinary claim, open since 1974, and the Lean was not compiled here.
- The constants and the polynomial are never exhibited. They are effectively computable in principle, so there is no conflict with Matiyasevich's non-effectivity result.
- The corollary is not formalized.

## 8. Extraction friction
- The decisive construction sits in `\emph`-headed paragraphs inside the proof of Prop growth. In Lean it becomes the separate lemma `square_window`.
- Most objects are defined in display math: W, κ, m_*, a_E, L₀, D₀, g, u, B, J, M, I_q, R_j, R₀, C.
- `power.tex` also contains the binary-containment section.
- Lean namespaces do not match file names. `E`, `Bits` and `System` are each redefined several times.
- Instance-only dependencies are invisible to the extractor.
- The appendix and the Lean diverge in route, so joining items by name fails there.
- Useful cue phrases: "adapt Matiyasevich's exponential single-fold construction", "as presented in", "already appears in Chaitin's account", "We state the precise version needed here".

Literature-check sources (snippets only; full-text fetches failed):
- [Omodeo 2023](https://ceur-ws.org/Vol-3428/paper5.pdf)
- [Cantone–Cuzziol–Omodeo 2024](https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/2044/1126)
- [Matiyasevich 2010](https://www.mathnet.ru/eng/znsl3816)
- [Eisenträger–Everest](https://arxiv.org/pdf/0707.1485)
- [Poonen survey](https://arxiv.org/pdf/1309.0441)
