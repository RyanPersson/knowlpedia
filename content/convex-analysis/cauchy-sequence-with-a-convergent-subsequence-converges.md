---
title: "Cauchy sequence with a convergent subsequence converges"
description: "A Cauchy sequence converges if one of its subsequences converges"
---

**Proposition.**
Let $(X,d)$ be a {{< knowl id="metric-metric-space" text="metric space" >}}. If $(x_n)$ is a {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}} and has a {{< knowl id="subsequence" text="subsequence" >}} $(x_{n_k})$ that {{< knowl id="convergence-of-a-sequence" text="converges" >}} to some $a\in X$, then the entire sequence converges to $a$.

**Context.** This result is often used to prove convergence once one can identify a candidate limit via a subsequence. It is also a standard step in showing completeness-type statements.

**Proof sketch.** Fix $\varepsilon>0$. Since $(x_n)$ is Cauchy, choose $N$ such that $d(x_n,x_m)<\varepsilon/2$ for all $m,n\ge N$. Since $x_{n_k}\to a$, choose $K$ such that $d(x_{n_k},a)<\varepsilon/2$ for all $k\ge K$. Pick $k\ge K$ with $n_k\ge N$. Then for all $n\ge N$,
$$
d(x_n,a)\le d(x_n,x_{n_k})+d(x_{n_k},a)<\varepsilon/2+\varepsilon/2=\varepsilon,
$$
so $x_n\to a$.
