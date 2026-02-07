---
title: "Abelian Lie algebra"
description: "A Lie algebra whose bracket vanishes identically."
---

Let $\mathfrak{g}$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}} over a field $\Bbbk$ with {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}} $[\cdot,\cdot]$.

**Definition.** $\mathfrak{g}$ is **abelian** if
$$
[x,y]=0 \quad \text{for all } x,y\in \mathfrak{g}.
$$

Equivalently, the {{< knowl id="derived-subalgebra" text="derived subalgebra" >}} satisfies $[\mathfrak{g},\mathfrak{g}]=0$, and the {{< knowl id="center-of-a-lie-algebra" text="center" >}} satisfies $Z(\mathfrak{g})=\mathfrak{g}$. In representation-theoretic terms, the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}} $\operatorname{ad}:\mathfrak{g}\to \mathfrak{gl}(\mathfrak{g})$ is the zero map.

**Context.** Abelian Lie algebras are the “linearized” version of commutative groups: if $G$ is an {{< knowl id="abelian-lie-group" text="abelian Lie group" >}}, then its {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" >}} $\mathfrak{g}$ is abelian. Conversely, for connected $G$, abelianness of $\mathfrak{g}$ forces the {{< knowl id="commutator-subgroup-of-a-lie-group" text="commutator subgroup" >}} to be discrete, hence trivial, so $G$ is abelian.
