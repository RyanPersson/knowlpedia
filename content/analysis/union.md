---
title: "Union"
description: "The set of elements that belong to at least one of the given sets."
---

The **union** of sets $A$ and $B$ is
$$A\cup B := \{x : (x\in A)\ \lor\ (x\in B)\}.$$
More generally, for an indexed family $\{A_i\}_{i\in I}$, the union is
$$\bigcup_{i\in I} A_i := \{x : \exists i\in I\ \text{with}\ x\in A_i\}.$$

Unions are central in topology and analysis: open sets are closed under arbitrary unions, and coverings are families whose union contains the set of interest.

**Examples:**
- $\{1,2\}\cup\{2,3\}=\{1,2,3\}$.
- $(0,1)\cup(1,2)=(0,2)\setminus\{1\}$.
- If $A_n:=(-1/n,1/n)\subseteq\mathbb{R}$, then $\bigcup_{n=1}^\infty A_n = (-1,1)$.
