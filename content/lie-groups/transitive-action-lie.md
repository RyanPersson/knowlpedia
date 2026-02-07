---
title: "Transitive Lie group action"
description: "A smooth action is transitive if it has a single orbit; equivalently for a stabilizer ."
---

### Definition
Let $G$ be a Lie group acting smoothly on a manifold $M$ (see {{< knowl id="smooth-action-lie-group" text="smooth Lie group actions" >}}). The action is **transitive** if for all $x,y\in M$ there exists $g\in G$ such that
$$
g\cdot x = y.
$$

Equivalently, for some (hence every) $x\in M$, the {{< knowl id="orbit-lie-group" text="orbit" >}} $G\cdot x$ equals all of $M$.

### Homogeneous space description
Fix $x_0\in M$ and let $H=G_{x_0}$ be the {{< knowl id="stabilizer-lie-group" text="stabilizer subgroup" >}}. Then $H$ is a Lie subgroup (by the {{< knowl id="closed-subgroup-theorem" text="closed subgroup theorem" >}}), and the orbit map induces a smooth surjection
$$
G/H \to M,\quad gH\mapsto g\cdot x_0.
$$

For transitive actions this map is a diffeomorphism under standard hypotheses, so $M$ is a {{< knowl id="homogeneous-space" text="homogeneous space" >}} (compare {{< knowl id="coset-space" text="coset spaces" >}}).

### Context
Transitive actions encode “geometries with a large symmetry group.” Many classical manifolds arise as homogeneous spaces, and questions about invariants on $M$ can often be translated into representation-theoretic questions about $H$.
