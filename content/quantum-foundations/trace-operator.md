---
title: "Trace of an Operator"
description: "A basis-independent scalar associated to a linear operator, equal to the sum of diagonal entries or eigenvalues in finite dimension."
---

Let \(H\) be a finite-dimensional complex Hilbert space and let \(A:H\to H\) be a linear operator. The **trace** of \(A\), denoted \(\operatorname{Tr}(A)\), is defined by choosing any orthonormal basis \((e_1,\dots,e_n)\) and setting
\[
\operatorname{Tr}(A) := \sum_{k=1}^n \langle e_k, A e_k\rangle.
\]
This value is independent of the chosen orthonormal basis.

This notion agrees with the usual matrix trace (see {{< knowl id="trace" section="linear-algebra" text="Trace" >}}) after identifying \(A\) with its matrix in an orthonormal basis.

## Equivalent descriptions (finite dimension)
- If \(A\) is represented by a matrix \((A_{ij})\) in any basis, then \(\operatorname{Tr}(A)=\sum_i A_{ii}\).
- \(\operatorname{Tr}(A)\) equals the sum of eigenvalues of \(A\), counted with algebraic multiplicity.

## Key properties
For operators \(A,B\) on \(H\) and scalars \(\alpha,\beta\):

- **Linearity:** \(\operatorname{Tr}(\alpha A+\beta B)=\alpha\operatorname{Tr}(A)+\beta\operatorname{Tr}(B)\).
- **Cyclic property:** \(\operatorname{Tr}(AB)=\operatorname{Tr}(BA)\).
- **Unitary invariance:** if \(U\) is unitary, then \(\operatorname{Tr}(U^\ast A U)=\operatorname{Tr}(A)\).
- **Positivity:** if \(A\) is positive semidefinite, then \(\operatorname{Tr}(A)\ge 0\).

## Trace and quantum expectation values
If \(\rho\) is a {{< knowl id="density-operator" text="Density Operator" >}} and \(A\) is an observable (self-adjoint operator), the expected value of \(A\) in state \(\rho\) is
\[
\mathbb{E}_\rho[A] = \operatorname{Tr}(\rho A).
\]
In particular, density operators are normalized by the condition \(\operatorname{Tr}(\rho)=1\).

## Note on infinite dimension
On an infinite-dimensional Hilbert space, not every bounded operator has a trace. One typically restricts to **trace-class** operators to extend \(\operatorname{Tr}\) with similar properties.
