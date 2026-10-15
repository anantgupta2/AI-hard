# Lean scope check brief

For 67 families our v2 labels say the Lean statement is `weaker` than, or `different` from, the family's headline
claim. The question now: **is the gap disclosed by OpenAI, and is our label right?** Each family's bundle
`data/lean_scope/bundles/<fid>.txt` has OpenAI's summary, our headline and notes, the manuscripts (with whether
`lean/formalization.yaml` lists each one as a paper "with a formalized main result"), OpenAI's own scope note
`lean/docs/<fid>.md`, and the exact comparator statements. You may open a manuscript's .tex under
`data/raw/openai-math/preprints/` to find its main theorem. Do not search the web. Do not re-run Lean; trust it.

For each fid decide:
1. `formalized_ms`: the title of the manuscript the Lean belongs to (the one the scope note links), and
   `ms_is_headline`: whether that manuscript states the family headline (true/false).
2. `lean_vs_ms_main`: the comparator statement(s) against that manuscript's own main theorem: `full` (states it,
   up to harmless formalization choices), `partial` (special case, weaker bound, one half, the setting only),
   or `lemma` (an intermediate or auxiliary result the main theorem uses).
3. `disclosure`: does OpenAI's scope note say plainly what the Lean does NOT cover? `explicit` (it says what is
   left out, e.g. "verifies only…", "does not prove…"), `implicit` (it describes the Lean statement accurately
   without claiming more, but does not flag the gap), or `overstated` (the note or the comparator name claims the
   headline or the main theorem is formalized when it is not).
4. `yaml_listed_but_partial`: true if formalization.yaml lists the formalized manuscript as having a formalized
   main result while `lean_vs_ms_main` is `partial` or `lemma`.
5. `our_label_check`: `confirmed` if our weaker/different label is right; `should_be_same` or the other value
   (`weaker`/`different`) if not. Rule: `weaker` = the Lean statement is implied by the headline; `different` =
   neither implies the other (a lemma, a companion result, a different case).
6. `category`, one of:
   - `companion_full`: Lean fully formalizes the main theorem of a companion manuscript, not the headline one.
   - `headline_partial_disclosed`: Lean is a partial version of the headline paper's result and the note says so.
   - `headline_lemma_disclosed`: Lean is a lemma toward the headline and the note says so.
   - `partial_undisclosed`: partial or lemma, and the note does not flag it (implicit) or overstates it.
   - `label_error`: our label was wrong (Lean actually states the headline).
7. `gap`: ≤ 25 words, what exactly the headline has that the Lean lacks (or why it is a label error).
8. `quote`: the scope note's key sentence (verbatim, ≤ 40 words).

Output: one JSON line per fid in the file named in your task, keys
`fid, formalized_ms, ms_is_headline, lean_vs_ms_main, disclosure, yaml_listed_but_partial, our_label_check, category, gap, quote`.
Validate with a short python3 check (every fid once, JSON parses, enums valid). Do not git commit and do not write
any other file. Final message: lines written, the counts by category, and every `overstated`, `partial_undisclosed`
or `label_error` with one line each.
