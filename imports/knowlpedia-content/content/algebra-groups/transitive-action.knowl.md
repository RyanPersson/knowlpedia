+++
id = "algebra-groups/transitive-action"
title = "Transitive Action"
kind = "knowl"
summary = "An action with a single orbit"
aliases = ["transitive-action", "Transitive Action"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/transitive-action.md"
+++

A [[algebra-groups/group-action|group action]] of a group $G$ on a set $X$ is **transitive** if for all $x,y\in X$ there exists $g\in G$ such that $g\cdot x = y$. Equivalently, the action has exactly one [[algebra-groups/orbit|orbit]].

Transitive actions are the natural context for coset actions: if $H\le G$, then the action of $G$ on $G/H$ is always transitive.

**Examples:**
- The natural action of $S_n$ on $\{1,\dots,n\}$ is transitive.
- The action of $G$ on $G/H$ by left multiplication is transitive for any subgroup $H$.
- The conjugation action of a nonabelian group on itself is generally not transitive (it has multiple conjugacy classes).
