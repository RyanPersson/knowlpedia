+++
id = "convex-analysis/holder-inequality-integrals"
title = "Hölder inequality (integrals)"
kind = "knowl"
summary = "∫|fg| ≤ (∫|f|^p)^(1/p)(∫|g|^q)^(1/q) for conjugate exponents"
aliases = ["holder-inequality-integrals", "Hölder inequality (integrals)"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/holder-inequality-integrals.md"
+++

**Proposition (Hölder inequality for integrals).**
Let $f,g:[a,b]\to\mathbb{R}$ be measurable functions with $f\in L^p[a,b]$ and $g\in L^q[a,b]$, where $p>1$, $q>1$, and $1/p+1/q=1$. Then
$$
\int_a^b |f(x)g(x)|\,dx
\le
\left(\int_a^b |f(x)|^p\,dx\right)^{1/p}
\left(\int_a^b |g(x)|^q\,dx\right)^{1/q}.
$$

**Context.** This is the continuous analogue of [[convex-analysis/holder-inequality-finite-sums|Hölder's inequality for sums]] and is foundational for $L^p$ estimates and duality.

**Proof sketch.** Assume the right-hand side is finite and normalize so the $L^p$ and $L^q$ norms are 1. Apply the pointwise inequality from [[convex-analysis/weighted-arithmeticgeometric-mean-inequality|weighted AM–GM]] (equivalently Young's inequality) to obtain $|f(x)g(x)|\le |f(x)|^p/p+|g(x)|^q/q$ almost everywhere, then integrate and rescale.
