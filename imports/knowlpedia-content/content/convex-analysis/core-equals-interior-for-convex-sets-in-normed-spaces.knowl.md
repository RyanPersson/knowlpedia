+++
id = "convex-analysis/core-equals-interior-for-convex-sets-in-normed-spaces"
title = "Core Equals Interior for Convex Sets in Normed Spaces"
kind = "knowl"
summary = "For convex sets with nonempty interior, algebraic and topological interiors coincide."
aliases = ["core-equals-interior-for-convex-sets-in-normed-spaces", "Core Equals Interior for Convex Sets in Normed Spaces"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/core-equals-interior-for-convex-sets-in-normed-spaces.md"
+++

Let $X$ be a [[convex-analysis/norm-normed-vector-space|normed vector space]] and let $\Omega\subset X$ be [[convex-analysis/convex-set|convex]] with [[convex-analysis/interior-of-a-set|int(Ω)]]$\neq\emptyset$.

**Theorem**:
$$
\operatorname{core}(\Omega)=\operatorname{int}(\Omega).
$$

**Context:**
The equality identifies the purely algebraic notion [[convex-analysis/algebraic-interior-core|core(Ω)]] with the usual topological interior once the set is convex and has nonempty interior. The proof in the notes uses the geometric lemma [[convex-analysis/segments-from-interior-points-stay-in-the-interior|segments from interior points stay in the interior]].

**Proof sketch (idea):**
The inclusion $\operatorname{int}(\Omega)\subset \operatorname{core}(\Omega)$ is direct. For the reverse direction, translate so that $0\in\operatorname{int}(\Omega)$ and use convexity plus the segment lemma to show any core point must lie in the interior.
