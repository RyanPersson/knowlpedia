---
title: "Quasiconvexity via convex sublevel sets"
description: "f is quasiconvex iff all sublevel sets {x: f(x)≤α} are convex"
---

**Proposition.**
Let $X$ be a vector space. A function $f:X\to\mathbb{R}$ is {{< knowl id="quasiconvex-function" text="quasiconvex" >}} if and only if for every $\alpha\in\mathbb{R}$ the sublevel set
$$
L_\alpha:=\{x\in X: f(x)\le \alpha\}
$$
is a {{< knowl id="convex-set" text="convex set" >}}.

**Context.** This is the defining geometric feature of quasiconvexity: convexity is demanded of *level sets* rather than of the epigraph.

**Proof sketch.** (⇒) If $x,y\in L_\alpha$, then $\max\{f(x),f(y)\}\le \alpha$, hence $f(\lambda x+(1-\lambda)y)\le \alpha$, so the combination lies in $L_\alpha$. (⇐) Fix $x,y$ and let $\alpha=\max\{f(x),f(y)\}$. Then $x,y\in L_\alpha$, so convexity of $L_\alpha$ gives $\lambda x+(1-\lambda)y\in L_\alpha$, i.e., $f(\lambda x+(1-\lambda)y)\le \alpha$.
