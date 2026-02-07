---
title: "Lorentz group"
description: "The group of linear transformations preserving the Minkowski bilinear form."
---

Fix the Minkowski bilinear form on $\Bbb R^n$ of signature $(1,n-1)$, represented (in a standard basis) by the matrix
$$
\eta=\mathrm{diag}(-1,1,\dots,1).
$$

The **Lorentz group** in dimension $n$ is the subgroup
$$
O(1,n-1)=\{A\in \mathrm{GL}(n,\Bbb R)\mid A^{T}\eta A=\eta\}.
$$

It is an instance of the {{< knowl id="orthogonal-group" text="orthogonal group in an indefinite signature" >}}. The case $n=4$ is the classical Lorentz group of special relativity.

Two commonly used subgroups are:
- $SO(1,n-1)=\{A\in O(1,n-1)\mid \det A=1\}$ (the “special” Lorentz group),
- the identity component $SO^{+}(1,n-1)$ (often called “proper orthochronous”), consisting of matrices preserving both orientation and time orientation.

## Lie algebra
Its Lie algebra is the indefinite orthogonal Lie algebra
$$
\mathfrak{so}(1,n-1)=\{X\in \mathfrak{gl}(n,\Bbb R)\mid X^{T}\eta+\eta X=0\},
$$
an instance of {{< knowl id="orthogonal-lie-algebra" text="orthogonal Lie algebras" >}}.

## Context
The Lorentz group acts linearly on Minkowski space, and adjoining translations yields the {{< knowl id="poincare-group" text="Poincaré group" >}}, the full isometry group of Minkowski spacetime.
