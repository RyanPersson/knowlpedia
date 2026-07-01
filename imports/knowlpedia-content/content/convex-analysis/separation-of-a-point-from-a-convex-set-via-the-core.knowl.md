+++
id = "convex-analysis/separation-of-a-point-from-a-convex-set-via-the-core"
title = "Separating a Point from a Convex Set via the Core"
kind = "knowl"
summary = "If x0 is outside core(Ω) and core(Ω)≠∅, then Ω and {x0} are separable by a hyperplane."
aliases = ["separation-of-a-point-from-a-convex-set-via-the-core", "Separating a Point from a Convex Set via the Core"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/separation-of-a-point-from-a-convex-set-via-the-core.md"
+++

Let $X$ be a real [[linear-algebra/vector-space|vector space]], let $x_0\in X$, and let $\Omega\subset X$ be [[convex-analysis/convex-set|convex]]. Assume that [[convex-analysis/algebraic-interior-core|core(Ω)]] is nonempty and $x_0\notin \operatorname{core}(\Omega)$.

**Theorem**: The sets $\Omega$ and $\{x_0\}$ can be [[convex-analysis/separation-by-a-hyperplane|separated by a hyperplane]]. Equivalently, there exists a nonzero linear functional $f:X\to\mathbb{R}$ such that
$$
f(x)\le f(x_0)\quad\text{for all }x\in\Omega.
$$

**Context:**
This is a geometric form of [[convex-analysis/hahn-banach-theorem-in-real-vector-spaces|Hahn–Banach]]. The proof uses the [[convex-analysis/minkowski-function-gauge-of-a-set|Minkowski gauge]] of $\Omega$ (after translation) to build a sublinear domination bound and then applies Hahn–Banach.
