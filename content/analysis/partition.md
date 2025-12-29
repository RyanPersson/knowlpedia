---
title: "Partition"
description: "A decomposition of a set into disjoint nonempty pieces covering the whole set."
---

A **partition** of a set $X$ is a collection $\mathcal{P}$ of subsets of $X$ such that:
- every $P\in\mathcal{P}$ is nonempty,
- if $P,Q\in\mathcal{P}$ and $P\neq Q$, then $P\cap Q=\varnothing$ (pairwise disjointness),
- $\bigcup_{P\in\mathcal{P}} P = X$ (covers all of $X$).

Partitions encode "grouping" of elements. Every equivalence relation induces a partition into equivalence classes, and conversely every partition defines an equivalence relation by declaring two elements equivalent iff they lie in the same part.

**Examples:**
- The congruence classes mod $n$ partition $\mathbb{Z}$ into $n$ disjoint subsets.
- $\bigl\{\{0\},\{1,2\}\bigr\}$ is a partition of $\{0,1,2\}$.
- The collection $\{[k,k+1):k\in\mathbb{Z}\}$ is a partition of $\mathbb{R}$ into half-open intervals.
