# Downstream report (Lean shortlist): family 075, thermal noisy labels

Machine-readable companion: `downstream.json`. This report builds on `f1_thermal_labels.json`, reusing its candidates, precedent check and Lean sources. All Lean checks are at **text level only**: no toolchain is available, and the comparator has nanoda disabled.

## Part A: is the item in the Lean?

**lean_status: `formalized, different route`.** The label, its update, the two-law Fisher sum and the decoding identity all lie on the proof DAG of the comparator paperMain, whose statement matches the headline exactly. The setting is a finite ZMod 2^M model with integrated (not sampled) labels and several route substitutions. GridBound fixes epsilon_j = r_{j+1} (Gi = the paper's g_I). That is exactly the only instance the paper ever uses, and it affects only output-side path lemmas, so the Lean does certify the label's role. Checked at text level only, without compiling.

### The epsilon_j question (from the shortlist)

**Question.** The Lean GridBound fixes the signs epsilon_j that the paper's Prop dyadic quantifies over. Does that mean the Lean does not certify the label's role?

**Answer: no.**

- Paper Prop dyadic (06-procedure.tex:10-47) quantifies over F_{j+1}-measurable epsilon_j with |epsilon_j| <= 1, 'the same epsilon_j for all modulations'. The procedure section (06-procedure.tex:55-66) says the coefficient is formed on the INPUT side and epsilon_j(x) only multiplies the OUTPUT, and 'the same multipliers are used for every piece and every label coordinate'. So the multipliers never enter the label construction.
- The paper's only use of Prop dyadic is Thm good-set (11-fourier.tex:63-65): 'on the output side choose epsilon_j = r_{j+1}, so that g_I = r_{j+1} r_{j+2}'. A grep for prop:dyadic finds only the intro, the procedure statement, its proof in 09-assembly, and this application.
- Lean: FinJump p F x = p.Gi(pos x) * p.avg(Hi * F) (Dyadic/Grid.lean:234). Gi = haarG o normarg, haarG x = haarH(2x) - haarH(2x-1) (Fourier/Haar.lean:18), and Gi_eq: Gi = L.Hi - R.Hi (Grid.lean:120). This is exactly the paper's summand E_p[rho chi_u h_I] * g_I with epsilon_j = r_{j+1}.
- The fixed sign is consumed only in the output-path layer: Paths/Trip.lean (Gi_half, blow, trip_delay: blow x c = curl c.bit * curl d.bit; trip_final: |blow| = 1), Paths/Frost.lean last_lag (uses t^2 = k^2 and |blow| = 1), Paths/Letters.lean (proceeds/duties), Paths/Tilt.lean, Assembly/Rail.lean and Assembly/Cast.lean stage_shift. Grep finds NO use of Gi, haarG or blow in Thermal/ or Procedure/, where label, channel, fisher, bit_def, space_deficit and fisher_bound live.
- The frequency supremum is intact. GridBound has 'exists W ... forall x good, forall u : Grid M, ||FinShift J (finMod rho u) x|| <= W x' with expU W <= C 2^j, i.e. one majorant for all 2^M modulations, uniformly as M -> infinity.
- The label lemmas are on the comparator chain (extract_lean BFS): paperMain -> almost_everywhere_fourier_convergence -> gridProof -> grossOur -> upper_total -> Road.fisher_bound -> one_split_price -> space_deficit -> bit_def, with fisher_bound -> Thermal.channel -> Thermal.label. Separately: gridProof -> annual_valid -> gala -> main_stage -> ride -> below_decode -> decode_track -> gain_decode -> duet_decode. And: gridProof -> plant -> fund_est -> certified_add -> F_increment -> cred_mono -> cred_add_mono -> ginibre. Thermal.label has 323 dependents in the DAG (24% of 2014 declarations).

```lean
def FinJump {M : ℕ} (p : Node) (F : Grid M → ℂ) (x : Grid M) :=
  p.Gi (pos x) • p.avg (fun y => p.Hi (pos y) • F y)

/-- Finite cut statement; asks for an L¹ majorant restricted to points where density steps stay
below threshold. There is no dependence on a frequency or depth cutoff in the constant. -/
def GridBound : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧ ∀ᶠ j : ℕ in atTop, ∀ J : ℕ, ∀ᶠ M : ℕ in atTop,
    ∀ (ρ : Grid M → ℝ), (∀ x, 0 ≤ ρ x) → expU ρ ≤ 2 →
      (∀ x, ρ x ≤ Real.exp ((2:ℝ)^j)) →
    ∃ W : Grid M → ℝ, (∀ x, 0 ≤ W x) ∧ expU W ≤ C*(2:ℝ)^j ∧
      ∀ x : Grid M, finGood (((j:ℝ)+1)^3) J ρ x →
        ∀ u : Grid M, ‖FinShift J (finMod ρ u) x‖ ≤ W x
```

**Residual caveat.** The Lean does NOT certify the general-multiplier Prop dyadic. Downstream targets that need other output multipliers would need the general form: variational Carleson, other Haar kernels, Walsh variants whose output signs are not r_{j+1} r_{j+2}. The fix looks local: replace curl c.bit by an arbitrary depth-(j+1)-measurable epsilon with |epsilon| <= 1 in trip_delay, trip_final and last_lag, using t^2 <= k^2 instead of equality, and complex parts in Frost. The extra lines (perhaps 100-300) are a guess from reading these four files, not a measurement.

**Recommended check.** State GeneralGridBound (epsilon : N -> Grid M -> C, constant on depth-(j+1) blocks, ||epsilon|| <= 1, FinJump with epsilon j * r_{j+2} in place of Gi). This is statable now in about 25 lines from Dyadic/Grid.lean. Then verify that the proof changes are confined to Paths/ and Assembly/Cast. Doing so would close the issue formally.

**Verdict.** The specialisation does not undercut the label. Remove the 'Lean may not certify the label's step' caveat from the shortlist and replace it with 'Lean certifies the epsilon_j = r_{j+1} instance (the one the paper uses); general multipliers are unformalised and are output-side only'.

### Comparator chain (FourierLLogL; solution module `OAI.Analysis.FourierLLogL.PaperMain`)

- OAI.FourierLLogL.paperMain (PaperMain.lean:8; comparator target)
- OAI.FourierLLogL.almost_everywhere_fourier_convergence (Main.lean:25)
- OAI.FourierLLogL.main_of_grid (Main.lean:17; GridBound -> unitTreeBound -> affine -> realGoodBound -> goodBound -> main_bound_consequence)
- OAI.FourierLLogL.Dyadic.gridProof : GridBound (Assembly/Endpoint.lean:18)
- OAI.FourierLLogL.Dyadic.Procedure.Paths.CastShow.grossOur (Assembly/Weighted.lean:82)
- OAI.FourierLLogL.Dyadic.Procedure.Paths.CastShow.upper_total (Verdict.lean:147)
- OAI.FourierLLogL.Dyadic.Procedure.Road.fisher_bound (Procedure/Fisher.lean:118)
- OAI.FourierLLogL.Dyadic.Procedure.Road.one_split_price (Procedure/Fisher.lean:68)
- OAI.FourierLLogL.Dyadic.Procedure.space_deficit (Procedure/Deficit.lean:147)
- OAI.FourierLLogL.Dyadic.Procedure.bit_def (Procedure/Deficit.lean:100)
- OAI.FourierLLogL.Dyadic.Thermal.channel (Thermal/Piece.lean:30; reached from fisher_bound)
- OAI.FourierLLogL.Dyadic.Thermal.label (Thermal/Form.lean:163)  <- THE ITEM

**Side branches:**

- **decoding**: gridProof -> annual_valid (Gross.lean:35) -> gala -> main_stage -> ride -> below_decode -> decode_track -> gain_decode -> duet_decode (Assembly/Phase.lean:28)
- **update**: gridProof -> Procedure.Play.Follows (Play.lean:102) -> Thermal.Update.Good -> Thermal.Update.next (Update.lean:33)
- **positivity**: gridProof -> plant (Procedure/Tree.lean:58) -> Fund.fund_est -> certified_add -> F_increment -> cred_mono -> cred_add_mono -> ginibre (Thermal/Ginibre.lean:212)
- **fixed_sign_use**: gridProof -> stage_shift (Assembly/Cast.lean:138; FinJump unfolding) and the Paths/Trip.lean trip_delay / trip_final consumers (output side only)
- **dag_stats**: extract_lean v2: 2448 declarations in 156 files (FourierLLogL plus the imported OAI/Analysis/Fourier). 2014 are in the comparator DAG. gridProof dominates 89.7%. Thermal.label has 323 dependents and Thermal.K 24.7%. Every label lemma is in the DAG.

### Gaps between paper and Lean

- NOT COMPILED (no toolchain; nanoda off). Text-level only. lean_layer_notes.md: no sorry, axiom or native_decide in the Procedure-through-Assembly layers.
- epsilon_j fixed to r_{j+1} (Gi = g_I) in GridBound, against arbitrary F_{j+1}-measurable |epsilon_j| <= 1 in Prop dyadic. This is the exact instance used in 11-fourier.tex:63-65, and it is output-side only; see epsilon_j_check. It does NOT affect the label.
- Good-set form instead of a stopped sum: finGood with cutoff (j+1)^3 replaces tau with threshold e^{4h} = (log d)^4. The layer height is d = 2^j (rho <= exp(2^j)). This is a different but adequate exceptional-set bookkeeping.
- Finite model: Grid M = ZMod 2^M and finite laws, with no MeasureTheory martingales. Labels are integrated as a law (Thermal.label, Thermal.channel = label.send (x + .)), never sampled.
- The simultaneous regular-evidence statement is replaced by a multiplicative path-product score supermartingale (Rare.lean:66 rare). log_mass_budget covers only the final state. Scalar potential psi becomes Huber + b x^2. Relative entropy for snapshots becomes triangular discrimination. The count cap is derived (fund_est) instead of being a transfer rule.
- Extra hypothesis 1000 * 2^J <= 2^M in grossOur, rating_bound, rare and stake_upper. Harmless, since GridBound quantifies 'eventually in M'.
- Constant C = 10^222 (gridProof). The comparator paperMain matches the headline exactly (full symmetric partial sums, a.e., integrable |f| log(2+|f|)).

The JSON `lean_source` has 34 verbatim entries: the 21 from F1 plus GridBound, FinJump, FinShift, finMod, finGood, Gi_eq, haarG, gridProof, Gi_half, blow, trip_delay, main_of_grid and paperMain.

## Part B: speedup targets

| id | target | status | expected / payoff | Lean feasibility |
|---|---|---|---|---|
| S1 | Walsh-Carleson theorem (Billard / Sjolin), proved through a Walsh GridBound | known theorem | high relative to tiles if the Walsh L log L port (O1) works; otherwise med | statable with < 300 lines of new definitions |
| S2 | Bourgain's multi-frequency lemma in a finite dyadic model | the Euclidean smooth-window version is known with (log N)^2, and the optimal power is open. For this rough dyadic-average variant I have NOT verified that the same bound is in the literature; check before use. | low-med (high value of information: a frequency-count saving on a different theorem would confirm the item) | statable with < 300 lines of new definitions |
| S3 | Walsh analogue of Sjolin-Soria / Antonov: Walsh series converge a.e. in L log L log log log L | known theorem (Walsh) | med | statable with < 300 lines of new definitions |
| S4 | CONTROL: scalar dyadic entropy/Fisher bound (label-free, A = 0) | known | none (control) | statable now |
| S5 | NEGATIVE CONTROL: sharpness of Rademacher-Menshov for general orthonormal systems | known | none (negative control) | statable with < 300 lines of new definitions |

## Open problems (ranked Lean-usable first)

| id | target | status | expected / payoff | Lean feasibility |
|---|---|---|---|---|
| O1 | Walsh-Fourier series converge a.e. for f in L log L (finite form: Walsh GridBound) | open (best known L log L log log log L) | resolves the Walsh L log L problem; best CHEAP Lean check (shortlist next_test) | statable with < 300 lines of new definitions |
| O2 | Sharp power of log N in Bourgain's multi-frequency lemma | open | possible (log N)^2 -> log N | statable with < 300 lines of new definitions |
| O3 | Variational Carleson near L^1 (r-variation of partial sums for f in L log L, r > 2) | open near L^1 as far as found | likely new endpoint result | statable with < 300 lines of new definitions |
| O4 | Vilenkin series of bounded type converge a.e. in L log L | open | resolves | statable with < 300 lines of new definitions |
| O5 | Cubic partial sums on T^d in L log L | open as far as found | L(log L)^d -> L log L | statable with < 300 lines of new definitions |
| O6 | Konyagin's lacunary conjecture (L log log L) | open | new bound at best | statable now |
| O7 | Pointwise ergodic averages along squares in L log L | open | new bound at best | statable now |
| O8 | Return-times theorem near L^1 | open near the endpoint | range extension | statable with < 300 lines of new definitions |
| O9 | Polynomial Carleson near L^1 | open near L^1 | — | statable with < 300 lines of new definitions |

## Theorem corollaries (not counted as reuse)

- Carleson's theorem (L^2), since L^2 is inside L log L on the circle. With paperMain in L it is about 5 lines; it must be EXCLUDED from any speedup measurement, or L must omit paperMain/gridProof. F1 listed it as a speedup target; it is moved here.
- Kolmogorov-Seliverstov-Plessner (its hypothesis gives f in L^2). Moved here from the F1 speedup list for the same reason.
- Hunt's theorem in L^p, p > 1; Sjolin's L log L log log L; Antonov's L log L log log log L (trigonometric): all contained in L log L.
- Weak-L^1 maximal bound on L log L (already in Lean: Main.lean weak_L1_maximal_bound) and maximal_good_sets.
- The gap in Konyagin's optimal-Orlicz-class problem shrinks to between the divergence class and L log L.

## Negative controls

- **Label-free scalar entropy bound (A = 0)**: The trivial channel: no speedup expected (S4). (Lean: statable now)
- **Rademacher-Menshov sharpness for general ONS**: No translation structure, so no positive-definite label (S5). (Lean: statable with < 300 lines of new definitions)
- **Kolmogorov's L^1 divergence example**: A proved-false analogue: the device must not 'prove' a.e. convergence in L^1. Budgets scale with d = log ||rho||_inf and are unbounded for L^1 densities. A prover that derives L^1 convergence from the label lemmas has a broken library. (Lean: statable now)

## Top 5 (Lean-usable first)

1. **O1: Walsh GridBound (finite Walsh L log L).** This is the cheapest and most decisive Lean check, and the shortlist's own 'run first' test. The statement is about 30-60 new lines on top of Dyadic/Grid.lean. The obstruction is identical. Decoding becomes exactly multiplicative, the output-side Haar sign structure is the same one GridBound already fixes (so the epsilon_j specialisation is no obstacle), and the Fisher lemmas are channel-agnostic. The formal baseline is gridProof's 2014-declaration DAG minus the Fourier transfer layer. A successful port shows the device is portable. A sceptic will call it 'the same theorem on another group', so it confirms portability, not a jump.
2. **S2 / O2: Bourgain's multi-frequency lemma, finite dyadic model.** This is the only DIFFERENT theorem where the obstruction (a loss in the number of frequencies) is the whole difficulty. The statement takes about 30-50 new lines using OAI's chi, Node.avg and expU. Any frequency-count saving would be a speedup on a 35-year-old theorem and would confirm the item. I rate it low-medium because of two real mismatches: the label budget is entropy (L log L), while Bourgain is L^2; and Bourgain's operator sums over theta inside the absolute value, while GridBound takes a sup over one modulation. Also check that the rough dyadic-average variant has a known (log N)^2 bound before using it.
3. **S1: Walsh-Carleson theorem via the label route.** This is a known theorem with a tile proof of about 20-30 pp. and no formalisation. It is statable in under 300 lines (Walsh-Paley functions on [0,1)). If O1 works it becomes a corollary. If O1 stalls, an L^2-only version measures whether the label lemmas shorten a tile-free proof.
4. **S3: Walsh L log L log log log L (Sjolin-Soria).** This is a known Walsh theorem strictly weaker than O1. As a speedup target it compares the label route against extrapolation from weak-L^p Walsh-Carleson bounds. It is statable in under 300 lines and shares definitions with S1.
5. **O3: Variational Carleson in L log L.** This is likely new and the Fisher budget is unchanged. It is statable in under 300 lines with OAI's symmetricPartialSum. It is the target that most needs the GENERAL-multiplier Prop dyadic, so it doubles as the test of whether the epsilon_j specialisation costs anything downstream. It is in the same family of problems, so it is weaker evidence than S2.

## Precedent

There is no earlier equivalent of the full device (F1 verdict, unchanged; no new web search in this pass). Every ingredient is precedented, so the N2 ("new bridge") risk stays real. No post-Oct-6 use was found.

**Lean-specific caveat for any speedup run:** remove `paperMain`, `almost_everywhere_fourier_convergence` and `gridProof` from the library. Otherwise Carleson, KSP and every L^p result are trivial corollaries.
