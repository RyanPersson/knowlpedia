+++
id = "convex-analysis/closed-convex-function"
title = "Closed convex function"
kind = "knowl"
summary = "A convex function whose epigraph is closed, equivalently a lower semicontinuous convex function."
aliases = ["closed-convex-function", "Closed convex function"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/closed-convex-function.md"
+++

A **closed convex function** is an extended-real-valued [[shared-foundations/function|function]] $f:\mathbb{R}^n\to(-\infty,+\infty]$ that is [[convex-analysis/convex-function-via-epigraph|convex]] and has a closed epigraph
$$
\mathrm{epi}(f)\;=\;\{(x,t)\in\mathbb{R}^n\times\mathbb{R}:\ t\ge f(x)\},
$$

so that $\mathrm{epi}(f)$ is a closed [[convex-analysis/convex-set|convex set]] in $\mathbb{R}^n\times\mathbb{R}$.

Equivalently, $f$ is closed convex iff it is convex and lower semicontinuous, meaning $\liminf_{x\to x_0} f(x)\ge f(x_0)$ for every $x_0$. Closedness is the regularity condition that makes conjugation behave well: for [[convex-analysis/domain-and-epigraph-proper-function|proper]] functions, closed convexity is exactly the condition for equality $f=f^{**}$ in the [[convex-analysis/biconjugate|biconjugate]] construction (see [[convex-analysis/fenchel-moreau-theorem|Fenchel–Moreau theorem]]).

**Examples:**
- The norm $f(x)=\|x\|_2$ is closed and convex on $\mathbb{R}^n$.
- If $C$ is a closed convex set, then the indicator $\delta_C$ is a closed convex function; if $C$ is convex but not closed (e.g. an open ball), then $\delta_C$ is convex but not closed.
