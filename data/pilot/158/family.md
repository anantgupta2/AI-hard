# Family 158: The Euclidean plane cannot be colored with five colors

Family analyst report. Influential-problems pass, 2026-10-10. Corpus `openai/math` at fd4aeeb. Manuscript: `preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026` (main.tex plus 7 section files, about 4.8k lines, 33 bib entries). There is no reasoning trace.

**Lean caveat:** this report works on the Lean code at the text level only. Following the instructions, I did not run `lake` or `lean`. The orchestrator compiles the comparators and records the result.

## 1. Main statement

> The Euclidean plane has no proper five-coloring, even when arbitrary color classes are allowed. Consequently, 6 ≤ χ(ℝ²) ≤ 7. (`sections/introduction.tex:62-68`)

**Paraphrase.** Every map ℝ² → {1,…,5} has a monochromatic pair at distance 1. Together with Isbell's 7-coloring, χ(ℝ²) ∈ {6, 7}.

**Lean comparator.** `OAI.EuclideanFiveColor.no_proper_five_coloring : ¬ ∃ c : ℂ → Fin 5, ∀ p q, ‖p - q‖ = 1 → c p ≠ c q`.
- Solution module: `OAI.Geometry.PlaneColoring.Five`.
- Permitted axioms: propext, Quot.sound, Classical.choice.
- The upper bound is a second comparator, `OAI.Problem160.properColoring_seven`.

**Match check: exact.** The comparator has no measurability hypothesis, and the norm on ℂ is Euclidean.

**Formalized:**
- the comparator;
- Thm 1.3, no weak five-coloring, for Borel c: `no_measurable_weak_five_coloring`;
- the forward transfer: `proper_to_borel_weak`;
- the rigidity theorem, stated as the vanishing of all nonzero Fourier coefficients: `wild_fourier`.

**Not formalized:**
- the converse transfer (it is not needed for the main theorem);
- Cor 1.4 (positive badness).

**An implied result the paper never states:** χ_m(ℝ²) ≥ 6. Every measurable proper coloring is a weak measurable coloring, so Thm 1.3 gives this at once. My searches found no improvement on Falconer's 1981 bound χ_m ≥ 5.

## 2. Trust surface
- **Grep, zero hits.** No `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `@[extern]`, `unsafe`, `opaque` or `maxHeartbeats` in the three directories:
  - PlaneColoring: 46 files, 14,661 lines;
  - PlaneSpectrum: 19 files, 8,466 lines;
  - CompactFactors: 14 files, 7,728 lines.
- **Imports.** Only Mathlib plus these three OAI directories.
- **`decide`.** About 86 kernel `decide` calls, all on finite label facts over Fin 3, Fin 5, Fin 6, Bool and Finset (Fin 5). The largest covers 5^6 = 15,625 tuples (`Exclusion.lean:60-63`, the five-cycle step-word lemma).

## 3. Computer-assisted status: **No**

The prompt asked specifically whether the proof is a de Grey-style SAT-certified graph. It is not. No finite 6-chromatic unit-distance graph is built, searched for, or verified.

| | de Grey 2018 / Heule 2018 / Polymath16 / Parts 2020 | Family 158 |
|---|---|---|
| Obstruction | finite UD graph, 1581 → 553 → 509 vertices (χ ≥ 5) | analytic, via the transfer theorem plus a measurable obstruction |
| Found by | hand + computer; SAT with unsat-core extraction | not by search |
| Certificate | SAT/DRAT refutation, or a human-verifiable case analysis (Parts) | 7-point rational interval certificate placing the **Moser spindle** (3-color obstruction) in a 3-label region, checked by hand in the paper (`angular.tex:619-773`) and in `Moser.lean` |
| Trust | SAT solver plus checker | Lean kernel; standard axioms; `decide` on ≤ 15,625 cases |

**Proof-complexity view.** There is no CNF refutation. The only finite combinatorial residue is a 3-coloring refutation of the 7-vertex Moser spindle, a few resolution steps. The rest is a roughly 30.9k-line Lean proof of a transfer theorem and a topological-measure obstruction.

Cor 1.4 needs a finite non-5-colorable graph H. It obtains one only existentially, by de Bruijn–Erdős. Its size |E(H)| is unknown, so δ = 1/|E(H)| is ineffective.

## 4. Labels
- **A5**, impossibility (high confidence).
- **B3**, partial progress on Hadwiger–Nelson: {5,6,7} narrows to {6,7}. B4 is an equally defensible reading.
  - The result is independent of de Grey; *full only with prior results* is no.
  - *Adds corollaries for other conjectures* is yes:
    - χ_m ≥ 6 (implied, unstated);
    - a transfer χ = χ_weak for every k;
    - positive five-color badness for the probabilistic Hadwiger–Nelson problem;
    - probably a computer-free χ ≥ 5 via Falconer plus the transfer (also unstated).
- **C3 primary.** The proof is by contradiction and non-constructive.
  - Secondaries:
    - C5: Bochner, SNAG, amenability, disintegration, Brouwer, ergodic decomposition;
    - C2: universal transfinite induction over a Furstenberg–Zimmer tower, and a van der Corput induction;
    - C4: collision counting, bounded distortion, Fourier decay;
    - C1: auxiliary placement only.
  - *computer-assisted* = **false**.
  - *ih_strengthened* = yes, by the template "strengthen to all substructures". The induction hypothesis ranges over all ergodic systems, maps and towers (`spectral.tex:341-346`).
- **D3, provisional, medium-low confidence.** It rests on I10, the rigidity of wild K-invariant laws.
- **E.**
  - Problem field: Combinatorics (05C15, 52C10).
  - Lean-dir field: Geometry/PlaneColoring, which imports Analysis/PlaneSpectrum and MeasureTheory/CompactFactors.
  - Method fields, essential:
    - ergodic theory;
    - abstract harmonic analysis;
    - real algebraic and number fields;
    - real analysis and GMT, plus Fourier decay;
    - circle dynamics (Sullivan bounded distortion);
    - algebraic topology and dimension theory;
    - probability;
    - discrete geometry.
  - Method field, corollary-only: de Bruijn–Erdős compactness.
  - That is 8 cross-field method areas. About 80% of the invoked theorems come from outside combinatorics.

## 5. Proof architecture

**Overall route:**

```
arbitrary proper 5-coloring
 └─ (I25) restrict to E = Q̄ ⊂ ℂ, Følner-average over E ⋊ K → invariant law on proper labelings
     └─ (I24) project label indicators onto continuous-translation factor (= conditional expectation)
         └─ residual spectral measure is K-invariant and gives C measure 0 ⇒ Haar (I10) ⇒ unit correlations survive
             └─ sample a jointly measurable field ⇒ weak measurable 5-coloring (I03)
                 └─ (I29) circle palettes; (I34) |P_x(e)| ≤ 2 via binary-center separation (I33)
                     └─ (I35, I36, I39) transition graphs are forests off a locally finite cyclic locus
                         └─ (I42, I43) thresholded disk averages: continuous map into K5 with tree-filled holes
                             └─ (I44) Lebesgue/Brouwer cover obstruction ⇒ non-null loop at a cyclic center (I45)
                                 └─ (I46–I48) label cycle + common exclusion continua K_j
                                     └─ (I49–I54) 5-cycle: word parity; 4-cycle: ray parity; 3-cycle: Moser spindle ⇒ ⊥
```

**Rigidity chain (I10):**
1. Null events (I11).
2. Invariant-mean line average vanishes (I13).
3. Relative singularity along a compact tower, by universal transfinite induction with phase-collision counting (I16, I18).
4. Conditional multiple averages for power maps (I19).
5. Radial subadditivity, w(|A−B|) ≤ w(A)+w(B), with w = −log m, from |A−Bu²|² = |−L+(A−B)u+Lu²|² (I20).
6. Number-field general position and capped residues (I21, I22) give m ≥ c on an interval of radii, contradicting step 2.
7. Hence all nonzero Fourier coefficients vanish, and the measure is Haar.

**Lean DAG.**
- 2,612 declarations; the target DAG has 2,329.
- Split of the target DAG: PlaneColoring 1,091, PlaneSpectrum 722, CompactFactors 516.
- Dominated shares:

| Declaration | Dominated share |
|---|---|
| `proper_to_borel_weak` | 0.52 |
| `no_measurable_weak_five_coloring` | 0.46 |
| `residual_fourier` | 0.44 |
| `fullApprox_exists` | 0.42 |
| `exists_terminal_factor` | 0.15 |
| `massReal_vanish` | 0.12 |
| `cyclicCore_compact_finite` | 0.10 |

- CompactFactors is Furstenberg–Zimmer background and should be excluded from the core.

**Lean vs paper.** The Lean follows the paper's route. The differences are:
- Packaging: a global `FullApprox` map, `commonInterface_graph_acyclic`, and a "no large positive region" contradiction.
- An invariant-mean "code" replaces ergodic decomposition.

## 6. Items (56; full list in family.json)

| Grade | Items |
|---|---|
| N0 | I01, I02, I06, I17, I18, I27, I41, I44 (Lebesgue covering), I46, I54 (graph), I55 |
| N1 | I07, I08, I09, I11, I12, I14 (moment-free median variant), I15, I19, I21, I22, I26, I28, I31, I32, I37, I38, I45, I47, I50, I53, L01 |
| N2 | I03 (weak coloring), I05 (as a theorem), I13, I16, I23, I24, I30, I33 (Sullivan/DKN, named), I34, I35 (BBM/Dávila-type interface density), I36, I39, I40, I42 (nerve map of a multiplicity-2 cover), I43, I48 (Sokolov–Voronov, named), I49 (named), I51, I52 (Townsend, named) |
| N3 candidates | I10, I25/I04 (joint with I10), I29 (weak), I20 (weak) |

## 7. Eureka candidates (provisional)

| Rank | Item | Prov. N | F | Nearest neighbour |
|---|---|---|---|---|
| 1 | **I10** rigidity of wild laws on the dual of discrete Q̄ (with I16, I20, I23) | N3 | F5 | Crum 1956 / Gneiting–Sasvári (radial measurable PD functions = continuous + c·δ₀), named by the paper as an analogue; BFLM-type stiffness on tori |
| 2 | **I25 + I24 + I03** forward transfer via the continuous-translation factor | N3 (joint with I10) | F5 | Bourgeat et al. 2015, Gwyn–Stavrianos 2020, Matolcsi et al. (averaging gives symmetry only); Payne 2009 (transfer fails for subgraphs) |
| 3 | **I29** circle traces and maximal palettes | N3 weak / N2 | F1 | Young measures, tangent measures, Falconer density points |
| 4 | **I20** radial identity giving the subadditivity of −log m | N3 weak | F2 | none found |
| 5 | **I16** relative singularity | N2 | – | Furstenberg 1977 tower induction (templated induction hypothesis) |

**Quick searches.** I ran WebSearch on 2026-10-10 for Crum's decomposition, Haar rigidity on duals of algebraic numbers and Bohr compactifications, transfers from arbitrary to measurable colorings, and measurable chromatic bounds.
- No match was found for I10 or for the transfer.
- The best known χ_m(ℝ²) is still Falconer's 5. The "≥ 6" hits concern the hyperbolic plane (DeCorte–Golubev).
- WebFetch is unavailable, so these rest on search summaries.

## 8. Correctness and trust concerns
- **Strength of the claim.** The claim is extraordinary: χ ≥ 6, implicitly χ_m ≥ 6, and an identification of χ with an almost-everywhere measurable chromatic number. It is consistent with known facts: χ ≥ 5, χ_m ≥ 5, and Payne's counterexample, which lacks full algebraic rotation invariance. Still, I10 needs expert reading.
- **Delicate points of I10 and I16:**
  - applying the universal induction hypothesis to a new system Z (`spectral.tex:476-486`);
  - choosing the fiber after fixing the bins;
  - measurable selections throughout.
- **Lean.** If the comparator compiles with only the standard axioms, the main theorem is machine-checked and these worries become exposition issues. Compilation is pending with the orchestrator.
- **Unstated corollary.** The paper never states χ_m ≥ 6, an odd omission. This is not a correctness issue.
- **SAT-style trust.** None of the SAT or DRAT trust issues apply.

## 9. Provenance (provisional)
No model-produced precedent was identified.
- **2025–26 citations:**
  - Sokolov–Voronov 2025 and Voronov 2025: human authors; they supply the strip and interface method precedents.
  - Matolcsi et al. 2025: human authors.
  - Jamneshan corrigendum 2026: journal.
  - Reed 2026: a GitHub manuscript claiming χ = 7. The paper critiques it and does not use it.
- **AI-related search.** Searching "Hadwiger–Nelson ChatGPT / GPT-5 / AI-assisted" found only the neural-network work of Mundinger–Pokutta et al. (arXiv 2501.18527) on variants. It is unrelated to this proof.

## 10. Extraction friction
- **Namespaces.** Problem160 and PlaneFiveColor are not family IDs.
- **Spread across directories.** The family spans 3 Lean dirs, one of which is general ergodic background.
- **Inline definitions.** Several definitions are inline `\emph`: typical, binary, state, split, triangle labels.
- **Extractor ranking.** The definition ranking puts plumbing first.
- **No WebFetch.** Literature checks rest on WebSearch alone.
