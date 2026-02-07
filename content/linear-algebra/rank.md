---
title: "Rank"
description: "The rank of a linear map or matrix is the dimension of its image."
---

Let \(T:V\to W\) be a linear map between vector spaces over a field \(\mathbb{F}\). The **rank** of \(T\) is
$$
\operatorname{rank}(T) \;:=\; \dim(\operatorname{im} T),
$$
where \(\operatorname{im}T=\{T(v):v\in V\}\subseteq W\).

If \(A\) is an \(m\times n\) matrix over \(\mathbb{F}\), its rank is the rank of the associated linear map \(x\mapsto Ax\), i.e.
$$
\operatorname{rank}(A) \;=\; \dim(\text{column space of }A).
$$

### Equivalent characterizations (matrices)
For an \(m\times n\) matrix \(A\), the following numbers are equal:
- \(\dim(\)span of the columns of \(A)\),
- \(\dim(\)span of the rows of \(A)\),
- the number of pivots in a row-reduced echelon form of \(A\),
- the largest integer \(r\) such that \(A\) has an \(r\times r\) minor with nonzero determinant.

In particular,
$$
0 \le \operatorname{rank}(A) \le \min(m,n).
$$

### Rank–nullity
If \(V\) is finite-dimensional, the kernel (null space) \(\ker T = \{v\in V : T(v)=0\}\) satisfies
$$
\dim V \;=\; \operatorname{rank}(T) \;+\; \dim(\ker T).
$$

### Example
For
$$
A=\begin{pmatrix}
1&2&3\\
2&4&6
\end{pmatrix},
$$
the second row is \(2\) times the first, so the row (and column) spaces are \(1\)-dimensional, hence \(\operatorname{rank}(A)=1\).
