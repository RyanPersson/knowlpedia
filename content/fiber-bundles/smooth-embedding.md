---
title: "Smooth embedding"
description: "A smooth map that is an injective immersion and a homeomorphism onto its image."
---

Let $f:M\to N$ be a {{< knowl id="smooth-map" text="smooth map" >}} between {{< knowl id="smooth-manifold" text="smooth manifolds" >}}. The map $f$ is a **smooth embedding** if

1. $f$ is a {{< knowl id="smooth-immersion" text="smooth immersion" >}} (equivalently, $\mathrm{d}f_p:T_pM\to T_{f(p)}N$ is injective for all $p\in M$), and
2. $f$ is a topological embedding: it is a homeomorphism from $M$ onto the subset $f(M)\subset N$ equipped with the subspace topology.

In this case $f$ identifies $M$ with an embedded submanifold of $N$: there is a unique smooth structure on $f(M)$ for which $f:M\to f(M)$ becomes a {{< knowl id="diffeomorphism" text="diffeomorphism" >}} and the inclusion $f(M)\hookrightarrow N$ is smooth.

A common pitfall is that an injective immersion need not be an embedding: for example, the map $t\mapsto (e^{it},e^{i\alpha t})$ from $\mathbb{R}$ to the torus $S^1\times S^1$ is an injective immersion when $\alpha$ is irrational, but its image is dense and the inverse to $\mathbb{R}$ is not continuous, so it fails condition (2).

## Examples
1. The standard inclusion $S^n\hookrightarrow \mathbb{R}^{n+1}$ is a smooth embedding; its image is the usual round sphere as an embedded hypersurface.
2. If $U\subset M$ is open, the inclusion $U\hookrightarrow M$ is a smooth embedding (in fact a diffeomorphism onto the open submanifold $U$ with the induced smooth structure).
3. For any smooth map $g:M\to N$, the graph map $\Gamma_g:M\to M\times N$ defined by $p\mapsto (p,g(p))$ is a smooth embedding; it realizes the graph of $g$ as an embedded submanifold of the product.
