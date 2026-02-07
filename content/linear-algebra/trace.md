---
title: "Trace"
description: "Sum of diagonal entries of a square matrix, invariant under change of basis."
---

A **trace** is the scalar associated to an $n\times n$ matrix $A=(a_{ij})$ over a field $\mathbb{F}$ defined by
\[
\operatorname{tr}(A)=\sum_{i=1}^n a_{ii}.
\]
For a {{< knowl id="linear-operator" text="linear operator" >}} $T:V\to V$ on a finite-dimensional {{< knowl id="vector-space" text="vector space" >}}, the trace $\operatorname{tr}(T)$ is defined as $\operatorname{tr}(A)$ for any matrix $A$ representing $T$ in a basis; this is independent of the basis.

Trace is often paired with the {{< knowl id="determinant" text="determinant" >}} in matrix identities and appears in coefficients of the {{< knowl id="characteristic-polynomial" text="characteristic polynomial" >}}. When the characteristic polynomial splits, the trace equals the sum of the {{< knowl id="eigenvalue" text="eigenvalues" >}} counted with algebraic multiplicity.

**Examples:**
- If $A$ is diagonal with diagonal entries $d_1,\dots,d_n$, then $\operatorname{tr}(A)=d_1+\cdots+d_n$.
- The identity matrix $I_n$ satisfies $\operatorname{tr}(I_n)=n$.
- Any nilpotent matrix (some power equals $0$) has trace $0$.
