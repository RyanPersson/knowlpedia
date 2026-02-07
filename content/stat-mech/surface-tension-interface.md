---
title: "Surface tension and interface free energy"
description: "Definition of surface tension as free-energy cost per area of an interface between coexisting phases; Ising/lattice-gas viewpoint."
---

## Extension: interface free energy and surface tension

In systems with phase coexistence, an **interface** separating two stable phases costs free energy proportional to its area. The proportionality constant (possibly direction-dependent) is the **surface tension**.

A canonical setting is the {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}} below its critical temperature, where distinct infinite-volume phases exist (see {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions" >}} and {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}).

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

- **Coexistence and order:** A positive $\tau(\mathbf{n})$ is tied to coexistence of distinct phases and nonzero {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}} (an {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}).
- **Geometry:** Directional dependence of $\tau(\mathbf{n})$ leads to equilibrium crystal shapes via Wulff-type constructions (a geometric “dual” of interface costs).
- **Large deviations of profiles:** Interface free energies govern probabilities of atypical magnetization profiles and droplet formation; this connects to {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviations" >}} and to the thermodynamic potential viewpoint via {{< knowl id="pressure-log-partition-density" text="pressure (log-partition density)" >}}.

### Prerequisites / cross-links

- {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonians" >}}, {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}}, {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equation" >}}
- {{< knowl id="ferromagnetic-ising" section="stat-mech-lattice" text="ferromagnetic Ising model" >}}
- {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}} (interface costs as excess free energies)
