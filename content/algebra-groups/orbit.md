---
title: "Orbit"
description: "The set of points reachable from a given point under a group action"
---

Let a {{< knowl id="group-action" text="group action" >}} of a group $G$ on a set $X$ be given, written $g\cdot x$. For $x\in X$, the **orbit** of $x$ is the subset
$$
G\cdot x := \{g\cdot x : g\in G\}\subseteq X.
$$

Orbits are precisely the equivalence classes of the relation "$x$ and $y$ lie in the same orbit," and hence the set of all orbits forms a {{< knowl id="partition" section="shared-foundations" text="partition" >}} of $X$. The size of an orbit is controlled by its {{< knowl id="stabilizer" text="stabilizer" >}} via the {{< knowl id="orbit-stabilizer-theorem" text="orbit-stabilizer theorem" >}}.

**Examples:**
- For the natural action of $S_3$ on $\{1,2,3\}$, every point has orbit $\{1,2,3\}$, so the action is {{< knowl id="transitive-action" text="transitive" >}}.
- For the action of $\mathbb{Z}$ on $\mathbb{R}$ by translations $n\cdot x = x+n$, the orbit of $x$ is $x+\mathbb{Z}$.
- For the {{< knowl id="conjugation-action" text="conjugation action" >}} of a group on itself, the orbits are the {{< knowl id="conjugacy-class" text="conjugacy classes" >}}.
