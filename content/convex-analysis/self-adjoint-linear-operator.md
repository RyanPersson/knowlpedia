---
title: "Self-adjoint linear operator"
description: "An operator A with ⟨Ax,y⟩=⟨x,Ay⟩ on an inner product space"
---

Let $H$ be an inner product space (real or complex), and let $A:H\to H$ be a {{< knowl id="linear-operator-linear-transformation" text="linear operator" >}}.

The operator $A$ is **self-adjoint** if
$$
\langle Ax,y\rangle=\langle x,Ay\rangle \quad \text{for all }x,y\in H.
$$

**Context.** Self-adjoint operators generalize symmetric (real) and Hermitian (complex) matrices and play a central role in convexity of quadratic forms and spectral theory.

**Examples:**
- In $\mathbb{R}^n$ with the standard inner product, $A(x)=Mx$ is self-adjoint iff $M$ is symmetric.
- In $\mathbb{C}^n$, $A(x)=Mx$ is self-adjoint iff $M$ is Hermitian.
