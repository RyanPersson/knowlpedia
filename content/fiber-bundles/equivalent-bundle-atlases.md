---
title: "Equivalent bundle atlases"
description: "Two atlases are equivalent if they define the same smooth bundle structure via compatible trivialisations."
---

Let \(\pi:E\to M\) be a smooth fiber bundle with typical fiber \(F\). Two {{< knowl id="bundle-atlas" text="bundle atlases" >}} \(\mathcal A\) and \(\mathcal B\) for \(\pi\) are **equivalent** if their union \(\mathcal A\cup \mathcal B\) is again a bundle atlas; equivalently, every local trivialization from \(\mathcal A\) is compatible with every local trivialization from \(\mathcal B\) in the sense that the induced changes of trivialization on overlaps are smooth and fiberwise diffeomorphisms.

A common rephrasing is that \(\mathcal A\) and \(\mathcal B\) admit a common refinement: there exists a third atlas \(\mathcal C\) such that each chart of \(\mathcal C\) is a restriction of a chart from \(\mathcal A\) and also of a chart from \(\mathcal B\). In this way, a smooth fiber bundle structure can be viewed as an equivalence class of atlases.

On overlaps between a chart from \(\mathcal A\) and a chart from \(\mathcal B\), the compatibility is expressed by smooth {{< knowl id="transition-function" text="transition functions" >}} taking values in \(\mathrm{Diff}(F)\).

## Examples
1. **Refinement by shrinking:** if \(\{(U_i,\Phi_i)\}\) is an atlas and \(V_i\subset U_i\) is an open cover, then \(\{(V_i,\Phi_i|_{\pi^{-1}(V_i)})\}\) is an equivalent atlas.
2. **Different gauges on a trivial bundle:** on \(M\times F\), changing trivializations by \((x,f)\mapsto(x,h(x)(f))\) for a smooth \(h:M\to \mathrm{Diff}(F)\) yields an equivalent atlas.
3. **Tangent bundle:** atlases for \(TM\) coming from different smooth atlases of \(M\) are equivalent because coordinate changes on \(M\) induce smooth fiberwise linear transition maps on \(TM\).
