+++
id = "stat-mech-lattice/pressure-lattice"
title = "Lattice pressure (finite volume)"
kind = "knowl"
summary = "Dimensionless free-energy density: the log partition function per lattice site in a finite region."
aliases = ["pressure-lattice", "Lattice pressure (finite volume)"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/pressure-lattice.md"
+++

Let $\Lambda$ be a finite region (see [[discrete-structures/boundary-finite-region|boundaries of finite regions]]) and let $Z_\Lambda(\beta,\tau)$ be the [[stat-mech-lattice/partition-function-lattice|finite-volume lattice partition function]] at inverse temperature $\beta$ with [[stat-mech-lattice/boundary-condition-lattice|boundary condition]] $\tau$.

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

so that $p_\Lambda(\beta,\tau) = -\beta\,\frac{F_\Lambda(\beta,\tau)}{|\Lambda|}$, matching the statistical-mechanics notion of [[stat-mech/free-energy-statistical|free energy]] and the thermodynamic [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] (up to conventions and units).

## Key properties

- **Intensive quantity.** $p_\Lambda$ is normalized per site and is therefore the natural quantity to send to the [[stat-mech-lattice/thermodynamic-limit-pressure-lattice|thermodynamic limit]].

- **Boundary effects are subextensive.** For many short-range models (e.g. [[stat-mech-lattice/finite-range-interaction-lattice|finite-range interactions]]), changing $\tau$ changes $\log Z_\Lambda$ by at most order $|\partial \Lambda|$, so $p_\Lambda(\beta,\tau)$ is often asymptotically independent of $\tau$ as $|\Lambda|\to\infty$.

- **Convexity in parameters.** Because it is a log-partition function density, $p_\Lambda$ is typically convex in couplings and fields appearing linearly in the [[stat-mech-lattice/lattice-hamiltonian|Hamiltonian]] (a finite-volume version of standard convexity for $\log Z$).

- **Derivatives give observables.** If the Hamiltonian includes an external field term (see [[stat-mech-lattice/external-field-coupling|external field coupling]]), then derivatives of $p_\Lambda$ with respect to that field give magnetization density and susceptibilities (see [[stat-mech/susceptibility-stat-mech|susceptibility]]).

## Physical interpretation

$p_\Lambda$ is the free-energy density in units of $k_B T$ (see [[thermodynamics/boltzmann-constant|Boltzmann constant]] and [[thermodynamics/temperature-thermo|temperature]]): it encodes the competition between energy minimization and entropy maximization in a finite region. Non-smooth behavior of its infinite-volume limit is a key diagnostic of [[stat-mech-lattice/phase-transition-gibbs|phase transitions]].
