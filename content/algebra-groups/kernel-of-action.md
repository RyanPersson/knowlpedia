---
title: "Kernel of an Action"
description: "The subgroup acting trivially on every point of the set"
---

Let a {{< knowl id="group-action" text="group action" >}} of a group $G$ on a set $X$ be given. The **kernel of the action** is
$$
\ker(G\curvearrowright X) := \{g\in G : g\cdot x = x \text{ for all } x\in X\}.
$$

This is a {{< knowl id="normal-subgroup" text="normal subgroup" >}} of $G$; it is the {{< knowl id="kernel-group" text="kernel" >}} of the associated permutation homomorphism $G\to \mathrm{Sym}(X)$. The action is {{< knowl id="faithful-action" text="faithful" >}} precisely when this kernel is trivial.

**Examples:**
- For the trivial action, the kernel is all of $G$.
- For the left translation action of $G$ on itself, the kernel is the identity element alone.
- For conjugation of $G$ on itself, the kernel is the center $Z(G)$ (elements that commute with everything).
