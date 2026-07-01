+++
id = "stat-mech-lattice/partition-function-lattice"
title = "Lattice partition function"
kind = "knowl"
summary = "Finite-volume normalization constant defining the Gibbs distribution of a lattice spin system in a region with a chosen boundary condition."
aliases = ["partition-function-lattice", "Lattice partition function"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/partition-function-lattice.md"
+++

Fix a finite region $\Lambda$ of the lattice (see [[discrete-structures/finite-box-lattice|finite boxes in a lattice]]) and a [[stat-mech-lattice/spin-space|single-site spin space]] $S$ with a reference (a priori) measure $\lambda$ on $S$. A [[stat-mech-lattice/spin-configuration|spin configuration]] on $\Lambda$ is an element $\sigma_\Lambda \in S^\Lambda$, and a [[stat-mech-lattice/boundary-condition-lattice|boundary condition]] is a configuration $\tau$ on the complement $\Lambda^c$.

Given an inverse temperature $\beta$ (see [[thermodynamics/inverse-temperature-beta|inverse temperature]]) and a [[stat-mech-lattice/lattice-hamiltonian|finite-volume lattice Hamiltonian]] $H_\Lambda(\sigma_\Lambda \mid \tau)$, the **finite-volume lattice partition function** is
$$
Z_\Lambda(\beta,\tau)
={}
\int_{S^\Lambda}
\exp\!\bigl(-\beta\, H_\Lambda(\sigma_\Lambda \mid \tau)\bigr)\,
\lambda_\Lambda(d\sigma_\Lambda),
$$

where $\lambda_\Lambda$ is the product measure on $S^\Lambda$ induced by $\lambda$ (see [[measure-theory/product-measure|product measure]]).

If $S$ is finite (e.g. the Ising single-spin set $\{\pm 1\}$), the integral reduces to a finite sum over $\sigma_\Lambda \in S^\Lambda$.

This object is the lattice analogue of the [[stat-mech/partition-function-canonical|canonical partition function]].

## Key properties

- **Normalization for Gibbs weights.** The partition function is the normalizing constant for the [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]]:
  $$
  \mu_\Lambda^{\beta,\tau}(d\sigma_\Lambda)
  ={}
  \frac{1}{Z_\Lambda(\beta,\tau)}
  \exp\!\bigl(-\beta\,H_\Lambda(\sigma_\Lambda\mid\tau)\bigr)\,
  \lambda_\Lambda(d\sigma_\Lambda).
  $$

- **Boundary dependence.** In general $Z_\Lambda(\beta,\tau)$ depends on the boundary condition $\tau$; for [[stat-mech-lattice/finite-range-interaction-lattice|finite-range interactions]] the dependence is through spins near the boundary of $\Lambda$.

- **Generates thermodynamics.** Derivatives of $\log Z_\Lambda$ with respect to parameters in $H_\Lambda$ (e.g. a [[stat-mech-lattice/external-field-coupling|magnetic field coupling]]) produce finite-volume expectations and fluctuations (see [[stat-mech/ensemble-average|ensemble averages]]).

## Physical interpretation

$Z_\Lambda(\beta,\tau)$ is the weighted “count” of microstates in $\Lambda$ compatible with an environment $\tau$, with each configuration weighted by the Boltzmann factor $\exp(-\beta H_\Lambda)$. Its logarithm controls the finite-volume free energy and leads directly to the [[stat-mech-lattice/pressure-lattice|lattice pressure]] and its thermodynamic limit.
