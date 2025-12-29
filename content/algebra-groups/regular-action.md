---
title: "Regular Action"
description: "An action that is both free and transitive"
---

A {{< knowl id="group-action" text="group action" >}} of a group $G$ on a set $X$ is **regular** if it is both {{< knowl id="free-action" text="free" >}} and {{< knowl id="transitive-action" text="transitive" >}}. Equivalently, for every pair $x,y\in X$ there exists a **unique** $g\in G$ such that $g\cdot x = y$.

Regular actions identify the set $X$ with the underlying set of $G$ (non-canonically, after choosing a basepoint), and are a standard way to model $G$ as permutations of a set.

**Examples:**
- The left translation action of $G$ on itself is regular.
- The action of $G$ on $G/H$ is regular iff $H$ is trivial.
- Any group acting on itself by left multiplication provides a regular action, hence a faithful permutation representation.
