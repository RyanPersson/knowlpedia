---
title: "General linear group"
description: "The Lie group GL(V) of invertible linear maps on a finite-dimensional vector space."
---

Let $V$ be a finite-dimensional real or complex vector space.

**Definition (General linear group).**  
The **general linear group** of $V$ is
\[
\mathrm{GL}(V)=\{A:V\to V \text{ linear and invertible}\},
\]
with group operation given by composition. After choosing a basis, $\mathrm{GL}(V)\cong \mathrm{GL}_n(\mathbb F)$ where $\mathbb F=\mathbb R$ or $\mathbb C$ and
\[
\mathrm{GL}_n(\mathbb F)=\{A\in M_n(\mathbb F):\det(A)\ne 0\}.
\]

**Lie group structure.**  
Viewed as a subset of the affine space $M_n(\mathbb F)$, $\mathrm{GL}_n(\mathbb F)$ is open (since $\det$ is continuous and $\mathbb F^\times$ is open), hence it is a smooth manifold and a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}. Its Lie algebra is the {{< knowl id="general-linear-lie-algebra" text="general linear Lie algebra" >}} $\mathfrak{gl}_n(\mathbb F)$, identified with $T_I\mathrm{GL}_n(\mathbb F)$ (compare {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}).

**Basic structure.**  
Over $\mathbb C$, $\mathrm{GL}_n(\mathbb C)$ is connected. Over $\mathbb R$, $\mathrm{GL}_n(\mathbb R)$ has two connected components distinguished by the sign of $\det$. The {{< knowl id="exponential-map-lie-group" text="exponential map" >}} is the matrix exponential $\exp:\mathfrak{gl}_n(\mathbb F)\to \mathrm{GL}_n(\mathbb F)$.

**Context.**  
Many linear representations of Lie groups are concretely {{< knowl id="lie-group-homomorphism" text="homomorphisms" >}} into some $\mathrm{GL}(V)$; special subgroups such as {{< knowl id="special-linear-group" text="SL_n" >}}, {{< knowl id="orthogonal-group" text="O(n)" >}}, and {{< knowl id="unitary-group" text="U(n)" >}} are defined by additional algebraic constraints.
