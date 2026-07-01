+++
id = "linear-algebra/matrix"
title = "Matrix"
kind = "knowl"
summary = "A rectangular array of numbers, symbols, or expressions arranged in rows and columns."
aliases = ["matrix"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/matrix.md"
+++

A **matrix** is a rectangular array of entries (typically from a [[algebra-rings/ring|ring]] or [[algebra-rings/field|field]]) arranged in rows and columns.

An \(m \times n\) matrix \(A\) has \(m\) rows and \(n\) columns, written
$$
A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}.
$$

The entry in row \(i\) and column \(j\) is denoted \(a_{ij}\) or \(A_{ij}\).

## Operations
- **Addition**: \((A + B)_{ij} = A_{ij} + B_{ij}\) (requires same dimensions).
- **Scalar multiplication**: \((cA)_{ij} = c \cdot A_{ij}\).
- **Matrix multiplication**: \((AB)_{ij} = \sum_k A_{ik} B_{kj}\) (requires compatible dimensions).

## Special matrices
- **Square matrix**: \(m = n\).
- **Identity matrix**: \(I_n\) with \(1\)s on diagonal, \(0\)s elsewhere.
- **Zero matrix**: All entries are \(0\).
- **Diagonal matrix**: Non-zero entries only on the main diagonal.
- **Symmetric matrix**: \(A = A^T\) (equals its transpose).

Matrices represent [[linear-algebra/linear-map|linear maps]] between finite-dimensional [[linear-algebra/vector-space|vector spaces]] once bases are chosen.
