+++
id = "real-analysis/jacobian-determinant"
title = "Jacobian determinant"
kind = "knowl"
summary = "Determinant of the Jacobian matrix for a map from Rn to Rn"
aliases = ["jacobian-determinant", "Jacobian determinant"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/jacobian-determinant.md"
+++

A **Jacobian determinant** of a differentiable map $f:U\to \mathbb{R}^n$ (with $U\subseteq \mathbb{R}^n$) at a point $a\in U$ is
$$
\det Jf(a),
$$

the [[linear-algebra/determinant|determinant]] of the [[real-analysis/jacobian-matrix|Jacobian matrix]] at $a$.

The Jacobian determinant controls local invertibility and local volume scaling: nonvanishing of $\det Jf(a)$ is the hypothesis of the [[real-analysis/inverse-function-theorem-rk|inverse function theorem]], and it appears in the [[real-analysis/change-of-variables-formula|change of variables formula]] for integrals.

**Examples:**
- For the linear map $f(x,y)=(2x,3y)$, one has $\det Jf(x,y)=6$ for all $(x,y)$.
- For $f(r,\theta)=(r\cos\theta,r\sin\theta)$, the Jacobian determinant is $\det Jf(r,\theta)=r$.
