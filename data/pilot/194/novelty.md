# Family 194: novelty analysis (Lech's multiplicity conjecture)

Analyst role: novelty, done at text level. Date: 2026-10-12. Machine-readable version: `novelty.json`.

Inputs:
- `family.json`/`.md`. There is no trace and no F1 file.
- `main.tex`, plus `sections/complex.tex` read in full.
- The comparator and the Lean files on its call chain, read as text only.
- `data/items/194_lean.json`.
- WebSearch summaries. WebFetch to arXiv, export.arxiv, alphaxiv and Wikipedia all failed (ENOTFOUND), so every literature check is at snippet level.

**L** = Mathlib d13f23b plus the paper's 29-entry bibliography. **L⁻** = L without SmallCM, the only model-produced entry. SmallCM contains no candidate.

## 1. Provenance verdict: **no**
- **The only model-produced citation is SmallCM** (openai/math family 195, the same release). It is cited at `main.tex:147-153` as motivation: Ulrich and small-CM routes cannot be universal.
  - A grep of its source finds no supernatural bundles, no blowup pairing and no complex estimate. It cites Eisenbud–Schreyer 2003 only, on exterior syzygies.
  - It is not a precedent for any candidate.
- **The 2025–2026 human citations** are CLMST (Invent. 2026), IMW2025 (arXiv:2510.02698), Bhatt–Hochster–Ma v2 and Meng v3.
  - The search snippets show no AI disclosure for any of them. Their acknowledgments were not read.
  - None contains Thm 2.1.
- **Searches for model-produced prior work.** "Lech's conjecture" together with ChatGPT, GPT-5, OpenAI or AI-assisted found nothing. The hits were Lech Mazur's Sendov work, which is unrelated.
- **No human proof found.** No 2025–2026 human proof of, or progress on, Lech turned up beyond Meng.

## 2. Lean eligibility (checked directly)
**Lech is not formalized.** `lean/docs/194.md` says "The paper's full flat-local result in arbitrary characteristic is outside it". The comparator is `OAI.Lech.dutta_domain`: IMW Conj 8.1 for complete char-p domains.

**Thm 2.1 *is* in the Lean, and it is on the comparator's dependency chain.** I verified the chain by imports and call sites:

```
dutta_domain → dutta_complete_charp (DuttaDomain.lean:22) → dutta_algClosed (DuttaAlgClosed.lean:15)
→ cyclicDuttaContribution_lower (CyclicDutta.lean:111, l.129) → CharP.dutta_lower_bound_infinite_perfect (DuttaInfinitePerfect.lean:19)
→ CharP.dutta_minimal_estimate (DuttaMinimalEstimate.lean:22, l.33) → complex_estimate_allModule (ComplexEstimateAllModule.lean:13, l.36)
→ complex_estimate_basis (ComplexEstimate.lean:88) → ReesRoot.sum_estimate + Numerical.roundedRoot
```

- `complex_estimate_basis` is Thm 2.1 for an abstract `TorsionLength`. It has the paper's parameter and Koszul hypotheses. The filtered-colimit axiom is weakened to `DirectSumZero`.
- So the N3 candidate is **Lean-backed and shortlist-eligible**, even though the headline is not.
- For the speedup test, the device to add to L is `complex_estimate_basis`, `complex_theorem` or `complex_estimate_allModule`. Dutta or Lech corollaries do not count as reuse.

## 3. Final grades
| ID | Item | N | F | Conf. | Lean-backed |
|---|---|---|---|---|---|
| C1 | Uniform complex estimate, Thm 2.1 (I08, with components C2–C4) | **N3** | F5 (F3) | 0.35 | **yes** (`complex_estimate_basis`) |
| C2 | Roots at s·(critical points of ∏(x+i)) (I17) | N2 | – | 0.7 | yes (`Numerical.roundedRoot`) |
| C3 | Blowup twist G = O(−is)^{b_i} plus local pairing positivity (I13+I18) | N2 | – | 0.6 | yes (`ReesRoot.*`) |
| C4 | Non-Noetherian Euler comparison (I15) | N2 | – | 0.55 | yes |
| C5 | Abstract stable length interface (I05) | N1 (analyst: N2) | – | 0.55 | yes (`TorsionLength`) |
| C6 | Mixed-char Heitmann depth plus two-limit scheme (I38+I40) | N2 | – | 0.6 | no |
| C7 | Char-0 one-sided certificate (I43) | N2 | – | 0.6 | no |
| C8 | Lean SeparableOrder route; Roberts re-proved | N1 | – | 0.7 | yes |

Excluded:
- The ES supernatural bundle (I16) is **N0 transfer**. It is re-proved over Z and re-implemented in Lean as about 246 `ProductSourceCover` declarations.
- The Dutta corollary and the Lean-only strengthening `dutta_complete_charp` are corollaries.

## 4. C1 in detail
**Test 1: no near-equivalent found.**
- **Nearest neighbour:** the graded Eisenbud–Schreyer / Eisenbud–Erman pairing.
  - For a graded complex over k[x₁..x_h] whose step-i shifts are at least is, pairing positivity (the HHS lower bound) gives roughly s^h·b₀.
  - C1 is the *local, ungraded, abstract-length, non-Noetherian* analogue, reached via the blowup.
  - The graded→local passage is exactly what was known to fail through associated graded rings (MaUlrich Rem. 3.9).
- **Other neighbours, all genuinely different:**
  - IMW2022 Conj 8.1 is C1's char-p consequence, proved there only under lim Ulrich hypotheses.
  - IMW2023 connects Boij–Söderberg cones to local-type rings via lim Ulrich sequences.
  - BEKS 2012 studies Boij–Söderberg shapes over regular local rings.
  - IMW2025 and IMW–Zhuang 2024 use the blowup's exceptional fibre for Ulrich questions.
  - Roberts, Kurano and Dutta 2013 work with local Chern characters on blowups.
  - Ma 2017 reaches only the d!/2^d constant.

**Test 2: pass.**
- The mechanism (blowup, twisted complex, bundle pairing, abstract length) is not a subterm of the goal or of L.
- But the *statement shape* is close to L: Ma 2017 and IMW2022 already state the desired char-p consequence. The novelty is in the proof, not in the statement.

**Test 3: pass, strongly.**
- Closure: 76.6% of the 3,499-node DAG, dominated share 0.70.
- Recomputed core share is **85.5%** (1,751 of 2,048 nodes). This excludes plumbing, the char-p length background, and the ES-bundle namespaces as transfer. The namespace filter is approximate, so this is an upper estimate.
- Every leg (char p, mixed, char 0) routes through C1.

**Test 4:** not run; see P-C1.
- Pivot distance is about 3:
  1. a deep-entry estimate (near Conj 8.1);
  2. the blowup rescale to a pure type (0, s, …, hs);
  3. the pairing with tuned roots.
- Chain depth is 3.

**Why the confidence is only 0.35.**
- Every component is precedented:
  - bundle and positivity: ES, N0;
  - division by the exceptional divisor: a standard move, N2;
  - roots: forced, N2.
- The candidate is the *assembly* that makes graded Boij–Söderberg positivity act on an ungraded local complex.
- If an expert calls this "the evident local transplant", C1 becomes a close variant, N2.
- In C1's favour: Iyengar, Ma and Walker held both ingredients, Boij–Söderberg cones (2023) and blowups (2025), and still left Conj 8.1 open.

## 5. Family verdict
- **family_D = D3** (confidence 0.35). It rests on C1, which is Lean-backed.
- **It falls to D2** on any of:
  - an expert "routine transplant" verdict;
  - a Boij–Söderberg-on-blowup precedent, which needs a full-text search;
  - a high P-C1 hit rate for a complete mechanism.
- **provenance_flag:** no.

**bridge_novelty:**

| Bridge | Classification | Basis |
|---|---|---|
| Boij–Söderberg → local multiplicity | Known route at the field level (ES/HHS, IMW2023, BEKS, IMW2022); the mechanism is new | The new mechanism is C1 itself and is not counted twice |
| Blowup → local multiplicity | Known | Rees; Roberts/Kurano; Dutta 2013; IMW 2024/2025 |
| Perfectoid lengths → mixed characteristic | Known | CLMST |
| Plus closure → mixed characteristic | Known | Heitmann, Heitmann–Ma |
| Artin approximation → char 0 | Known | Ma §5 |
| Rolle / Riemann sums → root choice | Minor new bridge | Trivial in content |

## 6. Discoverability protocols (not run)
**P-C1**
- **Hide:** §2 and all its uses. In Lean: ComplexEstimate, SumEstimate, ReesRoot, ProductSourceCover, RootUlrich, NumericalSupport.
- **Give as black boxes:** the reductions, the Cohen factorization with F = P⊗K, Ma's identity, and the normalized length.
- **Ask for:** a proof of e_HK(J+(x),T) ≥ e(T).
- **Arms:**
  - bare;
  - L: with abstracts of ES, EE, IMW2022/23/25, MaUlrich, CLMST and the others;
  - directed: with the hint "blowup + Boij–Söderberg positivity".
- **Full hit:** a coefficient-1 deep-entry bound *plus* a working mechanism.
- **Partial hit:** the statement only. This is expected to be common.
- **Judging:** an LLM judge against complex.tex, plus a Lean equivalence attempt against `complex_estimate_basis`.
- **k** = 1, 5, 25, 100.
- **Models:** training cutoff before 2026-09-23. Exclude the openai/math release (194 and 195) and post-release discussion. Claude Opus 5.5 qualifies.
- **Controls:**
  - positive: derive the HHS lower bound from the ES pairing;
  - negative: an Ulrich-route request over Yhee-type rings.

**P-C2:** give G, the pairing formula and free roots, and ask for a root choice that isolates b₀. The expected hit rate is high, since C2 is forced.

## 7. Open questions
- A full-text search of the Boij–Söderberg literature (Erman, Sam, EES, Fløystad) for pairings on blowups or Rees algebras of local rings.
- An expert view on whether the transplant is routine.
- The exact form of Heitmann–Ma Prop 2.8: genuine membership or "almost". This affects the mixed-char leg only.
- Whether C1 helps the IMW length conjecture ℓ(M) ≥ e(R). That would be a downstream target that is not a corollary.
