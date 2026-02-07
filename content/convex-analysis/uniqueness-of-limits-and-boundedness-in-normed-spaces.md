---
title: "Uniqueness of limits and boundedness in normed spaces"
description: "Limits are unique, and every convergent sequence is bounded"
---

**Proposition.**
Let $(X,\|\cdot\|)$ be a normed space.

1. If a sequence $(x_n)$ {{< knowl id="convergence-in-normed-spaces" text="converges" >}} to both $x$ and $y$, then $x=y$.
2. Every convergent sequence is {{< knowl id="bounded-set-and-bounded-sequence" text="bounded" >}}.

**Context.** These are basic structural properties of norm convergence, paralleling the corresponding facts in metric spaces.

**Proof sketch.**
1. Using the triangle inequality,
$$
\|x-y\|\le \|x-x_n\|+\|x_n-y\|\to 0,
$$

so $\|x-y\|=0$ and hence $x=y$.
2. If $x_n\to x$, then for $n$ large we have $\|x_n-x\|\le 1$. Then $\|x_n\|\le \|x\|+1$ for all large $n$; finitely many remaining terms are bounded as well.
