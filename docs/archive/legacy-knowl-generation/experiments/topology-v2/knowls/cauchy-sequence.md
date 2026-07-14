---
title: "Cauchy sequence"
description: "A sequence whose terms become arbitrarily close to each other"
---

A **Cauchy sequence** in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is a sequence $(x_n)$ such that for every $\varepsilon>0$ there exists $N$ with $d(x_m,x_n)<\varepsilon$ for all $m,n\ge N$.

Every {{< knowl id="convergent-sequence" text="convergent sequence" >}} is Cauchy (see {{< knowl id="convergent-sequence-is-cauchy" text="convergent sequence is Cauchy" >}}), and a metric space is {{< knowl id="complete-metric-space" text="complete" >}} precisely when every Cauchy sequence converges.

**Examples:**
- In $\mathbb{R}$, the partial sums $s_n=\sum_{k=0}^n 2^{-k}$ form a Cauchy sequence (and converge).
- In $\mathbb{Q}$ with the usual metric, a sequence of rational approximations to $\sqrt{2}$ is Cauchy but does not converge in $\mathbb{Q}$.
- In $\mathbb{R}$, the sequence $x_n=n$ is not Cauchy.
