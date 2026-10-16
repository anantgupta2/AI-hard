# Proposal: a p-divisible Witt fundamental class of the orbit space ("sheet-divisibility lemma")

**Idea in one line.** Use the averaged test map `a: Y -> S^d` to push a *Witt-group fundamental class* of `Y` to `E_d(S^d)`. Degree one forces the image to be `u_d`. The finite-sheet structure over `V` forces the same image to be divisible by `p^k` for every `k`. For large `k`, the fixed lattice `L_d^{-1} Z u_d` cannot hold both facts. This is a homological "Newman/Smith" argument done in Witt groups. Witt groups see signatures, not mod-p homology, so they survive the infinite-dimensional (dim `n+2`) quotient.

## Construction (Witt fundamental class)
Take a closed `d`-ball `D` inside a chart of `W`, with `D` small enough that Tool 4 applies (`a∘q|_D` has degree 1 rel `∂D`). Because `q|_D : D -> Y` is a map from a compact polyhedron, `q_* R_D[d]` lies in `T(Y)`. The Poincaré–Verdier duality `R_D[d] ≅ D(R_D)[-d]` (rel `∂D`) pushes forward along the proper map `q|_D`. It gives a `d`-symmetric form in the Verdier quotient `T(Y)/T(q(∂D))`. Use Tool 3, with a contractible neighbourhood `U` of the basepoint chosen so that `a(Y \ q(int D))` is near it after the pinch. This lifts the form to

  `ω_D ∈ E_d(Y)`, with `a_* ω_D = u_d` (Tool 4 plus naturality of `E_d` under proper maps).

## Key lemma (sheet divisibility)
Fix `k`, and take `V ⊂ Y` from Tool 5 with `π_k : W/p^kG -> Y` a trivial `p^k`-sheeted cover over `V`. Suppose `D ⊂ q^{-1}(V)`. Then in `E_d(Y)`:

  `ω_D = p^k · ω_D^{(k)}`,

where `ω_D^{(k)} = (s_j)_* (q^k|_D)_* [D]` is the class of `D` pushed into a single sheet `s_j` (for any one `j`).

*Proof sketch.* Over `V`, `q = π_k ∘ q^k`. The image `q^k(D)` lies in `π_k^{-1}V = ⊔_{j ∈ Z/p^k} V_j`. The sheets are disjoint, so the symmetric object `(q^k)_*R_D` splits orthogonally as `⊕_j F_j`, with `F_j` supported on `V_j`, and its Witt class is `Σ_j [F_j]`.

The multiplier `β` satisfies `β(gw) = ζ^g β(w)`, so translation by `g ∈ G` permutes the sheets transitively, `V_j -> V_{j+g}`. Since `D` meets every `G`-orbit in `q^{-1}V` in the same pattern, `F_{j+g} ≅ g_* F_j`, and this is an isometry. `π_k ∘ g = π_k`, so `(π_k)_*[F_j]` does not depend on `j`. Summing gives `ω_D = p^k (π_k)_*[F_0]`. ∎

## Contradiction with faithfulness
1. **Localize the degree to `V`.** Apply Tool 6 to `V_1` (from Tool 5 with `k = 1`) once: `N·a ≃ h` with `h` constant off `V_1`, and `N` is now fixed. By homotopy invariance, `h_* ω_D = N u_d` for every admissible `D`. Applying Tool 5 to the invariant open set `q^{-1}(V_1)` in place of `W` gives nested `V_k ⊂ V_1`. Because `h` is constant off `V_1` and `E_d` is covariant for proper maps of the one-point compactification, the ball `D` can be slid into `q^{-1}(V_k)` without changing `h_* ω_D`. The local degree of `h∘q` is constant along the connected region `q^{-1}V_1`, and `W` is connected after stabilization.
2. **Divide.** By the key lemma, `N u_d = h_* ω_D = p^k · h_* ω_D^{(k)} ∈ p^k L_d^{-1} Z u_d` (Tool 2). So `N ∈ p^k 2^{-e_d} Z` for all `k`.
3. **Conclude.** If `p` is odd, `p^k | N` for all `k`, which forces `N = 0`. That contradicts `N > 0`. If `p = 2`, `2^{k - e_d} | N` for all `k`, which is again impossible. So no faithful action exists. Faithfulness enters through Tool 4: on a faithful action, the shrunken subgroup `H` is still nontrivial and the sheets are genuinely `p^k` in number for every `k` (Newman/Yang). Without faithfulness the sheet count stabilizes and step 3 fails.

## Why this is the right invariant
- Mod-p Smith theory dies because `Y` has dimension `n+2`. The Witt class is a *rational, signature-type* invariant of a self-dual sheaf. Its denominators are 2-primary (Tool 2), so `p`-adic divisibility is the only thing it cannot absorb.
- The `d`-odd stabilization makes Tool 3 work integrally. Without it, the localization would lose the `N` bookkeeping.

## Gaps to check
- In step 1, `h_* ω_D` must be independent of the position of `D` inside `q^{-1}V_1`. This is a constancy-of-local-degree statement for `h∘q`. It needs `E_d` homotopy invariance applied to an isotopy of `D` (a compact family, so the objects stay in `T`).
- The isometry `F_{j+g} ≅ g_* F_j` needs `D` to be chosen `p^kG`-saturated. The fix is to replace `D` by its `p^kG`-orbit (Haar-averaged, as in Tool 4) and renormalize.
