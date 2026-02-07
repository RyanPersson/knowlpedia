---
title: "Lattice partition function"
description: "Finite-volume normalization constant defining the Gibbs distribution of a lattice spin system in a region with a chosen boundary condition."
---


Fix a finite region $\Lambda$ of the lattice (see {{< knowl id="finite-box-lattice" section="discrete-structures" text="finite boxes in a lattice" >}}) and a {{< knowl id="spin-space" text="single-site spin space" >}} $S$ with a reference (a priori) measure $\lambda$ on $S$. A {{< knowl id="spin-configuration" text="spin configuration" >}} on $\Lambda$ is an element $\sigma_\Lambda \in S^\Lambda$, and a {{< knowl id="boundary-condition-lattice" text="boundary condition" >}} is a configuration $\tau$ on the complement $\Lambda^c$.

Given an inverse temperature $\beta$ (see {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}}) and a {{< knowl id="lattice-hamiltonian" text="finite-volume lattice Hamiltonian" >}} $H_\Lambda(\sigma_\Lambda \mid \tau)$, the **finite-volume lattice partition function** is
$$
Z_\Lambda(\beta,\tau)
={}
\int_{S^\Lambda}
\exp\!\bigl(-\beta\, H_\Lambda(\sigma_\Lambda \mid \tau)\bigr)\,
\lambda_\Lambda(d\sigma_\Lambda),
$$

where $\lambda_\Lambda$ is the product measure on $S^\Lambda$ induced by $\lambda$ (see {{< knowl id="product-measure" section="measure-theory" text="product measure" >}}).

If $S$ is finite (e.g. the Ising single-spin set $\{\pm 1\}$), the integral reduces to a finite sum over $\sigma_\Lambda \in S^\Lambda$.

This object is the lattice analogue of the {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}.

## Key properties

- **Normalization for Gibbs weights.** The partition function is the normalizing constant for the {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}}:
  $$
  \mu_\Lambda^{\beta,\tau}(d\sigma_\Lambda)
  ={}
  \frac{1}{Z_\Lambda(\beta,\tau)}
  \exp\!\bigl(-\beta\,H_\Lambda(\sigma_\Lambda\mid\tau)\bigr)\,
  \lambda_\Lambda(d\sigma_\Lambda).
  $$

- **Boundary dependence.** In general $Z_\Lambda(\beta,\tau)$ depends on the boundary condition $\tau$; for {{< knowl id="finite-range-interaction-lattice" text="finite-range interactions" >}} the dependence is through spins near the boundary of $\Lambda$.

- **Generates thermodynamics.** Derivatives of $\log Z_\Lambda$ with respect to parameters in $H_\Lambda$ (e.g. a {{< knowl id="external-field-coupling" text="magnetic field coupling" >}}) produce finite-volume expectations and fluctuations (see {{< knowl id="ensemble-average" section="stat-mech" text="ensemble averages" >}}).

## Physical interpretation

$Z_\Lambda(\beta,\tau)$ is the weighted “count” of microstates in $\Lambda$ compatible with an environment $\tau$, with each configuration weighted by the Boltzmann factor $\exp(-\beta H_\Lambda)$. Its logarithm controls the finite-volume free energy and leads directly to the {{< knowl id="pressure-lattice" text="lattice pressure" >}} and its thermodynamic limit.
