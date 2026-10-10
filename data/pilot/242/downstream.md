# Family 242: downstream targets for the elliptic-height single-fold growth function

Machine-readable version: `downstream.json`. Analysis is at text level only: there is no Lean toolchain here, so nothing was compiled.

**Item.** Prop growth. Work on E: y² = x³ − 25x and set W(Q) = H(x([m*]Q)).
- An **index bracket**, W(Q) ≤ u + W₁ < max W(Q ± P), pins the index k at the scale of the input u.
- A **square window** compares W(2Q)·W(R)·W₁ with W(Q)²·max W(R ± P). The ratio lies within κ exactly when index(R) = k².
- The output g(u) = W_{k²} is single-fold, with δ(log u)² < log g(u) < u log u.

Type: F3 (+F5).

## Part A: Is the item in the Lean?

**lean_status: "as in paper".** `GrowthCompilation.growth` (EllipticGrowth.lean:487) states Prop growth verbatim, including δ = 1/(128a). `Bracket`, `Window` and `Representative` (EllipticGrowth.lean:281, 283, 145) are the paper's displayed conditions, and the comparator depends on them. Only the upstream arithmetic geometry takes a different route.

**Dependency chain from the comparator** (BFS over `data/items/242_lean.json`):

`main` → `recursively_enumerable_sf` → `CounterCompilation.halts_sf` → `system_sf` → `ScalarSF.powerRel` → `PowerCompilation.power` → **`GrowthCompilation.growth`** → `EllipticModel.growth_model` → `window_iff` (also via `growth_pair_existsUnique`) → **`HeightWindow.square_window`**

Dominated shares of the DAG:

| Declaration | Share |
|---|---|
| `growth` | 0.49 |
| `growth_model` | 0.15 |
| `square_window` | 0.005 |

**Key Lean statements** (verbatim copies in the JSON):
- `HeightWindow.square_window` (HeightGrowth.lean:233). It holds for **any** W : ℕ → ℕ with |log W_j − a j²| ≤ c, and states: product window ⟺ r = k².
- `GrowthEstimate.bracket_unique` (HeightGrowth.lean:41) and `eventual_output` (HeightGrowth.lean:143), both for a generic sequence.
- `EllipticModel.sequence_approx` (EllipticGrowth.lean:97): log W_j = 2m²ĥ(P)·j² ± c.
- `growth_model` (EllipticGrowth.lean:327) and `growth` (EllipticGrowth.lean:487).
- `PowerCompilation.power_of_growth` (Power.lean:279). `power` (Power.lean:299) is literally `power_of_growth` applied to `growth`.

**Gaps between the paper and the Lean:**
- **Upstream route differs.** Rank one comes from a full 2-descent through the Kummer map. Torsion comes from height growth plus a `decide +kernel` enumeration of 4,940 rationals. The canonical height and the uniform height bound are proved in-house. The paper instead uses a 2-isogeny descent, Nagell–Lutz and Silverman.
- **The window is generalised** to arbitrary quadratic-log sequences. This is the reusable form of the device.
- **The height API is tied to y² = x³ − 25x.** Using the device on another curve means re-proving that API.
- **Constants are existential**, in both the paper and the Lean. There is no explicit (unknowns, degree) pair.
- **Promise-undecidability is not formalized.** The comparator statement never mentions g.

## Precedent check: earlier equivalent found, so downgrade

**Garcia-Fritz, Pasten and Vidaux**, *Effectivity for existence of rational points is undecidable* (arXiv:2311.01958, Nov 2023; J. Number Theory 276 (2025) 81–97). I read the full text. Their setup:
- the rank-one curve y² = x³ + 2, with Γ = [200]E(ℚ);
- ĥ(Q_k) = k²D, with the naive height within 4 of the canonical one;
- **approximate (bounded-error) height comparisons**, used to define the relation "a and b are consecutive squares" on indices (Lemma 4.7). From this they interpret (ℕ, +, ×) in ℚ with height-comparison predicates.

This is the core mechanism of 242's window: index squaring on a rank-one curve through archimedean height comparisons with bounded error. The 242 novelty pass called this step unprecedented. **242 does not cite GPV.** OpenAI's own family **004** (H10 over ℚ, same release) does, describing it as using "elliptic canonical heights to encode consecutive squares".

**What remains new in 242:**
1. The comparisons are realised as Diophantine product inequalities over ℕ, so no extra predicates are needed. This is routine.
2. Single-fold uniqueness, via representatives and the neighbour-max bracket. This is N1 hygiene.
3. The specific five-term window, and the bracket that turns it into a growth function for Prop power. This is a close variant of GPV.

**Recommendation.** Grade C1 **N2, not N3**, unless an expert judges single-fold-ness itself to be the hard step. Test 4's L+ arm must include GPV.

**Other precedent results:**
- Nothing found after Oct 6, 2026. Only the arXiv API was queried, because the web tools hit a session limit.
- 242 still uses **Pell** in Prop power, so Pheidas's AIM Q9 ("elliptic curves instead of Pell") is only half realised.

## Part B: Targets

### Speedup targets (known theorems)

| # | Target | How the item helps | Speedup | Lean |
|---|---|---|---|---|
| 1 | **GPV Thm 1.1/1.2** (height-predicate interpretation of (ℕ,+,×) in ℚ; undecidability) | `square_window` decides r = k² in one comparison. OAI already supplies a rank-one curve with a uniform height bound, which replaces GPV's LMFDB and Silverman inputs. | med-high in Lean, low on paper | < 300 lines (height predicates plus a positive-existential interpretation, over Mathlib's `Height.logHeight`). No formal proof exists to compare against. |
| 2 | **Pell-free `Dioph.pow_dioph`** (Pheidas Q9, strict reading) | Supplies the growth half, and index multiplication by polarisation. It has no elliptic substitute for Pell's index-from-congruence step. | low; this is a proof-route test | statable now; compare with Mathlib's Pell proof (about 1,500 lines, estimated) |
| 3 | Poonen 2002, the index-squaring Lemma 8 over O_K | An archimedean window is not Diophantine over O_K. | low | needs a major new library |
| 4 | Eisenträger–Everest 2009 (rings ℤ[S⁻¹]) | Numerator and denominator cannot be separated there, so W is unavailable. | low | needs a major new library |

**Verdict.** The only strong known target is GPV, and it is also the precedent. For other known theorems: no strong candidate found.

### Open problems

1. **Explicit single-fold (unknowns, degree) bounds** (Matiyasevich 2000 problem list).
   - Statable now.
   - Needs explicit height constants.
   - This refines the theorem; it is not reuse of the device.
2. **Exponentiation with poly(log c)-bit witnesses, and Adleman–Manders D vs NP.**
   - The growth witnesses have log-size O((log u)²), and the Pell witnesses in Power are capped by g(u). An audit could show c = bⁿ has polynomially bounded witnesses.
   - Low confidence: the link to D vs NP was **not re-verified**, and a hidden obstruction is likely.
   - The sub-claim is statable now.
3. **Finite-fold definition of ℤ in O_K** (Pheidas-type; H10 over O_K was settled in 2024–25).
   - Archimedean comparisons and infinite unit groups are the obstacles.
   - Needs a major new library.
4. **Single-fold or finite-fold over F_q[t] or ℤ[T].**
   - Function-field Néron–Tate heights are degree-quadratic, so degree comparisons could replace the window.
   - This is the most promising adaptation. Needs a major library.
5. **CCO 2024 §7–8: univocal growth relations.**
   - Goal (1) is answered by the theorem. The CCO candidates are untouched by the device.
6. **Minimal height predicates for GPV-type undecidability.**
   - Our own formulation; its status is unverified.

### Theorem corollaries (not reuse of the device)
- the finite-fold conjecture;
- promise-H10 undecidability with fixed m and D;
- single-fold exponentiation (`power`), and with it single-fold primes, factorial and universal equations;
- non-effectivity of finite-fold bounds.

### Release reuse
- **Lean:** no other OAI directory imports SingleFold.
- **Family 004** (H10 over ℚ; not formalized) uses the same N0 ingredient, hgt(x(nP)) = 2ĥn² + O(1), only to bound indices. It has no window or growth function.

### Negative controls
1. **Mathlib `pow_dioph`.** Without uniqueness no cutoff is needed, so no speedup is expected.
2. **Definitions over ℚ in the pure ring language.** Height comparisons are not Diophantine there; GPV had to add them as predicates.
3. **A linear-growth (Pell) window.** It can test only linear index relations. This is an expected failure, not a published theorem.

## Top 5 (Lean-usable first)
1. **Re-prove GPV with `square_window` in the library.** This is the cleanest measurable test of the shared mechanism. It is not jump evidence, because GPV predates the item.
2. **Pell-free `pow_dioph`.** Success is objective: a proof that imports no Pell file. Failure is expected and informative.
3. **Witness-size audit of `power`.** It is cheap and decisive. If it succeeds, the device's quasi-polynomial growth does something Pell cannot.
4. **Explicit (unknowns, degree) bounds.** Lean-ready, but it measures the theorem's reach rather than the device.
5. **Finite-fold over O_K or F_q[t].** These are the natural open homes for the device, but they are not Lean-usable now.

## Search log
- BFS chain over the extractor DAG.
- Import grep across OAI.
- CONTENTS.md grep, which surfaced family 004.
- Family 004's introduction and bibliography, which led to GPV.
- arXiv API, then the GPV PDF, read in full.
- Searches for Adleman–Manders, zbMATH and MathOverflow were blocked by the session limit.
- Mathlib is not available locally, so its line counts are estimates.
