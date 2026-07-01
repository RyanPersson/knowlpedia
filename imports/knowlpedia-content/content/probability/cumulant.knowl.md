+++
id = "probability/cumulant"
title = "Cumulant"
kind = "knowl"
summary = "A numerical summary of a distribution given by derivatives of the cumulant generating function at zero."
aliases = ["cumulant"]
domains = ["probability"]
legacy_source_path = "probability/cumulant.md"
+++

A **cumulant** (of order $n$) of a [[probability/random-variable|random variable]] $X$ is the number
$$
\kappa_n(X) \;=\; K_X^{(n)}(0),
$$

provided the [[probability/cumulant-generating-function|cumulant generating function]] $K_X$ exists in a neighborhood of $0$ and is $n$ times differentiable at $0$. The first two cumulants are $\kappa_1(X)=\mathbb{E}[X]$ and $\kappa_2(X)=\mathrm{Var}(X)$, linking cumulants to [[probability/expectation|expectation]] and [[probability/variance|variance]]. Cumulants are additive over sums of [[probability/independence-random-variables|independent random variables]] (when defined), which makes them useful for studying distributional limits and approximations.

**Examples:**
- If $X\sim \mathcal{N}(\mu,\sigma^2)$, then $\kappa_1(X)=\mu$, $\kappa_2(X)=\sigma^2$, and $\kappa_n(X)=0$ for all $n\ge 3$.
- If $X\sim \mathrm{Bernoulli}(p)$, then $\kappa_1(X)=p$, $\kappa_2(X)=p(1-p)$, and $\kappa_3(X)=p(1-p)(1-2p)$.
