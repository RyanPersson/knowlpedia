---
title: "Alternating series test"
description: "A convergence test for alternating series with decreasing term magnitudes tending to zero."
---

**Alternating series test (Leibniz):** Let $(a_n)$ be a sequence of real numbers such that

1. $a_n\ge 0$ for all $n$,
2. $(a_n)$ is decreasing, and
3. $a_n\to 0$.

Then the {{< knowl id="series" text="series" >}} $\sum_{n=1}^\infty (-1)^{n-1}a_n$ {{< knowl id="convergent-series" text="converges" >}}.

A common consequence is an error bound for {{< knowl id="partial-sums" text="partial sums" >}}: if $s$ is the limit and $s_N=\sum_{n=1}^N (-1)^{n-1}a_n$, then $|s-s_N|\le a_{N+1}$. This test is a basic source of {{< knowl id="conditionally-convergent-series" text="conditional convergence" >}} and uses the necessary condition {{< knowl id="terms-go-to-zero" text="terms go to zero" >}}.
