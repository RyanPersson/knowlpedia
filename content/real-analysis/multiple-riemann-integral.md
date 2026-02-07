---
title: "Multiple Riemann integral"
description: "Riemann integration of a bounded function over a rectangular region in Euclidean space."
---

A **multiple Riemann integral** of a bounded function $f:R\to\mathbb{R}$ over a rectangle $R=\prod_{i=1}^n [a_i,b_i]\subset \mathbb{R}^n$ is a number $I\in\mathbb{R}$ such that for every $\varepsilon>0$ there exists $\delta>0$ with the property that for every rectangular partition of $R$ with mesh $<\delta$ and every choice of tags (sample points) $\xi_j$ in each subrectangle $R_j$, the corresponding Riemann sum
\[
S(f)=\sum_j f(\xi_j)\,\operatorname{vol}(R_j)
\]
satisfies $|S(f)-I|<\varepsilon$. In this case one writes $\int_R f = I$.

This extends the one-variable {{< knowl id="riemann-integral" text="Riemann integral" >}} by using partitions built from products of {{< knowl id="partition-of-an-interval" text="partitions of intervals" >}} (a product rectangle is a {{< knowl id="cartesian-product" section="shared-foundations" text="Cartesian product" >}} of intervals). The link with {{< knowl id="iterated-integral" text="iterated integrals" >}} is made precise by the {{< knowl id="fubini-theorem-riemann" text="Riemann–Fubini theorem" >}} under appropriate hypotheses.

**Examples:**
- If $f(x)\equiv c$ on $R$, then $\int_R f = c\,\operatorname{vol}(R)$.
- On $R=[-1,1]^n$, the function $f(x)=\mathbf{1}_{\{x_1>0\}}$ is Riemann integrable and $\int_R f = 2^{n-1}$ (the discontinuities lie on the hyperplane $x_1=0$).
