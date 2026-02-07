---
title: "Quantum relative entropy"
description: "Noncommutative generalization of Kullback-Leibler divergence for density operators."
---

Let \(\rho\) and \(\sigma\) be {{< knowl id="density-operator" >}}s on a finite-dimensional Hilbert space \(H\). The **quantum relative entropy** (also called Umegaki relative entropy) is defined by
\[
D(\rho\|\sigma) :=
\begin{cases}
\operatorname{Tr}\!\big(\rho(\log\rho-\log\sigma)\big), & \text{if }\operatorname{supp}(\rho)\subseteq \operatorname{supp}(\sigma),\\[4pt]
+\infty, & \text{otherwise.}
\end{cases}
\]
The support condition is needed because \(\log\sigma\) is not finite on the kernel of \(\sigma\). The operators \(\log\rho\) and \(\log\sigma\) are defined via spectral calculus (see {{< knowl id="spectrum-self-adjoint-finite" >}}).

### Classical (commuting) case
If \(\rho\) and \(\sigma\) commute, they are simultaneously diagonalizable and the formula reduces to the classical relative entropy (Kullback-Leibler divergence) of their eigenvalue distributions; compare {{< knowl id="relative-entropy-kl-divergence" section="probability" >}}.

### Key properties
- **Nonnegativity (Klein inequality):** \(D(\rho\|\sigma)\ge 0\), with equality iff \(\rho=\sigma\).
- **Not symmetric:** typically \(D(\rho\|\sigma)\ne D(\sigma\|\rho)\); it is not a metric.
- **Data processing inequality:** for any completely positive trace-preserving map \(\Phi\),
  \[
  D(\rho\|\sigma)\ \ge\ D(\Phi(\rho)\|\Phi(\sigma)).
  \]
  In particular, taking \(\Phi=\operatorname{Tr}_B\) (see {{< knowl id="partial-trace" >}}) gives
  \[
  D(\rho_{AB}\|\sigma_{AB})\ \ge\ D(\rho_A\|\sigma_A),
  \quad \rho_A=\operatorname{Tr}_B(\rho_{AB}),\ \sigma_A=\operatorname{Tr}_B(\sigma_{AB}).
  \]

### Relation to von Neumann entropy
If \(d=\dim H\) and \(\tau=I/d\) is the maximally mixed state, then
\[
D(\rho\|\tau)=\log d - S(\rho),
\]
where \(S(\rho)\) is the {{< knowl id="von-neumann-entropy" >}}.
