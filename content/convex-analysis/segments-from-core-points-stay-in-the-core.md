---
title: "Segments from Core Points Stay in the Core"
description: "If a is in core(Ω) and b in Ω, then points on [a,b) remain in core(Ω)."
---

Let $X$ be a {{< knowl id="vector-space" text="vector space" >}} and let $\Omega\subset X$ be {{< knowl id="convex-set" text="convex" >}}.

**Proposition**: If $a\in {{< knowl id="algebraic-interior-core-and-linear-closure" text="core(Ω)" >}}$ and $b\in\Omega$, then
$$
[a,b)\subset \operatorname{core}(\Omega),
$$
where $[a,b)$ is the half-open {{< knowl id="line-segments-in-a-vector-space" text="line segment" >}} from $a$ to $b$.

**Context:**
This is the "core" analogue of {{< knowl id="segments-from-interior-points-stay-in-the-interior" text="the interior segment lemma" >}} for normed spaces. It is used to prove structural properties of $\operatorname{core}(\Omega)$ such as idempotence.
