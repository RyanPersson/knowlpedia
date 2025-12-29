---
title: "Local maximum and local minimum"
description: "A point where a function attains a maximum/minimum relative to nearby points."
---

Let $f:E\to\mathbb{R}$ with $E\subseteq X$ where $(X,d)$ is a metric space, and let $a\in E$.

- The point $a$ is a **local maximum** of $f$ if there exists $r>0$ such that for all $x\in E\cap B(a,r)$,
  $$f(x)\le f(a).$$

- The point $a$ is a **local minimum** of $f$ if there exists $r>0$ such that for all $x\in E\cap B(a,r)$,
  $$f(a)\le f(x).$$

Local extrema are "nearby" maxima/minima. In one-variable calculus, local extrema in the interior of an interval are closely tied to critical points and derivative tests.

**Examples:**
- For $f(x)=x^2$ on $\mathbb{R}$, $0$ is a local minimum.
- For $f(x)=-x^2$ on $\mathbb{R}$, $0$ is a local maximum.
- For $f(x)=x^3$ on $\mathbb{R}$, there are no local maxima or minima (even though $f'(0)=0$).
