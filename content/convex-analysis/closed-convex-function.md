---
title: "Closed convex function"
description: "A convex function whose epigraph is closed, equivalently a lower semicontinuous convex function."
---

A **closed convex function** is an extended-real-valued {{< knowl id="function" section="shared-foundations" text="function" >}} $f:\mathbb{R}^n\to(-\infty,+\infty]$ that is {{< knowl id="convex-function-via-epigraph" text="convex" >}} and has a closed epigraph
$$
\mathrm{epi}(f)\;=\;\{(x,t)\in\mathbb{R}^n\times\mathbb{R}:\ t\ge f(x)\},
$$

so that $\mathrm{epi}(f)$ is a closed {{< knowl id="convex-set" text="convex set" >}} in $\mathbb{R}^n\times\mathbb{R}$.

Equivalently, $f$ is closed convex iff it is convex and lower semicontinuous, meaning $\liminf_{x\to x_0} f(x)\ge f(x_0)$ for every $x_0$. Closedness is the regularity condition that makes conjugation behave well: for {{< knowl id="domain-and-epigraph-proper-function" text="proper" >}} functions, closed convexity is exactly the condition for equality $f=f^{**}$ in the {{< knowl id="biconjugate" text="biconjugate" >}} construction (see {{< knowl id="fenchel-moreau-theorem" text="Fenchel–Moreau theorem" >}}).

**Examples:**
- The norm $f(x)=\|x\|_2$ is closed and convex on $\mathbb{R}^n$.
- If $C$ is a closed convex set, then the indicator $\delta_C$ is a closed convex function; if $C$ is convex but not closed (e.g. an open ball), then $\delta_C$ is convex but not closed.
