---
title: "Smooth chart (coordinate chart)"
description: "A homeomorphism from an open subset of a manifold to an open subset of Euclidean space, providing local coordinates."
---

Let $M$ be an $n$-dimensional topological manifold (in particular, any {{< knowl id="smooth-manifold" text="smooth manifold" >}} has such an underlying space). A **chart** (or **coordinate chart**) on $M$ is a pair $(U,\varphi)$ where

- $U\subset M$ is open, and
- $\varphi:U\to \varphi(U)\subset \mathbb{R}^n$ is a homeomorphism onto an open subset of $\mathbb{R}^n$.

The component functions of $\varphi$ are the **local coordinates** on $U$: writing $\varphi(p)=(x^1(p),\dots,x^n(p))$ defines coordinate functions $x^i:U\to\mathbb{R}$.

Given two charts $(U,\varphi)$ and $(V,\psi)$ with $U\cap V\neq\varnothing$, the **transition map** is the map $\psi\circ\varphi^{-1}$ from $\varphi(U\cap V)$ to $\psi(U\cap V)$. A collection of charts forms a {{< knowl id="smooth-atlas" text="smooth atlas" >}} precisely when all such transition maps are smooth in the usual multivariable sense.

## Examples
1. On $\mathbb{R}^n$, the pair $(\mathbb{R}^n,\mathrm{id})$ is a global chart; restricting $\mathrm{id}$ to any open set $U\subset\mathbb{R}^n$ gives a chart $(U,\mathrm{id}|_U)$.
2. On the sphere $S^n$, stereographic projection from the north pole gives a chart $(S^n\setminus\{N\},\sigma_N)$ with image $\mathbb{R}^n$; stereographic projection from the south pole gives a second chart that overlaps smoothly with the first, generating a smooth structure (see {{< knowl id="smooth-manifold" text="smooth manifold" >}}).
3. On the circle $S^1\subset\mathbb{R}^2$, stereographic projection from a point $p\in S^1$ gives a chart $(S^1\setminus\{p\},\sigma_p)$ with image $\mathbb{R}$, exhibiting $S^1$ as a $1$-dimensional smooth manifold.
