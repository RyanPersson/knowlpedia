+++
id = "real-analysis/bounded-derivative-implies-uniform-continuity"
title = "Bounded derivative implies uniform continuity"
kind = "knowl"
summary = "A differentiable function with bounded derivative is Lipschitz, hence uniformly continuous."
aliases = ["bounded-derivative-implies-uniform-continuity", "Bounded derivative implies uniform continuity"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/bounded-derivative-implies-uniform-continuity.md"
+++

**Bounded derivative implies uniform continuity:** Let $I\subseteq\mathbb R$ be an [[real-analysis/interval|interval]] and let $f:I\to\mathbb R$ be [[real-analysis/differentiability-1d|differentiable]] on $I$. If there is a constant $M$ such that $|f'(t)|\le M$ for all $t\in I$, then for all $x,y\in I$,
$$
|f(x)-f(y)|\le M|x-y|.
$$

Consequently, $f$ is Lipschitz and in particular uniformly continuous on $I$.

This estimate is a direct application of the [[real-analysis/mean-value-theorem|mean value theorem]]. It is the one-dimensional special case of the [[real-analysis/mean-value-inequality|mean value inequality]] for differentiable maps.
