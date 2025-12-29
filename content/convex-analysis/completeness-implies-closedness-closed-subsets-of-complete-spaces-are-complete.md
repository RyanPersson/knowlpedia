---
title: "Completeness and closedness"
description: "Complete subsets are closed; closed subsets of complete spaces are complete"
---

**Proposition.**
Let $(X,d)$ be a {{< knowl id="metric-metric-space" text="metric space" >}}.

1. If $E\subset X$ is {{< knowl id="complete-metric-space-complete-subset" text="complete" >}}, then $E$ is {{< knowl id="closed-subset" text="closed" >}} in $X$.
2. If $X$ is complete and $E\subset X$ is closed, then $E$ is complete (with the restricted metric).

**Context.** This gives a practical way to recognize complete sets: inside a complete ambient space, "closed" and "complete" coincide.

**Proof sketch.**
1. Take a sequence $(x_n)\subset E$ converging in $X$ to $x$. Any {{< knowl id="convergent-sequences-are-cauchy" text="convergent sequence is Cauchy" >}}, so $(x_n)$ is Cauchy in $E$. By completeness of $E$, it converges in $E$ to some $y\in E$. By {{< knowl id="uniqueness-of-limits-in-metric-spaces" text="uniqueness of limits" >}}, $x=y\in E$, hence $E$ is closed.
2. Let $(x_n)$ be Cauchy in $E$. Then it is Cauchy in $X$ and hence converges in $X$ (since $X$ is complete) to some $x\in X$. Because $E$ is closed and $(x_n)\subset E$ converges to $x$, we have $x\in E$. Thus $(x_n)$ converges in $E$.
