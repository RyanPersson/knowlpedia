+++
id = "algebra-groups/class-equation"
title = "Class Equation"
kind = "knowl"
summary = "A finite group decomposes into the center plus conjugacy classes of larger size"
aliases = ["class-equation", "Class Equation"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/class-equation.md"
+++

**Class Equation.**
Let $G$ be a finite [[algebra-groups/group|group]]. For $g \in G$, let the conjugacy class be
$$
\operatorname{Cl}(g)=\{xgx^{-1}: x\in G\},
$$
and let the [[algebra-groups/centralizer|centralizer]] be
$$
C_G(g)=\{x\in G : xg=gx\}.
$$

Then $|\operatorname{Cl}(g)| = [G:C_G(g)]$. If $Z(G)$ denotes the [[algebra-groups/center-of-group|center]] of $G$ and $g_1,\dots,g_r$ are representatives of the distinct [[algebra-groups/conjugacy-class|conjugacy classes]] contained in $G \setminus Z(G)$, then
$$
|G| = |Z(G)| + \sum_{i=1}^r [G:C_G(g_i)].
$$

The class equation is the orbit decomposition of the [[algebra-groups/conjugation-action|conjugation action]] of $G$ on itself, combined with the [[algebra-groups/orbit-stabilizer-theorem|orbit–stabilizer theorem]]. It is a standard tool for proving existence of normal subgroups, for example [[algebra-groups/p-group-nontrivial-center|a finite p-group has nontrivial center]].
