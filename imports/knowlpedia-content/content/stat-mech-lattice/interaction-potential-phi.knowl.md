+++
id = "stat-mech-lattice/interaction-potential-phi"
title = "Interaction potential (Φ)"
kind = "knowl"
summary = "A specification of local energy contributions indexed by finite subsets of the lattice, from which finite-volume Hamiltonians and Gibbs specifications are built."
aliases = ["interaction-potential-phi", "Interaction potential (Φ)"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/interaction-potential-phi.md"
+++

An **interaction potential** (often denoted $\Phi$) for a lattice spin system with [[stat-mech-lattice/spin-space|spin space]] $S$ is a family of functions
$$
\Phi = \{\Phi_X\}_{X \subset\subset \mathbb{Z}^d},
$$

indexed by finite subsets $X$ of the lattice. Each term $\Phi_X$ is a real-valued function of the spin variables in $X$ only; equivalently, it is a function on $S^X$ (measurable with respect to the product sigma-algebra on $S^X$).

From $\Phi$ one constructs the finite-volume [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]] by summing all interaction terms that intersect the volume, and from those Hamiltonians one builds the [[stat-mech-lattice/gibbs-specification|Gibbs specification]] and ultimately [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] via the [[stat-mech-lattice/dlr-equation|DLR equation]].

## Key properties
- **Support and range:**
  - $\Phi$ is **finite range** if $\Phi_X = 0$ whenever $\mathrm{diam}(X)$ exceeds some fixed range (see [[stat-mech-lattice/finite-range-interaction-lattice|finite-range interaction]]).
  - Nearest-neighbor models are special cases where only single-site and edge terms appear (see [[discrete-structures/nearest-neighbor-zd|nearest-neighbor structure]]).
- **Translation invariance:** $\Phi$ is translation invariant if translating $X$ and the spins on it does not change the functional form of $\Phi_X$ (see [[stat-mech-lattice/translation-invariant-interaction|translation-invariant interaction]]). This is the lattice analogue of homogeneity.
- **Summability/regularity (ensuring well-defined energies):** For infinite-volume considerations, one often requires a summability condition (e.g. absolute summability over sets containing the origin) so that energy differences and pressure are well-defined and the Gibbs formalism behaves well.
- **Multi-body interactions:** Terms with $|X|>2$ encode genuine many-body couplings. Pair interactions correspond to $|X|=2$ terms, plus possible on-site fields ($|X|=1$).
- **Symmetries and constraints:** Symmetries of $\Phi$ (spin-flip, rotations, permutations of Potts colors) control invariances of the model and are central to [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]].
- **Model identification:** Standard models correspond to specific choices of $\Phi$, e.g. [[stat-mech-lattice/ising-model|Ising]], [[stat-mech-lattice/potts-model|Potts]], [[stat-mech-lattice/xy-model|XY]], and [[stat-mech-lattice/heisenberg-model|Heisenberg]] interactions.

## Physical interpretation
The interaction potential specifies **how local patterns contribute to energy**:
- which alignments are favored (ferromagnetic vs antiferromagnetic tendencies; see [[stat-mech-lattice/ferromagnetic-ising|ferromagnetic Ising]] and [[stat-mech-lattice/antiferromagnetic-ising|antiferromagnetic Ising]]),
- how strongly and how far spins influence each other (range and decay),
- whether external fields bias single sites (see [[stat-mech-lattice/external-field-coupling|external field coupling]]),
- and whether the system has continuous or discrete symmetry.

In equilibrium, $\Phi$ determines the competition between energy minimization and entropic fluctuations, shaping typical configurations and the possible emergence of multiple Gibbs states (see [[stat-mech-lattice/extremal-gibbs-measure|extremal Gibbs measures]] and [[stat-mech-lattice/phase-transition-gibbs|phase transitions]]).
