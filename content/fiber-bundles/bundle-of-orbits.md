---
title: "Bundle of orbits"
description: "The quotient of a product P × F by the diagonal action of the structure group, yielding the associated bundle."
---

Let $\pi:P\to M$ be a principal bundle with {{< knowl id="right-principal-action" text="right principal action" >}} of the {{< knowl id="lie-group" text="Lie group" >}} $G$, and let $F$ be a smooth left $G$-space.

The **bundle of orbits** associated to $(P,F)$ is the orbit space
\[
(P\times F)/G
\]
for the right $G$-action on $P\times F$ defined by
\[
(p,f)\cdot g := (p\cdot g,\; g^{-1}\cdot f).
\]
When this action is free and proper (as it is in the principal-bundle setting with smooth $F$), the orbit space is a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and the natural projection
\[
[(p,f)] \longmapsto \pi(p)
\]
makes it a smooth fiber bundle over $M$. This orbit bundle is canonically identified with the {{< knowl id="associated-bundle" text="associated bundle" >}} $P\times_G F$ defined via the equivalent relation $(p\cdot g,f)\sim(p,g\cdot f)$.

## Examples
1. **Fiber a point.** If $F=\{\ast\}$ with the trivial action, then $(P\times F)/G \cong P/G \cong M$.
2. **Trivial principal bundle.** If $P=M\times G$, then $(P\times F)/G \cong M\times F$ by sending the orbit of $(x,h,f)$ to $(x,h\cdot f)$.
3. **Recovering P.** If $F=G$ with left multiplication, then $(P\times G)/G \cong P$ via $[(p,h)]\mapsto p\cdot h$.
