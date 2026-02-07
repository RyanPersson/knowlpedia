---
title: "Orthogonal group"
description: "The Lie group of linear transformations preserving a nondegenerate symmetric bilinear form."
---

Let $(V,\langle\ ,\ \rangle)$ be a finite-dimensional real inner product space.

## Definition (Euclidean case)
The **orthogonal group** is
$$
O(V)=\{A\in \mathrm{GL}(V)\mid \langle Av,Aw\rangle=\langle v,w\rangle\ \text{for all }v,w\in V\}.
$$

After choosing an orthonormal basis of $V\cong \Bbb R^n$, this becomes
$$
O(n)=\{A\in \mathrm{GL}(n,\Bbb R)\mid A^TA=I\}.
$$
It is a closed subgroup of the {{< knowl id="general-linear-group" text="general linear group" >}}, hence a Lie group by the {{< knowl id="closed-subgroup-theorem" text="closed subgroup theorem" >}}.

The determinant gives two connected components: $\det=1$ and $\det=-1$. The identity component is the {{< knowl id="special-orthogonal-group" text="special orthogonal group" >}} $SO(n)$.

## Indefinite signatures
More generally, given a nondegenerate symmetric bilinear form of signature $(p,q)$, the group of linear transformations preserving it is denoted $O(p,q)$. The case $O(1,n-1)$ is the {{< knowl id="lorentz-group" text="Lorentz group" >}}.

## Lie algebra
The Lie algebra of $O(n)$ is {{< knowl id="orthogonal-lie-algebra" text="$\mathfrak{so}(n)$" >}}, consisting of skew-symmetric matrices, reflecting the infinitesimal condition for orthogonality.
