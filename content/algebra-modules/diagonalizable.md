---
title: "Diagonalizable operator"
description: "A linear operator that has a basis of eigenvectors."
---

A {{< knowl id="linear-map" section="linear-algebra" text="linear operator" >}} \(T: V \to V\) on a finite-dimensional {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}} is **diagonalizable** if there exists a {{< knowl id="basis-module" text="basis" >}} of \(V\) consisting entirely of {{< knowl id="eigenvector" section="linear-algebra" text="eigenvectors" >}} of \(T\).

Equivalently, \(T\) is diagonalizable iff its {{< knowl id="matrix-representation" text="matrix representation" >}} in some basis is diagonal.

## Characterizations
The following are equivalent:

1. \(T\) is diagonalizable.
2. \(V = \bigoplus_{\lambda} E_\lambda\) where \(E_\lambda\) is the eigenspace for eigenvalue \(\lambda\).
3. The sum of geometric multiplicities equals \(\dim V\).
4. The {{< knowl id="minimal-polynomial" section="linear-algebra" text="minimal polynomial" >}} of \(T\) splits into distinct linear factors.

## Over algebraically closed fields
If the {{< knowl id="characteristic-polynomial" section="linear-algebra" text="characteristic polynomial" >}} has distinct roots, then \(T\) is diagonalizable. More generally, \(T\) is diagonalizable iff each eigenvalue's geometric multiplicity equals its algebraic multiplicity.

## Examples
- Any operator with \(n\) distinct eigenvalues (where \(\dim V = n\)).
- Self-adjoint operators on inner product spaces.
- Projections.

## Non-example
The matrix \(\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\) is not diagonalizable (only one eigenvector).
