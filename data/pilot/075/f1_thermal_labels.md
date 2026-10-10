# F1 downstream-use report: thermal noisy labels (family 075, slug `thermal_labels`)

**Item.** The cluster I26 + I27 + I10 from `family.json`, provisionally graded N3, F1 (F5 flavour). It has three parts:
- thermal noisy labels Z = Y + θ with θ ~ K_A;
- label updates A⁺ = A + S_p + D_i;
- the two-law (true input P vs uniform output U) Fisher-sum identity.

**Machine-readable version:** `f1_thermal_labels.json`, same folder.

**How this was produced.** I read the following:
- the paper sections 01 (structural argument), 05 (thermal), 06 (procedure and budgets), 08 (label-valued moments) and 09 (decoding);
- the Lean files Thermal/{Form, Order, Piece, Spatial, History, Update, Ginibre}, Procedure/{Capital, Deficit, Fisher} and Assembly/Phase.

## 1. The item, precisely

**Definition** (05-thermal.tex:11-28, 111-158).

*Thermal form:* A(y) = Σ_s λ_s(1 − Re χ_s(y)), with λ_s ≥ 0. From it:
- q_A = the Fourier coefficients of e^{−A};
- F(A) = −log q_A(0), the free energy;
- K_A = e^{F(A)−A}, a probability density on 𝕋;
- Δ_A(u) = ‖1 − χ_u‖_{L²(K_A)};
- B_A(r) = {u : Δ_A(u) ≤ r}.

*Label:* the input point Y has the true law dP = (ρ/m_top) dU. It is observed through Z = Y + θ mod 1, with θ ~ K_A.
- Errors are independent given Y.
- No choice the procedure makes ever looks at a sampled label.

*Update:* on each successful spectral update at interval p:
- the form becomes A⁺ = A + S_p + D_i, where S_p = R_p²(1 − Re χ₁) and R_p = |p|⁻¹;
- D_i = λ·(averaged cost over a compressed frequency set), chosen where the free energy is flat (eq. source-5);
- a fresh type-A⁺ label is drawn.

*Two-law Fisher sum* (06-procedure.tex:170-183, 611-630). At a final live state p, define
- M_±(z) = E_{p±}[a(Y)K_A(z−Y)]/α_e;
- D = (M₊ − M₋)/2 and M = (M₊ + M₋)/2;
- J_p = ∫|D|²/M dz.

Under the true law P, (α_e/m_p)·J_p is exactly the expected squared bias of the next spatial bit of Y given Z. Two facts then bound the total:
- Bias² ≤ 2·KL(bit ‖ fair).
- The entropy chain rule bounds the sum of these KL terms.

The result is Σ U(p) α_e J_p ≤ C d, where d ≈ log‖ρ‖_∞ is the layer height.

*Decoding* (09-assembly.tex:159-170). With c_A(n) = ∫χ_n K_A = 1 − Δ_A(n)²/2 ≥ ½:

> ∫ χ_n(z) 𝔞_p^s(z) dz = c_A(n) · c_p^{s+n}.

So one label-valued moment encodes the scalar modulation at every frequency s + n with n ∈ B_A(r_sep).

**Lean** (a finite version: labels are integrated, not sampled):
- `Thermal.label` and `Thermal.channel` (= `label.send (x + ·)`);
- `Update.next` (= `A + place p M + u.changeForm`);
- `Procedure.fisher` and `bit_def`, `space_deficit`, `fisher_bound`;
- `duet_decode`, which is the decoding identity.

The Fisher lemmas take an arbitrary channel `k : Grid M → Law α`. The thermal choice enters only through `channel s.fund.mood`.

**Obstruction dissolved.** Prop dyadic needs a bound of order d on ∫ max_u |Σ c_p^u ε_j r_{j+2}| that is uniform in the number of frequencies u.
- For one frequency, the scalar entropy/chain-rule argument suffices.
- For a supremum over frequencies, chaining or union bounds lose a factor in the number of frequencies (the Kolmogorov–Seliverstov–Plessner, Rademacher–Menshov and Bourgain-lemma type losses).
- Known Carleson proofs avoid that loss with time-frequency tiles. Those tiles are lossy at L log L: the best previous result is Antonov's L log L log log log L.

The label replaces the many costs with **one** information budget. That budget is the Fisher sum, which is O(d) independently of how many frequencies are decoded. Every frequency in a Δ_A-ball is read from the same moment at a loss of at most 2. When frequencies outside the ball are large, A is tightened, and the cost is paid in one of two ways:
- regular updates are paid by likelihood evidence;
- cheap updates are paid by the gap potential F(A) − log|B_A(r)|.

So the cost of information and the cost of choosing frequencies are kept separate. Information is charged under P and then converted into path bounds under U.

**Abstract mechanism (field-independent).** To bound a supremum over many linear statistics (characters) of a hidden variable, follow four steps:
1. Adjoin a noisy side-observation Z = Y + θ. The noise must be shift-invariant with nonnegative Fourier coefficients, i.e. a ferromagnetic Gibbs density.
2. Every statistic in a ball of the noise metric is then decoded exactly from the Z-conditional moments, with loss factor near 1.
3. The squared conditional biases along the filtration are a Fisher information. Their sum is paid once by the entropy of the hidden variable (chain rule + Pinsker), counted under the input-weighted law and transferred to the output law.
4. When too many separated statistics are large, tighten the noise. Pay for the tightening with a free-energy-minus-packing monovariant or with likelihood evidence.

In short, a single noisy side-channel, paid for by entropy, replaces a union bound over frequencies.

## 2. Downstream candidates

| # | Problem (status) | Match | Adaptation sketch | Payoff | Conf. |
|---|---|---|---|---|---|
| C1 | **Walsh–Fourier series a.e. in L log L**: open; best known L log L log log log L (Sjölin–Soria/Antonov; Di Plinio arXiv:1312.0398) | exact (modulated dyadic martingale) | Ising-type forms Σλ_s(1 − w_s) on ℤ₂^M; GKS replaces Ginibre; decoding is exact under dyadic addition; the Lean Fisher lemmas are channel-agnostic; no Fourier transfer is needed | resolves | med-high (device), med (full proof) |
| C2 | **Vilenkin bounded type, L log L**: open; best known L log L logloglog L (Oniani arXiv:2002.00350) | exact | clock-model forms on ∏ℤ_{m_j}; m-ary Pinsker | resolves | med |
| C3 | **Sharp log-power in Bourgain's multi-frequency lemma**: (log N)² upper bound; exact power open (NOT arXiv:0912.3010; KMT arXiv:1504.04132; Krause arXiv:2502.12887) | strong: the loss *is* the frequency count | label form over the N centres; the gap potential's packing term log\|B_A\| ~ log N is the only loss; needs an L² analogue of the two-law transfer | possible (log N)² → log N | low-med |
| C4 | Konyagin lacunary conjecture, L log log L: open (Lie arXiv:1902.03630; Di Plinio arXiv:1304.3943) | partial | budget would need to be log d, not d | new bound at best | low |
| C5 | Optimal Orlicz class between Konyagin's divergence class and L log L: open | calibration | needs an o(d) Fisher sum | speculative | low |
| C6 | Ergodic averages along n² (and polynomials, primes) in L log L: fails in L¹ (Buczolich–Mauldin), holds for p > 1 (Bourgain) | partial (multi-frequency at rationals) | labels built from major-arc frequencies | new bound at best | low |
| C7 | Return-times theorem near L¹ (DLTT; Demeter 1/p + 1/q < 3/2) | medium (needs a Carleson-free engine) | label-based Prop dyadic as the Carleson input | range extension | low |
| C8 | Cubic partial sums on 𝕋^d in L log L (Antonov: L(log L)^d logloglog L) | medium | one joint label on 𝕋^d with 2^d-ary digits | L(log L)^d → L log L? | low-med |
| C9 | Polynomial Carleson near L¹ (Lie arXiv:1105.4504) | medium, but decoding fails for nonlinear phases | needs noise on a nilmanifold with a positivity theorem (none known) | — | low |
| C10 | Nonlinear SU(2) Carleson (arXiv:2507.05124; SU(1,1) counterexample arXiv:2605.25108) | weak | none convincing | none | low |
| C11 | Stein/Zygmund Lipschitz-direction problems beyond release family 083 | medium-weak | swap 083's Lacey–Thiele input for the label engine | simplification only | low |
| C12 | Variational Carleson near L¹ (OSTTW, JEMS 2012) | strong (same family) | variation instead of max in Prop dyadic; Fisher budget unchanged | likely new endpoint result | med |

The JSON has each candidate's full sketch and difficulty. **Honest summary:** the strong matches (C1, C2, C12) are all "the same theorem on another group, or a stronger norm". The only truly *different* problem with a strong obstruction match is C3, and it is low-medium confidence.

## 3. Reuse within the release

No other family uses thermal labels, the update rule or the two-law Fisher identity. I grepped all preprint .tex files for the device's vocabulary; the Ginibre hits outside 075 are ordinary statistical-mechanics uses.

- **Closest sibling: family 093** (dimension-free log-Sobolev; 01-introduction.tex:166-178). It predicts w(Y) from Gaussian noisy observations Y + √r G and does entropy-loss accounting. This is the same "noisy side-channel plus entropy budget" pattern, but standard (stochastic-localization style): there is no character decoding and no adaptive tightening.
- **Families that could use the device:**
  - 083: its Lipschitz-direction Hilbert transform uses Lacey–Thiele tiles for the Carleson-along-lines step;
  - 082: triangular Hilbert transform;
  - 154: mixing ergodic averages;
  - 080: Schrödinger maximal estimates.

## 4. Speedup targets (known theorems)

1. **Carleson's theorem (L²).**
   - Lean `fpvandoorn/carleson`: about 2.41 MB of Lean, proving a generalisation; the blueprint is 130 pp.
   - The 075 Lean proves the stronger L log L statement in 1.28 MB / 29.2k lines, without importing Carleson. About 10k of those lines (53 of 155 files) touch the label/Fisher machinery.
   - Cross-check: family.md puts the "~29.2k lines" at 156 files; a fresh file count gives 155.
   - The comparison is confounded by the compression lemma.
2. **Walsh–Carleson theorem** (Billard; Sjölin). About 20–30 pp via Walsh tiles (Thiele's CBMS notes); no Lean exists. This is the cleanest home-turf measurement.
3. **Bourgain's multi-frequency lemma** in a finite/dyadic model. About 8–12 pp; not formalised. This is the frequency-count-free test.
4. **Kolmogorov–Seliverstov–Plessner** (Σ|c_n|² log n < ∞). About 3–4 pp; a sanity check, but the speedup ratio will be small.
5. **Control: scalar dyadic entropy/Fisher bound** (the A = 0 case: `no_label`, Procedure/Fisher.lean:51). The device should give no gain here.
6. **Negative control: Rademacher–Menshov.** The loss is sharp for general orthonormal systems, so any "speedup" would signal a broken evaluation.

## 5. Precedent and contamination

**No equivalent of the full device was found.** No information-theoretic or noisy-observation proof of a Carleson-type theorem exists in my searches; every known proof is tile-based. Each ingredient does have a precedent, however:
- **The noise law:** K_A is a centred **generalised von Mises** density (Maksimov 1967; Gatto–Jammalamadaka 2007), i.e. a one-site plane-rotator Gibbs measure. Its positivity is Ginibre 1970, which the paper cites.
- **Noisy observations paid for by entropy:** progressively sharper noisy observations of a hidden variable, with total information paid by entropy, is **stochastic localization** in its information-theoretic form (El Alaoui–Montanari arXiv:2109.00709) and the pinning lemma (Montanari 2008; Raghavendra–Tan 2012).
- **Squared biases summed over scales:** "Σ over scales of squared conditional bias ≤ relative entropy" is Tao's **entropy decrement** (arXiv:1509.05422) and a folklore dyadic bound.
- **Selection paid in information:** paying for an adaptively selected statistic with information instead of a union bound is **Russo–Zou** (arXiv:1511.05219), and noise injection is the Gaussian mechanism.
- **Character recovery:** recovering characters from a positive-definite kernel on a metric ball is Bohr-set / large-spectrum duality.

**Verdict.** I found no earlier equivalent that would force N0. The combination is new: input-law charging, exact frequency-count-free decoding, and adaptive free-energy/packing tightening. But the abstract mechanism is recognisably a **transfer of the stochastic-localization / information-budget template into Carleson theory**, so the N2 risk the family analyst flagged is real.

**After Oct 6, 2026:** no use or discussion of the device found. Press coverage lists 075 by title only, and `history.md` has no 075 entry.

## 6. Top 5

1. **C1, Walsh L log L.** Identical obstruction, exact decoding, classical GKS positivity. The Lean is already dyadic, finite and channel-agnostic, so this is close to a transcription. It shows the device is portable, but a judge may call it the same theorem.
2. **C3, Bourgain's multi-frequency lemma.** This is the purest instance of "loss in the number of frequencies". The packing term log|B_A| ~ log N suggests a possible (log N)² → log N improvement. It needs an L² version of the two-law transfer. It is the most informative test of whether this is a real cross-problem eureka.
3. **C12, Variational Carleson near L¹.** The Fisher budget does not depend on how many frequencies are decoded, so the move from max to variation looks natural. Likely a new endpoint result, but in the same family of problems.
4. **C2, Vilenkin bounded type.** C1 with m-ary digits and clock-model Ginibre: a genuine open problem with a clear path.
5. **C8, Cubic sums on 𝕋^d.** A joint label might avoid iterating one-dimensional bounds (the L(log L)^d loss). Speculative.

## 7. Exact Lean source

Every snippet is verbatim and under `data/raw/openai-math/lean/OAI/Analysis/FourierLLogL/`. Lemma statements are cut at `:= by`. The JSON `lean_source` field holds the full list of 21 entries.

**Definitions**
- **`Thermal/Form.lean:15-16`**: the `Form` abbrev, the coefficient form.
- **`Thermal/Form.lean:18-20`**: `wave`, `cost`, `form`.
- **`Thermal/Form.lean:89-90`**: `boltz` and `q`.
- **`Thermal/Form.lean:132-133`**: `F` and `K`.
- **`Thermal/Form.lean:162-166`**: `label`, with docstring "Label noise law centered at zero relative to counting measure."
- **`Thermal/Form.lean:181`**: `cred`.
- **`Thermal/Order.lean:89`**: `delta`.
- **`Thermal/Piece.lean:29-31`**: `channel`, with docstring "Observation type-A."
  ```lean
  def channel (A : Form M) (x : Grid M) : Law (Grid M) :=
    (label A).send (fun z => x+z)
  ```
- **`Thermal/Piece.lean:97-103`**: `omegaObs`, `Mz`, `fz`.
- **`Thermal/Spatial.lean:50-51`**: `S`.
- **`Thermal/History.lean:15`**: `place`.
- **`Thermal/Update.lean:33`**: the update rule.
  ```lean
  def next (u : Update j M p) (A : Form M) : Form M := A+place p M+u.changeForm
  ```
- **`Procedure/Capital.lean:25-26`**: `Fund.advance`.
- **`Procedure/Deficit.lean:69-76`**: `hist`, `diff`, `fisher`.
- **`Procedure/Fisher.lean:55-58`**: `givenD` and `massInfo`.

**Key lemmas**
- **`Thermal/Ginibre.lean:212`**: `ginibre`, the Griffiths–Ginibre covariance positivity.
  ```lean
  theorem ginibre {A : Form M} (hA : 0 ≤ A) (s t : Grid M) :
      cred A s * cred A t ≤ (label A).Ex (fun i => wave s i * wave t i)
  ```
- **`Procedure/Deficit.lean:100`**: `bit_def`, which bounds the label's Fisher information by 4 × the bit's relative-entropy deficit.
  ```lean
  lemma bit_def (s : Scene M) (k : Grid M → Law α) (hp : s.here.valid)
      (he : s.here.lev < M) (hh : 0 ≤ s.wage) (hm : 0 < s.mass) (hn : 0 < s.norm) :
      s.norm/s.mass * fisher s k ≤ 4*(log 2-sideH (step s) k)
  ```
- **`Procedure/Deficit.lean:147`**: `space_deficit`, the one-step chain-rule identity that charges the Fisher term to the entropy deficit.
- **`Procedure/Fisher.lean:118`**: `fisher_bound`, the global label Fisher sum.
  ```lean
  lemma fisher_bound :
      ∀ᶠ j : ℕ in atTop, ∀ M J : ℕ, ∀ f : Grid M → ℝ,
        (∀ x, f x ≤ exp (height j)) →
        let s := beginPlay f true
        ∀ t : Road j M s, Trusted J f t → 1/Thermal.H j ≤ s.mass →
          t.flatFee infoFee ≤ limitC* height j
  ```
- **`Assembly/Phase.lean:28`**: `duet_decode`, the exact decoding identity.
  ```lean
  lemma duet_decode (s : Scene M) (v k : Grid M) :
      ∑ z, chi k z*letter s v z = (cred (dye s) k:ℂ)*scalar s (v+k)
  ```
- **`Assembly/Phase.lean:55`**: `energy_near_channel`.

## Sources

The JSON `sources` and `search_log` fields have the full lists. Key references:
- arXiv: [1312.0398](https://arxiv.org/abs/1312.0398), [2002.00350](https://arxiv.org/abs/2002.00350), [0912.3010](https://arxiv.org/abs/0912.3010), [1504.04132](https://arxiv.org/abs/1504.04132), [2502.12887](https://arxiv.org/abs/2502.12887), [1902.03630](https://arxiv.org/abs/1902.03630), [1408.4783](https://arxiv.org/abs/1408.4783), [1304.3943](https://arxiv.org/abs/1304.3943), [math/0504067](https://arxiv.org/abs/math/0504067), [math/0601455](https://arxiv.org/abs/math/0601455), [1209.0856](https://arxiv.org/abs/1209.0856), [1105.4504](https://arxiv.org/abs/1105.4504), [2507.05124](https://arxiv.org/abs/2507.05124), [2609.31334](https://arxiv.org/abs/2609.31334), [2405.06423](https://arxiv.org/abs/2405.06423), [2109.00709](https://arxiv.org/abs/2109.00709), [1509.05422](https://arxiv.org/abs/1509.05422), [1511.05219](https://arxiv.org/abs/1511.05219), [2105.00833](https://arxiv.org/abs/2105.00833)
- Other: [mathnet sm8303](https://www.mathnet.ru/eng/sm8303)
