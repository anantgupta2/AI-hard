# 194: Downstream targets for the uniform complex estimate (Thm 2.1)

**Item:** C1 of `novelty.json`, the paper's Thm 2.1 (complex.tex:55-82). It is an F5/F3 estimate, produced by a construction.

- **Setting.** C is a commutative ring (not necessarily Noetherian) and I = (z_1..z_h). λ is an additive length on I-power-torsion modules with zero-stability. The powers of z behave like a parameter system for λ:
  - λ(C/(z^a)) = a^h μ;
  - positive Koszul homology has λ-length 0.
- **Complex.** F is a finite free complex in degrees 0..h, contractible off V(I). Its alternating rank is 0 and all its entries lie in I^s.
- **Conclusion.** λH_0(F) ≥ μ s^h (b_0 − A_h Σb_i / s).
- **Mechanism.**
  1. On the blowup, divide by L^s to get G_i = O(−is)^{b_i}.
  2. Pair with an Eisenbud–Schreyer-type bundle whose roots are at ⌊sρ_j⌋, where the ρ_j are the roots of H′ and H = ∏(x+i).
  3. This forces χ ≥ 0, and equal layer sums then isolate b_0 with coefficient 1.

**Method:** text level only. No `lake build` and no comparator run (the checkout is shared, and Lean is trusted per the 2026-10-12 rule).
- The dependency chain was traced by grep and cross-checked against `data/items/194_lean.json`.
- About 14 web searches, read as snippets only. WebFetch failed on DNS for every host tried, and arxiv.org is blocked. Everything external is **unverified**.

## Part A: Is the item in the Lean?

**lean_status: as in paper.**

**Two Lean forms of the item:**
- `OAI.Lech.complex_theorem` (ComplexTheorem.lean:26) is Thm 2.1 with the paper's hypotheses: ZeroStability, `LocallyContractibleOff`, 0 < μ < ∞, alternating rank 0, entries in I^s, and A depending only on h = n+1.
- `OAI.Lech.complex_estimate_basis` (ComplexEstimate.lean:22) is the on-chain form. Its hypotheses are marginally weaker:
  - only `DirectSumZero`, with no filtered-colimit stability;
  - no μ > 0;
  - "acyclic after inverting each z_k" instead of local contractibility.

**The proof follows the paper's route.** The blowup appears as Čech complexes on the Rees-algebra charts. The supernatural bundle is rebuilt over ℤ through (P¹)ⁿ → Pⁿ (`ProductSourceCover*`). The roots are `Numerical.roundedRoot`.

**Comparator chain:**
`dutta_domain` → `dutta_complete_charp` → `dutta_algClosed` → `cyclicDuttaContribution_lower` → `CharP.dutta_lower_bound_infinite_perfect` → `CharP.dutta_minimal_estimate` → `complex_estimate_allModule` → **`complex_estimate_basis`** → `ReesRoot.sum_estimate` → `rootTotal_euler_nonnegative`, plus `Numerical.uniform_from_sum_estimate`.

**Knockout check.** Removing the item breaks every positive-dimensional case of the comparator; only `dutta_dimension_zero` survives.

**Gaps and notes:**

1. **Wrong line in `novelty.json`.** It cites ComplexEstimate.lean:88, but the declaration is at line **22**.
2. **Comparator scope.** The comparator uses the item only through `complex_estimate_allModule`, a length on all modules: in char p, the normalized length on the perfection. The general `TorsionLength` version is proved. The mixed-characteristic use (CLMST perfectoid lengths, mixed.tex:270) is not formalized.
3. **Size.** The upstream closure of `complex_estimate_basis` is 2,679 declarations (about 20.9k lines in 163 files). That is 77% of the comparator DAG (3,499 declarations, about 32k lines).
   - Almost all of it is the blowup-pairing positivity: the `sum_estimate` closure has 2,641 declarations.
   - The root numerics are only about 470 lines.
   - The acyclicity half is about 880 lines.
4. **The comparator is weaker than the headline.** Lech is not stated in Lean. The comparator asks only for complete local *domains*.
5. **The Lean is stronger than the comparator.** `dutta_complete_charp` has **no `IsDomain`**. So Lean proves χ_∞(F) ≥ e(R) for every complete Noetherian local ring of characteristic p.

**For the speedup test:** hide `complex_estimate_basis` and `complex_estimate_allModule` together with `ComplexTheorem`, `SumEstimate`, `ReesRoot*`, `ProductSourceCover*`, `NumericalSupport` and everything downstream. Run three arms:
- **(A)** the baseline library;
- **(B)** the baseline plus the statement;
- **(C)** the baseline plus the statement and the internal interfaces `sum_estimate`, `rootTotal_euler_nonnegative` and `uniform_from_sum_estimate`. Target O1 needs this arm.

## Part B: Targets

**Bottom line: no strong device-reuse speedup target was found.**

- Every known theorem that the estimate shortens substantially is reached through the Dutta bound χ_∞ ≥ e(R), which makes it a theorem corollary.
- Coefficient 1 is the whole point of the device, but only e(R)-sharp statements need it: Lech, Dutta ≥ e, and length ≥ e.
- Weaker known consequences have elementary proofs without the device (see the negative controls below).

### Speedup targets (known theorems)

| # | Target | Lean | Speedup | Counts as reuse? |
|---|---|---|---|---|
| 1 | IMW 2022: χ_∞(F) ≥ e(R) for localized standard graded char-p algebras (≈45 pp, via lim Ulrich) | < 300 lines (graded localization, completion base change) | high | **no**: comparator corollary via completion; use as calibration |
| 2 | IMW length bound ℓ(M) ≥ β_0 e(R) over char-p complete intersections (strict CI known) | major (needs Dutta/Kurano χ_∞ = χ for CIs) | med | **no**: corollary of the Dutta bound plus χ_∞ = χ |
| 3 | Family 193 (Serre positivity), Lemma pos:positive-evaluation | major (193 has no Lean) | low | **component only**: it reuses the routine acyclicity half (Koszul homology first), not deep entries, the blowup or the pairing |

### Open problems

| id | Problem | Match | Lean | Confidence |
|---|---|---|---|---|
| O1 | **Local pure-type estimate with non-uniform depths** s_i: λH_0 ≥ μ b_0 ∏d_i/h! (1−o(1)), where d_i = s_1+…+s_i. This is the local analogue of Herzog–Kühl / the HHS lower bound. | exact obstruction; needs the design (twists O(−d_i), ES roots for the pure degree sequence) | **statable now** | 0.45 |
| O2 | **IMW Length Conjecture** ℓ(M) ≥ e(R) | partial: the device controls χ_∞, not ℓ. They agree only on numerically Roberts rings, and non-Roberts CM rings exist in char p. | **statable now** | 0.2 |
| O3 | **Kurano–Roberts positivity and IMW Conj 8.1 in mixed characteristic** (Dutta multiplicity via local Chern characters) | strong: the same inequality without Frobenius. The paper already runs Thm 2.1 with perfectoid lengths for Lech. Missing: identify the λ-limit with the local-Chern-character Dutta multiplicity (Adams operations?) | major | 0.3 |
| O4 | **Boij–Söderberg cones over local rings without lim Ulrich sequences** (IMW 2023, Yhee) | medium: the device gives only one Boij–Söderberg functional | major | 0.2 |
| O5 | **HMQS asymptotic Lech inequality in all characteristics** | weak (wrong direction for non-perfect ideals) | < 300 lines | 0.1 |

### Theorem corollaries (they show reach, not reuse)

- Lech in all characteristics.
- `dutta_domain`.
- The Lean-only non-domain Dutta bound, which keeps the factor b_0.
- The IMW 2022 standard-graded theorem.
- The length conjecture for char-p numerically Roberts rings, including all complete intersections. Whether this was already known is unverified.
- e_HK(J) ≥ e(R) for m-primary ideals J of finite projective dimension. Prior status unverified.
- Weakenings and earlier partial results:
  - Dutta positivity and the New Intersection Theorem in char p;
  - Ma 2017 and the graded cases of Lech;
  - a local asymptotic HHS-type bound / Betti–length trade-off. This is a direct instance with λ = length over CM rings; it appears new but is unverified.

### Release reuse

- **193 (Serre positivity):** reuses the acyclicity half only. It cites the Lech paper's Thm 3.1 for normalized lengths.
- **195 (SmallCM) and 200 (EGH):** none.
- **Lean:** no file outside `OAI/RingTheory/Multiplicity` imports the folder, apart from the `OAI.lean` aggregator.

### Negative controls

1. **Ordinary χ over non-Roberts rings is a proved-false analogue.** Roberts' short complex has χ(F) < 0, and Dutta–Hochster–McLaughlin give χ(M,N) = −1. Instantiating the item with ordinary length on such a ring must fail at `_hK` or `_ha`.
2. **Total rank and generalized total rank.** Walker's theorem holds, while the generalized version is false in odd characteristic. The ranks enter the item only as an O(1/s) error, so the device gives no Betti bound.
3. **The New Intersection Theorem and Dutta positivity in char p need no coefficient 1.**
   - H_0(Φⁿ F) surjects onto (R/m^[q])^{b_0}, which gives a lower bound of order q^d.
   - The OAI Frobenius growth bound gives an upper bound of order q^k.
   - So the expected speedup is about zero. Both statements are statable now, which makes this a cheap check of the harness.
4. **Kunz's Hilbert–Kunz Lech inequality and Watanabe–Yoshida** involve no deep complex.
5. **Tightness control.** For Koszul complexes K(z^s), λH_0 = μ s^h exactly, so coefficient 1 is optimal.

## Top 5 (Lean-usable first)

1. **O1, non-uniform depths (statable now).** It is the only Lean-usable target that forces reuse of the device's *design*. Arm C should turn it into a re-parametrization, while arm A has no route. Caveat: it generalizes the item itself.
2. **IMW 2022 standard-graded Dutta bound (< 300 lines).** The cleanest measurable before/after pair: a 45-page lim-Ulrich proof becomes completion glue. It is calibration only, because it is a corollary.
3. **O2, Length Conjecture (statable now).** The informative experiment is the general case. Expect failure, and a failure maps the device's scope.
4. **New Intersection Theorem in char p (statable now; negative control).** A harness that reports a large speedup here is miscalibrated.
5. **O3, mixed-characteristic Dutta positivity and bound (needs a major library).** The strongest genuine reuse candidate in mathematical terms, but it can only be tested informally.

## Precedent

- **Earlier equivalents:** none found. The closest is the graded Eisenbud–Schreyer / Eisenbud–Erman pairing: the HHS bound for degrees (0, s, …, hs) is s^h b_0. Next come IMW2025 and IMW–Zhuang, which use the blowup for Ulrich questions but have no pairing. This agrees with `novelty.json`.
- **After 6 Oct 2026:** only catalogue listings turned up (Pitt catalogue, kingy.ai). There is no expert reaction, no error report and no reuse.
- All of this is at snippet level.
