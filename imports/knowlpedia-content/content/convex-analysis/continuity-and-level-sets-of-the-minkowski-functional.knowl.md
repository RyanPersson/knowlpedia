+++
id = "convex-analysis/continuity-and-level-sets-of-the-minkowski-functional"
title = "Continuity and Level Sets of the Minkowski Gauge"
kind = "knowl"
summary = "If 0 lies in the interior of a convex set, its gauge is continuous and recovers int(Ω) and cl(Ω)."
aliases = ["continuity-and-level-sets-of-the-minkowski-functional", "Continuity and Level Sets of the Minkowski Gauge"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/continuity-and-level-sets-of-the-minkowski-functional.md"
+++

Let $X$ be a [[convex-analysis/norm-normed-vector-space|normed vector space]] and let $\Omega\subset X$ be [[convex-analysis/convex-set|convex]] with $0\in\operatorname{int}(\Omega)$ (see [[convex-analysis/interior-of-a-set|interior]]).

**Corollary**: The [[convex-analysis/minkowski-function-gauge-of-a-set|Minkowski gauge]] $p_\Omega$ is continuous. Moreover,
$$
\operatorname{int}(\Omega)=\{x\in X\mid p_\Omega(x)<1\}
$$
and
$$
\overline{\Omega}=\{x\in X\mid p_\Omega(x)\le 1\}.
$$

Here $\overline{\Omega}$ denotes the [[convex-analysis/closure-of-a-set|closure]] of $\Omega$.

**Context:**
Continuity comes from the inclusion of a norm ball into $\Omega$ (since $0\in\operatorname{int}(\Omega)$), yielding a Lipschitz bound for $p_\Omega$. The set identities combine [[convex-analysis/properties-of-the-minkowski-functional-of-a-convex-set|the gauge level-set theorem]] with [[convex-analysis/linear-closure-equals-closure-for-solid-convex-sets|lin(Ω)=cl(Ω) for solid convex sets]].
