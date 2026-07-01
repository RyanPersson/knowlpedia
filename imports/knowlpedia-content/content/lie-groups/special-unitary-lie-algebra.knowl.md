+++
id = "lie-groups/special-unitary-lie-algebra"
title = "Special unitary Lie algebra"
kind = "knowl"
summary = "The Lie algebra of : traceless skew-Hermitian matrices with the commutator bracket."
aliases = ["special-unitary-lie-algebra", "Special unitary Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/special-unitary-lie-algebra.md"
+++

### Definition
The **special unitary Lie algebra** $\mathfrak{su}(n)$ is the real Lie algebra of the [[lie-groups/special-unitary-group|special unitary group $SU(n)$]]. Concretely,
$$
\mathfrak{su}(n)=\{X\in M_n(\mathbb C)\mid X^\ast+X=0,\ \mathrm{tr}(X)=0\},
$$

where $X^\ast=\overline{X}^{\,T}$ is the Hermitian adjoint. The Lie bracket is the matrix commutator
$$
[X,Y]=XY-YX.
$$

Equivalently, $\mathfrak{su}(n)$ is the codimension-one ideal inside the [[lie-groups/unitary-lie-algebra|unitary Lie algebra $\\mathfrak{u}(n)$]] given by the trace-zero condition.

### Basic structure and context
- As a real vector space, $\dim_\mathbb{R}\mathfrak{su}(n)=n^2-1$.
- The center of $\mathfrak{su}(n)$ is trivial: if $X$ commutes with all of $\mathfrak{su}(n)$, then $X$ is a scalar matrix, and tracelessness forces $X=0$. In particular, for $n\ge 2$, $\mathfrak{su}(n)$ is a (real) [[lie-groups/simple-lie-algebra|simple Lie algebra]].
- The inclusion $\mathfrak{su}(n)\subset \mathfrak{gl}(n,\mathbb C)$ is the differential at the identity of the defining inclusion $SU(n)\subset GL(n,\mathbb C)$, as in [[lie-groups/lie-algebra-of-a-lie-group|the Lie algebra of a Lie group]] and the principle that the [[lie-groups/differential-is-lie-algebra-homomorphism|differential of a Lie group homomorphism is a Lie algebra homomorphism]].

A standard motivation is that $\mathfrak{su}(n)$ is the compact real form of $\mathfrak{sl}(n,\mathbb C)$ (see [[lie-groups/special-linear-lie-algebra|$\\mathfrak{sl}(n,\\mathbb C)$]]), and its representation theory is a cornerstone of highest-weight methods (compare [[lie-groups/highest-weight|highest weights]] and [[lie-groups/highest-weight-theorem|the highest-weight theorem]]).
