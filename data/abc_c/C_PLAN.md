# Proof type on two axes (replaces axis C)

Axis C mixed the logical shape of a proof with what its steps are made of. It is replaced by two independent axes,
labelled for the proof of the family's **headline theorem**, read at the top level (the backbone the paper itself
describes, not every lemma).

## C.form — the logical shape of the headline proof (one primary, any number of secondaries)
| Code | Form | Includes |
|---|---|---|
| F1 | Direct derivation | forward chain of implications, identities or inequalities from the hypotheses; a reduction "X implies Y" proved directly |
| F2 | Contradiction / contrapositive | "suppose not", minimal counterexample, assume a faithful action / a counterexample and derive absurdity |
| F3 | Induction / recursion / iteration | induction on a parameter or on structure, transfinite induction, descent, bootstrapping, iterative or multiscale schemes with a convergence or stopping argument |
| F4 | Explicit construction | exhibits a specific object (counterexample, witness, algorithm, example) and verifies its properties |
| F5 | Non-constructive existence | proves something exists without exhibiting it: probabilistic method, compactness or limiting arguments, fixed-point theorems, pigeonhole, Baire category, counting |
| F6 | Exhaustion / case analysis | a finite split into cases is the backbone, including computer enumeration, SAT/ILP certificates, certified numerics |

## C.engine — what the steps are made of (one primary, any number of secondaries)
| Code | Engine | Includes |
|---|---|---|
| E1 | Estimates and inequalities | analytic bounds, a priori and energy estimates, concentration, asymptotics, entropy and information inequalities |
| E2 | Exact algebraic computation | identities, explicit formulas, generating functions, character or representation computations, explicit matrices |
| E3 | Combinatorial structure and counting | graphs, extremal and counting arguments, discrete structures, words and partitions |
| E4 | Structural / categorical / cohomological | homological algebra, sheaves, derived categories, K- and L-theory, moduli and functoriality, model theory |
| E5 | Geometric / topological | geometric constructions, surgery and handle moves, curvature comparison, dynamics on spaces, topology of maps |
| E6 | Assembly of cited results | the proof mainly combines major external theorems with little new machinery of its own |
| E7 | Computation | computer search or verification does essential work |

## Tie-break rules
1. Label the backbone of the headline proof as the paper describes it ("the proof proceeds by…", the section outline). Lemmas inside it are secondaries.
2. An explicit counterexample or algorithm is F4 even if its verification argues by contradiction (F2 secondary).
3. Existence via a random or limiting object that is never written down is F5, even if the probability estimates are long (E1 engine).
4. A theorem proved by "assume the object exists, derive a contradiction" is F2, even when the contradiction comes from a long estimate (E1) or an induction (F3 secondary).
5. An iterative scheme (multiscale, bootstrap, recursive construction) whose iteration is the organizing idea is F3; if it builds a specific object, F4 primary with F3 secondary only when the paper presents the object first.
6. Conditional hardness or "A implies B" reductions are F1 unless the paper frames them as contradiction.
7. E6 only when most of the argument is invoking big cited theorems; otherwise label the engine of the new part and put E6 as secondary.
8. A classification into finitely many cases is F6 only if the case split is the backbone; a classification by induction on dimension is F3.
9. Computer-assisted (flag) only when computation does real search or certified verification, not a trivial check.
10. When the headline is a bundle of results, label the principal one (the same one the v2 headline sentence describes).

## Output record
`fid, form, form_secondary[], engine, engine_secondary[], computer_assisted, backbone (≤ 30 words: the top-level argument), quote (≤ 40 words verbatim from the input supporting the form), conf {form, engine}`
