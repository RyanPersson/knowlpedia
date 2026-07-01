+++
id = "real-analysis/mertens-theorem"
title = "Mertens' theorem"
kind = "knowl"
summary = "A condition ensuring the Cauchy product of two series converges to the product of their sums."
aliases = ["mertens-theorem", "Mertens' theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/mertens-theorem.md"
+++

**Mertens' theorem:** Let $\sum_{n=0}^\infty a_n$ and $\sum_{n=0}^\infty b_n$ be series. Assume that $\sum_{n=0}^\infty a_n$ converges and that $\sum_{n=0}^\infty |b_n|$ converges. Define the [[real-analysis/cauchy-product|Cauchy product]] coefficients
\[
c_n=\sum_{k=0}^n a_k\,b_{n-k}.
\]
Then the series $\sum_{n=0}^\infty c_n$ converges, and its sum satisfies
\[
\sum_{n=0}^\infty c_n=\left(\sum_{n=0}^\infty a_n\right)\left(\sum_{n=0}^\infty b_n\right).
\]

This theorem explains when multiplication of sums is compatible with multiplication of series via Cauchy products, a key fact in manipulating [[real-analysis/power-series|power series]] and in results about [[real-analysis/term-by-term-operations|term-by-term operations]].
