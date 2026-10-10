# Family 188: novelty pass, "The sharp terminal leave in random triangle removal"

## Verdict
- **Provenance flag: no.** The only 2025–2026 citation is Joos–Kühn, arXiv 2412.15039 (v1 Dec 2024, v2 Aug 2025). It is human-authored, and neither its abstract page nor its full text contains any AI-assistance wording. Four web searches pairing the problem with ChatGPT, GPT-5, OpenAI or "AI-assisted", or with the sharp constant, found no model-produced precedent. They also found no human proof of the constant.
- **family_D = D3 (provisional), confidence 0.4.** It rests on C1, the max-norm semigroup stability via star averaging.

| Candidate | Items | Final N | F | Conf. |
|---|---|---|---|---|
| C1 max-norm semigroup via star averaging | I23–I26 | **N3 (prov.)** | F5 (+F2) | 0.40 |
| C2 o(1/D) collision bound (witness + suffix template + off-pattern visitation) | I32–I40 | N2 | – | 0.60 |
| C3 Lean-only self-contained prefix via moving-star codegree stability | L04–L06 | N2 (variant of C1; evidence for C1) | – | 0.50 |
| C4 paired test with joint ordering | I10–I12 | N2 | – | 0.65 |
| C5 independent unfolding / cavity identities | I13–I17 | N0 | – | 0.65 |
| C6 two-root moments + first-repetition coupling | I30–I31, I41–I42 | N1 | – | 0.75 |

The constant 1/(2√2) itself is **N0**:
- It is Joos–Kühn's Conjecture 16.2. I checked it from JK's §16 heuristic: with k=2, e=v=3 and aut=6, p = 2^{−1/2}n^{−1/2} and R = n²p/2.
- It is also Spencer's survival law.

## Bohman–Frieze–Lubetzky (checked in full text, arXiv 1203.4223v3)
- **What BFL prove.** BFL 2015 prove F_n = n^{3/2+o(1)}. The upper bound uses scalar self-correcting martingales on the triangle count and codegrees. To get past the n^{7/4} barrier they rely on "carefully chosen triangular extensions".
- **Their final phase** appears only in the lower bound (Sec. 6). From time i₀ they use a uniform permutation of triangles and local events E_uvw, giving n^{3/2−O(ε)}.
- **No constant.** BFL neither state nor conjecture a constant. They use no branching process, no tree coupling and no spectral or operator argument.
- **Relation to the candidates.** BFL is the human route that the Lean prefix (C3) replaces. It is genuinely different from C1 and C2. The 2010 note and the 7/4-barrier paper also track codegrees in scalar form.

## Other precedent checks
- **Joos–Kühn.** This is the paper's only black box (Lemmas 7.15 and 10.1). Its heuristic is a Poisson-degree ODE, not a branching process. JK explicitly leave the constant open. It contains none of C1–C4.
- **Spencer 1995** (cited) is the source of the unfolding and the scalar law, so C5 is transfer. **Spencer's "Real Time Asymptotic Packing" (1996/97)** is *not cited*. It analyses a modified greedy with growing D and leave O(ND^{−1/k}log^c D), which is neither sharp nor a tree coupling.
- **Nguyen–Onak 2008 and Yoshida–Yamamoto–Ito 2009** (not cited) have the same recursive random-rank oracle as C4 and the same 1/ℓ! decreasing-path bound used in C2. Penrose–Sudbury (cited) has the same factorial decay.
- **Local-limit analysis of greedy MIS** (arXiv 1907.07216) has tree recursions with fixed degree. That makes it a close variant of C5 and different from C2.
- **Chung–Graham** (trace method) and **Engel–Nagel** (Dyson expansion) are close variants of *sub-steps* of C1. So are the classical line-graph identity BᵀB = 2I + A(L(G)) and the mixed-norm remainder trick of random-matrix local laws.

## C1, the strongest candidate
- **Test 1, pass (moderate).** Two searches (one extended) plus a full reading of BFL and JK found no argument that does both of the following:
  - controls the max-norm heat semigroup of a quasirandom edge operator;
  - does so by splitting it into star averages, which factor through vertex space (P = UV, VU = I + W), plus an ℓ²-small remainder handled by a mixed-norm Dyson expansion.

  Every step on its own is classical.
- **Test 2, pass.** Nothing of this kind appears in the goal or in L.
- **Test 3, pass by knockout; the proxy fails** (dominated share 0.035). Without C1 the semigroup costs e^{O(D)}. The same device also drives the Lean-only prefix (C3), so it pays off beyond its own proposition.
- **Test 4, not run.** The estimated pivot distance is 2–3 from L, and the chain depth is 2.
- **Grade: provisional N3, F5.** The low confidence reflects that each step is one move from a classical tool.

## C2: downgraded to N2
C2 is load-bearing, with dominated share 0.317, the only continuation item above the 20% proxy. It is also non-analytic. But every component has a close neighbour:
- tree-likeness certificates (Spencer; local limits);
- decreasing-path 1/ℓ! bounds (Nguyen–Onak; Penrose–Sudbury);
- rooted-extension bounds (JK Lemma 7.15).

What is new is quantitative: the off-pattern weights b = q² that turn D^ℓ into poly(D), and the length-independent D^{−B} gain from the suffix template.

## C3: the Lean-only prefix
The Lean does not cite JK. It proves the good-prefix event (failure ≤ exp(−(log n)^{4/3})) in about 7k exclusive lines. It does this by:
- writing the centred codegree vector's drift as −rate·(P_k + R_k), with a moving star average;
- keeping that vector under a max-norm barrier by mixed-norm stability;
- using Freedman's inequality, re-proved in the Lean, for the noise;
- tracking wheels and balanced templates by drift plus noise.

Against the literature this is genuinely different from BFL and JK. Inside the family, though, it is C1's device reapplied, so it grades **N2**. It is the strongest evidence for C1, because it is the downstream-reuse signature that PLAN step 9 looks for. It is not a held-out test, since the same model produced it on the same problem.

## Bridge novelty
- **Known routes:**
  - branching processes → greedy packing (Spencer 1995);
  - cavity / BP (Lean naming);
  - martingales (BFL, JK);
  - random-rank oracles (Nguyen–Onak; known but not cited).
- **New bridges** (no precedent found):
  - link-spectral (trace-method) control → stability of a removal process;
  - semigroup perturbation theory applied to this process.

## Discoverability protocols (summary; full text in JSON)
- **Eligible models:** training cutoff before 2026-09-25. The OAI preprint and repository are excluded, and the canary probe from the JSON applies.
- **P-C1:** hide I23–I26 and everything downstream, including L04–L06.
  - Arm A gives the link trace and star approximation.
  - Arm B gives only the linearized ODE and the remark that the trivial bound loses e^{O(D)}.
  - Equivalence: a structured part with an ℓ∞ semigroup bound, plus an ℓ²-small remainder, plus a norm-switching expansion.
  - k = 1..64.
- **P-C2, P-C3, P-C4:** as in the JSON. P-C3 has arms with and without C1.

## What would downgrade family_D to D2
- Test 4 arm B for C1 exceeds the threshold.
- An expert identifies a prior star-average or line-graph ℓ∞ semigroup argument, in process analyses or in random-matrix work.
- The Lean prefix route turns out to be folklore.

## Caveats and open questions
- **Correctness.** All grades assume the proof is correct. The family analyst found no gap. The Lean proves the exact comparator without JK and with no sorry or axiom. However, it was not built here, and the comparator is absent from `formalization.yaml`.
- **Open questions:**
  - Can C3 be written up as a short human proof of the BFL/JK prefix for triangles?
  - Does C1 extend to general strictly 2-balanced F?
  - Should the downstream test use BFL Theorem 1 as the held-out target?
