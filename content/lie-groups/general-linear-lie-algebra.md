---
title: "General linear Lie algebra"
description: "The Lie algebra gl(V) of all endomorphisms with commutator bracket."
---

Let $V$ be a finite-dimensional real or complex vector space.

**Definition (General linear Lie algebra).**  
The **general linear Lie algebra** is the vector space
\[
\mathfrak{gl}(V)=\mathrm{End}(V)
\]
equipped with the commutator {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}}
\[
[X,Y]=XY-YX.
\]
After choosing a basis, $\mathfrak{gl}(V)\cong \mathfrak{gl}_n(\mathbb F)=M_n(\mathbb F)$ with the same bracket.

**Relation to the group $\mathrm{GL}(V)$.**  
If $G=\mathrm{GL}(V)$ is the {{< knowl id="general-linear-group" text="general linear group" >}}, then $\mathfrak{gl}(V)$ is naturally the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of G" >}}, identified with $T_I G$; under this identification, the Lie bracket on $\mathfrak g$ agrees with the commutator bracket.

**Useful subalgebras.**  
The trace map $\mathrm{tr}:\mathfrak{gl}_n(\mathbb F)\to\mathbb F$ is a Lie algebra homomorphism to the abelian Lie algebra $(\mathbb F,0)$, and its kernel is {{< knowl id="special-linear-lie-algebra" text="sl_n" >}}. The center is the scalar matrices, matching {{< knowl id="center-of-a-lie-algebra" text="the center" >}} description $Z(\mathfrak{gl}_n)=\mathbb F\cdot I$.

**Context.**  
Representations of Lie groups and Lie algebras are, by definition, maps into some $\mathfrak{gl}(V)$ (see {{< knowl id="representation-of-a-lie-algebra" text="representation of a Lie algebra" >}} and {{< knowl id="representation-of-a-lie-group" text="representation of a Lie group" >}}).
