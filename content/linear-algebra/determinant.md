---
title: "Determinant"
description: "A scalar invariant of a square matrix measuring volume scaling and invertibility."
---

A **determinant** is a function that assigns to each $n\times n$ matrix $A=(a_{ij})$ over a field $\mathbb{F}$ the scalar
\[
\det(A)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^n a_{i,\sigma(i)},
\]
where $S_n$ is the set of permutations of $\{1,\dots,n\}$ and $\operatorname{sgn}(\sigma)\in\{\pm 1\}$ is the sign of $\sigma$.

For a {{< knowl id="linear-operator" text="linear operator" >}} $T:V\to V$ on a finite-dimensional {{< knowl id="vector-space" text="vector space" >}}, one defines $\det(T)$ as the determinant of any matrix representing $T$ in a basis (this does not depend on the choice of basis). The {{< knowl id="characteristic-polynomial" text="characteristic polynomial" >}} is defined using determinants.

**Examples:**
- If $A$ is diagonal with diagonal entries $d_1,\dots,d_n$, then $\det(A)=d_1\cdots d_n$.
- If $A$ is upper triangular, then $\det(A)$ is the product of its diagonal entries.
- For the scaling operator $T(v)=c\,v$ on an $n$-dimensional space, $\det(T)=c^n$.
