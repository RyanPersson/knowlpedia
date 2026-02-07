---
title: "Markov inequality"
description: "An upper bound on the tail probability of a nonnegative random variable using its expectation."
---

**Markov inequality:** If $X$ is a nonnegative {{< knowl id="random-variable" text="random variable" >}} and $a>0$, then
$$
\mathbb{P}(X \ge a) \;\le\; \frac{\mathbb{E}[X]}{a}.
$$

This is a basic tool for bounding {{< knowl id="event-probability" text="event probabilities" >}} using {{< knowl id="expectation" text="expectation" >}}. It directly implies the {{< knowl id="chebyshev-inequality" text="Chebyshev inequality" >}} (by applying it to $(X-\mathbb{E}[X])^2$) and is also a starting point for exponential tail bounds such as the {{< knowl id="chernoff-bound" text="Chernoff bound" >}}.
