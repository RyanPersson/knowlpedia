+++
id = "algebra-groups/kernel-of-action"
title = "Kernel of an Action"
kind = "knowl"
summary = "The subgroup acting trivially on every point of the set"
aliases = ["kernel-of-action", "Kernel of an Action"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/kernel-of-action.md"
+++

Let a [[algebra-groups/group-action|group action]] of a group $G$ on a set $X$ be given. The **kernel of the action** is
$$
\ker(G\curvearrowright X) := \{g\in G : g\cdot x = x \text{ for all } x\in X\}.
$$

This is a [[algebra-groups/normal-subgroup|normal subgroup]] of $G$; it is the [[algebra-groups/kernel-group|kernel]] of the associated permutation homomorphism $G\to \mathrm{Sym}(X)$. The action is [[algebra-groups/faithful-action|faithful]] precisely when this kernel is trivial.

**Examples:**
- For the trivial action, the kernel is all of $G$.
- For the left translation action of $G$ on itself, the kernel is the identity element alone.
- For conjugation of $G$ on itself, the kernel is the center $Z(G)$ (elements that commute with everything).
