---
title: "Convex function via epigraph"
description: "A function is convex if and only if its epigraph is a convex set"
---

Let $X$ be a vector space and let $f:X\to \mathbb{R}$ be an {{< knowl id="extended-real-number-system-and-conventions" text="extended-real-valued function" >}}.

The function $f$ is **convex** if its epigraph (see {{< knowl id="domain-and-epigraph-proper-function" text="epigraph" >}}) is a {{< knowl id="convex-set" text="convex set" >}} in $X\times\mathbb{R}$.

**Context.** This geometric definition is equivalent to analytic inequalities such as Jensen's inequality; see {{< knowl id="equivalent-characterizations-of-convex-functions" text="equivalent characterizations of convexity" >}}.

**Examples:**
- On a normed space, $x\mapsto \|x\|$ is convex (uses the triangle inequality; see {{< knowl id="norm-normed-vector-space" text="norm" >}}).
- The {{< knowl id="indicator-function-of-a-set" text="indicator function" >}} of a set $\Omega$ is convex iff $\Omega$ is convex.
- The {{< knowl id="distance-function-to-a-set" text="distance function" >}} to a convex set is convex (in normed spaces).
