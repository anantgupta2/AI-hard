# v2 A/B labeller brief (high-confidence pass)

You label the **headline claim** of each family on the v2 buckets defined in `data/abc_v2/BUCKETS_PLAN.md`
(read its "v2 buckets" section first, including the precedence rules). Work only from the family's input file
`data/abc_v2/inputs/<fid>.txt`: OpenAI's summary; for each manuscript the abstract, the start of the introduction
and its theorem statements; and, where one exists, the Lean comparator challenge, which is the exact formal statement.
If something essential is missing, you may open the manuscript's main .tex (path given in the input) under
`data/raw/openai-math/`, but do not search the web.

The headline claim is the principal result of the family: the one the title and summary lead with. If the family
bundles several results, label the principal one and mention the others in `notes`.

## Procedure for each family

1. Write the headline claim as one **semi-formal quantified sentence** (`claim_formal`), e.g.
   `∀ closed 4-manifold X, ∀ a.c.s. J on X: (∃ symplectic ω taming J) → (∃ symplectic ω' compatible with J)`.
   When a Lean comparator exists, read its `theorem` statement and make your sentence agree with it; note any
   gap between the Lean statement and the paper's headline in `notes`.
2. **A.prefix**: read the outer quantifiers off your sentence, outermost first, over the main objects only.
   Hypothesis-side quantifiers inside an implication do not count; parameters that only index a family of
   witnesses count as ∀. Alphabet: `∀ ∃ ∃! ∀ᵍ ∀^∞ ℙ ∃^∞`, or `none` for a closed statement about one specific
   object. Examples: `∀∃`, `∃`, `∀ᵍ`, `∀^∞`, `none`.
3. **A.matrix**: one of M1–M11, applying the precedence rules.
4. **A.flags**: any of `specific_instance, asymptotic_only, effective, ineffective, conditional_on, restricted_range,
   finite_checkable, probabilistic`. For `conditional_on` give the hypotheses, e.g. `{"conditional_on": ["GRH"]}`.
   Mark `effective`/`ineffective` only when the claim involves constants or bounds; otherwise omit both.
5. **B.problem**: P1–P5. **B.outcome**: O1–O9. **B.flags**: any of `full_only_with_prior_results, adds_corollaries,
   builds_on_model_output`.
6. Give one short verbatim **quote** supporting A and one supporting B, each with its source (`abstract`,
   `intro`, `theorem`, `lean`, or `summary`), and a **confidence** in [0,1] for each of A.matrix, A.prefix and B.outcome.

If no code fits, use `"other"` and explain in `notes`. That is useful signal for revising the buckets, so do not force a fit.

## Output

One JSON object per line, in the file named in your task, one line per fid, for example:

```
{"fid":"342","claim_formal":"∀ closed 4-manifold X, ∀ J: (∃ ω taming J) → ∃ ω' compatible with J","A_prefix":"∀∃","A_matrix":"M2","A_flags":[],"B_problem":"P1","B_outcome":"O1","B_flags":["adds_corollaries"],"quote_A":{"src":"abstract","text":"every smooth almost complex structure … is compatible with a symplectic form"},"quote_B":{"src":"abstract","text":"positive solution to Donaldson's tamed-to-compatible conjecture"},"conf":{"A_matrix":0.9,"A_prefix":0.9,"B_outcome":0.95},"notes":""}
```

Validate the file with a short python3 check before finishing: every fid once, codes valid, JSON parses.
Do not git commit. Do not write any other file in the repo. Your final message: lines written, and every
`other` or low-confidence (< 0.6) field with a one-line reason.
