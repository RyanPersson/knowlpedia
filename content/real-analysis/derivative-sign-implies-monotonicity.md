---
title: "Derivative sign implies monotonicity"
description: "A nonnegative derivative forces a function to be nondecreasing, and a nonpositive derivative forces it to be nonincreasing."
---

**Derivative sign implies monotonicity:** Let $I\subseteq\mathbb{R}$ be an {{< knowl id="interval" text="interval" >}}, and let $f:I\to\mathbb{R}$ be {{< knowl id="differentiability-1d" text="differentiable" >}} on $I$.

- If $f'(x)\ge 0$ for all $x\in I$, then $f$ is nondecreasing (monotone increasing) on $I$.
- If $f'(x)\le 0$ for all $x\in I$, then $f$ is nonincreasing (monotone decreasing) on $I$.

This is proved by applying the {{< knowl id="mean-value-theorem" text="mean value theorem" >}} on subintervals and interpreting the sign of the {{< knowl id="derivative" text="derivative" >}} as controlling slopes. The strict version is {{< knowl id="positive-derivative-implies-increasing" text="positive derivative implies increasing" >}}, and the conclusion is a special case of being a {{< knowl id="monotone-function" text="monotone function" >}}.
