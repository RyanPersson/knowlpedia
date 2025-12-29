---
title: "Domain, epigraph, and proper function"
description: "dom(f) is where f is finite; epi(f) is the set above the graph; proper means dom(f)≠∅"
---

Let $X$ be a vector space and let $f:X\to \mathbb{R}$ be an extended-real-valued function (see {{< knowl id="extended-real-number-system-and-conventions" text="extended reals" >}}).

- The **domain** of $f$ is
$$
\mathrm{dom}(f):=\{x\in X: f(x)<\infty\}.
$$
- The **epigraph** of $f$ is
$$
\mathrm{epi}(f):=\{(x,\alpha)\in X\times\mathbb{R}: f(x)\le \alpha\}.
$$

The function $f$ is **proper** if $\mathrm{dom}(f)\neq\emptyset$.

**Context.** The epigraph turns function properties into geometric properties of sets; convexity of $f$ is defined by convexity of $\mathrm{epi}(f)$ (see {{< knowl id="convex-function-via-epigraph" text="convex functions via epigraphs" >}}).
