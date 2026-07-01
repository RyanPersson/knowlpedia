+++
id = "convex-analysis/youngs-inequality"
title = "Young's Inequality"
kind = "knowl"
summary = "A conjugate-exponent bound: |xy| is controlled by |x|^p/p + |y|^q/q"
aliases = ["youngs-inequality", "Young's Inequality"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/youngs-inequality.md"
+++

**Young's Inequality**: Let $p,q>1$ satisfy $\frac1p+\frac1q=1$. Then for all $x,y\in\mathbb{R}$,
$$
|xy|\le \frac{|x|^p}{p}+\frac{|y|^q}{q}.
$$

This inequality is a standard tool behind [[convex-analysis/holder-inequality-finite-sums|Hölder's inequality]], [[convex-analysis/holder-inequality-integrals|Hölder's inequality for integrals]], and many estimates in [[convex-analysis/convex-function-via-epigraph|convex analysis]]. In the lecture notes it is obtained from the [[convex-analysis/weighted-arithmeticgeometric-mean-inequality|weighted AM–GM inequality]] applied to $a=|x|^p$ and $b=|y|^q$.

**Examples:**
- If $p=q=2$, then $|xy|\le \frac{x^2}{2}+\frac{y^2}{2}$.
- If $p=3$ and $q=\frac32$, then $|xy|\le \frac{|x|^3}{3}+\frac{2|y|^{3/2}}{3}$.
