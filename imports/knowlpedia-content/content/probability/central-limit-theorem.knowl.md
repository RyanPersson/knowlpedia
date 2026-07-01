+++
id = "probability/central-limit-theorem"
title = "Central limit theorem"
kind = "knowl"
summary = "The classical limit theorem stating that normalized sums of i.i.d. variables converge in distribution to a normal law."
aliases = ["central-limit-theorem", "Central limit theorem"]
domains = ["probability"]
legacy_source_path = "probability/central-limit-theorem.md"
+++

**Central limit theorem (i.i.d. version):** Let $(X_i)_{i\ge 1}$ be an [[probability/iid-sequence|i.i.d. sequence]] of real-valued [[probability/random-variable|random variables]] with $\mathbb{E}[X_1]=\mu$ and $\mathrm{Var}(X_1)=\sigma^2$ where $0<\sigma^2<\infty$. Define $S_n=\sum_{i=1}^n X_i$. Then
\[
\frac{S_n-n\mu}{\sigma\sqrt{n}} \Rightarrow \mathcal{N}(0,1)\quad\text{as }n\to\infty,
\]
where $\Rightarrow$ denotes convergence in distribution.

The theorem connects [[probability/expectation|expectation]] and [[probability/variance|variance]] to the asymptotic [[probability/distribution-law|distribution (law)]] of sums, and it underlies normal approximations used throughout probability and statistics.
