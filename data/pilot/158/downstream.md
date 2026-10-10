# Family 158: downstream targets (the plane is not 5-colorable)

Date: 2026-10-10. Analyst: downstream-target agent.

**Method.** Text-level reading of the Lean only. I did not run lake, lean or comparator, because another process is building in the workspace. The comparator PASS on 2026-10-10 is the orchestrator's result. Literature claims rest on WebSearch snippets; WebFetch was not used because arxiv.org is blocked.

**Item (F5 (lemma/theorem used as a transfer device)).** C1 Haar rigidity of wild K-invariant laws on the dual D of the discrete algebraic plane E = Q-bar (every K-invariant probability on D with ν(C) = 0 is Haar), together with its parts C4 (radial identity m(A)m(B) <= m(|A-B|)) and C2 (forward transfer: proper k-colouring gives a measurable weak k-colouring)

## Part A: Is the item in the Lean?

**lean_status: as in paper.** wild_fourier (Ergodicity.lean:335) states Thm 2.3 in Fourier form: every nonzero coefficient of a wild law vanishes, which is equivalent to Haar. It uses the paper's route: compact-factor tower (CompactFactors.Stationary.exists_terminal_factor), relative products, the radial identity massReal_difference, and a number-field step. residual_fourier -> projected_unit_correlation -> exists_label_field -> proper_to_borel_weak puts it on the comparator chain of no_proper_five_coloring. Checked at text level only; the orchestrator reports comparator PASS on 2026-10-10.

**Gaps**

- NOT COMPILED BY ME: text-level only, because another process is building. The comparator PASS (2026-10-10) is the orchestrator's; data/lean_checks.json had no 158 entry when read.
- Statement form: Haar rigidity appears as vanishing of nonzero Fourier coefficients (wild_fourier) and, in Hilbert form, as zero correlations of K-fixed vectors orthogonal to the continuous subspace (residual_fourier). It is not stated literally as ν = Haar; the two are equivalent by Fourier uniqueness on compact D.
- Only the forward transfer is formalized (proper_to_borel_weak, generic in k). The converse (weak gives proper, via typical points and de Bruijn-Erdős compactness) is not a Lean theorem. Only its local lemma weak_density_proper is there.
- Distance 1 is hardwired in LabelModel.Proper (Representations.lean:55) and in WeakColoring. Reuse on other distance sets (S1, S2, O1, O4) needs a 200-400-line generalization (estimate). The rigidity layer is distance-agnostic.
- Two weak-colouring notions coexist: EuclideanFiveColor.WeakColoring (ℂ, angularMeasure on angles, a.e. over the product), used on the 5-colour side, and Problem160.WeakMeasurableColoring (the paper's ball-integral form, Basic.lean:30), used on the 7-colour side. They are not linked by a Lean lemma.
- Second comparator PlaneColoring (properColoring_seven, Problem160) is independent of the item: its 9-file, 519-line closure does not import PlaneSpectrum.

**Comparator chain**

1. `OAI.EuclideanFiveColor.no_proper_five_coloring (Five.lean:124; comparator target)`
1. `OAI.EuclideanFiveColor.proper_to_borel_weak (BorelTransfer.lean:436)  [the other branch: no_measurable_weak_five_coloring, Five.lean:105]`
1. `OAI.PlaneFiveColor.LabelModel.exists_label_field (BorelTransfer.lean:341)`
1. `OAI.PlaneFiveColor.LabelModel.fieldVector_unit_correlation (BorelTransfer.lean:234)`
1. `OAI.PlaneFiveColor.LabelModel.projected_unit_correlation (BorelTransfer.lean:59)`
1. `OAI.PlaneFiveColor.Spectral.residual_fourier (Ergodicity.lean:403)`
1. `OAI.PlaneFiveColor.Spectral.finite_wild_fourier (Ergodicity.lean:364)`
1. `OAI.PlaneFiveColor.Spectral.wild_fourier (Ergodicity.lean:335)`
1. `OAI.PlaneFiveColor.Spectral.ergodic_wild_fourier (Ergodicity.lean:52)`
1. `OAI.PlaneFiveColor.Spectral.fourier_vanish_of_terminal / projectedMass_vanish (Ergodicity.lean:37 / 30) -> massReal_vanish (RadialEnergy.lean:452) -> massReal_difference (RadialEnergy.lean:157)`
1. `OAI.PlaneFiveColor.Spectral.exists_terminal_factor (CompactFactors/Stationary.lean:126)`

**Key declarations** (verbatim text is in downstream.json, `lean_source`)

| Declaration | Kind | File:line |
|---|---|---|
| `E` | abbrev (setting) | OAI/Analysis/PlaneSpectrum/Basic.lean:9 |
| `K` | def (setting: algebraic unit rotations) | OAI/Analysis/PlaneSpectrum/Basic.lean:11 |
| `OAI.PlaneFiveColor.Spectral.DiscreteE / D` | def + abbrev (setting: compact dual of discrete E) | OAI/Analysis/PlaneSpectrum/Basic.lean:44 |
| `C` | def (setting: ordinary continuous characters j(R^2)) | OAI/Analysis/PlaneSpectrum/Basic.lean:99 |
| `IsWild` | def (item hypothesis) | OAI/Analysis/PlaneSpectrum/Basic.lean:299 |
| `wild_fourier` | lemma (ITEM C1: Haar rigidity, Fourier form) | OAI/Analysis/PlaneSpectrum/Ergodicity.lean:334 |
| `residual_fourier` | lemma (C1 in Hilbert-space form, used by the transfer) | OAI/Analysis/PlaneSpectrum/Ergodicity.lean:403 |
| `exists_terminal_factor` | theorem (C1 engine: compact-factor tower / relative singularity) | OAI/MeasureTheory/CompactFactors/Stationary.lean:123 |
| `massReal_difference` | lemma (C4 radial identity: m(A) m(B) <= m(|A-B|)) | OAI/Analysis/PlaneSpectrum/RadialEnergy.lean:157 |
| `OAI.PlaneFiveColor.LabelModel.Proper / Space` | def + abbrev (C2 label model; distance 1 hardwired) | OAI/Analysis/PlaneSpectrum/Representations.lean:55 |
| `projected` | def (C2: projection onto the continuous subspace) | OAI/Geometry/PlaneColoring/BorelTransfer.lean:46 |
| `projected_unit_correlation` | lemma (C2: projection keeps zero unit correlations, via residual_fourier) | OAI/Geometry/PlaneColoring/BorelTransfer.lean:59 |
| `fieldVector_unit_correlation` | lemma (C2: extension to all real directions) | OAI/Geometry/PlaneColoring/BorelTransfer.lean:234 |
| `proper_to_borel_weak` | lemma (C2: forward transfer, generic in k) | OAI/Geometry/PlaneColoring/BorelTransfer.lean:436 |
| `WeakColoring` | def (target notion of the transfer) | OAI/Geometry/PlaneColoring/Coloring.lean:27 |
| `weak_density_proper` | lemma (support: density points of a weak class contain no unit pair) | OAI/Geometry/PlaneColoring/WeakColoring.lean:149 |
| `no_proper_five_coloring` | theorem (comparator target) | OAI/Geometry/PlaneColoring/Five.lean:124 |

## Verdict on speedup
Strong candidate family. The transfer (C1 + C2) appears to make at least two known, independently proved theorems short compositions with a classical measurable theorem (Davies odd distances; Davies-McCarty-Pilipczuk primes/polynomials). Both are Lean-statable in one line. This is conditional on three unverified links (see precedent_check.caveats).

## Top 5 (Lean-usable first)

1. **S1: odd distances (Davies 2022)** (Lean-usable: yes). This is the cleanest genuine device-reuse target. The statement takes one line in Lean, and it is not a corollary of chi >= 6. The device route is C1 + transfer + weak FKW, with no finite graphs, while the known proof is a dedicated spectral argument. With arm: the BorelTransfer closure (15,967 lines). Arm A makes the prover generalize Proper to an odd-distance set; arm B pre-adds that generalization (200-400 lines). Without arm: Mathlib + Coloring/WeakColoring. Both arms get the same weak-FKW lemma (about 1-2k lines), so the measured gap is the device. Run N2 (Campbell-Davies) as a consistency check first.

2. **S2: prime and polynomial distances (DMP 2025)** (Lean-usable: yes). Same arms as S1. Two more known theorems follow from the same composition, which tests whether the device, once found, makes a family of theorems cheap rather than one. A large with/without gap on S1 and S2 together is the strongest speedup evidence available for 158.

3. **O1: all unbounded algebraic distance sets** (Lean-usable: yes). Statable now. If S1/S2 go through, O1 is the same proof with S arbitrary, i.e. a new theorem produced by reusing the device. Its contrast with Campbell-Davies (non-measurable colourings avoid some unbounded distance set) makes it a proves-too-much test as well as a payoff.

4. **S3: chi(R^2) >= 5 via transfer + weak Falconer** (Lean-usable: yes). A known theorem whose existing proofs use 500-1,600-vertex graphs plus SAT. The arm design must delete the 14,369-line weak-five obstruction from both arms, otherwise chi >= 6 gives it for free. The open risk is whether Falconer's argument survives a.e.-only exclusions. weak_density_proper suggests it does.

5. **O2: chi(R^n) >= (1.268+o(1))^n via an n-dimensional transfer** (Lean-usable: yes). The statement is Lean-statable now, and the payoff is very high: it would beat Raigorodskii's 1.239 base. Both the n-dimensional rigidity and the measurable bound are major libraries, so this is a research direction, not a near-term prover test.

## Speedup targets (known theorems)

### S1. Odd distances: every finite colouring of the plane has a monochromatic pair at odd integer distance (Davies)
- **Statement:** For every k and every c : R^2 -> [k] there are x, y with c(x) = c(y) and |x-y| an odd integer.
- **Reference / status:** J. Davies, "Odd distances in colourings of the plane", arXiv:2209.15598 (resolves a conjecture of Soifer; proof described as a spectral method). Status: known theorem (2022); no Lean formalization found
- **Current proof size:** Paper length not verified (WebFetch blocked). Expected 10-20 pp. Lean: none.
- **How the item helps:** Device route: assume a k-colouring with no monochromatic odd distance. The odd integers are in F (real algebraic), so the distance-set version of the transfer (C1 + C2) gives a measurable weak k-colouring whose classes have zero pair-correlation at every odd radius. The densest class has positive upper density, so weak FKW gives positive correlation at all radii >= d0, a contradiction. The geometric/spectral finite-graph work in Davies' proof is replaced by C1 (wild laws are Haar) plus a classical measurable density theorem. This is device reuse: it is NOT a corollary of chi >= 6.
- **Counts as:** device reuse on another theorem (counts toward the speedup test)
- **Expected speedup:** high (if the distance-set transfer holds; see N2). **Confidence:** medium (two inferences unverified from sources: the a.e. pair-correlation form of Bourgain/FKW, and that nothing in C1/C2 uses distance 1 beyond Proper).
- **Lean statement:**

```lean
theorem odd_distance (k : ℕ) (c : ℂ → Fin k) : ∃ x y : ℂ, c x = c y ∧ ∃ n : ℕ, ‖x - y‖ = 2 * n + 1
```
- **With arm:** with-arm library = import closure of OAI.Geometry.PlaneColoring.BorelTransfer: 32 files, 15,967 lines (OAI/Analysis/PlaneSpectrum minus CircleDecay/CircleOperator/Fourier, all 16 files of OAI/MeasureTheory/CompactFactors, PlaneColoring.Coloring, PlaneColoring.BorelTransfer). Device declarations: Spectral.wild_fourier, residual_fourier, IsWild, LabelModel.projected*, fieldVector*, exists_label_field, sample_field, proper_to_borel_weak. Distance-set generalization the with-arm needs, 200-400 lines (estimate): replace LabelModel.Proper (Representations.lean:55, distance 1 hardwired) by ProperS (S : Set F) := ∀ x y, ‖x-y‖ ∈ S → ω x ≠ ω y. color_unit_correlation then holds at r*kCoeff b for r ∈ S; the rest of BorelTransfer goes through with Circle replaced by r•Circle. The rigidity (wild_fourier) is distance-agnostic and unchanged. Arm A (strict): give only the release declarations, so the prover must do the generalization. Arm B (assisted): pre-add proper_avoiding_to_borel_weak. Plus: Auxiliary lemma in BOTH arms ("weak FKW", Bourgain 1986 Fourier proof): if A ⊆ ℂ is measurable with positive upper density, there is d0 such that for every d ≥ d0, ∫∫ 1_A(x) 1_A(x + d·u) dσ(u) dx > 0 on some ball. Not in Mathlib; about 1,000-2,000 lines (estimate). OAI PlaneSpectrum/CircleDecay.lean (241 lines, Fourier decay of circle measure) and Fourier.lean (163) can seed it.
- **Without arm:** without-arm = Mathlib d13f23b + PlaneColoring.Coloring (ProperColoring, WeakColoring, angularMeasure, direction: 34 lines) + WeakColoring.lean (176 lines, density-point lemmas) + the same auxiliary measurable lemma as the with-arm. Remove PlaneSpectrum/*, CompactFactors/*, BorelTransfer.lean. Plus the same weak-FKW lemma.
- **Baseline formal proof:** None in Lean. Reference sizes: the device itself is 15,967 lines (BorelTransfer closure); weak FKW about 1-2k lines (estimate). Compare the prover budget for the remaining composition in each arm.
- **Lean feasibility:** statable now. Needs: Mathlib ℂ, norm, Fin k (same shape as ComparatorChallenges/EuclideanFiveColor.lean).. Missing: for the with-arm proof: distance-set transfer (200-400 lines, estimate); weak FKW / Bourgain lemma in both arms (1,000-2,000 lines, estimate). Compare against: none external; OAI BorelTransfer closure 15,967 lines is the device.

### S2. Prime and polynomial distances (Davies-McCarty-Pilipczuk)
- **Statement:** Every finite colouring of R^2 has a monochromatic pair at prime distance, and one at distance f(n) for any non-constant f in Z[x] with positive leading coefficient.
- **Reference / status:** Davies, McCarty, Pilipczuk, arXiv:2308.02483; Israel J. Math. (published 2025-11-30). Status: known theorem; no Lean formalization found
- **Current proof size:** not verified (WebFetch blocked)
- **How the item helps:** Identical to S1: primes and {f(n)} are unbounded subsets of F. The device route proves both statements by the same 1-page composition, while the known proofs need separate number-theoretic and spectral input.
- **Counts as:** device reuse
- **Expected speedup:** high. **Confidence:** medium.
- **Lean statement:**

```lean
theorem prime_distance (k : ℕ) (c : ℂ → Fin k) : ∃ x y : ℂ, c x = c y ∧ ∃ p : ℕ, p.Prime ∧ ‖x - y‖ = p
theorem poly_distance (k : ℕ) (c : ℂ → Fin k) (f : Polynomial ℤ) (hf : 0 < f.natDegree) (hl : 0 < f.leadingCoeff) : ∃ x y : ℂ, c x = c y ∧ ∃ n : ℕ, ‖x - y‖ = (f.eval (n : ℤ) : ℝ)
```
- **With arm:** As S1.
- **Without arm:** As S1.
- **Baseline formal proof:** none
- **Lean feasibility:** statable now. Needs: Mathlib Nat.Prime, Polynomial ℤ, ℂ norm. Missing: as S1. Compare against: none.

### S3. chi(R^2) >= 5 (de Grey 2018) via transfer + a Falconer-type weak four-colour obstruction
- **Statement:** The plane has no proper 4-colouring.
- **Reference / status:** de Grey 2018 (1,581-vertex graph, computer check); Heule (SAT, 553/874 vertices); Parts 2020 (509 vertices; human-verifiable proof arXiv:2010.12661); Exoo-Ismailescu arXiv:1805.00157; Falconer 1981 (chi_m >= 5 by density points and rotations). Status: known theorem (also a corollary of 158's chi >= 6, hence the arm design below)
- **Current proof size:** de Grey/Heule: SAT certificates for 500-1,600-vertex graphs. Parts' human proof is long (pages not verified). Falconer's measurable argument: a few pages.
- **How the item helps:** The forward transfer reduces "no proper 4-colouring" to "no weak measurable 4-colouring". Falconer's density-point argument should run on weak colourings: the paper says it adapts this mechanism, and weak_density_proper (WeakColoring.lean:149) already shows density points of a weak class contain no unit pair. The finite-graph route is replaced by about 1 page of measure theory plus the device.
- **Counts as:** device reuse IF the weak-five obstruction is removed from the library; otherwise a theorem corollary
- **Expected speedup:** med. **Confidence:** medium-low (Falconer's proof has not been checked for an a.e.-only step).
- **Lean statement:**

```lean
theorem no_proper_four_coloring : ¬ ∃ c : ℂ → Fin 4, EuclideanFiveColor.ProperColoring 4 c
```
- **With arm:** with-arm library = import closure of OAI.Geometry.PlaneColoring.BorelTransfer: 32 files, 15,967 lines (OAI/Analysis/PlaneSpectrum minus CircleDecay/CircleOperator/Fourier, all 16 files of OAI/MeasureTheory/CompactFactors, PlaneColoring.Coloring, PlaneColoring.BorelTransfer). Device declarations: Spectral.wild_fourier, residual_fourier, IsWild, LabelModel.projected*, fieldVector*, exists_label_field, sample_field, proper_to_borel_weak. Remove the weak-five obstruction (Five.lean and its 38 non-transfer files, 14,369 lines: Palettes, Transitions, Interfaces, FullApproximation, GraphCuts, FourContinuity, FourTransport, PlanarCovers, Mesh, etc.) from BOTH arms. Otherwise no_proper_five_coloring gives every 4-color statement for free. Keep WeakColoring.lean (176 lines) in both arms.
- **Without arm:** without-arm = Mathlib d13f23b + PlaneColoring.Coloring (ProperColoring, WeakColoring, angularMeasure, direction: 34 lines) + WeakColoring.lean (176 lines, density-point lemmas) + the same auxiliary measurable lemma as the with-arm. Remove PlaneSpectrum/*, CompactFactors/*, BorelTransfer.lean. Remove the weak-five obstruction (Five.lean and its 38 non-transfer files, 14,369 lines: Palettes, Transitions, Interfaces, FullApproximation, GraphCuts, FourContinuity, FourTransport, PlanarCovers, Mesh, etc.) from BOTH arms. Otherwise no_proper_five_coloring gives every 4-color statement for free.
- **Baseline formal proof:** No Lean/Isabelle formalization of chi >= 5 found (search 2026-10-10). Upper reference: the OAI weak-five obstruction (14,369 lines) proves the stronger weak statement.
- **Lean feasibility:** statable now. Needs: OAI EuclideanFiveColor.ProperColoring (comparator challenge file). Missing: for the proof: weak Falconer argument (about 500-1,500 lines, estimate). Compare against: none external; OAI Five route 14,369 lines (stronger statement).

### S4. Fractional chromatic number of the plane >= 4 (Matolcsi-Ruzsa-Varga-Zsámboki) via a fractional transfer
- **Statement:** chi_f of the unit-distance graph of R^2 is at least 4.
- **Reference / status:** Matolcsi, Ruzsa, Varga, Zsámboki, arXiv:2311.10069 (revised 2025-03-27). Their method uses Følner averaging over countable isometry groups (as described in the 158 paper's intro). Status: known theorem
- **Current proof size:** not verified
- **How the item helps:** A random independent set invariant under E ⋊ K, projected by C1/C2, gives a [0,1]-valued measurable density with zero unit autocorrelation. Measurable density bounds on unit-distance-avoiding functions then apply directly. Recalled, not searched: m_1(R^2) <= 0.247 (Ambrus et al. 2022) would give chi_f >= 4.04, strictly better than 4; see O5.
- **Counts as:** device reuse (variant)
- **Expected speedup:** low-med. **Confidence:** low (requires a fractional version of the transfer; the [0,1]-valued projection has ∫f^2 below its mean, which needs checking).
- **Lean statement:**

```lean
Needs fractional chromatic number of an infinite graph: def FracColorable (G : SimpleGraph V) (t : ℝ) := ∃ μ : Measure (Set V) supported on independent sets, ... ; or the finite-subgraph sup form: ∀ ε>0, ∃ finite unit-distance graph H, χ_f(H) ≥ 4 - ε.
```
- **With arm:** with-arm library = import closure of OAI.Geometry.PlaneColoring.BorelTransfer: 32 files, 15,967 lines (OAI/Analysis/PlaneSpectrum minus CircleDecay/CircleOperator/Fourier, all 16 files of OAI/MeasureTheory/CompactFactors, PlaneColoring.Coloring, PlaneColoring.BorelTransfer). Device declarations: Spectral.wild_fourier, residual_fourier, IsWild, LabelModel.projected*, fieldVector*, exists_label_field, sample_field, proper_to_borel_weak.
- **Without arm:** without-arm = Mathlib d13f23b + PlaneColoring.Coloring (ProperColoring, WeakColoring, angularMeasure, direction: 34 lines) + WeakColoring.lean (176 lines, density-point lemmas) + the same auxiliary measurable lemma as the with-arm. Remove PlaneSpectrum/*, CompactFactors/*, BorelTransfer.lean.
- **Baseline formal proof:** none
- **Lean feasibility:** statable with < 300 lines of new definitions. Needs: Mathlib SimpleGraph, finite sets; fractional chromatic number not in Mathlib. Missing: fractional chromatic number via LP on finite subgraphs (about 100-200 lines). Compare against: none.

## Open or new problems

| ID | Problem | Status | Obstruction match | Payoff / confidence / difficulty | Lean |
|---|---|---|---|---|---|
| O1 | Unbounded algebraic distance sets are unavoidable by finite colourings | apparently open/new (not found in searches). It follows from C1 + distance-set transfer + weak FKW if those hold. | exact: the passage from arbitrary to measurable colourings for distance constraints, which is what C1/C2 do | high (a new theorem subsuming two recent papers). Also the single most informative consistency check, see N2. / medium / moderate | statable now |
| O2 | Lift measurable exponential lower bounds to chi(R^n): is chi(R^n) >= (1.268+o(1))^n? | open. The 158 novelty pass's open question 5 asks whether C1 generalizes to R^n. | exact for the transfer. The measurable bounds use only pair autocorrelations vanishing on the unit sphere, which is what the weak notion provides, and an L^2 autocorrelation is continuous, so a.e. vanishing gives vanishing everywhere. | very high / low-medium / hard | statable now |
| O3 | Hadwiger-Nelson endgame: is there a weak measurable 6-colouring of the plane? | open | the device removes regularity entirely, which leaves a purely measurable problem | very high / low / very hard | statable now |
| O4 | Other algebraic distance graphs: chi(R^2, D) vs chi_m(R^2, D) for finite D ⊂ F | open in general | exact (the transfer is distance-agnostic for D ⊂ F) | medium / medium / moderate | statable now |
| O5 | Fractional chromatic number of the plane strictly above 4 | open (as far as found) | partial: needs the fractional transfer of S4 | medium / low / moderate | statable with < 300 lines of new definitions |
| O6 | Crum / Gneiting-Sasvári without measurability on all of R^2 | unknown to me (no source found either way) | C1 is exactly this statement on the countable group E with group K | medium (harmonic analysis) / low / hard | statable with < 300 lines of new definitions |
| O7 | For which countable fields E ⊂ C does Haar rigidity hold? | open (natural question raised by the device) | the device's hypotheses themselves | medium / medium / moderate | statable with < 300 lines of new definitions |

- **O1.** For every unbounded S ⊂ (real algebraic numbers)_{>0} and every finite colouring of R^2, some colour class contains two points at distance in S. Reference: Generalizes Davies (odd distances) and Davies-McCarty-Pilipczuk (primes, integer polynomials). Contrast: Campbell-Davies (2024 talks) give a NON-measurable finite colouring avoiding arbitrarily large distances; measurable case is Furstenberg-Katznelson-Weiss / Bourgain. (https://www.birs.ca/events/2024/5-day-workshops/24w5272/videos/watch/202410021108-Davies.html). Adaptation: S1 with S arbitrary. The transfer needs S ⊂ F so that r·K ⊂ E. Non-algebraic S would need a rigidity theorem for larger countable fields, where the number-field step (NumberFields.lean) may fail.
- **O2.** Prove an n-dimensional transfer (proper k-colouring of R^n gives a weak measurable k-colouring). Then the analytic bound chi_m(R^n) >= (1.268+o(1))^n (Bachoc-Passuello-Thiery) would hold for chi(R^n), improving Raigorodskii's (1.239+o(1))^n. Reference: Bachoc-Passuello-Thiery (cited in arXiv:2106.09360); Bachoc-Nebe-de Oliveira Filho-Vallentin arXiv:0801.1059 (SDP bounds for chi_m in dims 10-24); Raigorodskii 2000. (https://arxiv.org/abs/0801.1059). Adaptation: Replace E by (F)^n and K by SO_n(F). Rigidity: every SO_n(F)-invariant wild law on the dual of F^n is Haar. Restricting to 2-planes reduces part of this to C1; the conditional step is new.
- **O3.** By the transfer (both directions are in the paper; forward in Lean), chi(R^2) = 7 iff there is no weak measurable 6-colouring. Reference: Paper Thm transfer; Sokolov-Voronov 2025 (polygonal colourings need 7); Townsend 2005 (map colourings need 6). Erdős Problems #508. (https://www.erdosproblems.com/508). Adaptation: Run the paper's palette/interface machinery with six labels. The forward transfer is k-generic (proper_to_borel_weak takes any k).
- **O4.** For finite forbidden-distance sets D of real algebraic numbers, show chi(R^2,D) = chi_weak(R^2,D). Then lift known measurable lower bounds, e.g. for two forbidden distances, to unrestricted colourings. Reference: Voronov, "The chromatic number of the plane with an interval" (arXiv:2304.10163); Oliveira-Vallentin-type measurable bounds (recalled, not searched); Soifer 6-colourings with two distances (math.fau.edu abstract). (https://arxiv.org/html/2304.10163v3). Adaptation: Distance-set generalization the with-arm needs, 200-400 lines (estimate): replace LabelModel.Proper (Representations.lean:55, distance 1 hardwired) by ProperS (S : Set F) := ∀ x y, ‖x-y‖ ∈ S → ω x ≠ ω y. color_unit_correlation then holds at r*kCoeff b for r ∈ S; the rest of BorelTransfer goes through with Circle replaced by r•Circle. The rigidity (wild_fourier) is distance-agnostic and unchanged. Arm A (strict): give only the release declarations, so the prover must do the generalization. Arm B (assisted): pre-add proper_avoiding_to_borel_weak. Take S = D.
- **O5.** Is chi_f(R^2) >= 1/m_1(R^2) > 4 for unrestricted colourings? Reference: Matolcsi-Ruzsa-Varga-Zsámboki arXiv:2311.10069 (chi_f >= 4); measurable density bound m_1(R^2) <= 0.247 (Ambrus-Csiszárik-Matolcsi-Varga-Zsámboki, recalled from memory, not searched). (https://arxiv.org/abs/2311.10069v4). Adaptation: S4
- **O6.** Is every rotation-invariant positive-definite function on R^2, viewed as a discrete group, the sum of a continuous positive-definite function and c·δ_0? Reference: Crum 1956 (Proc. LMS 6, 548-560); Gneiting-Sasvári 1999 (Math. Geol. 31, 105-111: measurable isotropic covariances on R^d, d>=2, are continuous plus nugget). C1 is the Q-bar version without measurability. (https://link.springer.com/article/10.1023/A:1007597415185). Adaptation: Replace E by larger countable fields closed under the needed square roots. Transcendental radii break the finite number-field step (RadialEnergy/NumberFields). The non-measurable Campbell-Davies phenomenon suggests a counterexample may exist.
- **O7.** Characterize the pairs (E, K_E = E ∩ S^1) for which every K_E-invariant probability on the dual of discrete E with ν(C) = 0 is Haar. Reference: Payne 2009 (rational unit-distance graph: 2-colourable although chi_m >= 5, so rigidity fails for E = Q(i)); OAI Basic.lean uses RootableBy K ℕ (K_pow_surjective). (https://arxiv.org/pdf/1509.03667v1). Adaptation: Test divisibility of K (used in fixed_of_finite_orbit / finite_image_trivial) as the candidate criterion. Q(i) has non-divisible K and fails.

## Theorem corollaries (do not count as reuse)

- chi(R^2) >= 5 (de Grey): immediate from chi >= 6. It counts as reuse only with the arm design of S3.
- chi_m(R^2) >= 6 and the Borel chromatic number of the unit-distance graph >= 6: immediate since chi_m >= chi. This answers the novelty pass's open question 4 (why the paper omits chi_m >= 6): it is trivial.
- chi(R^n) >= 6 for all n >= 2 (contains R^2); new only for n = 3? Nechushtan 2002 already gives 6 for R^3 (recalled), so nothing new.
- Erdős Problems #508 status: 6 <= chi(R^2) <= 7 (with Isbell/Hadwiger 7).
- Transfer as an equivalence: chi(R^2) = min{k : a weak measurable k-colouring exists} (paper Thm transfer; the Lean has only the forward direction plus weak_density_proper).

## Negative controls

- **Payne 2009: rational-displacement unit graph (rigidity must FAIL for K = rational rotations).** The graph on R^2 whose edges are unit displacements with rational coordinates is 2-colourable, while every measurable colouring of it needs at least 5 colours (per the 158 paper's intro). Why the device must fail: With E = Q(i) and K = Pythagorean rotations (dense in S^1 but not divisible), the forward transfer would turn the 2-colouring into a weak measurable 2-colouring, contradicting chi_m >= 5. So the rigidity must be false there. This is a proved-false analogue and isolates divisibility of K (Basic.lean K_rootable) as load-bearing. Lean: statable with < 300 lines of new definitions; compare against: none.
- **Campbell-Davies: a finite (non-measurable) colouring avoiding arbitrarily large distances.** There is a finite colouring of R^2 and an unbounded set of distances realized by no monochromatic pair (2024 talk abstracts). The FKW measurable theorem fails for arbitrary colourings. Why the device must fail: Device + weak FKW proves O1 for every unbounded ALGEBRAIC distance set. So Campbell-Davies's distance set must be non-algebraic, or impossible to make algebraic. If their construction works with an algebraic (e.g. integer) unbounded sequence, then C1, the distance-set transfer or weak FKW is wrong. This is the sharpest proves-too-much test available. I could not fetch their paper; check its distance set first. Lean: needs major new library; compare against: none.
- **Upper bound chi(R^2) <= 7 (no-speedup control).** OAI.Problem160.properColoring_seven Why the device must fail: An explicit hexagonal colouring. The device produces no colourings, so the with-arm must not be cheaper. Lean: statable now; compare against: OAI Seven route: 9 files, 519 lines (Main.lean closure).
- **Configurations with three or more points / sphere colourings (pair-only and translation-only limits).** E.g. "every finite colouring of R^2 contains a monochromatic congruent copy of every large dilate of a fixed triangle" (Bourgain's measurable simplex theorem in R^3 and up, unrestricted analogue false in general); and the unit-distance chromatic number of S^2 (Lovász 1983). Why the device must fail: The projection onto the continuous spectral subspace preserves 2-point correlations only. For spheres there is no translation group E to dualize, so the device should give nothing. Lean: statable with < 300 lines of new definitions; compare against: none.

## Release reuse

- None found. A grep of all preprint .tex for "algebraic rotations / weak colo(u)ring / weak measurable colo" hits only family 158. A grep for Pontryagin / compact dual / positive definite hits unrelated families (e.g. 172 uses positive-definite matrices for an algebraic Ramsey criterion, not invariant measures).
- Could use it: 172 (classification of finite Euclidean Ramsey configurations): arbitrary finite colourings of R^n. The device preserves only PAIR correlations (projection onto the C-factor is a conditional expectation and does not preserve 3-point correlations), so it cannot transfer simplex/configuration density theorems (Bourgain simplex theorem) to arbitrary colourings. See negative control N4.
- Could use it: 073 (Falconer distance conjecture): shares Fourier decay of circle measure, but it concerns Hausdorff dimension of compact sets, not colourings. No reuse.
- Could use it: 167 (unit-distance counts): finite incidence geometry; no reuse.
- Lean note: Text-level only. proper_to_borel_weak is generic in k ([NeZero k]) but LabelModel.Proper hardwires distance 1. The rigidity layer (wild_fourier, residual_fourier) is distance-agnostic. The forward transfer's import closure (32 files, 15,967 lines) is disjoint from the weak-five obstruction (38 files, 14,369 lines), so clean with/without arms exist. The seven-colouring side (Problem160, 9 files, 519 lines) is independent of both.

## Precedent

**Earlier equivalent found: no.** No earlier equivalent was found, so the grade is not downgraded. The nearest statement-level analogues are still Crum 1956 and Gneiting-Sasvári 1999, which are measurable-only. The downstream search changes the picture in two ways. (1) The device has real reach beyond its own theorem: odd/prime/polynomial monochromatic distances (Davies; Davies-McCarty-Pilipczuk) appear to follow from C1 + transfer + Bourgain/FKW. That makes 158 a better speedup-test family than most. (2) The same argument proves O1 for every unbounded algebraic distance set, and Campbell-Davies is a sharp consistency test for it. The status stays N3 candidate. No independent expert review or external compile was found as of 2026-10-10 (comparator PASS reported by the orchestrator).

Nearest neighbours:
- Crum 1956 / Riesz: measurable PD = continuous PD + a.e.-zero PD part
- Gneiting-Sasvári 1999: measurable isotropic covariances on R^d (d >= 2) = continuous + nugget
- Furstenberg-Katznelson-Weiss 1990 / Bourgain 1986: measurable positive-density sets contain all large distances
- Matolcsi-Ruzsa-Varga-Zsámboki (Følner averaging over countable isometry groups for chi_f)
- Bourgeat-Heinrich-Melotti-Robert 2015; Gwyn-Stavrianos 2020 (invariant randomization, as cited by the paper)

Post-release use: None found (search 2026-10-10 found no 2026 discussion of chi >= 6).

Caveats: Three links in the S1/S2/O1 argument are mine and unverified: (a) the a.e. pair-correlation form of FKW/Bourgain; (b) the distance-set generalization of LabelModel.Proper; (c) that Campbell-Davies uses non-algebraic distances. Any of them could fail.

## Search log

- Local: read the brief, the 248 template, the 158 novelty/family files, the comparator configs, lean/docs/158.md, Five.lean, BorelTransfer.lean, WeakColoring.lean (parts), Ergodicity.lean (parts), Basic.lean (parts), Representations.lean:55-56, RadialEnergy declaration list, Stationary.exists_terminal_factor, and the paper's introduction.tex. Lean was NOT built (another process is building); everything is text-level.
- Local DAG: BFS in data/items/158_lean.json from no_proper_five_coloring to wild_fourier (chain recorded). Import closures computed by parsing import lines: BorelTransfer 32 files / 15,967 lines; Five 70 / 30,336; Main (seven) 9 / 519.
- Local release: grep CONTENTS.md for chromatic|unit distance|Falconer|Hadwiger|Crum|positive definite; grep all .tex for wild|Pontryagin|compact dual|positive definite and for algebraic rotations / weak colouring. Only 158 uses the device.
- WebSearch "formal proof chromatic number of the plane at least 5 Lean OR Isabelle": none found; Parts human-verifiable (2010.12661), Exoo-Ismailescu (1805.00157).
- WebSearch "measurable chromatic number R^n 1.268 Bachoc Passuello Thiery 1.239 Raigorodskii": 1.268 confirmed via the 2106.09360 citation; the 1.239 constant was not confirmed by the snippet (it was later seen in another snippet: "(1.239… + o(1))^n ≤ χ(R^n) ≤ (3 + o(1))^n").
- WebSearch "Erdős finite coloring plane one colour realizes all distances FKW": FKW measurable; Davies odd distances; Davies-McCarty-Pilipczuk prime distances; arXiv 2607.19946 (dense colour classes, unrelated).
- WebSearch x2 "Campbell Davies non-measurable colourings avoiding large distances": talk abstracts only; no arXiv id and no distance-set details. Recorded as the key unchecked fact.
- WebSearch "Odd distances in colourings of the plane" proof method: described as a spectral method; length not obtained.
- WebSearch "Prime and polynomial distances" abstract: polynomial f in Z[x] with positive leading coefficient, and primes; Israel J. Math. 2025.
- WebSearch "Crum 1956 ... Gneiting Sasvári": both confirmed at abstract level (measurable hypotheses).
- WebSearch "chromatic number of the plane 2026 not five-colorable": no 2026 discussion indexed.
- WebFetch not attempted (arxiv.org blocked per environment). All literature claims are snippet-level.

## Sources

- data/pilot/158/novelty.json, novelty.md, family.json
- data/items/158_lean.json (text-level DAG)
- data/raw/openai-math/lean/OAI/Analysis/PlaneSpectrum/{Basic,Ergodicity,RadialEnergy,Representations}.lean; OAI/MeasureTheory/CompactFactors/Stationary.lean; OAI/Geometry/PlaneColoring/{BorelTransfer,Coloring,WeakColoring,Five,Basic}.lean
- data/raw/openai-math/lean/ComparatorChallenges/{EuclideanFiveColor,PlaneColoring}.{json,lean}; lean/docs/158.md
- data/raw/openai-math/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/build/sections/introduction.tex
- https://ar5iv.labs.arxiv.org/html/2209.15598
- https://arxiv.org/pdf/2308.02483
- https://link.springer.com/article/10.1007/s11856-025-2857-4
- https://www.birs.ca/events/2024/5-day-workshops/24w5272/videos/watch/202410021108-Davies.html
- https://math.gatech.edu/node/32840434
- https://mccarty.math.gatech.edu/McCarty-2024-Shanks.pdf
- https://arxiv.org/pdf/2106.09360
- https://arxiv.org/abs/0801.1059
- https://arxiv.org/pdf/2010.12661
- https://arxiv.org/pdf/1805.00157
- https://arxiv.org/abs/2311.10069v4
- https://arxiv.org/html/2304.10163v3
- https://link.springer.com/article/10.1023/A:1007597415185
- https://arxiv.org/pdf/2607.19946
