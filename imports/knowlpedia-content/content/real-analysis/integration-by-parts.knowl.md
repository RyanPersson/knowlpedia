+++
id = "real-analysis/integration-by-parts"
title = "Integration by parts"
kind = "knowl"
summary = "An identity relating the integral of a product to boundary terms and another integral."
aliases = ["integration-by-parts", "Integration by parts"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/integration-by-parts.md"
+++

**Integration by parts:** Let $a<b$ and let $u,v:[a,b]\to\mathbb{R}$ be functions that are [[real-analysis/differentiability-1d|differentiable]] on $[a,b]$, with $u'$ and $v'$ [[real-analysis/riemann-integrable-function|Riemann integrable]] on $[a,b]$. Then
$$
\int_a^b u(x)\,v'(x)\,dx = u(b)v(b)-u(a)v(a) - \int_a^b u'(x)\,v(x)\,dx.
$$

This is the integral form of the product rule from [[real-analysis/differentiation-rules|differentiation rules]], typically justified using [[real-analysis/fundamental-theorem-of-calculus-ii|fundamental theorem of calculus II]].
