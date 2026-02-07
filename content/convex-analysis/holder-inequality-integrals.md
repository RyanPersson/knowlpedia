---
title: "Hölder inequality (integrals)"
description: "∫|fg| ≤ (∫|f|^p)^(1/p)(∫|g|^q)^(1/q) for conjugate exponents"
---

**Proposition (Hölder inequality for integrals).**
Let $f,g:[a,b]\to\mathbb{R}$ be measurable functions with $f\in L^p[a,b]$ and $g\in L^q[a,b]$, where $p>1$, $q>1$, and $1/p+1/q=1$. Then
$$
\int_a^b |f(x)g(x)|\,dx
\le
\left(\int_a^b |f(x)|^p\,dx\right)^{1/p}
\left(\int_a^b |g(x)|^q\,dx\right)^{1/q}.
$$

**Context.** This is the continuous analogue of {{< knowl id="holder-inequality-finite-sums" text="Hölder's inequality for sums" >}} and is foundational for $L^p$ estimates and duality.

**Proof sketch.** Assume the right-hand side is finite and normalize so the $L^p$ and $L^q$ norms are 1. Apply the pointwise inequality from {{< knowl id="weighted-arithmeticgeometric-mean-inequality" text="weighted AM–GM" >}} (equivalently Young's inequality) to obtain $|f(x)g(x)|\le |f(x)|^p/p+|g(x)|^q/q$ almost everywhere, then integrate and rescale.
