---
title: "Convergent sequence"
description: "A sequence in a metric space whose terms approach a limit point"
---

A **convergent sequence** in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is a sequence $(x_n)$ for which there exists $x\in X$ such that for every $\varepsilon>0$ there is $N$ with $d(x_n,x)<\varepsilon$ for all $n\ge N$.

The point $x$ is the {{< knowl id="limit-of-a-sequence" text="limit of the sequence" >}}. In terms of the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}, this is equivalent to saying $x_n$ is eventually in every {{< knowl id="neighborhood" section="topology-core" text="neighborhood" >}} of $x$.

**Examples:**
- In $\mathbb{R}$ with the usual metric, the sequence $x_n=1/n$ converges to $0$.
- The constant sequence $x_n=c$ converges to $c$ in any metric space.
- In the discrete metric on $X$, a sequence converges if and only if it is eventually constant.
