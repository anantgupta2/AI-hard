# Family 368: The three-dimensional Ball–Evans approximation problem

Analyst role: family analyst, working from the papers only. This family has no Lean formalization and no reasoning trace. Date: 2026-10-09. Machine-readable version: `family.json` (93 items).

**Manuscripts.** The two are logically independent; each says it does not use the other.
- **M1:** *Strong diffeomorphic approximation in three dimensions for 1 ≤ p ≤ 2*. About 5,000 lines: intro, smoothing, low-exponent tools, low-exponent assembly, conclusion.
- **M2:** *Strong diffeomorphic approximation in three dimensions for p > 2*. About 10,500 lines: intro, high-exponent preparation, quantizers, walls, mesh, high-exponent assembly, and an appendix duplicating M1's smoothing section.

File references are written `M1:` or `M2:` plus a path relative to that manuscript's `build/` directory.

**L** = Mathlib d13f23b plus the two bibliographies (41 + 50 entries; 58 distinct keys). In practice L is the bibliography, since Mathlib has none of this Sobolev-homeomorphism, 3D PL topology or GMT machinery.

## Main statement

> Let Ω,Λ⊂ℝ³ be nonempty bounded connected open sets, let 1≤p≤2 [M2: 2<p<∞], and let f:Ω→Λ be a homeomorphism in W^{1,p}. There exist C^∞ diffeomorphisms f_j:Ω→Λ in W^{1,p} with ∫(|f_j−f|^p+|Df_j−Df|^p)→0.

Sources: M1:sections/01-introduction.tex:29-34 and M2:sections/01-introduction.tex:25-35.

**Paraphrase.** Every finite p ≥ 1 is covered, the target is fixed, and no boundary regularity, inverse regularity or Jacobian sign is assumed. This answers Ball–Evans affirmatively in 3D. Hencl's 2025 survey lists 3D as open. In dimension ≥ 4 the answer is negative for p < ⌊n/2⌋ (Campbell–Hencl–Tengvall).

**Lean.** None. The trust surface (sorry/axiom grep) is not applicable, so everything rests on unreviewed LaTeX.

## Labels

| Axis | Label | Conf. | Evidence / note |
|---|---|---|---|
| A | **A2** | medium | ∀f ∃(f_j), following the 173 convention. A1 is the alternative reading ("diffeomorphisms are dense"). No explicit rate. |
| B | **B1** | high | "We resolve the three-dimensional Ball–Evans approximation problem" (M1:main.tex:54). Full only when the two OpenAI manuscripts are combined; no prior results are needed. By-product: strong approximation by PL homeomorphisms. |
| C | **C1** primary; C4, C5, C3 secondary | high / medium | C1: approximants are constructed. C4: long order-of-choices estimation chains. C5: heavy cited topology and GMT (Hamilton/Moise, Edwards–Kirby, Smale–Hirsch, Ahlfors–Bers, CHM, Alberti–Marchese, De Philippis–Rindler, Dehn, loop theorem). C3: probabilistic selection, and the guard barrier argues by contradiction. |
| C flags | computer-assisted **no**; ih_strengthened **no** | high | The only induction is a finite-stage bookkeeping induction in the PL library construction. |
| D | **D3 (provisional, low)** | low | Rests on M2's guard-pinned wall-realization cluster. See below. |
| Provenance | **no** | high | The only 2025–26 citations are the Hencl survey and Campbell–D'Onofrio–Vítek (both human), plus course notes. The companions cite each other but neither uses the other. |
| E | Problem field: PDE (OpenAI subject); MSC 46E35, 30C65, 74B20, 57K30. Lean dir: none. Method fields: Sobolev maps, 3-manifold geometric topology, GMT, quasiconformal maps (p=2), differential topology (immersions), convex analysis and power diagrams, probability (LLL, Markov), uniform convexity, free-group theory. | | Topology dominates the method fields. Cross-field count ≈ 9. |

## Proof architecture

**Common to both manuscripts: smoothing.** A locally bi-Lipschitz W^{1,p} homeomorphism is taken first to a PL map, then to a diffeomorphism, staying onto Λ:
- **Finite PL libraries.** Normalized local H-maps are binned into finitely many classes. One Hamilton-PL model is chosen per class *before* the mesh resolution is chosen. This fixes the derivative bounds M_P before the bad-cube volume is made small (M1:02-smoothing.tex:612-968). The paper names Väisälä 1977 / Carleson as precedent.
- **PL to smooth.** This uses edge tubes, variable-radius convolution (det is affine along rank-one face jumps) and a Smale isotopy at vertices.
- **Fixed target.** A degree argument shows the map is onto Λ.

**M1 (1≤p≤2): budgets of measured traces.**
1. Select compact jet sets by rank, with a small tail.
2. **Tie budget and softmax squeeze.** Count crossings of f-images of random source edges (and faces when p=2) with the barycentric "leader-tie" dual strata of a random target triangulation. Clean these crossings topologically, then squeeze the target by T_i = λ_i e^{aλ_i}/Σλ_j e^{aλ_j}. As a→∞, image lengths and areas converge to the flat budget, and the expected budget is ≤ C∫|Df|^p (M1:03-low-tools.tex:1232-1651).
3. **Rank 3.** Radial blocks recover the jets. Identity germs are installed by a star-replacement argument (Dehn's lemma, punctured-sphere mapping class group). At p=2 this also needs reverse rays (CHM inverse-BV) and angular attenuation with a first-power envelope.
4. **Ranks 1 and 2.** Kernel directions are compressed onto line or plane sections. Anisotropic Kuhn grids give near-sharp budgets (1+Cη).
   - Rank 1 uses the identity ∫|u′−e|² = s²+1−2e·d, which works at p=1.
   - Rank 2 at p=2 uses a sharp boundary-parametrized disk estimate (Ahlfors–Bers uniformization and coordinate rigidity).
   - Rank 2 at p<2 uses planar radial blocks.
5. Uncontrolled cells are filled by radial collapse, which works because p < cell dimension. The errors are summable; then smooth.

**M2 (p>2): carrier, quantizer, walls, guards.**
1. **Preparation.** Regular points exist for p>2. The decomposability bundle (Alberti–Marchese) plus the converse to Rademacher (De Philippis–Rindler) give a direction transverse to the rank-1/2 image. A thin-band collapse flattens that data onto plates, and protected double wells are placed there.
2. **Exact carrier F_b.** This is a continuous proper W^{1,p} surjection that is exactly affine or PL off a set of arbitrarily small residual target volume.
   - It is built from an **immersed-cubical-skeleton cutoff**: a near-identity map is lifted through a Whitney-layered immersion of the 2-skeleton at a common scale s. The volume factor (ℓ/s)³ against the overlap count (s/ℓ)² makes the energy sum, with a universal constant.
   - The uncontrolled hole fillings are collapsed to points, leaving ball fibres that are opened topologically later.
   - For 2<p<3, marked cubes with small collar budgets are added.
3. **Convex quantizer T = (∂G)⁻¹.** G is a sup of c-convex quadratic supports. A Poisson perturbation forces all contacts into the exact region.
   - T is Lipschitz onto Λ. Its 3D input blocks lie in exact regions, and elsewhere its output lies on a 2-complex with orthogonal product fibres.
   - The retained gradients sit on protected rectangular faces, carried by two polar labels (t,s).
4. **Walls.** In the graph-handlebody exterior (H₂=0, irreducible), level annuli A_D(t) and meridian disks B_e(s) are pulled back to the source and normalized à la Haken without raising any wall–edge count. They are thickened into pre-stacks with parameter slope density G, and made near-sharp on calibrated islands by canonical snapping and broadening.
5. **Routing.** Diagonal regular exchange conserves parameter length, and the oriented periods agree with the standard walls (via H₂=0).
6. **Guards.** Reference fibre paths are fixed after prior capacities for ∫G^p. A misplaced realized label forces ∫G^p ≳ a h^{2−p} → ∞ (p>2, oscillation on 2-spheres), contradicting the capacity. The realization theorem then yields a locally bi-Lipschitz h whose labels are pinned.
7. **Final map P₀∘T∘h.** Its derivative depends only on the label slopes (±du_j or ±(du_k−du_j)), never on Dh. A sharp energy bound plus the pinned mean gradient give strong convergence by uniform convexity. Then strictify, compress the marked cubes, smooth, correct the reserved full-rank cubes with the smooth cutoff, and smooth again.

## Items (highlights; all 93 are in JSON)

**Provisional grades**
- **N0/N1:** The cited topology and GMT, regular points, compact jets, radial collapse, crossing cleaning, Haken normalization, uniform convexity, and all bookkeeping.
- **N2:**
  - smoothing with libraries (M1-07, M1-14; Väisälä precedent)
  - sharp disk estimate (M1-17; Morrey precedent)
  - tie budget and squeeze (M1-27–29; Federer–Fleming/White precedent)
  - radial blocks, kernel compression and the thin-grid sharp coefficient (M1-32, M1-36, M1-39)
  - flattening (M2-04, M2-06; AM Lemma 7.5)
  - immersed-skeleton cutoff (M2-08/09; Kirby torus trick, not cited)
  - affine implant (M2-12) and carrier (M2-13)
  - quantizer (M2-17/19; Moreau, Aurenhammer)
  - routing (M2-29; Haken)
  - snapping (M2-46)
- **N3 candidates:** guards and barrier (M2-31, M2-34), wall realization (M2-36), and label-only parameter cost (M2-37). F5, with F3 for the guards.

## Eureka candidates (with quick literature check, 2026-10-09)

1. **Guard-pinned wall realization; energy through labels only** (M2-31/34/36/37). Provisional N3 (weak), F5.
   - *For:* The two labels of a 2-complex-valued map are realized topologically as level walls of a homeomorphism, and pinned by reference fibre paths through a capacity barrier. This decouples the energy from the derivative of the homeomorphism, so no quantitative 3D extension theorem is needed.
   - *Against:* Every ingredient is classical: oscillation on spheres for p > n−1, intersection numbers, Haken exchange. Planar scalar-coordinate approaches exist: IKO's coordinatewise p-harmonic replacement, and Ntalampekos 2019 on level sets of monotone functions.
   - *Search:* No match for level-set or label pinning in 3D.
2. **Immersed-skeleton cubical cutoff** (M2-08/09). N2, leaning N3; F3.
   - *For:* It gives a universal-constant energy cutoff via Whitney-scaled immersion lifting plus collapse of the hole fillings.
   - *Against:* Lifting through an immersion is Kirby's torus trick (Edwards–Kirby is cited only for M1-08). The novelty is the quantitative scaling.
3. **Tie budget plus softmax simplex squeeze** (M1-27/28/29). N2, F3.
   - *For:* It realizes a Federer–Fleming-type deformation count by an injective target homeomorphism.
   - *Against:* The paper itself cites White 1999 Prop 2.2.
4. **Convex product quantizer with Poisson contact exclusion** (M2-17/19). N2. The paper names Moreau and Aurenhammer.
5. **Finite PL libraries before resolution** (M1-14). N2. The paper names Väisälä 1977.

## Correctness and trust

Checked by hand and found correct or consistent:
- the M2-09 energy series, Σ(λ/s)³(s/λ)²;
- M2-12, where the condition number cancels;
- injectivity of the strict quantizer T_η;
- the guard-barrier arithmetic, with blow-up exactly when p>2;
- the sharp disk rigidity, where 2·Area ≤ 2+o(1) forces the X and Y energies to ≈1;
- the rank-one identity;
- consistency of the library models on good cubes;
- the coherence of the split at p=2 (area controls face energy only when p ≤ 2).

Concerns:
- **Size and opacity.** About 15k lines, with dozens of order-of-choice dependencies. Circularity is explicitly addressed (Remark ha:scale-order) but cannot be fully verified here.
- **Relative topology.** Relative forms of Hamilton's approximation, Edwards–Kirby and Smale–Hirsch are asserted, not quoted.
- **Conditional realization.** Theorem wl:realization is conditional, with its hypotheses discharged in Secs 8–9.
- **Terse injectivity proof.** The injectivity proof for the variable-exponent squeeze is terse.
- **Status.** This is an extraordinary claim on an open problem, unreviewed and unformalized; expert review is needed.

## Extraction friction

- The smoothing section is duplicated across the manuscripts, and labels collide (`main:theorem` appears in both).
- Few `\emph` definitions. The key objects (carrier, guards, softmax squeeze, walls) are defined in prose or inside proofs.
- The architecture is an order of choices, not a lemma DAG, and one theorem is explicitly conditional on later sections.
- Precedent cue phrases are plentiful and were used for the N2 caps: "classical precursor in Morrey", "appear in Väisälä's implementation of Carleson's method", "central to polyhedral deformation; see White", "graph-parametrized form of Alberti–Marchese's Lemma 7.5", "related to regular exchange", "following Haken", "planar construction of Hencl–Pratelli".
