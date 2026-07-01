+++
id = "real-analysis/cauchy-product"
title = "Cauchy product"
kind = "knowl"
summary = "A convolution-style product of two series."
aliases = ["cauchy-product", "Cauchy product"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/cauchy-product.md"
+++

A **Cauchy product** of two series $\sum_{n=0}^\infty a_n$ and $\sum_{n=0}^\infty b_n$ is the series $\sum_{n=0}^\infty c_n$ where
$c_n=\sum_{k=0}^n a_k\,b_{n-k}$ for each $n\ge 0$.

Under suitable hypotheses, the Cauchy product represents multiplication of sums; for instance, if both series are [[real-analysis/absolutely-convergent-series|absolutely convergent]] then the Cauchy product converges and sums to the product of the two sums, and [[real-analysis/mertens-theorem|Mertens' theorem]] gives a common sufficient condition beyond absolute convergence. Cauchy products are especially natural when multiplying [[real-analysis/power-series|power series]].

**Examples:**
- If $a_n=b_n=r^n$ with $|r|<1$, then $c_n=\sum_{k=0}^n r^k r^{n-k}=(n+1)r^n$, so $\left(\sum_{n=0}^\infty r^n\right)^2=\sum_{n=0}^\infty (n+1)r^n$.
- If $a_n=b_n=1$ for all $n$, then $c_n=n+1$, so the Cauchy product is $\sum_{n=0}^\infty (n+1)$ (a divergent series).
