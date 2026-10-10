# Family 112: novelty analysis ("Beyond the square-root exponent for depth-three circuits")

Analyst role: novelty. Date: 2026-10-09. The machine-readable version is `novelty.json`.

Inputs:
- `family.json` and `family.md`. There is no `trace.json` and no `f1_*.json` for 112.
- The preprint source.
- arXiv pages for 2601.04446 and 1206.1775.
- The lacker.io depth-3 problem page.
- 10 web searches, listed in `novelty.json`.

**L** = Mathlib d13f23b plus the 12-entry inline bibliography. No item in L is model-produced, so L⁻ = L.

## 1. Provenance verdict first: **no**

| Work | Role | AI disclosure | Contains 112's candidates? |
|---|---|---|---|
| GKPRT26, arXiv 2601.04446 (Jan/Feb 2026) | The only 2025–26 citation; says the problem is open | None on the abstract page (seen only through the summarizer) | Absent. It is an upper-bound paper about inner product. |
| GPPST24, CCC 2024 | States the problem | None known | Absent |
| DHMTW14, arXiv 1206.1775 (2012) | Disjointness device | n/a | **C6: same** |
| IPZ01 | Sparsification; random polynomials (§1.2) | n/a | C4: close variant. C6: same. |
| PSZ00 §5 | Evaluator with a hard subfunction | n/a | C5: close variant |

Problem-level searches found no prior model-produced attack. They paired the problem with ChatGPT, GPT-5, OpenAI and "AI-assisted", and also searched the exact title. The lacker.io problem page, verified 2026-08-10, still lists the problem as open.

## 2. Final grades

| ID | Item | Test 1 | Test 2 | Test 3 | Final |
|---|---|---|---|---|---|
| **C1** | Restriction lemma: a restricted width-k CNF becomes a signed mixture of width-b CNFs with E W ≤ 1/(1−θ), with no dependence on clause count and valid for **any constant pk** (I07 + I11 + I15) | No near-equivalent found | Pass | Pass (knockout; 17% of the DAG, about 38% of the lower-bound subDAG) | **N3 provisional, F3 (F5 flavour), conf 0.50** |
| C2 | Marker mixture: c/(c+w) as a convex mixture of conjunctions (I12) | The identity is classical; its use has no neighbour | Weak pass | Pass, within C1 | N2, conf 0.60 |
| C3 | Choose b after A; the slice's exponent does not depend on b (I32) | Close variant | Borderline fail | Pass | N2, conf 0.60 |
| C4 | Good slices: corr_b ≤ 2^{−\|T\|/8} on most restrictions (I26) | Close variant (IPZ01 §1.2) | Weak pass | Pass (27%) | N2, conf 0.65 |
| C5 | The language: hash, plus a polynomial over F₂[Z]/(P), with parameter bits as input (I23) | Close variant (PSZ00) | Fail | Carrier | N1, conf 0.60 (the analyst's N2 is downgraded) |
| C6 | Disjoint sparse partition (I17) | Equivalent (DHMTW14) | Fail | Pass (proxy over-ranks it) | N0, conf 0.70 (the analyst's N1 is downgraded) |

**family_D = D3 (provisional), confidence 0.50.** It rests on C1 alone. C1 is a tool from TCS itself, not a cross-field transfer.

## 3. C1 in detail

**What it does.** Håstad-type switching needs pk below an absolute constant, and that caps the exponent at c·√n. C1 instead writes H_{T,ρ} as K + K·Σ_j (−1)^j Σ_paths Π v / Π a_{U_h}, an alternating sum over paths of successively violated "hard" clauses. Each term is then turned into ω(P)·E[J_P], with J_P a width-b CNF, using the marker mixture (C2). Finally the paths are counted *backwards* from the terminal live set with weight 1/|V_R|. That weight averages over the eligible violated clauses instead of multiplying by their number, so each step costs at most θ. Clause count never enters, and θ is small whenever b is large compared with pk. That is what allows pk to be an arbitrary constant and the exponent ω(√n).

**Test 1 neighbours.** None is equivalent.
- **Håstad H89.** It concludes a small decision-tree depth and needs pk < 1/5. The paper itself contrasts its lemma with this one.
- **Razborov's encoding proof.** Its injective encoding of bad restrictions resembles I15, but Razborov pays log w auxiliary bits where C1 averages.
- **Rossman's entropy proof (2017).** It works in the small-p regime, with clause count entering only as log m.
- **Segerlind–Buss–Impagliazzo 2002/04 and Razborov's improvement.** These work only for small p.
- **Lovett–Wu–Zhang (STOC 2020).** This is closest in spirit: a lemma valid at any constant restriction rate, with a bounded first moment of useful terms. But its conclusion is DNF term compression, not a correlation-preserving reduction in width.
- **GMR DNF sparsification.** It reduces the number of terms, not the width.
- **Impagliazzo–Matthews–Paturi 2012 extended switching lemma.** It partitions into a decision tree with p = 1/O(k).
- **Cluster expansions and Moser–Tardos witness trees.** These are structural analogues for I11 only.

**Test 2.** Pass. The goal is a lower bound on circuit size. No statement in L carries a signed L1 expansion of a restricted CNF into narrow CNFs, and none uses the quantities a_U, c_U or 1/|V_R|. The building identities are tiny and appear nowhere in the goal, as in Cook's PHP example.

**Test 3.** Pass by knockout.
- Without C1, the only width-lifting tool in L is the switching lemma, which brings back the 2^{O(√n)} ceiling.
- In Lean, the dependency closure of C1 is 346 of 2,046 proof-DAG declarations (16.9%). The Turing-machine plumbing (60% of the DAG) dilutes this; on the lower-bound subDAG of 906 declarations the closure is about 38%.

**Why the confidence is only 0.50:**
- The switching-lemma neighbourhood is dense and expert-heavy.
- zbMATH and MathOverflow were not queried directly.
- The headline breaks a decades-old barrier and has not been reviewed. Lean proves it end to end with no sorry or axiom, but it was not built here.

**What would downgrade C1 to N2:**
- an expert finds a clause-count-free expansion into narrow CNFs at constant pk in work on proof-complexity switching or AC0 correlation; or
- the Test 4 directed arm hits above the threshold.

## 4. Bridge novelty
- **Sparsification → depth-3:** a known route (IPZ01 §1.2; PPZ/PPSZ; GPPST24).
- **k-wise independence and hashing → hard slices:** a known route (IPZ01; PSZ00).
- **Sunflowers and finite fields:** known routes.
- **Random-order markers → CNF mixtures (C2):** a minor new bridge.

## 5. Discoverability protocol (Test 4, not run)
- **Models:** training cutoff before 2026-09-23. Use a canary probe that asks whether a 2^{ω(√n)} depth-3 bound is known, and whether a clause-count-free narrow-CNF expansion exists. Allow no retrieval. Exclude the OpenAI lineage that produced the release from the main pool.
- **What to hide:** I07, I08, I10–I16, the intro paragraph at 00:116-128, and 05:26-136.
- **Arms:**
  - *open*: the problem only;
  - *directed*: the problem, plus C4, C6, the counting skeleton, and the explicit gap;
  - *lemma-given*: the statement of C1, with a request to prove it;
  - *L minus H89*: tests whether the switching lemma anchors proposals in the small-pk regime.
- **Sampling:** n = 256 per arm, with k = 1, 2, 4, …, 256 and K = 256.
- **Hit criterion:** a cost W that does not depend on G and has E W bounded by a function of (pk, b) alone, valid for **every** constant pk, with correlation bounded through a class of narrow tests closed under cylinders. In Lean, derive `cnf_restriction_bound`.
- **Chain depth:** 2. C1 pays off only together with C4.
- **Pivot distance:** there is no trace. At the text level, the statement is one step from H89 in shape, but the proof takes three non-obvious moves.

## 6. Open questions
1. Ask an expert whether C1 is known. This is the main risk to the N3 grade.
2. Build the Lean and run the comparator.
3. Find out whether the rate can be made effective.
4. Run downstream-speedup targets: other pseudorandom families, depth-3 AC0 correlation, and Res(k).
5. Run zbMATH and MathOverflow queries.
6. Check the full text of GKPRT26 for an AI disclosure.
