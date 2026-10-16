# Proof-type adjudicator brief

Two independent labellers coded every family on C.form and C.engine (data/abc_c/C_PLAN.md: read both tables and all
tie-break rules). For the families in your batch they disagree on form, engine or both. Both full records are in
data/abc_c/full/disputes.json (key = fid; `fields` lists the disputed fields).

For each fid in your batch:
1. Read data/abc_c/inputs/<fid>.txt. Open the main .tex under data/raw/openai-math/ (path in the input) if the
   proof's backbone is still unclear: look at the section that proves the headline theorem. Do not search the web.
2. Decide each disputed field, applying the rules strictly. You may choose a value neither labeller chose.
3. Write one JSON line per fid with the complete final record (keys `fid, form, form_secondary, engine,
   engine_secondary, computer_assisted, backbone, quote, conf`) plus `adjudicated_fields` and `reason` (≤ 40 words:
   which rule or which text decided it).

Write the file named in your task; validate it (every fid once, codes valid, JSON parses). Use only your own scratch
folder (named in your task). Do not commit and do not write other repository files. Final message: lines written, how
many disputes went to pass A's value, pass B's, or a third value, and any rule you found ambiguous.
