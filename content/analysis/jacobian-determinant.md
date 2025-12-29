---
title: "Jacobian determinant"
description: "For f:ℝ^k→ℝ^k, the determinant det(J_f) controlling local volume scaling."
---

Let $U\subseteq\mathbb{R}^k$ be {{< knowl id="open-set" text="open" >}} and let $f:U\to\mathbb{R}^k$. If $f$ has a {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}} $J_f(a)$ at $a\in U$, the **Jacobian determinant** of $f$ at $a$ is
$$\det J_f(a)\in\mathbb{R}.$$

When $f$ is {{< knowl id="class-ck-map" text="$C^1$" >}}, $\det J_f(a)\neq 0$ is the nondegeneracy condition in the inverse function theorem. In integration, $|\det J_f|$ appears in the change-of-variables formula as the local volume scaling factor.

**Examples:**
- If $f(x)=Ax$ is linear on $\mathbb{R}^k$, then $\det J_f(a)=\det A$ for all $a$.
- For $f(x,y)=(2x,3y)$, $J_f=\begin{pmatrix}2&0\\0&3\end{pmatrix}$ so $\det J_f=6$.
- For a rotation in $\mathbb{R}^2$, $\det J_f=1$ (orientation-preserving and area-preserving).
