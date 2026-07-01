+++
id = "convex-analysis/uniqueness-of-limits-in-metric-spaces"
title = "Uniqueness of limits"
kind = "knowl"
summary = "A sequence in a metric space has at most one limit"
aliases = ["uniqueness-of-limits-in-metric-spaces", "Uniqueness of limits"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/uniqueness-of-limits-in-metric-spaces.md"
+++

**Proposition.**
A sequence in a [[convex-analysis/metric-metric-space|metric space]] has at most one limit.

More precisely: if $(x_n)$ converges to $a$ and also converges to $b$, then $a=b$.

**Proof sketch.** Fix $\varepsilon>0$. For large $n$, both $d(x_n,a)<\varepsilon/2$ and $d(x_n,b)<\varepsilon/2$. Then
$$
d(a,b)\le d(a,x_n)+d(x_n,b)<\varepsilon.
$$

Since this holds for all $\varepsilon>0$, the lemma [[convex-analysis/nonnegative-real-less-than-every-0-must-be-zero|nonnegative below every epsilon]] gives $d(a,b)=0$, hence $a=b$.
