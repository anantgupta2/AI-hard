# Family 004: novelty analysis (Hilbert's tenth problem over Q)

Analyst role: novelty analyst, working at text level. There is no Lean formalization and no reasoning trace. Date: 2026-10-10. Machine-readable version: `novelty.json`.

> **Shortlist status.** This family is **excluded from the Lean eureka shortlist because it has no Lean formalization**, and the speedup test is Lean-only. The exclusion is **not a judgement on merit**. Its N3 item (E1) belongs on the informal list, `data/eureka_informal.json`, under PLAN.md (2026-10-10); this agent does not write that file.

**Method note.** WebFetch to arxiv.org failed with ENOTFOUND, so every web claim below rests on **search-result snippets**. Quotes from external papers are unverified.

## 1. Provenance verdict: **yes**

- **Model-produced dependencies.** MS1 essentially uses two model-produced, unreviewed manuscripts:
  - **MS2** (in this family): its 2-converse proves that Φ holds on every integer (`03-parity.tex:457-494`).
  - **Family 010**, "Fontaine–Mazur modularity at the prime 2": it supplies the modularity step of the height estimate (`04-height.tex:902-907`).
  - **Family 006**, the unrestricted 2-converse, is offered as an optional substitute for MS2.
- **No earlier model-produced literature found.** Searches for H10(Q) together with ChatGPT, GPT-5, OpenAI or "AI-assisted" returned only press coverage of this release (theprint.in, zeli.app). No earlier model-produced precedent turned up for any candidate.
- **Human 2023–2026 citations.** Koymans–Pagano, Alpöge–Bhargava–Ho–Shnidman, Garcia-Fritz–Pasten–Vidaux (GFPV), Smith 2025, Burungale–Tian and Keller–Yin all have human authors. The snippets show no AI-assistance wording.
- **Same-release relative.** Family 242 (OAI, also first dated 2026-09-24) uses the same canonical-height lever. 004 does not cite it.

## 2. Final grades

| # | Item | Nearest neighbour (verdict) | T2 | T3 | Final | F | Conf. |
|---|---|---|---|---|---|---|---|
| E1 | Contact-radical height squeeze (I15 representation axiom + I22 single-δ uniform height bound) | GFPV 2025: height predicates added to the language (genuinely different); 242: square window (canonical-height half only) | pass | pass (~60% of MS1 feeds it) | **N3** | F3 (F4 flavour) | 0.40 |
| E2 | Herbrand + compactness Turing reduction (finite tests) | Gilmore 1960 / Davis–Putnam 1960 / DPLL(T), plus compactness (equivalent device) | bridge yes, device no | pass | **N0** (transfer; new bridge) | – | 0.60 |
| E3 | Conjugate-curve paired local test, using (h−4)a | Poonen 2002 Lemmas 9 and 11 (close variant) | pass | pass | N2 | – | 0.60 |
| E4 | Pole-parity formula Φ | Demeyer–Van Geel 2006; Cornelissen–Zahidi 2007 (close variant) | pass | pass | N2 | – | 0.60 |
| E5 | Five-point odd-contact height estimate | von Känel 2013 Prop 9.9 and von Känel 2021; Long–Maclachlan–Reid / Nualart; Beckmann (close variant) | pass | pass | N2 | – | 0.65 |
| E6 | (MS2) Binary-cube missing vertex via Chevalley–Warning | Tian–Yuan–Zhang genus periods; Kriz–Li (close in purpose) | pass | pass | N2 | – | 0.45 |
| E7 | (MS2) Address lemma (matrix-tree networks) | Chaiken 1982; Rédei/Monsky and Smith (close variant) | pass | pass | N2 | – | 0.50 |

## 3. Family verdict

**family_D = D3 (provisional), confidence 0.35. It rests on E1 alone.**

E1 would fall and the family would drop to D2 if any of these happens:
- someone finds an earlier argument that bounds the heights of a whole (nonstandard) ring through a shared radical or divisibility estimate;
- the informal discoverability test finds E1 at a rate above the calibrated threshold;
- a judge grades E1 as a recombination of radical–height bounds and canonical heights (N2).

## 4. The route and Mazur's conjecture

**How the paper avoids Mazur's conjecture.**
- The paper builds **no** Diophantine definition and no Diophantine model of Z.
- It proves H10(Z) ≤_T H10(Q) by a Turing reduction. The reduction uses *negative* oracle answers: some finite existential test fails exactly when f has no integer zero.
- Mazur's conjecture (with Cornelissen–Zahidi's extension) blocks only positive-existential definitions and models. So the paper **neither disproves nor uses** Mazur's conjecture.
- Φ is a Diophantine set that contains Z and is not discrete, so it is compatible with Mazur.

**Route classification.** The route is not any of the following:
- Koenigsmann's universal definition;
- Poonen's ∀∃ definition;
- Shlapentokh-style elliptic definitions over rings of integers;
- Eisenträger's work.

The route is new. It combines:
- a model-theoretic Herbrand scheme with compactness;
- a Poonen-2002-style reading of indices on a rank-one curve over Q(√2);
- a von-Känel-type height bound on the discriminant-210 Shimura curve;
- GTZ prime patterns;
- a parity predicate that needs a 2-converse.

**Relation to Koymans–Pagano and Alpöge–Bhargava–Ho–Shnidman.**
- They settle different rings (finitely generated Z-algebras and rings of integers); Q is not finitely generated.
- The two works share a toolkit with family 004: full-2-torsion descent with Rédei matrices and additive combinatorics, plus rank-one curves over a quadratic field (the Poonen rank-stability pattern).

**Relation to family 242.**
- Both families pin a hidden index through quadratic canonical-height growth on a rank-one curve.
- 004 adds the contact-radical/δ half. That half is where the N3 claim rests.

## 5. Bridge novelty

| Bridge | Status |
|---|---|
| Logic (Herbrand, compactness) → H10(Q) | **New bridge.** A Yuyama-notes snippet says that the only known undecidability method goes through Diophantine models. |
| Modular height bounds on Shimura curves → Diophantine undecidability | **New bridge**, as far as I searched (an "abc implies H10(Q)" search found nothing). |
| GTZ / additive combinatorics → H10 | Known route (Koymans–Pagano). |
| Rank-one curves and formal groups → H10 | Known route (Denef, Poonen, Shlapentokh, Cornelissen–Zahidi). |
| 2-converse → existential predicate | New use of a known kind of input (Mazur–Rubin and Koymans–Pagano use Selmer control). |
| (MS2) Chevalley–Warning / matrix-tree → Iwasawa theory at p = 2 | Apparently new (no search hit). |

## 6. Discoverability protocol (text level; not run)

**Models.**
- Training cutoff must be strictly before **2026-09-23**. That is the earliest date in the dependency set: family 010 v1. MS1, MS2 and 242 v1 are all dated 2026-09-24.
- Exclude the OpenAI release lineage, except as a reference arm.
- Canary probe: exclude any model that claims H10(Q) has been resolved, or that knows the phrases "contact radical" or "five-point height estimate".
- No tools.

**E1 protocol.**
- **What to hide:** I15, everything in I22 from "Set δ" onward, the overview figure, and `01-introduction.tex:192-229`.
- **Arms:**
  - **L:** the five-point estimate is given as a black box.
  - **L−:** the five-point estimate is withheld.
  - **open:** the problem statement only.
  - **directed:** the finite-test and compactness strategy is stated.
- **Hit criterion:** the proposal must
  1. bound the heights of all elements of the term ring by O(B), using primes that divide one integer derived from f(η(a)); and
  2. finish with quadratic canonical-height growth.

  A proposal with (2) alone is scored separately.
- **Sampling and judging:** n = 256 per arm; k ∈ {1, 2, 4, …, 256}. Two LLM judges, then an expert check of every positive.
- **Estimated pivot distance:** 2–3 steps from L.
- **Chain depth:** 2. E1 needs E5 and E3/E4 in place first.

The E2 protocol and a generic template for E3–E7 are in `novelty.json`.

## 7. Trust concerns (carried from the family analysis)

1. **MS2's 2-converse at p = 2** (no residual irreducibility, every reduction type) is the main risk. If it fails, the tests are unsound. A Pan–Tian seminar abstract (2025, full rational 2-torsion) may overlap, and MS2 does not cite it. Kriz–Li is not cited either.
2. **Family 010 (Fontaine–Mazur at 2)** would be a major theorem in its own right. It is probably replaceable here by Ribet/Pyle plus Khare–Wintenberger. This is my assessment and is unverified.
3. The quantitative chain of Section 4 is plausible, but I did not rederive it.
4. The logic and height-squeeze part of Section 2 was checked line by line with no gap found.

## Open questions

- Is MS2 correct, and does it overlap Pan–Tian?
- Can family 010 be removed (Ribet/Pyle plus Khare–Wintenberger)?
- Does von Känel's Prop 9.9 already give E5 verbatim?
- Have experts ever proposed a "nonstandard height squeeze"?
- Run protocol E1.

Sources (search snippets):
- [Koymans–Pagano](https://arxiv.org/abs/2412.01768v2)
- [Alpöge–Bhargava–Ho–Shnidman](https://www.arxiv.org/abs/2501.18774)
- [Garcia-Fritz–Pasten–Vidaux](https://arxiv.org/pdf/2311.01958)
- [von Känel 2013](https://arxiv.org/abs/1310.7263)
- [Pasten](https://arxiv.org/abs/1705.09251)
- [Tian–Yuan–Zhang](https://arxiv.org/abs/1411.4728)
- [Kriz–Li](https://arxiv.org/pdf/1606.03172)
- [Smith 2025](https://arxiv.org/pdf/2503.17619)
- [Burungale–Tian](https://arxiv.org/abs/2506.03465v2)
- [Keller–Yin](https://arxiv.org/pdf/2410.23241)
- [Yuyama notes](https://www.math.mi.i.nagoya-u.ac.jp/~kihara/workshop/wakate/yuyama.pdf)
- [Pan–Tian abstract](https://math.ustc.edu.cn/2025/0603/c18822a686712/page.htm)
- [Cornelissen–Zahidi, Mazur's conjectures](https://arxiv.org/pdf/math/0006140)
- [Poonen slides](https://math.berkeley.edu/~poonen/slides/h10.pdf)
- [theprint.in](https://theprint.in/tech/weeks-after-claiming-ai-cracked-90-yr-old-maths-puzzle-openai-drops-the-mother-lode-on-mathematicians/3064174/)
- [zeli.app](https://zeli.app/story/49985787)
