---
title: "Special unitary Lie algebra"
description: "The Lie algebra of : traceless skew-Hermitian matrices with the commutator bracket."
---

### Definition
The **special unitary Lie algebra** $\mathfrak{su}(n)$ is the real Lie algebra of the {{< knowl id="special-unitary-group" text="special unitary group $SU(n)$" >}}. Concretely,
$$
\mathfrak{su}(n)=\{X\in M_n(\mathbb C)\mid X^\ast+X=0,\ \mathrm{tr}(X)=0\},
$$

where $X^\ast=\overline{X}^{\,T}$ is the Hermitian adjoint. The Lie bracket is the matrix commutator
$$
[X,Y]=XY-YX.
$$

Equivalently, $\mathfrak{su}(n)$ is the codimension-one ideal inside the {{< knowl id="unitary-lie-algebra" text="unitary Lie algebra $\\mathfrak{u}(n)$" >}} given by the trace-zero condition.

### Basic structure and context
- As a real vector space, $\dim_\mathbb{R}\mathfrak{su}(n)=n^2-1$.
- The center of $\mathfrak{su}(n)$ is trivial: if $X$ commutes with all of $\mathfrak{su}(n)$, then $X$ is a scalar matrix, and tracelessness forces $X=0$. In particular, for $n\ge 2$, $\mathfrak{su}(n)$ is a (real) {{< knowl id="simple-lie-algebra" text="simple Lie algebra" >}}.
- The inclusion $\mathfrak{su}(n)\subset \mathfrak{gl}(n,\mathbb C)$ is the differential at the identity of the defining inclusion $SU(n)\subset GL(n,\mathbb C)$, as in {{< knowl id="lie-algebra-of-a-lie-group" text="the Lie algebra of a Lie group" >}} and the principle that the {{< knowl id="differential-is-lie-algebra-homomorphism" text="differential of a Lie group homomorphism is a Lie algebra homomorphism" >}}.

A standard motivation is that $\mathfrak{su}(n)$ is the compact real form of $\mathfrak{sl}(n,\mathbb C)$ (see {{< knowl id="special-linear-lie-algebra" text="$\\mathfrak{sl}(n,\\mathbb C)$" >}}), and its representation theory is a cornerstone of highest-weight methods (compare {{< knowl id="highest-weight" text="highest weights" >}} and {{< knowl id="highest-weight-theorem" text="the highest-weight theorem" >}}).
