+++
id = "convex-analysis/convexity-via-nonnegative-second-derivative"
title = "Convexity via nonnegative second derivative"
kind = "knowl"
summary = "A twice differentiable function is convex iff f''≥0 on the interval"
aliases = ["convexity-via-nonnegative-second-derivative", "Convexity via nonnegative second derivative"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convexity-via-nonnegative-second-derivative.md"
+++

**Corollary.**
Let $f:I\to\mathbb{R}$ be twice differentiable on a nonempty open interval $I\subset\mathbb{R}$. Then $f$ is convex on $I$ if and only if
$$
f''(x)\ge 0 \quad \text{for all }x\in I.
$$

**Connection.** This follows from [[convex-analysis/convexity-characterized-by-monotonicity-of-derivative|convexity ⇔ monotone derivative]], since $f''\ge 0$ is equivalent to $f'$ being nondecreasing.
