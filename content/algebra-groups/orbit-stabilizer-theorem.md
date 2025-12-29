---
title: "Orbit–Stabilizer Theorem"
description: "For a group action, an orbit is in bijection with a coset space G/Stab(x)"
---

**Orbit–Stabilizer Theorem.**
Let $G$ be a {{< knowl id="group" text="group" >}} acting on a set $X$ via a {{< knowl id="group-action" text="group action" >}}. For $x \in X$, let $\operatorname{Orb}(x)$ be the {{< knowl id="orbit" text="orbit" >}} of $x$ and let $\operatorname{Stab}(x)$ be the {{< knowl id="stabilizer" text="stabilizer" >}} of $x$. Then the map
$$
G/\operatorname{Stab}(x) \to \operatorname{Orb}(x), \qquad g\,\operatorname{Stab}(x) \mapsto g\cdot x,
$$
is a bijection. In particular, if $G$ is finite then
$$
|\operatorname{Orb}(x)| = [G:\operatorname{Stab}(x)] \quad \text{and} \quad |G| = |\operatorname{Orb}(x)|\cdot |\operatorname{Stab}(x)|.
$$

This theorem converts problems about orbits into problems about {{< knowl id="coset" text="cosets" >}} and {{< knowl id="index-of-subgroup" text="index" >}}. It is the main input for the {{< knowl id="class-equation" text="class equation" >}} and many counting arguments.

**Proof sketch.**
The map $g \mapsto g\cdot x$ is constant on left cosets of $\operatorname{Stab}(x)$ and surjects onto $\operatorname{Orb}(x)$. Two elements $g,h$ give the same point iff $h^{-1}g \in \operatorname{Stab}(x)$, which is exactly the equivalence relation defining the coset space.
