+++
id = "algebra-groups/direct-sum-groups"
title = "Direct Sum of Groups"
kind = "knowl"
summary = "The subgroup of a direct product with finite support"
aliases = ["direct-sum-groups", "Direct Sum of Groups"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/direct-sum-groups.md"
+++

Let $(G_i)_{i\in I}$ be a family of [[algebra-groups/group|groups]] with identities $e_i$. The (external) **direct sum**
$$
\bigoplus_{i\in I} G_i
$$

is the subgroup of the [[algebra-groups/direct-product-groups|direct product]] $\prod_{i\in I} G_i$ consisting of all tuples $(g_i)_{i\in I}$ such that $g_i=e_i$ for all but finitely many indices $i$ (this "all but finitely many" condition is called **finite support**).

For finite index sets $I$, the direct sum coincides with the direct product. In practice the term "direct sum" is most common for [[algebra-groups/abelian-group|abelian groups]] and infinite families, where the finite-support condition matters.

**Examples:**
- If $I=\{1,\dots,n\}$ is finite, then $\bigoplus_{i=1}^n G_i=\prod_{i=1}^n G_i$ as groups.
- $\bigoplus_{n\in\mathbb{N}}\mathbb{Z}$ is the free abelian group on countably many generators (elements are integer sequences that are eventually $0$).
- $\bigoplus_{n\in\mathbb{N}} C_2$ is the group of $\{0,1\}$-sequences with finitely many $1$'s under componentwise addition mod $2$.
