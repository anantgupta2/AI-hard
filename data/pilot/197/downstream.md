# Family 197: downstream targets for the incidence criterion

Analyst role: downstream targets (Lean shortlist). Date: 2026-10-09. Machine-readable version: `downstream.json`.

**Item.** This is the incidence criterion of the characteristic-2 paper (CT), `thm:criterion` at `02-criterion.tex:10`. Its hypotheses are:
- ℓ is an odd prime, and K is a finite field of characteristic 2 containing ζ_ℓ;
- V is a finite set of points and F a family of subsets of V;
- every point lies in exactly ℓ+1 members of F, and the incidence graph has girth ≥ 12;
- there are vectors x_v ∈ K^m with Σ_V x_v x_vᵀ = −I_m and Σ_{v∈f} x_v x_vᵀ = 0 for every f ∈ F;
- 0 < m < t ≤ mℓ², where t = |V|.

Its conclusion: there are a finitely presented group G with an element of order ℓ, and a, b ∈ K[G], with ab = 1 and ba ≠ 1.

Item type: F5 (F3 flavour), a lemma-type certificate.

All Lean work was done at text level. Nothing was compiled.

## Part A. Declarations pinned down

**lean_status: `as in paper`.** The criterion's conclusion is proved from its hypotheses by the paper's own route, and it lies on the comparator path. The statement is split into two declarations and its hypotheses are Skolemized.

| Declaration | File:line | Role |
|---|---|---|
| **`ChosenCriterion.products`** | DirectFiniteness/ChosenCriterion.lean:42 | **The criterion as formalized.** Hypotheses: char 2; ℓ+1 faces per point (via `assign`, a bijection with `Option (ZMod ℓ)`); `egirth ≥ 12`; X·Xᵀ = −1; local Gram sums are zero; card m < card V; distinct (slot, α) pairs. Conclusion: aOut·bOut = 1 and bOut·aOut ≠ 1 |
| **`CharacterTwist.matrix_products`** | CharacterFormulas.lean:25 | **The characteristic-free algebraic core.** It needs only \|A\|, \|C\| ≠ 0 in K and an abstract subgroup decomposition |
| `CharacterTwist.square_witnesses` | AlgebraicCriterion.lean:63 | The existential twin. **Not on the comparator proof path** according to the extractor |
| `Rectangular.U/T/identities` | Rectangular.lean:13–24 | Glued averages give UP = U, PT = T, UT = 1 |
| `AssignedDevelopment.subgroup_decomposition` | AssignedDevelopment.lean:83 | Σ_{K_v} u = 1 + Σ_{f∋v}(Σ_{L_f} u − 1) |
| `AssignedDevelopment.point_injective` | AssignedDevelopment.lean:49 | Girth ≥ 12 makes each K_v embed (dominated share 0.078) |
| `AlgebraicPacking.transpose_mul_ne_one` | AlgebraicPacking.lean:70 | m < t detects the reverse defect, by rank |
| `sum_complement_gram` | Pairing.lean:237 | The pairing, "with no characteristic simplification" |
| `Prescription.X_global`, `X_local` | PrescribedData.lean:86/88 | The prescribed data meet the criterion |

### Comparator chains
- **KaplanskyDirectFiniteness.** `main_theorem` → `prescribed_main` → `prescribed_products` → **`ChosenCriterion.products`** → `subgroup_decomposition`, `point_injective`, **`matrix_products`** → `Rectangular.identities`, `prescribed_packing_products`, `defect_ne_zero` → `transpose_mul_ne_one`.
  - The data come from `Pairing` (the pairing) and `PrescribedIncidence.succeeds_217` (the hypergraph).
- **KaplanskyFinitelyPresented.** `thm_main.1` = the same `prescribed_products`, plus `prescribed_finitelyPresented` and `prescribed_odd_prime_order`.
- **GroupRingDeterminant.** This uses only the **existential** `KaplanskyCounterexample.main_theorem`. It is a theorem corollary.
- **OddKaplansky.** This does **not** use the criterion. It imports only `DirectFiniteness.ReducedWalks`.

### Gaps between the paper and the Lean
- No single declaration states thm:criterion. It is split into a characteristic-free core and a char-2 instance.
- "Exactly ℓ+1 members" becomes an explicit bijection with the ℓ+1 lines of F_ℓ².
- "t ≤ mκ" becomes a supplied injective (slot, form) assignment.
- In general the group is shown to be finitely generated only. Finite presentation and the order-ℓ element are proved only for the **prescribed** instance.
- Novelty's proposed Lean target `square_witnesses` is dead code. Use `ChosenCriterion.products` or `matrix_products` instead.
- **The comparators are weaker than the family headline.**
  - The torsion-free result over F₂ (TF) is not formalized.
  - Nonsoficity is not formalized.
  - CT's cellular-automaton statement is not formalized.

### Family 196 precedent: not a precedent for the criterion
- Family 196's paper (ZD, dated **Sep 23, the same day as CT**) builds αβ = 0 from coned labelled graphs: odd-degree product graphs have even components, which cancel in characteristic 2.
- It has no subgroup averages, no rectangular identity UT = I_m, no character packing and no rank-violating size bound.
- The shortlist's "against" note is about the **TF headline (Oct 4)**, which adapts ZD. TF does not contain the criterion.
- The overlap is thematic only: characteristic 2 kills an even incidence count, and finite-geometry lines appear in both. **No downgrade.**

## In-release reuse
- **OD (odd characteristic): a sibling schema, not reuse.**
  - It uses the same architecture type: local idempotents glued along combinatorial data, plus a size ratio that beats the rank bound.
  - Its local mechanism is different.
  - OD says: "The characteristic-two theorem is not an input to this odd-prime argument" (OD 01-introduction.tex:57–58).
- **DT:** a theorem corollary.
- **TF:** no reuse; it uses the family 196 mechanism.
- **Families 285 and 294:** no reuse.

## Part B. Targets

**Main finding: the criterion looks characteristic-portable.** This is my own reading, not a claim made in the release.
- **Where CT uses characteristic 2:** only to make the regular degree D = ℓ+1 vanish in K. Summing the line identities gives D·Σ_V W_v = 0 while Σ_V W_v = −I. See `03-pairing.tex:103–106` and `05-prescription.tex:64`.
- **CT's own choice already covers the odd case.** CT picks ℓ ≡ −1 mod q^100 with q = 2^h. Taking q = p^h instead makes D vanish in characteristic p and gives κ = ℓ² ≡ 1.
- **The Lean core is already characteristic-free:**
  - `matrix_products`;
  - `Rectangular.identities`;
  - `Pairing.sum_complement_gram`.
- **The char-2 assumptions sit in about 6 files:** ChosenCriterion, PrescribedFields, FrameTransport, PlaneOperators, SlabAssembly and PrescribedIncidence. In PlaneOperators, `CharP Q 2` serves only to pick a quadratic extension.
- **Risk:** the hole-size estimates for odd q have not been checked.

### Speedup targets (known theorems)

| # | Target | Lean | Speedup |
|---|---|---|---|
| S1 | **Weakened OddKaplansky** (some odd p) | statable now; OD's Lean (13,061 lines) proves a stronger fixed-prime version | medium, if the odd-p extension works. The exact OD comparator (\|K\| = p⁴) is **unreachable** by the criterion |
| S2 | Existence of a nonsofic group (OpenAI, Aug 2026; Fournier-Facio arXiv:2608.02025) | needs a major library (sofic groups, Elek–Szabó) | high, but corollary-like |
| S3 | TF torsion-free result | statable now | **none**: a negative control, since the criterion needs finite subgroups |

No strong known-theorem speedup target was found outside the release.

### Open problems

| Problem | Status | Confidence | Lean |
|---|---|---|---|
| **O1. DF in odd characteristic p (e.g. p = 3)** | open except OD's single prime | 0.35 | **statable now** |
| **O2. A small, machine-checkable certificate** (cf. Gardam; SATURN) | open; CT's prescription is unexecuted | 0.25 | **statable now**: the hypotheses are decidable on finite data |
| O3. Is every hyperbolic group sofic? (Ozawa, in Pestov arXiv:0804.3968, Q 9.2). It would follow if the glued group N is hyperbolic | open | 0.10 | needs a major library |
| O4. Normalized Sylvester rank functions in characteristic p | not posed in this form; the CT data refute it for K[N] | 0.5 | < 300 lines |
| O5. Search Thompson's V and Ã₂ lattices for embedded criterion configurations | open | 0.05 | needs a major library |

**Theorem corollaries** (not counted as reuse):
- DT, which is formalized via `main_theorem`;
- the failure of Gottschalk surjunctivity;
- nonsoficity of G and N;
- failure of stable finiteness.

**Negative controls.**
1. **Characteristic 0** (Kaplansky). The criterion's hypotheses are unsatisfiable there, since (ℓ+1)·(−I) = 0 forces ℓ+1 = 0 in K. This is a proved-false analogue.
2. **Sofic and residually amenable groups** (Elek–Szabó; Ara–O'Meara–Perera).
3. **Torsion-free groups** (the TF setting).

## Top 5 (Lean-usable first)
1. **O1: DF in characteristic 3.**
   - This is the decisive device-reuse test: the same certificate applied to a new instance of the conjecture.
   - It is statable now, and the Lean core is characteristic-free.
2. **Weakened OddKaplansky.**
   - The same experiment, measured against OD's 13,061-line formal proof.
3. **O2: a small certificate.**
   - Tests whether the design produces other witnesses. Any instance found is checked for free by `ChosenCriterion.products`.
4. **O4: rank functions.**
   - Statable in under 300 lines.
   - It measures the criterion's reach, not a jump.
5. **O3: a hyperbolic nonsofic group.** The highest payoff, but not Lean-usable and low confidence.

## Precedent
- **After 2026-10-06:** none found.
- **Earlier equivalent:** none found.
- **Family 196:** contemporaneous and thematic only, not an equivalent.
- **Search limits:** web search was rate-limited for part of the session, and zbMATH was not queried. An expert check is still advised (Jaikin-Zapirain, Thom, Elek), especially on O1.
