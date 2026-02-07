---
title: "Ratio Test"
description: "A series converges absolutely if successive terms shrink by a uniform factor less than one."
---

**Ratio test:** Let $\sum_{n=1}^\infty a_n$ be a {{< knowl id="series" text="series" >}} with $a_n\ne 0$ for all sufficiently large $n$, and define
\[
L=\limsup_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|.
\]
- If $L<1$, then $\sum a_n$ is {{< knowl id="absolutely-convergent-series" text="absolutely convergent" >}} (hence convergent).
- If $L>1$ (including $L=\infty$), then $\sum a_n$ is {{< knowl id="divergent-series" text="divergent" >}}.
- If $L=1$, the test is inconclusive.

The ratio test is particularly effective for factorials, exponentials, and power-series-like terms, and it is closely related to the {{< knowl id="root-test" text="root test" >}} and the {{< knowl id="cauchy-hadamard-theorem" text="Cauchy–Hadamard theorem" >}} for {{< knowl id="power-series" text="power series" >}}.
