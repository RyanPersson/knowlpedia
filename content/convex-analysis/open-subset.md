---
title: "Open set"
description: "A set that contains a small open ball around each of its points"
---

Let $(X,d)$ be a metric space and let $A\subset X$.

The set $A$ is **open** if for every $a\in A$ there exists $\delta>0$ such that
$$
B(a;\delta)\subset A,
$$
where $B(a;\delta)$ is the open ball in $X$.

Open sets are stable under arbitrary unions and finite intersections (see {{< knowl id="basic-properties-of-open-sets" text="basic properties of open sets" >}}). Complements of open sets are {{< knowl id="closed-subset" text="closed" >}}.

**Examples:**
- In $\mathbb{R}$, every open interval $(a,b)$ is open.
- In any metric space, $\emptyset$ and $X$ are open.
- In a discrete metric space, every subset of $X$ is open.
