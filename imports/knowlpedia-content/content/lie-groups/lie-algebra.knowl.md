+++
id = "lie-groups/lie-algebra"
title = "Lie Algebra"
kind = "knowl"
summary = "A vector space with a bilinear bracket operation that is antisymmetric and satisfies the Jacobi identity."
aliases = ["lie-algebra", "Lie Algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-algebra.md"
+++

A **Lie algebra** is a [[linear-algebra/vector-space|vector space]] \(\mathfrak{g}\) (typically over \(\mathbb{R}\) or \(\mathbb{C}\)) equipped with a bilinear map
$$
[\ ,\ ]:\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g},
$$
called the [[fiber-bundles/lie-bracket|Lie bracket]], such that for all \(X,Y,Z\in\mathfrak{g}\):
1. **Alternating / antisymmetry:** \([X,X]=0\) (equivalently \([X,Y]=-[Y,X]\)).
2. **Jacobi identity:**
$$
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
$$

## Examples
- Any associative algebra becomes a Lie algebra with commutator \([A,B]=AB-BA\), e.g. matrix Lie algebras \(\mathfrak{gl}(n,\mathbb{R})\).
- The space of [[fiber-bundles/vector-field|vector fields]] on a manifold with the commutator bracket.
- An [[lie-groups/abelian-lie-algebra|abelian Lie algebra]] is one with \([X,Y]=0\) for all \(X,Y\).

## Maps and structure
A structure-preserving map is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]; bijective ones are [[lie-groups/lie-algebra-isomorphism|isomorphisms]].

Important substructures include [[lie-groups/lie-subalgebra|Lie subalgebras]], [[lie-groups/ideal-of-lie-algebra|ideals]], and the [[lie-groups/center-of-a-lie-algebra|center]].

Many classification notions are defined in terms of the bracket, such as
[[lie-groups/solvable-lie-algebra|solvable]],
[[lie-groups/nilpotent-lie-algebra|nilpotent]],
[[lie-groups/semisimple-lie-algebra|semisimple]],
[[lie-groups/simple-lie-algebra|simple]], and
[[lie-groups/reductive-lie-algebra|reductive]] Lie algebras.
