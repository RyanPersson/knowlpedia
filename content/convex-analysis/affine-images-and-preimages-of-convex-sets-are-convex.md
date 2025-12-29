---
title: "Affine images and preimages of convex sets are convex"
description: "Affine maps preserve convexity under both images and inverse images"
---

**Proposition.**
Let $B:X\to Y$ be an {{< knowl id="affine-mapping" text="affine mapping" >}}.

1. If $\Omega\subset X$ is {{< knowl id="convex-set" text="convex" >}}, then $B(\Omega)\subset Y$ is convex.
2. If $\Theta\subset Y$ is convex, then the preimage $B^{-1}(\Theta)=\{x\in X:B(x)\in\Theta\}$ is convex in $X$.

**Context.** This is the main mechanism for generating new convex sets from old ones: apply an affine change of coordinates, or pull back convex constraints.

**Proof sketch.** For (1), take $u=B(x)$ and $v=B(y)$ with $x,y\in\Omega$ and use the defining identity for affine maps:
$$
\lambda u+(1-\lambda)v = B(\lambda x+(1-\lambda)y)\in B(\Omega).
$$
For (2), if $x,y\in B^{-1}(\Theta)$ then $B(x),B(y)\in\Theta$, and convexity of $\Theta$ plus the same identity gives $B(\lambda x+(1-\lambda)y)\in\Theta$.
