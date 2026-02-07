---
title: "Uniform convergence and integration"
description: "A uniformly convergent series of Riemann integrable functions may be integrated term by term."
---

**Uniform convergence and integration:** Let $f_n:[a,b]\to\mathbb{R}$ be {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} for all $n$, and let $s_N=\sum_{n=1}^N f_n$ be the partial sums. If $s_N\to s$ {{< knowl id="uniform-convergence" text="uniformly" >}} on $[a,b]$, then $s$ is {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} and
\[
\int_a^b s(x)\,dx \;=\; \lim_{N\to\infty}\int_a^b s_N(x)\,dx \;=\; \sum_{n=1}^\infty \int_a^b f_n(x)\,dx,
\]
where the series of real numbers on the right converges.

In applications, uniform convergence of $(s_N)$ is often established using the {{< knowl id="weierstrass-m-test" text="Weierstrass M-test" >}}.
