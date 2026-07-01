+++
id = "real-analysis/darboux-theorem"
title = "Darboux's theorem"
kind = "knowl"
summary = "Derivatives satisfy the intermediate value property even when they are not continuous."
aliases = ["darboux-theorem", "Darboux's theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/darboux-theorem.md"
+++

**Darboux's theorem:** Let $I\subseteq\mathbb{R}$ be an [[real-analysis/interval|interval]], and let $f:I\to\mathbb{R}$ be [[real-analysis/differentiability-1d|differentiable]] on $I$. Then the derivative $f'$ has the intermediate value property: whenever $a<b$ are in $I$ and $y$ lies between $f'(a)$ and $f'(b)$, there exists $c\in(a,b)$ such that
$$
f'(c)=y.
$$

Thus $f'$ behaves like a function satisfying the [[real-analysis/intermediate-value-theorem|intermediate value theorem]], even though $f'$ need not be a [[topology/continuous-map|continuous map]] and may have [[real-analysis/discontinuity-point|points of discontinuity]].
