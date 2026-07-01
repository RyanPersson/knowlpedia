+++
id = "quantum-foundations/self-adjoint-operator-observable"
title = "Self-Adjoint Operator (Observable)"
kind = "knowl"
summary = "A linear operator equal to its adjoint; in quantum theory it represents an observable with real measurement outcomes."
aliases = ["self-adjoint-operator-observable", "Self-Adjoint Operator (Observable)"]
domains = ["quantum-foundations"]
legacy_source_path = "quantum-foundations/self-adjoint-operator-observable.md"
+++

Let \(H\) be a complex Hilbert space and let \(A:H\to H\) be a bounded operator (see [[quantum-foundations/bounded-operator-hilbert|Bounded Operator Hilbert]]). The operator \(A\) is **self-adjoint** (or **Hermitian**) if
\[
A = A^\ast,
\]
where \(A^\ast\) is the adjoint defined by
\[
\langle x,Ay\rangle = \langle A^\ast x,y\rangle \quad \text{for all } x,y\in H.
\]

In (finite-dimensional) quantum mechanics, self-adjoint operators are used to represent **observables** (measurable quantities).

## Equivalent condition
\(A\) is self-adjoint if and only if
\[
\langle x,Ay\rangle = \langle Ax,y\rangle \quad \text{for all } x,y\in H.
\]

## Spectral properties in finite dimension
If \(H\) is finite-dimensional ([[quantum-foundations/complex-hilbert-space-finite|Complex Hilbert Space Finite]]), then:

- All eigenvalues of \(A\) are real.
- Eigenvectors corresponding to distinct eigenvalues are orthogonal.
- \(A\) is unitarily diagonalizable: there exists an orthonormal basis of eigenvectors.

Equivalently, \(A\) admits a spectral decomposition as in [[quantum-foundations/spectrum-self-adjoint-finite|Spectrum Self Adjoint Finite]].

## Expectation values and measurement
Given a quantum state \(\rho\) (a [[quantum-foundations/density-operator|Density Operator]]), the expectation value of the observable \(A\) is
\[
\mathbb{E}_\rho[A] = \operatorname{Tr}(\rho A),
\]
where \(\operatorname{Tr}\) is the operator trace ([[quantum-foundations/trace-operator|Trace Operator]]).

In a pure state \(|\psi\rangle\) (unit vector), the corresponding density operator is \(\rho = |\psi\rangle\langle \psi|\), and the expectation becomes
\[
\mathbb{E}_\psi[A] = \langle \psi, A\psi\rangle.
\]

## Note on unbounded observables
In infinite-dimensional quantum theory, important observables (like position and momentum) are often unbounded. Then “self-adjoint” requires careful domain conditions. This knowl focuses on the bounded (and in particular finite-dimensional) setting.
