+++
id = "real-analysis/term-by-term-integration"
title = "Term-by-term integration of a power series"
kind = "knowl"
summary = "Inside its radius of convergence, a power series can be integrated by integrating each term."
aliases = ["term-by-term-integration", "Term-by-term integration of a power series"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/term-by-term-integration.md"
+++

**Term-by-term integration (power series):** Let $\sum_{n=0}^\infty a_n(x-x_0)^n$ be a [[real-analysis/power-series|power series]] with radius of convergence $R>0$, and define
$$
f(x)=\sum_{n=0}^\infty a_n(x-x_0)^n \qquad (|x-x_0|<R).
$$

Then for every $x$ with $|x-x_0|<R$,
$$
\int_{x_0}^{x} f(t)\,dt \;=\; \sum_{n=0}^\infty \frac{a_n}{n+1}(x-x_0)^{n+1}.
$$

Moreover, the series $\sum_{n=0}^\infty \frac{a_n}{n+1}(x-x_0)^{n+1}$ is a power series with the same radius of convergence $R$, and its derivative equals $f$ on $|x-x_0|<R$.

This is justified by [[real-analysis/power-series-uniform-convergence-on-compacts|uniform convergence of power series on compact subsets]] together with [[real-analysis/uniform-convergence-integration|interchanging uniform limits and integration]] for the [[real-analysis/riemann-integral|Riemann integral]].
