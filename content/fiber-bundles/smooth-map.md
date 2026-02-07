---
title: "Smooth map"
description: "A map between smooth manifolds that becomes an ordinary smooth function in local coordinates."
---

Let $M$ and $N$ be {{< knowl id="smooth-manifold" text="smooth manifolds" >}} of dimensions $m$ and $n$. A function $f:M\to N$ is **smooth** (or $C^\infty$) if for every $p\in M$ there exist {{< knowl id="smooth-chart-coordinate-chart" text="charts" >}} $(U,\varphi)$ on $M$ with $p\in U$ and $(V,\psi)$ on $N$ with $f(U)\subset V$ such that the coordinate expression
$\psi\circ f\circ \varphi^{-1}:\varphi(U)\to \psi(V)$
is a smooth map between open subsets of $\mathbb{R}^m$ and $\mathbb{R}^n$ in the usual multivariable sense.

Because the transition maps in a {{< knowl id="smooth-atlas" text="smooth atlas" >}} are smooth, this definition is independent of the particular charts chosen: if it holds for one pair of charts around $p$ and $f(p)$, then it holds for any other such pair. Smooth maps are closed under composition, and the identity map on any smooth manifold is smooth.

A smooth map has a well-defined {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential (pushforward) on tangent spaces" >}} at each point; dually, it induces the {{< knowl id="pullback-of-covectors" text="pullback of covectors" >}} and the {{< knowl id="pullback-of-differential-forms" text="pullback of differential forms" >}}.

## Examples
1. Any ordinary $C^\infty$ function $F:U\subset\mathbb{R}^m\to\mathbb{R}^n$ is a smooth map when $U$ is regarded as an open submanifold of $\mathbb{R}^m$ with its standard smooth structure.
2. If $M$ and $N$ are smooth manifolds, the projection $\pi_M:M\times N\to M$ is smooth; in product coordinates it is just $(x,y)\mapsto x$.
3. The inclusion $i:S^n\hookrightarrow \mathbb{R}^{n+1}$ is smooth; in fact it is a {{< knowl id="smooth-embedding" text="smooth embedding" >}}.
