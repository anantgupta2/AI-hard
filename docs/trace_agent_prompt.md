# Trace-analysis agent brief (shared across families)

You are a REASONING-TRACE analyst on a research project, at `C:\Users\anant\AI-Hard`. The project tests whether AI-produced mathematics contains genuine **eureka steps (non-analytic cuts)**: new definitions or lemmas that are hard to find and that buy a large drop in proof budget. The anchor example is Cook–Reckhow's extension variables for pigeonhole in extended resolution. Importing a known concept from another field is *transfer*, not a eureka step; a known route between fields is not one either.

Read these first:
1. `docs/PLAN.md`: the codebook, the novelty grades N0–N3, the eureka types F1–F5, and the section "Search dynamics from the reasoning traces (CDCL analogy)".
2. `data/pilot/287/trace.json` and `data/pilot/287/trace.md`: the **worked example and reference schema**, family 287, already done. Reuse its JSON keys exactly, and apply its `search_dynamics.level_assignment_rules`, so results are comparable across traces. If a rule doesn't fit your trace, extend it and document the extension.

The trace is OpenAI's abridged, summarized chain of thought, with occasional VERBATIM EXCERPT blocks. Distinguish what the model did from the summarizer's framing, and treat the selection as curated, so all counts are lower bounds. You may skim the final paper's LaTeX, but only to map trace ideas to final-paper items.

Required content, at **maximal detail** (completeness over brevity):
- **timeline:** phases, approaches, literature invoked, outcomes.
- **dead_ends:** each with a full `lesson` object:
  - obstruction;
  - lesson_statement (+ verbatim excerpt);
  - lesson_form: negative result / constraint / salvaged tool / reformulation / sharpened target;
  - generality;
  - known_in_literature (with reference);
  - correctness;
  - salvage;
  - reused_at / influence;
  - what_was_not_learned.
- **pivots:** each with:
  - trigger;
  - new_idea;
  - final_paper_item;
  - classification: known technique / transfer / known route / new bridge / new concept;
  - pivot_distance;
  - chain_depth;
  - F_type.
- **search_dynamics (CDCL coding):** everything in the 287 schema:
  - nodes with levels, lengths (words, share), child decisions, propagations, literature count and time markers;
  - backtracks, each with distance d, trigger_type (conflict / insight / unclear) and branch length;
  - for each insight-driven backtrack: simplification_estimate, origin (retrieved / constructed) and novelty_candidate;
  - restarts, with the clauses that survive;
  - learned_clauses, with reused_at, and the reuse rate;
  - final_route_conflict_driven, with the clause chain;
  - fraction of the trace before the final route;
  - the branch-length stats and the length-vs-distance relation.
- **knowledge_flow:** how lessons accumulate into the final route, and which were necessary.
- **self_assessment**, **verification_behaviour**, **discoverability_evidence**, **items_seen_in_trace**.
- **eureka_candidates:** your shortlist of trace-level candidates (N2/N3-looking constructed steps), with arguments for and against each.

Deliverables, in `data/pilot/<FID>/`:
- `trace.json`
- `trace.md`: a readable report, any length needed. It must include an ASCII or Mermaid search tree, the metrics table, the decisive pivots, and how this trace compares with 287.

Your final message should be a ≤200-word summary, with key metrics: n_backtracks by trigger, distance histogram, n_restarts, fraction before the final route, the decisive pivot(s) and their classification. Use `sys.stdout.reconfigure(encoding='utf-8')` when printing Unicode from Python on Windows. Quote sparingly (the repo is Apache-2.0).
