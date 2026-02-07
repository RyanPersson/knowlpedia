---
title: "Oscillation criterion for Riemann integrability"
description: "A bounded function is Riemann integrable exactly when its total oscillation can be made small by a partition."
---

**Oscillation criterion:** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be bounded. For a {{< knowl id="partition-of-an-interval" text="partition" >}} $P=\{a=x_0<x_1<\cdots<x_n=b\}$, let $\omega_i$ be the {{< knowl id="oscillation" text="oscillation" >}} of $f$ on the subinterval $[x_{i-1},x_i]$. Then $f$ is a {{< knowl id="riemann-integrable-function" text="Riemann integrable function" >}} on $[a,b]$ if and only if for every $\varepsilon>0$ there exists a partition $P$ such that
$$
\sum_{i=1}^n \omega_i\,(x_i-x_{i-1})<\varepsilon.
$$

This criterion is equivalent to the usual definition via {{< knowl id="upper-sum" text="upper sums" >}} and {{< knowl id="lower-sum" text="lower sums" >}}, and it is especially useful for proving integrability results like {{< knowl id="riemann-integrability-finite-discontinuities" text="finite discontinuities imply integrability" >}}.
