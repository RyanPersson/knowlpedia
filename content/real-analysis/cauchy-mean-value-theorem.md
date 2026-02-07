---
title: "Cauchy mean value theorem"
description: "A two-function mean value theorem relating ratios of increments to ratios of derivatives."
---

**Cauchy mean value theorem:** Let $f,g:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$ and {{< knowl id="differentiability-1d" text="differentiable" >}} on $(a,b)$. Assume $g'(x)\neq 0$ for all $x\in(a,b)$ and $g(b)\neq g(a)$. Then there exists $c\in(a,b)$ such that
$$
\frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)}.
$$

Taking $g(x)=x$ recovers the {{< knowl id="mean-value-theorem" text="mean value theorem" >}}. This theorem is the main tool behind {{< knowl id="lhopitals-rule" text="L'Hôpital's rule" >}} for indeterminate limits.
