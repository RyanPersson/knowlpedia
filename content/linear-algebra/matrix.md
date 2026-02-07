---
title: "Matrix"
description: "A rectangular array of numbers, symbols, or expressions arranged in rows and columns."
---

A **matrix** is a rectangular array of entries (typically from a {{< knowl id="ring" section="algebra-rings" text="ring" >}} or {{< knowl id="field" section="algebra-rings" text="field" >}}) arranged in rows and columns.

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

Matrices represent {{< knowl id="linear-map" text="linear maps" >}} between finite-dimensional {{< knowl id="vector-space" text="vector spaces" >}} once bases are chosen.
