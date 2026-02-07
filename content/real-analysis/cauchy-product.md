---
title: "Cauchy product"
description: "A convolution-style product of two series."
---

A **Cauchy product** of two series $\sum_{n=0}^\infty a_n$ and $\sum_{n=0}^\infty b_n$ is the series $\sum_{n=0}^\infty c_n$ where
$c_n=\sum_{k=0}^n a_k\,b_{n-k}$ for each $n\ge 0$.

Under suitable hypotheses, the Cauchy product represents multiplication of sums; for instance, if both series are {{< knowl id="absolutely-convergent-series" text="absolutely convergent" >}} then the Cauchy product converges and sums to the product of the two sums, and {{< knowl id="mertens-theorem" text="Mertens' theorem" >}} gives a common sufficient condition beyond absolute convergence. Cauchy products are especially natural when multiplying {{< knowl id="power-series" text="power series" >}}.

**Examples:**
- If $a_n=b_n=r^n$ with $|r|<1$, then $c_n=\sum_{k=0}^n r^k r^{n-k}=(n+1)r^n$, so $\left(\sum_{n=0}^\infty r^n\right)^2=\sum_{n=0}^\infty (n+1)r^n$.
- If $a_n=b_n=1$ for all $n$, then $c_n=n+1$, so the Cauchy product is $\sum_{n=0}^\infty (n+1)$ (a divergent series).
