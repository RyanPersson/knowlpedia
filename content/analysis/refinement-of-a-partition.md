---
title: "Refinement of a partition"
description: "A partition Q that contains all points of a partition P (possibly with extra points)."
---

Let $P$ and $Q$ be partitions of $[a,b]$. The partition $Q$ is a **refinement** of $P$ if every point of $P$ is also a point of $Q$, i.e.
$$\{x_0,\dots,x_n\}\subseteq \{y_0,\dots,y_m\},$$
where $P:a=x_0<\cdots<x_n=b$ and $Q:a=y_0<\cdots<y_m=b$.

Refinements correspond to subdividing intervals further. Upper sums decrease and lower sums increase under refinement, which is fundamental in proving integrability criteria.

**Examples:**
- If $P:0<1$ and $Q:0<1/2<1$, then $Q$ is a refinement of $P$.
- If $P:0<1/3<2/3<1$ and $Q:0<1/6<1/3<1/2<2/3<1$, then $Q$ refines $P$.
- Any partition refines itself.
