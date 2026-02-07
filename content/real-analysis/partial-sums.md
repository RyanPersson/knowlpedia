---
title: "Partial sums"
description: "The finite sums obtained by truncating a series."
---

A **partial sum** is a finite sum $s_n=\sum_{k=1}^n a_k$ associated to a {{< knowl id="series" text="series" >}} $\sum_{k=1}^\infty a_k$.

The sequence $(s_n)$ encodes the series: statements about convergence or divergence of the series are statements about whether the partial sums form a sequence with a limit, as formalized in {{< knowl id="convergent-series" text="convergent series" >}}.

**Examples:**
- For $a_k=\frac{1}{k}$, the partial sums are $s_n=\sum_{k=1}^n \frac{1}{k}$ (harmonic numbers).
- For $a_k=r^{k-1}$, the partial sums are $s_n=\sum_{k=1}^n r^{k-1}=\frac{1-r^n}{1-r}$ (when $r\neq 1$).
