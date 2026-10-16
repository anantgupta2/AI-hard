# Judge brief (family 304 discoverability, protocol P-C1C2)

You grade proposals for proving that no continuous action of the p-adic integers Z_p on a connected n-manifold is faithful. Each file in data/pilot/304/discoverability/blind/S01.md … S36.md is one independent proposal. You do not know which prompt produced which file; do not try to guess.

The target idea (from a 2026 manuscript; you must not search for it) is:
(a) an integral invariant valued in a group with a FIXED lattice / bounded denominator (a signature, Witt-group or L-group class) attached to the action or to a test map out of the orbit space;
(b) split into parts indexed by characters of Z_p or of its finite quotients Z/p^k, with integrality preserved;
(c) an argument that the parts are equal (or permuted transitively) and sum to a fixed nonzero class, so p^k-divisibility for every k contradicts the fixed lattice.

Grade each file:
- HIT: (a), (b) and (c) are all present, stated as a concrete mechanism (not only mentioned as a possibility).
- PARTIAL_AC: (a) and (c) present (an integral signature/Witt/L-type invariant forced to be divisible by p^k for all k against a fixed bound) but without the character splitting (b).
- PARTIAL_B: (b) present (character / isotypic splitting of a Witt or signature class) without a fixed lattice argument.
- YANG_BRW: a divisibility or dimension argument in orbit-space (co)homology only (Yang / Bredon–Raymond–Williams style); this does not count.
- MISS: anything else.
Also record: uses_signature_or_witt (true/false), names the main obstacle it leaves open (≤ 20 words).

Output one JSON line per file to the path named in your task: {"file":"S01","grade":"HIT|PARTIAL_AC|PARTIAL_B|YANG_BRW|MISS","uses_signature_or_witt":true,"why":"≤ 30 words","open_gap":"≤ 20 words"}. Read only the 36 files in blind/ and this brief. Do not search the web. Validate that all 36 files appear once. Do not commit. Final message: counts per grade.
