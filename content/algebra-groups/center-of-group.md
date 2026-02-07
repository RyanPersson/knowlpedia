---
title: "Center of a Group"
description: "The set of elements commuting with every group element"
---

Let $G$ be a {{< knowl id="group" text="group" >}}. The **center** of $G$ is the subset
$
Z(G) \;=\; \{\,z\in G : zx=xz \text{ for all } x\in G\,\}.
$
It is a subgroup of $G$.

The center measures how far $G$ is from being abelian: $G$ is abelian iff $Z(G)=G$. Moreover, $Z(G)$ is always a {{< knowl id="characteristic-subgroup" text="characteristic subgroup" >}} (hence normal), and it can be described as the intersection of all {{< knowl id="centralizer" text="centralizers" >}} of elements of $G$.

**Examples:**
- If $G$ is abelian, then $Z(G)=G$.
- In $S_3$, $Z(S_3)=\{e\}$.
- In the quaternion group $Q_8$, the center is $\{\pm 1\}$.
