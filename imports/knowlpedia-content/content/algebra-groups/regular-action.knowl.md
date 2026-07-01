+++
id = "algebra-groups/regular-action"
title = "Regular Action"
kind = "knowl"
summary = "An action that is both free and transitive"
aliases = ["regular-action", "Regular Action"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/regular-action.md"
+++

A [[algebra-groups/group-action|group action]] of a group $G$ on a set $X$ is **regular** if it is both [[algebra-groups/free-action|free]] and [[algebra-groups/transitive-action|transitive]]. Equivalently, for every pair $x,y\in X$ there exists a **unique** $g\in G$ such that $g\cdot x = y$.

Regular actions identify the set $X$ with the underlying set of $G$ (non-canonically, after choosing a basepoint), and are a standard way to model $G$ as permutations of a set.

**Examples:**
- The left translation action of $G$ on itself is regular.
- The action of $G$ on $G/H$ is regular iff $H$ is trivial.
- Any group acting on itself by left multiplication provides a regular action, hence a faithful permutation representation.
