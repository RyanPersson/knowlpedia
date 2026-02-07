---
title: "Orthonormal frame bundle"
description: "Principal O(n) subbundle of the frame bundle determined by a Riemannian metric."
---

Let $(M,g)$ be an $n$-dimensional Riemannian manifold. The Riemannian metric gives an inner product $g_x$ on each tangent space $T_xM$.

The **orthonormal frame bundle** $O(TM)\to M$ is the subset of the {{< knowl id="frame-bundle-fr-of-a-manifold-m" text="frame bundle" >}} consisting of frames that are orthonormal with respect to $g$:
\[
O(TM)=\{(x,(e_1,\dots,e_n))\in \mathrm{Fr}(TM): g_x(e_i,e_j)=\delta_{ij}\}.
\]
The structure group is the orthogonal group $\mathrm{O}(n)$ (a {{< knowl id="lie-group" text="Lie group" >}}), acting on the right by change of orthonormal basis.

With this action, $O(TM)\to M$ is a principal $\mathrm{O}(n)$-bundle and is a reduction of $\mathrm{Fr}(TM)\to M$ from $\mathrm{GL}(n)$ to $\mathrm{O}(n)$; this reduction is the basic example in {{< knowl id="example-reduction-of-gl-structure-to-o-using-a-bundle-metric" text="reducing structure group using a bundle metric" >}}.

## Examples
1. **Euclidean space.**  
   On $M=\mathbb R^n$ with the standard metric, $O(T\mathbb R^n)\cong \mathbb R^n\times \mathrm{O}(n)$ via the constant orthonormal frame.

2. **Oriented Riemannian manifolds.**  
   If $M$ is oriented, the orthonormal frame bundle has a natural reduction to the connected subgroup $\mathrm{SO}(n)$ by restricting to oriented orthonormal frames.

3. **Round 2-sphere.**  
   For $S^2$ with the round metric, the oriented orthonormal frame bundle can be identified with $\mathrm{SO}(3)$: an oriented orthonormal tangent frame at $x\in S^2\subset\mathbb R^3$ uniquely extends to an oriented orthonormal frame of $\mathbb R^3$ by adding the outward unit normal.
