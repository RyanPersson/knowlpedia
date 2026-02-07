---
title: "Class Equation"
description: "A finite group decomposes into the center plus conjugacy classes of larger size"
---

**Class Equation.**
Let $G$ be a finite {{< knowl id="group" text="group" >}}. For $g \in G$, let the conjugacy class be
$$
\operatorname{Cl}(g)=\{xgx^{-1}: x\in G\},
$$
and let the {{< knowl id="centralizer" text="centralizer" >}} be
$$
C_G(g)=\{x\in G : xg=gx\}.
$$

Then $|\operatorname{Cl}(g)| = [G:C_G(g)]$. If $Z(G)$ denotes the {{< knowl id="center-of-group" text="center" >}} of $G$ and $g_1,\dots,g_r$ are representatives of the distinct {{< knowl id="conjugacy-class" text="conjugacy classes" >}} contained in $G \setminus Z(G)$, then
$$
|G| = |Z(G)| + \sum_{i=1}^r [G:C_G(g_i)].
$$

The class equation is the orbit decomposition of the {{< knowl id="conjugation-action" text="conjugation action" >}} of $G$ on itself, combined with the {{< knowl id="orbit-stabilizer-theorem" text="orbit–stabilizer theorem" >}}. It is a standard tool for proving existence of normal subgroups, for example {{< knowl id="p-group-nontrivial-center" text="a finite p-group has nontrivial center" >}}.
