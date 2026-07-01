+++
id = "stat-mech/surface-tension-interface"
title = "Surface tension and interface free energy"
kind = "knowl"
summary = "Definition of surface tension as free-energy cost per area of an interface between coexisting phases; Ising/lattice-gas viewpoint."
aliases = ["surface-tension-interface", "Surface tension and interface free energy"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/surface-tension-interface.md"
+++

## Extension: interface free energy and surface tension

In systems with phase coexistence, an **interface** separating two stable phases costs free energy proportional to its area. The proportionality constant (possibly direction-dependent) is the **surface tension**.

A canonical setting is the [[stat-mech-lattice/ising-model|Ising model]] below its critical temperature, where distinct infinite-volume phases exist (see [[stat-mech-lattice/phase-transition-gibbs|phase transitions]] and [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]]).

### Definition via boundary conditions (Ising example)

Let $\Lambda_L$ be a large box with linear size $L$, and impose boundary conditions that force an interface with normal direction $\mathbf{n}$ (for example, “$+$” on one side of a plane and “$-$” on the other). Let $Z_L^{+-}(\mathbf{n})$ be the finite-volume partition function with such mixed boundary conditions, and let $Z_L^{++}$ be the partition function with uniform “$+$” boundary conditions.

If $A_L(\mathbf{n})$ is the cross-sectional area of the imposed interface, the **surface tension in direction $\mathbf{n}$** is defined (when the limit exists) by
$$
\tau(\mathbf{n})
=\lim_{L\to\infty}-\frac{1}{\beta\,A_L(\mathbf{n})}\,
\log\left(\frac{Z_L^{+-}(\mathbf{n})}{Z_L^{++}}\right).
$$

Interpretation: the ratio of partition functions isolates the excess free energy due to creating the interface, normalized by area.

### Key consequences and context

- **Coexistence and order:** A positive $\tau(\mathbf{n})$ is tied to coexistence of distinct phases and nonzero [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] (an [[stat-mech-lattice/order-parameter|order parameter]]).
- **Geometry:** Directional dependence of $\tau(\mathbf{n})$ leads to equilibrium crystal shapes via Wulff-type constructions (a geometric “dual” of interface costs).
- **Large deviations of profiles:** Interface free energies govern probabilities of atypical magnetization profiles and droplet formation; this connects to [[large-deviations/large-deviation-principle|large deviations]] and to the thermodynamic potential viewpoint via [[stat-mech/pressure-log-partition-density|pressure (log-partition density)]].

### Prerequisites / cross-links

- [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonians]], [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measures]], [[stat-mech-lattice/dlr-equation|DLR equation]]
- [[stat-mech-lattice/ferromagnetic-ising|ferromagnetic Ising model]]
- [[thermodynamics/thermodynamic-stability|thermodynamic stability]] (interface costs as excess free energies)
