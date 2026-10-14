# v2 adjudicator brief

Two independent labellers labelled every family on the v2 buckets (`data/abc_v2/BUCKETS_PLAN.md`: read the
"v2 buckets" and "Tie-break rules" sections, including rules 11 and 12). For the families in your batch they
disagree on at least one field. The disagreements, with both full records, are in `data/abc_v2/full/disputes.json`
(key = fid; `fields` lists the disputed fields).

For each fid in your batch:
1. Read the family's input `data/abc_v2/inputs/<fid>.txt`. Open the main .tex under `data/raw/openai-math/`
   (path in the input) if the theorem statements there do not settle it. Do not search the web.
2. Decide every disputed field, applying the buckets and tie-break rules strictly. You may pick a value neither
   labeller chose. Check the agreed fields too; if one clearly breaks a rule, correct it and say so.
3. Write one JSON line per fid with the **complete final record** (the same keys as the labeller records:
   `fid, claim_formal, A_prefix, A_matrix, A_flags, B_problem, B_outcome, B_flags, lean_vs_headline, quote_A,
   quote_B, conf`), plus `adjudicated_fields` (the fields you decided or changed) and `reason` (≤ 40 words: which
   rule or which text decided it).

Write the file named in your task. Validate it with a short python3 check (every fid once, codes valid, JSON parses).
Do not git commit and do not write any other repo file. Final message: lines written, how many disputes went to
pass A's value, to pass B's, or to a third value, and any rule you found ambiguous.
