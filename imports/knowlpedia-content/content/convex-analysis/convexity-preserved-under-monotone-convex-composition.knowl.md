+++
id = "convex-analysis/convexity-preserved-under-monotone-convex-composition"
title = "Convexity Preserved Under Monotone Convex Composition"
kind = "knowl"
summary = "If f is convex and φ is convex and nondecreasing, then φ∘f is convex"
aliases = ["convexity-preserved-under-monotone-convex-composition", "Convexity Preserved Under Monotone Convex Composition"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convexity-preserved-under-monotone-convex-composition.md"
+++

**Convexity Under Monotone Convex Composition**: Let $X$ be a [[linear-algebra/vector-space|vector space]]. Suppose $f:X\to\overline{\mathbb{R}}$ is [[convex-analysis/convex-function-via-epigraph|convex]] and $\phi:\mathbb{R}\to\overline{\mathbb{R}}$ is convex and nondecreasing on a convex set containing the range of $f$. Then the composition $\phi\circ f$ is convex on $X$.

This rule is a standard way to build convex penalties (e.g., $\phi(t)=e^t$ or $\phi(t)=t_+ := \max\{t,0\}$) from an existing convex function $f$.

**Proof sketch (idea):** Apply Jensen to $f$ to get $f(\lambda x+(1-\lambda)y)\le \lambda f(x)+(1-\lambda)f(y)$. Then use monotonicity of $\phi$ followed by Jensen for $\phi$.
