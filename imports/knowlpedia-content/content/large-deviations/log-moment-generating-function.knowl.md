+++
id = "large-deviations/log-moment-generating-function"
title = "Log moment generating function"
kind = "knowl"
summary = "The logarithm of the moment generating function, viewed as a convex functional of the parameter."
aliases = ["log-moment-generating-function", "Log moment generating function"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/log-moment-generating-function.md"
+++

A **log moment generating function** (log-MGF) of an $\mathbb R^d$-valued [[probability/random-variable|random variable]] $X$ is the function $\Lambda:\mathbb R^d\to(-\infty,\infty]$ defined by
$$
\Lambda(\theta)=\log \mathbb E\big[e^{\langle \theta, X\rangle}\big],
$$

where $\langle\theta,X\rangle$ is the Euclidean inner product and the expectation is taken in the sense of [[probability/expectation|expectation]]. Equivalently, if $\mu$ is the [[probability/distribution-law|law]] of $X$, then
$$
\Lambda(\theta)=\log\int_{\mathbb R^d} e^{\langle\theta,x\rangle}\,\mu(dx),
$$
where the integral is a special case of the [[measure-theory/lebesgue-integral|Lebesgue integral]].

The log-MGF is a central object in large deviations: it is convex and encodes exponential moment growth, and its convex dual gives the [[large-deviations/cramer-transform|Cramér transform]]. In particular, for sums of an [[probability/iid-sequence|i.i.d. sequence]], the log-MGF is the starting point for [[large-deviations/cramers-theorem|Cramér's theorem]] and the [[large-deviations/gartner-ellis-theorem|Gärtner–Ellis theorem]].

**Examples:**
- If $X\sim \mathcal N(0,\sigma^2)$ on $\mathbb R$, then $\Lambda(\theta)=\frac{\sigma^2\theta^2}{2}$ for all $\theta\in\mathbb R$.
- If $X\sim \mathrm{Bernoulli}(p)$ on $\{0,1\}$, then $\Lambda(\theta)=\log\big((1-p)+p e^{\theta}\big)$ for all $\theta\in\mathbb R$.
