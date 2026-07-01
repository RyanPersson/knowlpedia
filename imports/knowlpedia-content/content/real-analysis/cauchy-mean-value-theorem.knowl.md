+++
id = "real-analysis/cauchy-mean-value-theorem"
title = "Cauchy mean value theorem"
kind = "knowl"
summary = "A two-function mean value theorem relating ratios of increments to ratios of derivatives."
aliases = ["cauchy-mean-value-theorem", "Cauchy mean value theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/cauchy-mean-value-theorem.md"
+++

**Cauchy mean value theorem:** Let $f,g:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$ and [[real-analysis/differentiability-1d|differentiable]] on $(a,b)$. Assume $g'(x)\neq 0$ for all $x\in(a,b)$ and $g(b)\neq g(a)$. Then there exists $c\in(a,b)$ such that
$$
\frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)}.
$$

Taking $g(x)=x$ recovers the [[real-analysis/mean-value-theorem|mean value theorem]]. This theorem is the main tool behind [[real-analysis/lhopitals-rule|L'Hôpital's rule]] for indeterminate limits.
