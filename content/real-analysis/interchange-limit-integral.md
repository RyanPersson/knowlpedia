---
title: "Interchanging limit and integral"
description: "Under uniform convergence, the limit of Riemann integrals equals the Riemann integral of the limit."
---

**Interchanging limit and integral:** Let $f_n:[a,b]\to\mathbb{R}$ be {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} for every $n$, and suppose $f_n\to f$ {{< knowl id="uniform-convergence" text="uniformly" >}} on $[a,b]$. Then $f$ is {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} and
\[
\lim_{n\to\infty}\int_a^b f_n(x)\,dx \;=\; \int_a^b f(x)\,dx.
\]

This is a basic continuity property of the {{< knowl id="riemann-integral" text="Riemann integral" >}} with respect to uniform convergence, and it is the key step behind {{< knowl id="uniform-convergence-integration" text="term-by-term integration of uniformly convergent series" >}}.
