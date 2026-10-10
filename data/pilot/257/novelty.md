# Family 257: novelty analysis ("A hyperbolic group without a geometric CAT(0) action")

Analyst role: novelty. Date: 2026-10-09. Machine-readable version: `novelty.json`.

**Inputs:**
- `family.json`/`.md` (Phase 1, same analyst);
- the preprint and the Lean dir;
- arXiv abstract pages for the 2025–26 citations;
- web searches.

There is no reasoning trace and no `f1_*.json`. **L** = Mathlib d13f23b plus 257's bibliography. No entry in the bibliography is model-produced, so L⁻ = L.

## 1. Provenance verdict: **no**
- **The 2025–26 citations are human work, cited only for the problem's status.**
  - Stark, arXiv:2506.10108, an expository survey submitted 2025-06-11.
  - Duchesne–Simon, arXiv:2603.03863, submitted 2026-03-04.
  - Neither abstract page discloses AI assistance. These checks went through a summarizer and are unverified.
  - Neither paper contains any candidate.
- **No model-produced prior work was found.** I searched the problem's name together with ChatGPT, GPT-5, OpenAI and "AI-assisted". OpenAI's August 2026 "Ten advances" (Astra) list contains no hyperbolic-group or CAT(0) item.
- **Sibling families share no machinery.** The hyperbolic-group families 246 (Cannon) and 252 (not residually finite) use none of 257's tools.

## 2. Final grades
| ID | Candidate | Final N | F | Conf. | Main reason |
|---|---|---|---|---|---|
| C1 | Uniform conditional test (P37, with P31, P35, P36) | **N3** | F5 | 0.40 | No target-uniform neighbour. IKN, Toyoda and Naor–Silberman all have target-dependent constants. Built from cited parts (Sturm, IN barycenter, extension couplings). |
| C2 | Nested near-critical random model (P08) | **N2** (↓ from N3) | – | 0.50 | The decoration layer is the square/hexagonal model in its known hyperbolic regime (Odrzygóźdź). Only the fan/top nesting is new. |
| C3 | Doubled-Fano gadget + all-CAT(0) finite obstruction (P03, P47) | **N3** | F3 | 0.50 | Fano/Heawood is classical but appears in the opposite role, as a CAT(0)-realizable Ã₂ link. No obstruction of this type was found. The gadget is tiny, non-analytic, and its carriers are used by 43% of the DAG. |
| C4 | Shared-cost-once counting with weights w_b | **N2** | – | 0.70 | The paper itself names Ollivier 2004 and AFL 2017. |
| C5 | Six-letter displacement bound (P35) | **N2** | – | 0.55 | Pair coverage at density ≈ 1/2 is standard; the rest is a short Cauchy–Schwarz. |
| C6 | Closure U + star/extension counts (P27–P31) | **N0** | – | 0.60 | Transfer of Spencer-style extension counting from random graphs. Not cited by the paper, and not web-verified here. |

**family_D = D3 (provisional), confidence 0.45.**
- **Rests on:** C3 or C1.
- **Falls to D2 if:**
  - the discoverability arms that hand over the limiting identities (P-C3 arm D) or the coupling (P-C1 arm R) hit at a high rate;
  - an expert finds a prior target-uniform fixed-point argument, or a prior Fano-type CAT(0) obstruction;
  - the comparator fails.
- **Floor:** D2, carried by C2, C4 and C5.

## 3. Test notes
- **Test 1.**
  - *C1:* the nearest neighbours share its purpose (fixed points of random hyperbolic groups on cocompact CAT(0) spaces) but not its mechanism. The paper's advance is the quantifier swap: one group for all targets, where Toyoda and IKN need one group per target or target family.
  - *C3:* the forced configuration is "cubical": each core hexagon is the skew hexagon of a unit cube, with cos ±1/3, radius √3/2, and three-step distance equal to the body diagonal √3. The doubling plus the one omitted incidence makes this cubical realization impossible in every complete CAT(0) space. I found no precedent for this.
- **Test 2.** All candidates pass. The comparator hides the witness behind ∃K, and no candidate is a subterm of the goal or of L.
- **Test 3** (patched Lean DAG, 3,726 nodes).
  - *C3:* the template carriers Edge/Field are dependencies of 42.7% and 40.5% of the DAG. The obstruction proof itself dominates only 1.3%.
  - *C1:* the no-action branch is 12.2% of the DAG; `conditional` itself dominates 0.9%.
  - The global 20% proxy undercounts C1, because most of the DAG serves the hyperbolicity and asphericity conjuncts. I recommend per-conjunct shares.
- **Test 4 (protocols written, not run).**
  - *Models:* cutoff before 2026-09-25; the OpenAI and Astra models are excluded; canary probes check for leakage.
  - *Arms:* O (open), R (route) and D (design hint).
  - *Hits:* exact template isomorphism, or a functional hit (any template within budget whose configuration is provably contradictory, checked by Lean where possible).
  - *Sample sizes:* k ∈ {1, 4, …, 1024}.
  - *Estimated pivot distance and chain depth (no trace exists):*

    | Candidate | Pivot distance | Chain depth |
    |---|---|---|
    | C1 | 2 | 1 |
    | C3 | 1–2, given the identities | 2 |
    | C2 | 2 | 0 |

## 4. Bridge novelty
| Import | Classification |
|---|---|
| Harmonic-energy fixed-point framework | known route (IKN, Toyoda) |
| Ollivier/AFL diagram counting with separators | known route |
| Ultralimits | known route |
| Hurewicz/Whitehead | known route |
| Cartan–Hadamard | known route |
| Random-graph extension couplings → target-uniform metric tests | **new bridge** (tentative) |
| Sturm inductive means → group fixed-point obstruction | **new bridge** (tentative) |
| Fano finite geometry as a CAT(0) *obstruction* | **new bridge in this role** |

## 5. Open questions
- Re-run the comparator.
- Ask fixed-point experts (Izeki, Kondo, Toyoda, Naor–Silberman) whether C1 has a precedent.
- Ask CAT(0) and cubical experts whether C3 has a precedent.
- Verify Spencer's closure theorem for C6.
- Check how Kondo's δ = 1 spaces bear on the argument.
- Decide whether to use per-conjunct load-bearing shares.
