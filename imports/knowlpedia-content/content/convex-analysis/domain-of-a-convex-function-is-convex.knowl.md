+++
id = "convex-analysis/domain-of-a-convex-function-is-convex"
title = "Domain of a convex function is convex"
kind = "knowl"
summary = "The effective domain dom(f) of a convex function is a convex set"
aliases = ["domain-of-a-convex-function-is-convex", "Domain of a convex function is convex"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/domain-of-a-convex-function-is-convex.md"
+++

**Corollary.**
If $f:X\to\mathbb{R}$ is a [[convex-analysis/convex-function-via-epigraph|convex function]] on a vector space $X$, then its [[convex-analysis/domain-and-epigraph-proper-function|domain]] $\mathrm{dom}(f)$ is a [[convex-analysis/convex-set|convex set]].

**Connection.** This follows immediately from Jensen's inequality in [[convex-analysis/equivalent-characterizations-of-convex-functions|Theorem (equivalent characterizations)]]: if $x,y\in\mathrm{dom}(f)$, then the right-hand side is finite, forcing $f(\lambda x+(1-\lambda)y)<\infty$.
