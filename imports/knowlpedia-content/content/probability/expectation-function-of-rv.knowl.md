+++
id = "probability/expectation-function-of-rv"
title = "Expectation of a function of a random variable"
kind = "knowl"
summary = "Compute the expectation of a transformed random variable using the distribution of the original."
aliases = ["expectation-function-of-rv", "Expectation of a function of a random variable"]
domains = ["probability"]
legacy_source_path = "probability/expectation-function-of-rv.md"
+++

**Law of the unconscious statistician:** Let $X:\Omega\to S$ be a [[probability/random-variable|random variable]] with [[probability/distribution-law|distribution (law)]] $\mu_X$ on $(S,\mathcal S)$. If $g:S\to\mathbb R$ is [[measure-theory/measurable-function|measurable]] and $g(X)$ is integrable, then
$$
\mathbb E[g(X)] = \int_\Omega g(X(\omega))\,d\mathbb P(\omega) = \int_S g(x)\,\mu_X(dx).
$$

This identity lets you compute expectations by integrating against the distribution of $X$ rather than over the original [[probability/probability-space|probability space]]. When $\mu_X$ has a density with respect to [[measure-theory/lebesgue-measure|Lebesgue measure]] (via the [[probability/radon-nikodym-theorem|Radon–Nikodym theorem]]), the right-hand side becomes an ordinary integral of $g(x)$ against that density.
