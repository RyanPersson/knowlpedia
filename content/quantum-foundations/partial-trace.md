---
title: "Partial trace"
description: "Linear map that traces out one tensor factor to produce a reduced operator."
---

Let \(H_A\) and \(H_B\) be finite-dimensional complex Hilbert spaces, and let \(X\) be an operator on the tensor product \(H_A\otimes H_B\). The **partial trace over \(B\)** is the unique linear map
\[
\operatorname{Tr}_B:\ \mathcal{L}(H_A\otimes H_B)\to \mathcal{L}(H_A)
\]
characterized by the identity
\[
\operatorname{Tr}\!\big((M_A\otimes I_B)\,X\big)=\operatorname{Tr}\!\big(M_A\,\operatorname{Tr}_B(X)\big)
\quad\text{for all operators } M_A\in \mathcal{L}(H_A),
\]
where \(\operatorname{Tr}\) is the usual trace (see {{< knowl id="trace-operator" >}}).

### Basis formula
If \(\{\,|j\rangle\,\}\) is any orthonormal basis of \(H_B\), then
\[
\operatorname{Tr}_B(X)=\sum_j (I_A\otimes \langle j|)\,X\,(I_A\otimes |j\rangle).
\]
This expression is independent of the chosen orthonormal basis.

### Basic properties
For operators \(A\) on \(H_A\) and \(B\) on \(H_B\),
\[
\operatorname{Tr}_B(A\otimes B)=\operatorname{Tr}(B)\,A.
\]
More generally:
- \(\operatorname{Tr}_B\) is linear.
- \(\operatorname{Tr}(\operatorname{Tr}_B(X))=\operatorname{Tr}(X)\) (trace-preserving).
- \(\operatorname{Tr}_B\) is positive and completely positive.

### Reduced states
If \(\rho_{AB}\) is a {{< knowl id="density-operator" >}} on \(H_A\otimes H_B\), then
\[
\rho_A := \operatorname{Tr}_B(\rho_{AB})
\]
is a density operator on \(H_A\), called the **reduced state** (or marginal) of subsystem \(A\). Even when \(\rho_{AB}\) is a {{< knowl id="pure-state-quantum" >}}, the reduced state \(\rho_A\) can be {{< knowl id="mixed-state-quantum" >}}.

### Example: maximally entangled state
If \(\dim H_A=\dim H_B=d\) and
\[
|\Phi\rangle=\frac{1}{\sqrt d}\sum_{i=1}^d |i\rangle\otimes |i\rangle,
\quad \rho_{AB}=|\Phi\rangle\langle\Phi|,
\]
then \(\operatorname{Tr}_B(\rho_{AB})=I_A/d\) is maximally mixed.
