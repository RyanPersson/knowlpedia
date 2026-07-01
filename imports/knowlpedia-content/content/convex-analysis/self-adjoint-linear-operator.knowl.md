+++
id = "convex-analysis/self-adjoint-linear-operator"
title = "Self-adjoint linear operator"
kind = "knowl"
summary = "An operator A with ⟨Ax,y⟩=⟨x,Ay⟩ on an inner product space"
aliases = ["self-adjoint-linear-operator", "Self-adjoint linear operator"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/self-adjoint-linear-operator.md"
+++

Let $H$ be an inner product space (real or complex), and let $A:H\to H$ be a [[convex-analysis/linear-operator-linear-transformation|linear operator]].

The operator $A$ is **self-adjoint** if
$$
\langle Ax,y\rangle=\langle x,Ay\rangle \quad \text{for all }x,y\in H.
$$

**Context.** Self-adjoint operators generalize symmetric (real) and Hermitian (complex) matrices and play a central role in convexity of quadratic forms and spectral theory.

**Examples:**
- In $\mathbb{R}^n$ with the standard inner product, $A(x)=Mx$ is self-adjoint iff $M$ is symmetric.
- In $\mathbb{C}^n$, $A(x)=Mx$ is self-adjoint iff $M$ is Hermitian.
