+++
id = "fiber-bundles/smooth-map"
title = "Smooth map"
kind = "knowl"
summary = "A map between smooth manifolds that becomes an ordinary smooth function in local coordinates."
aliases = ["smooth-map", "Smooth map"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/smooth-map.md"
+++

Let $M$ and $N$ be [[fiber-bundles/smooth-manifold|smooth manifolds]] of dimensions $m$ and $n$. A function $f:M\to N$ is **smooth** (or $C^\infty$) if for every $p\in M$ there exist [[fiber-bundles/smooth-chart-coordinate-chart|charts]] $(U,\varphi)$ on $M$ with $p\in U$ and $(V,\psi)$ on $N$ with $f(U)\subset V$ such that the coordinate expression
$\psi\circ f\circ \varphi^{-1}:\varphi(U)\to \psi(V)$
is a smooth map between open subsets of $\mathbb{R}^m$ and $\mathbb{R}^n$ in the usual multivariable sense.

Because the transition maps in a [[fiber-bundles/smooth-atlas|smooth atlas]] are smooth, this definition is independent of the particular charts chosen: if it holds for one pair of charts around $p$ and $f(p)$, then it holds for any other such pair. Smooth maps are closed under composition, and the identity map on any smooth manifold is smooth.

A smooth map has a well-defined [[fiber-bundles/differential-pushforward-of-a-smooth-map|differential (pushforward) on tangent spaces]] at each point; dually, it induces the [[fiber-bundles/pullback-of-covectors|pullback of covectors]] and the [[fiber-bundles/pullback-of-differential-forms|pullback of differential forms]].

## Examples
1. Any ordinary $C^\infty$ function $F:U\subset\mathbb{R}^m\to\mathbb{R}^n$ is a smooth map when $U$ is regarded as an open submanifold of $\mathbb{R}^m$ with its standard smooth structure.
2. If $M$ and $N$ are smooth manifolds, the projection $\pi_M:M\times N\to M$ is smooth; in product coordinates it is just $(x,y)\mapsto x$.
3. The inclusion $i:S^n\hookrightarrow \mathbb{R}^{n+1}$ is smooth; in fact it is a [[fiber-bundles/smooth-embedding|smooth embedding]].
