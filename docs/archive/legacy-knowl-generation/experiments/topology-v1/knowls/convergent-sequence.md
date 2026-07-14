---
title: "Convergent sequence"
description: "A sequence whose terms approach a point in a metric space."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $(x_n)$ be a sequence in $X$. The sequence is **convergent** if there exists $x\in X$ such that $d(x_n,x)\to 0$ as $n\to\infty$.

Equivalently: for every $\varepsilon>0$ there exists $N$ such that for all $n\ge N$, the term $x_n$ lies in the {{< knowl id="open-ball" text="open ball" >}} $B_d(x,\varepsilon)$. The point $x$ is called the {{< knowl id="limit-of-a-sequence" text="limit of the sequence" >}}.

**Examples:**
- In $\mathbb{R}$ with the usual metric, $x_n=1/n$ converges to $0$.
- In a discrete metric space, a sequence converges if and only if it is eventually constant.
- The sequence $x_n=(-1)^n$ in $\mathbb{R}$ does not converge.
