+++
id = "probability/strong-law-large-numbers"
title = "Strong law of large numbers"
kind = "knowl"
summary = "Sample averages of iid variables converge almost surely to the mean."
aliases = ["strong-law-large-numbers", "Strong law of large numbers"]
domains = ["probability"]
legacy_source_path = "probability/strong-law-large-numbers.md"
+++

**Strong law of large numbers:** Let $(X_n)_{n\ge 1}$ be an [[probability/iid-sequence|iid sequence]] of [[probability/random-variable|random variables]] such that $\mathbb{E}[|X_1|]<\infty$, and let [[probability/expectation|expectation]] $\mu=\mathbb{E}[X_1]$. Define the sample mean
$$
\overline{X}_n=\frac{1}{n}\sum_{k=1}^n X_k.
$$
Then
$$
\mathbb{P}\!\left(\lim_{n\to\infty}\overline{X}_n=\mu\right)=1,
$$

i.e., $\overline{X}_n\to\mu$ almost surely.

This strengthens the [[probability/weak-law-large-numbers|weak law of large numbers]] by replacing convergence in probability with almost-sure convergence. The phrase “almost surely” is the probability-theory analogue of [[measure-theory/convergence-almost-everywhere|almost-everywhere convergence]] with respect to the [[probability/probability-measure|probability measure]].
