---
title: "Monotonicity of quantum relative entropy"
description: "Quantum relative entropy cannot increase under completely positive trace-preserving maps (data processing inequality)."
---

Quantum relative entropy is the operator-algebraic analogue of {{< knowl id="relative-entropy-kl-divergence" section="probability" text="Kullback–Leibler divergence" >}} for {{< knowl id="density-operator" section="quantum-foundations" text="density operators" >}}.

For density operators $\rho,\sigma$ on the same finite-dimensional Hilbert space, define
$$
D(\rho\|\sigma)=
\begin{cases}
\mathrm{Tr}\big[\rho(\log\rho-\log\sigma)\big], & \mathrm{supp}(\rho)\subseteq \mathrm{supp}(\sigma),\\
+\infty, & \text{otherwise.}
\end{cases}
$$

## Statement (data processing inequality)
For every completely positive trace-preserving (CPTP) map (quantum channel) $\Phi$,
$$
D\big(\Phi(\rho)\,\|\,\Phi(\sigma)\big)\le D(\rho\|\sigma).
$$

## Key hypotheses
- $\rho,\sigma$ are density operators; if $\mathrm{supp}(\rho)\nsubseteq \mathrm{supp}(\sigma)$ then $D(\rho\|\sigma)=+\infty$ by convention.
- $\Phi$ is linear, completely positive, and trace-preserving (CPTP).

## Key conclusions
- **Information cannot increase under coarse-graining:** processing, measuring, adding noise, or discarding subsystems cannot increase $D$.
- **Partial trace case:** for bipartite states $\rho_{AB},\sigma_{AB}$,
  $$
  D(\rho_{AB}\|\sigma_{AB}) \ge D(\rho_A\|\sigma_A),
  $$

  where $\rho_A=\mathrm{Tr}_B\rho_{AB}$ and similarly for $\sigma_A$.
- **Nonnegativity:** choosing $\Phi$ to be a constant channel gives $0 = D(\Phi(\rho)\|\Phi(\sigma)) \le D(\rho\|\sigma)$, hence $D(\rho\|\sigma)\ge 0$.
- The inequality implies standard entropy consequences such as {{< knowl id="prop-von-neumann-entropy-concave" text="concavity of the von Neumann entropy" >}}.

