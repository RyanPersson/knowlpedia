+++
id = "lie-groups/general-linear-lie-algebra"
title = "General linear Lie algebra"
kind = "knowl"
summary = "The Lie algebra gl(V) of all endomorphisms with commutator bracket."
aliases = ["general-linear-lie-algebra", "General linear Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/general-linear-lie-algebra.md"
+++

Let $V$ be a finite-dimensional real or complex vector space.

**Definition (General linear Lie algebra).**
The **general linear Lie algebra** is the vector space
\[
\mathfrak{gl}(V)=\mathrm{End}(V)
\]
equipped with the commutator [[fiber-bundles/lie-bracket|Lie bracket]]
\[
[X,Y]=XY-YX.
\]
After choosing a basis, $\mathfrak{gl}(V)\cong \mathfrak{gl}_n(\mathbb F)=M_n(\mathbb F)$ with the same bracket.

**Relation to the group $\mathrm{GL}(V)$.**
If $G=\mathrm{GL}(V)$ is the [[lie-groups/general-linear-group|general linear group]], then $\mathfrak{gl}(V)$ is naturally the [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of G]], identified with $T_I G$; under this identification, the Lie bracket on $\mathfrak g$ agrees with the commutator bracket.

**Useful subalgebras.**
The trace map $\mathrm{tr}:\mathfrak{gl}_n(\mathbb F)\to\mathbb F$ is a Lie algebra homomorphism to the abelian Lie algebra $(\mathbb F,0)$, and its kernel is [[lie-groups/special-linear-lie-algebra|sl_n]]. The center is the scalar matrices, matching [[lie-groups/center-of-a-lie-algebra|the center]] description $Z(\mathfrak{gl}_n)=\mathbb F\cdot I$.

**Context.**
Representations of Lie groups and Lie algebras are, by definition, maps into some $\mathfrak{gl}(V)$ (see [[lie-groups/representation-of-a-lie-algebra|representation of a Lie algebra]] and [[lie-groups/representation-of-a-lie-group|representation of a Lie group]]).
