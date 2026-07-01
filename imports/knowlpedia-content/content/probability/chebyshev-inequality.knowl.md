+++
id = "probability/chebyshev-inequality"
title = "Chebyshev's inequality"
kind = "knowl"
summary = "Upper bound on deviation probability using variance."
aliases = ["chebyshev-inequality", "Chebyshev's inequality"]
domains = ["probability"]
legacy_source_path = "probability/chebyshev-inequality.md"
+++

**Chebyshev's inequality:** Let $X$ be a [[probability/random-variable|random variable]] with [[probability/expectation|expectation]] $\mu=\mathbb{E}[X]$ and finite [[probability/variance|variance]] $\sigma^2=\mathrm{Var}(X)$. Then for every $t>0$,
$$
\mathbb{P}\bigl(|X-\mu|\ge t\bigr)\le \frac{\sigma^2}{t^2}.
$$

Equivalently, for every $k>0$,
$$
\mathbb{P}\bigl(|X-\mu|\ge k\sigma\bigr)\le \frac{1}{k^2}.
$$

Here $\mathbb{P}$ denotes the [[probability/probability-measure|probability measure]] on the underlying [[probability/probability-space|probability space]]. Chebyshev's inequality is a direct consequence of [[probability/markov-inequality|Markov's inequality]] applied to $(X-\mu)^2$, and it is a standard tool for proving the [[probability/weak-law-large-numbers|weak law of large numbers]].
