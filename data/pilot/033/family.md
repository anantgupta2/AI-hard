# Family 033: Iitaka subadditivity, variation, and logarithmic additivity

Family analyst report (paper + Lean, text level). Corpus `openai/math` @ `fd4aeeb`. The structured version, with 68 items, is `family.json`.

**Lean was not built.** By orchestrator instruction this agent ran no `lake build`, `lake env` or `comparator`. The extractor v3 was run (`data/items/033_lean.json`).

## 1. The five manuscripts

| id | Title | Date | Lines | Lean | Headline claim |
|---|---|---|---|---|---|
| REV | The reverse logarithmic Kodaira inequality and additivity | Sep 26 | 4.8k | **yes (one trivial branch)** | κ(X,K+E) ≤ κ(Y,K+D)+κ(F,K+E_F) for stratum-smooth reduced-SNC fibrations. With ORB this gives Popa's log additivity |
| ORB | Orbifold and logarithmic Iitaka subadditivity | Sep 26 | 5.7k | no | Campana's orbifold Iitaka conjecture (class C, rational SNC, coefficient 1 allowed). Hence log subadditivity and C_{n,m} |
| VAR | Logarithmic Kodaira dimension and whole-fiber variation | Sep 26 | 7.1k | no | κ̄(U) ≥ κ(F)+max{κ̄(V), Var(f)}. This is Popa's Conj. 3.8, and Viehweg's C⁺_{n,m} follows |
| ORD | Projective Hodge lines and ordinary Iitaka subadditivity | Sep 27 | 3.7k | no | Iitaka C_{n,m} over any algebraically closed field of characteristic 0, via "projective adjoint positivity" |
| BSA | B-semiampleness for compact log-smooth Kähler fibrations | Sep 10 | 3.3k | no | Kähler b-semiampleness for effective SNC boundaries with coefficients in [0,1] (extends BFMT25's algebraic theorem) |

If correct, these claims settle several famous open problems at once: Iitaka's C_{n,m}, Viehweg's C⁺_{n,m}, Campana's orbifold conjecture and Popa's conjectures. They are unreviewed model output, and the papers cite one another.

## 2. Main statement and the Lean comparator

**Paper (REV Thm 1.1, `introduction.tex:30-37`).** Setup:
- f:(X,E)→(Y,D) is surjective with connected fibres, between smooth projective reduced-SNC pairs over ℂ.
- Supp f\*D ⊆ Supp E.
- X and all boundary strata are smooth over V = Y∖D.

Then κ(X,L_X) ≤ κ(Y,L_Y)+κ(F,L_F). If either term on the right is −∞, every H⁰(X,mL_X) vanishes. Corollary 1.2 (additivity) adds ORB's Cor 6.2.

**Comparator** `LogKodairaFiberNegative`, target `OAI.ReverseLogKodaira.SmoothProjectiveVariety.veryGenerally_fiber_negative_branch`. Permitted axioms are propext, Quot.sound and Classical.choice. The statement says: very generally in y, if a fibre model has log Kodaira dimension ⊥, then E.kodaira = D.kodaira + ⊥ and every positive-degree log pluriform on X is 0.

**Match check.** The comparator matches the paper's *negative-fiber branch only* (`reduction.tex:60-66`). That branch is a five-line restriction-plus-adjunction argument. The definitions are faithful:
- `kodaira` is the supremum of k for which some nonzero section has k algebraically independent ratios. This equals the Iitaka dimension.
- Log pluriforms are tested on principal affine opens, which cover X because `union_cartier` holds.
- `StratumSmoothFibration` encodes every hypothesis.

One minor weakening: the comparator has no `Nonempty FiberModel` clause.

**Not formalized:**
- the finite inequality;
- the negative-*base* vanishing, which is the real content: a log Popa–Schnell base-nonvanishing statement;
- all of the Hodge theory;
- the other four manuscripts.

The full statements exist only as `Prop` definitions (`Basic.lean:423-454`, `Descent.lean:52`). `lean/docs/033.md` itself states that the finite and negative-base branches are out of scope. A successful compile therefore lends **no** support to the big claims.

**Trust surface.** 17 files, 4,604 lines. No `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `partial` or heartbeat options. There is one `decide` on a numeral (`Basic.lean:187`, off the DAG).

**Lean shape.** 254 declarations: 157 theorems, 66 defs, 13 instances, 11 abbrevs, 7 structures. The target DAG has 142 declarations. One lemma, `exists_open_nonzero_fiber_pluriform` (`NonzeroFiber.lean:449`), dominates 77% of it: a nonzero log pluriform stays nonzero on fibres over a Zariski open set. The rest is plumbing that Mathlib lacks: Kähler differentials of function fields, standard-smooth charts, determinant adjunction.

The 112 declarations outside the DAG include `RootFactor.lean`, `Descent.lean` and `Blowup.lean`. They formalize the algebraic core of REV's **zero test** (Lemma 3.3): roots in integrally closed domains, and divisibility in blow-up charts. The comparator does not use them.

## 3. Labels

| Axis | Label | Evidence / note |
|---|---|---|
| A | **A1** universal inequality | ORB `introduction.tex:141-145`. The comparator is also A1 |
| B | **B1** (confirms fully; per-paper: REV comparator B3, BSA B4) | ORB `introduction.tex:148-151` "positive resolution of Campana's orbifold Iitaka conjecture". Flags: *full only with prior* = yes (REV and VAR need ORB). *Adds corollaries*: C_{n,m}, C⁺_{n,m}, log subadditivity, core decomposition, log Popa–Schnell nonvanishing, birational isotriviality |
| C | **C5** primary; C3, C1, C4 secondary | ORD `01-introduction.tex:219-222`: reduction to the log-general-type addition theorem (Kovács–Patakfalvi/Hashizume), plus Viehweg-type weak positivity and one new Hodge input. Not computer-assisted. No induction (ih_strengthened = no) |
| D | **D3 (provisional)** | Max item: the adjoint-positivity device (§5, C1). Flag *builds on prior model-produced result* = **yes**. REV and VAR use ORB, and VAR Cor 1.3 uses the OpenAI "Log abundance in characteristic zero" preprint |
| E | Problem: algebraic geometry (14E30, 14D07, 14J10). Lean dir: AlgebraicGeometry. Method fields: see below | 5 cross-field method fields; roughly 25% of invoked theorems come from other fields |

Method fields (E):
- **Essential:** Hodge theory/VHS; birational geometry/MMP; o-minimality (BBT, Ax–Schanuel); algebraic groups and Lie theory (André normality, adjoint groups, flags); SCV/Kähler geometry; L² and pluripotential methods (VAR only); Galois/étale descent (VAR); commutative algebra (zero test); toroidal semistable reduction.
- **Background:** an algebraic-integer argument for unipotent level.

## 4. Proof architecture (ORD, the cleanest route to C_{n,m})

1. **Reduction.** Take a relative Iitaka fibration X̃→Y→Z with Kodaira-zero generic fibre. The canonical bundle formula gives K ~ g\*(K_Y+B+M)+R, with B klt and M nef (Fujino–Mori, Ambro).
2. **Hodge realization.** The least-index root cover has p_g = 1, so M is the *entire* highest Hodge line of a rational VHS.
3. **New input: projective adjoint positivity.** After modification, M = p\*L with p:Y→S, L nef and K_S + jL big. Three ingredients prove it:
   - S is the full-period image, giving log general type by Brunebarbe–Cadorel at a neat level.
   - A rationally minimal subvariation (BFMT transcendental part) plus a tangential rank principle shows that the line strictly loses numerical dimension on every boundary divisor with N ≠ 0 and on every divisor fixed by finite inertia.
   - Volume counting then removes the boundary and the ramification.
4. **Nonvanishing on period fibres.** A generic p-fibre has κ ≥ 0, using the product map Y→S×Z and KP addition.
5. **Weak positivity.** K_Y+B+jM−p\*H is effective (Fujino).
6. **Interpolation.** D = λE₁+(1−λ)E₂ with λ = (1−v)/(j−v). E₂ is klt log canonical and big on q-fibres, so Hashizume/KP gives κ ≥ d+κ(Z).

ORB runs the same scheme with a complex character summand and a real polarization, in class C, using Ax–Schanuel for the rank loss. REV runs a variant: the chosen vector need not span the highest space, so it adds "marks" on compact flag factors and a Higgs-tail line, then removes the period twist numerically. VAR adds an analytic constancy criterion and a Galois-descent step to bound Var(f). BSA transfers BFMT25 to Kähler manifolds via product covers (MWWWZ) on an auxiliary compact base.

## 5. Eureka candidates (provisional)

| # | Item | N | F | Nearest neighbour |
|---|---|---|---|---|
| 1 | **Adjoint positivity of the highest Hodge line on the full-period quotient**: K_S + jL big with M = p\*L at the original level, via strict rank loss on boundary and ramification divisors (ORB Thm 3.1 + Lemma "strict loss"; ORD Thm 1.2 + Thm 4.1; REV Props 5.3, 5.5) | **N3 candidate** | F3 (F5 flavour) | Brunebarbe–Cadorel 2017; BBT; GGLR augmented Hodge bundle; BFMT 2025 (CY-VHS Hodge bundle semiample "under extra conditions"); Ambro 2005 (b-nef and abundant only after a generically finite base change) |
| 2 | Adjoint-addition interpolation D+M = (1−θ)E₊+θE₋ | N2 | – | Viehweg addition over a general-type base; Campana Orbifolds Prop 6.6 (cited) |
| 3 | Analytic birational constancy criterion: a flat top Hodge line forces birational constancy of Kodaira-zero families (L^{2/m} minimization, pole control) | N2 (maybe N3) | F3 | Ambro 2005 (numerically trivial moduli part); Viehweg–Zuo; Păun–Takayama |
| 4 | Marked periods, Higgs-tail line and period-twist removal (REV) | N2 | – | Viehweg–Zuo, Popa–Schnell, Campana–Păun |
| 5 | Section construction with zero retained in the original frame (REV Prop 1.3 + Lemma 3.3). The only piece with Lean (off-target) | N2 | – | Popa–Schnell Thms C, H |

**Arguments for candidate 1:**
- It is the single missing input that turns the classical reduction into C_{n,m}. Birkar identifies the κ(F) = 0 case as the obstruction.
- L does not contain the statement.
- It is reused across four of the five manuscripts, which counts as device reuse across the model's own manuscripts.

**Arguments against candidate 1:**
- Every component is named prior art.
- BFMT25's Hodge-theoretic semiampleness might subsume it if its "extra conditions" cover root-cover VHS. The family never discusses this.
- **It has no Lean declarations**, so it can enter only the informal list (`data/eureka_informal.json`), not the Lean shortlist.

**Literature check (WebSearch, 2026-10-12, snippets only; arxiv.org is unreachable from the sandbox):**
- No prior adjoint statement was found.
- BFMT 2508.19215 abstract: the Griffiths bundle is semiample on period images, and the CY Hodge bundle is semiample under extra conditions.
- A May 2026 preprint (arXiv 2605.08598) still treats C_{n,3} only partially. So C_{n,m} was open before the release.

## 6. Correctness concerns

**Checked by hand:**
- ORD §7 line by line: the interpolation identities, the period-fibre lemma and the effectivity lemma.
- ORB §3, including the coefficient identities.
- REV §2 in all sign cases, plus REV Prop 7.2 and Lemma 7.3.
- REV §3 read in full; its zero-test algebra matches the Lean.
- Elliptic modular curve sanity check: deg λ = 1/12, so K + jλ is big for j > 24.
- The companion locator "Cor 6.2" is correct.

**Concerns:**
1. **Single point of failure.** Everything rests on the boundary rank-loss / adjoint-positivity theorem. It is about 1,000 dense lines using Ax–Schanuel, André normality and limits at nilpotent and finite-inertia degenerations. I read it only at statement and sketch level and could not verify it. The papers offer three proofs, but all follow the same strategy.
2. **Possible BFMT overlap.** If adjoint positivity were this accessible, BFMT's machinery might already give C_{n,m}. The papers avoid BFMT Thm 1.5 because it needs an effective generic boundary, but they never address BFMT's purely Hodge-theoretic results. An expert check is needed.
3. **Class-C scope in ORB.** Lemma 3.3 (`adjoint-addition.tex:68-138`) applies Fujino's weak positivity, which is stated for projective morphisms, to a Kähler source. The projective corollaries are unaffected.
4. **Propagation through companions.** REV's additivity and VAR's main theorem both depend on ORB. VAR also leans on the OpenAI log-abundance preprint for one corollary. An error would propagate to four manuscripts and to other families (e.g. 034).
5. **History of failed claims.** Earlier claims of C_{n,m} (Tsuji 2010, Maehara 2009) were never accepted. Both are cited here as non-inputs.
6. **Lean gives no support.** It certifies only the trivial branch.

## 7. Extraction friction
- About 19k TeX lines across five papers. Label prefixes vary by paper, and the label `period:adjoint` is reused in ORB and VAR for different statements.
- ORB's `root-comparison.tex` starts with `\subsection`, which shifts theorem numbering relative to the file split. REV's companion locators go through a macro.
- 40% of the Lean declarations lie outside the target DAG. DAG shares are therefore uninformative about the papers' devices.
- There is no reasoning trace for this family.
