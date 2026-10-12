# Family 322: novelty pass (Tingley's sphere-isometry problem)

## Full-text re-check (2026-10-12)
arXiv was reachable via curl. I searched 15 full texts for fixed-point|Darbo|Schauder|Brouwer|Kuratowski|noncompact|Sadovskii|invariance of domain|condensing|contraction and read the relevant sections. Per-paper entries and quotes are in `novelty.json` → `verified_checks`. I also ran abstract searches through the arXiv API, e.g. Darbo with isometr*, and "fixed point" with Tingley or Mazur-Ulam. None returned anything relevant.

**What the full texts show**
- **No prior Tingley or Mazur-Ulam work uses a fixed-point theorem.** None uses Darbo, Schauder, Brouwer or a Kuratowski χ. This covers:
  - Kadets-Martín 1206.4839, whose method is differentiability of f and F plus Tingley's Mankiewicz-on-facet-cones step;
  - Peralta's survey 1801.02473;
  - Mori 1712.09192 and Mori-Ozawa 1804.10674;
  - Cueto-Avellaneda-Peralta 1803.00604 and 1903.11917;
  - Banakh 2103.09268 and Banakh-Cabello Sánchez 2103.09266;
  - Cabello Sánchez 1810.02461;
  - Fakhoury 2412.00891;
  - Huang-Zhu 2607.11244 and 2608.30131;
  - Nakamura-Tanaka 2609.31096.
- **"Fixed points" appear only as fixed-point *sets*.** In Cabello Sánchez Thm 3.11 and in Ma, the set {τ(x) = x} is shown to be clopen. That is a different argument.
- **New nearest neighbour, not cited by 322: Ma, arXiv:2609.25065 (15 Sep 2026).** It treats 3-dim Tingley, partially.
  - It uses chord-direction maps (x−a)/N(x−a), common supports, invariance of domain, and a clopen fixed set of L⁻¹f.
  - It has no f-driven self-map of directions, no defect-supplied contraction and no Darbo. It works in finite dimension only.
  - It has no AI disclosure, but its "ongoing proof search" status note suggests machine assistance.
- **AI disclosure.**
  - Nakamura-Tanaka 2609.31096 declares **explicitly** that it used OpenAI ChatGPT (GPT-5.6 Sol and GPT-6 Astra) for proof strategies and Lean. It postdates 322 and shares no device.
  - Huang-Zhu ×2 and Fakhoury carry funding acknowledgments only.
- **Still unread:** Tingley 1987 and Ding's 2009 survey. Neither is on arXiv. Every description of Tingley 1987 attributes to it only antipodality and facet-cone linearity.

**Effect on the grades**
- **C1 stays N3 (provisional).** Confidence rises from 0.45 to 0.50, because downgrade risk (ii) is largely discharged. Test 4 and the expert query are still open.
- **family_D stays D3 (provisional).** Confidence rises from 0.45 to 0.50.
- **Provenance flag stays "no".**
- **Contamination cutoff:** prefer models whose cutoff is before 2026-09-15, and exclude GPT-5.6 Sol and GPT-6 Astra from the controlled arms.
- **C4:** ultraproducts already appear in the Tingley literature (Fernández-Polo-Peralta 1709.08529). C4 stays N1.

*The original pass follows. Where it says that arXiv was unreachable, that is superseded by this section.*

Date: 2026-10-12. Inputs: `family.json`/`.md`, `main.tex` (Sections 1-5 read in full), `references.tex`, and the Lean declaration names in `lean/OAI/Analysis/SphereIsometry`. This family has no trace and no F1 files. Per PLAN (2026-10-12), the Lean is trusted as published; it was not built here.

**How the evidence was gathered**
- WebFetch failed with DNS errors on every host I tried: arxiv.org, alphaxiv, ar5iv, ugr.es and wikipedia. curl to arxiv.org got a proxy 403.
- So every literature claim rests on WebSearch summaries plus my own domain knowledge. No quote is verified, and no full text of a precedent was read.

## Provenance verdict: **no**
- **Cited 2025-26 works.** There are three, all class-specific, and none contains any candidate:
  - Fakhoury (arXiv:2412.00891, JFA 2025): Schreier spaces;
  - Huang-Zhu (arXiv:2607.11244): Schatten classes;
  - Huang-Zhu (arXiv:2608.30131): Haagerup L_p.

  Search summaries mention no AI assistance. That is unverified, because the abstract pages could not be fetched.
- **An uncited 2026 neighbour.** Nakamura-Tanaka (arXiv:2609.31096, 25 Sep 2026, two days after the manuscript) proves that isometric spheres imply linearly isometric spaces in finite dimension. That is the object-level question, *not* the extension of a prescribed isometry. Their method uses "Plücker contraction bodies" and has no return map and no Darbo.
- **Model-produced prior work.** Searches for Tingley together with ChatGPT, GPT-5, OpenAI or "AI-assisted" found none. OpenAI's 1 Aug 2026 "Ten advances" snippets do not mention Tingley.

## Final grades
| ID | Candidate | N | F | Conf. |
|---|---|---|---|---|
| C1 | Opposite-endpoint return map with self-supplied Kuratowski contraction, giving aligned chords (I10+I15→I16) | **N3** (provisional) | F3 + F5 | 0.50 (was 0.45) |
| C2 | Extremal common-support propagation and the invariant convex face (I11, I12, I28) | N2 | – | 0.6 |
| C3 | Secant cancellation lemma (I18) | N2 | – | 0.5 |
| C4 | Cross-radius defect with ultrapower attainment (I07-I09) | N1 | – | 0.65 |
| C5 | Chord contradiction: large regime by signs and perturbation, small by convexity (I19-I21) | N2 | – | 0.5 |
| C6 | Re-proved stack: χ, Darbo, Schauder, Sperner/Brouwer, Hahn-Banach, Mazur-Ulam | N0 (transfer) | – | 0.95 |

**family_D = D3 (provisional), confidence 0.50 (was 0.45), resting on C1 alone.**

It falls to D2 in any of these cases:
- P-C1 arm B shows that pre-cutoff models find the device;
- the unread full texts (Tingley 1987, Kadets-Martín 2012, Ding's survey, Cabello Sánchez) turn out to contain a return or fixed-point device on chords;
- an expert names a known Darbo/Sadovskii argument for sphere isometries.

## Candidate notes

### C1: return map with self-supplied contraction (N3 candidate)
**What it is.** Assume a positive maximal defect M is attained at (x₀, y, t). The return map g works on directions at ty:
- go to the sphere contact x = ty+pv;
- apply f, giving tb+sw;
- take the opposite contact tb−uw;
- pull back to z and reverse, giving g(v) = (ty−z)/r.

On the extremal set E = {s−p = M}, extremality forces r = u+M. The Lipschitz factor is then up/rs = (1−M/r)(1−M/s) ≤ (1−M/(1+t))² < 1. So **the hypothetical defect supplies the contraction margin** that Darbo needs. Binning the scalars p and u turns this into χ(gH) ≤ γχ(H), and a fixed point gives aligned chords.

**Test 1: no near-equivalent found.**
- Darbo and Sadovskii are ingredients (N0 transfer).
- Genuinely different:
  - the finite-dimensional arguments of Tingley 1987 and Kadets-Martín 2012 (compactness or topology; I could not verify which);
  - Banakh's planar "special points";
  - Mori-Ozawa's Mankiewicz-for-balls.
- The facial methods (Cheng-Dong, Tanaka, Mori) are close to C2, not C1.
- The nearest cross-field principles, both template-level only:
  - affine diameters and critical points of convex bodies (Klee, Grünbaum, Guo-Tóth), where a chord with parallel supports at both ends is an analogue of the aligned chord;
  - Kirk/Sadovskii minimal invariant convex sets.

**Test 2: passes.** Neither the goal nor any statement in L mentions g, opposite contacts or χ in a form that can be instantiated.

**Test 3: passes.**
- `exists_alignedConfiguration` dominates 55% of the core (66% of the whole DAG).
- 28-31% of core declarations depend on `pRadius`/`xPoint`.

**Against.**
- Every component is classical, and the contraction is two triangle inequalities.
- Once "aligned chords" is posed as the target, the fixed-point move may be one step away (arm A).
- It may be a one-off device in the downstream test.

### C2: invariant convex face (N2)
- The common support is a face of the ball, and the paper itself notes its "geometric affinity with facial methods" (Tanaka 2014 Lemma 3.5).
- Hull growth is a sequential Sadovskii/Kirk invariant-set construction.
- The IH "conv{v₀..vₙ} ⊂ E" is a templated strengthening (all substructures), which caps it at N2.

### C3 and C5: secant lemma and chord contradiction (N2)
- The weighting u·Δₓ + s·Δ_z cancels the unknown target norm, because sr−up = Md. It is clever, but it is elementary convexity and first variation at an extremum.
- Lean replaces the small-regime argument with two vector identities.

### C4: defect plus ultrapower (N1)
- **Analytic:** D_q is the difference of the goal's two sides once T is unfolded.
- The natural homogeneous extension is the standard object of the Tingley literature.
- Ultrapower attainment is textbook local theory (Heinrich, Heinrich-Mankiewicz, Dacunha-Castelle).

### C6: N0 transfer
- 39% of the Lean DAG re-proves Kuratowski, Darbo, Schauder and Sperner, which Mathlib d13f23b lacks. This share of the core is 0%.

## Bridge novelty
| Import | Status |
|---|---|
| Fixed-point theory (χ, Darbo, Schauder) → Tingley / sphere isometries | **New bridge (no precedent found)**, at summary level. It is recorded separately and is not by itself the jump. |
| Sperner → Brouwer → Schauder | Known route, used for self-containment |
| Banach ultrapowers → isometry problems | Known route (Heinrich-Mankiewicz 1982) |
| Supports and facial geometry; Mazur-Ulam | Known, in-field |

## Discoverability (Test 4, not run): protocol P-C1
- **Models:** training cutoff before 2026-09-23, the manuscript date (and before 2026-09-25). Use a canary probe on "is Tingley solved in general?". Exclude the OpenAI models behind the release. No retrieval.
- **What to hide:** I10-I16 and everything downstream (Sections 4-5).
- **Arms:**
  - **A, pivot:** gives I01-I09, Darbo and the *statement* of prop:alignment.
  - **B, decisive:** gives I01-I09 only, with the goal "an attained positive defect is impossible".
  - **C, bridge:** arm B with Darbo and Kuratowski removed from L.
- **Hit:** a direction self-map through f and opposite sphere contacts, *plus* a strict set-contraction on an invariant convex set of extremal directions, so that a fixed point gives chords with s−p = r−u = M. A return map with no contraction margin, or a fixed point valid only in finite dimensions, is partial credit.
- **Sampling:** k = 1..256, n = 256 per arm.
- **Controls:** the Cook PHP extension variables as the positive control; C4 and C3 as negative controls.
- **Pivot distance:** ≥2 in arm B and about 1 in arm A. Chain depth is 2.

P-C2 and P-C3 are in the JSON.

## Open questions
- Read the full texts of Tingley 1987, Kadets-Martín, Ding's survey and Cabello Sánchez for any fixed-point or return device.
- Verify the AI disclosures for 2607.11244, 2608.30131 and 2609.31096.
- Put an expert query to Peralta, Mori, Banakh, Cabello Sánchez and Kadets.
- The claim is extraordinary and unrefereed. Correctness rests on the trusted Lean.
- Downstream reuse candidates:
  - ε-isometry / Figiel-type stability on spheres, where the margin is quantitative in M;
  - Mankiewicz for boundaries of convex bodies;
  - phase isometries;
  - quasi-Banach spheres.
