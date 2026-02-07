---
title: "Reductive Lie algebra"
description: "A Lie algebra that decomposes as a direct sum of its center and a semisimple ideal."
---

A {{< knowl id="lie-algebra" text="Lie algebra" >}} \(\mathfrak{g}\) is **reductive** if it can be written as
$$
\mathfrak{g} = Z(\mathfrak{g}) \oplus [\mathfrak{g}, \mathfrak{g}]
$$
where \(Z(\mathfrak{g})\) is the center and \([\mathfrak{g}, \mathfrak{g}]\) is the derived algebra.

## Equivalent characterizations
The following are equivalent for a finite-dimensional Lie algebra over a field of characteristic zero:

1. \(\mathfrak{g}\) is reductive.
2. The {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}} is completely reducible.
3. \(\mathfrak{g}\) is a direct sum of simple and abelian Lie algebras.
4. Every finite-dimensional {{< knowl id="representation-of-a-lie-algebra" text="representation" >}} is completely reducible.

## Examples
- Semisimple Lie algebras (center is trivial).
- Abelian Lie algebras (derived algebra is trivial).
- \(\mathfrak{gl}_n\): center is scalar matrices, derived algebra is \(\mathfrak{sl}_n\).
- \(\mathfrak{u}(n) = i\mathfrak{u}(1) \oplus \mathfrak{su}(n)\).

## Non-example
The Lie algebra of upper triangular matrices is not reductive (it is solvable but not semisimple).
