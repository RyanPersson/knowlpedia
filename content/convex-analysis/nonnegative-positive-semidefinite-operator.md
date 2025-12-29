---
title: "Nonnegative (positive-semidefinite) operator"
description: "A self-adjoint operator A is nonnegative if ⟨Ax,x⟩≥0 for all x"
---

Let $H$ be an inner product space and let $A:H\to H$ be a {{< knowl id="self-adjoint-linear-operator" text="self-adjoint" >}} linear operator.

The operator $A$ is **nonnegative** (or **positive-semidefinite**) if
$$
\langle Ax,x\rangle\ge 0\quad \text{for all }x\in H.
$$

**Context.** Nonnegative operators correspond to convex quadratic forms. In finite dimensions, this matches the usual matrix notion of positive semidefiniteness.

**Example.** If $A=B^*B$ for some linear operator $B$, then $\langle Ax,x\rangle=\langle Bx,Bx\rangle\ge 0$, so $A$ is nonnegative.
