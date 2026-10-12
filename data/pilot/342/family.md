# Family 342: Donaldson's tamed-to-compatible conjecture

This is a FAMILY analysis of the paper and the Lean, done at text level. This agent did not build the Lean: the checkout is shared, so the orchestrator compiles the comparator.

- **Corpus:** `openai/math` at fd4aeeb.
- **Manuscript:** `preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/`. It has 8 sections and 1,919 TeX lines. A September-23 version also exists; see §7.
- **Reasoning trace:** none.
- **Machine-readable version:** `family.json`, with 32 paper items and 3 Lean-only items.
- **Companion:** family 341 (Donaldson's hypersymplectic conjecture) reuses this paper's machinery.

## 1. Main statement

- **Paper, Thm 1.1** (`sections/01-introduction.tex:23-27`): if a smooth almost complex structure J on a closed connected 4-manifold is tamed by a symplectic form, then some smooth symplectic form is compatible with J.
  - J is fixed.
  - The cohomology class of the compatible form is free. The paper explicitly does not claim that every taming class contains a compatible form.
- **Secondary results (Sec 8, not formalized):**
  - **Thm 1.2** describes the cones:
    - K^t = C + H_J^-;
    - K^c = {a ∈ C : a·y > 0 for all 0 ≠ y ∈ closure(C)}, where C = K^t ∩ (H_J^-)^⊥.
  - **Cor 1.3:** if h_J^- = b^+ − 1, then K^t = K^c + H_J^-. When b^+ = 1, this gives K^t = K^c.
  - **Example 8.6:** a flat T^4 where the inclusion K^c + H_J^- ⊆ K^t is strict.
- **Comparator** (`ComparatorChallenges/TamingCompatibility.lean`): `OAI.TamingCompatibility.taming_implies_compatibility`.
  - Hypotheses: X is compact, T2, second countable and connected, and is a C^∞ 4-manifold.
  - Statement: `(∃ α, IsSymplectic α ∧ Tames α J) → ∃ η, IsSymplectic η ∧ Compatible η J`.
  - Permitted axioms: propext, Quot.sound, Classical.choice.
- **Match check: exact for Thm 1.1.**
  - `Model.lean` is textually identical to the challenge definitions.
  - `IsClosed` and `IsSmooth` quantify over all smooth maps from open subsets of R^4. This is equivalent to dα = 0 and smoothness.
  - `Compatible` = `Tames` ∧ `IsInvariant`, which is the paper's notion.
  - I found no loophole.

## 2. Trust surface

The grep covered 582 files and 83,060 lines.
- Zero hits for: `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `ofReduceBool`, `partial def`.
- There is no `set_option` of any kind.
- There are 32 `decide` uses, all trivial (`2 ≠ 0`, `(0:Fin 2) ≠ 1`).
- The only imports are Mathlib and the family's own files.
- **Compile status: pending (orchestrator).**

## 3. Labels

| Axis | Label | Conf. | Evidence |
|---|---|---|---|
| A | **A2**: ∀ tamed J ∃ compatible ω. The witness is *not* constructed. Thm 1.2 is A4 | 0.75 | intro:23-27 |
| B | **B1**: answers Donaldson 2006, §5.2 Q2. Adds corollaries: the cone theorem, the b^+=1 class equality (previously claimed by TWZZ2022, whose estimates Lin–Zhou 2025 questioned), and use by 341 | 0.8, conditional on correctness | intro:12-21 |
| C | **C3** primary: contradiction via Hahn–Banach separation. Secondaries: C4 (mass, kernel and angular estimate chains; the critical r^{-3}·O(r²)·o(r)) and C5 (Hahn–Banach, Melrose/Taylor ΨDO, Ludewig heat kernel, Radon-measure differentiation) | 0.85 | intro:135-189; concl. |
| C2 flags | No induction: ih_strengthened = no | — | |
| Computer-assisted | **no** | 0.95 | |
| D | **D2 (provisional)**. The max item is Thm 5.1 (density splitting) at N2, N3-borderline | 0.5 | 05-density:32-37 |
| Provenance | **no**. The only OAI citation is companion 341, which depends on *this* paper | 0.9 | bib |

**E: fields.**
- Problem field: Differential geometry (MSC 53D05, 32Q60).
- Lean dir: Geometry.
- Method fields, essential:
  - functional analysis (Hahn–Banach, cone duality);
  - elliptic PDE / ΨDO calculus;
  - spectral theory / heat-kernel asymptotics;
  - semiclassical commutators;
  - GMT (currents, Lelong–Jensen monotonicity, tangent measures);
  - measure differentiation;
  - Riemannian normal coordinates.
- Method fields, other tags:
  - Hodge theory and the intersection form: essential for Thm 1.2, corollary-only for Thm 1.1;
  - pluripotential theory (Lamari, Buchdahl, Elkhadhra) and pseudoholomorphic curves (Gromov, Taubes): background-cited only.
- About 6 cross-field method fields. Roughly 80% of the invoked external results come from analysis, not geometry.

## 4. Proof architecture

1. **Separation** (Prop 2.2). Suppose no compatible form exists.
   - A probability measure λ on unit complex-line bivectors gives a positive current P that kills closed invariant forms.
   - The closed lift B = dd*G + H (Lemma 2.1; Lejmi's operator R dd*) gives T = P + Q, which kills all closed forms. Q = −P(BR·) is anti-invariant and therefore **self-dual**: the 4-dimensional input.
2. **Quadratic mass growth** (Prop 3.1): μ(B_s) ≤ Cs², obtained by testing P on the closed invariant radial forms (1−BR)dd^c_J u, with u = log√(s²+t²) and √(s²+t²).
3. **Energy** (Sec 4).
   - S_r = (1+r²Δ)^{-3}. Its kernel is a positive part p_r times parallel transport, plus an error.
   - The exact identity ⟨ℓ,*τm⟩ = ½|ℓ−τm|² − ¼|F−τF|² turns the self-pairing into c·r^{-4}·I_r minus a bounded shell error.
   - The mixing lemma gives ‖Π S_r W‖ ≤ Cr‖S_r W‖.
   - Expanding 0 = ⟨S_rT,*S_rT⟩ gives Q ∈ L², the angular bound I_r ≤ Cr⁴, and vanishing mixed terms.
4. **Density** (Sec 5).
   - θ = lim r^{-2}μ(B_r) exists everywhere, by Lelong–Jensen almost-monotonicity.
   - At positive-density points the tangent currents are planar. Hence the transverse moment N_r = o(r²).
5. **Thm 5.1: P_E = 1_{θ>0}P is closed** (Sec 6).
   - Use the smoothed density f_r and closure on d(h_r dz_j).
   - Tangential derivatives become δ·|z^⊥|/r.
   - Cauchy–Schwarz bounds the boundary term by r^{-3}√I_r√N_r = r^{-3}O(r²)o(r) = o(1).
6. **Residual pairing** (Sec 7).
   - T' = T − P_E is closed, and 0 = ⟨S_rT,*S_rT'⟩.
   - The positive factor P' lives on zero-density centres, so the negative error → 0.
   - Hence ‖Q‖² ≤ 0, so Q = 0. Then P = T kills the closed tamer, a contradiction.
7. **Cones** (Sec 8): prescribed-class separation, then the same estimates, the residual pairing against arbitrary positive currents, and the T^4 example.

The architecture is the Lamari/Buchdahl intersection argument for complex surfaces, rebuilt in real-variable form for almost-complex J:

| Pluripotential tool | Replaced by |
|---|---|
| dd^c-lemma | closed lift B |
| Demailly regularization | Hodge-resolvent smoothing |
| Siu decomposition and Lelong numbers | density θ and splitting P = P_E + P' |
| "zero Lelong numbers ⇒ nef" | residual pairing |

## 5. Lean structure

- **Size:**
  - 582 files plus Main and Model; 83k lines.
  - 4,916 declarations: 3,755 theorems, 909 defs, 183 instances.
  - Proof DAG: 4,240 declarations.
- **DAG by directory:** DifferentialForms 1507, Hodge 1323, Charts 476, Elliptic 263, Functional 260, Concentration 173, HeatFlow 171, Currents 53.
- **What fills it:** Hodge theory, Gårding, heat/Volterra parametrices and Sobolev spaces are built from scratch, because Mathlib has none of them. The paper's core is perhaps 10–20% of the DAG.
- **Main.lean:30-50:**
  - `exists_geometric_separating_current`;
  - `separating_current_L2_correction` (Q ∈ L², and ⟨Q,α⟩ = −1);
  - `concentrationActivationData_nonempty`;
  - `concentration_forces_correction_zero` (Q = 0);
  - which together give −1 = 0.

**Route differences from the paper:**
1. **The metric is built from the tamer.** `hermitianMetric J α` uses the invariant part of α. The contradiction is ⟨Q,α⟩ = −1.
2. **No density limit and no tangent measures.**
   - The Lean keeps the "defect" term (|z|²|v|² − ⟨z,v⟩² − ⟨z,Jv⟩²)/(s²+|z|²)² that the paper discards in Prop 3.1 (`Concentration/RadialDefect.lean:39`).
   - Its integrability gives transverse decay at every centre. This is the Allard/Simon monotonicity-excess mechanism.
3. **E is replaced by an exceptional set.**
   - The cutoffs are summable log activations c_n = 2^-n·log(1+f_n/δ_n), along chosen scales (`Charts/SlowLogCutoff.lean`, `Charts/SummableCutoff.lean`, `Concentration/ConcentrationActivations.lean`).
   - The exceptional set is {Σc_n = ∞}.
   - Closedness of the restriction comes from `restriction_zero_of_tail_bounds`.
4. **Q is a weak L² limit of regularized corrections.**
5. **Not formalized:** Thm 1.2, Cor 1.3 and the example. `normalized_defect_moment_tendsto_zero` is dead code.

## 6. Items (summary; full list in JSON)

**N0:**
- I01 (taming/compatible vocabulary);
- I02 (R, F);
- I03 (self-duality algebra);
- I04 (currents, trace measure);
- I06 (separation: Sullivan, Harvey–Lawson, Li–Zhang);
- I10 (S_r);
- I11 (zero pairing);
- I12 (heat kernel);
- I25 (cones);
- I27 (class separation);
- I32 (hypersymplectic);
- L03 (defect = monotonicity excess).

**N1:**
- I05 (closed lift; Lejmi, Draghici–Zhang);
- I07 and I08 (radial tests and correction bounds);
- I09 (quadratic growth);
- I13 (angular identity);
- I15 (mixing lemma);
- I19 (density existence);
- I20 (transverse moment via tangent measures);
- I22 (passage to E);
- I26, I28, I31 (the T^4 example);
- L01.

**N2:**
- I14 (positive-pairing lower bound);
- I16 (energy);
- I17 (θ/E as almost-complex Lelong/Siu);
- **I18 (Thm 5.1)**;
- I21 (density cutoff and the balance estimate);
- **I23 / I29 (residual pairing)**;
- I30 (cone theorem);
- L02 (activations).

**N3:** none assigned. I18 is flagged as borderline.

## 7. Eureka candidates

1. **Thm 5.1, density-splitting closedness (I18 + I17 + I21).** Provisional N2, N3-borderline. F3 if promoted.
   - **For:**
     - The hypothesis (only P+Q closed, with Q ∈ L² anti-invariant) is strictly weaker than in any restriction theorem found.
     - The angular × transverse balance r^{-3}·O(r²)·o(r) has no neighbour found.
     - It is the step that enables everything after it.
     - Family 341 reuses it for another Donaldson question.
   - **Against:**
     - Its conclusion has the same shape as Siu / El Mir–Skoda / Elkhadhra 2014, which handle *closed* positive currents.
     - Its ingredients are classical.
     - The Lean reaches the same split by a different, also classical route, so the statement is reachable by more than one route.
2. **Residual pairing (I23/I29).** N2.
   - **For:** this is what removes the h^- = b^+ − 1 restriction of all earlier Buchdahl-type approaches.
   - **Against:** it is the almost-complex analogue of Demailly 1992 (zero Lelong numbers ⇒ nef, so the self-intersection is ≥ 0) combined with the Lamari/Buchdahl intersection argument.
3. **Angular energy estimate (I13 + I14 + I16).** N2. This is regularization plus a calibration-type identity.
4. **Lean-only activations and defect route (L02, L03).** N2 / N0.
5. **Quadratic mass growth (I09).** N1.

**Literature check** (WebSearch, snippet level):
- Elkhadhra (arXiv 1211.0106) restricts only closed positive currents to J-analytic sets.
- Demailly's regularization paper bounds the negative part by Lelong numbers.
- No 2026 proof announcement other than this release was found. The best prior results are TWZZ (b^+=1 / h^- = b^+−1) and Taubes (generic J, b^+=1).

## 8. Correctness concerns

- **Extraordinary and unreviewed.** It resolves a 20-year-old Donaldson question.
- **No gap found in my read of Secs 2–7.** I checked by hand:
  - the angular identity, the mixing algebra and the energy inequality;
  - the closed-lift identities;
  - density monotonicity;
  - the tangential-cutoff signs and the critical scaling;
  - the final pairing;
  - the T^4 example.
- **Sketched (standard but not proved):**
  - the measurable spectral decomposition;
  - pointwise order-0 ΨDO bounds;
  - the heat-parametrix remainders;
  - the conditional-measure and differentiation inputs.
- **Version history.** Sep-23 claimed K^t = K^c + H_J^- in general by misapplying Li–Zhang Cor 1.1. Oct-6 withdrew this and added a counterexample (`history.md:23`). The main theorem was unaffected.
- **The Lean certifies Thm 1.1 only if it compiles.** It does not certify the paper's Lemmas 5.2–5.3, because the routes differ. The cone results are paper-only.

## 9. Extraction friction

- There are two manuscript versions. `lean/docs/342.md` links the old one.
- The Lean is huge but has descriptive names: Secs 2–4 and 7 join by name, Secs 5–6 only by role.
- The extractor ranking is dominated by plumbing and Hodge infrastructure.
- The Lean was not built (shared checkout).
- There is no reasoning trace.
