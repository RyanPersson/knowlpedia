---
title: "Orbit map"
description: "The smooth map from a Lie group to a manifold sending a group element to its action on a fixed point."
---

Let $G$ act on $M$ by a {{< knowl id="smooth-action-of-a-lie-group-on-a-manifold" text="smooth action" >}}.

For $x\in M$, the **orbit map at $x$** is the {{< knowl id="smooth-map" text="smooth map" >}}
\[
\Phi^x: G \longrightarrow M,\qquad \Phi^x(g)=g\cdot x.
\]
Its image is the {{< knowl id="orbit-of-a-group-action" text="orbit" >}} $G\cdot x$.

The kernel of $\Phi^x$ (in the sense of elements acting trivially at $x$) is the {{< knowl id="stabilizer" text="stabilizer subgroup" section="algebra-groups">}} $G_x$. Consequently, $\Phi^x$ is constant on left cosets of $G_x$ and factors through the quotient $G/G_x$.

## Examples
1. **Left translation on $G$.** For the action of $G$ on itself by left multiplication and a fixed $h\in G$, the orbit map is $g\mapsto gh$.
2. **Rotations of a vector.** For $SO(2)\curvearrowright \mathbb{R}^2$ and $x\neq 0$, the orbit map parametrizes the circle of radius $\|x\|$.
3. **Conjugation.** For the conjugation action of $G$ on itself, the orbit map at $h$ is $g\mapsto ghg^{-1}$, whose image is the conjugacy class of $h$.
