---
title: "Clutching function"
description: "A map on an overlap used to glue trivial bundles into a global bundle."
---

A **clutching function** is a transition map used to glue together locally trivial pieces of a bundle.

Let $M$ be covered by two open sets $U,V\subset M$ such that a bundle is trivial over each piece. For a principal bundle, take $U\times G$ and $V\times G$ and identify points over the overlap $U\cap V$ by
$$
(x,h)_U \sim (x, g(x)\,h)_V \qquad (x\in U\cap V,\; h\in G),
$$

where $g:U\cap V\to G$ is smooth. The map $g$ is the **clutching function**; it is exactly the {{< knowl id="transition-function" text="transition function" >}} (more precisely, a {{< knowl id="principal-bundle-transition-function" text="principal bundle transition function" >}}) for the cover $\{U,V\}$.

For a vector bundle with fiber $F$ and structure group $G\subset \mathrm{GL}(F)$, one instead glues $U\times F$ to $V\times F$ by
$$
(x,v)_U \sim (x, g(x)\cdot v)_V .
$$

If one uses more than two open sets, the clutching functions on overlaps must satisfy the {{< knowl id="cocycle-condition-for-transition-functions" text="cocycle condition" >}} on triple intersections; changing trivializations replaces $g$ by an {{< knowl id="equivalence-of-cocycles" text="equivalent cocycle" >}}.

### Sphere case
For $S^n = D^n_+\cup D^n_-$ (two hemispheres), the overlap deformation retracts to $S^{n-1}$. Thus, a clutching function can often be taken as a map
$$
g:S^{n-1}\to G,
$$
and many classification results reduce to the homotopy class of this map.

## Examples
1. **Möbius line bundle over $S^1$.** The Möbius bundle is obtained by gluing the ends of $[0,1]\times\mathbb R$ via $(0,v)\sim(1,-v)$. Interpreting this as a rank-1 real vector bundle over $S^1$, the clutching data is "$-1$" in $\mathrm{GL}_1(\mathbb R)$, producing a nontrivial bundle.

2. **Complex line bundles over $S^2$.** Using the hemisphere cover of $S^2$, a clutching function is a map $g:S^1\to U(1)$. The standard family
   $$
   g_k(e^{i\theta}) = e^{ik\theta}
   $$

   yields the complex line bundles with first {{< knowl id="chern-class" text="Chern class" >}} equal to $k$.

3. **The tangent bundle of $S^2$.** The nontriviality of $TS^2$ can be exhibited by a clutching description with structure group $SO(2)$, where the overlap map $S^1\to SO(2)$ has degree $2$.
