---
title: "Jacobian matrix"
description: "Matrix of first partial derivatives of a multivariable map"
---

A **Jacobian matrix** of a map $f=(f_1,\dots,f_m):U\to \mathbb{R}^m$ (with $U\subseteq \mathbb{R}^n$) at a point $a\in U$ is the $m\times n$ matrix
$$
Jf(a)=\left(\frac{\partial f_i}{\partial x_j}(a)\right)_{1\le i\le m,\;1\le j\le n},
$$
provided these {{< knowl id="partial-derivative" text="partial derivatives" >}} exist.

When $f$ is {{< knowl id="differentiable-map" text="differentiable" >}} at $a$, the {{< knowl id="frechet-derivative" text="Fréchet derivative" >}} $Df(a)$ is a linear map, and $Jf(a)$ is the matrix that represents $Df(a)$ in the standard bases of $\mathbb{R}^n$ and $\mathbb{R}^m$. For scalar-valued $f$, $Jf(a)$ is closely related (up to transpose conventions) to the {{< knowl id="gradient" text="gradient" >}}.

**Examples:**
- If $f(x,y)=(x^2y,\sin(x-y))$, then
  $$
  Jf(x,y)=
  \begin{pmatrix}
  2xy & x^2\\
  \cos(x-y) & -\cos(x-y)
  \end{pmatrix}.
  $$

- If $f(x,y,z)=x+y+z$, then $Jf(x,y,z)=\begin{pmatrix}1&1&1\end{pmatrix}$.
