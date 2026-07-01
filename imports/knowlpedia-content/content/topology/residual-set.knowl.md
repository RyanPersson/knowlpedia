+++
id = "topology/residual-set"
title = "Residual set"
kind = "knowl"
summary = "A set whose complement is meager"
aliases = ["residual-set", "Residual set"]
domains = ["topology"]
legacy_source_path = "topology/residual-set.md"
+++

A **residual set** in a [[topology/topological-space|topological space]] $X$ is a [[shared-foundations/subset|subset]] $R\subseteq X$ whose [[shared-foundations/complement|complement]] $X\setminus R$ is [[topology/meager-set|meager]].

Equivalently, $R$ is residual if it contains a countable [[shared-foundations/intersection|intersection]] of sets that are both [[topology/open-set|open]] and [[topology/dense-set|dense]]. In a [[topology/baire-space|Baire space]], every residual set is dense.

**Examples:**
- The irrationals $\mathbb{R}\setminus\mathbb{Q}$ form a residual subset of $\mathbb{R}$, since $\mathbb{Q}$ is [[topology/meager-set|meager]].
- In any Baire space, the intersection of countably many dense open sets is residual (and dense), as captured by [[topology/intersection-of-dense-open-is-dense|intersection of dense open sets is dense]].
