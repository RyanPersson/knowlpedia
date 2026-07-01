+++
id = "real-analysis/interchange-limit-integral"
title = "Interchanging limit and integral"
kind = "knowl"
summary = "Under uniform convergence, the limit of Riemann integrals equals the Riemann integral of the limit."
aliases = ["interchange-limit-integral", "Interchanging limit and integral"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/interchange-limit-integral.md"
+++

**Interchanging limit and integral:** Let $f_n:[a,b]\to\mathbb{R}$ be [[real-analysis/riemann-integrable-function|Riemann integrable]] for every $n$, and suppose $f_n\to f$ [[real-analysis/uniform-convergence|uniformly]] on $[a,b]$. Then $f$ is [[real-analysis/riemann-integrable-function|Riemann integrable]] and
\[
\lim_{n\to\infty}\int_a^b f_n(x)\,dx \;=\; \int_a^b f(x)\,dx.
\]

This is a basic continuity property of the [[real-analysis/riemann-integral|Riemann integral]] with respect to uniform convergence, and it is the key step behind [[real-analysis/uniform-convergence-integration|term-by-term integration of uniformly convergent series]].
