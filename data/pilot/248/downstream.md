# Downstream report (Lean shortlist): family 248, recursive Hilbert-ball colouring

Machine-readable companion: `downstream.json`. This report builds on `f1_recursive_coloring.json`, reusing its candidates, precedent check and Lean sources. All Lean checks are at **text level only**: no toolchain is available, and the comparator has nanoda disabled.

## Part A: is the item in the Lean?

**lean_status: `as in paper`.** partitionColor (RecursiveColoring.lean:23) is the paper's p(T) with the same recursion, the same well-founded measure (cell count) and the paper's displayed choice of intervals (selectedInterval: depth 2D, odd indices), and every step the item drives (pullback globalColor, recursive identity, exact covariance, the generic correlation core, the explicit L^2([0,1];R^2) displacement map) lies on the proof DAG of the comparator theorem, whose statement matches the headline exactly; this was checked at text level only, without compiling.

**Comparator chain** (ThompsonNonamenability; solution module `OAI.GroupTheory.Thompson.Main`):

- OAI.ThompsonNonamenability.thompson_F_nonamenable_composition (Main.lean:69; comparator target)
- OAI.ThompsonNonamenability.thompson_F_not_amenable (Main.lean:65)
- OAI.ThompsonNonamenability.thompson_F_uniform_boundary (Main.lean:45)
- OAI.ThompsonNonamenability.thompson_F_boundary_with_exact_constant (Main.lean)
- OAI.ThompsonNonamenability.exists_fixed_boundary (FiniteBoundary.lean:16)
- OAI.ThompsonNonamenability.globalColor (GlobalColors.lean:37)
- OAI.ThompsonNonamenability.optionFamilyColor
- OAI.ThompsonNonamenability.partitionFamilyColor (PartitionColorFamily.lean:29)
- OAI.ThompsonNonamenability.partitionColor (RecursiveColoring.lean:23)  <- THE ITEM

**Side branches**, all reachable from the comparator target (via `scripts/extract_lean.py` and a BFS over `uses`):

- **headline_step**: thompson_F_not_amenable -> not_amenable_of_uniform_boundary (MeanToFolner.lean:47)
- **recursive_identity**: exists_fixed_boundary -> globalColor_parent -> partitionFamilyColor_parent -> partitionColor_restrict (RecursiveColoring.lean:62)
- **covariance**: exists_fixed_boundary -> separated_correlation_bound -> globalCorrelation_translate_bound -> globalCorrelation_covariance -> globalColor_covariance (GlobalColors.lean:96)
- **generic_core**: exists_fixed_boundary -> boundaryConstant_le_of_correlations (FiniteCorrelationBoundary.lean:56) -> finite_energy_of_variance -> displacement_le_mean_energy (DisplacementEstimate.lean:23)
- **dag_stats**: scripts/extract_lean.py v2 (text-level): 879 declarations in 68 files; 572 in the comparator proof DAG. partitionColor is in the DAG, with 4.5% of DAG declarations depending on it. exists_fixed_boundary dominates 47.6% of the DAG.

**Gaps between paper and Lean:**

- NOT COMPILED: there is no local toolchain and the comparator config has enable_nanoda=false. All checks here are text-level. A grep of the 68 Thompson files finds no sorry, admit or axiom.
- Comparator vs internal results: the comparator asks only for a composition-compatible group structure on F with no InvariantMean. Main.lean also proves thompson_F_boundary_with_exact_constant and thompson_F_uniform_boundary, but they are not comparator targets. The item is on the comparator's chain either way.
- Constants are NOT numerically explicit in the Lean. displacementLipschitzConstant depends on separationAtScale := Classical.choose (gamma_uniform_separation (1/32) _) (AnalyticConstruction.lean). The transports pairTransport are Classical.choose of exists_affine_pair_transport (TransportFamily.lean:41-59). So the Lean certifies an existential boundary constant boundaryConstant L (1/2) D, not a numeral. This matters for the explicit Folner and Kesten targets (S4, S5).
- Route addition, not a gap: the forward Folner criterion (invariant mean => Folner sets) is proved in Lean (MeanApproximation, ProbabilityDefects, FiniteCoarea, MeanToFolner, about 10% of the DAG), where the paper cites it.
- The selected intervals are fixed to selectedInterval D (depth 2D, index 2i+1). This is the paper's displayed choice (finite-proof.tex:121-123, I_j=[(2j-1)2^{-r},2j 2^{-r}]). partitionColor itself is generic in I : Fin D -> BasicInterval.
- Carrier: F is a subtype of interval homeomorphisms with a dyadic PL witness (Model.lean:52). StandardCharacterization.standardPLEquiv identifies it with the standard finite-breakpoint model, so the formalisation is faithful.

The main gap that matters downstream: **L and the transports are `Classical.choose`**. The Lean therefore certifies an existential boundary constant only. Any explicit Folner or Kesten target (S4, S5) needs effective versions of `gamma_uniform_separation` and `exists_affine_pair_transport`.

Verbatim declarations (`partitionColor`, `partitionColor_restrict`, `partitionFamilyColor`, `globalColor`, `globalColor_covariance`, `displacement_le_mean_energy`, `boundaryConstant_le_of_correlations`, `exists_fixed_boundary`, `not_amenable_of_uniform_boundary`, the comparator theorem) are in JSON `lean_source`. They were re-extracted from disk, with proofs cut at `:=`.

```lean
def partitionColor (I : Fin D → BasicInterval) (hI : ∀ i, (I i).Internal)
    (hD : 0 < D) (f : UnitBall E → UnitBall E) (T : BasicPartition) :
    UnitBall E := by
  classical
  exact if h : ∀ i, T.Respects (I i) then
    f (ballMean hD (fun i =>
      partitionColor I hI hD f (T.restrict (I i) (h i))))
  else unitBallZero E
termination_by T.cellCount
decreasing_by
  exact T.restrict_cellCount_lt _ _ (hI _)
```

## Two skeptical findings on the shortlist's test

1. **The overgroup lemma trivialises any rerun that uses transports from F.** Suppose F has a uniform boundary with a fixed S in F. Then every G containing F has a uniform boundary with the same S and constant b/|S|, by decomposing A into right cosets of F. A "direct" rerun on Lodha-Moore cone partitions uses prefix-replacement transports, which lie in F. It is therefore the corollary in disguise (S6, negative control).
2. **H(A) for A != Z cannot host the device natively.** The stabiliser in PSL_2(A) of a cell contains dilations x -> lambda^2 x for units lambda of A. Projective renormalisation is then not unique, so (T_I)_J = T_{I.J} and exact covariance fail.
   - The Farey rerun works only on PSL_2(Z)-cells, i.e. on Thurston's copy of F, followed by the overgroup lemma.
   - It still tests the step from affine to projective renormalisation, and it removes Carriere-Ghys from Monod's theorem.
   - It cannot avoid the embedding of F.

So the genuinely embedding-free reruns are F_n, Stein and F_tau. These have their own unique-renormalisation cells and their own transports, but all of them also contain F.

## Part B: speedup targets (ranked Lean-usable first)

| id | target | status | expected | Lean feasibility |
|---|---|---|---|---|
| S1 | n-adic Thompson groups F_n are nonamenable, by a direct n-adic rerun of the device | true. Known since 2026-09 via 248 plus the embedding F <= F_n plus the overgroup lemma. No direct proof exists. | med | statable with < 300 lines of new definitions |
| S2 | Stein groups F_{2,3} (and F_{n1,...,nk}) and Cleary's F_tau are nonamenable, by direct reruns | true via containment of F; no direct proof | low-med | statable with < 300 lines of new definitions |
| S3 | Monod's H(A) nonamenable, by rerunning the device on Farey (projective) cells | A != Z: known (Monod, via Carriere-Ghys). A = Z: follows from 248 via Thurston's isomorphism. | low-med (removes Carriere-Ghys for every A, but only through the F copy) | statable with < 300 lines of new definitions |
| S4 | Explicit isoperimetric (Folner) constant for the generators {x0, x1} of F | open as an explicit bound (only numerics or bounds in the wrong direction) | n/a (new result); measures the definition's quantitative reach | statable with < 300 lines of new definitions |
| S5 | Explicit Kesten bound: ||lambda(x0)+lambda(x0^-1)+lambda(x1)+lambda(x1^-1)|| <= 4 - c on l^2(F) | open as an explicit bound | n/a (new) | statable with < 300 lines of new definitions |
| S6 | Lodha-Moore group G_0 is nonamenable | true (known; G_0 contains F) | none beyond the corollary (control) | statable with < 300 lines of new definitions |

Details, including `lean_feasibility` (statable_with, missing, formal_proof_to_compare), are in the JSON. Every speedup target has a statement under 300 lines. None is statable with *zero* new definitions: Mathlib has no Thompson-like groups, and as far as I know (unverified at d13f23b) no amenability or Cheeger theory. OAI supplies the generic `InvariantMean` and `not_amenable_of_uniform_boundary`.

## Open problems

| id | target | status | expected | Lean feasibility |
|---|---|---|---|---|
| O1 | Explicit cogrowth / spectral-radius bound for F (rigorous separation from 16 and 4) | open (qualitatively implied by 248; no explicit gap) | new explicit bound (first rigorous one) | statable with < 300 lines of new definitions |
| O2 | Explicit counterexample to Moore's convex Ramsey statement for finite binary trees | now false by 248, with no explicit witness | explicit finite witness generated by the definition | statable with < 300 lines of new definitions |
| O3 | Explicit fixed-point-free affine action of F on a convex compact set (nonlinear Day witness) | existence follows from 248 (Day); explicit construction open | new construction | statable with < 300 lines of new definitions |
| O4 | Uniform non-amenability of F | open | likely negative | statable now |
| O5 | Co-amenability / Schreier-graph amenability problems in F, T, V | scattered results | partial classification | statable with < 300 lines of new definitions |
| O6 | Brin-Sapir conjecture: every subgroup of PL_+(I) is elementary amenable or contains F | open | none (records the device's boundary) | statable with < 300 lines of new definitions |
| O7 | Abstract criterion: conditions (a)-(d) imply uniform boundary, for any group acting on self-similar configurations | template; no new example found outside groups containing F (see O6, S6) | reusable library lemma; no known new application | statable now |

## Theorem corollaries (not counted as reuse)

- Any group containing an injective image of F is nonamenable: Lodha-Moore G_0, H(A) for every A (via Thurston's H_Q(Z) = F), F_n, Stein groups, F_tau, T, V. Overgroup lemma: uniform boundary with fixed S in F passes to overgroups with constant b/|S| (right cosets). Lean: statable now; about 30-60 lines of proof.
- T is C*-simple (Le Boudec-Matte Bon arXiv:1605.01651: T is C*-simple iff F is nonamenable).
- F is not Liouville for any symmetric generating measure (Kaimanovich arXiv:1602.02971 context; nonamenable implies non-Liouville).
- p_c < p_u for Cayley graphs of F (family 214, Benjamini-Schramm for nonamenable graphs).
- F has a non-unitarizable uniformly bounded representation (family 251; OAI Analysis/Unitarizability has its own Amenable definition, so this is statable now in Lean given an equivalence lemma between the OAI amenability definitions).
- Moore's convex Ramsey statement for binary trees fails (non-explicitly).
- Existence (non-explicit) of a fixed-point-free affine F-action on a compact convex set (Day).

## Negative controls

- **Family 253's polygon-exchange group is amenable**: Translation-only exchanges have no scale-changing transports, so (d) fails. A prover with the device in L must not derive non-FolnerAmenable. (Lean: statable now)
- **Groups containing F (Lodha-Moore, H(A), F_n via embedding): the device should give NO speedup over the overgroup lemma**: If a 'device rerun' is cheaper than the 30-60-line coset argument, the measurement is rewarding the embedding, not the definition. (Lean: statable now)
- **Rational-rank <= 2 IET subgroups are amenable**: Translations only, so condition (d) fails (Lean: statable with < 300 lines of new definitions)
- **T and V are nonamenable via free subgroups (ping-pong)**: Not a failure but a no-speedup control: the trivial proof should win. (Lean: statable with < 300 lines of new definitions)

## Top 5 (Lean-usable first)

1. **S1: F_n nonamenable by a direct n-adic rerun.** This is the cleanest Lean speedup test available. The statement needs about 60-80 lines (copy Model.lean with base n), and there is an exact formal baseline: the 248 development (9457 lines, 572-declaration comparator DAG). The n-adic transports lie in F_n, not in an embedded copy of F, so the rerun is a genuine reuse of the definition rather than the overgroup lemma. The measurement is the prover budget with versus without partitionColor plus the generic core in L, with the embedding route (BCS plus overgroup lemma) as the control arm. Caveat: the qualitative result is already known via embedding, so this measures portability and cost, not new mathematics.
2. **S2: Stein F_{2,3} and F_tau by direct reruns.** This is the same test as S1, but with mixed-arity or irrational cell geometry. It checks whether self-similar restriction and unique affine renormalisation, the two facts the definition rests on, survive a non-uniform branching factor. The statement takes under 300 lines and the baseline is again 248's Lean. It is lower priority than S1 because it adds plumbing cost without a new conceptual test.
3. **S3: H(A) via Farey (projective) cells.** This is the shortlist's named test. My analysis says it can only run on PSL_2(Z)-Farey cells. For A != Z, PSL_2(A) contains dilations fixing every cell, so the projective renormalisation is not unique and (T_I)_J = T_{I.J} fails. The rerun therefore reproves Thurston's projective copy of F and still needs the overgroup lemma; it cannot avoid embedding F. It remains worth running as an affine-to-projective portability test, and it would remove Carriere-Ghys from Monod's theorem. The statement takes under 300 lines (piecewise-Mobius carrier). There is no formal baseline.
4. **S4: explicit Folner constant for {x0, x1}.** This has the highest mathematical payoff: the first explicit isoperimetric constant for F. It comes directly from the definition's explicit boundaryConstant formula, which Lean already proves by rfl. The statement takes under 300 lines (x0, x1 as DyadicPLWitness elements). The proof is the problem. The Lean's L and transports are Classical.choose, so it needs an effective separation constant, plus normal forms and word-length bounds for the transports. That is a major new library, so this is a discovery target rather than a cheap speedup test.
5. **S5: explicit Kesten bound for F.** This is the shortlist's 'explicit Kesten-norm bound'. It is statable with under 300 lines (l^2 regular representation plus Mathlib's operator norm), but it needs S4 plus a discrete Cheeger/Kesten inequality for infinite graphs, which is absent from Mathlib. It ranks below S4 because it is strictly harder and adds no new use of the device.

## Precedent

**Verdict (re-checked 2026-10-10): no earlier equivalent found, so N3 is not downgraded. No error report, but the theorem is still unreviewed. The item remains an N3 candidate, not a confirmed eureka step.** The 2026-10-09 pass ran no new web search. The F1 findings were:
- VibeMathed lists the result as "candidate, review pending".
- Kalai's post of 2026-10-07 mentions it without assessment.

**Web re-check, 2026-10-10.** Coverage was limited. WebSearch ran 28 queries. Every WebFetch failed with `ENOTFOUND`, and curl through the proxy got `CONNECT 403`: this is egress policy, not a rate limit, and retries did not help. The blocked pages were Kalai, VibeMathed, arXiv, Nature, X, Kingy AI and proofsandprompts, so primary pages were not re-read. The findings below come from search snippets.

- **Post-release use of the device:** none found. Searches covered reuse on F_n, Stein groups, F_τ, Lodha–Moore, Monod's H(A) and T C\*-simplicity. The newest hits do not cite 248:
  - arXiv:2603.28228 (2026) still treats C\*-simplicity of F as open;
  - Farley, AGT 26(4), 2026, is on finiteness properties of piecewise-projective groups.
- **Assessments:** no named expert verdict was found. Sources checked: Moore, Brin, Guba, Monod, Lodha, MathOverflow, Mathstodon, Lean Zulip and Quanta.
  - Kalai's snippet: the manuscript "announces" nonamenability.
  - VibeMathed's snippet restates Theorem 1.1 and the Benyamini–Sternfeld mechanism. Its status could not be re-confirmed.
  - Kingy AI lists "1 manuscript, Lean scope".
  - An X post lists the title.
  - Release-wide coverage does not mention Thompson's group F in the snippets returned: Nature, Fortune, Futurism, the AHM statement on Tao's blog, and proofsandprompts "100+ reactions".
  - No independent compile of the Lean files was found.
- **Error reports:** none for the 2026 claim. The searches surfaced only the historical withdrawals:
  - Wajnryb–Witowicz, arXiv:1408.2188;
  - Akhmedov, arXiv:0902.3849;
  - Shavgulidze, via the note arXiv:1102.0747.

  A read-only git check found github.com/openai/math `main` still at `fd4aeeb`, the merge of PR #1 "codex/update-10-7" from 2026-10-07. No Thompson or 248 file has changed since the initial commit `adc7f12`, so there is no erratum or withdrawal.
- **Earlier equivalents:** none. Re-verified nearest neighbours:
  - Moore's Følner-function tower bound (arXiv:0905.1118 = GGD 7 (2013) 633–651): scalar.
  - Moore's Ramsey reformulation (Fund. Math. 220, 2013; KST Thm 4.1): a reformulation, not a mechanism.
  - Akhmedov's height functions (1310.4395, 0902.4755). Guba disproved TSP for F (math/0508014).
  - Monod 2305.00796 (GGD 2025): affine.
  - Benyamini–Sternfeld (Proc. AMS 88, 1983) and Lin–Sternfeld: no group-theoretic application found.
  - Wiśnicki 1612.06270: a nonexpansive analogue of Day's theorem, not an obstruction.
  - Brothier–Jones / Brothier–Wijesena Pythagorean representations: linear isometry recursions.

  Searches for tree-indexed vector-valued colourings or cocycles proving nonamenability, and for fixed-point-free Lipschitz maps used for amenability, found nothing relevant.

The theorem is unrefereed, on a problem with a history of withdrawn claims. Everything downstream is conditional on it. Details, per-query log and URLs are in `downstream.json` (`precedent_check.update_2026_10_10_web`, `search_log`, `sources`).
