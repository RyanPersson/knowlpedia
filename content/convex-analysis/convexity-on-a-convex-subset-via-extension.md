---
title: "Convexity on a convex subset via extension"
description: "Define convexity on Ω by extending f to X with value ∞ outside Ω"
---

Let $X$ be a vector space, let $\Omega\subset X$ be a nonempty {{< knowl id="convex-set" text="convex set" >}}, and let $f:\Omega\to\mathbb{R}$ be a real-valued function.

Define the **extension** $\tilde f:X\to\mathbb{R}$ by
$$
\tilde f(x)=
\begin{cases}
f(x), & x\in\Omega,\\
\infty, & x\notin\Omega.
\end{cases}
$$

We say that $f$ is **convex on $\Omega$** if $\tilde f$ is a {{< knowl id="convex-function-via-epigraph" text="convex function" >}} on $X$.

Equivalently: for all $x,y\in\Omega$ and $\lambda\in(0,1)$,
$$
f(\lambda x+(1-\lambda)y)\le \lambda f(x)+(1-\lambda)f(y).
$$

**Context.** This convention packages "convexity + domain restriction" into a single extended-real function, aligning convexity on subsets with epigraph-based convexity.

**Example.** If $\Omega$ is the unit ball in a normed space and $f(x)=\|x\|$ on $\Omega$, then $\tilde f$ encodes the constraint $x\in\Omega$ by assigning $\infty$ outside.
