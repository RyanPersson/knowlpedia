+++
id = "convex-analysis/convex-function-via-epigraph"
title = "Convex function via epigraph"
kind = "knowl"
summary = "A function is convex if and only if its epigraph is a convex set"
aliases = ["convex-function-via-epigraph", "Convex function via epigraph"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convex-function-via-epigraph.md"
+++

Let $X$ be a vector space and let $f:X\to \mathbb{R}$ be an [[convex-analysis/extended-real-number-system-and-conventions|extended-real-valued function]].

The function $f$ is **convex** if its epigraph (see [[convex-analysis/domain-and-epigraph-proper-function|epigraph]]) is a [[convex-analysis/convex-set|convex set]] in $X\times\mathbb{R}$.

**Context.** This geometric definition is equivalent to analytic inequalities such as Jensen's inequality; see [[convex-analysis/equivalent-characterizations-of-convex-functions|equivalent characterizations of convexity]].

**Examples:**
- On a normed space, $x\mapsto \|x\|$ is convex (uses the triangle inequality; see [[convex-analysis/norm-normed-vector-space|norm]]).
- The [[convex-analysis/indicator-function-of-a-set|indicator function]] of a set $\Omega$ is convex iff $\Omega$ is convex.
- The [[convex-analysis/distance-function-to-a-set|distance function]] to a convex set is convex (in normed spaces).
