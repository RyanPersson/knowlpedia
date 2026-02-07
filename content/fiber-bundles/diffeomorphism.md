---
title: "Diffeomorphism"
description: "A bijective smooth map with smooth inverse; an isomorphism of smooth manifolds."
---

Let $M$ and $N$ be {{< knowl id="smooth-manifold" text="smooth manifolds" >}}. A map $f:M\to N$ is a **diffeomorphism** if

1. $f$ is bijective,
2. $f$ is a {{< knowl id="smooth-map" text="smooth map" >}}, and
3. the inverse function $f^{-1}:N\to M$ is also smooth.

Equivalently, $f$ is a smooth bijection whose inverse is smooth. Any diffeomorphism is, in particular, a homeomorphism of the underlying topological spaces, and it identifies the smooth structures on $M$ and $N$.

If $f$ is a diffeomorphism, then for each $p\in M$ its {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential" >}} $\mathrm{d}f_p$ is a linear isomorphism $T_pM\to T_{f(p)}N$, where $T_pM$ denotes the {{< knowl id="tangent-space-at-a-point" text="tangent space" >}}.

## Examples
1. On $\mathbb{R}^n$, any translation $x\mapsto x+a$ and any invertible linear map $x\mapsto Ax$ (with $A\in \mathrm{GL}(n,\mathbb{R})$) is a diffeomorphism.
2. The logarithm map $\log:(0,\infty)\to\mathbb{R}$ is a diffeomorphism of $1$-manifolds with inverse $\exp:\mathbb{R}\to(0,\infty)$.
3. Stereographic projection gives a diffeomorphism between $S^n\setminus\{N\}$ and $\mathbb{R}^n$, showing that punctured spheres are smoothly equivalent to Euclidean space.
