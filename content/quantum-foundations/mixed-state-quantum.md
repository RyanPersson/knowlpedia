---
title: "Mixed quantum state"
description: "A quantum state described by a density operator that is not a rank-one projector."
---

A **mixed quantum state** on a finite-dimensional complex Hilbert space \(H\) is a {{< knowl id="density-operator" >}} \(\rho\) that is **not** pure (see {{< knowl id="pure-state-quantum" >}}). Concretely, \(\rho\) is mixed iff it cannot be written as \(|\psi\rangle\langle\psi|\) for any unit vector \(\psi\).

### Equivalent characterizations (finite dimension)
For a density operator \(\rho\), the following are equivalent:
- \(\rho\) is **mixed**.
- \(\rho\) has rank \(\ge 2\).
- \(\rho^2 \ne \rho\).
- \(\operatorname{Tr}(\rho^2) < 1\).
- The {{< knowl id="von-neumann-entropy" >}} satisfies \(S(\rho) > 0\).

### Convex mixture form
Every density operator admits a decomposition as a convex combination of pure states:
\[
\rho = \sum_i p_i\, |\psi_i\rangle\langle\psi_i|,
\quad p_i\ge 0,\ \sum_i p_i=1.
\]
This decomposition is generally **not unique**. A distinguished choice is the spectral decomposition, where the \(|\psi_i\rangle\) are orthonormal eigenvectors and the \(p_i\) are eigenvalues.

### How mixed states arise
Mixed states appear in (at least) two mathematically distinct ways:
- **Classical uncertainty (statistical mixture):** the system is prepared in pure state \(|\psi_i\rangle\) with probability \(p_i\).
- **Reduced state of a larger system:** if \(\rho_{AB}\) is a state on \(H_A\otimes H_B\), then the subsystem state
  \[
  \rho_A = \operatorname{Tr}_B(\rho_{AB})
  \]
  obtained by the {{< knowl id="partial-trace" >}} can be mixed even when \(\rho_{AB}\) is pure (entanglement).

### Special cases
- **Maximally mixed state:** on \(d=\dim H\),
  \[
  \rho_* = \frac{I}{d},
  \]
  which has the largest von Neumann entropy \(S(\rho_*)=\log d\).
