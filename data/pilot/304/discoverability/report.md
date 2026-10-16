# Discoverability test, family 304 (Hilbert–Smith), protocol P-C1C2 — results (2026-10-16)

Setup: see README.md. 36 independent samples (Claude subagents, cutoff June 2026, canary passed), each read only its
arm prompt and wrote one answer (3 tool calls each, verified). Two blind judges graded against the protocol's
equivalence rule (judge_brief.md); they agreed on 34/36. A HIT needs (a) an integral signature/Witt/L-type invariant
with a fixed lattice or bound, (b) a split by characters of Z_p or Z/p^k, (c) equal parts summing to a fixed nonzero
class, so p^k-divisibility for every k is a contradiction.

| Arm | What the prompt adds | n | HIT (both judges) | HIT (one judge) | Partial | Uses signatures / Witt groups at all |
|---|---|---|---|---|---|---|
| bare | problem, the classical reduction, Newman, Yang | 10 | 0 | 0 | 0 (9 Yang/BRW-style, 1 miss) | 0 / 10 |
| open (protocol) | + 304's bibliography, as titles (includes Balmer, Woolf, Ranicki–Weiss on Witt groups) | 10 | 0 | 1 | 7 | 10 / 10 |
| template | + the finite-group fact: free G-action ⇒ equal isotypic signatures, |G| divides the signature | 10 | 7 | 1 | 1 | 10 / 10 |
| pivot | + the paper's test categories, fixed sphere lattice, averaged test, finite sheets, move-test | 6 | 2 | 0 | 4 (sheets, not characters) | 6 / 6 |

Reading:
- The bridge itself is the hard step. With the bare problem, no sample out of 10 reached for signatures, Witt groups
  or L-theory; 9 of 10 stayed inside orbit-space cohomology (Iwasawa modules, Smith theory, the Yang n+2 jump),
  the route the literature already took.
- The bridge is triggered by the reading list. Adding 304's bibliography as bare titles made every sample use
  Witt groups, but without the equal-parts mechanism (0–1 HIT in 10).
- Given the classical finite-group template, the decisive C1+C2 mechanism is found almost every time (7–8 of 10).
  Under the protocol's decisive arm this keeps C2 at N2, not N3: it is a short step from a classical template.
- With the paper's own machinery (pivot), samples use the fixed lattice and the p^k sheets directly; 2 of 6 add the
  character split, 4 of 6 count sheets instead of characters.
- No sample is a proof. The common open gaps are exactly the paper's hard parts: contributions of non-free strata
  uniformly in k, and a k-independent bound on the moving multiple N.

Deviations from the protocol: n = 10/10/10/6 rather than 256 per arm; one proposer family (Claude); the judges are the
same family as the proposer; no positive or negative controls; no topologist check; the subagents may have seen the
repository's CLAUDE.md (which describes the project but not 304's content).
