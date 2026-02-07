---
title: "Segments from interior points stay in the interior"
description: "From an interior point, the segment to any other point stays interior except possibly at the endpoint"
---

**Lemma.**
Let $X$ be a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}} and let $\Omega\subset X$ be a {{< knowl id="convex-set" text="convex" >}} set with nonempty interior. If $a\in \mathrm{int}(\Omega)$ and $b\in\Omega$, then
$$
[a,b)\subset \mathrm{int}(\Omega),
$$

where $[a,b)$ is the half-open {{< knowl id="line-segments-in-a-vector-space" text="segment" >}} from $a$ to $b$.

**Context.** This is a key geometric fact for convex sets: interior points "see" the whole set through interior segments. It underlies closure/interior relations for convex sets.

**Proof idea.** Starting from a ball around $a$ contained in $\Omega$, use convexity and scaling properties of balls to build a ball around each point $\lambda a+(1-\lambda)b$ (with $\lambda\in(0,1]$) that still lies in $\Omega$.
