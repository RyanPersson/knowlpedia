---
title: "Convexity characterized by monotonicity of the derivative"
description: "A differentiable function on an interval is convex iff its derivative is nondecreasing"
---

**Theorem.**
Let $f:I\to\mathbb{R}$ be differentiable on a nonempty open interval $I\subset\mathbb{R}$. Then $f$ is {{< knowl id="convex-function-via-epigraph" text="convex" >}} on $I$ if and only if $f'$ is nondecreasing on $I$.

**Context.** This provides a practical test for convexity in one variable and connects geometric convexity with calculus.

**Proof sketch.**
- If $f$ is convex, apply {{< knowl id="slope-inequalities-for-convex-functions" text="slope inequalities" >}} and take limits as $x\downarrow a$ and $x\uparrow b$ to get $f'(a)\le f'(b)$ for $a<b$.
- If $f'$ is nondecreasing, then for $a<b$ the mean value theorem implies the secant slope $(f(b)-f(a))/(b-a)$ lies between values of $f'$, giving Jensen's inequality and hence convexity.
