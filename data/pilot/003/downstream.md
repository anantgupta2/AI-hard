# Family 003: downstream targets for the sextic-twist Möbius ↔ cubic-theta duality

**Analyst:** DOWNSTREAM-TARGET agent, 2026-10-10.
**Lean:** read at text level only. I ran no lake, lean or comparator, because another build was in progress; the comparator results for this family are pending with the orchestrator.
**Extractor:** I ran `scripts/extract_lean.py 003` and `023` with output to the scratchpad.
**Literature:** WebSearch summaries only. WebFetch was not used.

## Item
**C1 (N3, F5, confidence 0.45).** The device works in five steps:
1. Twist the Möbius sum of a Hecke character over ℚ(√−3) by sextic residue symbols.
2. Apply Poisson in the twist. This produces sextic Gauss sums.
3. Use γ₂³ = μα to turn μ times the sextic Gauss sum into cubic Gauss sums, which are theta coefficients.
4. Reflect the theta function. The result carries a quadratic twist.
5. Close the estimate with the quadratic large sieve and a Heath-Brown recursion.

The output is a mean square with square-root cancellation, and the zero-free half-plane follows from it.

## Part A: `lean_status` = **formalized, different route**

**The device is in Lean and is load-bearing for all three 7/8 comparators.** Each of its pieces is present:

| Piece | Lean declaration |
|---|---|
| Sextic row twist | `CanonicalRowCompletion.rowTwist`, i.e. Ψ · sextic(m⁶f⁴z) |
| Local identity | `breveGamma1_gamma2_eq_neg_alpha_G` |
| Möbius ↔ Gauss conversion | `MixedGaussConversion.moebius_mixed_gauss_conversion` |
| Use inside the reflected moment | `SecondPassArithmetic.mobius_second_gauss_restore` |
| The mean square (A04-type) | `HeckeInverseAmplification.RawMoment`, proved by `raw_reference_moment` |

**Size.** The `raw_reference_moment` sub-cone has 10,161 declarations (~127k lines). That is about **55%** of the zeta cone, which has 18,626 declarations and ~254k lines.

**Chain from the zeta target to the local identity:**
`riemannZeta_ne_zero_of_seven_eighths_lt_re` → `zeta_nonzero` → `zeta_of_certified` → `chosen_moments_of_certified` → … → `raw_reference_moment` → … → `mobius_second_gauss_restore` → `active_productGauss_eq_mobius_converted` → `moebius_mixed_gauss_conversion` → `local_sign_conversion` → `breveGamma1_gamma2_eq_neg_alpha_G`. There are 25 links in all.

**Why the status is "different route":**
- The Lean appears to skip Q's 11/12 bootstrap.
- Manuscript A's direct route, A04 → p⁶ replication → Littlewood, is not the route the comparator uses. Its replication step exists only off-cone, as `PowerExtraction.from_mean_square_and_prime_rows`, with exponent 23/24.
- The frequency-transport form of the conversion is also off-cone.
- The Siegel comparator (2,616 declarations) uses none of the device.

## Arms
**Library buckets.** The library splits into three buckets:
- **Device declarations.** Listed in `lean_library_arms_common`.
- **Classical transfer.** Eisenstein/Kubota–Patterson theta and the quadratic sieve. This bucket stays in every arm.
- **The theorem itself.** The 7/8 nonvanishing results and the final assembly.

**Three arms:**
- **A:** no device, no theorem.
- **B:** device, no theorem.
- **C:** theorem available.

Only the comparison B vs A measures the device.

## Speedup targets (known theorems)

| id | target | Lean | Baseline | Speedup |
|---|---|---|---|---|
| S1 | **Patterson first moment** (release 023; comparator `PattersonFirstMoment`) | statable now (comparator definitions) | 023 cone: 11,245 declarations, ~181k lines. It uses none of the device (only 9 DirichletL declarations, from `CubicDyadicDecay`). | med |
| S2 | Heath-Brown 1986: one of 2, 3, 5 is a primitive root for infinitely many primes | statable now: `∃ a ∈ ({2,3,5} : Finset ℕ), Set.Infinite {p \| p.Prime ∧ orderOf (a : ZMod p) = p - 1}` | none | low |
| S3 | Positive proportion of nonvanishing L(1/2, χ) for cubic Hecke characters (DFDS 2024) | < 300 lines, using the `HeckeFamily` comparator definitions | none | low |
| S4 | Quadratic analogue (Gao–Zhao) | statable now | none | low |

## Open problems

| id | problem | Lean | payoff / confidence |
|---|---|---|---|
| O1 | **Artin's conjecture for base 2**. Claimed by 029 through a port of the device. | statable now: `Set.Infinite {p : ℕ \| p.Prime ∧ orderOf (2 : ZMod p) = p - 1}` | very high / med (029 is unreviewed) |
| O2 | ζ_K has no zeros for Re s > 1 − 10⁻⁶, with K = ℚ(ζ₁₂, 2^{1/4}). This is 029's theorem. It is not a corollary of 003, because K/ℚ(√−3) is non-abelian. | < 300 lines. Use an **existential continuation**: Mathlib's `dedekindZeta` is a bare LSeries and returns a junk value outside its convergence half-plane. | high / med |
| O3 | Quasi-RH for ζ_K of the S5 quintic x⁵ − x − 1 | < 300 lines | high / low |
| O4 | ζ(s) ≠ 0 for Re s > 5/6 | statable now | very high / low |
| O5 | Patterson's moment with a power-saving error term | statable now (023 definitions) | med-high / low-med |
| O6 | Zero density on 3/4 ≤ σ ≤ 7/8 beyond Guth–Maynard | statable now, via PNT+ `riemannZeta.N'` | high / low |

**Why O3 sits beyond both releases (my own reasoning).** Base change to ℚ(μ_{lcm(m,12)}), followed by factorization into entire Hecke L-functions, extends 029's strip to every finite-order Hecke L-function over an abelian number field. A Galois closure that is not solvable, as for S5, is therefore the first case outside both releases.

## Corollaries of the theorem (not reuse)
- **Siegel comparator.** It follows trivially with c = (log 3)/8.
- **Mertens and the prime number theorem.** M(x) ≪ x^{7/8+ε}, and the PNT error term x^{7/8+ε}. Both are statable now in Mathlib.
- **Claims made in the papers.** Linnik, Vinogradov, Miller, class numbers and idoneal numbers.
- **Dedekind zeta functions.** The zeta functions of ℚ(√−3), ℚ(ζ₁₂) and ℚ(2^{1/3}) have no zeros for Re s > 7/8.
- **Consumers.** Families 142 and 182 use the theorem.

## Negative controls
1. **Davenport–Heilbronn function (proved false).** It is a combination of L(s, χ) and L(s, χ̄) for the character χ mod 5 with χ(2) = i, weighted by κ ≈ 0.284079. It has infinitely many zeros with Re s > 1.
   - Lean: statable now with Mathlib's `DirichletCharacter.LFunction`.
   - The device must fail here, because there is no Euler product and so no multiplicative μ.
2. **Epstein zeta of x² + 5y² (proved false; Davenport–Heilbronn 1936).** It has zeros with Re s > 1.
   - Lean: statable now with Mathlib's `LSeries`.
   - The 1936 result was not re-checked by web search in this session.
3. **GL(2), L(s, Δ).** The device should not help, because there is no theta dual. This control needs a major new library.

## Top 5 (all Lean-usable)
1. **S1, Patterson first moment.** Uses the existing 023 comparator and its large formal baseline, with the three-arm design.
2. **O1, Artin for base 2.** A one-line statement.
3. **O2, ζ_K for K = ℚ(ζ₁₂, 2^{1/4}).** Isolates reuse of the device from reuse of the theorem.
4. **O5, power-saving Patterson.**
5. **S2, Heath-Brown's 2/3/5 theorem.**

## Precedent
- No earlier equivalent was found. The closest work is Dunn–Radziwiłł 2024: the same objects, approached from the opposite direction and conditional on GRH.
- Within the release, family 029 reuses the device.
- Outside the release, coverage is press only, with no independent verification.
