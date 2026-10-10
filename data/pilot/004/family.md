# Family 004: Hilbert's tenth problem over Q (family analysis)

Analyst role: family analyst, working from the papers only. There is **no Lean formalization** and no reasoning trace. Date: 2026-10-10 (influential-problems pass). Machine-readable version: `family.json`.

> **Shortlist status.** This family is **excluded from the Lean eureka shortlist because it has no Lean formalization**, and the downstream speedup test is Lean-only. The exclusion is **not a judgement on merit**. Under PLAN.md (2026-10-10), any N3 items it has belong on the informal list (`data/eureka_informal.json`), which this agent does not write.

Manuscripts (commit fd4aeeb):
- **MS1**, "Hilbert's tenth problem over the rational numbers" (2026-10-06; 5.4k lines).
  - v1 is dated 2026-09-24. A `diff` shows that only the citation URLs changed.
- **MS2**, "A pointwise 2-converse for elliptic curves with rational two-torsion" (2026-10-07; 7.5k lines). MS1 uses it.

## 1. Main statement

- **Statement** (MS1 `01-introduction.tex:7-11`): no algorithm decides whether an integer polynomial f in X_1…X_n has a zero in Q^n, where n is part of the input.
- **Corollary 7.1:** H10(Z) ≤_T H10(Q). So H10(Q) has Turing degree 0′. The same holds for inputs of total degree ≤ 4 and for sums of squares of quadratics.
- **MS2 headline:** let E/Q have E(Q)[2] ≠ 0 and 2^∞-Selmer corank s₂ ∈ {0,1}. Then ord_{s=1} L(E,s) = rank E(Q) = s₂, and Sha(E/Q) is finite, with any reduction type at 2.

### Route, and how Mazur's conjecture is avoided

**What the proof is not:**
- It is **not** a Diophantine definition of Z (Koenigsmann gives a universal one, Poonen a ∀∃ one).
- It is **not** a Diophantine model in the sense of Cornelissen–Zahidi.
- It is **not** the rank-stability route for rings of integers (Shlapentokh, Poonen, Mazur–Rubin, Koymans–Pagano, Alpöge–Bhargava–Ho–Shnidman).

**What it is:** a Turing reduction that uses **negative** oracle answers.
- Mazur's conjecture (and its extension by Cornelissen and Zahidi) rules out only positive-existential definitions and models.
- The paper builds neither (`07-consequences.tex:105-107`: "it gives no single existential definition of Z in Q").
- So the paper **neither disproves nor relies on** Mazur's conjecture. The introduction says so explicitly (`01-introduction.tex:76-87`).
- The one Diophantine set it does construct is Φ. Φ contains Z and is not discrete, so it is compatible with Mazur's conjecture.

**Steps of the route:**
1. **Finite tests.** Skolemize a recursive theory T together with f(a)=0 and Φ. Each finite set of ground instances is a finite set of H10(Q) queries. The tests are sound: an integer zero passes every test.
2. **Compactness.** If every test passes, there is a ring R ⊂ *Q (nonstandard rationals) containing a root a. The elliptic points T_a give an additive injection η: R → *Z, which need not be multiplicative.
3. **Local recovery of indices.** Formal-group comparisons recover ã ≡ η(a) mod q^K at every "contact prime" q. There are two comparisons: one on E/Q(√2) and one on its Galois conjugate.
4. **Height squeeze.**
   - Every ring element is a sum of three "slopes". Every contact prime of every slope divides the single integer δ = f(η(a)) to order K.
   - A new **five-point height estimate**, h(s) ≤ H·M(s)^c, then bounds the height of every element of R by O(B), where B = max|η(a_j)|.
   - Canonical heights make h(x(ηP)) grow like B². So B is standard, and a is an integer root.

## 2. Labels (codebook axes A–E)

| Axis | Label | Evidence and notes |
|---|---|---|
| A | **A5**, impossibility (high confidence) | `01-introduction.tex:8-10`. MS2 alone would be A1. |
| B | **B1**, confirms the negative answer fully | Flag *full only with prior results* = **yes**: it needs MS2 and OAI family 010, both model-produced. Flag *adds corollaries* = yes (degree 0′, quartic normal form; MS2 is a 2-converse). |
| C | **C5** primary (medium confidence); secondaries C3, C4, C1 | Reduction to DPRM (`02-reduction.tex:884-886`). C3: compactness / proof by contradiction. C4: the height chains, plus GTZ and the sieve. C1: Φ, the curve, the prime networks. Computer-assisted = **no**: rank is by hand descent, and the constants are never computed (`02-reduction.tex:465-467`). ih_strengthened = no. |
| D | **D3, provisional** (low-to-medium confidence) | Rests on E1, the contact-radical height squeeze. Provenance flag = **yes** (MS2, family 010). |
| E | Problem field: Number theory (MSC 11U05, 03D35). Lean-dir field: none. | Essential method fields: logic and computability; elliptic curves; Shimura varieties and QM surfaces; Galois representations and modularity; Arakelov heights and isogeny estimates; additive combinatorics and sieves; class field theory and Rédei matrices; Iwasawa theory and Euler systems (MS2); combinatorics (Chevalley–Warning, matrix-tree). Topology of rational points is background only. That is 9 essential cross-field imports. |

## 3. Proof architecture (MS1)

| Step | Content | Items |
|---|---|---|
| 1 | E: y² = x³ − d²x over F = Q(√2), with d = 75 − 53√2 (norm 7). E(F) has rank 1 by hand 2-isogeny descent. Formal-log index comparisons. | I05, I06, I10 |
| 2 | **Local comparison.** Fix h, j₀ independently of a. The test on the conjugate curve forces η(ha) ≡ 4η(a) mod q^K, which makes the main curve's truncated-log ratio usable. | I11, I45 |
| 3 | **Five-point height estimate.** Uses the Shimura curve of discriminant 210 (genus 5); its quotient by the full Atkin–Lehner group is P¹ with 5 rational branch points. A QM abelian-surface family over it, odd-contact ramification, Q-curve descent, controlled splitting, modularity via **OAI family 010**, level N ≪ M², von Känel's modular-height method and Gaudron–Rémond together give h ≤ H·M^c. | I12, I32–I43 |
| 4 | **Representation axiom of T.** Every A ∈ R equals u₁/v + u₂/v + u₃/v, and each of the 13 contact values is ±k·r for a tested "prime" r with local witnesses. The integer model comes from Green–Tao–Ziegler (GTZ) prime patterns plus Selberg-sieve removal of common factors. | I14, I15, I44–I50 |
| 5 | **Pole-parity formula Φ.** Built from a pair of twists of y² = x(x−l)(x+3l). Its soundness is elementary. Its completeness on Z uses Monsky matrices, the **MS2 2-converse** and Cassels–Tate. | I17, I24–I31 |
| 6–7 | Finite tests, compactness, valuation coarsening (where Φ makes odd valuations survive), index congruences. | I04, I18–I21 |
| 8 | **Height squeeze**, giving an integer root. | I22 |
| 9 | Parallel search, DPRM, degree 0′. | I23, I51 |

**MS2 architecture:**
- Kato-class determinants and Heegner/Kolyvagin determinants are interpolated over binary cubes of quadratic twists. Chevalley–Warning transfers the bounds to the missing vertex (J05, J11).
- Half-integral-weight coefficients (Waldspurger) become binary symbols (J15–J17).
- An address lemma builds auxiliary prime networks so that every nonzero vertex is a unit. Its forest expansion uses grounded-Laplacian minors (matrix-tree) (J19).
- Assembly is in J20.

## 4. Items

There are 71 items in `family.json`: I01–I51 for MS1 and J01–J20 for MS2. The non-trivial grades:

| Item | What | Provisional N |
|---|---|---|
| I15 | Representation axiom (substructure-robust ∀∃ axiom tying all heights to tested primes) | **N3 candidate**, F3 |
| I22 | Uniform ring-height bound via a single δ; canonical-height squeeze | **N3 candidate**, F3 |
| I04 | Finite-test Turing reduction architecture | N2 (logic = N0 transfer; bridge new) |
| I11 / I45 | Conjugate-curve paired local test | N2, F3 |
| I12 | Five-point odd-contact height estimate | N2 (von Känel Prop 9.9) |
| I17 / I24 / I31 | Pole-parity formula and simultaneous Rédei design | N2 |
| I14 | Integer contact representations | N2 |
| I20 | Coarsening with Φ | N2 |
| I39 | Controlled splitting, character order O(M) | N2 |
| J05 | Binary-cube missing vertex (MS2) | **N3 candidate** (F5), likely N2 |
| J04, J11, J13, J16, J17, J19 | MS2 lower bound, ring-class transfer, switches, theta detector, symbols, address lemma | N2 |
| everything else | Textbook or cited inputs: DPRM, compactness, formal groups, descent, Shimura curves, Faltings, GTZ, sieves, Kato, Waldspurger | N0–N1 |

## 5. Eureka candidates (provisional; full grading is in novelty.md)

1. **E1: contact-radical height squeeze (I15 + I22 + I12).** Provisional N3, F3.
   - **For:** it turns local data at nonstandard primes into one archimedean bound on the whole ring. The "same δ for every A" step (`02-reduction.tex:810-814`) is tiny and nowhere in the goal. Searches found no precedent.
   - **Against:**
     - Every ingredient is classical (quadratic growth of canonical heights; radical bounds height, as in Szpiro/abc).
     - Family 242 (OAI, also dated 2026-09-24) uses quadratic height growth to pin indices.
     - Garcia-Fritz–Pasten–Vidaux 2025 encode squares with canonical heights, but in a language extended by height predicates.
2. **E2: the Herbrand + compactness Turing reduction (I04, I18, I19).** Provisional N2; probably N0 as a device.
   - It is the step that makes Mazur's conjecture irrelevant.
   - Its logic, however, is textbook (Herbrand, Gilmore, Davis–Putnam, compactness). In SAT terms it is a DPLL(T)-style refutation search over the Herbrand expansion, with H10(Q) as the theory oracle.
3. **E3: conjugate-curve paired local test (I11, I45).** N2, F3. The paper names Poonen 2002 Lemmas 9 and 11 as precedents.
4. **E4: pole-parity formula Φ.** N2. Nearest is Demeyer–Van Geel 2006.
5. **E5: five-point height estimate.** N2. Nearest are von Känel 2013 Prop 9.9 and von Känel 2021; the curve geometry is tabulated in Long–Maclachlan–Reid and Nualart.
6. **E6 (MS2): binary-cube missing vertex.** N3 candidate, likely N2. Nearest are Tian's induction and Tian–Yuan–Zhang genus periods; Kriz–Li mod-2 Heegner congruences (not cited by MS2); and Smith's cubes.

## 6. Correctness and trust

**Checked.** The logic and height-squeeze part of Section 2 was read line by line with no gap found. Specifically:
- the substructure-robustness of T;
- the arithmetic of the local comparison;
- the odd-contact parity step;
- valuation coarsening;
- the divisibility M^K | δ and the height chain.

**Spot checks:**
- N(d) = 7.
- The point Q lies on E (checked in Python).
- The discriminant-210 Shimura curve has genus 5 with no elliptic points, and Riemann–Hurwitz gives r = 5.
- v₂ gcd(d₁, d₂) = 2 for r ≡ 1 mod 8.

**Concerns:**
- **Dependence on unreviewed OAI work.**
  - MS2's 2-converse at p = 2 has no residual-irreducibility hypothesis and covers every reduction type. It is a frontier claim and was read here only at the architecture level. If it fails, Φ is unproved on Z, and the soundness of the tests fails.
  - Family 010's Fontaine–Mazur at p = 2 with no residual hypothesis would be a major theorem in its own right. My unverified assessment is that it can probably be replaced here by Ribet/Pyle (building blocks) plus Khare–Wintenberger.
  - Family 006 is offered as an alternative to MS2; it too comes from OAI.
- Section 4 stacks many quantitative inputs (Gaudron–Rémond in growing dimension, Javanpeykar, Pazuki theta heights). The bookkeeping looks consistent but was not rederived.
- The algorithm is non-uniform: its constants exist but are not computed. That is fine for undecidability.
- External reception: press snippets (theprint.in, zeli.app) note that the result is unreviewed and not Lean-checked. I found no expert evaluation.

## 7. Relations

- **Family 242** (single-fold representations; see `data/pilot/242/`).
  - Shared mechanism: a rank-one curve plus quadratic canonical-height growth pins a hidden index (242's square window; 004's B² ≪ B).
  - Differences: 242 works over N; 004 works over Q through a nonstandard model. 004 does not cite 242.
  - Both v1 manuscripts are dated 2026-09-24, which suggests a shared model "house style".
- **Koymans–Pagano** (arXiv:2412.01768; JAMS 2026) and **Alpöge–Bhargava–Ho–Shnidman** (arXiv:2501.18774; Invent. 2026).
  - They cover different rings: rings of integers and finitely generated Z-algebras, via rank stability. Q is not finitely generated (`01-introduction.tex:129-143`).
  - Shared toolkit: Koymans–Pagano's full-2-torsion 2-descent with Rédei matrices plus additive combinatorics reappears in MS1 §3 and §6 and in MS2. The rank-one curve over Q(√2) follows the Poonen 2002 pattern, and its Weil restriction is a rank-one abelian surface over Q, in the spirit of Alpöge–Bhargava–Ho–Shnidman.

## 8. Extraction friction

- There is no Lean, so everything is at the LaTeX level.
- Many definitions are inline: contact forms; "formal for this localization"; local filters; the graph vocabulary.
- MS2 is very dense. Read in full: its statements, the cyclotomic section and the assembly. Its ring-class sections were read at the statement level only.
- Two dependencies live in other families (010 and 006).

Sources (all web claims rest on search-result snippets; WebFetch was not used):
- [Koymans–Pagano arXiv:2412.01768](https://arxiv.org/abs/2412.01768v2)
- [Alpöge–Bhargava–Ho–Shnidman arXiv:2501.18774](https://www.arxiv.org/abs/2501.18774)
- [Garcia-Fritz–Pasten–Vidaux arXiv:2311.01958](https://arxiv.org/pdf/2311.01958)
- [von Känel arXiv:1310.7263](https://arxiv.org/abs/1310.7263)
- [Pasten arXiv:1705.09251](https://arxiv.org/abs/1705.09251)
- [Tian–Yuan–Zhang arXiv:1411.4728](https://arxiv.org/abs/1411.4728)
- [Kriz–Li arXiv:1606.03172](https://arxiv.org/pdf/1606.03172)
- [Yuyama notes](https://www.math.mi.i.nagoya-u.ac.jp/~kihara/workshop/wakate/yuyama.pdf)
- [theprint.in](https://theprint.in/tech/weeks-after-claiming-ai-cracked-90-yr-old-maths-puzzle-openai-drops-the-mother-lode-on-mathematicians/3064174/)
- [zeli.app](https://zeli.app/story/49985787)
