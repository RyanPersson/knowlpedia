---
title: "Orthonormal frame bundle"
description: "The principal O(n)-bundle of orthonormal frames determined by a bundle metric on a real rank-n bundle."
---

Let $\pi:E\to M$ be a real vector bundle of rank $n$ over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $\langle\cdot,\cdot\rangle$ be a {{< knowl id="bundle-metric" text="bundle metric" >}} on $E$. The **orthonormal frame bundle** of $(E,\langle\cdot,\cdot\rangle)$, denoted $\mathrm{O}(E)$, is the submanifold of the {{< knowl id="frame-bundle-frame-bundle-of-a-rank-n-vector-bundle" text="frame bundle" >}} consisting of frames that are orthonormal in each fiber:
\[
\mathrm{O}(E):=\{(e_1,\dots,e_n)\in \mathrm{Fr}(E)\ :\ \langle e_i,e_j\rangle = \delta_{ij}\ \text{fiberwise}\}.
\]

The right action of $\mathrm{GL}(n,\mathbb R)$ on $\mathrm{Fr}(E)$ restricts to a right action of the orthogonal group $\mathrm{O}(n)$ on $\mathrm{O}(E)$, and $(\mathrm{O}(E),p)$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $\mathrm{O}(n)$.

This construction realizes a reduction of structure group from $\mathrm{GL}(n,\mathbb R)$ to $\mathrm{O}(n)$ determined by the metric.

## Examples
1. **Riemannian orthonormal frames.** If $E=TM$ and the metric comes from a Riemannian metric on $M$, then $\mathrm{O}(TM)$ is the usual bundle of orthonormal tangent frames.

2. **Trivial bundle with Euclidean metric.** On $E=M\times\mathbb R^n$ with the standard inner product, $\mathrm{O}(E)\cong M\times \mathrm{O}(n)$.

3. **Rank-one case.** If $n=1$, then $\mathrm{O}(1)=\{\pm 1\}$ and $\mathrm{O}(E)$ is a double cover of $M$ (the bundle of unit vectors in each 1-dimensional fiber).
