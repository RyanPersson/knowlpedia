+++
id = "stat-mech-lattice/spin-configuration"
title = "Spin configuration"
kind = "knowl"
summary = "A specification of spin values at each site of a lattice region (finite or infinite)."
aliases = ["spin-configuration", "Spin configuration"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/spin-configuration.md"
+++

Let $S$ be the [[stat-mech-lattice/spin-space|spin space]] and let $\Lambda$ be a set of lattice sites (often a finite box; see [[discrete-structures/finite-box-lattice|finite box]] in the [[discrete-structures/lattice-zd|integer lattice]]).

A **spin configuration on** $\Lambda$ is a function
$$
\sigma_\Lambda : \Lambda \to S,
$$

assigning a spin value $\sigma_i \in S$ to each site $i\in\Lambda$. The set of all such configurations is $S^\Lambda$ (see [[stat-mech-lattice/configuration-space-lattice|configuration space]] for the infinite-volume analogue).

If $\Omega = S^{\mathbb{Z}^d}$ denotes the full configuration space, then:
- the **restriction** of a full configuration $\sigma\in\Omega$ to $\Lambda$ is denoted $\sigma_\Lambda$;
- given a boundary condition $\eta$ outside $\Lambda$ (see [[stat-mech-lattice/boundary-condition-lattice|boundary condition]]), one forms a combined configuration $\sigma_\Lambda \eta_{\Lambda^c}$ on the whole lattice by using $\sigma_\Lambda$ inside and $\eta$ outside.

## Key properties
- **Locality:** Many observables and energies depend only on finitely many coordinates of $\sigma$ (e.g. nearest-neighbor models; see [[discrete-structures/nearest-neighbor-zd|nearest-neighbor structure]]).
- **Gluing with boundary conditions:** Finite-volume energies and probabilities are naturally defined for $\sigma_\Lambda$ together with an exterior configuration $\eta_{\Lambda^c}$. This is central in the definition of the [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] and in the [[stat-mech-lattice/dlr-equation|DLR equation]].
- **Coordinate maps:** For each site $i$, the map $\sigma \mapsto \sigma_i$ is a basic random variable when $\sigma$ is distributed according to a Gibbs measure (see [[probability/random-variable|random variable]]).

## Physical interpretation
A spin configuration is the **microscopic state** of the lattice degrees of freedom at a fixed time (or in equilibrium sampling). In equilibrium statistical mechanics, configurations are weighted by Boltzmann factors built from the [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]], producing a probability distribution (a Gibbs measure) over configurations (see [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]]).
