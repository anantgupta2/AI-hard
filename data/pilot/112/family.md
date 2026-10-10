# Family 112: "Beyond the square-root exponent for depth-three circuits"

Source: `preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/` at commit fd4aeeb. `main.tex` inputs `common.tex`, sections 00–05, the appendix `finite_fields.tex`, and an inline 12-entry `references.tex`. The catalog's `bib` field is empty.

Lean: `lean/OAI/Computability/DepthThree`. It has 179 files, about 25,000 lines and 2,652 declarations (1,655 theorems, 757 defs). It imports only Mathlib, with no other OAI dirs. There is no reasoning trace for this family. The full item list (39 items, each with Lean counterparts and DAG metrics) is in `family.json`.

Base library L: Mathlib d13f23b plus ABI86, DHMTW14, ER60, GKPRT26, GPPST24, H89, HJP95, IPZ01, Krawczyk94, PPSZ05, PPZ99 and PSZ00.

## Main statement
**Thm main** (00_introduction.tex:52-66): there is a language L ⊆ {0,1}* and a deterministic Turing machine that decides it in time C(n+1)^a, with lim log₂ S₃(f_n)/√n = ∞. Equivalently, for every A > 0, S₃(f_n) > 2^{A√n} for all n ≥ N_A.
- S₃ counts **all** gates of an unbounded fan-in OR–AND–OR circuit, including the bottom layer.
- The language is fixed before A is chosen.

This answers the "2^{ω(√n)} for an explicit function" depth-3 question. GPPST24 §1.1 discusses that question, and GKPRT26 §1 still calls it open. The prior record was 2^{1.282√n} (PPSZ05), and parity is tight at Θ(n^{1/4}2^{√n}) (PPZ99). The result is weaker than HJP95's 2^{n^{1/2+ε}} question and says nothing about Majority.

### Lean comparator and match
- **DepthThree**, target `OAI.DepthThreeLowerBound.exists_polynomial_time_language_depth_three_lower_bound`. It is proved in `Main.lean:8-16` from `language_polynomial_time` and `language_depth_three_gate_lower_bound`.
- **The match is exact.**
  - L, the machine M and the constants C, a are all fixed before A.
  - `gateCount = bottomCount + middleCount + 1` matches the paper's total count.
  - Literals are `V × Bool`, so negations are free, and constants are allowed.
  - Bottom gates can be shared through Finset indices.
  - "Deterministic TM" is rendered as a finite multi-tape machine built on Mathlib's `Turing.Tape`.
- **Formalized:** everything, end to end. That includes an explicitly compiled multi-tape machine with C = 24000·3⁸ and a = 8.
- **Route differences:** the appendix's irreducible-polynomial existence proof is replaced by Mathlib `GaloisField` with a primitive element, and Lagrange interpolation comes from Mathlib.

## Trust surface
The grep covered all 179 files and the comparator.

| Pattern | Count |
|---|---|
| `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `partial def`, `set_option`, `#eval`/`run_cmd` | 0 |
| `decide` | 169 lines in 55 files |

- Every `decide` is a Bool case split or a numeral side goal.
- The only `sorry` is the one in the comparator challenge stub, which is there by design.
- The permitted axioms are propext, Quot.sound and Classical.choice.
- Lean was not built in this pass.
- Three files import `Mathlib.Basic.Real.Basic`, which is unusual. Since 71 files across the release use it, it presumably exists at the pinned Mathlib.
- **Computer-assisted: no.**

## Labels

**A. A5** (impossibility), confidence medium-high.
- The innermost conclusion is that every computing circuit has more than 2^{A√n} gates (00:60-64).
- Secondary: A2, for the single witness language.
- A3 rate flag: the rate is ω(√n) but **not explicit**, since b(A) and M(b, 1/8) are tower-like.

**B. B1**, confidence medium-high.
- It resolves the 2^{ω(√n)} explicit-function question (00:85-91).
- It would be B3 relative to HJP95's n^{1/2+ε} question or the Majority question.
- On explicitness: the language is in P only because the hard slice's parameter bits are inputs, which is the PSZ00 trick. The slice itself is chosen by the probabilistic method.

**C. Primary C1:** the language is built (00:130). Secondaries:
- C3: the probabilistic choice of the slice, and the final contradiction.
- C4: the chain of estimates.
- C2: the sparsification tree, the Erdős–Rado induction, and the induction F_s ≤ θ^s.

There is no C5: every cited tool is re-proved.

Flags:
- **ih_strengthened: yes.** It is mild and templated. F_s(R) ≤ θ^s is proved for every state R ("strengthen to all substructures", 02:318-320), and the sparsification carries an extra tracked occurrence invariant inherited from IPZ01.
- **computer_assisted: no.**

**D. D3, provisional**, confidence low-medium. It rests on the restriction-lemma cluster (I07 with I11, I12 and I15). **Provenance flag: no.** Every cited work is human-authored, GKPRT26 has no AI disclosure, and no earlier model-produced attempt was found.

**E. Fields.**
- **Problem field:** TCS, circuit complexity (MSC 68Q06, 68Q17, 94C11).
- **Lean-dir field:** Computability.
- **Method fields, essential:**
  - random restrictions;
  - SAT sparsification (IPZ01, DHMTW14);
  - pseudorandomness, via Toeplitz hashing and k-wise independence (Krawczyk94, ABI86);
  - extremal set theory (the Erdős–Rado sunflower lemma);
  - finite fields and interpolation;
  - elementary probability;
  - entropy counting;
  - Turing-machine implementation.
- **Method fields, background-cited:** the Håstad switching lemma (contrasted, not invoked), PPZ/PPSZ, HJP95, and GPPST24/GKPRT26.
- **Cross-field count** (essential, non-TCS): 4. Two of the six invoked citations are from other fields.

## Proof architecture
1. **The language** (Def 4.1). The input has d data bits, a Hankel/Toeplitz hash seed, a monic modulus P of degree r = ⌈d^{2/3}⌉, and t ≈ d^{1/6} coefficients β_j in F₂[Z]/(P). An input is accepted iff λ(Σ β_j h(x)^j) = 0. The machine runs in polynomial time and never searches or tests irreducibility (Prop 4.2).
2. **Sparse partition** (Lemma 3.1). Every width-b CNF on m variables is a disjoint sum of at most 2^{ηm} width-b CNFs, each with at most M(b,η)·m clauses. This is IPZ01 sunflower branching with DHMTW14's disjointness side condition, Erdős–Rado re-proved, and entropy leaf counting.
3. **Good slices** (Prop 4.3). Take p = B/√d. Some parameter setting makes the restricted slice satisfy corr_b ≤ 2^{-|T|/8} simultaneously for all width-b CNFs, except with probability 4·2^{-m₀/16}. The ingredients:
   - the hash is injective on the restricted cube except with probability 2^{m-r};
   - Lagrange interpolation gives t-wise independent signs;
   - a t-th moment bound and a union bound over the 2^{O(m log m)} sparse tests;
   - the sparse partition, which pays a 2^{m/8} factor.
4. **Restriction lemma** (Lemma 2.1, the new core). For any width-k CNF H and θ = Σ_{ℓ>b} C(k,ℓ)(2p/(1-p))^ℓ < 1, the restricted correlation satisfies |E G·H_{T,ρ}| ≤ W·corr_b(G), where E W ≤ 1/(1-θ). W does not depend on G or on the number of clauses. The proof has four parts:
   - (a) **Path expansion.** Distribute the excess K − H as Σ v_i/q over the violated hard clauses. Replace q by a_{U_j}, the count of violated easy clauses, and telescope over violation paths. This gives a finite alternating identity.
   - (b) **Marker mixture.** Write c/(c+w) as the probability that a marker comes first in a random order of w clauses and c markers. Each term then becomes ω(P)·E[J_P] with J_P a width-b CNF.
   - (c) **Reweighting.** Sample a full assignment y first.
   - (d) **Backward counting.** Count paths backward from the terminal live set R. The factor 1/|V_R| *averages* over the eligible violated clauses rather than multiplying by their number. Each step weighs at most θ, so E W_j ≤ θ^j.
5. **Parameters** (§5).
   - Fix A, and set s = 3A, B = 64(s+1) and k = ⌈3(s+1)√d⌉.
   - Then pk ≤ Q, a constant that depends on A. Choose b = b(A) with Σ_{ℓ>b} Q^ℓ/ℓ! ≤ 1/2, so θ ≤ 1/2.
   - The slice is chosen for this (b, B), which gives |E gH| ≤ 6·2^{-m₀/16} for every width-k CNF H.
6. **Counting.**
   - There are at most S middle CNFs, each with at most S clauses.
   - Deleting clauses wider than k costs at most S·2^{-k} per gate.
   - Because gH = H for the middle gates of an exact OR, each middle gate accepts at most 6·2^{-m₀/16} + S·2^{-k} of the inputs.
   - Summing over middle gates contradicts the acceptance density, which is at least 1/4.

**Why it works.** In the classical method pk must stay below an absolute constant, which caps the exponent at c√n. Here pk may be any constant, because b can grow with A. That only helps if the function's restricted correlation with width-b CNFs decays at a rate (1/8) that does not depend on b. Pseudorandom slices have that property; parity and majority do not, since corr_b(parity) ≈ 2^{-m/b}. This is consistent with PPZ99's tight parity bound.

## Items: highlights (all 39 are in the JSON)
| ID | Item | cited/new | N (prov.) |
|---|---|---|---|
| I07 | Lemma restriction (clause-count-free signed CNF expansion, any constant pk) | new ("Our main ingredient", 00:116) | **N3**, F3/F5 |
| I11 | Telescoping violation-path expansion | new | N3 (cluster) |
| I15 | Backward averaging count, F_s ≤ θ^s | new ("source of the clause-count independence", 00:126-128) | N3 (cluster) |
| I12 | Marker mixture c/(c+w) as a convex mixture of CNFs | new use of a classical identity | N2 |
| I10, I08, I13 | Violation paths; easy/hard counts; path weights | new (bookkeeping) | N2 |
| I26 | Prop good slices | combination (IPZ01 §1.2 analogue) | N2 |
| I32 | b chosen after A; pk an arbitrary constant | new strategy, arithmetically forced | N2 |
| I23 | The language (hash + polynomial, parameter bits as input) | assembly (PSZ00, ABI86, Krawczyk94) | N2 |
| I17, I20, I21 | Disjoint sparse partition | adapted (IPZ01 + DHMTW14) | N1 |
| I04, I09, I16, I33, I34, I37 | corr_b, K, θ, the transfer step, balance, slice | routine | N1 |
| I01–I03, I05, I06, I18, I19, I22, I24, I25, I27–I31, I35, I36, I39 | Background, standard tools, TM plumbing | standard | N0 |

## Eureka candidates (quick literature check)
1. **I07 restriction lemma**, as the cluster I11 + I12 + I15. **N3, F3**, with F5 flavour.
   - *For:* it is the only step that lifts width k = Θ(√d) down to constant b at arbitrary constant pk. Its conclusion appears nowhere in the goal or in L. Its Lean closure is 346 of 2,046 declarations (17%), about 38% of the lower-bound subDAG.
   - *Against:* the switching-lemma neighbourhood is dense: Razborov's encodings, the SBI small-restriction lemma, Lovett–Wu–Zhang 2020's mild-restriction lemma (which bounds the first moment of useful terms), and Rossman's entropy proof.
   - Searches found no statement of a CNF→CNF expansion with bounded L1 mass and no clause-count dependence.
2. **The strategy insight (I32 + I26), N2.** Choose b after A, and use a slice whose correlation exponent does not depend on b. It is forced arithmetic once I07 is stated, and slices that are pseudorandom against bounded-width CNFs come from IPZ01 §1.2.
3. **I26 good slices, N2.** Every component is standard.
4. **I12 marker mixture, N2.** A classical random-order identity in a new role.
5. **I17 sparse partition, N1.** DHMTW14 already has the disjoint (counting) version.

## Correctness audit
No gap was found in sections 2–5 on a line-by-line reading.
- **Hand checks of the restriction lemma:**
  - the expansion's cases;
  - the residual identity;
  - the marker identity;
  - injectivity of the reverse encoding;
  - the one-step bound θ.
- **Worked examples:** a single width-k clause, and parity written as a CNF. In both, W matches E W ≤ 1 + θ.
- **Parameter conditions:**
  - the union-bound condition holds, since t ≈ d^{1/6} is much larger than log d and m ≈ √d;
  - the hash failure probability 2^{m−r} is small, since r ≈ d^{2/3} is much larger than m;
  - the final exponents work out: m₀/16 = 4(s+1)√d and k ≥ 3(s+1)√d.

**Residual concerns:**
- The claim is extraordinary: a long-open barrier falls.
- The Lean end-to-end proof is the main safeguard, and it was not compiled here.
- The ω is astronomically slow and ineffective: b(A) feeds M(b, 1/8), which is tower-like.
- "Explicit" means in P, via parameter bits supplied as input. The slice inside is non-constructive.
- g depends on only d^{2/3} linear forms. This is harmless for the proof, but worth noting.
- The result has not been reviewed.

## Extraction friction
- The extractor's ranking is dominated by Turing-machine plumbing. The polytime closure is 60% of the DAG, and Tape* carriers have frac_dag_dependents of 0.21–0.27. The 20% proxy therefore misses I07 (17%) and over-ranks the N1 sparse partition (Sparse* carriers ≈ 0.22). Measure load-bearing on the lower-bound subDAG (906 declarations) instead.
- The key constructions sit inside proofs, with no environments: paths, the marker mixture, the reverse encoding, the parameter order.
- There are few `\emph` definitions: slice, easy/hard, compatible, cylinder, sunflower, eligible.
