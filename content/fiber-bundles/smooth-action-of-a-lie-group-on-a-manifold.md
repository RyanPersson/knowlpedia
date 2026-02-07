---
title: "Smooth action of a Lie group on a manifold"
description: "A smooth map defining a group action of a Lie group on a smooth manifold."
---

Let {{< knowl id="lie-group" text="Lie group" >}} $G$ and {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$ be given.

A **smooth left action** of $G$ on $M$ is a {{< knowl id="smooth-map" text="smooth map" >}}
\[
\Phi: G\times M \longrightarrow M
\]
such that, writing $g\cdot x:=\Phi(g,x)$, the following hold for all $g,h\in G$ and $x\in M$:

1. (**Identity**) $e\cdot x = x$.
2. (**Compatibility**) $(gh)\cdot x = g\cdot(h\cdot x)$.

For each $g\in G$, the map $\Phi_g:M\to M$, $\Phi_g(x)=g\cdot x$, is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}} with inverse $\Phi_{g^{-1}}$.

A **smooth right action** is defined similarly, using a smooth map $M\times G\to M$, $(x,g)\mapsto x\cdot g$, with $x\cdot e=x$ and $(x\cdot g)\cdot h = x\cdot(gh)$.

## Examples
1. **Left translation on the group.** $G$ acts on itself by $g\cdot h := gh$.
2. **Rotations of the plane.** $SO(2)$ acts on $\mathbb{R}^2$ by matrix multiplication.
3. **Change of frame.** The general linear group $GL(n,\mathbb{R})$ acts on the frame bundle of a manifold by post-composition of frames (a standard example of a right action in principal bundle theory).
