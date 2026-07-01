+++
id = "lie-groups/unitary-lie-algebra"
title = "Unitary Lie algebra"
kind = "knowl"
summary = "The Lie algebra of : skew-Hermitian matrices with the commutator bracket."
aliases = ["unitary-lie-algebra", "Unitary Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/unitary-lie-algebra.md"
+++

### Definition
The **unitary Lie algebra** $\mathfrak{u}(n)$ is the Lie algebra of the [[lie-groups/unitary-group|unitary group $U(n)$]]. Concretely,
$$
\mathfrak{u}(n)=\{X\in M_n(\mathbb C)\mid X^\ast+X=0\},
$$

with Lie bracket $[X,Y]=XY-YX$.

It is a real Lie algebra of dimension $\dim_\mathbb{R}\mathfrak{u}(n)=n^2$.

### Center and derived subalgebra
The center is
$$
Z(\mathfrak{u}(n))=\{i t\,I_n\mid t\in\mathbb R\},
$$
since scalar matrices commute with everything, and skew-Hermitian forces the scalar to be purely imaginary (compare [[lie-groups/center-of-a-lie-algebra|the center of a Lie algebra]]). The [[lie-groups/derived-subalgebra|derived subalgebra]] satisfies
$$
[\mathfrak{u}(n),\mathfrak{u}(n)]=\mathfrak{su}(n),
$$

where $\mathfrak{su}(n)$ is the [[lie-groups/special-unitary-lie-algebra|special unitary Lie algebra]].

### Context
As the Lie algebra of a compact Lie group, $\mathfrak{u}(n)$ is reductive in the sense of [[lie-groups/lie-algebra-compact-is-reductive|compact Lie algebras are reductive]]: it splits as a direct sum of its center and a semisimple ideal (here $\mathfrak{su}(n)$). This decomposition is ubiquitous in unitary representation theory.
