---
title: "Open set"
description: "A set in a metric space that contains an open ball around each of its points."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}}. A subset $U\subseteq X$ is **open** if for every $x\in U$ there exists $r>0$ such that
$$B(x,r)\subseteq U.$$

Open sets are the primitive "admissible {{< knowl id="neighborhood" text="neighborhoods" >}}" in topology. In analysis, openness is the natural condition for local arguments (e.g., {{< knowl id="differentiability-one-variable" text="differentiability" >}} is typically defined on open subsets of $\mathbb{R}^k$).

**Examples:**
- In $\mathbb{R}$, every open interval $(a,b)$ is open.
- In $\mathbb{R}^k$, every open ball $B(x,r)$ is open.
- In any metric space, $\varnothing$ and $X$ are open.
