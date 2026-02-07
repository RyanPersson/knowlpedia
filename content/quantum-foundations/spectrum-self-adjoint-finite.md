---
title: "Spectrum of a Self-Adjoint Operator in Finite Dimension"
description: "For a finite-dimensional self-adjoint operator, the spectrum is exactly the set of its real eigenvalues and yields a spectral decomposition."
---

Let \(H\) be a finite-dimensional complex Hilbert space ({{< knowl id="complex-hilbert-space-finite" text="Complex Hilbert Space Finite" >}}) and let \(A:H\to H\) be self-adjoint ({{< knowl id="self-adjoint-operator-observable" text="Self Adjoint Operator Observable" >}}).

## Spectrum in finite dimension
In finite dimension, the **spectrum** of \(A\) is the set of scalars \(\lambda\in\mathbb{C}\) for which \(A-\lambda I\) is not invertible. Equivalently, the spectrum is exactly the set of {{< knowl id="eigenvalue" section="linear-algebra" text="Eigenvalue" >}}s of \(A\).

For self-adjoint \(A\), all eigenvalues (hence all spectral values) are **real**.

## Spectral theorem (finite-dimensional form)
There exist distinct real eigenvalues \(\lambda_1,\dots,\lambda_m\) and orthogonal projections \(P_1,\dots,P_m\) onto the corresponding eigenspaces such that:

1. \(P_iP_j = 0\) for \(i\ne j\),
2. \(\sum_{i=1}^m P_i = I\),
3. \(A\) decomposes as
   \[
   A = \sum_{i=1}^m \lambda_i P_i.
   \]

The projections \(P_i\) are uniquely determined by \(A\) (they are the spectral projectors).

## Functional calculus
For any function \(f\) defined on the spectrum \(\{\lambda_i\}\), one defines
\[
f(A) := \sum_{i=1}^m f(\lambda_i)\,P_i.
\]
Common examples include powers \(A^k\), the exponential \(e^{A}\), and \(\log(A)\) when \(A\) is positive definite on its support.

## Quantum interpretation
If \(A\) is an observable, then the possible measurement outcomes are its spectral values \(\lambda_i\). In a state \(\rho\) ({{< knowl id="density-operator" text="Density Operator" >}}), the Born rule assigns outcome probabilities
\[
\Pr(\lambda_i) = \operatorname{Tr}(\rho P_i),
\]
using the operator trace ({{< knowl id="trace-operator" text="Trace Operator" >}}).
