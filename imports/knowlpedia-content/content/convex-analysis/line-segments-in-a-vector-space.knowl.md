+++
id = "convex-analysis/line-segments-in-a-vector-space"
title = "Line segments in a vector space"
kind = "knowl"
summary = "Segments are sets of convex combinations of two points"
aliases = ["line-segments-in-a-vector-space", "Line segments in a vector space"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/line-segments-in-a-vector-space.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $a,b\in X$.

- The **closed line segment** joining $a$ and $b$ is
$$
[a,b]:=\{\lambda a+(1-\lambda)b:\lambda\in[0,1]\}.
$$
- The **open segment** is
$$
(a,b):=\{\lambda a+(1-\lambda)b:\lambda\in(0,1)\}.
$$

- The **half-open segments** are $[a,b):=\{\lambda a+(1-\lambda)b:\lambda\in(0,1]\}$ and $(a,b]:=\{\lambda a+(1-\lambda)b:\lambda\in[0,1)\}$.

**Context.** A set is [[convex-analysis/convex-set|convex]] exactly when it contains $[a,b]$ for every $a,b$ in the set.

**Examples:**
- In $X=\mathbb{R}$, $[a,b]$ is the usual interval between $a$ and $b$.
- In $X=\mathbb{R}^2$, $[a,b]$ is the straight segment in the plane from $a$ to $b$.
