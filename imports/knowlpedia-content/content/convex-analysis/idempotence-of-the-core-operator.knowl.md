+++
id = "convex-analysis/idempotence-of-the-core-operator"
title = "Idempotence of the Core Operator"
kind = "knowl"
summary = "Taking the core twice gives the same set: core(core(Ω))=core(Ω)."
aliases = ["idempotence-of-the-core-operator", "Idempotence of the Core Operator"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/idempotence-of-the-core-operator.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $\Omega\subset X$ be [[convex-analysis/convex-set|convex]].

**Corollary**:
$$
\operatorname{core}(\operatorname{core}(\Omega))=\operatorname{core}(\Omega).
$$

Here [[convex-analysis/algebraic-interior-core|core]] denotes the algebraic interior. This follows from [[convex-analysis/segments-from-core-points-stay-in-the-core|segments from core points stay in the core]]: once a point is in $\operatorname{core}(\Omega)$, small segment perturbations remain inside, so taking the core again does not remove any points.
