---
title: "Bundle metric"
description: "A smoothly varying inner product on the fibers of a real vector bundle."
---

Let $\pi:E\to M$ be a smooth real vector bundle over a {{< knowl id="smooth-manifold" text="smooth manifold" >}}. A **bundle metric** on $E$ is an assignment of an inner product
\[
\langle\cdot,\cdot\rangle_x : E_x\times E_x\to \mathbb R
\]
for each $x\in M$ such that:

- Each $\langle\cdot,\cdot\rangle_x$ is a positive-definite symmetric bilinear form on the real vector space $E_x$.
- For any smooth local sections $s,t:U\to E$ (defined on an open set $U\subseteq M$), the function
  \[
  U\to\mathbb R,\qquad x\mapsto \langle s(x),t(x)\rangle_x
  \]
  is smooth.

Equivalently, in any local frame $(e_1,\dots,e_r)$ over $U$, the matrix-valued function $G=(G_{ij})$ with
\[
G_{ij}(x)=\langle e_i(x),e_j(x)\rangle_x
\]
is a smooth map $U\to \mathrm{Sym}^+(r,\mathbb R)$ (positive-definite symmetric matrices), and transforms under changes of frame by the usual congruence rule.

A bundle metric is the same as a reduction of the {{< knowl id="frame-bundle-frame-bundle-of-a-rank-n-vector-bundle" text="frame bundle" >}} from the general linear group to the orthogonal group, yielding the {{< knowl id="orthonormal-frame-bundle-reduction-of-the-frame-bundle" text="orthonormal frame bundle" >}}.

## Examples
1. **Riemannian metric.** A Riemannian metric on $M$ is precisely a bundle metric on the {{< knowl id="tangent-bundle" text="tangent bundle" >}} $TM$.

2. **Standard metric on a trivial bundle.** On $E=M\times\mathbb R^r$, the standard Euclidean inner product on $\mathbb R^r$ defines a bundle metric with constant matrix $I_r$ in the standard frame.

3. **Induced metrics.** A bundle metric on $E$ induces canonical bundle metrics on $E^*$, on $E\oplus F$, and on tensor and exterior powers (e.g. on $\Lambda^kE$) by the standard linear-algebraic constructions performed fiberwise.
