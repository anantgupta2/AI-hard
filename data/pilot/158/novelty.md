# Family 158: novelty pass (influential-problems pass, 2026-10-10)

**Scope:** this pass worked at the text level. I did not compile the Lean; the orchestrator compiles the comparators. There is no reasoning trace and no F1 file.

## Provenance verdict: **no**
I found no model-produced precedent.
- **2025–26 citations.**
  - Sokolov–Voronov 2025 and Voronov 2025 (arXiv) are by human authors. They are method precedents for strips and interfaces.
  - Matolcsi–Ruzsa–Varga–Zsámboki 2025 is by human authors.
  - The Jamneshan corrigendum (ETDS, 2025/26) is journal material. Its corrected lemmas concern the spectral analysis of conditional Hilbert–Schmidt operators. The paper re-proves its own fiberwise version and does not rely on them.
  - Reed 2026 is a GitHub manuscript claiming χ = 7. The paper criticizes it and does not use it.
- **AI search.** Searching Hadwiger–Nelson together with ChatGPT, GPT-5 or AI-assisted turned up only Mundinger–Pokutta et al. (arXiv 2501.18527). That work uses neural networks to find constructions for coloring variants and is unrelated to any candidate.
- **Prior χ ≥ 6 or χ_m ≥ 6 claims.** None found. Erdős Problems #508 (edited January 2026) and Heule's FoCM talk both still treat 6 as open.
- **Method limits.** WebFetch to arxiv.org failed with ENOTFOUND. All AI-disclosure checks rest on search snippets, and acknowledgment sections were not read.

## Final grades

| ID | Candidate | N | F | Conf. |
|---|---|---|---|---|
| C1 | **Haar rigidity of wild K-invariant laws on the dual of discrete Q̄** (Thm 2.3, plus its engine) | **N3** | F5 | 0.45 |
| C2 | Forward transfer: proper → weak measurable coloring, via the continuous-translation factor | N3 (same device as C1; counted once) | F5 | 0.40 |
| C3 | Circle traces and maximal palettes P_x(e) | N2 | – | 0.55 |
| C4 | Radial identity, giving w(\|A−B\|) ≤ w(A)+w(B) | N3 (a sub-lemma of C1; not counted separately) | F2 | 0.30 |
| C5 | Relative singularity along the compact tower | N2 (templated-IH cap) | – | 0.65 |
| C6 | Transition graph Γ_x and avoiding traces | N2 | – | 0.60 |
| C7 | K5-valued approximants plus the Lebesgue/Brouwer cover obstruction | N1 (dimension-theory transfer) | – | 0.70 |
| C8 | Weak measurable coloring (definition) | N2 | – | 0.60 |
| C9 | Exclusion continua and one-sided strips | N2 (Sokolov–Voronov, Townsend named) | – | 0.70 |
| C10 | Binary-center separation | N2 (Sullivan/DKN named) | – | 0.70 |

## C1 in detail
**Statement.** Let E = Q̄ ⊂ ℂ be a discrete group, D its compact dual, C = j(ℝ²) the ordinary continuous characters, and K the algebraic unit rotations. Every K-invariant probability measure on D with ν(C) = 0 is Haar.

**Why it matters.** This is what allows an *arbitrary* proper coloring to be averaged and projected into a measurable one without losing the unit-distance exclusions.

**Test 1 (precedents).** No near-equivalent was found.
- **Crum 1956 and Gneiting–Sasvári 1999.** The paper names these as analogues: a measurable (radial) positive-definite function on ℝⁿ is a continuous part plus a null or δ₀ part. That is the same statement shape, but it needs Lebesgue measurability on ℝⁿ, which is exactly the hypothesis C1 removes. The proof methods do not overlap.
- **Measure rigidity** (BFLM 2011, Benoist–Quint, ×2×3, Einsiedler–Lind) concerns lattice or positive-entropy actions on tori and solenoids. It is a different setting.
- Searches covered Crum, Bohr/dual rigidity, positive-definite functions on Q̄, and BFLM. zbMATH was not queried.

**Test 2 (non-analytic).** Passes. Nothing spectral appears in the goal or in L, including the problem as originally posed.

**Test 3 (load-bearing).** Passes.
- `residual_fourier` has a dominated share of 0.44 and `wild_fourier` 0.41. The transfer `proper_to_borel_weak` has 0.52.
- Rigidity-specific code is about 40% of the non-background core.
- Knockout check: Payne 2009 shows that the transfer is false for smaller rotation groups.

**Test 4 (discoverability).** Protocol P-C1. Pivot distance is about 3 from L and chain depth is 3.

**Downgrade risk.** An expert might recognize C1 as "Crum on Q̄" or as a known rigidity result. A high hit rate in the directed arm of P-C1 would also count against it.

## Family verdict
- **family_D = D3, confidence 0.40.** It rests on C1, with C2 as the same device.
- **Falls to D2** if C1 has a precedent or is easy to rediscover.
- **Firms up** with a successful Lean compile, expert review and a low P-C1 hit rate.
- **Downstream.** C1 is a general statement about invariant laws. It could plausibly be reused for unrestricted-vs-measurable questions in ℝⁿ or for other distance graphs, which makes it a better speedup-test candidate than a one-off device. Corollaries such as χ_m ≥ 6 and positive badness do not count as reuse.

## Computer-assisted check
The proof is **not** a SAT-certified finite graph.
- **No finite graph.** No 6-chromatic unit-distance graph is built. Compactness implies one exists, but its size is unknown.
- **Finite residue.** The only finite parts are:
  - a hand-checked 7-point rational certificate placing the Moser spindle;
  - kernel `decide` over at most 15,625 label tuples.
- **Proof-complexity contrast.** The SAT route stalled at 5: Heule calls 6 a hard target. This proof skips the finite refutation entirely, much as an extended-resolution proof skips the exponential resolution proof. The analogy is qualitative, because there is no size measurement.

## Bridges

| Import | Classification | Note |
|---|---|---|
| Ergodic theory / harmonic analysis → *unrestricted* colorings | **new bridge** | Earlier uses were measurable-only (Falconer, FKW/Bourgain, Bachoc et al.) or symmetry-only (Bourgeat et al., Gwyn–Stavrianos). |
| Number fields | known route | — |
| Dimension theory / topology | known route (partial) | Woodall, Townsend, Sokolov–Voronov |
| Circle dynamics | minor new bridge | Sullivan/DKN |
| Circle Fourier decay | known route | — |

## Discoverability protocols

| Protocol | What is hidden | What the model gets | Arms |
|---|---|---|---|
| P-C1 | Sections 2–3 and everything downstream | the problem; Thm 1.3 as a black box; L | bare / L / directed |
| P-C2 | the transfer | C1 as a black box | — |
| P-C3 | the palettes | — | — |

- **k values:** 1, 5, 25, 100.
- **Models:** training cutoff before 2026-09-23. Exclude the OAI release.
- **Controls:**
  - Positive: Falconer's χ_m ≥ 5.
  - Negative: Payne's rational graph, which must fail.

## Open questions
1. Is C1 known to harmonic analysts?
2. Does Crum's paper state the exact radial δ₀ form?
3. What is the Lean compile result?
4. Why does the paper omit χ_m ≥ 6?
5. Does the result generalize to ℝⁿ?
6. How large is the finite 6-chromatic graph guaranteed by compactness?
