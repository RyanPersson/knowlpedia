---
title: "Partial sums"
description: "The finite sums s_N = ∑_{n=1}^N a_n associated to a series."
---

Given a sequence $(a_n)$ in $\mathbb{R}$ or $\mathbb{C}$, the **partial sums** of the series $\sum_{n=1}^\infty a_n$ are the numbers
$$s_N := \sum_{n=1}^N a_n\qquad (N\in\mathbb{N}).$$

A series is defined to converge precisely when its partial sums converge as $N\to\infty$. Many convergence tests are statements about the behavior of $(s_N)$.

**Examples:**
- If $a_n=1/2^n$, then $s_N=\sum_{n=1}^N 1/2^n = 1-2^{-N}$.
- If $a_n=1$, then $s_N=N$.
- If $a_n=(-1)^{n+1}$, then $s_1=1$, $s_2=0$, $s_3=1$, $s_4=0$, so $(s_N)$ does not converge.
