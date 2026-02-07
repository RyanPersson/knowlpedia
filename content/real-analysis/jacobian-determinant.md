---
title: "Jacobian determinant"
description: "Determinant of the Jacobian matrix for a map from Rn to Rn"
---

A **Jacobian determinant** of a differentiable map $f:U\to \mathbb{R}^n$ (with $U\subseteq \mathbb{R}^n$) at a point $a\in U$ is
$$
\det Jf(a),
$$

the {{< knowl id="determinant" section="linear-algebra" text="determinant" >}} of the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}} at $a$.

The Jacobian determinant controls local invertibility and local volume scaling: nonvanishing of $\det Jf(a)$ is the hypothesis of the {{< knowl id="inverse-function-theorem-rk" text="inverse function theorem" >}}, and it appears in the {{< knowl id="change-of-variables-formula" text="change of variables formula" >}} for integrals.

**Examples:**
- For the linear map $f(x,y)=(2x,3y)$, one has $\det Jf(x,y)=6$ for all $(x,y)$.
- For $f(r,\theta)=(r\cos\theta,r\sin\theta)$, the Jacobian determinant is $\det Jf(r,\theta)=r$.
