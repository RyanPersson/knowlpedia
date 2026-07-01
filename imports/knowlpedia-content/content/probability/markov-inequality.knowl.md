+++
id = "probability/markov-inequality"
title = "Markov inequality"
kind = "knowl"
summary = "An upper bound on the tail probability of a nonnegative random variable using its expectation."
aliases = ["markov-inequality", "Markov inequality"]
domains = ["probability"]
legacy_source_path = "probability/markov-inequality.md"
+++

**Markov inequality:** If $X$ is a nonnegative [[probability/random-variable|random variable]] and $a>0$, then
$$
\mathbb{P}(X \ge a) \;\le\; \frac{\mathbb{E}[X]}{a}.
$$

This is a basic tool for bounding [[probability/event-probability|event probabilities]] using [[probability/expectation|expectation]]. It directly implies the [[probability/chebyshev-inequality|Chebyshev inequality]] (by applying it to $(X-\mathbb{E}[X])^2$) and is also a starting point for exponential tail bounds such as the [[probability/chernoff-bound|Chernoff bound]].
