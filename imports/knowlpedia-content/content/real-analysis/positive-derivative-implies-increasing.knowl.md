+++
id = "real-analysis/positive-derivative-implies-increasing"
title = "Positive derivative implies increasing"
kind = "knowl"
summary = "If a differentiable function has positive derivative everywhere on an interval, then it is strictly increasing."
aliases = ["positive-derivative-implies-increasing", "Positive derivative implies increasing"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/positive-derivative-implies-increasing.md"
+++

**Positive derivative implies increasing:** Let $I\subseteq\mathbb{R}$ be an [[real-analysis/interval|interval]], and let $f:I\to\mathbb{R}$ be [[real-analysis/differentiability-1d|differentiable]] on $I$. If
$$
f'(x)>0 \quad \text{for all } x\in I,
$$

then $f$ is strictly increasing on $I$.

This follows from the [[real-analysis/mean-value-theorem|mean value theorem]] applied to pairs $x<y$ in $I$. The non-strict version is [[real-analysis/derivative-sign-implies-monotonicity|derivative sign implies monotonicity]].
