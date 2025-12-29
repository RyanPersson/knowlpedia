---
title: "Convex sets via convex combinations"
description: "A set is convex iff it contains convex combinations of its points"
---

**Proposition.**
A nonempty set $\Omega\subset X$ in a real vector space $X$ is {{< knowl id="convex-set" text="convex" >}} if and only if it contains every {{< knowl id="convex-combination" text="convex combination" >}} of finitely many of its points; i.e., for all $m\in\mathbb{N}$, all $x_1,\dots,x_m\in\Omega$, and all $\lambda_i\ge 0$ with $\sum_{i=1}^m\lambda_i=1$, we have
$$
\sum_{i=1}^m \lambda_i x_i\in\Omega.
$$

**Context.** This is the "finite averaging" characterization of convexity and is used to describe convex hulls and many convex constructions.

**Proof sketch.** The "only if" direction follows by induction on $m$ using the two-point definition of convexity. For "if," take $m=2$ to recover the defining two-point condition.
