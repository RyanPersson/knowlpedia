---
title: "Minimal polynomial"
description: "Smallest-degree monic polynomial that annihilates a linear operator."
---

A **minimal polynomial** of a {{< knowl id="linear-operator" text="linear operator" >}} $T:V\to V$ on a finite-dimensional {{< knowl id="vector-space" text="vector space" >}} is the unique monic polynomial $m_T(t)\in\mathbb{F}[t]$ of least degree such that
\[
m_T(T)=0,
\]
meaning that substituting $T$ into the polynomial yields the zero operator.

The minimal polynomial divides the {{< knowl id="characteristic-polynomial" text="characteristic polynomial" >}} and has the same set of {{< knowl id="eigenvalue" text="eigenvalues" >}} (in a splitting field). It encodes algebraic properties of $T$ more economically than the characteristic polynomial.

**Examples:**
- For the identity operator $I$, the minimal polynomial is $m_I(t)=t-1$.
- If $T$ is nilpotent and $T^k=0$ with minimal such $k$, then $m_T(t)=t^k$.
- If $T$ is diagonalizable with distinct eigenvalues $\lambda_1,\dots,\lambda_r$ (over a field where they exist), then $m_T(t)=\prod_{i=1}^r (t-\lambda_i)$.
