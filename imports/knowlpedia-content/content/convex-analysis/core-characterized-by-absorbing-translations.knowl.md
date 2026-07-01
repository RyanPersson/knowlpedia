+++
id = "convex-analysis/core-characterized-by-absorbing-translations"
title = "Core Characterized by Absorbing Translations"
kind = "knowl"
summary = "A point lies in core(Ω) iff translating Ω by that point makes it absorbing"
aliases = ["core-characterized-by-absorbing-translations", "Core Characterized by Absorbing Translations"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/core-characterized-by-absorbing-translations.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and $\Omega\subset X$ be nonempty. For $x\in X$, consider the translate $\Omega-x:=\{w-x\mid w\in\Omega\}$ (using [[convex-analysis/set-operations-sum-scalar-multiple-difference|set difference/translation notation]]).

**Proposition**: A point $x\in X$ lies in [[convex-analysis/algebraic-interior-core|core(Ω)]] if and only if $\Omega-x$ is an [[convex-analysis/balanced-and-absorbing-sets|absorbing set]], i.e., for every $v\in X$ there exists $\lambda>0$ such that $v\in \alpha(\Omega-x)$ for all scalars $\alpha$ with $|\alpha|\ge \lambda$.

**Context:** This characterization turns the "two-sided line" definition of the core into a scaling condition that is often easier to check in practice.
