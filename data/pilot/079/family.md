# Family 079: Local smoothing in three dimensions

**Manuscript:** *Critical local smoothing for the three-dimensional wave equation* (OpenAI, September 24, 2026).
**Location:** `preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/`, with `main.tex` and 11 section files totalling 12,654 lines, plus `references.bib` (35 entries).
**Subject:** Real and complex analysis.

There is no Lean formalization and no reasoning trace. All extraction comes from the LaTeX alone.

**Reading depth.**
- Read line by line: Sections 0–2, 9 and 10, and the closing proofs of Thm 2.4 (06:1083-1276) and Thm 8.1 with its descent lemma (08:1384-1471).
- Read at statement level, with spot proofs: Sections 3–8, about 9,350 lines.
- This is not a verification.

## 1. Main statement

> **Theorem 1.1 (Critical local smoothing)** (00-introduction.tex:25-32). For every ε>0 there is C_ε with ‖Uf‖_{L³(ℝ³×[1,2])} ≤ C_ε‖J^ε f‖_{L³(ℝ³)}.

In words, the half-wave e^{it√−Δ} at the critical exponent p = 3 = 2n/(n−1) loses only ε derivatives.

Corollary 9.6 interpolates this with L² and with an L^∞ kernel bound. It gives the full strict range 2<p<∞, α>max{0,1−3/p}, which is Sogge's Euclidean conjecture for n=3. The lossless endpoint ε=0 is explicitly not claimed (00:46).

**Corollaries, all via cited implications (Sec. 10):**
- the maximal half-wave bound and a.e. convergence (BHS survey, eq. 3.24);
- maximal Bochner–Riesz for p≥3, δ>1−3/p, and the nonmaximal Bochner–Riesz conjecture in ℝ³ (BHS Props 3.2/3.3);
- spherical extension L^r→L^r for r>3 (Tao 1999);
- the Kakeya maximal L³ estimate (Wolff 1999).

If the paper is correct, it settles all of these in ℝ³.

**Relation to prior work.**
- Guth–Wang–Zhang settled the 2+1 case.
- Bourgain–Demeter covers p≥4 in 3+1.
- Gao–Liu–Miao–Xi reach α>1/9 at p=3.
- Gan–He–Li–Wu v2 (Jan 2026) give the sharp gain for p≥10/3, hence α>1/12 at p=3.
- Rozendaal–Schippa (Aug 2026) reach α>2/9 for rough coefficients.

The paper uses GWZ's **2+1 wave-envelope theorem as an input**, applied to parabolic-cylinder sections. GWZ is a tool here, not a special case of the result.

## 2. Trust surface
- There is no Lean, so the grep for sorry/axiom/native_decide is not meaningful (0 hits in the .tex).
- The paper is not computer-assisted: no search or numerics.
- Trust rests on an unrefereed 12.6k-line argument.

## 3. Labels

| Axis | Label | Evidence | Conf. |
|---|---|---|---|
| A | **A3** (outer A1), explicit rate: no | "For every ε>0 there exists C_ε" (00:26) | high |
| B | **B1**; full-only-with-prior: no; adds corollaries: **yes** (Bochner–Riesz, restriction, Kakeya maximal, maximal wave) | "these estimates resolve Sogge's Euclidean local smoothing conjecture in three spatial dimensions" (00:44-45) | high as a claim |
| C | **C3** primary; secondaries C4, C5, C1, C2. Computer-assisted: no. ih_strengthened: no; ih_template: n/a | "The model bounds are proved by contradiction." (00:259) | med-high |
| D | **D3 (provisional)** | The entropy-excess potential (§5) | low |
| E | Problem field: Real/complex analysis (MSC 42B37, 35L05, 42B15, 35B65). Lean dir: none. Method fields: see below | | high |

**Notes on C.**
- C2 appears only as a backward induction over a finite mesh (02:751) and as an induction over peeling levels.
- There is no induction on the estimate. The role of induction on scales is played by the extremal exponent Γ.
- The extremizer is then enriched lexicographically, by minimal mass exponent p and then minimal shear costs c and c₁. This resembles the template "carry an extra tracked quantity", but it is an extremal selection, not a strengthened induction hypothesis.

**E. Method fields.**

Essential:
- decoupling / square functions (GWZ Thm 1.3);
- incidence geometry / GMT (Ren–Wang Thm 4.1);
- information theory (entropy, mutual information, KL divergence);
- probability (replicas, disintegration);
- wave packets and Schrödinger coherent states;
- conformal geometry of the wave equation (Bateman 1909);
- real analysis (Lipschitz profiles, Arzelà–Ascoli, differentiation);
- the finite Ramsey theorem;
- descriptive set theory (analytic sets; Bertsekas–Shreve).

Corollary-only:
- the Bochner–Riesz, restriction and Kakeya implication chain (BHS, Tao, Wolff).

Background-cited:
- Hochman–Shmerkin local entropy averages, which the paper names as the analogy for its "names";
- Wang–Zahl Kakeya;
- broad–narrow methods;
- earlier local-smoothing papers.

Of the 5 invoked theorems that are essential for the headline, 3 come from other fields (Ren–Wang, Ramsey, Bertsekas–Shreve).

**Provenance flag: partial.**
- The paper cites OpenAIBochnerRiesz2026 (family 078) only for comparison: "That article is not an input to the deduction above" (10:138-141).
- It does not cite the same-release sibling **074** (*Kakeya maximal conjecture in three dimensions*, Sept 23). 074 shares the architecture: a critical exponent, equality configurations, a "canonical profile", conditional coordinate entropies in two frames, Ren–Wang projections, and product-slope pinning adapted from Shmerkin–Wang.

## 4. Proof architecture
1. **Annular reduction (Sec. 9).** It suffices to prove ‖W_H g‖₃ ≤ H^{-δ}‖g‖₃ on one frequency annulus. Null coordinates (t,b,y)=(τ+x₃, x_⊥, τ−x₃) make the wave a free round-cone (Schrödinger-type) wave.
2. **Input regularity.** Bounded-amplitude pieces of the L³ data give energy e≲‖g‖₂² and κ = H^{-γ}B² on all round and null-hyperquadric tests, with weight r⁴f^{1−η}. The synthesis lemma gives ∫|v|³ ≲ H^{-1/2}Σm^{3/2}. Together these reduce everything to the normalized cubic functional 𝓑_s.
3. **Thm 8.1 (round Γ ≤ 100η), by contradiction.** Take the extremal data (p,d) with Γ = d+(1−p)/2; saturation then gives E_a = e s^{-da} and κ_a = κ s^{pa}.
4. **Thin shapes become cylinders (Prop 7.x).** A conformal chart flattens a null hyperquadric, so thin round packets become classical or hybrid parabolic-cylinder experiments. In the hybrid case the normal fibre carries a 1-D Schrödinger evolution.
5. **Thm 2.4 (cylinder Γ ≤ η/2).** The steps are:
   - matched gates with shear compatibility (M);
   - the Planck floor;
   - minimal shear costs c and c₁, then Lipschitz width profiles;
   - shape constraints b₂(i) ≥ c(i−1), giving affine profiles (F).
6. **Zero-cost exclusion (Sec. 3).**
   - Hybrid case: the GWZ wave envelope gives a kinetic estimate, combined with the scalar channel and memory bounds.
   - Classical case: a conditional Ren–Wang bootstrap gives D′(a) ≥ 1+3d, which contradicts D(1) ≤ p+d = 1+3d−2Γ.
7. **Positive cost (Secs 4–6).**
   - Define canonical names 𝒞(a,v) and the entropy excess E(a,v) = 𝓗 − D₀ − (p+d)a − W ≥ 0, with E = 0 at label-recoverable boundary points.
   - Conditional replicas and walks, the projection rule and the radial dichotomy give rate inequalities. These lead to the **local actions (∂_a − k∂_v)E ≥ 2Γ**.
   - A path that follows them backward from the boundary drives E below 0, a contradiction.
   - A case analysis over c, J, q and d completes the argument.
8. **Round labels at the uncertainty scale (Sec. 8).**
   - Define the excess E = D − 4v − (p+d)a ≥ 0, with E(a,u(a)) = 0.
   - Outgoing entropy: o_T ≥ 4d + min(1−d, m/2), from four transverse pins, Gram–Schmidt and a Ramsey colouring.
   - The classical case closes by integration and the wave case by the two-direction descent lemma.
9. **Corollaries (Secs 9–10).**

## 5. Eureka candidates (provisional)

| # | Item | N | F | For | Against |
|---|---|---|---|---|---|
| 1 | **Entropy-excess potential.** E(a,v) ≥ 0 with zero boundary trace, transport inequalities (∂_a − k∂_v)E ≥ 2Γ, and a path contradiction (P54+P68+P72; round versions P86+P88) | N3 cand. (borderline N2) | F4 (name: F1) | Non-analytic; it closes every positive-cost and round case; the paper itself calls it the one quantity estimated | Hochman–Shmerkin is named as a precedent for the records; 1-parameter branching-function arguments are standard; sibling 074 is architecturally the same |
| 2 | **Lexicographic extremal reduction.** Minimal p, then minimal shear costs c, c₁, giving affine width profiles (P21, P23, P30–P33) | N2 | F2/F4 | Pins the geometry | Wang–Zahl worst-case exponent; Orponen–Shmerkin ε-linear profiles; the "minimum-delay canonical profile" of 074 |
| 3 | **Hybrid cylinder + conformal thin-shape transfer** (P13, P77) | N2 | F5 | Makes GWZ (2+1) usable in 3+1 | Lorentz rescaling and cone-to-cylinder reductions are standard; Bateman 1909 |
| 4 | **Outgoing entropy via transverse pins + Ramsey** (P87) | N2 (borderline N3) | F3 | The single inequality that closes the round case | Shmerkin–Wang / OSW radial-projection pinning, which sibling 074 cites |
| 5 | **Rarity transport (Sp)**, the energy-to-probability bridge (P34) | N2 | F2 | Lets entropy arguments run on masked quantum evolutions | Short consequence of the extremal tail bound |

**Quick literature check** (WebSearch, Oct 2026). No 2-parameter entropy-excess potential with transport inequalities was found. The nearest neighbours are:
- Orponen–Shmerkin branching functions (arXiv 2106.03338);
- Hochman–Shmerkin 2012;
- the Wang–Zahl worst-case exponent, as described in Guth's Bourbaki survey;
- the same-release papers 074/077/078.

## 6. Items
`family.json` lists 87 items. In summary:
- the framework lemmas are N0/N1;
- the model definitions (P13, P14, P75) and the extremal-reduction propositions are N2;
- the lower-dimensional inputs are N0 (GWZ, RW), with their probabilistic and Hilbert-valued forms N1;
- the canonical name P52 is N2 (F1 if upgraded);
- the excess and surplus package (P54, P68, P86) is an N3 candidate (F4);
- the physical reduction and corollaries are N0/N1.

## 7. Correctness concerns
- **Extraordinary scope.** One unrefereed, model-produced paper claims to settle local smoothing, Bochner–Riesz, sphere restriction and Kakeya maximal in ℝ³.
- **Fragile limit ordering.** The argument depends on exponent closures and ordered limits; extremal configurations exist only in the closure. The text itself warns about diagonal-limit failure modes (01:229-238, 299-305).
- **Long case analysis.** The proof of Thm 2.4 splits into many regimes (06:1083-1276). A missed regime would be fatal.
- **The hybrid quantum model.** Entropy arguments run on artificial classical rays extended backward from quantum samples (04:36-41). They are justified only by the Planck floor, and positivity of phase-space laws is explicitly not claimed.
- **What did check out.** Exponent algebra, the closing inequalities of Thm 8.1, the descent lemma, the synthesis lemma, the predecessor-volume lemma, the Ren–Wang exponent match, the Gaussian randomisation, and the corollary chain.
- **Shared-machinery risk.** Siblings 074/077/078 share the toolkit, so an error in a common tool would propagate across all four papers.

## 8. Extraction friction
- There is no Lean.
- Key objects are equation tags rather than environments: (M), (A), (B), (F), (Pl), (Sp), (canon), (surplus), (excess), (round-out).
- Symbols are heavily overloaded (D, J, E, H, p).
- Several definitions sit inside proofs.
- The cylinder and round developments run in parallel.
- Vocabulary is shared with families 074/077/078.
