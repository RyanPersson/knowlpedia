---
title: "Continuity and Level Sets of the Minkowski Gauge"
description: "If 0 lies in the interior of a convex set, its gauge is continuous and recovers int(Ω) and cl(Ω)."
---

Let $X$ be a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}} and let $\Omega\subset X$ be {{< knowl id="convex-set" text="convex" >}} with $0\in {{< knowl id="interior-of-a-set" text="int(Ω)" >}}$.

**Corollary**: The {{< knowl id="minkowski-function-gauge-of-a-set" text="Minkowski gauge" >}} $p_\Omega$ is continuous. Moreover,
$$
\operatorname{int}(\Omega)=\{x\in X\mid p_\Omega(x)<1\}
$$
and
$$
{{< knowl id="closure-of-a-set" text="cl(Ω)" >}}=\{x\in X\mid p_\Omega(x)\le 1\}.
$$

**Context:**
Continuity comes from the inclusion of a norm ball into $\Omega$ (since $0\in\operatorname{int}(\Omega)$), yielding a Lipschitz bound for $p_\Omega$. The set identities combine {{< knowl id="properties-of-the-minkowski-functional-of-a-convex-set" text="the gauge level-set theorem" >}} with {{< knowl id="linear-closure-equals-closure-for-solid-convex-sets" text="lin(Ω)=cl(Ω) for solid convex sets" >}}.
