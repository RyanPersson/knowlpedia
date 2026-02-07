---
title: "Susceptibility equals variance of magnetization"
description: "Finite-volume fluctuation–response identity: magnetic susceptibility is β times the magnetization variance (per volume)."
---

Let $\mu_{\Lambda,\beta,h}$ be a {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}} on a finite region $\Lambda$, with inverse temperature $\beta>0$ and external magnetic field $h$ coupled linearly to the total magnetization
$M_\Lambda(\sigma)=\sum_{x\in\Lambda}\sigma_x$ (e.g. for the {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}}).
Let
- $Z_\Lambda(\beta,h)$ be the {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="partition function" >}},
- $p_\Lambda(\beta,h)=\frac{1}{|\Lambda|}\log Z_\Lambda(\beta,h)$ be the (finite-volume) {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="pressure" >}},
- $m_\Lambda(\beta,h)=\frac{1}{|\Lambda|}\,\mathbb{E}_{\mu_{\Lambda,\beta,h}}[M_\Lambda]$ be the magnetization density,
- $\chi_\Lambda(\beta,h)=\partial_h m_\Lambda(\beta,h)$ be the (finite-volume) {{< knowl id="susceptibility-stat-mech" section="stat-mech" text="susceptibility" >}} per site.

## Statement
Assume the Hamiltonian depends on $h$ only through a term $-h\,M_\Lambda$ (linear field coupling). Then $\chi_\Lambda(\beta,h)$ exists and
$$
\chi_\Lambda(\beta,h)
= \frac{\beta}{|\Lambda|}\,\mathrm{Var}_{\mu_{\Lambda,\beta,h}}(M_\Lambda)
= \beta\,|\Lambda|\,\mathrm{Var}_{\mu_{\Lambda,\beta,h}}(m_\Lambda).
$$
Equivalently,
$$
\partial_h^2 p_\Lambda(\beta,h)
= \frac{\beta^2}{|\Lambda|}\,\mathrm{Var}_{\mu_{\Lambda,\beta,h}}(M_\Lambda)
\quad\text{and}\quad
\chi_\Lambda(\beta,h)=\frac{1}{\beta}\,\partial_h^2 p_\Lambda(\beta,h).
$$

## Key hypotheses
- Finite region $\Lambda$ and a well-defined {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}}.
- External field enters the energy as $H_{\Lambda,h}=H_{\Lambda,0}-h\,M_\Lambda$ (linear coupling).
- Expectations and {{< knowl id="variance-observable-ensemble" section="stat-mech" text="variances in the ensemble" >}} are finite (automatic for bounded spins).

## Conclusions
- $\chi_\Lambda(\beta,h)\ge 0$ since it is proportional to a variance.
- Susceptibility is a fluctuation: large magnetization fluctuations imply large response to $h$.
- This is a concrete instance of the {{< knowl id="prop-fluctuation-response-equivalence" text="fluctuation–response principle" >}}.

