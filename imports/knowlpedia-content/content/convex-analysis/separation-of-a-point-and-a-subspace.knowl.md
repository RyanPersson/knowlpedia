+++
id = "convex-analysis/separation-of-a-point-and-a-subspace"
title = "Separation of a Point and a Subspace"
kind = "knowl"
summary = "If a point has positive distance to a subspace, a bounded functional separates them."
aliases = ["separation-of-a-point-and-a-subspace", "Separation of a Point and a Subspace"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/separation-of-a-point-and-a-subspace.md"
+++

Let $X$ be a [[convex-analysis/norm-normed-vector-space|normed space]], let $Y\subset X$ be a [[convex-analysis/linear-subspace|subspace]], and let $x_0\in X$ satisfy
$$
d(x_0,Y):=\inf_{y\in Y}\|x_0-y\|=d>0.
$$

**Theorem (separating a point and a subspace)**: There exists a [[convex-analysis/bounded-linear-functional-norm-of-a-functional|bounded linear functional]] $f:X\to\mathbb{K}$ such that
1. $f(y)=0$ for all $y\in Y$,
2. $\|f\|=1/d$, and
3. $f(x_0)=1$.

**Context:**
This is a geometric consequence of [[convex-analysis/hahn-banach-theorem-in-normed-spaces|Hahn–Banach in normed spaces]]. It produces a continuous [[convex-analysis/hyperplane|hyperplane]] through $Y$ that separates $x_0$ from $Y$.

**Proof sketch (idea):**
Define a linear functional on $Y\oplus \operatorname{span}\{x_0\}$ (see [[convex-analysis/direct-sum-of-subspaces|direct sum]]) by mapping $y+\lambda x_0\mapsto \lambda$ and bound its norm using the distance assumption; then extend it by Hahn–Banach.
