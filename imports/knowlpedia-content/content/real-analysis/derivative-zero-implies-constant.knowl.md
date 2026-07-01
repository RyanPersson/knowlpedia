+++
id = "real-analysis/derivative-zero-implies-constant"
title = "Derivative zero implies constant"
kind = "knowl"
summary = "If the derivative of a differentiable function is zero everywhere on an interval, the function is constant."
aliases = ["derivative-zero-implies-constant", "Derivative zero implies constant"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/derivative-zero-implies-constant.md"
+++

**Derivative zero implies constant:** Let $I\subseteq\mathbb{R}$ be an [[real-analysis/interval|interval]], and let $f:I\to\mathbb{R}$ be [[real-analysis/differentiability-1d|differentiable]] on $I$. If
$$
f'(x)=0 \quad \text{for all } x\in I,
$$

then $f$ is constant on $I$.

This is a direct application of the [[real-analysis/mean-value-theorem|mean value theorem]]: the derivative controls differences $f(y)-f(x)$ on intervals. It can be viewed as a special case of [[real-analysis/derivative-sign-implies-monotonicity|derivative sign implies monotonicity]] applied in both directions.
