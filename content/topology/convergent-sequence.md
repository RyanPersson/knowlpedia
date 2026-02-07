---
title: "Convergent sequence"
description: "A sequence whose terms eventually remain in every neighborhood of a limit point."
---

A **convergent sequence** $(x_n)$ in a {{< knowl id="topological-space" text="topological space" >}} $X$ converges to a point $x\in X$ if for every {{< knowl id="neighborhood" text="neighborhood" >}} $U$ of $x$, there exists $N$ such that $x_n\in U$ for all $n\ge N$.

In a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$, this is equivalent to $d(x_n,x)\to 0$. In a {{< knowl id="hausdorff-space" text="Hausdorff space" >}}, limits of convergent sequences are unique (see {{< knowl id="uniqueness-of-limits-hausdorff" text="uniqueness of limits" >}}).

**Examples:**
- In $\mathbb{R}$ with the usual metric, the sequence $x_n=1/n$ converges to $0$.
- In a space with the discrete metric, a sequence converges if and only if it is eventually constant.
