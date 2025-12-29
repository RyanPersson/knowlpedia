---
title: "Convergent series"
description: "A series whose sequence of partial sums converges in ℝ or ℂ."
---

A {{< knowl id="series" text="series" >}} $\sum_{n=1}^\infty a_n$ (with $a_n\in\mathbb{R}$ or $\mathbb{C}$) is **convergent** if its {{< knowl id="partial-sums" text="partial sums" >}}
$$s_N := \sum_{n=1}^N a_n$$
{{< knowl id="convergent-sequence" text="converge" >}} to a {{< knowl id="limit-of-a-sequence" text="limit" >}} $s$ as $N\to\infty$. In that case one writes
$$\sum_{n=1}^\infty a_n = s.$$

Convergent series provide a rigorous meaning to infinite sums and are essential for analytic expansions and approximation. See also {{< knowl id="absolutely-convergent-series" text="absolute convergence" >}} and {{< knowl id="conditionally-convergent-series" text="conditional convergence" >}}.

**Examples:**
- The geometric series $\sum_{n=0}^\infty r^n$ converges to $\frac{1}{1-r}$ if $|r|<1$.
- $\sum_{n=1}^\infty \frac{1}{n^2}$ converges (to $\pi^2/6$, though that value is not needed for the definition).
- $\sum_{n=1}^\infty (-1)^{n+1}\frac{1}{n}$ converges (alternating harmonic series).
