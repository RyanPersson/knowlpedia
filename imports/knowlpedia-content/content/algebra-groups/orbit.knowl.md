+++
id = "algebra-groups/orbit"
title = "Orbit"
kind = "knowl"
summary = "The set of points reachable from a given point under a group action"
aliases = ["orbit"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/orbit.md"
+++

Let a [[algebra-groups/group-action|group action]] of a group $G$ on a set $X$ be given, written $g\cdot x$. For $x\in X$, the **orbit** of $x$ is the subset
$$
G\cdot x := \{g\cdot x : g\in G\}\subseteq X.
$$

Orbits are precisely the equivalence classes of the relation "$x$ and $y$ lie in the same orbit," and hence the set of all orbits forms a [[shared-foundations/partition|partition]] of $X$. The size of an orbit is controlled by its [[algebra-groups/stabilizer|stabilizer]] via the [[algebra-groups/orbit-stabilizer-theorem|orbit-stabilizer theorem]].

**Examples:**
- For the natural action of $S_3$ on $\{1,2,3\}$, every point has orbit $\{1,2,3\}$, so the action is [[algebra-groups/transitive-action|transitive]].
- For the action of $\mathbb{Z}$ on $\mathbb{R}$ by translations $n\cdot x = x+n$, the orbit of $x$ is $x+\mathbb{Z}$.
- For the [[algebra-groups/conjugation-action|conjugation action]] of a group on itself, the orbits are the [[algebra-groups/conjugacy-class|conjugacy classes]].
