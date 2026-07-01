+++
id = "probability/weak-law-large-numbers"
title = "Weak law of large numbers"
kind = "knowl"
summary = "Sample averages of iid variables converge in probability to the mean."
aliases = ["weak-law-large-numbers", "Weak law of large numbers"]
domains = ["probability"]
legacy_source_path = "probability/weak-law-large-numbers.md"
+++

**Weak law of large numbers:** Let $(X_n)_{n\ge 1}$ be an [[probability/iid-sequence|iid sequence]] of [[probability/random-variable|random variables]] with [[probability/expectation|expectation]] $\mu=\mathbb{E}[X_1]$ and finite [[probability/variance|variance]] $\mathrm{Var}(X_1)<\infty$. Define the sample mean
$$
\overline{X}_n=\frac{1}{n}\sum_{k=1}^n X_k.
$$

Then for every $\varepsilon>0$,
$$
\mathbb{P}\bigl(|\overline{X}_n-\mu|>\varepsilon\bigr)\to 0
\quad\text{as } n\to\infty.
$$

This is a convergence-in-probability statement on the underlying [[probability/probability-space|probability space]]. A standard proof uses [[probability/chebyshev-inequality|Chebyshev's inequality]] applied to $\overline{X}_n$, and the result is weaker than the [[probability/strong-law-large-numbers|strong law of large numbers]], which upgrades the mode of convergence.
