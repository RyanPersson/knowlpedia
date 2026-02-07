---
title: "Smooth chart"
description: "A local coordinate map from an open subset of a smooth manifold to an open subset of Euclidean space."
---

Let $M$ be an $n$-dimensional {{< knowl id="smooth-manifold" text="smooth manifold" >}}. A **(topological) chart** on $M$ is a pair $(U,\varphi)$ where $U\subset M$ is open and $\varphi:U\to V$ is a homeomorphism onto an open set $V\subset \mathbb{R}^n$.

A **smooth chart** (or **coordinate chart**) on $M$ is a chart $(U,\varphi)$ such that for every chart $(U',\varphi')$ belonging to the smooth structure of $M$, the **transition map**
\[
\varphi'\circ \varphi^{-1}:\varphi(U\cap U')\longrightarrow \varphi'(U\cap U')
\]
is smooth (as a map between open subsets of $\mathbb{R}^n$). Equivalently, $\varphi$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}} between the open submanifold $U$ (with the induced smooth structure) and the open set $V\subset \mathbb{R}^n$.

Given a smooth chart $(U,\varphi)$ with $\varphi=(x^1,\dots,x^n)$, the functions $x^i:U\to \mathbb{R}$ are called the **local coordinates** associated to the chart.

## Examples
1. **Euclidean space.** On $M=\mathbb{R}^n$, the pair $(\mathbb{R}^n,\mathrm{id})$ is a smooth chart. Any open set $U\subset\mathbb{R}^n$ with the inclusion $U\hookrightarrow\mathbb{R}^n$ gives a smooth chart $(U,\mathrm{id}_U)$.
2. **Stereographic charts on the sphere.** On $S^n\subset\mathbb{R}^{n+1}$, stereographic projection from the north pole defines a chart $(S^n\setminus\{N\},\sigma_N)$ with $\sigma_N:S^n\setminus\{N\}\to\mathbb{R}^n$ smooth; similarly from the south pole. The overlap transition map is smooth.
3. **Product charts.** If $(U,\varphi)$ is a chart on $M$ and $(W,\psi)$ is a chart on $N$, then $(U\times W,\varphi\times\psi)$ is a chart on $M\times N$, giving the standard product coordinate system.
