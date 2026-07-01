+++
id = "convex-analysis/hahn-banach-theorem-in-complex-vector-spaces"
title = "Hahn–Banach Theorem (Complex Vector Spaces)"
kind = "knowl"
summary = "Complex linear functionals dominated by a seminorm extend to the whole space."
aliases = ["hahn-banach-theorem-in-complex-vector-spaces", "Hahn–Banach Theorem (Complex Vector Spaces)"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/hahn-banach-theorem-in-complex-vector-spaces.md"
+++

Let $X$ be a complex [[linear-algebra/vector-space|vector space]], let $Y\subset X$ be a [[convex-analysis/linear-subspace|linear subspace]], and let $p:X\to\mathbb{R}$ be a [[convex-analysis/seminorm|seminorm]].

**Theorem**: If $f:Y\to\mathbb{C}$ is complex-linear and satisfies
$$
|f(y)|\le p(y)\quad\text{for all }y\in Y,
$$

then there exists a complex-linear functional $F:X\to\mathbb{C}$ such that
- $F|_Y=f$, and
- $|F(x)|\le p(x)$ for all $x\in X$.

**Context:**
A standard route is to extend the real part via [[convex-analysis/hahn-banach-extension-dominated-by-a-seminorm-real-case|the real seminorm Hahn–Banach theorem]] after viewing $X$ as a real vector space, and then reconstruct the complex functional.
