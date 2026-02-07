---
title: "Partition"
description: "A way to break a set into disjoint nonempty blocks that cover it."
---

A **partition** of a set $X$ is a set $\mathcal{P}$ of subsets of $X$ (called **blocks** or **parts**) such that:

1. (**Nonempty blocks**) For every $B\in\mathcal{P}$, one has $B\neq\varnothing$.
2. (**Pairwise disjoint**) For all $B,C\in\mathcal{P}$, if $B\neq C$ then $B\cap C=\varnothing$.
3. (**Covers $X$**) $\bigcup_{B\in\mathcal{P}} B = X$.

Partitions are in bijective correspondence with {{< knowl id="equivalence-relation" text="equivalence relations" >}}: an equivalence relation yields a partition by its {{< knowl id="equivalence-class" text="equivalence classes" >}}, and a partition yields an equivalence relation by declaring two elements equivalent exactly when they lie in the same block.

**Examples:**
- $\bigl\{\{1,3\},\{2\},\{4\}\bigr\}$ is a partition of $\{1,2,3,4\}$.
- The set of residue classes modulo $n$ forms a partition of $\mathbb{Z}$.
