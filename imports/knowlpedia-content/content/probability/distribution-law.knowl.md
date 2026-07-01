+++
id = "probability/distribution-law"
title = "Distribution (law)"
kind = "knowl"
summary = "The probability measure induced by a random variable on its state space."
aliases = ["distribution-law", "Distribution (law)"]
domains = ["probability"]
legacy_source_path = "probability/distribution-law.md"
+++

A **distribution (law)** of a [[probability/random-variable|random variable]] $X:\Omega\to S$ (more generally, a measurable map into a measurable space $(S,\mathcal S)$) is the [[probability/probability-measure|probability measure]] $\mu_X$ on $(S,\mathcal S)$ defined by
$$
\mu_X(A)=\mathbb P(X\in A)\qquad\text{for all }A\in\mathcal S,
$$

where $X\in A$ abbreviates the event $\{\omega\in\Omega: X(\omega)\in A\}\in\mathcal F$.

This is the pushforward of $\mathbb P$ along $X$; it packages all probabilities of [[measure-theory/measurable-set|measurable sets]] in the state space into a single measure, and is often written $\mu_X=\mathbb P\circ X^{-1}$.

**Examples:**
- If $X$ is Bernoulli$(p)$ taking values in $\{0,1\}$, then $\mu_X(\{1\})=p$ and $\mu_X(\{0\})=1-p$.
- If $X$ is uniform on $[0,1]$, then $\mu_X((a,b))=b-a$ for $0\le a<b\le 1$ (equivalently, $\mu_X$ has density $1$ with respect to [[measure-theory/lebesgue-measure|Lebesgue measure]] on $[0,1]$).
