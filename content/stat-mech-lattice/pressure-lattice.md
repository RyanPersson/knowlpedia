---
title: "Lattice pressure (finite volume)"
description: "Dimensionless free-energy density: the log partition function per lattice site in a finite region."
---


Let $\Lambda$ be a finite region (see {{< knowl id="boundary-finite-region" section="discrete-structures" text="boundaries of finite regions" >}}) and let $Z_\Lambda(\beta,\tau)$ be the {{< knowl id="partition-function-lattice" text="finite-volume lattice partition function" >}} at inverse temperature $\beta$ with {{< knowl id="boundary-condition-lattice" text="boundary condition" >}} $\tau$.

The **finite-volume (dimensionless) pressure** is
$$
p_\Lambda(\beta,\tau)
={}
\frac{1}{|\Lambda|}\,\log Z_\Lambda(\beta,\tau),
$$

where $|\Lambda|$ is the number of lattice sites in $\Lambda$.

Equivalently, the finite-volume Helmholtz free energy is
$$
F_\Lambda(\beta,\tau) = -\frac{1}{\beta}\log Z_\Lambda(\beta,\tau),
$$

so that $p_\Lambda(\beta,\tau) = -\beta\,\frac{F_\Lambda(\beta,\tau)}{|\Lambda|}$, matching the statistical-mechanics notion of {{< knowl id="free-energy-statistical" section="stat-mech" text="free energy" >}} and the thermodynamic {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} (up to conventions and units).

## Key properties

- **Intensive quantity.** $p_\Lambda$ is normalized per site and is therefore the natural quantity to send to the {{< knowl id="thermodynamic-limit-pressure-lattice" text="thermodynamic limit" >}}.

- **Boundary effects are subextensive.** For many short-range models (e.g. {{< knowl id="finite-range-interaction-lattice" text="finite-range interactions" >}}), changing $\tau$ changes $\log Z_\Lambda$ by at most order $|\partial \Lambda|$, so $p_\Lambda(\beta,\tau)$ is often asymptotically independent of $\tau$ as $|\Lambda|\to\infty$.

- **Convexity in parameters.** Because it is a log-partition function density, $p_\Lambda$ is typically convex in couplings and fields appearing linearly in the {{< knowl id="lattice-hamiltonian" text="Hamiltonian" >}} (a finite-volume version of standard convexity for $\log Z$).

- **Derivatives give observables.** If the Hamiltonian includes an external field term (see {{< knowl id="external-field-coupling" text="external field coupling" >}}), then derivatives of $p_\Lambda$ with respect to that field give magnetization density and susceptibilities (see {{< knowl id="susceptibility-stat-mech" section="stat-mech" text="susceptibility" >}}).

## Physical interpretation

$p_\Lambda$ is the free-energy density in units of $k_B T$ (see {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}} and {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}): it encodes the competition between energy minimization and entropy maximization in a finite region. Non-smooth behavior of its infinite-volume limit is a key diagnostic of {{< knowl id="phase-transition-gibbs" text="phase transitions" >}}.
