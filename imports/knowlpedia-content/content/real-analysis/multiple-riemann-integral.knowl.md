+++
id = "real-analysis/multiple-riemann-integral"
title = "Multiple Riemann integral"
kind = "knowl"
summary = "Riemann integration of a bounded function over a rectangular region in Euclidean space."
aliases = ["multiple-riemann-integral", "Multiple Riemann integral"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/multiple-riemann-integral.md"
+++

A **multiple Riemann integral** of a bounded function $f:R\to\mathbb{R}$ over a rectangle $R=\prod_{i=1}^n [a_i,b_i]\subset \mathbb{R}^n$ is a number $I\in\mathbb{R}$ such that for every $\varepsilon>0$ there exists $\delta>0$ with the property that for every rectangular partition of $R$ with mesh $<\delta$ and every choice of tags (sample points) $\xi_j$ in each subrectangle $R_j$, the corresponding Riemann sum
\[
S(f)=\sum_j f(\xi_j)\,\operatorname{vol}(R_j)
\]
satisfies $|S(f)-I|<\varepsilon$. In this case one writes $\int_R f = I$.

This extends the one-variable [[real-analysis/riemann-integral|Riemann integral]] by using partitions built from products of [[real-analysis/partition-of-an-interval|partitions of intervals]] (a product rectangle is a [[shared-foundations/cartesian-product|Cartesian product]] of intervals). The link with [[real-analysis/iterated-integral|iterated integrals]] is made precise by the [[real-analysis/fubini-theorem-riemann|Riemann–Fubini theorem]] under appropriate hypotheses.

**Examples:**
- If $f(x)\equiv c$ on $R$, then $\int_R f = c\,\operatorname{vol}(R)$.
- On $R=[-1,1]^n$, the function $f(x)=\mathbf{1}_{\{x_1>0\}}$ is Riemann integrable and $\int_R f = 2^{n-1}$ (the discontinuities lie on the hyperplane $x_1=0$).
