# Family 358: novelty analysis ("A three-manifold without conjugate points or nonpositive curvature")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

Inputs:
- `family.json`/`.md`. There is no trace and no `f1_*` file for this family.
- The preprint source. I read the introduction, cometric and variations sections; the others I took from family.json.
- `lean/docs/358.md` and the release README (author: "OpenAI").
- Web checks of IK, Burns–Matveev, Leeb, Croke–Schroeder, Gulliver and the convexity sources. For Leeb and Burns–Matveev, WebFetch saved the PDFs and I extracted the text locally, so quotes from those two are verified.

**L** = Mathlib d13f23b plus the 8 bibliography entries. None of them is model-produced and none dates from 2025–2026. L contains **no** convex-analysis or calculus-of-variations source.

## 1. Provenance verdict: **no**

- **Bibliography.** All 8 references date from 1963–2021: Milnor, Gulliver, Leeb, Kapovich–Leeb, Bridson–Haefliger, Bonahon, IK, and BM (ETDS 2021 = arXiv 2013). The arXiv abstract pages of IK (1205.4455), BM (1308.5417v3) and Leeb (dg-ga/9410002) carry no AI statement.
- **Recent work on the topic.** The only 2025–2026 items I found are Tchuiaga arXiv:2504.07616 (2025, product rigidity for *closed* Σ×S¹, genus ≥ 2) and Pardo-Guerra–Washburn arXiv:2607.22594 (scalar convex actions). Neither discloses AI use on its abstract page, neither is cited, and neither contains any candidate item.
- **Model-produced prior work.** WebSearch for the problem together with ChatGPT/GPT-5/OpenAI/AI-assisted found no model-produced precedent and no prior resolution.
- The 358 preprint itself is authored "OpenAI". It is the object under study, not a precedent.

## 2. Final grades

| ID | Item | Grade | Confidence | Reason |
|---|---|---|---|---|
| C1 | Returning-passage free-endpoint index estimate (P29 + P24–P28, P13; Lean L08) | **N2** | 0.6 | No neighbour found, and it is load-bearing by knockout (cone 0.131). However, its statement is the goal's own index-nonnegativity predicate, localised, with endpoints freed and made uniform. That is a templated strengthening (by analogy), so it is capped. Its proof is elementary once C2 and C3 are given. The analyst's "N3 weak" is withdrawn. |
| C2 | Concave cometric ⇒ coordinate second variation E ≥ 0, plus an engineered boundary sign (P19/P20, P23) | **N2** | 0.7 | The core is **N0 transfer**: concave P = Q⁻¹ ⇔ the geodesic Lagrangian is jointly convex ⇔ the Hamiltonian is concave in position (Rockafellar 1970; Kiefer 1959 / Lieb–Ruskai 1974). The design of the end germs (P′(0) = κe₁e₁ᵀ) is new. |
| C3 | Concave neck path with δ/δ² scaling and the period trick B₁ = δ²B₂ (P11, P05, P10, P13) | **N2** | 0.65 | Necks between flat tori and period choices are standard. Sol is a neck with a *convex* cometric. The ordering is a bespoke F3-type gadget, driven by C2. Dependents share 0.215. |
| C4 | Localisation to passages with independent gauges (P31) | **N1** | 0.6 | Additivity of the index integral plus pointwise tangential invariance, both in L. |
| C5 | (Lean) cyclic shear obstruction in CN spaces (L05) | N2 | 0.6 | Close variant of Leeb Ex. 4.1 / Kapovich–Leeb, with flats avoided. |
| C6 | (Lean) fibre nontriviality via essential closed geodesics (L03) | N1 | 0.65 | Morse–Hedlund / Hadamard–Cartan applied to the paper's own metric. |
| C7 | Topological obstruction (P04, P07–P09) | **N0** | 0.95 | It is Leeb 1995 Example 4.1. I read Leeb's text: NPC holds iff the gluing preserves {±b, ±f}, proved by orthogonality of the splittings. |

No candidate earns an F type; none is N3.

## 3. Family verdict

**family_D = D2, confidence 0.6.**
- **What it rests on.** It rests on C1, C2 and C3, all N2. No item passes Tests 1–3 cleanly:
  - C1 fails Test 2: it is a goal-shaped strengthening.
  - C2's core fails Test 1: it is classical convexity.
  - C3 is a gadget built to satisfy hypotheses that C1 and C2 set.
- **Path up to D3** (F5, on the *cluster* C2+C3, mirroring 287's coupling argument). Two conditions must both hold:
  - (i) an expert confirms there is no prior Riemannian use of a convex-Lagrangian or concave-cometric certificate for no conjugate points;
  - (ii) Test 4 (the P-C2 open arm and P-C3) gives a hit rate below threshold.

  Transfer alone cannot give D3.
- **Path down to D1.** This needs a prior concave-inverse-metric neck *and* C1 being judged routine. Both seem unlikely.
- **Change from the analyst.** family.json had provisional D3 at low confidence, resting on P29. It had flagged this same downgrade risk.

**The result is important but the machinery is N2.** The paper answers IK Q1.1/8.1 and Burns–Matveev Q4.1.2 negatively; both have been open since 2012–13. BM say "the problem is still open even in dimension 3". The difficulty looks architectural: an NPC-obstructed Leeb manifold, plus a neck certified by a convexity bridge, plus free-endpoint passage estimates. It does not sit in a single non-analytic item. Two cautions about scope:
- IK's "simplest test case" Q8.2 (|tr A| > 2) is **not** settled. The gluing here has trace 1.
- All grades assume correctness. Lean was not built.

## 4. Precedent checks (summary)

- **Ivanov–Kapovitch (1205.4455).**
  - It is the problem source. It suspects a negative answer in general, "but might hold in dimension 3".
  - Q8.2 asks about a |tr| > 2 gluing and proposes no construction.
  - It has no necks, no convexity of the inverse metric and no positive-curvature regions.
  - All candidates are absent. Quotes are via the summariser and unverified.
- **Burns–Matveev (1308.5417v3).** Q4.1.2 reads: "If (M,g) has no conjugate points, does M carry a metric with non-positive sectional curvature?" This is verified from the extracted text. It points only to group-theoretic necessary conditions (Croke–Schroeder, Lebedeva, IK). All candidates are absent.
- **Leeb Ex. 4.1 (dg-ga/9410002, read).**
  - Equivalent to C7 and a close variant of C5.
  - The existence constructions glue NPC pieces along *isometric* flat tori, with no interpolating neck. So C1, C2 and C3 are absent.
- **Croke–Schroeder 1986 (via IK and Dibble; not opened).**
  - For analytic metrics, abelian subgroups are straight and solvable subgroups are virtually abelian. Lebedeva and Dibble later completed this for all metrics.
  - These are necessary conditions only, and 358's π₁ satisfies them.
  - They also explain why Sol-type necks fail. Sol's cometric diag(e^{−2t}, e^{2t}) is *convex*, the opposite of 358's.
- **Gulliver 1975 (full text 403; method via Dibble).** It inserts a positive-curvature cap with radial comparison. That is a different mechanism and the nearest classical neighbour for C1.
- **Joint convexity / calculus of variations.**
  - The relevant sources are Rockafellar (PJM 1970; Convex Analysis Thm 33.1), the joint convexity of y ↦ yᵀP⁻¹y (Kiefer 1959; Lieb–Ruskai 1974), and textbook sufficiency for jointly convex problems.
  - The derivation (mine): yᵀP⁻¹y = sup_p(2pᵀy − pᵀPp). If P(t) is concave, this is a supremum of functions convex in (t,y), so it is jointly convex. 358's E is exactly the second derivative of the coordinate energy along affine variations.
  - The paper never names this. I found no Riemannian use of the criterion; the dynamics papers I found (CIPP 1999, Lee 2012) *assume* there are no conjugate points.
  - Side fact (mine): in dimension 2, a concave cometric forces K ≤ 0 (f″ ≥ 3f′²/f). So the device produces positive curvature only through the 2×2 shear, which may be why it went unused.

## 5. Bridge novelty

| Import | Into | Verdict |
|---|---|---|
| Convex analysis / CoV (jointly convex Lagrangian, concave–convex Hamiltonian, matrix-fractional convexity) | Riemannian construction without conjugate points (C2) | **New bridge, no precedent found** (confidence 0.5; the implication is textbook, so a folklore use is possible) |
| CAT(0) geometry (flat torus theorem, axis shifts) | obstruction (C7) | known route (Leeb; Kapovich–Leeb) |
| Hyperbolic punctured torus with cusp | product cores | known route |
| H₀¹ duality, Schur complement | C1 | generic technique (Lean removes it) |
| Morse–Hedlund / Hadamard–Cartan | C6 (Lean) | known route |

## 6. Discoverability protocols (not run)

**Models.**
- Training cutoff before 2026-09-24, with no exposure to the openai/math release.
- Use a canary probe on IK Q8.1 and on "concave cometric".
- No tools.
- The producing OpenAI model(s) run only as an upper-reference arm.

**Arms.**
- **L:** the problem plus L.
- **L+:** adds Rockafellar and the matrix-fractional lemma.
- **open:** the problem only.
- **directed:** gives Leeb's manifold, NPC pieces and the neck ansatz dt² + dxᵀQ(t)dx.

**Sampling and judging.**
- n = 256 per arm, with pass@k for k = 1…256.
- Two LLM judges plus an expert check.
- Lean equivalence against `energy_nonnegative`, `uniform_cometric_bounds` and `returning_arbitrary_field_nonnegative`.

**Per-item protocols.**
- **P-C2.**
  - Hide: P19, P20's sign clause, and the concavity requirement in P11/P13, plus everything downstream.
  - Hit: any condition equivalent to concavity of Q(t)⁻¹ (or joint convexity of yᵀQ(t)y, or a Hamiltonian concave in t).
  - Pivot distance 2 from L (1 in L+); chain depth 1.
- **P-C3.**
  - Give: C2 and the end-sign requirement.
  - Hit: an explicit concave path with exact product germs, end slopes that are positive multiples of e₁e₁ᵀ, and a realisation of the integral gluing. Linear interpolation alone is a miss.
  - Pivot distance 1 given C2; chain depth 2.
- **P-C1.** This is a proof-completion task.
  - Give: C2, C3, P22, P23 and the target.
  - Hit: a complete argument that is uniform in L. Also record the three ingredients (control of e-only by the boundary term, the |p₁|-relative mixed bound, the timing margin).
  - Pivot distance about 3 from L; chain depth 3.
- **P-C4 and P-C5** are short, k up to 64.
- **Controls.** Positive: Cook–Reckhow ER. Negative: C4 and C7.

## 7. Open questions
1. Expert query: is a convex-Lagrangian or concave-cometric certificate for no conjugate points folklore? This decides whether the C2 bridge is new and whether a C2+C3 cluster can be N3.
2. Does the same neck handle IK Q8.2 (|tr A| > 2)? If so, that is a natural target for the downstream speedup test.
3. Build the Lean files.
4. Open Kapovich–Leeb 1996, Buyalo–Svetlov and the full text of Gulliver 1975.
5. `docs/templates.md` does not exist. The cap on C1 is applied by analogy and needs ratification.
6. zbMATH, MathSciNet and Google Scholar were not queried.
7. The IK quotes are unverified (they came through the summariser).
