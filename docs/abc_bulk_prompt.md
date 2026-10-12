# Bulk A/B/C labelling brief (cheap pass, all 372 families)

You label the **headline claim** of each family on three codebook axes, from a short input bundle only:
`data/abc_bulk/inputs/<fid>.txt` (title, OpenAI summary, each manuscript's abstract, and its first few theorem statements).
Do not open the papers or the Lean. Do not search the web. One careful reading of the bundle per family is enough.

When a family has several manuscripts, label the principal result (usually the one the title and summary lead with).

## Axes

**A. Logical form** of the headline claim's innermost conclusion. Parameters that only index a family of witnesses count as an outer ∀.
- A1 Universal ∀ (every X has property P)
- A2 Existential ∃, including counterexamples and constructions of an object
- A3 Quantitative/sharp (an explicit bound, rate, constant, asymptotic, or exact value/formula)
- A4 Characterization ⇔ (iff, classification)
- A5 Impossibility ¬∃ (no X exists; lower bounds of the form "cannot", hardness, non-existence, independence)

**B. Relation to the posed problem.**
- B1 Confirms fully (proves the conjecture/answers the question affirmatively in the posed generality)
- B2 Refutes (disproves a conjecture, answers negatively)
- B3 Partial, conditional, or special case
- B4 Extends a known result (no named open problem; generalizes or sharpens)

**C. Proof method**, judged from what the abstract and statements say about how the proof goes. One primary label plus secondaries.
- C1 Construction (builds the object/witness/algorithm explicitly)
- C2 Induction/iteration (induction, descent, iterative scheme, bootstrapping)
- C3 Indirect/non-constructive (contradiction, compactness, probabilistic existence, fixed-point existence)
- C4 Estimation chain (chains of inequalities, analytic bounds)
- C5 Reduction/transfer (reduces to cited known results invoked without re-proof)

Precedence: if the witnessing object is built, C1 is primary. A minimal-counterexample argument is C3. C5 only for cited results invoked without being re-proved.

If the bundle does not say enough to judge C, still give your best guess and set `confidence` low.

## Output

Write ONE file, `data/abc_bulk/labels_<chunk>.jsonl`, one JSON object per line, one line per family in your chunk:

```
{"fid": "161", "A": "A2", "B": "B2", "C_primary": "C1", "C_secondary": ["C4", "C3"], "computer_assisted": false, "confidence": 0.8, "evidence": "≤25 words: the phrase(s) the labels rest on"}
```

- `confidence` in [0, 1] for the triple as a whole.
- `computer_assisted`: true only if the bundle mentions a real computer search or certificate.
- Every fid in your chunk list must appear exactly once. Valid codes only (A1–A5, B1–B4, C1–C5).

Do not git commit. Do not write any other file. Final message: the number of lines written and any fids whose bundle was too thin to label confidently.
