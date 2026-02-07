---
title: "Holonomy element from parallel transport around a loop"
description: "Definition of the holonomy element in G obtained by transporting a point around a based loop."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with {{< knowl id="principal-connection" text="principal connection" >}} $\omega$. Fix a basepoint $x\in M$ and a point $p\in P_x$. Let $\gamma:[0,1]\to M$ be a loop based at $x$, meaning $\gamma(0)=\gamma(1)=x$.

Using {{< knowl id="construction-parallel-transport-map-along-a-curve" text="parallel transport" >}}, $p$ is carried to another point in the same fiber:
\[
\mathrm{PT}^\omega_\gamma(p)\in P_x.
\]
Because $P_x$ is a right $G$-torsor, there is a unique element $h_\gamma(p)\in G$ such that
\[
\mathrm{PT}^\omega_\gamma(p)=p\cdot h_\gamma(p).
\]
This element is the **holonomy element** of $\omega$ along $\gamma$ based at $p$.

Changing the basepoint in the fiber conjugates the element: if $p'=p\cdot g$, then
\[
h_\gamma(p') = g^{-1}\,h_\gamma(p)\,g.
\]
Thus the subgroup $\{h_\gamma(p)\}$ depends on $p$, but its conjugacy class depends only on $x$ and defines the {{< knowl id="holonomy-group" text="holonomy group" >}} at $x$.

## Examples
1. If $\omega$ is flat and $M$ is simply connected, then $h_\gamma(p)=e$ for all loops, so the holonomy group is trivial.
2. On the Levi-Civita connection of the round 2-sphere, transporting a tangent frame around a latitude circle yields a nontrivial rotation, giving a nontrivial holonomy element.
3. For an abelian structure group $G$, the conjugation ambiguity disappears, so $h_\gamma(p)$ is independent of the choice of $p\in P_x$.
