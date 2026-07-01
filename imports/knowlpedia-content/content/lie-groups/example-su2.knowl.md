+++
id = "lie-groups/example-su2"
title = "Example: $SU(2)$ and its Lie algebra"
kind = "knowl"
summary = "is simply connected; is 3D with Pauli-matrix commutators, and is a 2-fold cover."
aliases = ["example-su2", "Example: $SU(2)$ and its Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/example-su2.md"
+++

The [[lie-groups/special-unitary-group|special unitary group]]
\[
SU(2)=\left\{\begin{pmatrix}a&b\\-\overline b&\overline a\end{pmatrix} : |a|^2+|b|^2=1\right\}
\]
is a compact, connected, simply connected Lie group (topologically $S^3$).

Its Lie algebra is [[lie-groups/special-unitary-lie-algebra|$\mathfrak{su}(2)$]], the traceless skew-Hermitian $2\times 2$ matrices.

## A concrete basis and commutators
Using the Pauli matrices $\sigma_1,\sigma_2,\sigma_3$, set
\[
X_i := \frac{i}{2}\sigma_i \in \mathfrak{su}(2).
\]
A standard multiplication calculation yields
\[
[X_1,X_2] = -X_3,\qquad [X_2,X_3]=-X_1,\qquad [X_3,X_1]=-X_2,
\]
so (up to an overall sign convention) $\mathfrak{su}(2)$ has the same structure constants as [[lie-groups/orthogonal-lie-algebra|$\mathfrak{so}(3)$]] (compare [[lie-groups/example-so3|the $\mathfrak{so}(3)$ example]]).

## Exponentials (explicit)
For $t\in\mathbb R$,
\[
\exp(tX_3)=\exp\!\left(\frac{it}{2}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\right) = \begin{pmatrix}e^{it/2}&0\\0&e^{-it/2}\end{pmatrix}\in SU(2).
\]
This shows directly that one-parameter subgroups arise from the [[lie-groups/exponential-map-lie-group|exponential map]].

## The 2-to-1 covering $SU(2)\to SO(3)$
Let $SU(2)$ act on $\mathfrak{su}(2)$ by conjugation $g\cdot X=gXg^{-1}$. This preserves the (negative) Killing form inner product, giving a homomorphism
\[
\mathrm{Ad}:SU(2)\to SO(\mathfrak{su}(2))\cong SO(3)
\]
(compare [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]]). One checks:
- $\mathrm{Ad}$ is surjective,
- $\ker(\mathrm{Ad})=\{\pm I\}$.

Hence $\mathrm{Ad}$ is a [[lie-groups/covering-lie-group|covering Lie group]] map $SU(2)\to SO(3)$ with discrete central kernel $\{\pm I\}$.
