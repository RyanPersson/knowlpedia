---
title: "Infimum (greatest lower bound)"
description: "The largest lower bound of a subset in an ordered set, if it exists."
---

Let $(X,\le)$ be an ordered set and let $S\subseteq X$. An element $i^\ast\in X$ is the **infimum** of $S$, written $i^\ast=\inf S$, if:
- $i^\ast$ is a lower bound of $S$, i.e. $\forall s\in S,\ i^\ast\le s$, and
- $i^\ast$ is the greatest such lower bound: for every lower bound $\ell$ of $S$, one has $\ell\le i^\ast$.

Infima are the "best possible" lower bounds. In $\mathbb{R}$, the existence of infima for bounded-below sets is equivalent to the existence of suprema for bounded-above sets.

**Examples:**
- In $\mathbb{R}$, $\inf(0,1)=0$ (even though $0\notin(0,1)$).
- In $\mathbb{R}$, $\inf\{1/n:n\in\mathbb{N}\}=0$.
- In $\mathbb{Z}$, the set $S=\{n\in\mathbb{Z}: n>0\}$ has $\inf S=1$ (and here the infimum is also a minimum).
