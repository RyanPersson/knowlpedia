+++
id = "stat-mech-lattice/spontaneous-magnetization"
title = "Spontaneous magnetization"
kind = "knowl"
summary = "Nonzero magnetization in zero external field, defined via symmetry-breaking limits of Gibbs states in the thermodynamic limit."
aliases = ["spontaneous-magnetization", "Spontaneous magnetization"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/spontaneous-magnetization.md"
+++

Consider a lattice spin system with an [[stat-mech-lattice/external-field-coupling|external field coupling]] parameter $h\in\mathbb{R}$ (e.g. coupling to $\sum_x \sigma_x$). Let $\mu_{\beta,h}^{+}$ denote a translation-invariant [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]] selected by a *positive* field (or, equivalently in ferromagnets, by $+$ [[stat-mech-lattice/boundary-condition-lattice|boundary conditions]] and then taking volume $\to\infty$).

The **spontaneous magnetization** at inverse temperature $\beta$ is
$$
m_*(\beta)\;:=\;\lim_{h\downarrow 0}\,\mu_{\beta,h}^{+}(\sigma_0),
$$

provided the limit exists. For translation-invariant states, $\mu_{\beta,h}^{+}(\sigma_0)=\mu_{\beta,h}^{+}(\sigma_x)$ for all $x$.

Equivalently (when differentiability from the right holds), it is the right derivative at $h=0$ of the thermodynamic pressure:
$$
m_*(\beta)\;=\;\left.\frac{\partial}{\partial h}\,p(\beta,h)\right|_{h=0^+},
$$

where $p(\beta,h)$ is the [[stat-mech-lattice/pressure-lattice|pressure]] obtained as a [[stat-mech-lattice/thermodynamic-limit-pressure-lattice|thermodynamic limit]] of finite-volume pressures.

## Key properties
- **Order parameter:** $m_*(\beta)$ is a canonical [[stat-mech-lattice/order-parameter|order parameter]] for $\mathbb{Z}_2$-symmetric models such as the [[stat-mech-lattice/ising-model|Ising model]].
- **Symmetry selection:** In systems with spin-flip symmetry at $h=0$, one typically has
  $$
  \mu_{\beta,0}^{+}(\sigma_0)=+m_*(\beta),\qquad \mu_{\beta,0}^{-}(\sigma_0)=-m_*(\beta),
  $$

  for the $+$ and $-$ extremal states, when they exist (see [[stat-mech-lattice/extremal-gibbs-measure|extremal Gibbs measures]] and [[stat-mech-lattice/pure-phase|pure phases]]).
- **Phase transition signal:** $m_*(\beta)>0$ is a standard signature of a [[stat-mech-lattice/phase-transition-gibbs|phase transition]] and of [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]] in $\mathbb{Z}_2$-symmetric systems.
- **Relation to susceptibility:** Fluctuations of magnetization are measured by the [[stat-mech/susceptibility-stat-mech|susceptibility]], typically involving derivatives of $p(\beta,h)$ at $h=0$ and/or integrated two-point correlations.

## Physical interpretation
$m_*(\beta)$ quantifies *long-range alignment* persisting even when the field is removed. Operationally, the limit $h\downarrow 0$ encodes the idea that an infinitesimal bias selects one of multiple competing macrostates; if the selected state retains nonzero magnetization at $h=0$, the system exhibits stable macroscopic order.
