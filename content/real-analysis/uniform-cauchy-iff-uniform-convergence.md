---
title: "Uniform Cauchy criterion"
description: "For functions into a complete metric space, uniform convergence is equivalent to being uniformly Cauchy."
---

**Uniform Cauchy criterion:** Let $E$ be a set and let $(Y,\rho)$ be a {{< knowl id="complete-metric-space" section="topology" text="complete metric space" >}}. A sequence of functions $f_n:E\to Y$ converges {{< knowl id="uniform-convergence" text="uniformly" >}} on $E$ if and only if it is {{< knowl id="uniform-cauchy" text="uniformly Cauchy" >}}, meaning: for every $\varepsilon>0$ there exists $N$ such that for all $m,n\ge N$ and all $x\in E$,
\[
\rho\bigl(f_n(x),f_m(x)\bigr)<\varepsilon.
\]

Equivalently, uniform convergence is exactly convergence in the {{< knowl id="uniform-metric" text="uniform metric" >}} (and, for bounded real-valued functions, in the {{< knowl id="supremum-norm" text="supremum norm" >}}).
