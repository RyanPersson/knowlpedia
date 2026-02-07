---
title: "Expectation"
description: "The integral of a random variable with respect to the underlying probability measure."
---

An **expectation** of a {{< knowl id="random-variable" text="random variable" >}} $X$ is the number
$$
\mathbb E[X]=\int_\Omega X(\omega)\,d\mathbb P(\omega),
$$

provided $X$ is integrable, i.e. $\int_\Omega |X|\,d\mathbb P<\infty$ (so $X$ is an $L^1$ random variable; see {{< knowl id="l1-function" section="measure-theory" text="L1 function" >}}).

This definition uses the {{< knowl id="lebesgue-integral" section="measure-theory" text="Lebesgue integral" >}} on the underlying {{< knowl id="probability-space" text="probability space" >}}; expectation is the basic averaging operation underlying {{< knowl id="variance" text="variance" >}}, {{< knowl id="covariance" text="covariance" >}}, and many limit theorems.

**Examples:**
- If $X$ takes values $x_k$ with probabilities $p_k$ (countably many), then $\mathbb E[X]=\sum_k x_k p_k$ whenever $\sum_k |x_k|p_k<\infty$.
- If $X$ is uniform on $[0,1]$, then $\mathbb E[X]=\int_0^1 x\,dx=\tfrac12$.
