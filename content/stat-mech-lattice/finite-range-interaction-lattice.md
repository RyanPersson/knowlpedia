---
title: "Finite-range interaction (lattice)"
description: "An interaction on a lattice spin system in which only finitely separated sets of sites can contribute nontrivially to the energy."
---

Let $\Lambda \subset \mathbb{Z}^d$ be a finite region and let the single-site spin space be $\mathcal S$ (see {{< knowl id="spin-space" text="spin space" >}}). A (finite-volume) interaction is a family
$$
\Phi=\{\Phi_A\}_{A \Subset \mathbb{Z}^d},
$$

indexed by finite subsets $A$ of $\mathbb{Z}^d$, where each $\Phi_A$ is a real-valued function of the spins in $A$, i.e. $\Phi_A : \mathcal S^A \to \mathbb{R}$ (see {{< knowl id="interaction-potential-phi" text="interaction potential $\Phi$" >}}).

The interaction $\Phi$ is **finite-range** if there exists $R<\infty$ such that
$$
\Phi_A \equiv 0 \quad \text{whenever } \operatorname{diam}(A) > R,
$$

where $\operatorname{diam}(A)=\max\{\|x-y\|:x,y\in A\}$ for a chosen lattice norm.

Equivalently: only subsets $A$ whose sites fit inside a ball of radius $R$ can contribute to the energy.

## Cross-links
- The resulting energy in a region is given by a {{< knowl id="lattice-hamiltonian" text="lattice Hamiltonian" >}} built from $\Phi$ and a {{< knowl id="boundary-condition-lattice" text="boundary condition" >}}.
- Finite-range interactions are a common sufficient hypothesis for constructing {{< knowl id="gibbs-specification" text="Gibbs specifications" >}} and {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}} via the {{< knowl id="dlr-equation" text="DLR equation" >}}.
- Typical examples include {{< knowl id="ising-model" text="the Ising model" >}} with {{< knowl id="nearest-neighbor-zd" section="discrete-structures" text="nearest-neighbor" >}} coupling.

## Key properties
1. **Locality of energy contributions.** The energy change from modifying spins in a small set depends only on spins within distance $R$ of that set.
2. **Well-defined finite-volume Gibbs measures.** For any finite $\Lambda$ and boundary condition $\eta$, the corresponding {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} has a Hamiltonian that depends on $\eta$ only near $\partial\Lambda$ (a boundary layer of thickness $R$).
3. **Quasilocal conditional probabilities.** Finite-range interactions yield conditional distributions where the spin at a site depends on the exterior configuration only through a finite neighborhood.
4. **Compatibility with thermodynamic limits.** Finite-range is a standard condition ensuring the existence of limits of pressures/free energies along increasing volumes (see {{< knowl id="thermodynamic-limit-pressure-lattice" text="thermodynamic limit of the pressure" >}}).

## Physical interpretation
A finite-range interaction models systems where forces are short-ranged: spins influence each other only up to a finite distance (e.g. exchange interactions in many magnetic materials). The parameter $R$ is a microscopic interaction range; macroscopic long-range correlations (large {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}) can still emerge near criticality even when the microscopic interaction range is finite.
