+++
id = "lie-groups/abelian-lie-algebra"
title = "Abelian Lie algebra"
kind = "knowl"
summary = "A Lie algebra whose bracket vanishes identically."
aliases = ["abelian-lie-algebra", "Abelian Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/abelian-lie-algebra.md"
+++

Let $\mathfrak{g}$ be a [[lie-groups/lie-algebra|Lie algebra]] over a field $\Bbbk$ with [[fiber-bundles/lie-bracket|Lie bracket]] $[\cdot,\cdot]$.

**Definition.** $\mathfrak{g}$ is **abelian** if
$$
[x,y]=0 \quad \text{for all } x,y\in \mathfrak{g}.
$$

Equivalently, the [[lie-groups/derived-subalgebra|derived subalgebra]] satisfies $[\mathfrak{g},\mathfrak{g}]=0$, and the [[lie-groups/center-of-a-lie-algebra|center]] satisfies $Z(\mathfrak{g})=\mathfrak{g}$. In representation-theoretic terms, the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] $\operatorname{ad}:\mathfrak{g}\to \mathfrak{gl}(\mathfrak{g})$ is the zero map.

**Context.** Abelian Lie algebras are the “linearized” version of commutative groups: if $G$ is an [[lie-groups/abelian-lie-group|abelian Lie group]], then its [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]] $\mathfrak{g}$ is abelian. Conversely, for connected $G$, abelianness of $\mathfrak{g}$ forces the [[lie-groups/commutator-subgroup-of-a-lie-group|commutator subgroup]] to be discrete, hence trivial, so $G$ is abelian.
