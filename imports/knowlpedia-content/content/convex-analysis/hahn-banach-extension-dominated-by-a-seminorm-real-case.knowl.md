+++
id = "convex-analysis/hahn-banach-extension-dominated-by-a-seminorm-real-case"
title = "Hahn–Banach Extension Dominated by a Seminorm (Real Case)"
kind = "knowl"
summary = "A real linear functional bounded by a seminorm extends with the same bound."
aliases = ["hahn-banach-extension-dominated-by-a-seminorm-real-case", "Hahn–Banach Extension Dominated by a Seminorm (Real Case)"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/hahn-banach-extension-dominated-by-a-seminorm-real-case.md"
+++

Let $X$ be a real [[linear-algebra/vector-space|vector space]], let $Y\subset X$ be a [[convex-analysis/linear-subspace|subspace]], and let $p:X\to\mathbb{R}$ be a [[convex-analysis/seminorm|seminorm]].

**Theorem**: If $f:Y\to\mathbb{R}$ is linear and satisfies
$$
|f(y)|\le p(y)\quad\text{for all }y\in Y,
$$

then there exists a linear functional $F:X\to\mathbb{R}$ such that
- $F|_Y=f$, and
- $|F(x)|\le p(x)$ for all $x\in X$.

**Context:**
This is obtained from [[convex-analysis/hahn-banach-theorem-in-real-vector-spaces|the sublinear Hahn–Banach theorem]] by applying it to both $f$ and $-f$ (or, equivalently, to the sublinear function $x\mapsto p(x)$ with symmetric domination).
