# Family 046: "Shafarevich counterexamples in dimension two and with large fundamental group" (family analyst)

Subject: Algebraic and complex geometry. There are two manuscripts, both at commit fd4aeeb:
- **S**: *A surface counterexample to Shafarevich holomorphic convexity* (2026-09-23), `preprints/A-surface-counterexample-…-September-23-2026/build/`, 6 sections and 27 bib entries.
- **F**: *A projective fourfold with large fundamental group and non-Stein universal cover* (2026-10-05), `preprints/A-projective-fourfold-…-October-5-2026/build/`, 7 sections and 31 bib entries.

There is **no Lean formalization** (`has_lean_doc` is False and there are no comparators), so the Lean sections and the trust-surface grep do not apply. The full item list (80 items, S01–S38 and F01–F42) is in `family.json`.

## Main statements
- **S, Thm main** (S: 01-introduction.tex:19-26). This is a smooth projective surface X with a connected nodal curve Z₀ of smooth rational curves such that im(π₁Z₀ → π₁X) is infinite.
  - A component of the preimage of Z₀ in X̃ is then an infinite connected chain of compact rational curves, an *infinite Nori string*.
  - Every hull containing one of its points is noncompact, so X̃ is not holomorphically convex.
  - So Shafarevich's conjecture fails in dimension 2.
- **F, Thm main** (F: 01-introduction.tex:105-114). This is a smooth projective fourfold X with **large** π₁, containing a simple abelian surface A with im(π₁A → π₁X) ≅ ℤ.
  - X̃ contains no compact positive-dimensional subvariety and is not Stein.
  - So the large-π₁ form fails (Kollár's formulation, "large ⇒ X̃ Stein"), and with it holomorphic convexity.
- **Relation between the two.** They are independent and use unrelated machinery. Neither cites the other.

## Labels
| Axis | Label | Notes |
|---|---|---|
| A | **A2** | Both headlines are existential counterexamples. |
| B | **B2** | Refutes. Flag *adds corollaries*: S is not special and not semialgebraic, and π₁ is non-linear. |
| C | **C1** primary | Secondaries: **C3** (GS counting; contradiction in the path lemma), **C4** (GS margin; hyperbolicity constants), **C5** (Stover–Toledo, Zarhin, SGA1, Hamm–Lê, Andreotti–Frankel), **C2**. |
| Computer-assisted | **No** | One hand-checkable rational inequality (S). The Frobenius cycle types (F) are asserted via weak approximation and never computed. |
| IH flags | ih_strengthened = **true** (F only) | Template: "carry an extra tracked quantity" plus "uniform/quantitative version". The path invariant carries a guide class modulo width-H ladders, and narrowing keeps the width uniform. |
| D | **D3, provisional, low confidence** | Rests on witness designs F14+F21 and S13, and on S27. See below. |
| Provenance | **partial** | S cites two OpenAI release preprints, OpenAIAbelianity2026 (family 057) and OpenAISemialgebraicCovers2026 (family 058), for **corollaries only**. The main theorems use no model-produced result. F cites none. |

**E. Fields**
- **Problem field:** AG/complex geometry. MSC 32Q30 and 14F35, plus 32E05/32Q28; F also lists 20F67 and 14K12.
- **Lean-dir field:** none.
- **Essential method fields:**
  - S: profinite group theory (weighted Golod–Shafarevich, Magnus); surface topology and monodromy; CM elliptic curves; AG (SGA1, normalization, resolution); real-analytic triangulation.
  - F: geometric group theory (Gromov hyperbolicity, hyperbolic cones); arithmetic ball quotients (Borel–Harish-Chandra, Baily–Borel, Stover–Toledo); number theory (Zarhin, Galois S₆); projective geometry (Lefschetz, Hamm–Lê, Godeaux–Serre, Atiyah flop); Stein topology (Andreotti–Frankel); orbifolds.
- **Corollary-only:** EKPR non-linearity; Campana special varieties; OpenAI 057/058.
- **Background-cited:** BK98, Eyssidieux–Funar, Kollár, Campana, Deng–Yamanoi, BBT.
- **Cross-field count (essential, non-AG):** 5.

## Proof architecture
**S (surface)**
1. **Witness family.** The Eisenstein curve E, multiplication by 4 and the sign quotient give spheres with 48 moving punctures. At s\* these collide in 24 pairs (S13, S14).
2. **Torus lift.** The 7-generator torus group F has weights (1,1,1,1,1,2,2). Corrected monodromy is **degree-raising** on the pro-2 Magnus algebra (S20). This is proved by three explicit invariant double covers Y_j² = q(z) − ω̄^j s, which show the action is trivial in degree one (S19).
3. **Core collapse.** Collapsing gives L, free pro-2 on 48 generators a_{h,j}, with pinched involution σ(a_{h,j}) = a_{b_j−h,j}⁻¹. The comparison with the actual sphere group runs through p: K → Π, which is surjective (S21–S23).
4. **Shift-adapted basis and involution relators.** The basis is u = δ_{T1}^i δ_{T2}^ℓ(a_{0,j}), with weights i+ℓ+1 (S25). On it, the **economical involution presentation** (S27) imposes σ-coinvariance with 24 relators of degree w_g+1, at cost tG(t).
   - The weight polynomials satisfy P = (1+t)G, with G = 3t(1+t)(1+t²)².
   - The mechanism: the Frattini differential d = u + u²∂_u + v²∂_v on 𝔽₂[u,v]/(u⁴,v⁴) satisfies d² = 0 and is acyclic.
5. **Infinite quotient.** All deep monodromy relators are added (cost 97t(4t)^J/(1−4t)), plus Golod high powers 2^e of the boundary meridians. At t = 49/200 the weighted GS sum is below −1/125, so the pro-2 quotient Q is infinite (S29–S35).
6. **Compact surface.** A finite quotient injective on every local boundary group gives a smooth projective cover X with ρ_X (S36). The distinguished fiber stays a nodal union of P¹s (S37). A deformation-retract neighbourhood transfers infinite image from a nearby fiber to a component Z₀ (S38). The Nori-string lemma (S07) then finishes.

**F (fourfold)**
1. **Reduction (F03, F06).** Take A ⊂ S′ with image ℤ, and a general complete intersection of c = d+2 sections of I_F ⊗ L^m in S′ × B, where B is an abelian 6-fold.
   - Lefschetz gives π₁(X) = π₁(S′) × ℤ¹².
   - An incidence count (4c = 4d+8 > 4d+6) leaves at most 3 points per fiber off A, which gives largeness.
   - X̃ ⊃ C²/ℤ³ ≃ T³×ℝ, which has H₃ ≠ 0. By Andreotti–Frankel it is not Stein.
2. **Local path criterion (F07–F12).** Suppose charts are uniformly hyperbolic and prefix-compatible up to radius N ≥ N₀(δ). Then a single-edge loop that does not close on reading is nontrivial modulo short closing loops.
   - Proof: guides (k-local geodesics), ladders, narrowing, and one-edge extension by minimization.
3. **Geometry (F13–F20).** Six real slopes have Galois group S₆, so by Zarhin Jac(C) is simple.
   - A Hermitian form over a CM field gives a cocompact arithmetic lattice in PU(4,1).
   - The 16-hyperplane arrangement D consists of two 6-slope pencils (4 red slopes with |λ| < 0.01, 2 blue with |λ| > 4) and coupling hyperplanes z₁ = ±c that meet only the red slopes.
   - Deep congruence levels give exact local copies of D.
   - Then come the Stover–Toledo sign covers, filling, V with F\* = C×C, the order-4 symmetry s, an ordinary resolution over o, and f: Y = Bl(Jac C) → 𝒮.
4. **Local labels (F21–F30).** Each finite model carries a local D_∞ label: red meridians go to r, blue to b, and coupling square roots modify it over the red disk.
   - Translation labels ℓ_z, ℓ_w extend over the fillings. The sum label is used at the centre.
   - Buffered kernel compatibility holds.
   - **Projected-diameter graphs** are uniformly hyperbolic, by quasi-isometry to a hyperbolic cone over the ideal arrangement complement.
5. **Infinite cyclic image (F31–F38).**
   - The coupling relations k·h_i = 1 make the image cyclic.
   - The pushed loop e has a nonzero sum label, and every power eⁿ is **one** non-closing edge.
   - All orbifold relations close in charts, so the path criterion gives that eⁿ ≠ 1.
6. **Back to the reduction (F39–F42).** A relative Godeaux–Serre construction gives a smooth projective fivefold. Atiyah-type ambient blowdowns then remove the point blowups, and step 1 applies.

## Eureka candidates, with a quick literature check
1. **F14+F21, the fourfold witness. Provisional N3, F3.** The design couples red and blue pencils so that coupling hyperplanes collapse the genus-2 surface group to the even part of D_∞. Local dihedral labels, which are not a global representation, then read the infinite part.
   - *For:* not in the goal or in L. It is the source of both the relations and the local covers.
   - *Against:* once D_∞ is chosen, the coupling hyperplanes are a short step. Arrangement orbifolds on ball quotients are classical.
   - Nearest neighbours: Stover–Toledo ramified covers; Eyssidieux 1611.09178 (Hirzebruch arrangement covers satisfy Shafarevich); BK98. None is equivalent.
2. **S13 cluster, the surface witness. Provisional N3, F3.** It is the genus-0 family with a torus lift and degree-raising pro-2 monodromy.
   - *For:* it makes the Bogomolov–Katzarkov route provably work. BK's infinitude was conditional, and Eyssidieux–Funar (2112.06726) showed most BK candidates *satisfy* the conjecture.
   - *Against:* the paper itself says it follows BK's "same broad passage", so the architecture is precedented.
3. **S27 (+S25), the economical involution presentation. Provisional N3 (weak), F5.** It is self-described as a reusable mechanism and produces the GS margin.
   - *Against:* Koch–Venkov (σ-inverted relators of Schur σ-groups lie deeper in the Zassenhaus filtration, which is how they beat plain GS) is the same family of ideas. Jennings bases are standard. Likely N2.
4. **F08+F26, the local path criterion with projected-diameter edges. N2.** It is a variant of Gromov's Cartan–Hadamard local-to-global theorem: Gromov 1987, the Delzant–Gromov orbifold version, Coulon 1302.6933, and DGO 1111.7048. Diameter edges amount to coning off bounded regions (Farb-style electrification). Still, it is the indispensable representation-free way to prove infinite order.
5. **F03+F06, the abelian-surface reduction / C²/ℤ³ obstruction. N2.** Given Andreotti–Frankel it is elementary. Neighbours are toroidal (Cousin) groups and the Nori-string obstruction. It is borderline analytic, being phrased in the goal's own vocabulary.

All other items are N0–N2. Examples:
- weighted GS, Golod powers, the Nori-string lemma, Bonk–Schramm cone and Stover–Toledo: N0;
- substitution, Frattini/Hopf, local detection, Godeaux–Serre realization and the arithmetic exact-arrangement proposition: N1;
- the degree-one lemma, monodromy raising, kernel compatibility and the ambient blowdown: N2.

## Correctness audit
I read both manuscripts in full and found **no definite gap**. These checks passed:
- **S arithmetic:**
  - P = (1+t)G.
  - G(49/200) ≥ 1.02817827 > 257/250.
  - The total sum is below −1/125.
  - The ranks are 97, 47, 48 and 4.
- **S algebra:**
  - The char-2 cyclic endpoint trick ((T′−id)⁴ = T′⁴ − id, with z₃ appearing once as the first letter).
  - The Frattini differential: d² = 0 and R = C ⊕ dC.
  - The weight-2 boundary estimate in S20.
  - The invariant double covers in S19.
- **F geometry:**
  - The coupling and slope incidences for 0.85 < c/√a < 0.9.
  - The rank-loss codimension 3 > 2 and the incidence count in the reduction.
  - The cyclic upper bound.
  - The normal-bundle bookkeeping in the ambient blowdown.

Consistency checks:
- **EKPR (fixed rank N) applied to F** forces some power of the generator e to die in every rank-N representation. Otherwise C²/ℤ³ would be closed in a holomorphically convex space with no compact curves, hence Stein. F's proof uses no representation, which is consistent. The paper understates this: no linear representation *can* detect e.
- **Treger (1008.1745, unrefereed)** says large plus residually finite implies Stein. If that holds, π₁ of F's fourfold is not residually finite, which is consistent with F avoiding finite quotients.
- **For S**, the infinite image is seen only through finite 2-groups of unbounded size, so fixed-rank EKPR raises no contradiction.

Residual concerns:
- **F, the global crux.** Lemma app:true-relations requires every orbifold relation to close in its chart, including at fixed loci of σ-powers away from Γo and at Γ₀o∖Γo. The argument is terse.
- **F, the path lemma.** It is a self-contained Cartan–Hadamard proof with "transport of competitors" shortcuts.
- **F, model hyperbolicity.** The quasi-isometry is sketched near the arrangement at infinity.
- **S, Lemma shift-basis.** The T₂ and σ propagation steps are two-sentence inductions.
- **S, chronology.** It cites the Sept-24 OpenAI semialgebraic paper from a Sept-23 preprint, which suggests co-development or a later revision.
- **Both.** These are extraordinary unrefereed claims against a 1972 conjecture, with no internal cross-citation.

## Extraction friction
- The two architectures are unrelated, so items need S/F prefixes.
- The witness objects, the shift basis, the dihedral labels, the projected-diameter graphs and the charts are all defined in prose or display math.
- Key sub-lemmas sit inside proofs: S26, and F06.
- `\emph` covers vocabulary such as red/blue, guide, ladder, central/individual model and pure.
- The model-produced citations appear only as `@misc` GitHub links in S's bib.
- There is no Lean DAG, so load-bearing judgements rest on the text dependency graph.
