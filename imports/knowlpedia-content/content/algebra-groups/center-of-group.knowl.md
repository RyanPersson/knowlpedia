+++
id = "algebra-groups/center-of-group"
title = "Center of a Group"
kind = "knowl"
summary = "The set of elements commuting with every group element"
aliases = ["center-of-group", "Center of a Group"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/center-of-group.md"
+++

Let $G$ be a [[algebra-groups/group|group]]. The **center** of $G$ is the subset
$
Z(G) \;=\; \{\,z\in G : zx=xz \text{ for all } x\in G\,\}.
$
It is a subgroup of $G$.

The center measures how far $G$ is from being abelian: $G$ is abelian iff $Z(G)=G$. Moreover, $Z(G)$ is always a [[algebra-groups/characteristic-subgroup|characteristic subgroup]] (hence normal), and it can be described as the intersection of all [[algebra-groups/centralizer|centralizers]] of elements of $G$.

**Examples:**
- If $G$ is abelian, then $Z(G)=G$.
- In $S_3$, $Z(S_3)=\{e\}$.
- In the quaternion group $Q_8$, the center is $\{\pm 1\}$.
