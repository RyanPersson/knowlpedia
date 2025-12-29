---
title: "Inner product on ℝ^k"
description: "The dot product ⟨x,y⟩ = sum xi yi defining angles and lengths in ℝ^k."
---

For $x=(x_1,\dots,x_k)$ and $y=(y_1,\dots,y_k)$ in $\mathbb{R}^k$, the **(standard) inner product** is
$$\langle x,y\rangle := \sum_{i=1}^k x_i y_i.$$

The inner product is bilinear, symmetric, and positive definite, and it generates the Euclidean norm by $\|x\|_2=\sqrt{\langle x,x\rangle}$. It is the algebraic structure behind orthogonality, projections, and many inequalities.

**Examples:**
- In $\mathbb{R}^2$, $\langle (1,2),(3,4)\rangle = 1\cdot 3 + 2\cdot 4 = 11$.
- $\langle x,x\rangle \ge 0$ for all $x$, with equality iff $x=0$.
- If $x=(1,0)$ and $y=(0,1)$, then $\langle x,y\rangle=0$.
