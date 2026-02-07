---
title: "Central limit theorem"
description: "The classical limit theorem stating that normalized sums of i.i.d. variables converge in distribution to a normal law."
---

**Central limit theorem (i.i.d. version):** Let $(X_i)_{i\ge 1}$ be an {{< knowl id="iid-sequence" text="i.i.d. sequence" >}} of real-valued {{< knowl id="random-variable" text="random variables" >}} with $\mathbb{E}[X_1]=\mu$ and $\mathrm{Var}(X_1)=\sigma^2$ where $0<\sigma^2<\infty$. Define $S_n=\sum_{i=1}^n X_i$. Then
\[
\frac{S_n-n\mu}{\sigma\sqrt{n}} \Rightarrow \mathcal{N}(0,1)\quad\text{as }n\to\infty,
\]
where $\Rightarrow$ denotes convergence in distribution.

The theorem connects {{< knowl id="expectation" text="expectation" >}} and {{< knowl id="variance" text="variance" >}} to the asymptotic {{< knowl id="distribution-law" text="distribution (law)" >}} of sums, and it underlies normal approximations used throughout probability and statistics.
