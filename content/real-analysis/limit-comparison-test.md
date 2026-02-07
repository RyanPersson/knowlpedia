---
title: "Limit Comparison Test"
description: "Two positive series with asymptotically proportional terms converge or diverge together."
---

**Limit comparison test:** Let $\sum_{n=1}^\infty a_n$ and $\sum_{n=1}^\infty b_n$ be {{< knowl id="series" text="series" >}} with $a_n>0$ and $b_n>0$ for all sufficiently large $n$. Suppose the limit
\[
\lim_{n\to\infty}\frac{a_n}{b_n}=c
\]
exists and satisfies $0<c<\infty$. Then $\sum a_n$ converges if and only if $\sum b_n$ converges.

This is often used when the {{< knowl id="comparison-test" text="comparison test" >}} is too rigid, but one can identify the asymptotic size of $a_n$ relative to a known $b_n$ (such as a $p$-series or a geometric series).
