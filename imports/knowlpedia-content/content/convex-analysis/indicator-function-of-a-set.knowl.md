+++
id = "convex-analysis/indicator-function-of-a-set"
title = "Indicator function of a set"
kind = "knowl"
summary = "The extended-real function that is 0 on Ω and ∞ outside Ω"
aliases = ["indicator-function-of-a-set", "Indicator function of a set"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/indicator-function-of-a-set.md"
+++

Let $X$ be a vector space and let $\Omega\subset X$ be nonempty. The **indicator function** of $\Omega$ is the [[convex-analysis/extended-real-number-system-and-conventions|extended-real-valued]] function $\delta_\Omega:X\to\mathbb{R}$ defined by
$$
\delta_\Omega(x)=
\begin{cases}
0, & x\in\Omega,\\
\infty, & x\notin\Omega.
\end{cases}
$$

Its [[convex-analysis/domain-and-epigraph-proper-function|domain]] is $\mathrm{dom}(\delta_\Omega)=\Omega$, and its epigraph is $\mathrm{epi}(\delta_\Omega)=\Omega\times[0,\infty)$.

**Context.** Indicator functions encode constraints as penalties: minimizing $f+\delta_\Omega$ is equivalent to minimizing $f$ subject to $x\in\Omega$.

**Convexity.** $\delta_\Omega$ is [[convex-analysis/convex-function-via-epigraph|convex]] if and only if $\Omega$ is a [[convex-analysis/convex-set|convex set]].

**Examples:**
- If $\Omega$ is a subspace, then $\delta_\Omega$ is convex.
- If $\Omega$ is a nonconvex set (e.g., two disjoint balls), then $\delta_\Omega$ is not convex.
