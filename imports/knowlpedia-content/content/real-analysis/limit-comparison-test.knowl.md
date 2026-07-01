+++
id = "real-analysis/limit-comparison-test"
title = "Limit Comparison Test"
kind = "knowl"
summary = "Two positive series with asymptotically proportional terms converge or diverge together."
aliases = ["limit-comparison-test", "Limit Comparison Test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-comparison-test.md"
+++

**Limit comparison test:** Let $\sum_{n=1}^\infty a_n$ and $\sum_{n=1}^\infty b_n$ be [[real-analysis/series|series]] with $a_n>0$ and $b_n>0$ for all sufficiently large $n$. Suppose the limit
\[
\lim_{n\to\infty}\frac{a_n}{b_n}=c
\]
exists and satisfies $0<c<\infty$. Then $\sum a_n$ converges if and only if $\sum b_n$ converges.

This is often used when the [[real-analysis/comparison-test|comparison test]] is too rigid, but one can identify the asymptotic size of $a_n$ relative to a known $b_n$ (such as a $p$-series or a geometric series).
