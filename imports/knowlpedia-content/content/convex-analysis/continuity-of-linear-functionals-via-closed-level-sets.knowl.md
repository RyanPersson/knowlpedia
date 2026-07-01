+++
id = "convex-analysis/continuity-of-linear-functionals-via-closed-level-sets"
title = "Continuity of Linear Functionals via Closed Level Sets"
kind = "knowl"
summary = "A linear functional on a normed space is continuous iff one of its level sets is closed."
aliases = ["continuity-of-linear-functionals-via-closed-level-sets", "Continuity of Linear Functionals via Closed Level Sets"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/continuity-of-linear-functionals-via-closed-level-sets.md"
+++

Let $X$ be a real [[convex-analysis/norm-normed-vector-space|normed space]], let $f:X\to\mathbb{R}$ be a nonzero linear functional, and let $\alpha\in\mathbb{R}$.

**Theorem**: The functional $f$ is continuous if and only if the level set
$$
A:=\{x\in X\mid f(x)=\alpha\}
$$

is a [[convex-analysis/closed-subset|closed subset]] of $X$.

**Context:**
This links geometric closedness of a [[convex-analysis/hyperplane|hyperplane]] level set to analytic boundedness of $f$ (compare [[convex-analysis/bounded-linear-functional-norm-of-a-functional|bounded linear functionals]]). It is used to upgrade algebraic separation in vector spaces to separation by **closed** hyperplanes in normed spaces; see [[convex-analysis/separation-by-closed-hyperplane-under-interior-condition|closed hyperplane separation]].
