---
title: "Pure quantum state"
description: "A quantum state represented by a rank-one projector onto a unit vector."
---

Let \(H\) be a (finite-dimensional) complex Hilbert space (see {{< knowl id="complex-hilbert-space-finite" >}}). A **pure quantum state** can be specified in either of two equivalent ways:

1. **State vector (ray):** a unit vector \(\psi \in H\) with \(\|\psi\|=1\), where \(\psi\) and \(e^{i\theta}\psi\) represent the same physical state (global phase is unobservable).

2. **Density operator (projector):** the rank-one operator
\[
\rho_\psi = |\psi\rangle\langle\psi|,
\]
which is a {{< knowl id="density-operator" >}} (positive semidefinite with trace \(1\)).

### Equivalent characterizations (finite dimension)
For a density operator \(\rho\) on \(H\), the following are equivalent:
- \(\rho\) is **pure**.
- \(\rho\) has rank \(1\).
- \(\rho^2=\rho\) (idempotent projector).
- \(\operatorname{Tr}(\rho^2)=1\) (maximal “purity” among states).
- The eigenvalues of \(\rho\) are \(\{1,0,\dots,0\}\).

### Expectation values
If \(A\) is an observable (a self-adjoint operator; see {{< knowl id="self-adjoint-operator-observable" >}}), then in the pure state \(\psi\),
\[
\langle A\rangle_\psi = \langle \psi, A\psi\rangle
\qquad\text{and equivalently}\qquad
\langle A\rangle_\psi = \operatorname{Tr}(\rho_\psi A).
\]

Pure states are the extreme points of the convex set of all density operators; mixtures of distinct pure states produce {{< knowl id="mixed-state-quantum" >}}.
