---
title: "Total derivative (Fréchet derivative in ℝ^k)"
description: "The linear map Df(a) giving the best first-order approximation f(a+h)=f(a)+Df(a)h+o(‖h‖)."
---

Let $U\subseteq\mathbb{R}^k$ be {{< knowl id="open-set" text="open" >}} and let $f:U\to\mathbb{R}^m$. The function $f$ is **(Fréchet) differentiable at $a\in U$** if there exists a {{< knowl id="linear-map" text="linear map" >}} $A:\mathbb{R}^k\to\mathbb{R}^m$ such that
$$
\lim_{h\to 0}\frac{\|f(a+h)-f(a)-A h\|_2}{\|h\|_2}=0.
$$
The map $A$ is uniquely determined when it exists and is called the **(total) derivative** of $f$ at $a$, denoted $Df(a)$.

This definition captures the best linear approximation of $f$ near $a$. In coordinates, $Df(a)$ is represented by the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}} $J_f(a)$ when $f$ has continuous {{< knowl id="partial-derivative" text="partial derivatives" >}}.

**Examples:**
- If $f(x)=Ax+b$ is affine (with $A$ an $m\times k$ matrix), then $Df(a)=A$ for all $a$.
- If $f:\mathbb{R}^2\to\mathbb{R}$, $f(x,y)=x^2+y^2$, then $Df(a)$ is the linear map $h\mapsto 2\langle a,h\rangle$ (equivalently, gradient dot $h$).
- Existence of all partial derivatives at $a$ does not necessarily imply existence of $Df(a)$ (Fréchet differentiability).
