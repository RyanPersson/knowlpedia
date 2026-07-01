+++
id = "lie-groups/dual-representation-lie"
title = "Dual (contragredient) representation"
kind = "knowl"
summary = "Given a representation on , the induced representation on is ; infinitesimally, ."
aliases = ["dual-representation-lie", "Dual (contragredient) representation"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/dual-representation-lie.md"
+++

Let $V$ be a finite-dimensional vector space.

## Lie group version
If $\rho:G\to GL(V)$ is a [[lie-groups/representation-of-a-lie-group|representation of a Lie group]] $G$, the **dual (contragredient) representation** on $V^*$ is
\[
\rho^*:G\to GL(V^*),\qquad
(\rho^*(g)\lambda)(v) := \lambda\bigl(\rho(g^{-1})v\bigr).
\]
Equivalently, in a chosen basis, $\rho^*(g)$ is represented by $(\rho(g^{-1}))^{\mathsf T}$.

## Lie algebra version
If $\pi:\mathfrak g\to \mathfrak{gl}(V)$ is a [[lie-groups/representation-of-a-lie-algebra|representation of a Lie algebra]] $\mathfrak g$, its dual representation $\pi^*:\mathfrak g\to\mathfrak{gl}(V^*)$ is defined by
\[
(\pi^*(X)\lambda)(v) := -\,\lambda\bigl(\pi(X)v\bigr).
\]
In matrix form, $\pi^*(X) = -\,\pi(X)^{\mathsf T}$.

These definitions are compatible under differentiation: if $\pi=d\rho_e$ (see [[lie-groups/differential-is-lie-algebra-homomorphism|differentiation of a group homomorphism]]), then $d(\rho^*)_e=\pi^*$.

## Context
Duals interact naturally with other constructions such as [[lie-groups/tensor-product-of-representations-lie|tensor products]]. In highest-weight theory, dualizing typically negates weights (compare [[lie-groups/weight-of-a-representation|weights]] and [[lie-groups/weights-in-dual-cartan|weights in the dual Cartan]]).
