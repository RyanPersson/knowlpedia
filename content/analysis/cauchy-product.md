---
title: "Cauchy product of two series"
description: "The series formed by convolving coefficients of two given series."
---

Let $\sum_{n=0}^\infty a_n$ and $\sum_{n=0}^\infty b_n$ be series in $\mathbb{R}$ or $\mathbb{C}$. Their **Cauchy product** is the series $\sum_{n=0}^\infty c_n$ defined by
$$c_n := \sum_{k=0}^n a_k\, b_{n-k}\qquad (n\ge 0).$$

Cauchy products correspond to multiplication of power series and to discrete convolution. Convergence of the Cauchy product requires hypotheses (e.g., absolute convergence of one factor or suitable conditions such as Mertens' theorem).

**Examples:**
- If $a_n=b_n=1$ for all $n$, then $c_n=n+1$, so the Cauchy product is $\sum_{n=0}^\infty (n+1)$, which diverges.
- If $a_0=1$, $a_1=1$, $a_n=0$ for $n\ge 2$ and similarly for $b_n$, then $c_0=1$, $c_1=2$, $c_2=1$, $c_n=0$ for $n\ge 3$ (finite convolution).
- If $f(x)=\sum a_n x^n$ and $g(x)=\sum b_n x^n$, then formally $f(x)g(x)=\sum c_n x^n$ with $c_n$ as above.
