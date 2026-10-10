# F1 downstream-use report: spliced stable permutation symbol (family 271)

**Item:** E1 / pivot PV3 of the family-271 trace. The *spliced stable permutation symbol* F_π(x,y) = ∏ᵢ (xᵢ + y_π(i)) appears in *Spontaneous magnetization in the quantum Heisenberg ferromagnet* (24 Sep 2026), sec. 2 (`02-pin-test.tex`). The trace grade was N3 candidate (borderline N2), F1/F5.
**Machine-readable:** `f1_stable_permutation_symbol.json`, which includes 19 verbatim Lean declarations.
**Bottom line:** the object is a known one, the Borcea–Brändén symbol of the permutation-averaging operator. Splicing is a known closure operation, a half-plane analogue of the Asano/Suzuki–Fisher trace contraction. The new step is the bridge: the contraction produces exactly Tóth's weight 2, so BBL negative dependence carries over to the pinned θ=2 measure. **Recommended regrade: N2.** Downstream use is confirmed only inside family 271. The best cross-problem target is the easy-plane XXZ / Ueltschi loop model with u∈(½,1). I verified that the stability half of the device extends to that model.

---

## 1. The item, precisely

**Definition (paper Lemma `lem:pin-exchange-symbol`; Lean `permutationSymbol`, `lawSymbol`).**
- For a permutation π of a finite set V, F_π(x,y) = ∏_{i∈V}(xᵢ + y_π(i)). This is a multiaffine polynomial with one input variable and one output variable per point.
- For a random π, the law symbol is 𝔼F_π.
- 𝔼F_π is *stable* (no zeros on ℍ^{2|V|}) whenever π is a product of independent Bernoulli(u) transpositions and deterministic permutations, or a limit of such laws. These limits cover Poisson exchange processes, uniform permutations on blocks, and independent products of these.
- Proof: one Bernoulli step is the partial symmetrization (1−u)F + uτF in two output variables (BBL Thm 4.20). The paper also gives an elementary two-variable section proof, and Lean `stable_symmetrize` formalizes it. Limits are handled by Hurwitz.

**Layering.**
- Cut the periodic time circle of Tóth's exchange picture at every pin time.
- The interval maps are independent and use disjoint variables, so the layered symbol F_V is a product of stable symbols.

**Splicing (Lemma `lem:pin-splicing`; Lean `splice`, `splice_permutationSymbol`, `stable_spliced_law`, `stable_pinLaw`).**
- To delete an unpinned vertex q, set x_q = y_q = t and take the coefficient of t.
- A path i→q→j becomes (xᵢ+t)(t+y_j), whose linear coefficient is xᵢ + y_j: the path is spliced.
- A fixed point gives x_q + y_q = 2t, which contributes the factor **2**.
- Deleting all non-pins leaves F_P = 𝔼_b[2^{n_P} ∏_{i∈P}(xᵢ + y_σ(i))]. Here σ is the next-pin permutation and n_P counts the cycles that avoid the pins.
- This is a stable encoding of the *cycle-weighted* pin law ℙ_P.

**Output extraction and decisive use.**
- G_T(y) = 𝔼_P ∏_{i∈T} y_σ(i) is the stable subset-generating polynomial of σ(T).
- Stability gives the presence inequality ℙ(J⊆σ(T)) ≤ ∏ ℙ(j∈σ(T)).
- Prop. `prop:pin-test` then gives ℙ_E(T ⊆ 𝓑_E) ≤ (2r)^{|T|}. In Lean this is `finite_simultaneous_pin_test`.

**Obstruction dissolved.**
- The θ=2 cycle weight 2^{#cycles} is a global reweighting. BBL negative dependence was available only for the *unweighted* exchange process.
- The model's previous route used holes, exterior powers and signed minors. That route computes first moments but cannot bound the *positive* event that many test points all lie on pin-avoiding cycles (trace conflict C9).
- Scalar density and bootstrap arguments fail against trapping walls (C7, C8).
- The spliced symbol solves this. Stability is kept through the unweighted layers, where BBL applies, and the contraction itself manufactures the weight 2.

**Abstract mechanism (field-independent).** Encode a random bijection by its two-sided symbol ∏(inᵢ + out_π(i)). This object is preserved by independent local mixing moves. Compose layers by multiplying symbols in disjoint variables. Then take a trace by contracting each output variable with the matching input variable (identify the two, then take the linear coefficient). This contraction preserves stability, splices paths, and gives each closed loop the weight tr(I_{ℂ²}) = 2. The result is a stable generating polynomial for a *globally loop-weighted* measure. Negative dependence for simultaneous positive events then follows.

## 2. Precedent and contamination (step 4)

- **The unspliced object is the Borcea–Brändén symbol.** For the operator T f(y) = 𝔼 f(y_π), we have T[∏(zᵢ + wᵢ)] = 𝔼∏(zᵢ + w_π(i)).
  - Borcea–Brändén (Invent. Math. 2009) show that T preserves stability iff this symbol is stable.
  - Stability for exclusion and interchange laws is BBL 2009, Thms 4.20 and 5.2.
  - Nestoridi–Priestley–Schmid (arXiv:2304.02588, 2023, Cor. 3.6) apply exactly this symbol criterion to uniform block permutations in the S_k shuffle.
- **The splicing is a composition of standard closure operations** (identification, differentiation, real specialization).
  - Its role is to trace a layered product of two-site multiaffine transfer polynomials, assigning 2 to each closed loop. That is the half-plane counterpart of the Asano contraction Suzuki–Fisher (1971) used for the quantum Heisenberg Lee–Yang theorem.
  - The OAI spherical companion itself describes its disk version as an Asano–Ruelle contraction.
- **Not found anywhere:** use of the spliced symbol to get negative dependence for the θ=2 cycle measure or for a next-pin permutation. No post-Oct-6 use was found outside the release; Ryan's Aug 2026 loop-weight-2 paper uses six-vertex methods.
- **Verdict:** the device is a new *bridge* (an instantiation of known machinery in a new, θ=2-specific way), not a new *object*. This confirms and strengthens the trace's "against" note. **Downgrade E1 to N2.**

## 3. Reuse inside the release

| Where | Use |
|---|---|
| Bloch's law (Oct 5), `02-pins.tex` L300–345 | Re-derives the layered symbol, the splicing and G_T for finite-range anisotropic couplings |
| Spherical law (Oct 5), `02-exchange.tex` | Cites the September paper for the stable symbol and the presence inequality. **New use:** the disk form 𝔼∏(1 + xᵢ y_π(i)) with contraction A+D gives zero-free layered traces (Lemma `trace-zero-free`) |
| First lattice correction (Oct 5) | Imports the pin estimates; no new use of the symbol |
| Family 238 (Thorp shuffle), *Routing densities* §4 and *Compatibility entropy* intro | Uses only the BBL ingredient (fair swaps preserve strongly Rayleigh occupancy). This is a separate reuse of the precedent, not of the spliced device |

No cross-family reuse of the spliced object was found.

## 4. Candidate downstream problems (step 2)

Full fields for each candidate are in the JSON. The table is a summary.

| # | Problem | Status | Match / sketch | Payoff | Conf. |
|---|---|---|---|---|---|
| C1 | Ueltschi loop model θ=2, u∈(½,1): easy-plane XXZ ferromagnet, d≥3 | open (RP and Betz–Klippel–Nauth 2025 stop at u≤½) | Exact obstruction. With double bars the next-pin map is a Brauer pairing. **Verified here:** the two-strand mixture symbol (1−u−v)(y₁+w₁)(y₂+w₂) + u(y₂+w₁)(y₁+w₂) + v(w₁+w₂)(y₁+y₂) is Lorentzian with eigenvalues {2, −2u, −2v, −2(1−u−v)}, so it is real stable. Random Brauer laws tested stable, and splicing still gives 2 per loop. **Missing:** a presence inequality for pairings, and an easy-plane version of the leakage half | new theorem | med-low |
| C2 | Heisenberg ferromagnet magnetization on trees of every degree, on nonamenable or polynomial-growth Cayley graphs, and with long-range J | open (Björnberg–Ueltschi: large-degree trees only) | Device is graph-independent and transfers verbatim; only the return-fraction/leakage geometry changes | new theorems | medium |
| C3 | Lee–Yang zero-freeness for quantum Heisenberg; Barvinok-type algorithms | SF71 known; strips partly new | Disk symbol + Asano contraction (spherical companion) | short re-proof of SF71; maybe new regions | med-high (re-proof) |
| C4 | PD(2) law of cycle lengths in Tóth's model on ℤ^d | open | Weight-2 negative dependence as an input to split-merge | partial | low |
| C5 | Strongly Rayleigh property for exclusion and card shuffles (S_k shuffle, Thorp occupancy, open-boundary SEP) | known | Unspliced half plus output extraction | simplifies proofs | high |
| C6 | Classical FPRAS for the isotropic Heisenberg ferromagnet (gap left by Bravyi–Gosset) | open | Stability only of pinned output polynomials; route to spectral independence unclear | new algorithm | low |
| C7 | Antiferromagnet (u=0) without reflection positivity, bipartite graphs | ℤ^d n.n. covered by RP | Reversing time on one sublattice makes loops oriented, so the device applies; AF spin-wave half mismatched | new Néel results | low |
| C8 | Lorentz mirror model with loop weight 2 / XXZ chain (Ryan 2026) | recent | Brauer symbol in discrete time | correlation inequality | low |
| C9 | **Negative:** θ≠2 loop models (SU(n), spin-1 nematic) | — | Doubled symbol for θ=4 is **not stable** numerically (3/3 trials) | none | high (fails) |
| C10 | **Negative:** spatial random permutations / Bose gas | open | Permanental symbol per[a_ij(xᵢ+y_j)] is **not stable** in general (counterexamples include a Gaussian kernel); cycle weight there is 1 anyway | none | high (fails) |
| C11 | **Negative:** θ=1 interchange in d=3,4 (Tóth conjecture) | open | No stability-preserving contraction gives weight 1 | none | high (fails) |
| C12 | Permanent inequalities (Carlen–Lieb–Loss; family 238's four-row inequality) | known | Symbol is only the affine slice fᵢ(j) = xᵢ + y_j | minor | low |

## 5. Held-out speedup targets (step 3)

| # | Known theorem | Current proof | Device route |
|---|---|---|---|
| S1 | Image of a deterministic set under interchange / Bernoulli-transposition products is strongly Rayleigh (BBL Thm 5.2 from deterministic starts) | BBL Thm 4.20 via multivariate Obreschkoff, about 3–5 pages plus BB machinery; not in Mathlib | `lawSymbol` + `stable_lawSymbol_bernoulli` + `stable_outputSymbol`; already about 825 Lean lines in the OAI library |
| S2 | Liggett's negative-correlation inequality for SEP: P(A⊆η_t) ≤ ∏ P(x∈η_t) | Liggett 1985 Ch. VIII, several pages (duality and coupling) | under 1 page given the closure lemmas |
| S3 | S_k-shuffle projection stays strongly Rayleigh (Nestoridi–Priestley–Schmid 2023, Cor. 3.6) | half a page, but cites the 25-page BB symbol theorem | uniform block law as a limit of Poisson exchanges, plus extraction |
| S4 | Suzuki–Fisher Lee–Yang theorem for the quantum Heisenberg ferromagnet | about 10–12 pages (Trotter classical map + Asano) | disk symbol + contraction, about 1–2 pages (spherical companion) |
| S5 | Simultaneous pin test (in-family control) | paper sec. 2 | is the device (already formalized) |

Caveat: in S1–S3 the gain comes from the *unspliced* half, which is precedent. Only S4 and S5 exercise the splicing or contraction.

## 6. Ranked top 5 (step 5)

1. **C1, easy-plane XXZ / Ueltschi u∈(½,1).**
   - This is the only open problem where the obstruction matches exactly: θ=2, no reflection positivity, and a need for product bounds on simultaneous avoidance events.
   - The stability half of the device provably extends to crosses plus double bars, by the Lorentzian eigenvalue computation above.
   - Two pieces are still missing: a presence inequality for non-orientable pairings, and an easy-plane escape/leakage analysis.
   - If both close, this is a genuine cross-model use.
2. **C2, other transient geometries for the Heisenberg ferromagnet.**
   - The device transfers verbatim, and the Bloch companion already shows it absorbs anisotropic finite-range couplings.
   - The open problems are real, and the geometric half should be easier on trees and nonamenable graphs.
   - It ranks second because it stays inside the same model, so it is a weaker test of cross-problem power. It is also the most likely to succeed.
3. **C3/S4, Lee–Yang for quantum Heisenberg.**
   - The disk form is already a second, independent use inside the release, and it gives a clear measurable speedup over SF71.
   - However, it sits closest to the Asano/Suzuki–Fisher precedent.
4. **C5/S1–S3, negative dependence for exclusion and shuffles.**
   - These are the cleanest Lean-measurable targets, but any speedup credits the BB symbol rather than the splicing.
   - Use them as a control.
5. **C4, PD(2) for Tóth cycles.**
   - This is the natural next question in the same model.
   - The device supplies a missing negative-dependence ingredient, but it is far from a resolution.

## 7. Numerical checks done for this report

The tests used Brändén's Rayleigh-difference criterion, sampled at 3–4k random real points with mixed scales.

- **Brauer mixtures:** all stable, with an analytic proof for the two-strand step.
- **Doubled (θ=4) symbol:** unstable.
- **Permanental laws:** unstable in general.
- **Laws not generated by transpositions:** uniform on the 3-cycles is unstable; uniform on S₃ is stable.
- **Splicing identities:** checked symbolically. A weighted contraction x_q = a·t, y_q = b·t gives a+b per loop but a path-dependent factor (a·xᵢ + b·y_j), so a=b is forced. The device is therefore intrinsically θ=2.

## 8. Lean source (step 6)

Files are under `data/raw/openai-math/lean/OAI/MathematicalPhysics/Heisenberg/`. The full verbatim text is in the JSON `lean_source`; key items:

- `PermutationSymbols.lean:15`
  ```lean
  def permutationSymbol (π : Equiv.Perm V) : MvPolynomial (V ⊕ V) ℂ :=
    ∏ i, (MvPolynomial.X (Sum.inl i) + MvPolynomial.X (Sum.inr (π i)))
  ```
- `PermutationSymbols.lean:70`
  ```lean
  def lawSymbol (μ : Ω → ℝ) (π : Ω → Equiv.Perm V) : MvPolynomial (V ⊕ V) ℂ :=
    ∑ ω, MvPolynomial.C (μ ω : ℂ) * permutationSymbol (π ω)
  ```
- `PinSplicing.lean:27`
  ```lean
  def splice (p : MvPolynomial (Option V ⊕ Option V) ℂ) : MvPolynomial (V ⊕ V) ℂ :=
    eraseNone (MvPolynomial.pderiv none (MvPolynomial.rename spliceVariables p))
  ```
- Key lemma statements:
  - `stable_lawSymbol_bernoulli` (PermutationSymbols:128)
  - `splice_permutationSymbol` (PinSplicing:171)
  - `stable_spliced_law` (PinSplicing:203)
  - `stable_pinLaw` (StablePinLaw:218)
  - `stable_outputSymbol` (PermutationSymbols:248)
  - `presence_product` (PinSymmetrization:145)
  - `finite_simultaneous_pin_test` (PinDensity:92)

None of these declarations has a docstring in the source.

## Sources
- BBL 2009 (https://arxiv.org/abs/0707.2340)
- Borcea–Brändén I (https://arxiv.org/abs/0809.0401)
- Pemantle survey (https://arxiv.org/abs/1210.3231)
- Nestoridi–Priestley–Schmid (https://arxiv.org/abs/2304.02588)
- Ueltschi (https://arxiv.org/abs/1301.0811, https://arxiv.org/abs/1211.4141)
- Betz–Klippel–Nauth (https://arxiv.org/html/2503.17857v1)
- Ryan 2026 (https://arxiv.org/abs/2608.21306)
- Goldschmidt–Ueltschi–Windridge (https://arxiv.org/abs/1104.0983)
- Björnberg (https://arxiv.org/abs/1505.06716)
- Björnberg–Ueltschi (https://arxiv.org/abs/1803.11430)
- Elboim–Sly (https://arxiv.org/abs/2211.17023)
- Harrow–Mehraban–Soleimanifar (https://arxiv.org/abs/1910.09071)
- Bravyi–Gosset (https://arxiv.org/abs/1612.05602)
- Bravyi–Gosset–Liu–Wong (https://arxiv.org/abs/2607.14401)
- Suzuki–Fisher, J. Math. Phys. 12 (1971)

The search log is in the JSON.
