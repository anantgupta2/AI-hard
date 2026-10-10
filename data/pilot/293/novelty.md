# Family 293: novelty pass

Prepared 2026-10-10. The Lean was read at text level only; it was not compiled. Web evidence comes from search-result snippets only: WebFetch failed (ar5iv DNS error) and arXiv is blocked.

## Provenance verdict: **no**

- **No model-produced prior work was found.** The only 2025–2026 works cited are both human:
  - Kérchy 2026 (CAOT), cited for context;
  - Kérchy–Pearcy 2025, an equivalence claim that has been withdrawn.
  - Their snippets show no AI-use statement. The abstract pages could not be fetched.
- **Searches came up empty.** I searched for the HSP, the Zhu–Fang–Shi question and the relative ISP in the hyperfinite factor, each together with ChatGPT, GPT-5, OpenAI and AI-assisted. Nothing model-produced came back.
- **Intra-family dependence only.** BI imports two elementary lemmas from IP, its same-day companion. IP is model output, so it is removed from L for tests 2 and 4.

## Final grades

| Candidate | Items | N | F | Conf. |
|---|---|---|---|---|
| **E1** Backward intertwiner across odometer fibers (two-ended opposite-drift weights; bounded V ∈ {S}' moving tails K_{≥h} → K_{≥h−1}) | B16–B18 | **N3 (provisional; test 4 pending)** | F3 (F5 flavour) | 0.45 |
| E2 Conditional convolution obstruction on ordered biased couplings | C15–C17 | N2 | – | 0.6 |
| E3 Rare-drop cost cocycle at a prescribed angle | C08, C12 | N2 | – | 0.6 |
| E4 Affiliated trace-preserving transport (named precedent: Mori, Prop 3.1) | C18, C19 | N2 | – | 0.75 |
| E5 Domar quadratic criterion; strict-descent lemma | B09–B12, B20 | N1 / N0 | – | 0.8 |

## Family verdict

**family_D = D3 (provisional), confidence 0.45.** It rests on E1 alone.

It falls to D2 in any of these cases:
- the L− arm of test 4 finds the device at a rate above the threshold. The risk is that once "a decomposable model with a commutant element that moves fibers" is suggested, the commutation recurrence is forced.
- an expert finds an earlier fibred-shift or opposite-drift construction.
- the comparators fail to compile.

**What counts as transfer (N0), not as the candidate:**
- Domar unicellularity;
- the odometer and recurrence;
- direct integrals;
- the II_1 route.

The candidate is only the bounded coupling of fibers.

## Problem precision

**The family refutes the hyperinvariant-subspace problem (HSP), not the invariant-subspace problem (ISP).**
- An ISP counterexample would be an HSP counterexample, but not conversely.
- The operator S has many ordinary invariant subspaces, `L^2(X;K_{≥h})`.
- So Enflo's 2023 positive ISP claim is not contradicted.

**Corollaries:**
- The transitive algebra problem is answered negatively.
- Known positive results stop at abelian subalgebras of *finite* multiplicity (Arveson for a MASA, Douglas–Pearcy for finite multiplicity). BI's transitive algebra contains `L^∞(X)⊗1`, which has infinite multiplicity, so it sits exactly in that gap.

**Direct conflicts:**
- the claimed *affirmative* HSP solutions of Garayev (arXiv 2607.16373, July 2026) and Lee (arXiv 2306.13940);
- Cho–Ko–Lee 2017, Cor 2.8.

## E1 in detail

**Test 1: pass.**
- Neighbours, all judged genuinely different or only analogous:
  - Domar, Nikolskii and Grabiner, which give the fibers only;
  - Atzmon–Sodin bilateral shifts. A single fiber cannot carry a bounded backward intertwiner, because w_{j−1}/w_j → ∞.
  - Bastian 1976, which decomposes weighted translation operators but has no hyperinvariance;
  - Dykema's Prop 2.1 / the II_1 route, an architectural analogue only. The commutant of T∈M contains JMJ.
  - ergodic cocycles with non-integrable transfer functions, a pattern-level neighbour;
  - Read and Enflo on Banach spaces, which is different.
- No neighbour turned up in searches on:
  - direct integrals of weighted shifts with commutant analysis;
  - odometer/skew-product shifts;
  - the transitive algebra problem;
  - the 2026 HSP status.

**Test 2: pass.** I judged it against the HSP as originally posed, since this is a counterexample family. The problem names no weights, no base and no intertwiner.

**Test 3: pass, by knockout.**
- V is the only non-diagonal element of the commutant that is used.
- Without V, `L^2(X;K_{≥h})` survive as common invariant subspaces.
- The intertwiner branch is about 37% of the direct-route Lean DAG lines, roughly 0.94k of 2.5k.

**Test 4: not run.** The protocol is P-E1:
- Hide B16–B21.
- Prompt arms: L−, fibers-given, directed, and an uncontrolled II1-informed arm.
- k = 1…256.
- Allowed models have a cutoff before 2026-09-27; the OpenAI release models are excluded.
- Estimated pivot distance 2, chain depth 1. There is no trace.

**Compression signal.** The same HSP conclusion costs:

| Route | Lean DAG lines (text level) |
|---|---|
| E1 (BI) | about 2.5k |
| II_1 product model | about 15k |
| Circle model | about 28k |

That is a 6–11× drop, which is a natural input for step 3b.

## Bridge novelty

| Bridge | Status |
|---|---|
| Weighted ℓ^p (Domar) → shifts | known route |
| II_1 / Brown measure → HSP (Dykema, Haagerup–Schultz) | known route |
| Ergodic recurrence/descent as the obstruction to commutant-invariant subspaces | **new bridge** (none found) |
| Probability couplings → invariant projections (IP) | new bridge, technique-level |

## Open questions

- The orchestrator should compile the comparators and check:
  - that `definition_names: []` still locks the statement definitions;
  - the two `run_cmd auxLemmasExt` edits.
- Ask experts (Bercovici, Kérchy, Atzmon; ergodic theorists) whether the fibred-shift intertwiner is known or folklore.
- Read Domar 1981 and ZFS p.264 directly.
- Find out whether the model found BI after IP or independently. Only OpenAI can answer.
