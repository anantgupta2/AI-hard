# Discoverability test for family 304 (Hilbert–Smith), protocol P-C1C2

Scaled-down run of the protocol in data/pilot/304/novelty.json (`discoverability_protocols`).
- Proposer: Claude subagents (training cutoff June 2026, before the 304 manuscript date 2026-09-23). Canary probe passed: the model does not know of a general proof or of any signature / Witt / L-theory approach (canary.md).
- Each sample is an independent subagent that reads only its arm prompt and writes one answer file (tool use is checked: read + write + hand-back).
- Arms: bare (problem only), open (protocol: problem plus 304's bibliography as titles), template (open plus the finite-group signature-divisibility fact), pivot (open plus the paper's test categories, fixed lattice, averaged test, finite sheets and move-test, with the character classes and equal-parts argument hidden).
- Deviations from the protocol: n = 10/10/10/6 instead of 256 per arm; one proposer family; the judge is a separate Claude instance (same family), blinded to arm; no positive/negative controls; no human topologist check.
