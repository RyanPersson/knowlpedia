---
title: "Spontaneous magnetization"
description: "Nonzero magnetization in zero external field, defined via symmetry-breaking limits of Gibbs states in the thermodynamic limit."
---

Consider a lattice spin system with an {{< knowl id="external-field-coupling" text="external field coupling" >}} parameter $h\in\mathbb{R}$ (e.g. coupling to $\sum_x \sigma_x$). Let $\mu_{\beta,h}^{+}$ denote a translation-invariant {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measure" >}} selected by a *positive* field (or, equivalently in ferromagnets, by $+$ {{< knowl id="boundary-condition-lattice" text="boundary conditions" >}} and then taking volume $\to\infty$).

The **spontaneous magnetization** at inverse temperature $\beta$ is
$$
m_*(\beta)\;:=\;\lim_{h\downarrow 0}\,\mu_{\beta,h}^{+}(\sigma_0),
$$

provided the limit exists. For translation-invariant states, $\mu_{\beta,h}^{+}(\sigma_0)=\mu_{\beta,h}^{+}(\sigma_x)$ for all $x$.

Equivalently (when differentiability from the right holds), it is the right derivative at $h=0$ of the thermodynamic pressure:
$$
m_*(\beta)\;=\;\left.\frac{\partial}{\partial h}\,p(\beta,h)\right|_{h=0^+},
$$

where $p(\beta,h)$ is the {{< knowl id="pressure-lattice" text="pressure" >}} obtained as a {{< knowl id="thermodynamic-limit-pressure-lattice" text="thermodynamic limit" >}} of finite-volume pressures.

## Key properties
- **Order parameter:** $m_*(\beta)$ is a canonical {{< knowl id="order-parameter" text="order parameter" >}} for $\mathbb{Z}_2$-symmetric models such as the {{< knowl id="ising-model" text="Ising model" >}}.
- **Symmetry selection:** In systems with spin-flip symmetry at $h=0$, one typically has
  $$
  \mu_{\beta,0}^{+}(\sigma_0)=+m_*(\beta),\qquad \mu_{\beta,0}^{-}(\sigma_0)=-m_*(\beta),
  $$

  for the $+$ and $-$ extremal states, when they exist (see {{< knowl id="extremal-gibbs-measure" text="extremal Gibbs measures" >}} and {{< knowl id="pure-phase" text="pure phases" >}}).
- **Phase transition signal:** $m_*(\beta)>0$ is a standard signature of a {{< knowl id="phase-transition-gibbs" text="phase transition" >}} and of {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}} in $\mathbb{Z}_2$-symmetric systems.
- **Relation to susceptibility:** Fluctuations of magnetization are measured by the {{< knowl id="susceptibility-stat-mech" section="stat-mech" text="susceptibility" >}}, typically involving derivatives of $p(\beta,h)$ at $h=0$ and/or integrated two-point correlations.

## Physical interpretation
$m_*(\beta)$ quantifies *long-range alignment* persisting even when the field is removed. Operationally, the limit $h\downarrow 0$ encodes the idea that an infinitesimal bias selects one of multiple competing macrostates; if the selected state retains nonzero magnetization at $h=0$, the system exhibits stable macroscopic order.
