+++
id = "lie-groups/representation-of-a-lie-group"
title = "Representation of a Lie Group"
kind = "knowl"
summary = "A smooth homomorphism from a Lie group to the group of invertible linear maps on a vector space."
aliases = ["representation-of-a-lie-group", "Representation of a Lie Group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/representation-of-a-lie-group.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] and \(V\) a finite-dimensional [[linear-algebra/vector-space|vector space]].
A **(linear) representation of \(G\)** is a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]]
$$
\rho: G \to \operatorname{GL}(V),
$$
where \(\operatorname{GL}(V)\) is the group of invertible [[linear-algebra/linear-operator|linear operators]] on \(V\).

Equivalently, \(\rho\) is a smooth action of \(G\) on \(V\) by linear isomorphisms, written \(g\cdot v := \rho(g)v\).

## Differentiating a representation
The differential at the identity gives a Lie algebra representation
$$
d\rho_e : \mathfrak{g} \to \mathfrak{gl}(V),
$$
which is a [[lie-groups/representation-of-a-lie-algebra|representation of the Lie algebra]] \(\mathfrak{g}=T_eG\); see
[[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]] and [[fiber-bundles/differential-of-a-smooth-map|differential]].

## Examples
- The defining representation \(\operatorname{GL}(n,\mathbb{R})\to \operatorname{GL}(\mathbb{R}^n)\).
- Orthogonal/unitary representations of \(\operatorname{SO}(n)\), \(\operatorname{SU}(n)\) on \(\mathbb{R}^n\), \(\mathbb{C}^n\).
- The [[lie-groups/adjoint-action-of-a-lie-group|adjoint representation]] \(G\to \operatorname{Aut}(\mathfrak{g})\).

Many structural notions for representations can be studied via the induced Lie algebra representation and tools such as the [[lie-groups/killing-form|Killing form]] in the semisimple case.
