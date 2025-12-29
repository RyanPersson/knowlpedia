---
title: "Class equation decomposition"
description: "A finite group decomposes into its center and nontrivial conjugacy classes"
---

**Proposition (Decomposition underlying the class equation).**
Let $G$ be a finite {{</* knowl id="group" text="group" */>}}. Consider the action of $G$ on itself by conjugation (see {{</* knowl id="conjugation-action-self" text="conjugation action" */>}}). Then:

1. $G$ is a disjoint union of its conjugacy classes.
2. The elements with singleton conjugacy class are exactly the {{</* knowl id="center-of-group" text="center" */>}} $Z(G)$.
3. For each $x\in G$, the size of the conjugacy class of $x$ equals the index $[G:C_G(x)]$, where $C_G(x)$ is the {{</* knowl id="centralizer" text="centralizer" */>}}, and this is a consequence of the {{</* knowl id="orbit-stabilizer-theorem" text="orbit–stabilizer theorem" */>}}.

In particular, choosing one representative $x_i$ from each conjugacy class outside the center yields the decomposition
$$
|G| \;=\; |Z(G)| \;+\; \sum_i [G:C_G(x_i)].
$$

**Context.**
This is the structural content behind the {{</* knowl id="class-equation" text="class equation" */>}}: it turns the conjugation action into a counting identity, a key tool for $p$-groups and Sylow theory.

**Proof sketch.**
(1) Orbits of an action partition the underlying set.
(2) A conjugacy class of $x$ has size $1$ iff $gxg^{-1}=x$ for all $g$, i.e. $x\in Z(G)$.
(3) Apply orbit–stabilizer to the conjugation action: the stabilizer of $x$ is precisely $C_G(x)$.
