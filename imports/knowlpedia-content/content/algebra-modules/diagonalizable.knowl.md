+++
id = "algebra-modules/diagonalizable"
title = "Diagonalizable operator"
kind = "knowl"
summary = "A linear operator that has a basis of eigenvectors."
aliases = ["diagonalizable", "Diagonalizable operator"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/diagonalizable.md"
+++

A [[linear-algebra/linear-map|linear operator]] \(T: V \to V\) on a finite-dimensional [[linear-algebra/vector-space|vector space]] is **diagonalizable** if there exists a [[algebra-modules/basis-module|basis]] of \(V\) consisting entirely of [[linear-algebra/eigenvector|eigenvectors]] of \(T\).

Equivalently, \(T\) is diagonalizable iff its [[algebra-modules/matrix-representation|matrix representation]] in some basis is diagonal.

## Characterizations
The following are equivalent:

1. \(T\) is diagonalizable.
2. \(V = \bigoplus_{\lambda} E_\lambda\) where \(E_\lambda\) is the eigenspace for eigenvalue \(\lambda\).
3. The sum of geometric multiplicities equals \(\dim V\).
4. The [[linear-algebra/minimal-polynomial|minimal polynomial]] of \(T\) splits into distinct linear factors.

## Over algebraically closed fields
If the [[linear-algebra/characteristic-polynomial|characteristic polynomial]] has distinct roots, then \(T\) is diagonalizable. More generally, \(T\) is diagonalizable iff each eigenvalue's geometric multiplicity equals its algebraic multiplicity.

## Examples
- Any operator with \(n\) distinct eigenvalues (where \(\dim V = n\)).
- Self-adjoint operators on inner product spaces.
- Projections.

## Non-example
The matrix \(\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\) is not diagonalizable (only one eigenvector).
