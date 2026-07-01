+++
id = "real-analysis/differentiability-criterion"
title = "Differentiability criterion"
kind = "knowl"
summary = "Characterization of differentiability via a best linear approximation."
aliases = ["differentiability-criterion", "Differentiability criterion"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/differentiability-criterion.md"
+++

**Differentiability criterion:** Let $U\subseteq\mathbb R^k$ be an [[topology/open-set|open set]], let $f:U\to\mathbb R^m$, and fix $a\in U$. The following are equivalent:

1. $f$ is [[real-analysis/differentiable-map|differentiable at]] $a$ (in the [[real-analysis/frechet-derivative|Fréchet]] sense).
2. There exists a [[linear-algebra/linear-map|linear map]] $A:\mathbb R^k\to\mathbb R^m$ such that
   $$
   \lim_{h\to 0}\frac{\|f(a+h)-f(a)-Ah\|}{\|h\|}=0.
   $$

In this case, $A$ is unique and is denoted $Df(a)$.

This formulation says that differentiability is exactly the existence of a first-order linear approximation with an error term that is $o(\|h\|)$. In the one-dimensional case $k=m=1$, it is equivalent to the existence of the usual [[real-analysis/derivative|derivative]] at $a$.
