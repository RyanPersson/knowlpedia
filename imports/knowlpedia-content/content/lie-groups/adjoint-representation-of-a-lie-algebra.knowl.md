+++
id = "lie-groups/adjoint-representation-of-a-lie-algebra"
title = "Adjoint Representation of a Lie Algebra"
kind = "knowl"
summary = "The representation sending an element to the linear map given by bracketing with it."
aliases = ["adjoint-representation-of-a-lie-algebra", "Adjoint Representation of a Lie Algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/adjoint-representation-of-a-lie-algebra.md"
+++

Let \(\mathfrak{g}\) be a [[lie-groups/lie-algebra|Lie algebra]] with [[fiber-bundles/lie-bracket|Lie bracket]] \([\ ,\ ]\).
For \(X\in\mathfrak{g}\), define a linear map
$$
\operatorname{ad}_X:\mathfrak{g}\to \mathfrak{g},\qquad \operatorname{ad}_X(Y)=[X,Y].
$$
This gives a map
$$
\operatorname{ad}:\mathfrak{g}\to \mathfrak{gl}(\mathfrak{g}),\qquad X\mapsto \operatorname{ad}_X,
$$
called the **adjoint representation** of \(\mathfrak{g}\).

## Key property
The map \(\operatorname{ad}\) is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]:
$$
[\operatorname{ad}_X,\operatorname{ad}_Y]=\operatorname{ad}_{[X,Y]}
\quad\text{in}\quad \mathfrak{gl}(\mathfrak{g}).
$$
Thus \(\operatorname{ad}\) is a [[lie-groups/representation-of-a-lie-algebra|representation of a Lie algebra]] on the vector space \(\mathfrak{g}\).

## Kernel and center
\(\ker(\operatorname{ad})\) consists of elements commuting with everything, i.e. the [[lie-groups/center-of-a-lie-algebra|center]] \(Z(\mathfrak{g})\).

## Killing form
The [[lie-groups/killing-form|Killing form]] is defined by
$$
B(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y),
$$
using the [[linear-algebra/trace|trace]]. It is fundamental for [[lie-groups/semisimple-lie-algebra|semisimple Lie algebras]].

For a Lie group version, see [[lie-groups/adjoint-action-of-a-lie-group|adjoint action of a Lie group]].
