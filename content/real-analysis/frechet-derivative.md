---
title: "Fréchet derivative"
description: "The derivative of a multivariable function as a best linear approximation at a point"
---

A **Fréchet derivative** of a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:U\to \mathbb{R}^m$ (with $U\subseteq \mathbb{R}^n$) at a point $a\in U$ is a {{< knowl id="linear-map" section="linear-algebra" text="linear map" >}} $Df(a):\mathbb{R}^n\to \mathbb{R}^m$ such that
$$
\lim_{h\to 0}\frac{\|f(a+h)-f(a)-Df(a)h\|}{\|h\|}=0,
$$

where $\|\cdot\|$ is the {{< knowl id="euclidean-norm" section="linear-algebra" text="Euclidean norm" >}}.

If such a map exists, it is unique; it is the linear part of the first-order approximation $f(a+h)=f(a)+Df(a)h+o(\|h\|)$. When $f$ has partial derivatives, $Df(a)$ is represented by the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}} at $a$, and existence of $Df(a)$ is the defining condition for a {{< knowl id="differentiable-map" text="differentiable map" >}} at $a$.

**Examples:**
- If $f(x)=Ax$ for a fixed matrix $A$, then $Df(a)h=Ah$ for every $a$.
- For $f:\mathbb{R}^2\to \mathbb{R}^2$ given by $f(x,y)=(x^2y,\,x+y)$, the derivative at $(a,b)$ is the linear map represented by the matrix
  $$
  \begin{pmatrix}
  2ab & a^2\\
  1 & 1
  \end{pmatrix}.
  $$
