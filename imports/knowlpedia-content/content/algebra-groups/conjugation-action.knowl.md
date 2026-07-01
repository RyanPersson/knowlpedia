+++
id = "algebra-groups/conjugation-action"
title = "Conjugation Action"
kind = "knowl"
summary = "The action of a group on itself (or its subgroups) by conjugation"
aliases = ["conjugation-action", "Conjugation Action"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/conjugation-action.md"
+++

Let $G$ be a [[algebra-groups/group|group]]. The **conjugation action** of $G$ on itself is the [[algebra-groups/group-action|group action]] defined by
$$
g\cdot x := gxg^{-1}.
$$

Under this action, two elements lie in the same orbit exactly when they are [[algebra-groups/conjugate-element|conjugate]], so the orbits are the [[algebra-groups/conjugacy-class|conjugacy classes]]. The stabilizer of $x$ is its [[algebra-groups/centralizer|centralizer]], and the kernel of the action is the [[algebra-groups/center-of-group|center]], consisting of elements that commute with all of $G$.

More generally, $G$ acts on its subgroups by $g\cdot H := gHg^{-1}$; the stabilizer of a subgroup $H$ in this action is its [[algebra-groups/normalizer|normalizer]]. A subgroup is normal iff it is fixed by every element under this action.

**Examples:**
- In $S_3$, the conjugacy classes are $\{e\}$, the three transpositions, and the two $3$-cycles.
- If $G$ is abelian, then $gxg^{-1}=x$ for all $g,x$, so every conjugacy class is a singleton.
- For the subgroup action, $H\le G$ is normal exactly when $gHg^{-1}=H$ for all $g\in G$.
