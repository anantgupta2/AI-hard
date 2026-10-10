# Family 002: the full Birch–Swinnerton-Dyer formula in Selmer coranks zero and one

Family analyst report (paper only), influential-problems pass, 2026-10-10. Release `openai/math` at commit `fd4aeeb`. Machine-readable version: `family.json` (269 items).

> **Shortlist status.** The family has **no Lean formalization**: no Lean dirs, no comparators, no `lean/docs/002.md`. The downstream speedup test is Lean-only (PLAN.md, 2026-10-09), so the family is **excluded from the Lean eureka shortlist**. The reason is the missing Lean, not the merit of the work. Any N3 items go on the informal list `data/eureka_informal.json` (PLAN.md, 2026-10-10).

## 1. The three manuscripts and how they fit together

| id | Manuscript | Lines | Role |
|---|---|---|---|
| M1 | *Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank* (Oct 7; Oct 3 edition kept) | 7,190 | Headline. Proves the exact p-adic valuation of the leading-term formula at every **odd** prime, then assembles. |
| M2 | *The Selmer converse for elliptic curves at every prime* (Oct 7; Sep 24 edition kept) | 5,918 | Shows that s_p ∈ {0,1} ⇒ a(E) = rank = s_p and Ш finite, for every p. Corollary: Sylvester cube sums for primes ℓ ≡ 4, 7, 8 mod 9. |
| M3 | *The two-primary BSD formula in Selmer corank at most one* (Oct 6; Sep 24 edition kept) | 9,051 | The 2-part, v₂(Q_E) = v₂(#Ш), plus an independent proof of the 2-converse. |

**Dependency graph.**
- 006 → M2 (the case p = 2 and the auxiliary fields).
- 006 → M1 (auxiliary fields).
- M2 → M1 (rank and finiteness; theta and extraction lemmas cited by number).
- M3 → M1 (the 2-part, positivity and rationality).
- M2 → M3 (Cor 1.2 only).
- Smith 2025 → 006.

**No circularity found.**
- 006 mentions M2 and M3 only in its introduction, as subsequent companions.
- M3 proves its 2-converse from Gross–Zagier–Kolyvagin (GZK) alone (15-conclusion.tex:29-79).

**Link to family 006 (Goldfeld).** 006 supplies three things:
1. The 2-converse, which M2 uses at p = 2.
2. The analytic twist-density theorem (twists of rank 0 and of rank 1 each have density 1/2). M1 and M2 use it to choose the auxiliary imaginary quadratic fields K and L = Q(√D, √D').
3. Through Smith's 2^∞-Selmer distribution, s₂(E^d) ∈ {0,1} for a density-one set of signed squarefree d.

Together with M1, item 3 gives **full BSD for a density-one set of quadratic twists of every E/Q**, with rank 0 and rank 1 each of density 1/2. Each link is essential, and every link is an unreviewed model-produced manuscript.

## 2. Main statement

> **Theorem (M1 01-introduction.tex:47-62).** Let E/Q be an elliptic curve and q any prime. If s_q(E) ∈ {0,1}, then r(E) = a(E) = s_q(E), #Ш(E/Q) < ∞, and L^{(r)}(E,1)/r! = Ω_E Reg_E #Ш ∏c_ℓ / #E(Q)_tors². This holds with no hypotheses on reduction, torsion, isogenies, CM or the residual representation.

Here Ω_E is the period over all of E(ℝ), and Reg_E is computed on the full Mordell–Weil lattice with H = 2× the canonical height for [O].

**A stronger statement is implicit.** M1 Prop `center:odd-valuations` (10:231-237) proves v_p(Q_E) = v_p(#Ш) for **every E of analytic rank ≤ 1** and every odd p. M3 gives the 2-part whenever s₂ ≤ 1, which follows from a(E) ≤ 1 by GZK. So the family claims **full BSD for every E/Q of analytic rank ≤ 1**. The Selmer-corank phrasing only adds the converse direction from M2.

## 3. Which primes were previously open, and how they are handled

This section is based on the cited literature and on search snippets; we did not read the cited papers.

**What was known before, at analytic rank ≤ 1.** The p-part of BSD was known only under hypotheses:
- **Rank 0:** Skinner–Urban: p ≥ 3, good ordinary, E[p] irreducible, plus a ramification hypothesis.
- **Rank 1:**
  - Zhang 2014 and Jetchev–Skinner–Wan (JSW) 2017: p ≥ 5 or p ≥ 3; semistable; good ordinary or supersingular; irreducibility.
  - Castella–Grossi–Lee–Skinner (CGLS) 2022: odd good ordinary Eisenstein primes.
  - Keller–Yin 2024: Eisenstein primes, multiplicative and potentially good ordinary reduction.
  - Burungale–Castella–Skinner (BCS) 2025: p > 3 good ordinary, irreducible, ramification hypothesis removed.
  - Castella 2024: multiplicative reduction.
  - Burungale–Skinner–Tian–Wan (BSTW) 2024: semistable supersingular primes.
- **CM curves:** Rubin and Burungale–Flach (rank 0, all p); Li–Tian–Yan–Zhu (LTYZ) 2025 (rank 1, p = 2, good ordinary).
- **The prime 2:** only twist families (Zhao; Coates–Li–Tian–Zhai 2015; Cai–Li–Zhai 2020; Shu–Zhai 2021; Kriz–Li 2019).

Full BSD was known only for individual curves (Miller: 16,714 of 16,725 curves of conductor < 5000 [snippet]) and for explicit families (BSTW; Banwait–Huang 2026 [snippet]). Bhargava–Skinner–Zhang (BSZ) prove only the *rank* part, for ≥ 66.48% of curves.

| Previously open case | How the family handles it |
|---|---|
| **p = 2**, non-CM in general | M3 splits by the image of E[2]: reducible (2-descent graph seeds), imaginary S₃ (conjugate Bockstein alternation), real S₃ (**real-component detector Θ** with a Pfaffian cofactor lift), cyclic cubic (ray units). CM curves are treated directly. Kato classes and BDP-type disk measures are worked out integrally at 2. |
| **p = 3**, including the additive cube-sum curves | M1 and M2 run one uniform argument for all odd p; M2 Sec 10 applies it at the additive prime 3. |
| **Additive p**, including potentially supersingular | The deformation variable t is a ring-class character at moving primes q_i, unramified at p. The local condition at p is therefore just the Kummer line of V⊗R_b, with no ordinarity or p-adic Hodge input on E. BDP measures use the ordinary locus of the *modular curve* (p splits in K), "not ordinary reduction of A₀" (M2 01:210). |
| **Residually reducible or non-surjective p**, without ramification hypotheses | "Residual concentration" (M1 `vertical:tests`) adjoins tame variables, chosen by Heisenberg-commutator Frobenius addressing (EC1), until the determinants are nonzero mod (p, t). This replaces residual-irreducibility hypotheses. |
| **p dividing c_E or a Tamagawa number** | c_E, every c_ℓ, τ_p and the torsion are kept exactly in the central volume (M1 10:34-141). |
| **CM curves of rank 1, odd p** | The pair identity X(E) + X(E^D) = 0, with Burungale–Flach for the CM rank-0 twist. |

## 4. Labels

- **A1** (universal implication), secondary "exact formula" (A3-like). Medium confidence.
- **B3**, partial: the corank/analytic-rank ≤ 1 case of BSD. Secondary **B4**, since it extends all the earlier p-part results. Flags:
  - *full only with prior results*: yes. Needs M2, M3, 006, GZ, Kolyvagin, Kato, modularity and Burungale–Flach.
  - *adds corollaries*: yes. Sylvester cube sums; density-one twists with full BSD (with 006); full BSD in analytic rank ≤ 1; the p-converse at every p; Perrin-Riou's log² formula at every p.
- **C4** primary: two-sided integral determinant comparisons, i.e. X ≥ 0 and X(E) + X(E^D) = 0. Secondaries:
  - C3: M2 argues by contradiction, with incompatible Greenberg lengths.
  - C5: massive use of cited theorems.
  - C1: theta families and Kato classes are constructed.

  Not computer-assisted. ih_strengthened = no.
- **D3 (provisional, 0.3)**: rests on EC1 and EC3; final grade in `novelty.json`. Flag *builds on prior model-produced result*: **yes**, through release-sibling 006 and the companion manuscripts.
- **E**:
  - Problem field: number theory (MSC 11G40, 11G05, 11R23, 11F67, 11G15). Lean dir: none.
  - Essential method fields (13 in all): Selmer complexes and Iwasawa theory; Euler systems; arithmetic of modular curves; CM theory and BDP p-adic L-functions; the theta correspondence on U(3,1); PEL Shimura varieties (Lan); Labesse base change and Galois representations for RACSDC; generalized matrix algebras; p-adic Lie groups; analytic NT (twist densities); commutative algebra; **ultrafilters**; homological perturbation; real components of modular curves (M3 only); 2-descent combinatorics (M3 only); arithmetic duality and parity.
  - Background-cited only: the weighted fundamental lemma (M2 appendix, unused).

## 5. Proof architecture

1. **Assembly** (M1 10:254-270). M2 gives a = r = s_q and Ш finite. Hence s_p = r for every p. M3 gives Q_E ∈ ℚ_{>0} and the correct v₂. M1 gives every odd v_p. A positive rational number with all valuations 0 equals 1.
2. **M2 reduction.**
   - p = 2 comes from 006.
   - For odd p, the density theorem selects D and D' such that H¹_f(K, V) is a line and the auxiliary line comes from a nontorsion point.
   - It then suffices to show the conductor-one Heegner trace y is nontorsion. Assume it is torsion.
3. **M2 upper bound.**
   - Moving split primes q_i carry ring-class characters of order p^{n_i}. A nonprincipal ultrafilter gives the limit ℓ, ψ = (1+t)^ℓ, and *admissible cochains* over R_b = k[t]/t^b.
   - Outside the strict case the Greenberg group vanishes.
   - In the strict case (the Selmer line is everywhere locally zero), a **Heisenberg commutator** modifies the limiting Frobenius γ so that the first-order obstruction matrix is [[0, κ], [−κ, 0]] with κ ≠ 0. Then length ≤ 2 < b* = 3.
4. **M2 analytic side.**
   - A torsion y makes the weighted Heegner logarithms vanish to order b*.
   - A holomorphic theta family on U(3,1) has constant terms tied to toric periods (a square identity, BDP), and a bounded positive Fourier–Jacobi coefficient.
   - It lifts to cusp forms mod p^{M_i} over (O/p^M)[t]/t^{b*} on the ordinary locus of the PEL variety.
5. **M2 Galois side.** Labesse transfer to GL₄; BGHT Galois representations; Hodge–Newton flags; uniform nilpotent control; generalized-matrix-algebra (GMA) corner modules. The Fitting ideal gives length ≥ b*. This is a contradiction, so y is nontorsion, and GZK finishes.
6. **M3 (p = 2).**
   - *Positive comparison* X ≥ 0: integral Kato classes at 2, and a tame-height route to the rank-one log² formula.
   - *Split-pair anchor* X(A^h) + X(A^{hk}) = 0, by the four residual-image branches.
   - *CM comparison.*
   - The sandwich gives X = 0 for a positive twist, which then transfers back to E.
7. **M1 odd p.**
   - **Secs 3–4:** integral finite models over R = Z_p[[t, u]], then residual concentration.
   - **Sec 5:** X(E) ≥ 0 for non-CM E. Integral Kato classes; the period law in rank 0; Perrin-Riou's formula via tame heights in rank 1.
   - **Sec 6:** U_w = B_w/L_w is integral and prime to p. Uses BDP measures, divisibility at high characters, and Chai–Hida primitivity.
   - **Secs 7–8:** the theta implication. If the undepleted CM series vanishes on a horizontal divisor, there is a one-sided strict jump.
   - **Sec 9:** U_w is a unit. Adjoining tame directions makes simultaneous jumps codimension ≥ 2.
   - **Sec 10:** the exact central volume gives X(E) + X(E^D) = 0, so X(E) = 0. Burungale–Flach handles CM rank 0.

## 6. Items (summary; full list in JSON)

There are 269 items:
- 259 environments: M1 73, M2 52, M3 134;
- 10 inline definitions: the tame variables u_j; ψ = (1+t)^ℓ and M_b; U_w; the strict case; b*; "jump"; "necessary lift matrix"; square/rectangular order; 2-descent labels.

Provisional grade counts: N0 24, N1 158, N2 79, N3 candidate 5, ungraded (goal statements) 3.

Most items fall into four kinds:
- cited inputs (N0);
- integral re-derivations of known constructions (N1): Kato, BDP, Gross–Zagier normalizations, finite/singular switches, Weierstrass division;
- variants of the Skinner–Urban / Castella–Liu–Wan / Ribet–Wiles machinery on U(3,1) (N2);
- the tame-direction cluster.

**Plumbing and N0/N1 examples:**
- `models:finite-models` is the homological perturbation lemma plus ultrafilter limits.
- `real:weighted-pfaffian` is Pf(DBD) = det D · Pf B.
- `unit:augmented-alternating` and `unit:tangent-minors` are elementary determinantal algebra.
- The M2 appendix on the weighted fundamental lemma is not used by any proof.

## 7. Eureka candidates (provisional)

| # | Candidate | Where | Prov. N | F |
|---|---|---|---|---|
| EC1 | **Heisenberg-commutator Frobenius addressing.** The first-order obstruction H_γ(x, d) = u(γ) − e((V(γ)−1)⁻¹x(γ), d(γ)) − (conjugate), where u is a primitive of x∪d. Multiplying γ by a commutator [g, g'] in ker(G → GL V) shifts u by an alternating form and changes nothing else. This makes the obstruction nondegenerate (M2), spanning (M1), or makes a tame height nonzero (M1, M3). | M2 03:414-610; M1 04:336-442, 09:330-345; M3 06:155-238 | N3 cand. (borderline N2) | F3 |
| EC3 | **Real-component detector Θ at 2.** Each real circle of X₀(n) under w_n∘c gets the weight ψ(a) + ψ(a)⁻¹, where a is the ideal class of the anti-linear isogeny S (S² = n). The resulting functional is a Hecke eigenfunctional and is nonzero on the Heegner trace. | M3 13:138-265, 1053-1101 | N3 cand. (low conf.) | F3 |
| EC4 | **Codimension-two divisor removal.** Adjoining new tame variables makes simultaneous one-sided jumps codimension ≥ 2. So the integral quotient has no height-one divisor, i.e. it is a unit. | M1 09:136-439 | N2 (N3 if no neighbour) | F5 |
| EC2 | **Ultralimit tame deformation variables and admissible cochains.** These give a deformation variable unramified at p. | M2 03:240-330; M1 03:47-129 | N2 | — |
| EC5 | **Tame-height route to Perrin-Riou's log² formula**, at every p and for all reduction types. | M1 05:740-1000; M3 06 | N2 | — |

Quick nearest-neighbour checks (search snippets only):
- **EC2** is close to Sweeting's ultrapatching (arXiv 2012.11771) and to Loeffler–Zerbes's ultra-Kolyvagin systems (arXiv 2511.08793, Nov 2025). The latter uses nonprincipal ultrafilters on auxiliary primes precisely to avoid ordinarity.
- **EC1**'s ingredients are classical: Mazur–Tate / Bertolini–Darmon derived heights, Massey-product Heisenberg extensions, and Ramakrishna- or Kolyvagin-style auxiliary primes. No source was found that uses a commutator-shifted Frobenius to control tame obstructions of Selmer classes.
- **EC3**'s nearest neighbours are Ogg's real loci of X₀⁺(N) and Snowden's *Real components of modular curves*. No class-group-weighted Hecke eigenfunctional was found.

## 8. Correctness and trust

- **No Lean, no code, no trace.** About 22k lines of unrefereed and extremely compressed LaTeX, plus essential dependence on 006 (two more unreviewed model-produced manuscripts) and on Smith 2025.
- **The ultralimit framework** (EC2) is unconventional:
  - cohomology lives on "sequences of Galois elements" modulo an ultrafilter;
  - the uniform bound on residual cohomology with growing ramification at the moving primes is justified in two sentences (M1 03:121-129).

  An expert needs to check this.
- **Deep steps are sketched in a few paragraphs:** cusp lifting on the U(3,1) PEL compactification, Hodge–Newton contacts, uniform nilpotent control, and the theta moment bounds. M1 Secs 7–8 cite M2 lemma by lemma.
- **Read and found coherent:** the M1 assembly, the discrepancy identity, the exact center and the unit argument; M2's Poitou–Tate case split, Heisenberg identity and length bound; M3's Pfaffian identity and detector proof outline. **Not verified:** the theta, automorphic and Galois sections (statement-level only).
- **Editing artefacts:**
  - The M2 appendix (weighted fundamental lemma for nonstandard groups, citing an undated author draft) is never used.
  - M1's Oct-3 edition cited `\cite{Dv}` with no bibitem. history.md says it pointed to a "removed supporting manuscript", whose content is unknown.
  - M1 equation labels were renamed `eq:source-N`.
- **The 2-converse is proved twice**, in 006 and in M3. This gives some redundancy, but both proofs are unreviewed.
- **Extraordinary scope.** If correct, the family subsumes all the earlier p-part results in analytic rank ≤ 1 and proves full BSD for every E/Q of analytic rank ≤ 1. Treat it as unverified.

## 9. Extraction friction

- Core devices live in prose and inside proofs: u_j, ψ, U_w and the commutator step have no environments.
- Lemma names repeat across M1 and M3 with different proofs.
- Cross-paper citations point to lemma numbers in the companion PDFs.
- `uses_items` is only approximate (computed by regex over `\ref`).
- WebFetch of arxiv.org failed (DNS), so every literature claim rests on WebSearch summaries.
