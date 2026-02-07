---
title: "Lie bracket"
description: "A bilinear alternating operation satisfying the Jacobi identity; for vector fields it is the commutator."
---

A **Lie bracket** on a real vector space $\mathfrak{g}$ is a bilinear map
\[
[\,,\,]:\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}
\]
such that:

1. **Alternating / skew-symmetry:** $[X,X]=0$ for all $X\in\mathfrak{g}$ (equivalently $[X,Y]=-[Y,X]$).
2. **Jacobi identity:** for all $X,Y,Z\in\mathfrak{g}$,
   \[
   [X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
   \]

In differential geometry, there is a canonical Lie bracket on the space of {{< knowl id="vector-field" text="vector fields" >}} on a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$: for vector fields $X,Y$ define $[X,Y]$ by its action on smooth functions,
\[
[X,Y](f) := X(Y(f)) - Y(X(f)), \qquad f\in C^\infty(M).
\]
This produces another vector field and turns the space of vector fields into a Lie algebra.

For a {{< knowl id="lie-group" text="Lie group" >}} $G$, the Lie bracket on the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of $G$" section="lie-groups">}} is obtained by restricting the vector-field bracket to {{< knowl id="left-invariant-vector-field" text="left-invariant vector fields" section="lie-groups">}} and evaluating at the identity.

## Examples

1. On $M=\mathbb{R}^2$ with coordinates $(x,y)$, the coordinate vector fields commute:
   \[
   \Big[\frac{\partial}{\partial x},\frac{\partial}{\partial y}\Big]=0.
   \]

2. On $M=\mathbb{R}$ with coordinate $x$, let $X=x\frac{\partial}{\partial x}$ and $Y=\frac{\partial}{\partial x}$. Then
   \[
   [X,Y] = -\,\frac{\partial}{\partial x}.
   \]

3. In the matrix Lie algebra $\mathfrak{gl}(2,\mathbb{R})$ (the Lie algebra of $GL(2,\mathbb{R})$), with bracket $[A,B]=AB-BA$, take
   \[
   A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
   B=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
   \]
   Then
   \[
   [A,B]=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
   \]
