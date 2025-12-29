---
title: "Intersection"
description: "The set of elements common to all of the given sets."
---

The **intersection** of sets $A$ and $B$ is
$$A\cap B := \{x : (x\in A)\ \land\ (x\in B)\}.$$
More generally, for an indexed family $\{A_i\}_{i\in I}$, the intersection is
$$\bigcap_{i\in I} A_i := \{x : \forall i\in I,\ x\in A_i\}.$$

Intersections encode simultaneous constraints. In topology, closed sets are closed under arbitrary intersections, and limit-point definitions often involve intersections of neighborhoods.

**Examples:**
- $\{1,2\}\cap\{2,3\}=\{2\}$.
- $(0,2)\cap(1,3)=(1,2)$.
- If $A_n := (-1/n,1/n)$, then $\bigcap_{n=1}^\infty A_n = \{0\}$.
