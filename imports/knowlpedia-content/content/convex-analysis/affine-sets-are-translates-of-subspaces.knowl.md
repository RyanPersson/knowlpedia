+++
id = "convex-analysis/affine-sets-are-translates-of-subspaces"
title = "Affine Sets are Translates of Subspaces"
kind = "knowl"
summary = "Ω is affine iff Ω−ω is a linear subspace (equivalently, Ω=ω+L)."
aliases = ["affine-sets-are-translates-of-subspaces", "Affine Sets are Translates of Subspaces"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/affine-sets-are-translates-of-subspaces.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $\Omega\subset X$ be nonempty.

**Lemma**: The set $\Omega$ is [[convex-analysis/affine-set|affine]] if and only if for every $\omega\in\Omega$, the translate
$$
\Omega-\omega:=\{x-\omega\mid x\in\Omega\}
$$

is a [[convex-analysis/linear-subspace|linear subspace]] of $X$.

Equivalently, $\Omega$ is affine iff there exist $\omega\in X$ and a subspace $L\subset X$ such that $\Omega=\omega+L$.

**Context:**
This lemma explains why affine sets are often called "affine subspaces": they are precisely translates of linear subspaces.
