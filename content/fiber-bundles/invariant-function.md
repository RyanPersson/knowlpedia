---
title: "Invariant function"
description: "A smooth function constant along the orbits of a Lie group action."
---

Let $G$ act smoothly on a manifold $M$.

A smooth function $f:M\to \mathbb{R}$ is **$G$-invariant** if
\[
f(g\cdot x)=f(x)\qquad\text{for all }g\in G,\ x\in M.
\]
Equivalently, $f$ is constant on each {{< knowl id="orbit-of-a-group-action" text="orbit" >}}. In that case, $f$ factors uniquely through the quotient map $\pi:M\to $ as a function $\bar f:M/G\to \mathbb{R}$ with $f=\bar f\circ \pi$.

## Examples
1. **Radial functions.** For the $SO(n)$-action on $\mathbb{R}^n$, the norm $x\mapsto \|x\|$ and any function of $\|x\|$ are invariant.
2. **Pullbacks from a quotient.** If $\pi:P\to B$ is a principal bundle, then any smooth $h:B\to\mathbb{R}$ gives an invariant function $h\circ \pi$ on $P$.
3. **Transitive actions.** If the action is transitive (one orbit), for instance $\mathbb{R}^n$ acting on itself by translations, then every invariant smooth function is constant.
