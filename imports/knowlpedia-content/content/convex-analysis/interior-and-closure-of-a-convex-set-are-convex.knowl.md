+++
id = "convex-analysis/interior-and-closure-of-a-convex-set-are-convex"
title = "Interior and closure of a convex set are convex"
kind = "knowl"
summary = "In a normed space, convexity is preserved under interior and closure"
aliases = ["interior-and-closure-of-a-convex-set-are-convex", "Interior and closure of a convex set are convex"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/interior-and-closure-of-a-convex-set-are-convex.md"
+++

**Proposition.**
Let $X$ be a [[convex-analysis/norm-normed-vector-space|normed vector space]] and let $\Omega\subset X$ be [[convex-analysis/convex-set|convex]]. Then:

- the [[convex-analysis/interior-of-a-set|interior]] $\mathrm{int}(\Omega)$ is convex (possibly empty),
- the [[convex-analysis/closure-of-a-set|closure]] $\overline{\Omega}$ is convex.

**Context.** Convexity is stable under two basic topological operations in normed spaces, which is essential for analyzing convex feasible regions.

**Proof sketch.** For $\overline{\Omega}$, approximate points by sequences in $\Omega$ and use convexity plus limit arguments. For $\mathrm{int}(\Omega)$, if $x,y\in\mathrm{int}(\Omega)$ then small balls around $x$ and $y$ lie in $\Omega$; convex combinations of these balls give a neighborhood of $\lambda x+(1-\lambda)y$ contained in $\Omega$, so the combination lies in $\mathrm{int}(\Omega)$.
