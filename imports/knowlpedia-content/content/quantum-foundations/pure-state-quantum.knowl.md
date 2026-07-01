+++
id = "quantum-foundations/pure-state-quantum"
title = "Pure quantum state"
kind = "knowl"
summary = "A quantum state represented by a rank-one projector onto a unit vector."
aliases = ["pure-state-quantum", "Pure quantum state"]
domains = ["quantum-foundations"]
legacy_source_path = "quantum-foundations/pure-state-quantum.md"
+++

Let \(H\) be a (finite-dimensional) complex Hilbert space (see [[quantum-foundations/complex-hilbert-space-finite|complex-hilbert-space-finite]]). A **pure quantum state** can be specified in either of two equivalent ways:

1. **State vector (ray):** a unit vector \(\psi \in H\) with \(\|\psi\|=1\), where \(\psi\) and \(e^{i\theta}\psi\) represent the same physical state (global phase is unobservable).

2. **Density operator (projector):** the rank-one operator
\[
\rho_\psi = |\psi\rangle\langle\psi|,
\]
which is a [[quantum-foundations/density-operator|density-operator]] (positive semidefinite with trace \(1\)).

### Equivalent characterizations (finite dimension)
For a density operator \(\rho\) on \(H\), the following are equivalent:
- \(\rho\) is **pure**.
- \(\rho\) has rank \(1\).
- \(\rho^2=\rho\) (idempotent projector).
- \(\operatorname{Tr}(\rho^2)=1\) (maximal “purity” among states).
- The eigenvalues of \(\rho\) are \(\{1,0,\dots,0\}\).

### Expectation values
If \(A\) is an observable (a self-adjoint operator; see [[quantum-foundations/self-adjoint-operator-observable|self-adjoint-operator-observable]]), then in the pure state \(\psi\),
\[
\langle A\rangle_\psi = \langle \psi, A\psi\rangle
\qquad\text{and equivalently}\qquad
\langle A\rangle_\psi = \operatorname{Tr}(\rho_\psi A).
\]

Pure states are the extreme points of the convex set of all density operators; mixtures of distinct pure states produce [[quantum-foundations/mixed-state-quantum|mixed-state-quantum]].
