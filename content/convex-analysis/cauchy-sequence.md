---
title: "Cauchy sequence"
description: "A sequence whose terms eventually become arbitrarily close to each other"
---

Let $(X,d)$ be a {{< knowl id="metric-metric-space" text="metric space" >}}. A sequence $(x_n)$ in $X$ is a **Cauchy sequence** if
$$
(\forall \varepsilon>0)(\exists N\in\mathbb{N})(\forall m,n\ge N):\ d(x_m,x_n)<\varepsilon.
$$
This definition depends only on the internal mutual distances of the sequence, not on a candidate limit.

Every {{< knowl id="convergence-of-a-sequence" text="convergent" >}} sequence is Cauchy, but the converse holds exactly in {{< knowl id="complete-metric-space-complete-subset" text="complete metric spaces" >}}.

**Examples:**
- In $\mathbb{R}$, $x_n=1/n$ is Cauchy (and convergent).
- In $\mathbb{Q}$ with the usual metric, a sequence of rationals converging to $\sqrt{2}$ is Cauchy but not convergent in $\mathbb{Q}$.
