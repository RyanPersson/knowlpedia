---
title: "Sequentially compact set"
description: "A set in which every sequence has a convergent subsequence with limit in the set."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $K\subseteq X$. The set $K$ is **sequentially compact** if for every sequence $(x_n)$ in $K$ there exist:
- a {{< knowl id="subsequence" text="subsequence" >}} $(x_{n_k})$, and
- a point $x\in K$
such that
$$x_{n_k}\to x \quad\text{as }k\to\infty$$
(see {{< knowl id="convergent-sequence" text="convergence" >}}).

In metric spaces, sequential compactness is equivalent to {{< knowl id="compact-set" text="compactness" >}}, but the sequential formulation is often easier to use in analysis.

**Examples:**
- In $\mathbb{R}^k$, any closed and bounded set is sequentially compact (Bolzano–Weierstrass + closedness).
- The set $\{1/n:n\in\mathbb{N}\}\subset\mathbb{R}$ is not sequentially compact as a subset of itself (the sequence $1/n$ converges to $0\notin\{1/n\}$).
- Any finite subset of a metric space is sequentially compact (every sequence has an eventually constant subsequence).
