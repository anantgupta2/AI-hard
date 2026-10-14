# A/B buckets v2 and a high-confidence labelling plan

Status: pilot done (2026-10-14; 50 families, κ 0.88–0.98, see `pilot/report.md`); rules below added for the full run. Nothing here changes `docs/PLAN.md` or the argument doc yet.

## Why v1 is not enough

v1 forced each headline claim into one of five A codes and four B codes. The cheap pass agreed with the
in-depth labels at κ = 0.77 (A) and 0.79 (B), but the 10 disagreements on the 39-family gold set are
almost all bucket problems, not reading errors:

| Family | Claim | Deep | Cheap | What v1 cannot express |
|---|---|---|---|---|
| 342 | every tamed J admits a compatible form | A2 | A1 | a ∀∃ statement: v1 makes you pick the outer or the inner quantifier |
| 357, 368 | at every regular point there are bi-Lipschitz coordinates; every map has an approximation | A2 | A1 | same ∀∃ problem |
| 312 | two homotopy theories are equivalent | A1 | A4 | identity/equivalence of given objects vs. a characterization |
| 367 | the critical dimension is exactly 7 | A3 | A4 | an exact value vs. an iff |
| 107, 108 | ω ≤ 9/4; a better permanent lower bound | B3 | B4 | quantitative progress on a record, which is neither partial nor an extension |
| 004 | Hilbert's tenth problem over ℚ is undecidable | B1 | B2 | a question with no "expected" direction: is the answer a confirmation or a refutation? |
| 240 | an obstruction under CH to a prescribed threshold | A2 B2 | A1 B1 | a conditional (CH) refutation of one form of a conjecture |

Release-wide, the summaries also use quantifiers and settings v1 has no place for (counts over the 372 OpenAI summaries):
sharp/optimal/exact/threshold 105, iff/characterize/classify 65, counterexample/refute 55,
independence/consistency 44, asymptotic/limit 48, "sufficiently large" 26, "with high probability"/random 24,
explicit/effective 21, hardness/decidability 19, "very general"/generic/almost every 14, unique 13,
conditional (GRH, CH, assuming) 9, infinitely many 6.

## v2 buckets

### A. Logical form: three fields instead of one code

**A.prefix**: the quantifier prefix of the headline claim in prenex form over its main objects, written as a
string over this alphabet (outermost first):

| Symbol | Meaning | Example |
|---|---|---|
| ∀ | for every | every flat local map |
| ∃ | there exists | there is a graph G |
| ∃! | there exists a unique | |
| ∀ᵍ | for generic / very general / almost every | a very general cubic fourfold |
| ∀^∞ | for all sufficiently large / eventually | for all n ≥ n₀ |
| ℙ | with high probability / almost surely (random object) | a random 3-SAT instance |
| ∃^∞ | there are infinitely many | infinitely many primes p with… |
| (none) | closed statement about one specific object | ζ(3) is irrational; L = BPL |

So 342 is `∀∃`, 161 is `∃`, 054 is `∀ᵍ` with a negated matrix, 103 is `(none)`.

**A.matrix**: what is asserted under the prefix. One primary code:

| Code | Matrix | Examples |
|---|---|---|
| M1 | property holds (inclusion, implication, inequality between given objects with no rate) | every flat local map satisfies e(R) ≤ e(S) |
| M2 | existence of an object | a compatible symplectic form exists |
| M3 | counterexample: an object violating a conjectured ∀ | a 35-vertex graph violating Sidorenko |
| M4 | non-existence / impossibility (incl. irrationality, non-embedding, no bijection) | no bi-Lipschitz embedding exists |
| M5 | equivalence / characterization (P ⇔ Q) | X is amenable iff… |
| M6 | classification (complete list up to equivalence) | all such groups are… |
| M7 | identity / isomorphism / equivalence of named objects or classes | L = RL = BPL; two model structures are Quillen equivalent |
| M8 | one-sided bound or rate (upper or lower, explicit or asymptotic) | ω ≤ 9/4; d_p(n) ≤ exp(C(log n)^γ) |
| M9 | exact value / sharp bound with attainment / threshold / asymptotic formula | the critical dimension is 7; the sharp constant is 4/(3√3 π) |
| M10 | computational status (complexity class, hardness, (un)decidability, algorithm existence) | NP-hard to approximate beyond…; H10 over ℚ is undecidable |
| M11 | metamathematical (independence, consistency, provability) | the Partition Principle does not imply Choice |
| M12 | limit law: scaling limit, convergence in law, universality, limiting formula (added at adjudication, rule 13) | uniform random triangle removal leaves ≈ n^{3/2}/(2√2) edges |

Precedence: M10 and M11 override M4 (hardness and independence are impossibility statements of a special kind);
M9 overrides M8 when the bound is shown attained; M3 overrides M2 when the object refutes a stated conjecture.

**A.setting flags** (any number):
`specific_instance` (no free parameters) · `asymptotic_only` · `effective` / `ineffective` / `n/a` (are constants explicit?) ·
`conditional_on: [GRH, CH, P≠NP, UGC, …]` · `restricted_range` (dimension, characteristic, class stated in the headline) ·
`finite_checkable` (in principle a finite computation) · `probabilistic` (random objects).

### B. Relation to the posed problem: two fields instead of one code

**B.problem**, what was posed:

| Code | Kind |
|---|---|
| P1 | named conjecture (Sidorenko, Lech, UGC) |
| P2 | open question without a predicted answer (Hilbert 10 over ℚ, Tingley's problem) |
| P3 | entry in a problem list or database (Erdős, Kourovka, OPG) |
| P4 | record to improve (an exponent, a constant, a bound) |
| P5 | nothing posed: a new result |

**B.outcome**, what the family did to it:

| Code | Outcome |
|---|---|
| O1 | settles affirmatively, in full |
| O2 | settles negatively, in full (refutation, or "no" to the question) |
| O3 | refutes and replaces: counterexample plus a corrected true statement |
| O4 | shows independence or undecidability of the posed statement |
| O5 | settles a special case or restricted range |
| O6 | settles conditionally on an unproved hypothesis |
| O7 | quantitative progress on a record, not settling it |
| O8 | extends or strengthens a known theorem |
| O9 | new proof of a known result |

For P2 questions, O1/O2 follow the wording of the question as posed ("is H10 over ℚ decidable?" → O2).

**B.flags** (kept from v1): `full_only_with_prior_results` · `adds_corollaries` · `builds_on_model_output`.

v1 is recoverable from v2 (A1 ≈ prefix ending ∀ with M1, A2 ≈ M2/M3, A3 ≈ M8/M9, A4 ≈ M5/M6, A5 ≈ M4/M10/M11;
B1 ≈ O1, B2 ≈ O2/O3, B3 ≈ O5/O6/O7, B4 ≈ O8), so the cheap pass stays comparable.

## Tie-break rules (added after the pilot)

1. **Explicit witnesses.** If the headline says "there is an X" and the paper or Lean fixes X explicitly, the prefix still starts with ∃. Use `none` only for claims about an object that was named before the paper (ζ(3), χ(ℝ²), the class L, ω).
2. **Thresholds.** "For all sufficiently large n" with no explicit threshold → ∀^∞. An explicit threshold (∀ m ≥ 1408) → ∀ with the flag `effective`.
3. **Almost every / generic / very general** → ∀ᵍ, even when the Lean writes it as "∃ a null set E, ∀ x ∉ E".
4. **Random processes.** A limit or concentration statement about a random object → ℙ (not `none`, not ∀^∞).
5. **Counterexamples to questions.** An object answering a universal question negatively is M3, like a counterexample to a conjecture.
6. **Restricted dimension.** Settling one dimension (or characteristic, or class) of a problem posed in general → O5 with `restricted_range`. Use O1 only if the source poses exactly that case as its own problem.
7. **Records.** If the posed object is a number (exponent, constant, chromatic number): improving it without settling it → P4/O7; determining it exactly → O1 with M9; refuting a conjectured value and determining the true one → O3.
8. **Problem lists.** P3 only for an explicit numbered list or database (Hilbert, Erdős, Kourovka, OPG). A question that a survey merely repeats stays P2.
9. **Earlier proofs.** If the paper says the headline was already proved by others, the outcome is O9 (new proof), whatever the problem type.
10. **Lean coverage.** A new field `lean_vs_headline` ∈ {`same`, `weaker` (special case, one direction or one half), `different` (a secondary or intermediate result), `no_lean`}.
11. **Operator bounds.** "T is bounded on X" (∃C hidden inside "bounded") → M1, prefix over the main objects only. Use M8 only when the rate, exponent or uniform constant is itself the content (δ^{-ε} losses, explicit growth).
12. **Completing the remaining cases.** If the family finishes the last open cases of a conjecture whose other cases were already proved, so that the conjecture is now settled in full → O1 with `full_only_with_prior_results`. O5 only if the posed general problem is still open after the family.
13. **Limit theorems (added at adjudication).** A headline that identifies a limit — scaling limit, convergence in law or distribution, universality of local statistics, a limiting free energy or formula as n → ∞ — gets the new matrix code **M12 limit law**. M12 overrides M7 and M9 for such claims.
14. **Counterexample prefix.** A counterexample's prefix is the quantifiers over the witness (usually `∃`); the universal quantifiers inside the property it violates stay in the matrix (so `∃`, not `∃∀`).
15. **Physics predictions.** A prediction from the physics literature that the paper treats as the target (e.g. a conjectured exponent or formula) is P1.
16. **Which claim is the headline.** The headline is the claim OpenAI's summary leads with. If the paper itself says that claim was already known, the headline is the paper's main new theorem and the outcome is judged for that theorem (usually O8); note the summary's claim.
17. **Several formulations posed side by side.** If a conjecture is posed jointly in several models or forms and the family settles one of them, that is O5 (rule 6) unless the source singles that form out as the main one.

## High-confidence labelling protocol

1. **Richer input per family.** For every manuscript: the abstract, every theorem/corollary/conjecture environment of
   the introduction (up to 10), the introduction text (≤ 4,000 characters), and, where it exists, the theorem
   statement of the Lean comparator challenge. The Lean statement fixes the quantifier prefix unambiguously for
   the 242 families that have one.
2. **Write the claim before labelling it.** Each labeller first writes the headline claim as a semi-formal
   quantified sentence, then fills A.prefix, A.matrix, A.flags, B.problem, B.outcome and B.flags, each with a
   verbatim quote, its file and line, and a confidence.
3. **Two independent labellers per family.** Two passes with different batchings, so no agent sees the other's
   labels. Default model, not the cheap one.
4. **Adjudication.** Fields where the two passes disagree go to a third agent that reads the full theorem
   statements and decides, recording why.
5. **Validation.**
   - Inter-rater κ per field between the two passes (target ≥ 0.8 on A.matrix, B.outcome; ≥ 0.7 on A.prefix).
   - Agreement with the 39 deep labels through the v1 mapping.
   - A hand check of 20 random families.
6. **Pilot first.** Run steps 1–5 on the 39 gold families plus 11 random ones (50 total). Revise any bucket with
   κ < 0.7 or with more than 10% "other" before the full run.

Cost: the full run is about 2 × 372 labels in ~24 agent batches plus ~3 adjudication batches; the pilot is about 4 batches.

## Outputs

`data/abc_v2/`: `inputs/<fid>.txt`, `pass_a.jsonl`, `pass_b.jsonl`, `adjudicated.jsonl`, `labels_v2.json`,
`stats.json`, `report.md` (distributions, prefix patterns, cross-tables with subject and Lean, κ).
