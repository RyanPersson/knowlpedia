+++
id = "real-analysis/derivative-sign-implies-monotonicity"
title = "Derivative sign implies monotonicity"
kind = "knowl"
summary = "A nonnegative derivative forces a function to be nondecreasing, and a nonpositive derivative forces it to be nonincreasing."
aliases = ["derivative-sign-implies-monotonicity", "Derivative sign implies monotonicity"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/derivative-sign-implies-monotonicity.md"
+++

**Derivative sign implies monotonicity:** Let $I\subseteq\mathbb{R}$ be an [[real-analysis/interval|interval]], and let $f:I\to\mathbb{R}$ be [[real-analysis/differentiability-1d|differentiable]] on $I$.

- If $f'(x)\ge 0$ for all $x\in I$, then $f$ is nondecreasing (monotone increasing) on $I$.
- If $f'(x)\le 0$ for all $x\in I$, then $f$ is nonincreasing (monotone decreasing) on $I$.

This is proved by applying the [[real-analysis/mean-value-theorem|mean value theorem]] on subintervals and interpreting the sign of the [[real-analysis/derivative|derivative]] as controlling slopes. The strict version is [[real-analysis/positive-derivative-implies-increasing|positive derivative implies increasing]], and the conclusion is a special case of being a [[real-analysis/monotone-function|monotone function]].
