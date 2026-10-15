# Lean scope check (67 families whose Lean statement differs from the headline)

**category:** companion_full 40 · headline_partial_disclosed 14 · headline_lemma_disclosed 9 · partial_undisclosed 3 · label_error 1

**disclosure:** explicit 37 · implicit 29 · overstated 1

**lean_vs_ms_main:** full 41 · partial 19 · lemma 7

**our_label_check:** confirmed 61 · weaker 3 · different 2 · should_be_same 1

**ms_is_headline:** False 45 · True 22

**yaml_listed_but_partial:** False 60 · True 7

## Flagged

- **027** headline_lemma_disclosed · disclosure explicit · label confirmed · yaml lists it as formalized: Lean proves only seam-equation compatibility of the produced marked solution; potential integral density, prescribed boundary classes and all-component conclusion absent.
- **066** headline_lemma_disclosed · disclosure explicit · label confirmed · yaml lists it as formalized: Lean is only a compactness lemma for chart-field retractions; neither uniform Cartier sections nor bounded klt complements with index N(d,eps) are stated.
- **157** label_error · disclosure explicit · label should_be_same: Lean has alpha<=2 and h<26m/75+2/3<m/2<=chi; chi_f>=m/alpha>=m/2 is a one-line LP step, so Lean implies headline (plus cm<m/100).
- **184** companion_full · disclosure implicit · label weaker: Lean lacks the O_F(Δ/logΔ) correspondence-coloring bound; the AEKS bound follows from it via max-degree deletion, so Lean is implied (weaker, not different).
- **195** headline_partial_disclosed · disclosure explicit · label weaker · yaml lists it as formalized: Lean only asserts such a ring exists (trivially, e.g. C[[x,y,z]]); absence of nonzero f.g. MCM modules is missing. Implied by headline, so weaker.
- **212** headline_partial_disclosed · disclosure explicit · label confirmed · yaml lists it as formalized: Companion limit-shape paper, differentiability only (no strict convexity); headline no-bigeodesics theorem not formalized at all.
- **227** headline_partial_disclosed · disclosure explicit · label different: Lean has discrete ratio cutoff only for beta<1/2, with no location or continuous time. Its spectral-gap and beta>=1 comparators are not implied by the headline.
- **230** partial_undisclosed · disclosure implicit · label confirmed: Only positivity (lower half) of H^h on segments; finiteness of H^h(gamma[s,t]) and finite expected measure in disks are missing, unflagged.
- **237** companion_full · disclosure explicit · label confirmed · yaml lists it as formalized: Only strip-crossing main theorem is full; others summability/free-energy/B_h lemmas (yaml-listed Chords paper only a lemma). Fixed-length SAW diameter n^{3/4} absent.
- **238** partial_undisclosed · disclosure overstated · label confirmed: Only explicit constants missing: ThorpRemaining states t_mix=Θ(log N) and 2048d/32800d convergence, but not 1600d or the 2d−O(1) lower bound.
- **261** headline_partial_disclosed · disclosure explicit · label weaker: Lean proves only the a.s. spectrum [-4-h,4+h], a conjunct of main theorem and our headline, so implied (weaker); pure-point type absent.
- **266** companion_full · disclosure explicit · label different: Lean has N(6)<=5 plus Fourier vanishing, which N(6)=3 does not imply, so the label is different. The bound of three is missing.
- **277** partial_undisclosed · disclosure implicit · label confirmed · yaml lists it as formalized: Lean rate exponent is δ^13, the paper's universal rate is δ^5; the note states δ^13 without saying it is weaker than the paper's.
- **301** headline_lemma_disclosed · disclosure explicit · label confirmed · yaml lists it as formalized: Lean proves only ideal-lattice transport and idempotent-trace description under a trace-cone equivalence; the classification A⊗W⊗K ≅ B⊗W⊗K absent.

## All

| fid | category | Lean vs its paper | disclosure | gap |
|---|---|---|---|---|
| 009 | headline_partial_disclosed | partial | explicit | Companion Galois-data paper, injectivity half only; headline is mod-ell Milnor K-theory bijection (existence/surjectivity and K-theory setting absent). |
| 027 | headline_lemma_disclosed | lemma | explicit | Lean proves only seam-equation compatibility of the produced marked solution; potential integral density, prescribed boundary classes and all-component conclusion absent. |
| 033 | companion_full | partial | explicit | Lean is only the negative-fiber branch of a companion paper's log additivity; no orbifold/log/ordinary Iitaka subadditivity at all. |
| 058 | companion_full | full | implicit | Kollár–Pardon characterization of semialgebraic universal covers (D×ℂ^m×F) and its corollaries are absent; Lean is only the companion bounded-domain symmetry theorem. |
| 066 | headline_lemma_disclosed | lemma | explicit | Lean is only a compactness lemma for chart-field retractions; neither uniform Cartier sections nor bounded klt complements with index N(d,eps) are stated. |
| 076 | companion_full | full | implicit | Headline is two-sided ultraflatness (lower bound (1-ε)√N too); Lean gives only the max upper bound and L^p flatness; merit-factor corollary absent. |
| 082 | companion_full | full | implicit | Headline annular r-variation bound (every r>2) is stronger; Lean has only the two-endpoint maximal L3xL3->L3/2 estimate. |
| 084 | companion_full | full | implicit | Lean covers only ratio q=1/2 (dyadic); headline is every q in (0,1). Note describes the dyadic case accurately but never flags general q. |
| 095 | companion_full | full | implicit | Lean: explicit degree-20 cone is not spectrahedral (no LMI). Headline: no semidefinite lift with auxiliary variables; that explicit cone does have one. |
| 104 | companion_full | full | implicit | Deterministic algorithm, exact values and optimal positional strategies, stochastic and parity extensions; Lean has only the Monte Carlo (prob ≥7/8) algorithm plus Truffet counterexample. |
| 114 | companion_full | full | implicit | Headline counts common integer bases of two integral polymatroids with binary capacities via rank oracles; Lean is only the 0/1 matroid common-bases case. |
| 116 | companion_full | full | explicit | No positive-characteristic uniform tuple (O(n^3 s^6), poly(log p) time); char-0 point lacks its poly-time and O(ns^2) bounds. |
| 117 | companion_full | full | explicit | Headline is NP-hardness of constant-factor approximation (reduction from 3SAT); Lean is the companion Goemans-Linial integrality-gap sequence. |
| 126 | headline_partial_disclosed | partial | explicit | Lean gives only superpolynomial (n^C) bounds for the unshifted slack matrix and lifts; headline has 2^{Omega(n)} for every fixed shift 0<rho<1. |
| 143 | companion_full | full | implicit | Lean covers only quintic classical Liénard systems (≤2 cycles, attained); the headline's uniform bound B(d) for all planar polynomial fields is absent. |
| 149 | companion_full | full | implicit | Classwise uniform permanence: one compact convex absorbing set per stoichiometric class; Lean bounds depend on the initial state. |
| 150 | companion_full | full | implicit | Headline is weak mixing (ergodicity of the product flow); Lean states only ergodicity. The note never says weak mixing is not formalized. |
| 152 | headline_partial_disclosed | partial | explicit | Lean asserts only finite Kolmogorov–Sinai entropy, not zero entropy. |
| 157 | label_error | full | explicit | Lean has alpha<=2 and h<26m/75+2/3<m/2<=chi; chi_f>=m/alpha>=m/2 is a one-line LP step, so Lean implies headline (plus cm<m/100). |
| 182 | companion_full | full | implicit | Lean covers only h(x)=x^2; headline is every intersective h of degree k with degree-only exponent c_k (and prime-argument variant). Note silent on this. |
| 184 | companion_full | full | implicit | Lean lacks the O_F(Δ/logΔ) correspondence-coloring bound; the AEKS bound follows from it via max-degree deletion, so Lean is implied (weaker, not different). |
| 186 | companion_full | full | implicit | r-uniform hypergraph influence bound and threshold width O_r((log n)^{-r/(r-1)}), incl. nonmonotone variance bound; Lean covers graphs (r=2) only. |
| 191 | headline_partial_disclosed | partial | explicit | Lean gives the n^{-2+eta} bound only along an unbounded sequence n_j, not every large n, and uses a smaller exponent than the paper's eta. |
| 194 | headline_lemma_disclosed | lemma | explicit | Lean is the char-p complete-domain Dutta multiplicity comparison; Lech's e(R)≤e(S) for flat local maps is absent. |
| 195 | headline_partial_disclosed | partial | explicit | Lean only asserts such a ring exists (trivially, e.g. C[[x,y,z]]); absence of nonzero f.g. MCM modules is missing. Implied by headline, so weaker. |
| 197 | companion_full | full | explicit | Lean groups have odd-prime torsion over some char-2 field; headline needs torsion-free G over F_2 (and nonsofic). Determinant/odd-char are separate companions. |
| 206 | headline_partial_disclosed | partial | explicit | Lean is only part (i), the colored-graph criterion; it lacks undecidability (ii), the nonrepresentable lattice (iii) and subgroup intervals (iv). |
| 207 | companion_full | full | implicit | ℓ¹(G) Banach-algebra idempotents and finite support on finite-order classes; Lean covers only the complex group ring ℂ[G] (plus torsion-free Kaplansky corollary). |
| 210 | companion_full | full | explicit | Lean gives Foulkes-Howe surjectivity for b>=a(a-1), so the sixth case only for b>=30; headline embedding for 6<=b<30 is missing. |
| 211 | companion_full | full | implicit | Only the q>4 CRT regime; the q∈(0,4] LQG-sphere limits (surface side of the transition), random-walk and spectral results absent. |
| 212 | headline_partial_disclosed | partial | explicit | Companion limit-shape paper, differentiability only (no strict convexity); headline no-bigeodesics theorem not formalized at all. |
| 215 | companion_full | full | explicit | Lean is finite-volume O(n) correlation decay; headline O(3) continuum limit (OS axioms, non-Gaussian, unique vacuum, mass gap) absent; note flags O(4), not O(3). |
| 218 | headline_lemma_disclosed | partial | explicit | Lean is a finite-graph likelihood comparison lemma (an input to the universality papers); it has no scaling limits, CFT correlations or SLE3 convergence. |
| 222 | headline_lemma_disclosed | lemma | explicit | Ising free-energy convergence and Borel potentials absent (only finiteness of variational value); spherical companion formula is fully formalized. |
| 227 | headline_partial_disclosed | partial | explicit | Lean has discrete ratio cutoff only for beta<1/2, with no location or continuous time. Its spectral-gap and beta>=1 comparators are not implied by the headline. |
| 229 | headline_partial_disclosed | partial | explicit | Only reconstruction above Kesten–Stigum for 3 states; nonreconstruction at/below threshold, the four-state Potts case and SBM corollary absent. |
| 230 | partial_undisclosed | partial | implicit | Only positivity (lower half) of H^h on segments; finiteness of H^h(gamma[s,t]) and finite expected measure in disks are missing, unflagged. |
| 237 | companion_full | full | explicit | Only strip-crossing main theorem is full; others summability/free-energy/B_h lemmas (yaml-listed Chords paper only a lemma). Fixed-length SAW diameter n^{3/4} absent. |
| 238 | partial_undisclosed | partial | overstated | Only explicit constants missing: ThorpRemaining states t_mix=Θ(log N) and 2048d/32800d convergence, but not 1600d or the 2d−O(1) lower bound. |
| 240 | companion_full | full | explicit | ZFC eventual categoricity theorem (uniform threshold μ(λ) transfer) absent; Lean is only the CH counterexample to the prescribed Hanf threshold. |
| 247 | companion_full | full | implicit | Lean has an infinite f.p. periodic St_12(R) but no residual finiteness and no 2-power element orders. The note flags only the omitted nil-algebra results. |
| 256 | companion_full | full | implicit | Lean is the one-variable unimodular case (m=n=1); Howie's general nonsingular m×n systems over arbitrary groups absent. |
| 260 | headline_lemma_disclosed | lemma | explicit | Companion CKS paper: end-replacement construction plus Schwarzschild equality examples; neither the Bondi-Penrose inequality nor the headline enclosing-area inequality. |
| 261 | headline_partial_disclosed | partial | explicit | Lean proves only the a.s. spectrum [-4-h,4+h], a conjunct of main theorem and our headline, so implied (weaker); pure-point type absent. |
| 262 | companion_full | full | implicit | Lean is the scalar (m=1) case only; it lacks matrix-valued potentials of every size and the classification of all equality cases. |
| 263 | companion_full | full | implicit | Excess-charge bound n ≤ Z+CM for molecules and neutral-atom ionization/radius bounds absent; Lean gives generalized ionization energy and radius asymptotics. |
| 266 | companion_full | full | explicit | Lean has N(6)<=5 plus Fourier vanishing, which N(6)=3 does not imply, so the label is different. The bound of three is missing. |
| 267 | companion_full | full | explicit | Lean is zero-temperature ground-state BEC; headline is condensation of the positive-temperature canonical Gibbs state (and depletion law). |
| 271 | companion_full | full | implicit | Headline Bloch T^{3/2} law with exact coefficient (finite-range J, d=3) absent; Lean is companion KMS-state spontaneous magnetization, d>=3. |
| 272 | headline_partial_disclosed | partial | explicit | Lean gives PPT-composition/PPT-square counterexamples and entangled Choi matrix (no product vector in range); zero distillable key, the headline, absent. |
| 277 | partial_undisclosed | partial | implicit | Lean rate exponent is δ^13, the paper's universal rate is δ^5; the note states δ^13 without saying it is weaker than the paper's. |
| 280 | headline_partial_disclosed | partial | explicit | Complete rationality of the net, unitarizability of simple modules, braided unitary tensor equivalence Rep(V)≃Rep^f(A_V), extension classification. |
| 281 | headline_lemma_disclosed | lemma | explicit | Lean has Parisi value identities (conditional on a minimizer) and companion full support; nothing about QAOA circuit energies converging to the SK ground state. |
| 290 | companion_full | full | explicit | Lean is the bounded spectral recovery tool; no amenable expected P⊂N with P'∩c(M)=N'∩c(M) (relative bicentralizer), nor absolute bicentralizer. |
| 291 | companion_full | full | implicit | Headline equivariant Jiang-Su stability (cocycle conjugacy) absent; Lean is companion RR0-of-tracial-ultrapower implies uniform Gamma (Problem XXI). |
| 301 | headline_lemma_disclosed | lemma | explicit | Lean proves only ideal-lattice transport and idempotent-trace description under a trace-cone equivalence; the classification A⊗W⊗K ≅ B⊗W⊗K absent. |
| 307 | companion_full | full | implicit | Lean kills the class only under reduced assembly; the headline needs vanishing in maximal Roe algebra K-theory (stronger, since reduced factors through maximal). |
| 312 | headline_lemma_disclosed | full | explicit | Semi-model structure and equivalence with the homotopy theory of spaces (the homotopy hypothesis); Lean states the paper's thm:main, elementary expansions are weak equivalences. |
| 323 | headline_partial_disclosed | partial | explicit | Lean has only CH implies not SQ over R and C. The consistency of SQ (from a measurable cardinal) and hence independence are missing. |
| 337 | companion_full | full | implicit | Lean is CAT(0) Euclidean filling bound plus coefficient optimality; κ<0 manifold isoperimetry for finite-perimeter sets and equality rigidity absent. |
| 347 | companion_full | full | explicit | Headline dim-22 stable-Morse counterexamples with unbounded deficit absent; Lean is companion Q^3 three-fixed-point example (cup-length=4 conjunct omitted). |
| 348 | companion_full | full | implicit | Lean covers strictly positive sectional curvature; headline is sec>=0 (zero-plane case giving S2xS2) plus L2 gap. Note does not flag this. |
| 356 | companion_full | full | implicit | Lean is the auxiliary weak-Hessian-along-geodesics theorem; it does not give the Alexandrov ⇔ RCD + distributional sectional curvature characterization. |
| 361 | companion_full | full | implicit | Three-dimensional metrics for all large k with ≥(k+2)^2 (c(k+1)^2) harmonic functions; Lean is a single even n≥8 counterexample. |
| 363 | companion_full | full | explicit | Lean solutions conserve only local mass and total momentum, satisfy an energy inequality, and are L1-continuous only initially. The headline has exact local conservation throughout. |
| 365 | companion_full | full | implicit | Lean is the measurable-conductivity nonuniqueness counterexample; joint metric-plus-connection uniqueness from one boundary patch absent. |
| 367 | headline_partial_disclosed | partial | explicit | Only existence of nonflat minimizer in R^7 (known, De Silva-Jerison); the new flatness for d<=6 and regularity corollaries missing. |
