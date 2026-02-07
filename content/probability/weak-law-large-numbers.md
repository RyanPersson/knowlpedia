---
title: "Weak law of large numbers"
description: "Sample averages of iid variables converge in probability to the mean."
---

**Weak law of large numbers:** Let $(X_n)_{n\ge 1}$ be an {{< knowl id="iid-sequence" text="iid sequence" >}} of {{< knowl id="random-variable" text="random variables" >}} with {{< knowl id="expectation" text="expectation" >}} $\mu=\mathbb{E}[X_1]$ and finite {{< knowl id="variance" text="variance" >}} $\mathrm{Var}(X_1)<\infty$. Define the sample mean
$$
\overline{X}_n=\frac{1}{n}\sum_{k=1}^n X_k.
$$

Then for every $\varepsilon>0$,
$$
\mathbb{P}\bigl(|\overline{X}_n-\mu|>\varepsilon\bigr)\to 0
\quad\text{as } n\to\infty.
$$

This is a convergence-in-probability statement on the underlying {{< knowl id="probability-space" text="probability space" >}}. A standard proof uses {{< knowl id="chebyshev-inequality" text="Chebyshev's inequality" >}} applied to $\overline{X}_n$, and the result is weaker than the {{< knowl id="strong-law-large-numbers" text="strong law of large numbers" >}}, which upgrades the mode of convergence.
