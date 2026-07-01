+++
id = "lie-groups/reductive-lie-algebra"
title = "Reductive Lie algebra"
kind = "knowl"
summary = "A Lie algebra that decomposes as a direct sum of its center and a semisimple ideal."
aliases = ["reductive-lie-algebra", "Reductive Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/reductive-lie-algebra.md"
+++

A [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak{g}\) is **reductive** if it can be written as
$$
\mathfrak{g} = Z(\mathfrak{g}) \oplus [\mathfrak{g}, \mathfrak{g}]
$$
where \(Z(\mathfrak{g})\) is the center and \([\mathfrak{g}, \mathfrak{g}]\) is the derived algebra.

## Equivalent characterizations
The following are equivalent for a finite-dimensional Lie algebra over a field of characteristic zero:

1. \(\mathfrak{g}\) is reductive.
2. The [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] is completely reducible.
3. \(\mathfrak{g}\) is a direct sum of simple and abelian Lie algebras.
4. Every finite-dimensional [[lie-groups/representation-of-a-lie-algebra|representation]] is completely reducible.

## Examples
- Semisimple Lie algebras (center is trivial).
- Abelian Lie algebras (derived algebra is trivial).
- \(\mathfrak{gl}_n\): center is scalar matrices, derived algebra is \(\mathfrak{sl}_n\).
- \(\mathfrak{u}(n) = i\mathfrak{u}(1) \oplus \mathfrak{su}(n)\).

## Non-example
The Lie algebra of upper triangular matrices is not reductive (it is solvable but not semisimple).
