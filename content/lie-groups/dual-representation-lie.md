---
title: "Dual (contragredient) representation"
description: "Given a representation on , the induced representation on is ; infinitesimally, ."
---

Let $V$ be a finite-dimensional vector space.

## Lie group version
If $\rho:G\to GL(V)$ is a {{< knowl id="representation-of-a-lie-group" text="representation of a Lie group" >}} $G$, the **dual (contragredient) representation** on $V^*$ is
\[
\rho^*:G\to GL(V^*),\qquad
(\rho^*(g)\lambda)(v) := \lambda\bigl(\rho(g^{-1})v\bigr).
\]
Equivalently, in a chosen basis, $\rho^*(g)$ is represented by $(\rho(g^{-1}))^{\mathsf T}$.

## Lie algebra version
If $\pi:\mathfrak g\to \mathfrak{gl}(V)$ is a {{< knowl id="representation-of-a-lie-algebra" text="representation of a Lie algebra" >}} $\mathfrak g$, its dual representation $\pi^*:\mathfrak g\to\mathfrak{gl}(V^*)$ is defined by
\[
(\pi^*(X)\lambda)(v) := -\,\lambda\bigl(\pi(X)v\bigr).
\]
In matrix form, $\pi^*(X) = -\,\pi(X)^{\mathsf T}$.

These definitions are compatible under differentiation: if $\pi=d\rho_e$ (see {{< knowl id="differential-is-lie-algebra-homomorphism" text="differentiation of a group homomorphism" >}}), then $d(\rho^*)_e=\pi^*$.

## Context
Duals interact naturally with other constructions such as {{< knowl id="tensor-product-of-representations-lie" text="tensor products" >}}. In highest-weight theory, dualizing typically negates weights (compare {{< knowl id="weight-of-a-representation" text="weights" >}} and {{< knowl id="weights-in-dual-cartan" text="weights in the dual Cartan" >}}).
