---
title: "Euler class via Chern–Weil theory"
description: "The top-degree characteristic class of an oriented even-rank real vector bundle defined from curvature using the Pfaffian."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $\pi:E\to M$ be an oriented real vector bundle of rank $2m$. Choose a Euclidean metric on $E$ and a compatible {{< knowl id="connection-on-a-vector-bundle" text="connection" >}} $\nabla$ whose structure group is reduced to $SO(2m)$. Let $F_\nabla\in\Omega^2(M;\mathfrak{so}(E))$ be its {{< knowl id="curvature" text="curvature" >}}.

## Definition (Euler form and Euler class)
The **Pfaffian** $\mathrm{Pf}$ is an $Ad$-invariant polynomial of degree $m$ on $\mathfrak{so}(2m)$ characterized by $\mathrm{Pf}(A)^2=\det(A)$ for skew-symmetric matrices $A$. The **Euler form** of $\nabla$ is the closed $2m$-form
\[
e(\nabla)\;:=\;\mathrm{Pf}\!\Big(\frac{1}{2\pi}F_\nabla\Big)\in\Omega^{2m}(M).
\]
(Here $\mathrm{Pf}$ is applied fiberwise after choosing a local oriented orthonormal frame.)

Then:
1. $d\,e(\nabla)=0$, where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}}.
2. The de Rham class $[e(\nabla)]\in H^{2m}_{\mathrm{dR}}(M)$ is independent of the choice of metric-compatible oriented connection.
3. The **Euler class** $e(E)\in H^{2m}(M;\mathbb Z)$ is the unique integral class mapping to $[e(\nabla)]$ under the natural map to real (or de Rham) cohomology.

Naturality holds: for any {{< knowl id="smooth-map" text="smooth map" >}} $f:N\to M$,
\[
e(f^*E)=f^*e(E).
\]

## Examples
1. **Oriented rank-2 bundles.** If $\mathrm{rank}(E)=2$, then $F_\nabla$ is an $\mathfrak{so}(2)\cong\mathbb R$-valued 2-form. In an oriented orthonormal frame, $F_\nabla$ is represented by a scalar 2-form $\Omega$, and
   \[
   e(\nabla)=\frac{1}{2\pi}\Omega.
   \]
   In particular, the Euler class is represented by $\frac{1}{2\pi}\Omega$.

2. **Tangent bundle of an oriented closed surface.** For a closed oriented surface $\Sigma$, the Euler class of $T\Sigma$ satisfies
   \[
   \langle e(T\Sigma),[\Sigma]\rangle=\chi(\Sigma),
   \]
   and $e(\nabla)$ is the Gauss curvature form normalized by $2\pi$ for the Levi-Civita connection.

3. **Flat oriented bundles.** If $\nabla$ is flat ($F_\nabla=0$), then $e(\nabla)=0$, so $e(E)$ vanishes in real cohomology (and hence in rational cohomology).
