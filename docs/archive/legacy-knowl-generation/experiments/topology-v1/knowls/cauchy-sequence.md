---
title: "Cauchy sequence"
description: "A sequence whose terms eventually get arbitrarily close to each other."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $(x_n)$ be a sequence in $X$. The sequence is **Cauchy** if for every $\varepsilon>0$ there exists $N$ such that for all $m,n\ge N$,
$$
d(x_m,x_n)<\varepsilon.
$$

Every {{< knowl id="convergent-sequence" text="convergent sequence" >}} is Cauchy, and a space is {{< knowl id="complete-metric-space" text="complete" >}} precisely when every Cauchy sequence converges to a point of the space.

**Examples:**
- In $\mathbb{R}$, the sequence $x_n=1/n$ is Cauchy (and convergent).
- In $\mathbb{Q}$ (with the usual metric), a sequence of rational approximations to $\sqrt{2}$ is Cauchy but does not converge in $\mathbb{Q}$.
- The sequence $x_n=n$ in $\mathbb{R}$ is not Cauchy.
