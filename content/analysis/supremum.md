---
title: "Supremum (least upper bound)"
description: "The smallest upper bound of a subset in an ordered set, if it exists."
---

Let $(X,\le)$ be a {{< knowl id="partial-order" text="partially ordered set" >}} and let $S\subseteq X$. An element $s^\ast\in X$ is the **supremum** of $S$, written $s^\ast=\sup S$, if:
- $s^\ast$ is an {{< knowl id="upper-bound" text="upper bound" >}} of $S$, i.e. $\forall s\in S,\ s\le s^\ast$, and
- $s^\ast$ is the least such upper bound: for every upper bound $u$ of $S$, one has $s^\ast\le u$.

Suprema are "best possible" upper bounds and are the key completeness feature of $\mathbb{R}$. In general ordered sets, $\sup S$ need not exist.

**Examples:**
- In $\mathbb{R}$, $\sup(0,1)=1$ (even though $1\notin(0,1)$).
- In $\mathbb{R}$, if $S=\{x\in\mathbb{R}: x^2<2\}$, then $\sup S=\sqrt{2}$.
- In $\mathbb{Q}$ with its usual order, the set $S=\{q\in\mathbb{Q}: q^2<2\}$ has no supremum in $\mathbb{Q}$ (its least upper bound in $\mathbb{R}$ is $\sqrt{2}\notin\mathbb{Q}$).
