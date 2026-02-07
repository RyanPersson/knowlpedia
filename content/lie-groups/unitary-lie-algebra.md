---
title: "Unitary Lie algebra"
description: "The Lie algebra of : skew-Hermitian matrices with the commutator bracket."
---

### Definition
The **unitary Lie algebra** $\mathfrak{u}(n)$ is the Lie algebra of the {{< knowl id="unitary-group" text="unitary group $U(n)$" >}}. Concretely,
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
since scalar matrices commute with everything, and skew-Hermitian forces the scalar to be purely imaginary (compare {{< knowl id="center-of-a-lie-algebra" text="the center of a Lie algebra" >}}). The {{< knowl id="derived-subalgebra" text="derived subalgebra" >}} satisfies
$$
[\mathfrak{u}(n),\mathfrak{u}(n)]=\mathfrak{su}(n),
$$

where $\mathfrak{su}(n)$ is the {{< knowl id="special-unitary-lie-algebra" text="special unitary Lie algebra" >}}.

### Context
As the Lie algebra of a compact Lie group, $\mathfrak{u}(n)$ is reductive in the sense of {{< knowl id="lie-algebra-compact-is-reductive" text="compact Lie algebras are reductive" >}}: it splits as a direct sum of its center and a semisimple ideal (here $\mathfrak{su}(n)$). This decomposition is ubiquitous in unitary representation theory.
