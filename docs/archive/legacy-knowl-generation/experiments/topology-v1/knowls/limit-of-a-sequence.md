---
title: "Limit of a sequence"
description: "A point that a sequence approaches in a metric space."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $(x_n)$ be a sequence in $X$. A point $x\in X$ is a **limit** of $(x_n)$ if for every $\varepsilon>0$ there exists $N$ such that for all $n\ge N$,
$$
d(x_n,x)<\varepsilon.
$$
When such an $x$ exists, the sequence is {{< knowl id="convergent-sequence" text="convergent" >}} to $x$.

In metric spaces, limits are unique; this is a special case of {{< knowl id="uniqueness-of-limits-hausdorff" text="uniqueness of limits in Hausdorff spaces" >}}.

**Examples:**
- The limit of $x_n=1/n$ in $\mathbb{R}$ is $0$.
- A constant sequence $x_n=a$ has limit $a$.
