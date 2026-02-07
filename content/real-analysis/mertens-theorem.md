---
title: "Mertens' theorem"
description: "A condition ensuring the Cauchy product of two series converges to the product of their sums."
---

**Mertens' theorem:** Let $\sum_{n=0}^\infty a_n$ and $\sum_{n=0}^\infty b_n$ be series. Assume that $\sum_{n=0}^\infty a_n$ converges and that $\sum_{n=0}^\infty |b_n|$ converges. Define the {{< knowl id="cauchy-product" text="Cauchy product" >}} coefficients
\[
c_n=\sum_{k=0}^n a_k\,b_{n-k}.
\]
Then the series $\sum_{n=0}^\infty c_n$ converges, and its sum satisfies
\[
\sum_{n=0}^\infty c_n=\left(\sum_{n=0}^\infty a_n\right)\left(\sum_{n=0}^\infty b_n\right).
\]

This theorem explains when multiplication of sums is compatible with multiplication of series via Cauchy products, a key fact in manipulating {{< knowl id="power-series" text="power series" >}} and in results about {{< knowl id="term-by-term-operations" text="term-by-term operations" >}}.
