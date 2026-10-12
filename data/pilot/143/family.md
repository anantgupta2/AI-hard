# Family 143: Hilbert's sixteenth problem, uniform bounds for limit cycles

**Analyst:** FAMILY agent, working at text level. Lean was not built here because the checkout is shared, so the comparator compile is pending with the orchestrator. Algebraic identities in 143b were re-checked with sympy.
**Corpus:** openai-math `fd4aeeb`. **Subject:** Dynamical systems and ergodic theory (MSC 34C07).

| | 143a: *Uniform bounds for planar polynomial limit cycles* | 143b: *Two limit cycles for quintic Liénard systems* |
|---|---|---|
| Size | 11.9k TeX lines, 11 sections | 3.2k TeX lines, 7 sections |
| Claim | Finite B(d) for every degree, i.e. the existential Hilbert 16 | Exact maximum 2 for x'=y-F(x), y'=-x with deg F ≤ 5 (LMP conjecture, n=5) |
| Lean | **none** (not in formalization.yaml) | `OAI/Analysis/LienardCycles`: 146 files, 16.7k lines, comparator `OAI.QuinticLienard.main` |
| Method | Complex multi-scale asymptotics (Ilyashenko/Écalle style) + subanalytic preparation + Khovanskii-type projection count | Elementary real ODE comparison: global quadratic fit of half-arc endpoint data, a Schwarzian model inequality, and a sign case split |

The two papers do not cite each other and share no devices.

## Main statements

- **143a, Theorem 1.1** (`01-introduction.tex:12-16`): for each d ≥ 1 there is a finite B(d) such that every real planar polynomial vector field of degree ≤ d has at most B(d) limit cycles in the whole plane.
  - The bound is not effective.
  - Cycles are counted geometrically, with no hyperbolicity or genericity assumption.
  - Individual finiteness (Ilyashenko–Écalle) is not used as a premise.
- **143b, Theorem 1.1** (`introduction.tex:13-17`): if deg F ≤ 5, the classical Liénard system has at most two limit cycles, and two are attained.

**Comparator.** The comparator `QuinticLienard.lean` states:
- (∀F, F.degree ≤ 5 → {C | IsLimitCycle F C}.encard ≤ 2);
- ∧ (∃F, F.degree ≤ 5 ∧ … .encard = 2).

**Match check.** The match is exact.
- The definitions (`vectorField`, `IsSolution` with global HasDerivAt, `IsPeriodicOrbit` nonconstant periodic with range = C, `IsLimitCycle` with an open U ⊇ C in which every periodic orbit equals C) are textually identical to `Model.lean`.
- `Main.lean:20-23` proves the theorem as `⟨upper_bound, Sharpness.sharpness⟩`.
- `definition_names` is empty, as in 388 of 416 comparator JSONs in this release.
- No loophole found.

**Formalized vs claimed.**
- All of 143b is formalized.
- **None of 143a is formalized.** The family headline (Hilbert 16 uniform boundedness) is therefore an unrefereed, unformalized claim. The comparator certifies only the far narrower LMP n=5 case.

## Trust surface (Lean)
Searched all 146 files:
- 0 each of `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque` and `maxHeartbeats`;
- 2 trivial `decide` uses;
- imports: only Mathlib plus sibling files.

The surface is clean at text level. The compile is pending.

## Labels

| Axis | Label | Evidence / note | Conf. |
|---|---|---|---|
| A | **A3** | 143a: a bound, non-explicit (innermost form ∀ fields ≤ B(d)). 143b: sharp exact value; the upper bound is A5-form, the lower bound A2 | 0.8 |
| B | **B1** | 143a: claims the existential part of Hilbert 16 (open since 1900, open even for d=2 per Ilyashenko 2002). 143b: B1 for the degree-5 LMP question (still listed as open by CLZZ, arXiv:2608.19542, Aug 2026); B3 relative to the full LMP conjecture (false for n ≥ 6). Corollary: refutes Hernández Rosales' proposed 4-cycle quintic (it is Odani's Example 3) | 143a 0.3 (conditional); 143b 0.85 |
| C | **C3** primary; secondaries C1, C2, C4, C5 | See below | 0.7 / 0.6 |
| C2 flags | ih_strengthened = yes, by template | 143a's projection count is proved "simultaneously for all systems in the stated closure" (strengthen to all substructures). Its elimination induction carries two quantitative alternatives (an extra tracked quantity) | |
| Computer-assisted | **no** | Polynomial certificates are displayed by hand. Lean has 2 trivial `decide` uses | |
| D | **D3** (provisional) | E1 (Lean-backed) and E3 (informal) are N3 candidates | 0.45 |
| Provenance | no prior model output | 2026 citations are human preprints | |

C in detail:
- **143b:** first-zero barrier contradictions along characteristics plus a Rolle-type count. Sharpness is C1, by a first-order energy displacement.
- **143a:** contradictions on escaping sequences, a Sard/Fubini generic tilt and a non-effective bound. It invokes Lion–Rolin preparation, Bierstone–Milman and Sard as C5.

**E (fields).**
- Problem field: dynamical systems / ODE (34C07).
- Lean dir: Analysis.
- Method fields:
  - 143b: ODE theory (essential, re-proved in Lean); projective differential geometry, i.e. the Schwarzian and Riccati linearization (essential); real polynomial sign certificates (essential); averaging (sharpness only).
  - 143a: complex analysis on nested domains, and asymptotic analysis / resurgence (essential, re-proved for its own class); o-minimality / subanalytic geometry (Lion–Rolin, Bierstone–Milman, Gabrielov: essential, invoked); differential topology (Sard: essential); Khovanskii Pfaffian theory (background, Rolle lemma re-proved); rotated vector fields (essential, re-proved and **not cited**: Duff 1953).

## Proof architecture

**143b (Lean-backed).**
1. Normalize so the x⁵ coefficient is ≥ 0. Put u = x²/2 on each half-plane to get the arc equation du/dy = φ±(u) − y with φ±(u) = F(±√(2u)). This is the classical Filippov transformation.
2. Set up arc data at base height h: half-width r, relative midpoint M, v = M_r. Add characteristics with hyperbolic angles θ = artanh(M/r), L = artanh v, a variation formula, smooth zero-width scaling, and continuation to the non-smooth axis.
3. **Matching.** Periodic orbits correspond to zeros of Δ(r) = M₊(0,r) − M₋(0,r) on a single interval, and isolated orbits to isolated zeros (Prop. 2.5).
4. **Quadratic fit (E1).**
   - H(λ,κ,r) is the midpoint of the quadratic profile λu + κu²/2.
   - Theorem 3.6: (λ,κ,r) ↦ (H, H_r, r) is a diffeomorphism onto {|M| < r, |v| < 1}, with P, Q, R, S, G > 0.
   - Lemma 3.7: the fitted (λ,κ) of any actual profile obey Dκ = −(R/G)(λ − k(h)) and Dλ − κ = (S/G)(λ − k(h)).
5. **Model inequality (E2).** (R/G)_r ≤ 0, from:
   - W = RS_r − SR_r = 16r³/45 + O(r⁴), with a first-zero argument;
   - at a zero of W, the sign of γ_rr − σ₀γ_r comes from the endpoint determinant identity, the Schwarzian of the endpoint correspondence n(m) (via Riccati linearization and a common projective label), and three polynomial-certificate cases.
6. **Shape comparisons (E4).**
   - φ''' > 0 implies κ_r > 0 and λ < k(h).
   - ((φ' − d)/u)' > 0 implies λ − hκ < d.
   - The fitted curvature lies in [min φ'', max φ''].
7. **Quintic split**, with φ± = d₀u + b₀u² ± (e u^{1/2} + c u^{3/2} + a u^{5/2}):
   - case 1 (e, c ≥ 0): no cycles;
   - case 2 (e ≥ 0, c < 0): Δ' = AΔ + Bq with q = κ₊ − κ₋ nondecreasing, so at most 2 cycles;
   - cases 3 and 4: Δ' > 0 at every zero, so at most 1.
8. **Sharpness:** F_ε = ε(4x − 20x³/3 + 8x⁵/5), with Q(s,0) = −πs²(s²−1)(s²−4).

**143a (no Lean).**
1. Logarithmic flags and complex contours along escaping sequences.
2. Packets: trees of lateral expansions on nested bands. The separation theorem gives quasianalyticity without simultaneous convergence.
3. Packet calculus, including the implicit function step; elimination induction; absolute isolated-zero finiteness.
4. Packets verified for additive, one-rate and two-clock passage maps (about 4.4k lines).
5. Lion–Rolin preparation, a box induction and the crossing lemma give finite passage templates (bounded words) for all fields of degree ≤ d. A terminal reduction connects these to the primitives.
6. The projection count (Khovanskii-style) reduces uniformity to absolute finiteness. Matching systems with moving cuts put different hyperbolic cycles on different fiber components.
7. A rotated-field perturbation makes any finite set of cycles hyperbolic; rescaling then gives B(d).

## Lean structure (extractor v3)
**Size.**
- 1352 declarations: 1047 theorems, 280 defs.
- Proof DAG: 1274 declarations, 11.9k lines.
- Core (paper Secs 3–7) = 61% of DAG declarations, about 48% of lines.
- Re-proved ODE flow infrastructure plus arc/matching plumbing = 39% of declarations.

**Key items.**

| Lean item | Location | DAG measure |
|---|---|---|
| `QuadraticCoordinates.H` | `QuadraticCoordinates.lean:20` | 404 dependents, about 52% of the core |
| `model_inequality` / `Cr_nonpos` | | dominated share 16.6% (about 27% of the core) |
| `kappa_width_pos` | | dominated share 22% |
| `matching_isolated_case2` | | dominated share 25% |
| `fitK_spec` | | 10% of the DAG downstream |

**Route.** Lean follows the paper one-to-one. It also builds its own global ODE flow layer, which Mathlib lacks.

## Eureka candidates (provisional)

1. **E1: quadratic-fit coordinates** (Q11+Q19+Q20), 143b, Lean. **N3 candidate (borderline N2), F5.**
   - For: this is the engine of the first proof of degree-5 LMP (open since 1977). It turns the comparison of two non-symmetric half-arcs into monotonicity of the fitted curvature and intercept. H is tiny to state, defined implicitly through ODE solutions, absent from the goal and from L, and about 52% of the Lean core depends on it.
   - Against: strong template in Lagrange's osculating elements / variation of parameters (match value and derivative with a model family, then transport the parameters). Comparison with model equations is standard in Liénard theory (Zhang Zhifen, Coppel, Villari–Zanolin). The paper itself motivates the choice from the common even part.
   - Quick WebSearch: no quadratic-profile fit of half-arc midpoint/width data found, and no prior degree-5 proof.
2. **E2: model inequality (R/G)_r ≤ 0** via the Schwarzian of the endpoint correspondence (Q21–Q26), 143b, Lean. **N2 (upper N3).**
   - For: load-bearing, with 27% of the core dominated.
   - Against: a natural question once E1 exists; textbook tools (OT, Riccati linearization); Schwarzian cycle bounds exist already (Coll–Gasull–Prohens 1996).
3. **E3: packets + separation + absolute isolated-zero finiteness** (U05/U06/U09/U12), 143a, no Lean. **N3 candidate, informal list only; correctness unverified.**
   - For: if correct, it supplies the multivariable quasianalytic finiteness that was missing. Galal–Kaiser–Speissegger 2020 is one-variable only, and Yeung 2025 found a closure gap in Ilyashenko 1991.
   - Against: precedents in Ilyashenko superexact series, Écalle analysable functions and Ilyashenko algebras. The text is unauditable at this depth.
4. **E4: general shape comparisons** (Q28, Q29). **N2.** The hypotheses are classical Liénard shape conditions, such as Zhang Zhifen's monotone ratio.
5. **E5: moving-cut matching systems + projection count** (U19–U21). **N2.** Named precedents: Ilyashenko–Yakovenko cyclic systems and Khovanskii/Gabrielov.

Classed N0/N1 (not candidates):
- the Filippov transformation;
- arc coordinates and the matching proposition;
- the Rolle-type zero count;
- sharpness by averaging;
- Lion–Rolin preparation;
- the crossing lemma (Khovanskii);
- the projection count as a technique;
- the rotation lemma (Duff).

## Correctness audit
**143b.** Read in full; the algebra checks out.

These identities were verified with sympy:
- the p''', p'' and up''−p' formulas;
- J(0,1+ξ) = ξ²+4ξ+1 and J(1,1+ξ) = 2ξ(ξ+2)(ξ²+ξ+1);
- A > 0;
- the AT and Δ₀ factorizations;
- both numerator reductions and A₀ + βA_β;
- W ~ 16r³/45;
- J⁻¹b = (−1/35, 2/7);
- Q(s,0), with Q_s(1,0) = 6π and Q_s(2,0) = −48π;
- the Rosales roots X² = (5±√15)/2.

Consistency checks:
- The odd case reduces to Rychkov.
- The quartic case is consistent with Li–Llibre: case 2 with a=0 gives ≤ 2, weaker than their bound but not contradictory.
- The sharpness example lies in case 2, the only case that allows 2 cycles.

The trust rests on the Lean compile, which is pending.

**143a.** This is an extraordinary claim with no formalization and no external confirmation found. A 2026 arXiv paper still calls uniform boundedness open even for n=2.

Main risks:
- **The absolute zero property.** It asserts finiteness of isolated solutions when coefficients, cut positions, multipliers and jets are all unknowns. That amounts to multiparameter quasianalytic/o-minimal finiteness for Dulac-type passages at arbitrary degenerations. The quantifier management "per finite request" in Secs 3–8 is where errors would hide.
- **The desingularization substitute.** Can one-variable preparation plus a jet-order box induction really reduce *every* degenerate configuration (non-elementary graphics, behaviour near infinity) to the three passage models?

Not a risk: Sec. 11 (projection count, matching, rotation, final assembly) reads as sound given its hypotheses.

## Extraction friction
- Two manuscripts with completely different methods; only 143b has Lean.
- 143a's technical lemmas are grouped (60 items total: Q01–Q36, U01–U24).
- The extractor ranks plumbing highest (`IsArch`, `GlobalODE.flow`), so dominated share and a section mapping were used instead.
- Lean names are descriptive, so the paper–Lean join is easy.
- There is no reasoning trace.
