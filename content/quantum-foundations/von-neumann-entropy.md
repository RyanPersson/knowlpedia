---
title: "Von Neumann entropy"
description: "Entropy of a quantum state defined as minus the trace of rho log rho."
---

Let \(\rho\) be a {{< knowl id="density-operator" >}} on a finite-dimensional Hilbert space \(H\). The **von Neumann entropy** of \(\rho\) is
\[
S(\rho) := -\operatorname{Tr}(\rho \log \rho).
\]
Here \(\log \rho\) is defined by functional calculus via the spectral decomposition of \(\rho\) (see {{< knowl id="spectrum-self-adjoint-finite" >}}). By convention, eigenvalues equal to \(0\) contribute \(0\log 0 := 0\).

### Eigenvalue formula
If \(\rho\) has eigenvalues \(p_1,\dots,p_d\) (with \(p_i\ge 0\) and \(\sum_i p_i=1\)), then
\[
S(\rho) = -\sum_{i=1}^d p_i \log p_i.
\]
Unless specified otherwise, \(\log\) denotes the natural logarithm; changing the logarithm base rescales the entropy by a constant factor.

### Basic facts
Let \(d=\dim H\).
- **Bounds:** \(0 \le S(\rho)\le \log d\).
- **Pure states:** \(S(\rho)=0\) iff \(\rho\) is {{< knowl id="pure-state-quantum" >}}.
- **Maximally mixed state:** \(S(I/d)=\log d\).
- **Unitary invariance:** \(S(U\rho U^\ast)=S(\rho)\) for any unitary \(U\).
- **Additivity for product states:** if \(\rho_{AB}=\rho_A\otimes \rho_B\), then \(S(\rho_{AB})=S(\rho_A)+S(\rho_B)\).

### Classical reduction
If \(\rho\) is diagonal in some orthonormal basis with diagonal entries \(p_1,\dots,p_d\), then \(S(\rho)\) equals the Shannon entropy of the probability vector \((p_i)\).

### Subsystems and entanglement entropy
For a bipartite state \(\rho_{AB}\), the reduced state \(\rho_A=\operatorname{Tr}_B(\rho_{AB})\) is defined using the {{< knowl id="partial-trace" >}}. When \(\rho_{AB}\) is pure, the quantities \(S(\rho_A)\) and \(S(\rho_B)\) coincide and quantify entanglement between \(A\) and \(B\).
