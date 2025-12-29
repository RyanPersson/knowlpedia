---
title: "Conjugation Action"
description: "The action of a group on itself (or its subgroups) by conjugation"
---

Let $G$ be a {{< knowl id="group" text="group" >}}. The **conjugation action** of $G$ on itself is the {{< knowl id="group-action" text="group action" >}} defined by
$$
g\cdot x := gxg^{-1}.
$$
Under this action, two elements lie in the same orbit exactly when they are {{< knowl id="conjugate-element" text="conjugate" >}}, so the orbits are the {{< knowl id="conjugacy-class" text="conjugacy classes" >}}. The stabilizer of $x$ is its {{< knowl id="centralizer" text="centralizer" >}}, and the kernel of the action is the {{< knowl id="center-of-group" text="center" >}}, consisting of elements that commute with all of $G$.

More generally, $G$ acts on its subgroups by $g\cdot H := gHg^{-1}$; the stabilizer of a subgroup $H$ in this action is its {{< knowl id="normalizer" text="normalizer" >}}. A subgroup is normal iff it is fixed by every element under this action.

**Examples:**
- In $S_3$, the conjugacy classes are $\{e\}$, the three transpositions, and the two $3$-cycles.
- If $G$ is abelian, then $gxg^{-1}=x$ for all $g,x$, so every conjugacy class is a singleton.
- For the subgroup action, $H\le G$ is normal exactly when $gHg^{-1}=H$ for all $g\in G$.
