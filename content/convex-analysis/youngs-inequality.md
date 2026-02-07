---
title: "Young's Inequality"
description: "A conjugate-exponent bound: |xy| is controlled by |x|^p/p + |y|^q/q"
---

**Young's Inequality**: Let $p,q>1$ satisfy $\frac1p+\frac1q=1$. Then for all $x,y\in\mathbb{R}$,
$$
|xy|\le \frac{|x|^p}{p}+\frac{|y|^q}{q}.
$$

This inequality is a standard tool behind {{< knowl id="holder-inequality-finite-sums" text="Hölder's inequality" >}}, {{< knowl id="holder-inequality-integrals" text="Hölder's inequality for integrals" >}}, and many estimates in {{< knowl id="convex-function-via-epigraph" text="convex analysis" >}}. In the lecture notes it is obtained from the {{< knowl id="weighted-arithmeticgeometric-mean-inequality" text="weighted AM–GM inequality" >}} applied to $a=|x|^p$ and $b=|y|^q$.

**Examples:**
- If $p=q=2$, then $|xy|\le \frac{x^2}{2}+\frac{y^2}{2}$.
- If $p=3$ and $q=\frac32$, then $|xy|\le \frac{|x|^3}{3}+\frac{2|y|^{3/2}}{3}$.
