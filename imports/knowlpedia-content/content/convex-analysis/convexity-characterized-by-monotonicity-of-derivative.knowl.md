+++
id = "convex-analysis/convexity-characterized-by-monotonicity-of-derivative"
title = "Convexity characterized by monotonicity of the derivative"
kind = "knowl"
summary = "A differentiable function on an interval is convex iff its derivative is nondecreasing"
aliases = ["convexity-characterized-by-monotonicity-of-derivative", "Convexity characterized by monotonicity of the derivative"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convexity-characterized-by-monotonicity-of-derivative.md"
+++

**Theorem.**
Let $f:I\to\mathbb{R}$ be differentiable on a nonempty open interval $I\subset\mathbb{R}$. Then $f$ is [[convex-analysis/convex-function-via-epigraph|convex]] on $I$ if and only if $f'$ is nondecreasing on $I$.

**Context.** This provides a practical test for convexity in one variable and connects geometric convexity with calculus.

**Proof sketch.**
- If $f$ is convex, apply [[convex-analysis/slope-inequalities-for-convex-functions|slope inequalities]] and take limits as $x\downarrow a$ and $x\uparrow b$ to get $f'(a)\le f'(b)$ for $a<b$.
- If $f'$ is nondecreasing, then for $a<b$ the mean value theorem implies the secant slope $(f(b)-f(a))/(b-a)$ lies between values of $f'$, giving Jensen's inequality and hence convexity.
