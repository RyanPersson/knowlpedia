---
title: "Jacobian matrix"
description: "The matrix of first partial derivatives of a map f:ℝ^k→ℝ^m."
---

Let $U\subseteq\mathbb{R}^k$ be open and let $f:U\to\mathbb{R}^m$ with components $f=(f_1,\dots,f_m)$, where each $f_i:U\to\mathbb{R}$. If all relevant partial derivatives exist at $a\in U$, the **Jacobian matrix** of $f$ at $a$ is the $m\times k$ matrix
$$
J_f(a) := \left[\frac{\partial f_i}{\partial x_j}(a)\right]_{1\le i\le m,\ 1\le j\le k}.
$$

When $f$ is differentiable at $a$ in the (Fréchet) sense, $J_f(a)$ represents the derivative as a linear map $\mathbb{R}^k\to\mathbb{R}^m$ with respect to the standard bases.

**Examples:**
- If $f(x,y)=(x+y,x-y)$, then
  $J_f(x,y)=\begin{pmatrix}1&1\\ 1&-1\end{pmatrix}.$
- If $f:\mathbb{R}^2\to\mathbb{R}$ is scalar-valued, then $J_f(a)$ is a $1\times 2$ row vector (the transpose of the gradient).
- For a linear map $f(x)=Ax$, $J_f(a)=A$ for all $a$.
