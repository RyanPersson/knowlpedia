---
title: "Hessian matrix"
description: "The matrix of second partial derivatives of a scalar function f:ℝ^k→ℝ."
---

Let $U\subseteq\mathbb{R}^k$ be open and let $f:U\to\mathbb{R}$. If all second partial derivatives exist at $a\in U$, the **Hessian matrix** of $f$ at $a$ is the $k\times k$ matrix
$$
H_f(a) := \left[\frac{\partial^2 f}{\partial x_i\,\partial x_j}(a)\right]_{1\le i,j\le k}.
$$

When $f$ is $C^2$, the Hessian is symmetric (mixed partials commute) and governs second-order Taylor approximation and second-derivative tests for extrema.

**Examples:**
- If $f(x,y)=x^2+y^2$, then $H_f(x,y)=\begin{pmatrix}2&0\\0&2\end{pmatrix}$.
- If $f(x,y)=xy$, then $H_f(x,y)=\begin{pmatrix}0&1\\1&0\end{pmatrix}$.
- For a linear function $f(x)=\langle c,x\rangle$, the Hessian is the zero matrix.
