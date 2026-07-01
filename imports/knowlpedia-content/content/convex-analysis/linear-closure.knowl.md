+++
id = "convex-analysis/linear-closure"
title = "Linear Closure"
kind = "knowl"
summary = "The algebraic analogue of closure for subsets of vector spaces"
aliases = ["linear-closure", "Linear Closure"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/linear-closure.md"
+++

Let $X$ be a real [[linear-algebra/vector-space|vector space]] and let $\Omega\subset X$.

The **linear closure** of $\Omega$ is
$$
\operatorname{lin}(\Omega):=\Big\{x\in X\ \Big|\ \exists w\in\Omega \text{ with } [w,x)\subset \Omega\Big\},
$$

where $[w,x)$ denotes the half-open [[convex-analysis/line-segments-in-a-vector-space|line segment]]
$$
[w,x):=\{\lambda w+(1-\lambda)x\mid \lambda\in(0,1]\}.
$$

Equivalently, $x\in\operatorname{lin}(\Omega)$ iff there exists a point $w\in\Omega$ such that the entire segment from $w$ to $x$ (excluding $x$) lies in $\Omega$.

When $X$ is a [[convex-analysis/norm-normed-vector-space|normed vector space]] and $\Omega$ is [[convex-analysis/convex-set|convex]], we have
$$
\Omega \subset \operatorname{lin}(\Omega)\subset \overline{\Omega},
$$

where $\overline{\Omega}$ is the usual [[convex-analysis/closure-of-a-set|closure]]. See also [[convex-analysis/algebraic-interior-core|algebraic interior (core)]] for the dual notion.

**Examples:**
- If $\Omega$ is a linear subspace $L$, then $\operatorname{lin}(L)=L$.
