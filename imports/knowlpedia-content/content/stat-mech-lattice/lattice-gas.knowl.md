+++
id = "stat-mech-lattice/lattice-gas"
title = "Lattice gas"
kind = "knowl"
summary = "Particle (occupation) model on a lattice with 0–1 variables, equivalent to the Ising model in a field and used to model gas–liquid coexistence and adsorption."
aliases = ["lattice-gas", "Lattice gas"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/lattice-gas.md"
+++

A **lattice gas** is a statistical-mechanical model of particles on a lattice, where each site is either empty or occupied. It can be formulated as a lattice spin system with spin space $\{0,1\}$ and is closely related to the [[stat-mech-lattice/ising-model|Ising model]].

Let $\Lambda\subset\mathbb{Z}^d$ be finite. A configuration is $n=(n_x)_{x\in\Lambda}$ with $n_x\in\{0,1\}$, where $n_x=1$ means “occupied.” A common nearest-neighbor attractive lattice gas [[stat-mech-lattice/lattice-hamiltonian|Hamiltonian]] is
$$
H_\Lambda(n)
={}
-J\sum_{\langle x,y\rangle:\, x,y\in\Lambda} n_x n_y
-\mu\sum_{x\in\Lambda} n_x,
\qquad J\ge 0,
$$

where $\mu$ is the chemical potential (an analogue of an [[stat-mech-lattice/external-field-coupling|external field]]) and $J\ge 0$ makes occupied neighbors energetically favorable. More general lattice gases can be defined using an [[stat-mech-lattice/interaction-potential-phi|interaction potential]] beyond nearest neighbors.

At inverse temperature $\beta$, the finite-volume Gibbs distribution is the [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]]
$$
\mu_{\Lambda,\beta}(n)\propto \exp\!\big(-\beta H_\Lambda(n)\big),
$$

normalized by the [[stat-mech-lattice/partition-function-lattice|partition function]]. The associated [[stat-mech-lattice/pressure-lattice|pressure]] is typically defined from $\frac{1}{|\Lambda|}\log Z_\Lambda$ (and its infinite-volume limit by [[stat-mech-lattice/thermodynamic-limit-pressure-lattice|thermodynamic limit of the pressure]]).

## Key properties

- **Density as the main observable.** The natural order parameter is the particle density
  $$
  \rho_\Lambda=\frac{1}{|\Lambda|}\sum_{x\in\Lambda} n_x,
  $$

  or its infinite-volume expectation. Phase coexistence appears as multiple possible limiting densities at the same $(\beta,\mu)$.

- **Equivalence to Ising in a field.** Define Ising spins $\sigma_x\in\{-1,+1\}$ by $\sigma_x=2n_x-1$. For nearest-neighbor interactions on $\mathbb{Z}^d$ (degree $2d$), one obtains (up to an additive constant)
  $$
  H_\Lambda(n)
  ={}
  -\frac{J}{4}\sum_{\langle x,y\rangle}\sigma_x\sigma_y
  -\left(\frac{\mu}{2}+\frac{Jd}{2}\right)\sum_{x\in\Lambda}\sigma_x
  +\text{const}.
  $$
  Thus an attractive lattice gas is equivalent to a ferromagnetic Ising model with an effective field, making lattice gases a convenient physical reinterpretation of Ising [[stat-mech-lattice/phase-transition-gibbs|phase transitions]].

- **Gas–liquid transition and coexistence line.** In the Ising correspondence, the “coexistence” regime (two densities) corresponds to the regime with multiple infinite-volume Gibbs states. The symmetry point (Ising zero field) corresponds to a particular chemical potential.

- **Boundary conditions and phase separation.** Different [[stat-mech-lattice/boundary-condition-lattice|boundary conditions]] can select low-density (“gas”) or high-density (“liquid”) phases in finite volume, and interfaces/domain walls appear in mixed boundary conditions.

## Physical interpretation

The lattice gas is a coarse-grained model of a **fluid on discrete sites**, useful for:
- gas–liquid coexistence and criticality,
- adsorption in porous materials (occupied vs empty sites),
- phase separation and interfaces.

Because of its exact mapping to the Ising model, it provides a direct bridge between **magnetic language** (spins, fields, magnetization) and **fluid language** (occupations, chemical potential, density).
