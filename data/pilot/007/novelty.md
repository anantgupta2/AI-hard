# Family 007: novelty analysis ("Ordinary two-point correlations and the corrected Elliott conjecture")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`, which uses the 287 keys plus `precedent_checks`, `bridge_novelty` and `sources`.

Inputs:
- `trace.json`/`.md`, the only prior analysis for 007. There is no `family.json`, `lean.json` or `f1_*.json`, so I extracted the paper's key items myself from `build/` (main.tex, introduction.tex, quantitative/01–08, qualitative/*).
- Full text of Pilatte arXiv:2310.19357v3 and Helfgott–Radziwiłł arXiv:2103.06853v2, both fetched as PDFs with the text extracted.
- Tao–Teräväinen arXiv:2512.01739v2, read only through the WebFetch summarizer.
- Lean spot checks by grep; Lean was not compiled.

**L** = Mathlib d13f23b plus 007's 19-entry `refs.bib`. L contains Pilatte26, HR21, TT26, Braverman10, AGM03 and Linial–Nisan90.

## 1. Provenance verdict first: **no** model-produced precedent

| Work (2025–26 / named precedent) | AI disclosure | Contains 007 candidates? |
|---|---|---|
| Pilatte, arXiv:2310.19357. v1 2023-10-30; v3 2026-08-25; JAMS online 2026-09-10 | None, on the abstract page or in the extracted full text. v1 is from 2023 | **C1: close variant** (Prop. 9.1, Lemma 9.2, Lemma 9.4). C6, C7, C9: close variant. C2, C3, C8: absent |
| Tao–Teräväinen, arXiv:2512.01739. v1 2025-12-01; v2 2026-04-25 | **Yes, but minor and unrelated.** Relayed by the summarizer, so unverified: "ChatGPT was used to generate initial code for the graphs … the text in this paper is entirely human-generated". A forum observation "using GPT 5.4 Thinking" is credited for an *irrationality* side problem | Absent. Its §3 uses J bands for decoupling, 1/p centring, Ramaré, the circle method and the Selberg sieve |
| Helfgott–Radziwiłł 2021 (named method source) | – | **C1's problem stated verbatim** (§5, "Obtaining cancellation from lone primes"). **C3's role** (§3.3, a multidimensional Kubilius model) |
| Uncited 2026 neighbours: Guo arXiv:2608.23500; Hughes arXiv:2609.28526 | None (abstract pages) | Absent. Both are logarithmic only; Hughes explicitly excludes natural density |

Web searches turned up nothing earlier that is model-produced. I searched for ordinary two-point Chowla with ChatGPT, GPT-5 or OpenAI, for 2026 non-logarithmic Chowla, and scanned all 719 release manuscripts for Chowla, Elliott, Liouville and related terms. The only hits were coverage of the release itself.

**Flag: no.** The one timing note is that the template for the whole method, Pilatte's JAMS paper, appeared 14 days before the paper date. That is human work.

## 2. Final grades

| # | Item | Nearest neighbour (verdict) | T2 | T3 | Final | conf |
|---|---|---|---|---|---|---|
| C1 | Mixed difference over hybrids plus common-hybrid witness cover (q:mixed-difference, q:witness-cover, q:active, q:singletons; trace PV9, "turning point") | Pilatte Prop. 9.1/Lemma 9.2/Lemma 9.4(1): only sieve terms whose modulus contains all singleton primes escape cancellation (**close variant**). HR21 §5 poses the same obstacle | object passes; principle in L | knockout for Thm 1.1 | **N2** | 0.70 |
| C2 | Two-band divisor graph: uncentred core plus vertex-normalised centre band with θ = β_Z² centring (graph-setup; lem:trace-integration; trace PV4, insight) | No arithmetic precedent found. The principle "centre by the tilted mean" is standard (normalised-adjacency centring). Internal sibling: Part I's padding/supply split | pass | knockout for Thm 1.2 | **N2 (borderline N3)** | 0.55 |
| C3 | Braverman bounded-independence comparison plus AGM correction (q:finite-law; PV8) | Braverman and AGM themselves (equivalent); HR21 Kubilius model (same role) | fail | knockout for Thm 1.1 (Lean proves Braverman, 72 files) | **N0 transfer**; new bridge | 0.80 |
| C4 | Fixed-B order of limits plus finite-prime stability (PV5) | standard | fail | knockout for Thm 1.2 | N1 | 0.75 |
| C5 | First-visit tree plus subtree-weight identity (PV6) | trace-method exploration trees; percolation total probability | fail | yes | N1 | 0.70 |
| C6 | Conditional cylinder sieve (PV7) | Pilatte Def. 13.3 and Lemmas 13.4/13.6, which the paper names | fail | yes | N2 | 0.60 |
| C7 | J supplies plus whole-tuple non-backtracking matrix (PV10) | Pilatte §§4–5; HR21 §9 | fail | yes | N1 | 0.75 |
| C8 | Padding divisors (4^ω weights, √w normalisation, anti-concentration) plus forest code uniform over padding. Extracted from the paper; not a trace pivot | no padding in Pilatte or HR. Smoothing by an independent factor is standard | weak pass | yes | N2 | 0.50 |
| C9 | Random-prime rank estimate over ℝ | HR21 §§6–7; Pilatte §11 | fail | yes | N1 | 0.65 |
| C10 | Single narrow core band (the second insight step) | parameter simplification | fail | part of C2 | N1 | 0.70 |

**Overrides of the trace analyst.**
- **E1/PV9: N2–N3 → N2.** The paper credits Pilatte only for the "active-prime and triangular" half. But Pilatte §9 already contains the covering principle in sieve form: Lemma 9.2 says a progression whose modulus misses a singleton prime cancels, and Prop. 9.1 combines this with a rank bound. HR21 §5 states the identical obstacle ("restrict A to X and still get cancellation"). 007's real contribution is the packaging: an exact discrete-derivative identity, used only for existence, replaces the truncated sieve and its coefficient and remainder bounds, and minimal covers with private primes replace rank.
- **E2/PV4: N2–N3 → N2 (borderline).** No arithmetic precedent was found, so this is the family's best candidate. Two things hold it at N2:
  - the θ match is the textbook rule of centring under the tilted measure, and the trace shows β²/p centring was already present in the single-band design retrieved from Pilatte;
  - the two-role split (uncentred weighted primes for savings, centred primes for cancellation) has a same-paper sibling in Part I's padding (C8).
- **E3/PV8: N0 / N2 bridge → N0 transfer, with the bridge recorded as new** (see §4).

## 3. Discoverability protocols (Test 4, not run)

The full specification is in `novelty.json → discoverability_protocols`.

**Common settings.**
- **Models:** training cutoff strictly before **2026-09-24** (the 007 date). Each must pass a canary: it does not know that ordinary two-point Chowla has been claimed. No tools.
- **Excluded models:** the OpenAI model that produced 007 and its lineage. They run only as a reference arm.
- **Library arms:** **L** (Pilatte and HR21 included; they are precedents, not contamination) vs **L minus §§9, 13 of Pilatte and §§3.3, 5 of HR21**.
- **Sampling:** n = 256 per arm, T = 1, pass@k for k = 1…256.
- **Judging:** two LLM judges given the paper's "adapt" remarks and this neighbour list. A human analytic number theorist checks every hit. Hits that reproduce the precedent route are scored in a separate column.

**P-C1.**
- **Hide:** q:mixed-difference, q:witness-cover, q:active and q:singletons, plus everything downstream.
- **Give:** everything through eq. q:word-product, the lit/unlit expansion, q:many-unlit and the rank lemma.
- **Hit:** an exact discrete-derivative bound for the deletion damage, plus a common-configuration cover forcing many eliminable congruences. Pilatte's sieve plus Lemma 9.2 counts as "precedent reproduction".
- **Trace distances:** pivot distance 2, chain depth 2.

**P-C2 (decisive for any D3).**
- **Hide:** graph-setup and the whole of Part II downstream of it.
- **Arms:** A gives Part I, which contains the padding sibling; **B hides Part I** and is decisive.
- **Hit:** (i) uncentred weighted primes for savings plus centred primes for cancellation, *and* (ii) a centring constant equal to the tilted mean under the vertex normalisation, so that one-edge primes cancel. Either part alone earns partial credit.
- **Trace distances:** pivot distance 2, chain depth 2.

**P-C3 (transfer control).**
- **Hide:** the finite-law section.
- **Hit:** bounded-independence fooling of AC0. Kubilius or fundamental-lemma answers are logged as an alternative route and checked for validity.
- **Trace distances:** pivot distance 1, chain depth 1.

**Other items:** C4–C7, C9 and C10 all have pivot distance 1. C8 does not appear as a trace pivot. One-line protocols for each are in the JSON.

**Trace context.**
- Both decisive pivots arrive right after a stated requirement, with no restart: the single restart is a 12-word counterexample probe.
- Part II shows no search at all.
- This is weaker evidence of hard discoverability than in 287.

## 4. Family verdict

**family_D: D2, confidence 0.65.**
- It rests on C2 (N2, borderline N3) and C1 (N2), with C6 and C8 as further N2 support.
- **Falls to D1** if vertex-normalised tilted-mean centring, or a sieve-free singleton-cover argument, turns up in the HR/Pilatte/TT line. TT26 §§3–4 and Tao's December 2025 blog posts are the places to look.
- **Rises to D3** only via C2: P-C2 arm B must fall below threshold *and* an expert must confirm there is no arithmetic precedent.
- Correctness is unrefereed: this is a claimed resolution of a famous open problem.
- The Lean comparator for all three theorems is discharged via `TwoPoint/Main.lean`. Grep finds no sorry, admit or axiom in about 232k lines, and both Braverman and the MRT inputs are proved. Lean was not compiled.

**provenance_flag: no** (see §1).

**bridge_novelty.**
- **TCS → number theory (Braverman AC0 fooling plus the AGM correction): new bridge for a known role.**
  - No prior use of Braverman, Bazzi or Tal-type results in sieve or correlation problems was found. Green 2012 links Möbius and AC0 only in the opposite direction.
  - The role itself (comparing integers with an independent residue model) was filled in HR21 §3.3 by the Kubilius model.
  - Linial–Nisan's approximate inclusion–exclusion had already signposted the link.
- **Spectral graph theory** (high trace, non-backtracking, Ihara–Bass) → number theory: known route (HR21, Pilatte).
- **Rota poset Möbius** → sieve: known route (HR21 §3; Pilatte App. B).
- **Erdős–Szekeres:** a known tool.
- **C\*-dynamics/KMS:** attempted in the trace, abandoned, and absent from the proof.

## 5. Open questions

1. Verify the TT26 AI quotes against the PDF.
2. Is C3 replaceable by HR21's multidimensional Kubilius model? If so, the TCS bridge is optional.
3. Ask an expert whether tilted-mean centring (θ = β²) exists in the arithmetic graph literature.
4. Read Pilatte §13 and TT26 §3 in full.
5. **Catalog gap.** `catalog_families.csv` omits the Lean dir `OAI/NumberTheory/TwoPoint` (138k lines, holding `Main.lean`, `Circuits/` and `MixedDifference.lean`). 007 needs a Lean analyst pass for DAG shares and step 3b.
6. Compile Lean.
7. Order of discovery between the trace's two parts: if the padding design came first, C2's split is an intra-paper transfer.
8. Inspect the unverified preprint "Proof of Chowla conjecture" (ResearchGate, April 2026).
