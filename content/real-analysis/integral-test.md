---
title: "Integral test"
description: "A convergence test that compares a nonnegative decreasing series to an improper integral."
---

**Integral test:** Let $f:[1,\infty)\to[0,\infty)$ be continuous and decreasing, and define $a_n=f(n)$. Then the {{< knowl id="series" text="series" >}} $\sum_{n=1}^\infty a_n$ {{< knowl id="convergent-series" text="converges" >}} if and only if the improper integral
\[
\int_1^\infty f(x)\,dx
\]
converges (is finite).

Moreover, for each integer $N\ge 1$ one has the remainder bounds
\[
\int_{N+1}^\infty f(x)\,dx \;\le\; \sum_{n=N+1}^\infty a_n \;\le\; \int_N^\infty f(x)\,dx.
\]

This test complements the {{< knowl id="comparison-test" text="comparison test" >}} for nonnegative series and is often paired with the {{< knowl id="cauchy-condensation-test" text="Cauchy condensation test" >}} for slowly varying terms.
