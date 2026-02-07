---
title: "Domain of a convex function is convex"
description: "The effective domain dom(f) of a convex function is a convex set"
---

**Corollary.**
If $f:X\to\mathbb{R}$ is a {{< knowl id="convex-function-via-epigraph" text="convex function" >}} on a vector space $X$, then its {{< knowl id="domain-and-epigraph-proper-function" text="domain" >}} $\mathrm{dom}(f)$ is a {{< knowl id="convex-set" text="convex set" >}}.

**Connection.** This follows immediately from Jensen's inequality in {{< knowl id="equivalent-characterizations-of-convex-functions" text="Theorem (equivalent characterizations)" >}}: if $x,y\in\mathrm{dom}(f)$, then the right-hand side is finite, forcing $f(\lambda x+(1-\lambda)y)<\infty$.
