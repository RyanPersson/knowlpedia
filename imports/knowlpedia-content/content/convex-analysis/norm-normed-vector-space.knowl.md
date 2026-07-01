+++
id = "convex-analysis/norm-normed-vector-space"
title = "Norm and normed vector space"
kind = "knowl"
summary = "A norm assigns lengths to vectors and induces a metric"
aliases = ["norm-normed-vector-space", "Norm and normed vector space"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/norm-normed-vector-space.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] over $\mathbb{R}$ (or $\mathbb{C}$). A **norm** on $X$ is a function $\|\cdot\|:X\to[0,\infty)$ such that for all $x,y\in X$ and scalars $\alpha$:

1. **Positive definiteness:** $\|x\|=0$ iff $x=0$.
2. **Absolute homogeneity:** $\|\alpha x\|=|\alpha|\,\|x\|$.
3. **Triangle inequality:** $\|x+y\|\le \|x\|+\|y\|$.

A pair $(X,\|\cdot\|)$ is called a **normed vector space**.

**Context.** Norms provide a quantitative notion of size. Via [[convex-analysis/norm-induces-a-metric-and-conversely|the induced metric]], normed spaces are a fundamental class of metric spaces used to define convergence, continuity, and completeness.

**Examples:**
- On $\mathbb{R}^n$, $\|x\|_2=\big(\sum_{i=1}^n x_i^2\big)^{1/2}$ is a norm (Euclidean norm).
- On $\mathbb{R}^n$, $\|x\|_1=\sum_{i=1}^n |x_i|$ and $\|x\|_\infty=\max_i |x_i|$ are norms.
- On the space $C([0,1])$ of continuous functions, $\|f\|_\infty=\max_{t\in[0,1]}|f(t)|$ defines a norm.
