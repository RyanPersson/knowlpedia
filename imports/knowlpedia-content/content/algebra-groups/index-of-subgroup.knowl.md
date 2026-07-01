+++
id = "algebra-groups/index-of-subgroup"
title = "Index of a Subgroup"
kind = "knowl"
summary = "The number of cosets of a subgroup in a group"
aliases = ["index-of-subgroup", "Index of a Subgroup"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/index-of-subgroup.md"
+++

Let $H$ be a [[algebra-groups/subgroup|subgroup]] of a [[algebra-groups/group|group]] $G$. The **index** of $H$ in $G$, denoted $[G:H]$, is the [[shared-foundations/cardinality|cardinality]] of the set of left [[algebra-groups/coset|cosets]] of $H$ in $G$:
$$
[G:H] := \bigl|\{gH : g\in G\}\bigr|.
$$
(Equivalently, it is the number of distinct right cosets.)

For finite $G$, [[algebra-groups/lagranges-theorem|Lagrange's theorem]] implies $[G:H] = |G|/|H|$, so in particular $|H|$ divides $|G|$. Small index has strong consequences: $[G:H]=1$ iff $H=G$, and if $[G:H]=2$ then $H$ is [[algebra-groups/index-2-normal|normal]], i.e. a normal subgroup.

**Examples:**
- In $\mathbb{Z}$ with $H=3\mathbb{Z}$, one has $[\mathbb{Z}:3\mathbb{Z}]=3$ since there are exactly three residue classes mod $3$.
- In $S_3$ with $H=\{e,(12)\}$, one has $[S_3:H]=3$ because $|S_3|=6$ and $|H|=2$.
- In an infinite group, the index can be infinite; for example, $[\mathbb{Z}:2\mathbb{Z}] = 2$ but $[\mathbb{Z}:\{0\}]$ is infinite.
