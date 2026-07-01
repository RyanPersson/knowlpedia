+++
id = "algebra-groups/class-equation-decomposition"
title = "Class equation decomposition"
kind = "knowl"
summary = "A finite group decomposes into its center and nontrivial conjugacy classes"
aliases = ["class-equation-decomposition", "Class equation decomposition"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/class-equation-decomposition.md"
+++

**Proposition (Decomposition underlying the class equation).**
Let $G$ be a finite [[algebra-groups/group|group]]. Consider the action of $G$ on itself by conjugation (see [[algebra-groups/conjugation-action-self|conjugation action]]). Then:

1. $G$ is a disjoint union of its conjugacy classes.
2. The elements with singleton conjugacy class are exactly the [[algebra-groups/center-of-group|center]] $Z(G)$.
3. For each $x\in G$, the size of the conjugacy class of $x$ equals the index $[G:C_G(x)]$, where $C_G(x)$ is the [[algebra-groups/centralizer|centralizer]], and this is a consequence of the [[algebra-groups/orbit-stabilizer-theorem|orbit–stabilizer theorem]].

In particular, choosing one representative $x_i$ from each conjugacy class outside the center yields the decomposition
$$
|G| \;=\; |Z(G)| \;+\; \sum_i [G:C_G(x_i)].
$$

**Context.**
This is the structural content behind the [[algebra-groups/class-equation|class equation]]: it turns the conjugation action into a counting identity, a key tool for $p$-groups and Sylow theory.
