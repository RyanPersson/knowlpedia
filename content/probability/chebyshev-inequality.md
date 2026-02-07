---
title: "Chebyshev's inequality"
description: "Upper bound on deviation probability using variance."
---

**Chebyshev's inequality:** Let $X$ be a {{< knowl id="random-variable" text="random variable" >}} with {{< knowl id="expectation" text="expectation" >}} $\mu=\mathbb{E}[X]$ and finite {{< knowl id="variance" text="variance" >}} $\sigma^2=\mathrm{Var}(X)$. Then for every $t>0$,
$$
\mathbb{P}\bigl(|X-\mu|\ge t\bigr)\le \frac{\sigma^2}{t^2}.
$$

Equivalently, for every $k>0$,
$$
\mathbb{P}\bigl(|X-\mu|\ge k\sigma\bigr)\le \frac{1}{k^2}.
$$

Here $\mathbb{P}$ denotes the {{< knowl id="probability-measure" text="probability measure" >}} on the underlying {{< knowl id="probability-space" text="probability space" >}}. Chebyshev's inequality is a direct consequence of {{< knowl id="markov-inequality" text="Markov's inequality" >}} applied to $(X-\mu)^2$, and it is a standard tool for proving the {{< knowl id="weak-law-large-numbers" text="weak law of large numbers" >}}.
