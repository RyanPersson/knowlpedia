---
title: "Strong law of large numbers"
description: "Sample averages of iid variables converge almost surely to the mean."
---

**Strong law of large numbers:** Let $(X_n)_{n\ge 1}$ be an {{< knowl id="iid-sequence" text="iid sequence" >}} of {{< knowl id="random-variable" text="random variables" >}} such that $\mathbb{E}[|X_1|]<\infty$, and let {{< knowl id="expectation" text="expectation" >}} $\mu=\mathbb{E}[X_1]$. Define the sample mean
$$
\overline{X}_n=\frac{1}{n}\sum_{k=1}^n X_k.
$$
Then
$$
\mathbb{P}\!\left(\lim_{n\to\infty}\overline{X}_n=\mu\right)=1,
$$

i.e., $\overline{X}_n\to\mu$ almost surely.

This strengthens the {{< knowl id="weak-law-large-numbers" text="weak law of large numbers" >}} by replacing convergence in probability with almost-sure convergence. The phrase “almost surely” is the probability-theory analogue of {{< knowl id="convergence-almost-everywhere" section="measure-theory" text="almost-everywhere convergence" >}} with respect to the {{< knowl id="probability-measure" text="probability measure" >}}.
