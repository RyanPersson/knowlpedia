---
title: "Index of a Subgroup"
description: "The number of cosets of a subgroup in a group"
---

Let $H$ be a {{< knowl id="subgroup" text="subgroup" >}} of a {{< knowl id="group" text="group" >}} $G$. The **index** of $H$ in $G$, denoted $[G:H]$, is the {{< knowl id="cardinality" section="shared-foundations" text="cardinality" >}} of the set of left {{< knowl id="coset" text="cosets" >}} of $H$ in $G$:
$$
[G:H] := \bigl|\{gH : g\in G\}\bigr|.
$$
(Equivalently, it is the number of distinct right cosets.)

For finite $G$, {{< knowl id="lagranges-theorem" text="Lagrange's theorem" >}} implies $[G:H] = |G|/|H|$, so in particular $|H|$ divides $|G|$. Small index has strong consequences: $[G:H]=1$ iff $H=G$, and if $[G:H]=2$ then $H$ is {{< knowl id="index-2-normal" text="normal" >}}, i.e. a normal subgroup.

**Examples:**
- In $\mathbb{Z}$ with $H=3\mathbb{Z}$, one has $[\mathbb{Z}:3\mathbb{Z}]=3$ since there are exactly three residue classes mod $3$.
- In $S_3$ with $H=\{e,(12)\}$, one has $[S_3:H]=3$ because $|S_3|=6$ and $|H|=2$.
- In an infinite group, the index can be infinite; for example, $[\mathbb{Z}:2\mathbb{Z}] = 2$ but $[\mathbb{Z}:\{0\}]$ is infinite.
