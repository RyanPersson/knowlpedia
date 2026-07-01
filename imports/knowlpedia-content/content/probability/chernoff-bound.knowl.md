+++
id = "probability/chernoff-bound"
title = "Chernoff bound"
kind = "knowl"
summary = "Exponential tail bound using moment generating functions."
aliases = ["chernoff-bound", "Chernoff bound"]
domains = ["probability"]
legacy_source_path = "probability/chernoff-bound.md"
+++

**Chernoff bound:** Let $X$ be a [[probability/random-variable|random variable]]. Suppose $\mathbb{E}[e^{tX}]<\infty$ for some $t>0$. Then for every real $a$ and every $t>0$ for which the expectation is finite,
$$
\mathbb{P}(X\ge a)\le e^{-ta}\,\mathbb{E}\!\left[e^{tX}\right].
$$
Equivalently,
$$
\mathbb{P}(X\ge a)\le \inf_{t>0} \; e^{-ta}\,\mathbb{E}\!\left[e^{tX}\right].
$$

Similarly, if $\mathbb{E}[e^{-tX}]<\infty$ for some $t>0$, then for every real $a$ and every such $t$,
$$
\mathbb{P}(X\le a)\le e^{ta}\,\mathbb{E}\!\left[e^{-tX}\right].
$$

This bound is obtained by applying [[probability/markov-inequality|Markov's inequality]] to the nonnegative random variable $e^{tX}$, and it is naturally expressed in terms of the [[probability/moment-generating-function|moment generating function]] of $X$.
