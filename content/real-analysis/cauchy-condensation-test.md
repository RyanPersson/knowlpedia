---
title: "Cauchy condensation test"
description: "A convergence test for nonincreasing nonnegative series using dyadic subsequences."
---

**Cauchy condensation test:** Let $(a_n)$ be a nonincreasing sequence of real numbers with $a_n\ge 0$. Then the {{< knowl id="series" text="series" >}} $\sum_{n=1}^\infty a_n$ {{< knowl id="convergent-series" text="converges" >}} if and only if the condensed series
\[
\sum_{k=0}^\infty 2^k\,a_{2^k}
\]
converges.

This test is especially effective for borderline cases where comparison with $\sum 1/n^p$ is delicate; it is often used alongside the {{< knowl id="integral-test" text="integral test" >}} and the {{< knowl id="comparison-test" text="comparison test" >}}.
