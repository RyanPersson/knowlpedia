---
title: "Total order (linear order)"
description: "A partial order in which every pair of elements is comparable."
---

A **total order** (or **linear order**) on a set $X$ is a partial order $\le$ on $X$ such that for all $x,y\in X$,
$$x\le y\ \text{or}\ y\le x.$$
This property is called **comparability** (or **trichotomy** when strengthened appropriately).

Total orders allow one to speak of intervals, monotonicity, and order convergence, which are central in one-variable real analysis.

**Examples:**
- The usual order $\le$ on $\mathbb{R}$ is a total order.
- Lexicographic order on $\mathbb{R}^2$: define $(a,b)\le_{\mathrm{lex}}(c,d)$ iff either $a<c$, or $a=c$ and $b\le d$; this is a total order.
- $\subseteq$ on $\mathcal{P}(\{1,2\})$ is not a total order since $\{1\}$ and $\{2\}$ are incomparable.
