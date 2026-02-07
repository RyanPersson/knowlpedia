---
title: "Finite-Dimensional Complex Hilbert Space"
description: "A finite-dimensional complex inner product space, automatically complete, used as the state space in finite-dimensional quantum theory."
---

A **finite-dimensional complex Hilbert space** is a complex vector space \(H\) of finite dimension equipped with an inner product
\[
\langle \cdot,\cdot\rangle : H\times H \to \mathbb{C}
\]
that is linear in one argument and conjugate-linear in the other (conventions vary), positive definite, and induces a norm \(\|x\|=\sqrt{\langle x,x\rangle}\). In finite dimension, every normed vector space is complete, so “Hilbert space” is automatic once the inner product is given.

This is the basic setting for finite-dimensional quantum mechanics: **pure states** are unit vectors up to a global phase, and more generally states are represented by {{< knowl id="density-operator" text="Density Operator" >}}.

## Equivalent concrete model
If \(\dim H = n\), then \(H\) is (non-canonically) isomorphic to \(\mathbb{C}^n\) with the standard inner product
\[
\langle x,y\rangle = \sum_{k=1}^n \overline{x_k}\,y_k.
\]
Choosing an orthonormal basis identifies vectors with column vectors and linear maps with matrices.

## Orthonormal bases and expansions
An **orthonormal basis** \((e_1,\dots,e_n)\) satisfies \(\langle e_i,e_j\rangle=\delta_{ij}\). Every \(x\in H\) has the expansion
\[
x=\sum_{k=1}^n \langle e_k,x\rangle\,e_k,
\qquad
\|x\|^2=\sum_{k=1}^n |\langle e_k,x\rangle|^2.
\]
The identity operator can be written as \(I=\sum_{k=1}^n |e_k\rangle\langle e_k|\) in bra–ket notation.

## Linear maps and adjoints
Every linear map \(A:H\to H\) is automatically continuous and {{< knowl id="bounded-operator-hilbert" text="Bounded Operator Hilbert" >}} in finite dimension. The **adjoint** \(A^\ast\) is the unique operator satisfying
\[
\langle x,Ay\rangle=\langle A^\ast x,y\rangle \quad \text{for all } x,y\in H.
\]
Self-adjoint operators ({{< knowl id="self-adjoint-operator-observable" text="Self Adjoint Operator Observable" >}}) play the role of observables, with real eigenvalues and an orthonormal eigenbasis.

For the general (possibly infinite-dimensional) notion, see {{< knowl id="hilbert-space" section="linear-algebra" text="Hilbert Space" >}}.
