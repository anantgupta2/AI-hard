# Family 322: downstream analysis of C1 (Tingley's sphere-isometry problem)

**Item C1.** The opposite-endpoint return map g on extremal directions. Its Kuratowski contraction factor (1−M/r)(1−M/s) ≤ (1−M/(1+t))² < 1 comes from the hypothetical attained defect M, and Darbo's theorem then gives aligned chords. In the paper this is I10 + I15 → I16 (prop:alignment). Provisional grade: N3, F3 + F5.

**Date and scope.** 2026-10-12, text level only.
- No `lake build` or comparator run, because the checkout is shared. The Lean is trusted as published.
- arxiv.org is blocked. Several other hosts failed DNS (umj.imath.kiev.ua, dehesa.unex.es, nsysu). All literature is therefore at summary level.

The JSON twin is `downstream.json`, which also holds the verbatim Lean text.

---

## Part A: Is C1 in the Lean?

**`lean_status`: as in paper.**
- `ReturnMap.lean` defines exactly the paper's g (eq:return) and its radii p, s, u, r.
- Three files prove eq:contraction, the factor (1−M/(1+t))², and χ(gH) ≤ γχ(H) for every H ⊆ C:
  - `ReturnMapEstimate.lean`
  - `ReturnMapBounds.lean`
  - `ReturnMapNoncompactness.lean`
- `Alignment.lean` combines these with a re-proved Darbo theorem to obtain prop:alignment.
- `exists_alignedConfiguration` lies on the comparator's only path to M = 0.

### Key declarations
All live in `lean/OAI/Analysis/SphereIsometry/`.

| Declaration | File:line | Role |
|---|---|---|
| `pRadius, xPoint, sRadius, wDirection, uRadius, zPoint, rRadius, returnSphere` | ReturnMap.lean:69-106 | g and the four radii (I10) |
| `returnAmbient` (+ p/s/u/rAmbient) | ReturnMap.lean:265-279 | g totalized to X for Darbo |
| `extremalSphere`, `extremalSet` | ExtremalPropagation.lean:30-34 | E = {s − p = M} |
| `extremal_radius_identities` | ExtremalPropagation.lean:122 | r − u = M, forced triangle equality |
| `returnSphere_pair_estimate` | ReturnMapEstimate.lean:82 | eq:contraction |
| `return_coefficient_le` | ReturnMapBounds.lean:21 | up/rs ≤ (1−M/U)²: **the margin supplied by M** |
| `chi_return_image_le` | ReturnMapNoncompactness.lean:60 | χ(gH) ≤ (1−M/(1+t))² χ(H) (I15) |
| `exists_fixedPoint_of_return_estimate` | ReturnMapFixedPoint.lean:22 | a generic estimate implies a fixed point |
| `AlignedConfiguration`, `exists_alignedConfiguration` | AlignedConfiguration.lean:23, Alignment.lean:61 | prop:alignment (I16) |
| `exists_fixedPoint_of_kuratowski_contraction` | CondensingFixedPoint.lean:26 | Darbo, re-proved (N0) |

### Comparator chain
1. `tingley_sphere_isometry_full`
2. `extension`
3. `hasDefectBound_zero`
4. `maxDefect_eq_zero`
5. `no_attained_positive_defect`
6. **`exists_alignedConfiguration`**, which uses:
   - `exists_return_invariant_convex`. This is C2.
   - `returnSphere_pair_estimate`, through `returnAmbient_pair_estimate_on`.
   - `exists_fixedPoint_of_return_estimate`, which in turn uses:
     - `chi_return_image_le`;
     - `return_coefficient_le`;
     - Darbo.
   - `aligned_of_return_fixed`, built on `returnSphere`, `xPoint`, `zPoint` and the radius functions.

**Extractor cross-check** (`data/items/322_lean.json`):

| Declaration | Dominated share of the 579-declaration target DAG |
|---|---|
| `exists_alignedConfiguration` | 0.665 |
| `exists_fixedPoint_of_return_estimate` | 0.408 (mostly the Darbo stack beneath it) |

### Gaps between paper and Lean (none of them substantive)
- **Same route.** The comparator matches the headline exactly.
- **Totalization.** g becomes `returnAmbient`, which is 0 off the sphere, and is continuous only on the sphere.
- **Lean is cleaner than the paper.** `exists_fixedPoint_of_return_estimate` is **map-agnostic**: the hypotheses are only scalar relations and a two-point estimate. That makes it the natural library interface for reuse.
- **Darbo, Schauder and Brouwer are re-proved**, because Mathlib d13f23b lacks them. This is 39% of the DAG and is N0.
- **C1 runs on the completed-ultrapower isometry**, not on the original f. The paper does the same.
- **C1 needs C2's invariant convex set as input.**

---

## Part B: Where else could the device help?

### Bottom line
**No strong speedup candidate was found.**
- Every known theorem that the 322 Lean shortens dramatically is a *corollary of the Tingley theorem*.
- The known theorems that are *not* corollaries have one of two problems:
  - they need a quantitative re-proof of the device with ε-slack (S1);
  - they lack the antipodal / opposite-contact structure and the defect that C1 exploits (S3, S4).

**Risk.** C1 risks being a one-off device in the downstream test.

### Speedup targets (known theorems)

| # | Target | Helps by | Speedup | Conf. | Lean |
|---|---|---|---|---|---|
| S1 | Vestfrid: ε-isometries of S(ℓ2^n), S(ℓ∞^n) (UMJ 2020) and S(ℓ1^n) (Colloq. Math. 177, 2024) are C(n)ε-close to linear isometries | An ε-slack version of the margin argument could give one dimension-free proof. Gap: approximately radial T does not yet give a nearby linear isometry | low–med | 0.25 | statable now |
| S2 | Darbo for maps that are Lipschitz up to the oscillation of finitely many bounded scalars (Banaś–Goebel-type applications) | `exists_fixedPoint_of_return_estimate` applies verbatim, but this reuses only the N0 shell | low (device) | 0.6 | statable now |
| S3 | Leung–Ng–Wong: positive-sphere Tingley for L^p and C(K) (TAMS 2025) | Probably nothing: −w leaves the positive cone. A soft negative control | low / none | 0.1 | statable now |
| S4 | Hammer 1954: every interior point lies on an affine diameter | Template only (aligned chord = fixed direction). There is no defect, so there is no margin | low | 0.1 | < 300 lines |

### Open problems

| # | Problem | Status | Match to C1 | Conf. | Lean |
|---|---|---|---|---|---|
| O1 | **Dimension-free stability of Tingley:** a surjective ε-isometry S_X → S_Y lies within Cε^α of a linear isometry | open (as found) | **Exact.** Without compactness, M is the only source of margin. Uses ultrapower attainment, χ-contraction with an O(ε) error, approximate alignment, then a quantitative contradiction | 0.3 | statable now |
| O2 | Phase-isometries between unit spheres (the Tan–Huang question) | open; class-wise results, with a gap flagged by Enami–Matsuzaki 2026 | Partial. Mostly a theorem-corollary use, but the opposite-contact step is sign-symmetric, so a run with a sign-invariant defect is testable | 0.25 | statable now |
| O3 | Tingley for boundaries of convex bodies (Mankiewicz-type, Cabello Sánchez 2019) | open (unverified) | Radial contacts generalize to gauges, but the 322 defect needs a fixed centre. Finding the centre is outside C1 | 0.15 | statable now |
| O4 | Positive Tingley for Banach lattices / ordered Banach spaces | open in general | Weak: no antipodes | 0.1 | statable now |
| O5 | Quasi-Banach Tingley (0 < p < 1) | open in general | Supports and Schauder/Darbo fail. Expected to fail, so it doubles as a control | 0.1 | < 300 lines (quasi-norm) |
| O6 | Local Tingley: isometries between relatively open subsets of spheres | unverified | Poor: C1 needs the global defect bound and f⁻¹ | 0.1 | statable now |
| O7 | Figiel-type left inverse for *into* sphere isometries | unverified | C1 needs f⁻¹ at the opposite contact | 0.1 | statable now |
| O8 | Affine diameters through interior points in infinite dimensions | unverified (own formulation) | Template only, with no margin source | 0.1 | statable now |

### Theorem corollaries (show reach; not device reuse)
- The Mazur–Ulam property for every real Banach space.
- Tingley 1987 antipodality.
- Kadets–Martín (polyhedral) and Banakh (2D).
- Class results:
  - Ding;
  - Tan;
  - Fernández-Polo–Peralta;
  - Mori;
  - Mori–Ozawa;
  - Fakhoury;
  - Maślany;
  - Huang–Zhu ×2.
- Object-level rigidity in all dimensions, which contains Nakamura–Tanaka 2609.31096.
- The extension half of the phase-isometry results.

### Release reuse
**None.**
- No OAI file outside the family imports `OAI.Analysis.SphereIsometry`.
- The preprint grep for Darbo, Sadovskii and noncompactness hit only "Darboux".

### Negative controls
1. **Into-isometry into ℓ∞ (proved false).** The map Φ(x) = (1, (‖x−a_n‖−1)_n) is an isometry S_X → S_{ℓ∞} with no linear extension. C1 fails at `zPoint := f.symm …`, so surjectivity is essential.
2. **The Mazur map S(ℓ_p) → S(ℓ_2) (proved-false uniform analogue).** C1 needs exact distance preservation to force r = u + M.
3. **Complex conjugation on S_ℂ.** The device can only ever give real-linearity.
4. **Mankiewicz / Mazur–Ulam.** The device is unnecessary here, so expect zero speedup. This is the baseline.

### Top 5 (all Lean-usable)
1. **O1, ε-stability.** This is the only target that needs C1's specific content and is not settled by the theorem. The ε-slack refactor costs about 400 lines.
2. **S1, Vestfrid's finite-dimensional theorems.** The measurable instance of O1: Darbo reduces to Brouwer and no ultrapower is needed.
3. **O2, phase-isometries.** An active literature with a concrete sign-invariant adaptation.
4. **S2, the generic Darbo shell (calibration).** It separates the transfer speedup (Darbo available) from any C1 speedup.
5. **O3, convex-body boundaries.** It tests the scope of the device. It will probably fail at the centre-finding step.

## Precedent
- **After 2026-10-06:** nothing found.
- **Earlier equivalent:** none found.
  - The nearest work is Nakamura–Tanaka, which uses Plücker contraction bodies and has no return map or Darbo.
  - Other neighbours are the facial methods (close to C2) and affine-diameter arguments (template only).
- **Verdict: no downgrade.** The caveat is that the full texts of Tingley 1987, Kadets–Martín 2012 and Cabello Sánchez 2019 are still unread.
