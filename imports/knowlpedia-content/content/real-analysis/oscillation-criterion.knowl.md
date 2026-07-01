+++
id = "real-analysis/oscillation-criterion"
title = "Oscillation criterion for Riemann integrability"
kind = "knowl"
summary = "A bounded function is Riemann integrable exactly when its total oscillation can be made small by a partition."
aliases = ["oscillation-criterion", "Oscillation criterion for Riemann integrability"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/oscillation-criterion.md"
+++

**Oscillation criterion:** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be bounded. For a [[real-analysis/partition-of-an-interval|partition]] $P=\{a=x_0<x_1<\cdots<x_n=b\}$, let $\omega_i$ be the [[real-analysis/oscillation|oscillation]] of $f$ on the subinterval $[x_{i-1},x_i]$. Then $f$ is a [[real-analysis/riemann-integrable-function|Riemann integrable function]] on $[a,b]$ if and only if for every $\varepsilon>0$ there exists a partition $P$ such that
$$
\sum_{i=1}^n \omega_i\,(x_i-x_{i-1})<\varepsilon.
$$

This criterion is equivalent to the usual definition via [[real-analysis/upper-sum|upper sums]] and [[real-analysis/lower-sum|lower sums]], and it is especially useful for proving integrability results like [[real-analysis/riemann-integrability-finite-discontinuities|finite discontinuities imply integrability]].
