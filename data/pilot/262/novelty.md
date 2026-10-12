# Family 262: novelty pass (sharp 1D Lieb–Thirring, scalar / matrix / equality cases)

Novelty analyst, 2026-10-12. Machine-readable version: `novelty.json`. Inputs: `family.json`/`family.md` (there is no trace and no f1 file), the S/M/E TeX, and the Lean field definitions (text only).

**Access caveat.** arxiv.org and its mirrors were unreachable from this session: WebFetch failed on DNS and the Bash proxy returned 403. Everything said about Read–Schulz below comes from WebSearch result summaries, so all RS wording is **unverified**. Check it against arXiv:2609.10478v2 before citing it.

## Provenance verdict: **partial**
- **Closest precedent:** Read–Schulz, arXiv:2609.10478 (v1 2026-09-09, v2 2026-09-14), a human paper. No search summary shows any AI disclosure; affiliations are academic (Orsay, Copenhagen). S cites v2, so the paper was in the model's context.
- **What RS contains, as summarized:**
  - the sharp γ=1 constant 4/(3√3π);
  - an operator-valued bound L_{1,d} ≤ (2/√3)L^cl;
  - a method that extends Benguria–Loss's cumulative-mass argument to orthonormal families via a **cumulative mass matrix** A(x)=∫_{−∞}^x UUᵀ (0≤A≤I, A′=UUᵀ, any rank), with a tangent-type auxiliary q and a Riccati-type identity.
- **Model-produced prior work:** none found before 262-S. M builds on S, and E builds on M; both are model-produced, which is why the flag is "partial".
- **Effect on the Lean candidate:** none. C1 lives in S, and S builds on no model output.

## Final grades
| Id | Item | N | F | Conf. | Lean-backed | Route |
|---|---|---|---|---|---|---|
| C1 | Regularized matrix field M_δ(B)=c∫(f(K²−2sB+s²)−f(s²))ds with primitive J and rank-one comparison (I05/I07–I09/I11/I14) | **N3** (borderline N2) | F1 (F3) | 0.40 | **yes** (`matrixField`, `fieldPrimitive`, `source_rankone_comparison`) | **Lean shortlist** |
| C2 | Integrated trace comparison tr(NV) ≥ tr(N^q) with exact SOS deficit (M Thm 3.1, I25) | N2 (provisional N3 withdrawn) | – | 0.55 | no | none (informal list only if ever regraded N3) |
| C3 | Potential-free action inequality keeping the k_i (S Thm 2.1) | N2 (templated-strengthening cap) | – | 0.7 | partial (`ActionClaim` unproved; `finite_action_upper_test` proved) | – |
| C4 | Gamma–Gaussian conjugation average + Klein (I10/I12/I13) | N2 | – | 0.65 | yes | – |
| C5 | Calibration identity + compact penalty (I15/I18) | N2 | – | 0.7 | yes | – |
| C6 | Mod-2 continuation modulo row signs (I16/I17, Lean PL parity I23) | N2 | – | 0.7 | yes | – |
| C7 | Half-line boundary maps S,T (I26) | N1 | – | 0.6 | no | – |
| C8 | Dimension-free defect Φ_K + m-column compactness (E, I31/I32) | N2 | – | 0.6 | no | – |

## Key comparison: C1 against Read–Schulz
**Different object, with only a shared template.**
- **RS:** the matrix variable is the integrated density A(x). It has endpoints 0 and I, does not involve K, and satisfies A′ = density exactly.
- **262:** the matrix variable B is a matrix Riccati (log-derivative) variable with endpoints K and −K that carries the eigenvalue scales. The density enters only through the penalized constraint M(B)=aaᵀ.
- **The σ=½ member:** at γ=1 we have β=0 and f is a regularized log. M_δ then becomes a log-type integral of the pencil K²−2sB+s², not a function of A.
- **Conclusion:** M_δ is not the γ=1 member of RS's construction, and the precedent does not downgrade C1.
- **What they share** is the Benguria–Loss architecture: a matrix path with prescribed endpoints, a calibration whose boundary difference gives the constant, and a completed square. That shared template is why C5 is N2.

## Why C1 stays N3 only at 0.40
**Interpretation.** X_s(B) = (s−B)² + (K²−B²) is the Fourier symbol of −(d/dx − iB)² + K² − B². M itself makes this explicit with ∇ = ∂−iB. So M_δ is, up to regularization, a *local Weyl density* of a constant operator with a non-abelian gauge shift.
- In the commuting case the shift integrates out, giving the classical scalar calibration (k²−b²)^σ. That is Keller's one-state first integral.
- In the noncommuting case the shift makes the field affine in B, so it is a trace gradient. Naive (K²−B²)^σ is not a gradient.

**Neighbours.**
- Laptev–Weidl lifting and the LT semiclassical phase-space integral: ingredients, in L.
- Benguria–Loss 2000/2004 and Read–Schulz: template.
- Trace-function calculus and Hellmann–Feynman: textbook.
- Noncommutative-gauge spectral traces: genuinely different.
- No neighbour was found for the field itself. Searches covered RS ×4, matrix pencil gradient fields, matrix-symbol phase-space integrals with non-abelian shifts, the conjecture's status, and AI-assisted LT work. zbMATH and MathOverflow were not reachable.

**The four tests.**
- **Test 2: pass, borderline.** The field occurs nowhere in the goal or in L; only its scalar shadow and the unshifted momentum integral do.
- **Test 3: pass.** The field plus rank-one block is 69% of the mathematical core, and knocking it out kills the route.
- **Main risk.** An expert may call it "just" a gauge-shifted Laptev–Weidl phase-space density used as a calibration, which would make it N2.

## family_D
**D3 (provisional), confidence 0.40.** It rests on C1 alone.

It falls to D2 if any of these happens:
- the full RS text has an energy-dependent matrix field matching M_δ at σ=½;
- an expert identifies M_δ as a known Weyl-density calibration;
- Test 4 shows high pass@k in the directed arm.

The ingredients are N0 transfer. The candidate is their coupling, so the transfer exclusion does not apply.

## Bridge novelty
- **Phase-space lifting → calibration field (C1):** an intra-field new use of a known object type (0.5).
- **Matrix analysis → rank-one comparison:** known route.
- **Mod-2 degree → LT path existence:** a known ODE-shooting route, first in LT as far as searched.
- **Weyl–Titchmarsh / Riccati commutation → trace inequality (C2, C7):** known route (Benguria–Loss 2000, Clark–Gesztesy).
- **Solitons → equality cases:** known route (Keller; Frank–Gontier–Lewin 2025).

## Why C2 was downgraded
- Against M's base library, which contains the model-produced ScalarCompanion, the statement is the rank-free version of S's rank-one comparison (N = aaᵀ gives a^TVa ≥ |a|^{2q}). That is a templated strengthening.
- The device is Benguria–Loss commutation plus matrix Weyl–Titchmarsh boundary maps.
- Its γ=1 result is already in RS (operator-valued, any rank), as M concedes.
- The exact SOS deficit is a real refinement, but it counts as design.
- It is not in Lean. If it were ever regraded N3, it would go to the informal list.

## Discoverability (Test 4, not run)
- **P-C1 (Lean):**
  - **Hide:** the field, the primitive, the rank-one comparison and everything that names them (path ODE, penalty, action limit, and the corresponding Lean files).
  - **Arms:** L− / L (+RS) / open / directed. The directed arm gives Thm 2.1, the scalar calibration and the gradient + commuting + rank-one spec.
  - **Sampling:** n=256, pass@k for k ∈ {1,…,256}.
  - **Hit criterion:** a momentum integral of a scalar function of K²−2sB+s², or its Weyl-density equivalent. Alternative fields meeting the spec are recorded separately and can be checked against `RankOneClaim` in Lean.
  - **Models:** training cutoff before 2026-09-09. Exclude RS, S/M/E, the release and the producing model lineage, and run canary probes.
- **P-C2 (informal):** give S, hide M §3, and ask for the full-rank comparison. Judging is pen-and-paper.

## Open questions
1. Read the RS full text and verify every quote.
2. Ask an expert whether a gauge-shifted Weyl density has been used as a calibration field before.
3. Check whether M_δ at σ=½ maps onto RS's argument under a change of variables B ↔ A.
4. Downstream test: does the *device* shorten other sharp inequalities? Candidates are vector NLS ground states with distinct masses, a re-proof of RS's operator-valued γ=1 bound, and the endpoints.
5. Check whether C2 is a known Lieb–Thirring/Legendre inequality for constant-coefficient operators with matrix gauge fields.
