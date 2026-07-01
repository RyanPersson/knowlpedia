+++
id = "convex-analysis/segments-from-core-points-stay-in-the-core"
title = "Segments from Core Points Stay in the Core"
kind = "knowl"
summary = "If a is in core(Ω) and b in Ω, then points on [a,b) remain in core(Ω)."
aliases = ["segments-from-core-points-stay-in-the-core", "Segments from Core Points Stay in the Core"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/segments-from-core-points-stay-in-the-core.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $\Omega\subset X$ be [[convex-analysis/convex-set|convex]].

**Proposition**: If $a\in\operatorname{core}(\Omega)$ (see [[convex-analysis/algebraic-interior-core|core]]) and $b\in\Omega$, then
$$
[a,b)\subset \operatorname{core}(\Omega),
$$

where $[a,b)$ is the half-open [[convex-analysis/line-segments-in-a-vector-space|line segment]] from $a$ to $b$.

**Context:**
This is the "core" analogue of [[convex-analysis/segments-from-interior-points-stay-in-the-interior|the interior segment lemma]] for normed spaces. It is used to prove structural properties of $\operatorname{core}(\Omega)$ such as idempotence.
