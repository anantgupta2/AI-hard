# Family 003: The quasi-Riemann hypothesis (family analysis)

Commit `fd4aeeb`. Three manuscripts:
- **Q**: *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s>7/8*, 2026-09-30. `build/paper.tex`, 16,677 lines. Lean-formalized.
- **A**: *The Quasi-Riemann Hypothesis*, the alternate 11/12 proof, 2026-10-05. `build/paper2.tex`, 3,988 lines. Not formalized separately.
- **S**: *Uniform exclusion of Landau–Siegel zeros*, 2026-10-01. 773 lines. Lean-formalized.

Analyst role and limits:
- Paper and Lean were read **at text level only**. Lean was not compiled; lake and lean were deliberately not run. The orchestrator compiles the comparators.
- S was read in full and re-derived.
- For Q and A, every statement and outline was read. The long inductive proofs (Q:9783–14983 and A's appendices) were skimmed only.
- `extract_lean.py` was run with `--out` pointing to the scratchpad.
- Web claims rest on WebSearch snippets; WebFetch was not used.

## 1. Main statements

**Q, Theorem 1.1 (Q:106-111).**
- Every finite-order Hecke L-function over Q(√−3) has no zero in Re s > 7/8.
- The same holds for every Dirichlet L-function, including ζ.
- A pole at s = 1 is allowed for a principal character.

**A, Theorem 1.1 (A:73-77).** The same statement with 11/12, proved differently.

**S, Theorem 1 (S:66-75).** There is an absolute c > 0 such that (1−β) log q ≥ c for every real zero β ∈ (0,1) of every primitive nonprincipal real Dirichlet L-function of conductor q ≥ 3.

### Lean comparators: do they match the classical claim?

| Comparator | Statement | Match |
|---|---|---|
| `QuasiRiemannHypothesis` | `(7/8:ℝ) < s.re → riemannZeta s ≠ 0`. Imports Mathlib only, so this is **Mathlib's `riemannZeta`**. No OAI declaration shadows it. | **Exact** classical quasi-RH with the explicit 7/8. No extra hypotheses. At s = 1 Mathlib's junk value is nonzero (`riemannZeta_one_ne_zero`), so there is no artefact. |
| `DirichletSevenEighths` | For all q (NeZero) and all χ, with ¬(χ = 1 ∧ s = 1): `DirichletCharacter.LFunction χ s ≠ 0` (Mathlib). | Exact. It is even stronger than the headline: it covers imprimitive χ and q = 1. |
| `HeckeSevenEighths` | The challenge file **defines its own** L-function: a theta-product `WeakFEPair`, Λ·π^s/Γ(s)/6, over `CyclotomicField 3 ℚ`. `Character` = MulChar on O/m that is trivial on units. | Plausibly faithful. The 30 challenge definitions occur verbatim in the library. The library proves `LFunction_eq_ideal_tsum` (Re s > 1) and holomorphy off {0,1} (Hecke/IdealBridge.lean). These lemmas are **not part of the comparator**. Because the class number is 1 and there are no real places, `Character` covers all finite-order Hecke characters (my reasoning). |
| `SiegelZeros` | ∃ c > 0, ∀ q ≥ 3, χ primitive, nonprincipal and real-valued, 0 < β < 1 with L(β) = 0 ⇒ c ≤ (1−β) log q. | Matches the logarithmic Landau–Siegel statement. It is a **trivial corollary** of the Dirichlet comparator (β ≤ 7/8 ⇒ c = (log 3)/8), yet it is proved independently in Lean. |

### Trust surface
Text-level grep over 3,232 files in `OAI/NumberTheory/DirichletL` and `SiegelZeros`:
- **0** each of `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `@[extern`, `unsafe`, `opaque`, `set_option`, `macro` and `elab`.
- 770 `decide` calls, all small side conditions.

The comparators permit only `propext`, `Quot.sound` and `Classical.choice`. `enable_nanoda` is false, so there is no second-kernel replay.

The external imports are:
- Mathlib.
- PrimeNumberTheoremAnd (c39a751, `SiegelZeros.HadamardSupport` and `Wiener`). Its `SiegelZeros/*.lean` files (6,754 lines of Hadamard factorization support) are **added by OpenAI's patch** `lean/patches/PrimeNumberTheoremAnd-lean4341.patch`. They contain no sorry.
- RellichKondrachov (one import).

**Size.** 31,058 declarations. The zeta target reaches 18,626 of them. The largest directory shares are:
- Moments 16.5%
- Eisenstein 15.4%. This builds the cubic theta function from hyperbolic-3-space spectral theory, including the resolvent, scattering and Eisenstein residues.
- Detector 11.9%
- Descent 6.4%
- CubicSieve 6.1%
- Hecke 6.0%
- Inversion 5.0%
- GaussSum 4.7%
- QuadraticSieve 4.3%

The Siegel target reaches 2,616 declarations. These include **none** of the 7/8 chain, so it is an independent formal proof.

**Route differences between Lean and paper:**
- The Lean 7/8 proof starts directly from β > 7/8. `HighData` has κ ≤ 1 and the hypotheses are only β ≥ 51/100. It appears to skip the paper's Part I (11/12) bootstrap, which the paper uses to get Δ ≤ 1/24 (Q:6812-6822).
- The Lean Siegel proof replaces S's nearest-point interpolation lemma with a local isolated Bézout bound (`Intersection/IsolatedBezoutFromRegularSelection.lean:25`).
- All of the papers' cited inputs are re-proved in Lean: Patterson/DR theta, the Goldmakher–Louvel sieve, BGL and the Hadamard product.

## 2. Labels

- **A: A5** (nonvanishing, i.e. impossibility). The explicit-rate flag is set: 7/8 and 11/12 are explicit, the Siegel c is not. Confidence high.
- **B: B1** (confirms quasi-RH fully). Flag *adds corollaries*:
  - Vinogradov's nonresidue conjecture and deterministic square roots (Q:325-361);
  - Landau–Siegel zeros, PNT in arithmetic progressions with x^{11/12} log x, the Miller test, effective class numbers and Euler's 65 idoneal numbers (A:97-125);
  - downstream release families 029, 142 and 182.
  - Not *full only with prior results*.
- **C: primary C3**, with secondaries C4, C2 and C5.
  - Q is a contradiction against a hypothetical family supremum β\*. A is a direct estimate plus Littlewood. S is a contradiction along a sequence.
  - **ih_strengthened = yes**: the canonical family adds an averaged squarefree label f with χ_n(f)^4 (A:641-648, A:1261), and Q adds prime-slot marks.
  - **ih_template = yes**: "add a parameter" and "carry an extra tracked quantity", the Heath-Brown admissible-exponent method.
  - Computer-assisted: **no**.
- **D: D3 (provisional, 0.4)**, resting on C1. See the novelty pass.
- **E.**
  - Problem field: number theory (MSC 11M26, 11M20, 11R42).
  - Lean-dir field: NumberTheory.
  - Method fields:
    - essential: automorphic forms (metaplectic cubic theta), analytic number theory (large sieves, Poisson, zero detection), algebraic number theory (Gauss and Jacobi sums, sextic reciprocity, Kummer theory), complex analysis, and transcendence theory (S);
    - essential in Lean only: spectral theory of hyperbolic 3-space, and commutative algebra (local Bézout);
    - corollary-only: complexity theory;
    - background-cited: zero density (Guth–Maynard), Vinogradov–Korobov, Goldbach.
  - Cross-field count: 5.
- **Provenance flag: partial.**
  - Q cites OpenAICubicFirstMoment (family 023, model-produced) as "not used here".
  - A cites Q.
  - S cites no model output.
  - No model-produced precedent for the problem was found.

## 3. Proof architecture

**Q (7/8).**
1. β\* = the supremum of zero real parts over the primitive Hecke family. The continuation criterion (Q04): if a probe J_η is small directly (≪ Z^{C(σ₀)+ω}) and close to a Mellin signal containing 1/L (error ≪ Z^{C(β\*)−σ}), with margins uniform in η, then 1/L continues past β\*, a contradiction.
2. Arithmetic:
   - γ₂(p)³ = −α(p);
   - the sextic symbols keep their zeros;
   - reciprocity phases.
3. Completed cubic reflection (Q11) for theta sums over cn³ twisted by sextic symbols. The dual sums carry a **quadratic** twist, so the quadratic large sieve bounds them.
4. **Base probe** I_η(X,Y,Z) (Q16). The low side is ≪ Z^{1/4+ε} at X = Y = Z^{1/2}.
5. Poisson in m gives rows u·a⁶. By the local Euler identity (Q18), the principal row is a nonzero scalar times the Mellin signal of **1/L_F(s,η)**.
6. A zero detector gives two saturated witnesses (Q20). The sextic large sieve counts the rows. Rows are measured against C(β\*) (Q25, the bootstrap).
7. The margins are 1021/25000, 1/40, 1/1200, 43/300 and >1. This gives the saving 1/4800 and the **11/12** theorem (Part I). The Dirichlet case follows by quadratic transfer.
8. Part II:
   - a compensated probe (Q27): prime slots, marked minus rescaled;
   - X = Z^{17/48}, Y = Z^{23/48};
   - C_II(s) = s − 11/16;
   - a marked inverse moment (Q31) whose consequence is eq:raw-moment (Q33);
   - a plain fourth moment (Q34) and refined row counts, giving **7/8**.

**A (11/12).**
1. The family is A_u(D) = Σ μ(n)ν(n)χ_n(u)W(Nn/D) (A03).
2. Key estimate (A04): Σ_{N u ≤ D^{1+θ}} |A_u|² ≪ D^{2+θ+ε}.
3. Since A_{p⁶} = A_1 + O(D/Y), the target appears in the family about Y/log Y times. This gives A_1 ≪ D^{11/12+ε} (A05), and Littlewood (A06) finishes.
4. A04 is proved as follows:
   - Poisson in u: sextic Gauss sums absorb μ into cubic Gauss sums, because γ₂(n)³ = μ(n)α(n) (A07).
   - These are Patterson theta coefficients. Theta reflection with a quadratic twist plus the GL quadratic sieve give the completed bound (A12).
   - Cube factors are removed by Möbius inversion (A13).
   - A transfer estimate (A14) uses two Poisson summations at contracted scales and is iterated O(1) times (A11).

**S (Siegel).**
1. A Siegel zero makes primes with χ(p) = −1 carry almost all of the mass Σ log p/p up to q^{O(1)} (S02).
2. Build K = Q(√d, √2), points θ_n on a box of side N, and three conjugates. The interpolation lemma (S03) gives a nonzero determinant Δ with rows weighted by α₁ + H(α₂+α₃) (S06).
3. For inert p > H, θ^p ≡ σθ or στθ (mod p). A unitriangular replacement then gives p^{E_p} | Δ (S08).
4. Comparing norms gives S₁ log U against (3/4)(S₁+S₂) log U, so 1 ≤ 7/8, a contradiction.
5. Sanity check (mine): without a Siegel zero, Frobenius ∈ {id, σ, στ} has mass ≈ ¾ log U, and the bounds balance at exactly 3/4. So the method does not prove too much.

### Comparison of the two 11/12 proofs (Q Part I vs A)

| | Q Part I | A |
|---|---|---|
| Object | Probe mixing sextic Gauss sums with completed cubic-theta rows. Its principal Poisson row contains 1/L. | Möbius sum embedded in a sextic-twisted family. |
| Logic | Indirect bootstrap on β\*, using a zero detector and the sextic large sieve. | Direct, unconditional mean square, then p⁶ replication, then Littlewood. |
| Shared core | γ₂³ = −α, theta reflection to a quadratic twist, GL sieve, cube completion. | The same, plus the HB recursion. |
| Exponent | C_I(s) = s − 2/3; weakest margin 1/1200. | (1 + 5/6)/2 = 11/12, from Y = H^{1/6}. |
| Relation | Q derives A's key estimate as eq:raw-moment (Q:12370) but uses it only for sixth-power-*free* rows. | A notices that the sixth-power rows replicate the target, which gives a far shorter proof. |
| Lean | The Lean 7/8 route seems to skip Part I. | Not formalized. Its engine (raw moment) has a counterpart on the 7/8 path. |

## 4. Items
There are 63 items in `family.json`: Q01–Q37, A01–A17 and S01–S09. Grades:

| Grade | Items |
|---|---|
| **N3 (provisional)** | Q16 (base probe), A03 (sextic Möbius family), A04 (mean square), S06 (weighted determinant) |
| **N2** | Q11, Q12, Q13, Q18, Q20, Q25, Q27, Q29, Q31, Q33, Q34, A05, A09, A11, A12, A14, S03, S05, S08 |
| **N0/N1** | the rest |

## 5. Eureka candidates (provisional)

1. **C1, sextic-twist duality (N3, F5).**
   - The device: twisting the Möbius (or 1/L) sum by sextic residue symbols makes Poisson duality turn μ times a sextic Gauss sum into cubic-theta coefficients. Automorphy plus the quadratic large sieve then give square-root cancellation on average.
   - For: no source was found; it is the whole engine of A and Q; family 029 reuses the device.
   - Against: every ingredient is classical (Hasse/HB00 identity, Patterson, DR, GL, HB). DR may contain the reverse bridge. Gao–Zhao is the quadratic analogue.
2. **C6, Siegel weighted Frobenius determinant.**
   - Before the quick check it was N3 (F3); after it, **N2**. The Dobrowolski/Cantor–Straus Frobenius-congruence determinant for Lehmer's problem is the same divisibility mechanism.
3. **C2, β\* family bootstrap plus saturated zero detector (N2).** It replaces DR's GRH and is classical in kind.
4. **C3, compensated probe (N2).** Mollifier-like and design-specific.
5. **C4, sixth-power replication/amplification (N2).** Standard amplifier.

## 6. Correctness concerns
- These are extraordinary, unreviewed claims. The formal check, pending from the orchestrator, is the decisive anchor.
- A04 needs square-root cancellation over rows D^{1+θ}, beyond the BGL sextic sieve. This needs checking against Dunn–Radziwiłł's GRH-conditional sharpness of the cubic large sieve. I could not access the full text.
- The Lean route skips Part I, so it is not a line-by-line certificate of Q.
- The Hecke definitions' fidelity rests on library lemmas outside the comparator.
- The PNT+ package is patched with OpenAI code (covered by the axiom check).
- There is no nanoda replay.
- The corollaries are unformalized.
- S was checked by hand: no gap found.

## 7. Extraction friction
- Q is a single 16.7k-line file whose key objects sit in displays and prose.
- There are three manuscripts with two unrelated methods.
- A is not in `lean/docs/003.md`.
- Lean namespaces are opaque, e.g. `SiegelZerosAwei.W63` and `ActualEisensteinCubic`.
- The Lean routes differ from the papers.
- `extract_lean` dominated shares are diluted, with a maximum of 0.15.
- Cited inputs are re-proved in Lean.
