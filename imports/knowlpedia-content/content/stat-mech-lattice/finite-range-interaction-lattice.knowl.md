+++
id = "stat-mech-lattice/finite-range-interaction-lattice"
title = "Finite-range interaction (lattice)"
kind = "knowl"
summary = "An interaction on a lattice spin system in which only finitely separated sets of sites can contribute nontrivially to the energy."
aliases = ["finite-range-interaction-lattice", "Finite-range interaction (lattice)"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/finite-range-interaction-lattice.md"
+++

Let $\Lambda \subset \mathbb{Z}^d$ be a finite region and let the single-site spin space be $\mathcal S$ (see [[stat-mech-lattice/spin-space|spin space]]). A (finite-volume) interaction is a family
$$
\Phi=\{\Phi_A\}_{A \Subset \mathbb{Z}^d},
$$

indexed by finite subsets $A$ of $\mathbb{Z}^d$, where each $\Phi_A$ is a real-valued function of the spins in $A$, i.e. $\Phi_A : \mathcal S^A \to \mathbb{R}$ (see [[stat-mech-lattice/interaction-potential-phi|interaction potential $\Phi$]]).

The interaction $\Phi$ is **finite-range** if there exists $R<\infty$ such that
$$
\Phi_A \equiv 0 \quad \text{whenever } \operatorname{diam}(A) > R,
$$

where $\operatorname{diam}(A)=\max\{\|x-y\|:x,y\in A\}$ for a chosen lattice norm.

Equivalently: only subsets $A$ whose sites fit inside a ball of radius $R$ can contribute to the energy.

## Cross-links
- The resulting energy in a region is given by a [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]] built from $\Phi$ and a [[stat-mech-lattice/boundary-condition-lattice|boundary condition]].
- Finite-range interactions are a common sufficient hypothesis for constructing [[stat-mech-lattice/gibbs-specification|Gibbs specifications]] and [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] via the [[stat-mech-lattice/dlr-equation|DLR equation]].
- Typical examples include [[stat-mech-lattice/ising-model|the Ising model]] with [[discrete-structures/nearest-neighbor-zd|nearest-neighbor]] coupling.

## Key properties
1. **Locality of energy contributions.** The energy change from modifying spins in a small set depends only on spins within distance $R$ of that set.
2. **Well-defined finite-volume Gibbs measures.** For any finite $\Lambda$ and boundary condition $\eta$, the corresponding [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] has a Hamiltonian that depends on $\eta$ only near $\partial\Lambda$ (a boundary layer of thickness $R$).
3. **Quasilocal conditional probabilities.** Finite-range interactions yield conditional distributions where the spin at a site depends on the exterior configuration only through a finite neighborhood.
4. **Compatibility with thermodynamic limits.** Finite-range is a standard condition ensuring the existence of limits of pressures/free energies along increasing volumes (see [[stat-mech-lattice/thermodynamic-limit-pressure-lattice|thermodynamic limit of the pressure]]).

## Physical interpretation
A finite-range interaction models systems where forces are short-ranged: spins influence each other only up to a finite distance (e.g. exchange interactions in many magnetic materials). The parameter $R$ is a microscopic interaction range; macroscopic long-range correlations (large [[stat-mech/correlation-length|correlation length]]) can still emerge near criticality even when the microscopic interaction range is finite.
