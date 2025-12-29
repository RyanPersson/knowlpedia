---
title: "Restriction of a function"
description: "The same function viewed only on a specified subset of its domain."
---

Let $f:X\to Y$ be a function and let $A\subseteq X$. The **restriction** of $f$ to $A$ is the function
$$f|_A:A\to Y,\qquad f|_A(a):=f(a)\ \text{for all }a\in A.$$

Restrictions are used constantly in analysis to localize statements (e.g., continuity on a subset, behavior near a point, or defining inverses on domains where a function becomes injective).

**Examples:**
- If $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$, then $f|_{[0,\infty)}:[0,\infty)\to\mathbb{R}$ is injective.
- If $f(x)=\sin x$ on $\mathbb{R}$, then $f|_{[-\pi/2,\pi/2]}$ is bijective onto $[-1,1]$.
- If $A=\varnothing$, then $f|_{\varnothing}:\varnothing\to Y$ is the unique function with empty domain.
