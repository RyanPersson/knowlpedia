---
title: "Indicator function of a set"
description: "The extended-real function that is 0 on Ω and ∞ outside Ω"
---

Let $X$ be a vector space and let $\Omega\subset X$ be nonempty. The **indicator function** of $\Omega$ is the {{< knowl id="extended-real-number-system-and-conventions" text="extended-real-valued" >}} function $\delta_\Omega:X\to\mathbb{R}$ defined by
$$
\delta_\Omega(x)=
\begin{cases}
0, & x\in\Omega,\\
\infty, & x\notin\Omega.
\end{cases}
$$

Its {{< knowl id="domain-and-epigraph-proper-function" text="domain" >}} is $\mathrm{dom}(\delta_\Omega)=\Omega$, and its epigraph is $\mathrm{epi}(\delta_\Omega)=\Omega\times[0,\infty)$.

**Context.** Indicator functions encode constraints as penalties: minimizing $f+\delta_\Omega$ is equivalent to minimizing $f$ subject to $x\in\Omega$.

**Convexity.** $\delta_\Omega$ is {{< knowl id="convex-function-via-epigraph" text="convex" >}} if and only if $\Omega$ is a {{< knowl id="convex-set" text="convex set" >}}.

**Examples:**
- If $\Omega$ is a subspace, then $\delta_\Omega$ is convex.
- If $\Omega$ is a nonconvex set (e.g., two disjoint balls), then $\delta_\Omega$ is not convex.
