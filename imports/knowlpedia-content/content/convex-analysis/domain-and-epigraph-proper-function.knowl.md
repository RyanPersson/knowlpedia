+++
id = "convex-analysis/domain-and-epigraph-proper-function"
title = "Domain, epigraph, and proper function"
kind = "knowl"
summary = "dom(f) is where f is finite; epi(f) is the set above the graph; proper means dom(f)≠∅"
aliases = ["domain-and-epigraph-proper-function", "Domain, epigraph, and proper function"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/domain-and-epigraph-proper-function.md"
+++

Let $X$ be a vector space and let $f:X\to \mathbb{R}$ be an extended-real-valued function (see [[convex-analysis/extended-real-number-system-and-conventions|extended reals]]).

- The **domain** of $f$ is
$$
\mathrm{dom}(f):=\{x\in X: f(x)<\infty\}.
$$

- The **epigraph** of $f$ is
$$
\mathrm{epi}(f):=\{(x,\alpha)\in X\times\mathbb{R}: f(x)\le \alpha\}.
$$

The function $f$ is **proper** if $\mathrm{dom}(f)\neq\emptyset$.

**Context.** The epigraph turns function properties into geometric properties of sets; convexity of $f$ is defined by convexity of $\mathrm{epi}(f)$ (see [[convex-analysis/convex-function-via-epigraph|convex functions via epigraphs]]).
