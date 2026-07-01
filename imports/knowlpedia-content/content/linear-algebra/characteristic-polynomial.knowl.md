+++
id = "linear-algebra/characteristic-polynomial"
title = "Characteristic polynomial"
kind = "knowl"
summary = "Polynomial det(tI - A) attached to a square matrix or linear operator."
aliases = ["characteristic-polynomial", "Characteristic polynomial"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/characteristic-polynomial.md"
+++

A **characteristic polynomial** of a [[linear-algebra/linear-operator|linear operator]] $T:V\to V$ on an $n$-dimensional [[linear-algebra/vector-space|vector space]] is the polynomial
\[
p_T(t)=\det(tI-A)\in\mathbb{F}[t],
\]
where $A$ is the matrix of $T$ in any basis and $I$ is the $n\times n$ identity matrix. This definition is independent of the chosen basis.

The [[linear-algebra/eigenvalue|eigenvalues]] of $T$ are exactly the roots of $p_T(t)$ (in any field extension where the polynomial splits). The polynomial is central to statements like the [[linear-algebra/cayley-hamilton-theorem|Cayley–Hamilton theorem]].

**Examples:**
- If $A=\operatorname{diag}(d_1,\dots,d_n)$, then $p_A(t)=\prod_{i=1}^n (t-d_i)$.
- For $A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$, one has $p_A(t)=t^2-(a+d)t+(ad-bc)$, involving the [[linear-algebra/trace|trace]] and [[linear-algebra/determinant|determinant]] of $A$.
