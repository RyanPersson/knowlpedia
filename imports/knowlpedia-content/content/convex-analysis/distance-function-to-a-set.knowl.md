+++
id = "convex-analysis/distance-function-to-a-set"
title = "Distance function to a set"
kind = "knowl"
summary = "d_Ω(x)=inf{||x−w||: w∈Ω} in a normed space"
aliases = ["distance-function-to-a-set", "Distance function to a set"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/distance-function-to-a-set.md"
+++

Let $(X,\|\cdot\|)$ be a [[convex-analysis/norm-normed-vector-space|normed vector space]] and let $\Omega\subset X$ be nonempty. The **distance function** to $\Omega$ is the real-valued map $d_\Omega:X\to[0,\infty)$ defined by
$$
d_\Omega(x):=\inf\{\|x-w\|: w\in \Omega\}.
$$

**Context.** Distance functions quantify constraint violation and are fundamental in projection methods and variational analysis.

**Basic properties.**
- $d_\Omega(x)=0$ iff $x$ belongs to $\overline{\Omega}$.
- $d_\Omega$ is 1-Lipschitz: $|d_\Omega(x)-d_\Omega(y)|\le \|x-y\|$.

**Convexity.** If $\Omega$ is [[convex-analysis/convex-set|convex]], then $d_\Omega$ is convex. Conversely, if $\Omega$ is closed and $d_\Omega$ is convex, then $\Omega$ is convex (standard exercise-level fact).

**Examples:**
- If $\Omega=\{0\}$, then $d_\Omega(x)=\|x\|$.
- If $\Omega$ is a closed ball, $d_\Omega(x)$ is the excess of $\|x-x_0\|$ over the radius, truncated below by 0.
