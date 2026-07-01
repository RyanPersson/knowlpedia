+++
id = "stat-mech/corollary-relative-fluctuations-vanish"
title = "Vanishing of relative fluctuations in the thermodynamic limit"
kind = "knowl"
summary = "Under extensivity, canonical energy fluctuations are O(N) and relative fluctuations are O(N^{-1/2}), hence vanish as system size grows."
aliases = ["corollary-relative-fluctuations-vanish", "Vanishing of relative fluctuations in the thermodynamic limit"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/corollary-relative-fluctuations-vanish.md"
+++

## Statement (self-averaging of extensive observables)
Consider a sequence of systems of size $N$ (or volume $|\Lambda|$) in the [[stat-mech/canonical-ensemble|canonical ensemble]] at fixed temperature $T$, with Hamiltonian $H_N$.

Assume the mean energy and constant-volume heat capacity are extensive:
- $\langle H_N\rangle = \Theta(N)$,
- $C_V(N) = \Theta(N)$, where $C_V(N)=\left(\frac{\partial \langle H_N\rangle}{\partial T}\right)_{V,N}$.

Then
$$
\frac{\sqrt{\operatorname{Var}(H_N)}}{\langle H_N\rangle} \;=\; O(N^{-1/2}) \quad \text{as } N\to\infty,
$$
so the relative energy fluctuations vanish:
$$
\frac{\sqrt{\operatorname{Var}(H_N)}}{\langle H_N\rangle}\;\longrightarrow\;0.
$$

## Key hypotheses
- Canonical equilibrium is well-defined for each $N$ (finite partition function).
- Extensivity: $\langle H_N\rangle$ and $C_V(N)$ scale linearly in $N$ (away from anomalous regimes such as critical points where scaling may change).
- Smoothness in $T$ sufficient to define $C_V(N)$.

## Conclusions
- Energy is *self-averaging*: typical fluctuations are negligible compared to the mean at large $N$.
- Quantitative scaling:
  $$
  \operatorname{Var}(H_N)=k_B T^2 C_V(N)=\Theta(N),\qquad \sqrt{\operatorname{Var}(H_N)}=\Theta(\sqrt{N}).
  $$
- This provides a basic mechanism behind [[stat-mech/ensemble-equivalence-theorem|equivalence of ensembles]] for macroscopic observables.

## Cross-links (definitions and supporting results)
- [[stat-mech/corollary-energy-fluctuations-cv|energy fluctuations vs. C_V]]
- [[stat-mech/canonical-energy-fluctuation-identity|canonical energy fluctuation identity]]
- [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]]
- [[stat-mech/large-deviation-equilibrium|large-deviation characterization of equilibrium]]
- [[large-deviations/large-deviation-principle|large deviation principle]]
