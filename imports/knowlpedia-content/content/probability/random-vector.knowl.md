+++
id = "probability/random-vector"
title = "Random vector"
kind = "knowl"
summary = "A measurable map from a probability space into a finite-dimensional real vector space."
aliases = ["random-vector", "Random vector"]
domains = ["probability"]
legacy_source_path = "probability/random-vector.md"
+++

A **random vector** is a [[measure-theory/measurable-function|measurable function]] $X:(\Omega,\mathcal F)\to(\mathbb R^d,\mathcal B(\mathbb R^d))$ defined on a [[probability/probability-space|probability space]] $(\Omega,\mathcal F,\mathbb P)$, where $\mathcal B(\mathbb R^d)$ is the Borel $\sigma$-algebra on $\mathbb R^d$.

Equivalently, $X=(X_1,\dots,X_d)$ where each coordinate $X_i$ is a [[probability/random-variable|random variable]]; conversely, any $d$-tuple of random variables defines a random vector by bundling them into a single map.

**Examples:**
- Let $\Omega=[0,1]$ with $\mathbb P$ the uniform distribution, and define $X(\omega)=(\omega,\omega^2)\in\mathbb R^2$. Then $X$ is a random vector in $\mathbb R^2$.
- Roll two fair six-sided dice and let $X=(D_1,D_2)\in\{1,\dots,6\}^2$. This pair-valued map is a random vector (taking values in a finite subset of $\mathbb R^2$).
