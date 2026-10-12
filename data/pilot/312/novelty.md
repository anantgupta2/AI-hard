# Family 312: novelty pass — Grothendieck homotopy hypothesis (Henry's pushout conjecture)

**Date:** 2026-10-12. **JSON:** `novelty.json` (287/003 keys).

## Full-text re-check (2026-10-12)
arXiv became reachable through curl (abstract pages plus PDFs, converted with `pdftotext`). Each entry is in `novelty.json` → `verified_checks`.
- **Lanari 2018, arXiv:1809.07923** (only v1 exists). Read: §1, Thm 3.1, all of §4, Lemma 5.4, §5.3, §5.6, the opening of §6, and Thm 6.10. The "(slightly less than) a path object" is a functorial path object, ev: P ⇒ Id × Id, on models of **C^W**, which is a coherator for n-*categories* with free left and right inverses (Thm 4.4, Rem 4.11). It is built from Lanari's **full** cylinders Cyl(D_k). The weakening is in the ambient theory, not in dimension. The dim-3 case climbs the coherator tower, and its top step is free by truncation (Lemma 6.1: "extending along i3 is automatic"). **There are no index-partial cylinders, no contractibility taken from higher cases, and no descending induction.** It supplies ingredients only, and it supports the template cap on C3.
- **Taylor, *A Tale of Two Paths*, arXiv:2609.20860.** Read in full (24 pp.). It re-presents Lanari's full cylinder as a colimit of pushouts along F_n(S^n) → F_n(D^{n+1}), built in ascending n. Thm 3.11 gives an isomorphism with Lanari's E. **It has no contractibility, no interpretation of operations, no pushout lemma and no cutoff.** It is a close variant of the bare object only (C2, already N2). **AI disclosure: none.** The paper thanks the author's husband and Simon Henry, and mentions using "Python script" with the algebraic coherator.
- **Lanari 2020, 1805.00156** (introduction), **Henry–Lanari 1905.05625** (introduction and §2) and **Henry 1609.04622** (§4.2 and §5.3) confirm the ingredient-only reading. These cover full cylinders, coskeletal models (Henry–Lanari: the pushout lemma is "a very plausible conjecture"), and relative path objects taken over a base.
- **Taylor 2607.28540, the one 2026 citation in 312.** No AI disclosure; its revision is credited to referee reports. Taylor is also confirmed as the author of 2604.09867 and 2510.22326.
- **Verdict:** none of these papers has partial cylinders in 312's sense, only the ingredients.
  - **C1 stays an N3 candidate**, with confidence raised from 0.35 to 0.45. It does not go higher because Test 4 is not run, there is no expert verdict, and the IH-strengthening reading is still open.
  - **family_D stays D3 (provisional)**, with confidence raised from 0.35 to 0.45.
  - Provenance: **no**.
  - The `precedent_check` in `downstream.json` is updated.

*The rest of this file is the original pass. Where it says "unread" or "snippet level" about 1809.07923 or 2609.20860, the section above supersedes it.*

**Inputs:**
- `family.json` and `family.md`. No trace was released and there is no `f1_*` file.
- Paper: the introduction and §3.1 of `03-partial-cylinders.tex`, plus `references.bib`.
- Lean, read at text level: `Expansion`, `CutoffExpansion`, `CylinderContractibility`, `ReflectedCylinder` and `ElementaryExpansion`.
- Release family 317, §8.
- 14 WebSearch queries.

**Web caveat:** WebFetch failed with DNS errors on every host (arxiv.org, alphaxiv, emergentmind, pith.science), and curl was refused by the proxy. All external evidence is therefore at the level of search snippets and abstracts. No full precedent text was read, and every paraphrase is unverified.

## Provenance verdict: **no**
- **312 cites no model-produced work.**
  - The one 2026 citation is Taylor, arXiv:2607.28540 (30 Jul 2026). It assumes a generalized pushout conjecture. Snippets attribute its change of method to referee reports, which suggests a human workflow. No AI disclosure surfaced.
- **Uncited 2026 neighbours show no AI disclosure at abstract level, but none was read in full:**
  - Taylor, *A Tale of Two Paths*, arXiv:2609.20860 (8 Sep 2026). It is about cylinder objects in coglobular ∞-groupoids and gives an isomorphism with Lanari's construction.
  - arXiv:2604.09867 and arXiv:2510.22326, the "inductive coherator". These induct *upward* from n to n+1 and are conditional.
- **Searches for the problem plus ChatGPT, GPT-5, OpenAI or "AI-assisted"** return only coverage of this release.
- **Model-produced descendant.** Release family 317, Thomason model structures (25 Sep 2026), cites 312 as `OpenAI2026`, summarizes its method (§8) and uses an analogous pushout argument with "stationary cylinders" in the strict setting. It states: "No result of [312] is a premise of this proof." Record this as possible release-wide device reuse; it is not a precedent.

## Final grades
| id | Item | N | F | conf | Lean-backed |
|---|---|---|---|---|---|
| **C1** | **Scheme E1: index-n partial cylinders bootstrapped by descending induction at a fixed coskeletal cutoff (I19+I25+I27→I28)** | **N3 (candidate)** | **F3+F2** | **0.45** (was 0.35; full-text re-check) | **yes** |
| C2 | Partial cylinder objects P_j alone (I25) | N2 | – | 0.6 | yes |
| C3 | Descending induction at cutoff q (I19 / `expansionContraction_all`) | N2 (template cap) | – | 0.7 | yes |
| C4 | Cylinder contractibility from higher indices, alone (I27) | N2 (merged into C1) | – | 0.5 | yes |
| C5 | Generator-homotopy promotion; tree and whisker contractibility (I23/I24) | N2 | – | 0.7 | yes |
| C6 | Lean `ExpansionContraction` invariant (I33) | N2 (template cap) | – | 0.7 | yes |
| C7 | Cutoff reflector R_q in free order (I15) | N2 | – | 0.65 | yes |
| C8 | Partial path functor: interpretation from contractibility (I28/I34) | N1 (↓ from N2) | – | 0.6 | yes |
| C9 | Endpoint-section retract argument (I29) | N1 | – | 0.75 | yes |
| C10 | Spines T_m(S) (I17) | N1 | – | 0.7 | yes |

**Changes from the family pass:**
- The analyst's two provisional N3s (I25 and I27) are merged into a single scheme-level N3 (C1), so the same idea is not counted twice. Alone, each is N2.
- I28 is lowered to N1. Its mechanism, that a contractible coglobular object carries the coherator structure, is in L (Bourke 2016 Thm 5.1; Ara 2013 §2.9; Lumsdaine and van den Berg–Garner in type theory).

## C1 in detail
- **Test 1 (no near-equivalent).** No equivalent was found, at snippet level, in searches A–K (listed in the JSON). Nearest neighbours:
  - **Lanari 2020** (1805.00156): full coglobular cylinders, with compositions, identities and inverses only. Its open step is interpreting all higher operations. *Close variant of the object; different in the bootstrap.*
  - **Lanari 2018** (1809.07923): in dimension 3, "an endofunctor that behaves like a path object". The abstract places the obstruction in arbitrary dimension in building "(slightly less than) a path object". *This is the largest unread risk.*
  - **Henry 2016:** cylinder coherators put the cylinders into the theory by fiat, and §4.3 gives path objects for bifibrant objects. *Genuinely different.*
  - **Henry–Lanari 2023 §2:** coskeletal models. *Ingredient only (the cutoff).*
  - **Taylor 2609.20860:** cylinder objects isomorphic to Lanari's. *Not checked beyond the abstract.*
  - **2604.09867:** ascending transfer. *Opposite order.*
  - **Cross-field neighbours:**
    - homotopy relative to the boundary, i.e. stationary cylinders;
    - Métayer and Lafont–Métayer–Worytkiewicz cylinders, and the Ara–Métayer strict model structures;
    - Nikolaus's algebraic Kan complexes;
    - the type-theory route through Bourke, Lumsdaine and van den Berg–Garner.

    These are all templates, not the bootstrap.
- **Test 2 (non-analytic): pass, partially.** The generic route "path object ⇒ pushout lemma" is in L (Henry, Lanari), so that component is analytic. Three things are not in L: cylinders that are partial in the expansion index (stationary below n, a single joining cell at n), contractibility supplied by the theorem's own higher-index cases, and the descending order from a cutoff. Syntactic size is irrelevant: P_j is trivial for j ≤ n.
- **Test 3 (load-bearing): pass.** `cylinderPathData` has dominated share 0.648 of the 856-declaration proof DAG. The text-level chain is `elementary_expansion` → `cutoff_elementary_exactBoundaryTest` → `cylinderPathData … (expansionContraction_all hC q (n+1))` (CutoffExpansion.lean:79, :99) → `cylinder_oneSided_contractible` (hypothesis `ExpansionContraction hC q (n+1)`).
- **Test 4 (discoverability): not run.** Protocol P-C1 is below. Estimated pivot distance is about 2 from L; chain depth is 2.
- **Templated-strengthening cap.** The descending order and the extra parameter q (C3), and the Lean weakening (C6), are templates and are capped at N2. C1 is not capped. Its new content is an *auxiliary object* (F3) whose contractibility is exactly what the reversed induction supplies (F2). The cap would apply if a reviewer judged the whole scheme to be just "make the IH self-feeding".
- **Shape.** C1 resembles Cook's device: cheap objects, P_j trivial below n, that open an obstruction stated since 2016/2018. No reuse outside its own theorem is known yet.

## family_D
- **D3, provisional, confidence 0.45** (was 0.35; downgrade route (a) checked and not triggered on 2026-10-12). It rests on C1 alone.
- **It falls to D2 if any of the following holds:**
  - the full text of Lanari 2018, Taylor 2609.20860, Henry 2016 §4 or Henry–Lanari 2023 already has a path object that is partial in the working dimension, with fillers drawn from higher dimensions;
  - Test 4 shows easy rediscovery once Lanari's obstruction is stated;
  - an expert calls the scheme standard "downward from a truncation" practice;
  - the scheme is judged a templated IH strengthening in substance.
- **Speedup test.** Corollaries do not count: Cor 5.1/5.2, coherator independence, and Taylor Thm 5.8 in the Ara–Henry convention. Real reuse targets:
  - the pushout lemma for Grothendieck n-groupoids;
  - coherators outside the arity-height convention (Maltsiniotis);
  - Taylor's controlled theories;
  - Grothendieck–Maltsiniotis (∞,n)-categories.

  Family 317's strict setting serves as a negative or analogue control.

## bridge_novelty
Every import is a **known route**; there is no new bridge:
- homotopical algebra applied to algebraic groupoid models (Ara, Henry, Lanari, Nikolaus);
- the contractible-coglobular interpretation from type theory (Bourke 2016, cited);
- coskeletal truncation (Henry–Lanari 2023);
- relative and stationary cylinders (classical; Métayer).

The cross-field count is 1.

## Discoverability protocol P-C1 (not run)
- **Hide:**
  - every part of the paper from Lemma 3.1 onward: the cutoff, E(q,n), trees, whiskers and all of §4;
  - the Lean files downstream of the basics (Expansion, CutoffExpansion, Cylinder\*, Whisker\*, Tree, Spines, Reflection).
- **Keep:** the theorem and the preliminaries (the W-test).
- **Arms:**
  - **A (open):** problem plus L.
  - **B (directed):** adds the path-object reduction, Lanari's stated obstruction and R_q as a given.
  - **C:** uncontrolled post-release models, as an upper reference.
- **Full hit** requires all three of:
  - (a) a path object tailored to the expansion dimension n, trivial or stationary below it;
  - (b) its higher fillers or contractibility obtained from the higher-dimensional cases;
  - (c) induction downward from a cutoff with a trivial top case.

  Partial levels are recorded but not counted. An ascending n → n+1 strategy is a miss.
- **Sampling:** n = 256 samples per arm, temperature 1.0, k ∈ {1, 2, 4, …, 256}.
- **Judges:** two LLM judges plus a higher-category-theory expert.
- **Models:** training cutoff before **2026-09-08** (Taylor 2609.20860), with no tools.
  - Excluded: OpenAI's release model and its successors; the openai/math release (312, 317); 2609.20860; post-release indices and blogs.
  - Canary probes: whether the conjecture is reported as solved; the phrase "partial cylinders, stationary below the working dimension"; recognition of `cylinderPathData`.

## Open questions (top)
1. Read Taylor 2609.20860 and Lanari 1809.07923 (v2024) in full. These decide whether C1 stays N3.
2. Check the AI-disclosure fields of 2607.28540, 2609.20860, 2604.09867 and 2510.22326 once arXiv is reachable.
3. Is the stationary cylinder in 317 a reuse of C1, or classical homotopy rel A? This feeds PLAN's device-reuse tally.
4. Re-extract the Lean DAG with the `theorem foo.{v}` fix, and construct an `IsCoherator` instance before running any downstream Lean experiment, so that the experiment does not test a vacuous statement.
