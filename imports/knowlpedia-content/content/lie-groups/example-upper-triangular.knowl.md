+++
id = "lie-groups/example-upper-triangular"
title = "Example: upper triangular matrices (a solvable Lie algebra)"
kind = "knowl"
summary = "Upper triangular matrices form a Lie algebra whose derived subalgebra is strictly upper triangular, giving an explicit derived series."
aliases = ["example-upper-triangular", "Example: upper triangular matrices (a solvable Lie algebra)"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/example-upper-triangular.md"
+++

Let $B\subset GL(2,\mathbb R)$ (see [[lie-groups/general-linear-group|general linear group]]) be the subgroup of invertible upper triangular matrices:
\[
B=\left\{\begin{pmatrix}a&b\\0&d\end{pmatrix}: a,d\ne 0\right\}.
\]
It is a Lie subgroup, and its Lie algebra is the upper triangular matrices
\[
\mathfrak b=\left\{\begin{pmatrix}x&y\\0&z\end{pmatrix}: x,y,z\in\mathbb R\right\}\subset \mathfrak{gl}(2,\mathbb R).
\]

## Commutator calculation
Take
\[
A=\begin{pmatrix}x&y\\0&z\end{pmatrix},\quad
A'=\begin{pmatrix}x'&y'\\0&z'\end{pmatrix}.
\]
Then
\[
[A,A']=AA'-A'A = \begin{pmatrix} 0 & (x-z)y'-(x'-z')y\\ 0 & 0 \end{pmatrix},
\]
which is **strictly** upper triangular.

Therefore the [[lie-groups/derived-subalgebra|derived subalgebra]] is
\[
[\mathfrak b,\mathfrak b] = \left\{\begin{pmatrix}0&u\\0&0\end{pmatrix}: u\in\mathbb R\right\} \cong \mathbb R,
\]
matching the [[lie-groups/example-strictly-upper-triangular|strictly upper triangular]] pattern.

## Derived series (explicit)
Since strictly upper triangular $2\times 2$ matrices commute with each other, we get
\[
\mathfrak b^{(1)}=[\mathfrak b,\mathfrak b]=\left\{\begin{pmatrix}0&u\\0&0\end{pmatrix}\right\},
\qquad
\mathfrak b^{(2)}=[\mathfrak b^{(1)},\mathfrak b^{(1)}]=0.
\]
Hence $\mathfrak b$ is solvable (see [[lie-groups/solvable-lie-algebra|solvable Lie algebra]] and [[lie-groups/derived-series-lie-algebra|derived series]]).

**Context.** Upper triangular (Borel) subalgebras are the archetypal solvable subalgebras inside semisimple Lie algebras, and computations like the one above are the linear-algebraic shadow of triangularization phenomena.
