---
title: "Characteristic polynomial"
description: "Polynomial det(tI - A) attached to a square matrix or linear operator."
---

A **characteristic polynomial** of a {{< knowl id="linear-operator" text="linear operator" >}} $T:V\to V$ on an $n$-dimensional {{< knowl id="vector-space" text="vector space" >}} is the polynomial
\[
p_T(t)=\det(tI-A)\in\mathbb{F}[t],
\]
where $A$ is the matrix of $T$ in any basis and $I$ is the $n\times n$ identity matrix. This definition is independent of the chosen basis.

The {{< knowl id="eigenvalue" text="eigenvalues" >}} of $T$ are exactly the roots of $p_T(t)$ (in any field extension where the polynomial splits). The polynomial is central to statements like the {{< knowl id="cayley-hamilton-theorem" text="Cayley–Hamilton theorem" >}}.

**Examples:**
- If $A=\operatorname{diag}(d_1,\dots,d_n)$, then $p_A(t)=\prod_{i=1}^n (t-d_i)$.
- For $A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$, one has $p_A(t)=t^2-(a+d)t+(ad-bc)$, involving the {{< knowl id="trace" text="trace" >}} and {{< knowl id="determinant" text="determinant" >}} of $A$.
