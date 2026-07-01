+++
id = "algebra-groups/free-action"
title = "Free Action"
kind = "knowl"
summary = "An action in which only the identity can fix a point"
aliases = ["free-action", "Free Action"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/free-action.md"
+++

A [[algebra-groups/group-action|group action]] of a group $G$ on a set $X$ is **free** if for every $x\in X$, the [[algebra-groups/stabilizer|stabilizer]] $G_x$ is the [[algebra-groups/trivial-subgroup|trivial subgroup]]. Equivalently, the condition
"$g\cdot x = x$ for some $x$"
forces $g=e$.

Free actions are one half of the definition of a [[algebra-groups/regular-action|regular action]] (free + transitive).

**Examples:**
- The left translation action of $G$ on itself is free.
- The action of $G$ on the coset space $G/H$ by left multiplication is free iff $H=\{e\}$.
- The action of $C_n$ on the vertices of a regular $n$-gon by rotation is free when restricted to the vertex set (no nontrivial rotation fixes a vertex).
