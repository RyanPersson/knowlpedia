+++
id = "probability/expectation"
title = "Expectation"
kind = "knowl"
summary = "The integral of a random variable with respect to the underlying probability measure."
aliases = ["expectation"]
domains = ["probability"]
legacy_source_path = "probability/expectation.md"
+++

An **expectation** of a [[probability/random-variable|random variable]] $X$ is the number
$$
\mathbb E[X]=\int_\Omega X(\omega)\,d\mathbb P(\omega),
$$

provided $X$ is integrable, i.e. $\int_\Omega |X|\,d\mathbb P<\infty$ (so $X$ is an $L^1$ random variable; see [[measure-theory/l1-function|L1 function]]).

This definition uses the [[measure-theory/lebesgue-integral|Lebesgue integral]] on the underlying [[probability/probability-space|probability space]]; expectation is the basic averaging operation underlying [[probability/variance|variance]], [[probability/covariance|covariance]], and many limit theorems.

**Examples:**
- If $X$ takes values $x_k$ with probabilities $p_k$ (countably many), then $\mathbb E[X]=\sum_k x_k p_k$ whenever $\sum_k |x_k|p_k<\infty$.
- If $X$ is uniform on $[0,1]$, then $\mathbb E[X]=\int_0^1 x\,dx=\tfrac12$.
