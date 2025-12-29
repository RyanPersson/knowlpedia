---
title: "Series (summable family)"
description: "An infinite sum ∑ a_n defined via convergence of its partial sums."
---

Let $(a_n)_{n\in\mathbb{N}}$ be a sequence in $\mathbb{R}$ or $\mathbb{C}$. The **series**
$$\sum_{n=1}^\infty a_n$$
is defined via its **partial sums** $s_N=\sum_{n=1}^N a_n$. One says the series is **summable** if the sequence $(s_N)$ converges.

Series are the basic mechanism for defining many analytic objects (power series, Fourier series, infinite products) and for quantifying convergence beyond finite sums.

**Examples:**
- $\sum_{n=1}^\infty \frac{1}{2^n}$ is summable (it converges to $1$).
- $\sum_{n=1}^\infty \frac{1}{n}$ is not summable (it diverges).
- $\sum_{n=0}^\infty z^n$ is a geometric series in $\mathbb{C}$, summable iff $|z|<1$.
