---
title: "Affine Sets are Translates of Subspaces"
description: "Ω is affine iff Ω−ω is a linear subspace (equivalently, Ω=ω+L)."
---

Let $X$ be a {{< knowl id="vector-space" text="vector space" >}} and let $\Omega\subset X$ be nonempty.

**Lemma**: The set $\Omega$ is {{< knowl id="affine-set" text="affine" >}} if and only if for every $\omega\in\Omega$, the translate
$$
\Omega-\omega:=\{x-\omega\mid x\in\Omega\}
$$
is a {{< knowl id="linear-subspace" text="linear subspace" >}} of $X$.

Equivalently, $\Omega$ is affine iff there exist $\omega\in X$ and a subspace $L\subset X$ such that $\Omega=\omega+L$.

**Context:**
This lemma explains why affine sets are often called "affine subspaces": they are precisely translates of linear subspaces.
