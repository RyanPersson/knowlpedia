---
title: "Interior and closure relations for convex sets with nonempty interior"
description: "For convex sets with nonempty interior: cl(int Ω)=cl Ω and int(cl Ω)=int Ω"
---

**Theorem.**
Let $X$ be a normed vector space and let $\Omega\subset X$ be {{< knowl id="convex-set" text="convex" >}} with $\mathrm{int}(\Omega)\neq\emptyset$. Then:

1. $\overline{\mathrm{int}(\Omega)}=\overline{\Omega}$.
2. $\mathrm{int}(\overline{\Omega})=\mathrm{int}(\Omega)$.

**Context.** For convex sets with nonempty interior, "taking closure" and "taking interior" are tightly compatible. This is special to convexity and can fail for arbitrary sets.

**Proof sketch.**
1. The inclusion $\overline{\mathrm{int}(\Omega)}\subset\overline{\Omega}$ is immediate. For the reverse, it suffices to show $\Omega\subset\overline{\mathrm{int}(\Omega)}$: fix $b\in\Omega$ and $a\in\mathrm{int}(\Omega)$; by {{< knowl id="segments-from-interior-points-stay-in-the-interior" text="the interior-segment lemma" >}}, points $(1/k)a+(1-1/k)b$ lie in $\mathrm{int}(\Omega)$ and converge to $b$.
2. The inclusion $\mathrm{int}(\Omega)\subset\mathrm{int}(\overline{\Omega})$ is obvious. For the converse, use a "push-out" argument: given $b\in \mathrm{int}(\overline{\Omega})$ and $a\in\mathrm{int}(\Omega)$, move slightly past $b$ along the ray from $a$ through $b$ to find a point $c\in\overline{\Omega}$, then apply the interior-segment lemma to conclude $b\in\mathrm{int}(\Omega)$.
