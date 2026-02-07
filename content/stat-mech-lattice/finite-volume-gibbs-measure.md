---
title: "Finite-volume Gibbs measure"
description: "The equilibrium probability distribution on spin configurations in a finite region, defined from the Hamiltonian and temperature with a chosen boundary condition."
---

Let $\Lambda \Subset \mathbb{Z}^d$ be finite, with spin space $\mathcal S$ ({{< knowl id="spin-space" text="spin space" >}}) and configuration space $\mathcal S^\Lambda$ ({{< knowl id="configuration-space-lattice" text="configuration space" >}}). Fix an inverse temperature $\beta$ (see {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature $\beta$" >}}) and a boundary condition $\eta$ ({{< knowl id="boundary-condition-lattice" text="boundary condition" >}}).

Given a finite-volume Hamiltonian $H_\Lambda(\sigma_\Lambda\mid \eta)$ ({{< knowl id="lattice-hamiltonian" text="lattice Hamiltonian" >}}), the **finite-volume Gibbs measure** on $\mathcal S^\Lambda$ is
$$
\mu_{\Lambda,\beta}^{\eta}(\sigma_\Lambda)
= \frac{1}{Z_{\Lambda,\beta}^{\eta}}
\exp\!\bigl(-\beta\, H_\Lambda(\sigma_\Lambda\mid \eta)\bigr),
$$
where the normalizing constant
$$
Z_{\Lambda,\beta}^{\eta}
=\sum_{\sigma_\Lambda\in \mathcal S^\Lambda}
\exp\!\bigl(-\beta\, H_\Lambda(\sigma_\Lambda\mid \eta)\bigr)
$$
is the {{< knowl id="partition-function-lattice" text="lattice partition function" >}} (for discrete spins; replace the sum by an integral for continuous spins).

## Cross-links
- Built from an {{< knowl id="interaction-potential-phi" text="interaction potential $\Phi$" >}} and a {{< knowl id="boundary-condition-lattice" text="boundary condition" >}} via the {{< knowl id="lattice-hamiltonian" text="Hamiltonian" >}}.
- The collection $\{\mu_{\Lambda,\beta}^{\eta}\}$ (varying $\Lambda$) forms a {{< knowl id="gibbs-specification" text="Gibbs specification" >}}; its infinite-volume consistency is expressed by the {{< knowl id="dlr-equation" text="DLR equation" >}}.
- Thermodynamic quantities are derived from $Z_{\Lambda,\beta}^{\eta}$, including the {{< knowl id="pressure-lattice" text="pressure" >}} and its {{< knowl id="thermodynamic-limit-pressure-lattice" text="thermodynamic limit" >}}.
- Model examples: {{< knowl id="ising-model" text="Ising model" >}}, {{< knowl id="potts-model" text="Potts model" >}}, {{< knowl id="xy-model" text="XY model" >}}.

## Key properties
1. **Boltzmann form and normalization.** $\mu_{\Lambda,\beta}^{\eta}$ is a probability measure: $\sum_{\sigma_\Lambda}\mu_{\Lambda,\beta}^{\eta}(\sigma_\Lambda)=1$ by definition of $Z_{\Lambda,\beta}^{\eta}$.
2. **Dependence on boundary conditions.** For finite $\Lambda$, changing $\eta$ changes $\mu_{\Lambda,\beta}^{\eta}$ through boundary interaction terms; this dependence typically decays into the bulk away from $\partial\Lambda$ when correlations are short-ranged.
3. **Domain Markov / consistency property.** If $\Delta \subset \Lambda$, then conditioning $\mu_{\Lambda,\beta}^{\eta}$ on the spins in $\Lambda\setminus\Delta$ yields a Gibbs measure in $\Delta$ with boundary condition given by the conditioned exterior configuration. This is the finite-volume precursor of the {{< knowl id="dlr-equation" text="DLR" >}} consistency.
4. **Thermodynamic limit and phases.** Along an increasing sequence of volumes $\Lambda_n \uparrow \mathbb{Z}^d$, subsequential weak limits of $\mu_{\Lambda_n,\beta}^{\eta}$ (if they exist) are candidates for {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}}. Different $\eta$ can lead to different limits in the presence of a {{< knowl id="phase-transition-gibbs" text="phase transition" >}}.

## Physical interpretation
$\mu_{\Lambda,\beta}^{\eta}$ is the equilibrium distribution of a finite sample in contact with a heat bath at temperature $T=1/\beta$ (up to constants), with the outside world modeled by the boundary condition $\eta$. Observables are computed as ensemble averages under this measure (compare {{< knowl id="ensemble-average" section="stat-mech" text="ensemble average" >}}), and the sensitivity of bulk behavior to $\eta$ distinguishes single-phase regimes from coexistence of multiple phases.
