+++
id = "convex-analysis/nonnegative-positive-semidefinite-operator"
title = "Nonnegative (positive-semidefinite) operator"
kind = "knowl"
summary = "A self-adjoint operator A is nonnegative if ⟨Ax,x⟩≥0 for all x"
aliases = ["nonnegative-positive-semidefinite-operator", "Nonnegative (positive-semidefinite) operator"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/nonnegative-positive-semidefinite-operator.md"
+++

Let $H$ be an inner product space and let $A:H\to H$ be a [[convex-analysis/self-adjoint-linear-operator|self-adjoint]] linear operator.

The operator $A$ is **nonnegative** (or **positive-semidefinite**) if
$$
\langle Ax,x\rangle\ge 0\quad \text{for all }x\in H.
$$

**Context.** Nonnegative operators correspond to convex quadratic forms. In finite dimensions, this matches the usual matrix notion of positive semidefiniteness.

**Example.** If $A=B^\ast B$ for some linear operator $B$, then $\langle Ax,x\rangle=\langle Bx,Bx\rangle\ge 0$, so $A$ is nonnegative.
