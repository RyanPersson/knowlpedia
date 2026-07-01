+++
id = "convex-analysis/line-connecting-two-points"
title = "Line Connecting Two Points"
kind = "knowl"
summary = "The affine line through a and b: {λa+(1−λ)b : λ∈R}."
aliases = ["line-connecting-two-points", "Line Connecting Two Points"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/line-connecting-two-points.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $a,b\in X$. The **line connecting $a$ and $b$** is
$$
L[a,b]:=\{\lambda a+(1-\lambda)b\mid \lambda\in\mathbb{R}\}.
$$

This is the smallest [[convex-analysis/affine-set|affine set]] containing $\{a,b\}$ and is the affine analogue of the [[convex-analysis/line-segments-in-a-vector-space|line segment]] $[a,b]$ (where $\lambda\in[0,1]$).

**Examples:**
- In $\mathbb{R}^2$, $L[a,b]$ is the usual straight line through $a$ and $b$.
- If $a=b$, then $L[a,a]=\{a\}$.
