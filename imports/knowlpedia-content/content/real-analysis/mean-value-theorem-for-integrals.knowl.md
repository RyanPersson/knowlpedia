+++
id = "real-analysis/mean-value-theorem-for-integrals"
title = "Mean value theorem for integrals"
kind = "knowl"
summary = "A continuous function attains its average value somewhere on the interval."
aliases = ["mean-value-theorem-for-integrals", "Mean value theorem for integrals"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/mean-value-theorem-for-integrals.md"
+++

**Mean value theorem for integrals:** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be continuous. Then there exists $c\in[a,b]$ such that
$$
\int_a^b f(x)\,dx = f(c)\,(b-a).
$$

Equivalently, the average value $\frac{1}{b-a}\int_a^b f(x)\,dx$ is achieved by $f$ at some point; this relies on the [[real-analysis/intermediate-value-theorem|intermediate value theorem]] together with existence of the [[real-analysis/riemann-integral|Riemann integral]] for continuous functions.
