# Proof-type labeller brief (two axes)

Read data/abc_c/C_PLAN.md first (both tables and all tie-break rules; they are binding). For each family in your
batch, read data/abc_c/inputs/<fid>.txt: the summary, the v2 headline sentence, and for each manuscript the abstract,
main statements, the paper's own proof-strategy paragraphs, the section outline and the openings of its longest proofs.
If the input does not settle the backbone, you may open the manuscript's main .tex (path in the input) under
data/raw/openai-math/. Do not search the web and do not read other labellers' files.

For each fid, first write `backbone`: one sentence on the top-level argument of the headline proof. Then pick
`form` (F1–F6) and `engine` (E1–E7) for that backbone, with secondaries, the `computer_assisted` flag, one verbatim
`quote` (≤ 40 words) that supports the form, and `conf` in [0,1] for form and engine. If nothing fits, use "other"
and explain in `backbone`.

Output: one JSON line per fid in the file named in your task, e.g.
{"fid":"248","form":"F2","form_secondary":["F3"],"engine":"E1","engine_secondary":["E3"],"computer_assisted":false,"backbone":"Assume F amenable; a recursive Hilbert-ball colouring of dyadic partitions plus Følner averaging yields an approximate fixed point of a fixed-point-free map.","quote":"The proof turns approximate translation invariance of finite averages of scalar functions on F into an approximate fixed point of a Lipschitz map on a Hilbert ball.","conf":{"form":0.8,"engine":0.7}}
Validate with a short python3 check (every fid once, codes valid, JSON parses). Use only your own scratch folder
for helper scripts (the one named in your task). Do not commit and do not write other repository files.
Final message: lines written, and every "other" or confidence < 0.6 with one line each.
