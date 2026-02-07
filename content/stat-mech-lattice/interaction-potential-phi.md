---
title: "Interaction potential (Φ)"
description: "A specification of local energy contributions indexed by finite subsets of the lattice, from which finite-volume Hamiltonians and Gibbs specifications are built."
---

An **interaction potential** (often denoted $\Phi$) for a lattice spin system with {{< knowl id="spin-space" text="spin space" >}} $S$ is a family of functions
$$
\Phi = \{\Phi_X\}_{X \subset\subset \mathbb{Z}^d},
$$

indexed by finite subsets $X$ of the lattice. Each term $\Phi_X$ is a real-valued function of the spin variables in $X$ only; equivalently, it is a function on $S^X$ (measurable with respect to the product sigma-algebra on $S^X$).

From $\Phi$ one constructs the finite-volume {{< knowl id="lattice-hamiltonian" text="lattice Hamiltonian" >}} by summing all interaction terms that intersect the volume, and from those Hamiltonians one builds the {{< knowl id="gibbs-specification" text="Gibbs specification" >}} and ultimately {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}} via the {{< knowl id="dlr-equation" text="DLR equation" >}}.

## Key properties
- **Support and range:**
  - $\Phi$ is **finite range** if $\Phi_X = 0$ whenever $\mathrm{diam}(X)$ exceeds some fixed range (see {{< knowl id="finite-range-interaction-lattice" text="finite-range interaction" >}}).
  - Nearest-neighbor models are special cases where only single-site and edge terms appear (see {{< knowl id="nearest-neighbor-zd" section="discrete-structures" text="nearest-neighbor structure" >}}).
- **Translation invariance:** $\Phi$ is translation invariant if translating $X$ and the spins on it does not change the functional form of $\Phi_X$ (see {{< knowl id="translation-invariant-interaction" text="translation-invariant interaction" >}}). This is the lattice analogue of homogeneity.
- **Summability/regularity (ensuring well-defined energies):** For infinite-volume considerations, one often requires a summability condition (e.g. absolute summability over sets containing the origin) so that energy differences and pressure are well-defined and the Gibbs formalism behaves well.
- **Multi-body interactions:** Terms with $|X|>2$ encode genuine many-body couplings. Pair interactions correspond to $|X|=2$ terms, plus possible on-site fields ($|X|=1$).
- **Symmetries and constraints:** Symmetries of $\Phi$ (spin-flip, rotations, permutations of Potts colors) control invariances of the model and are central to {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}}.
- **Model identification:** Standard models correspond to specific choices of $\Phi$, e.g. {{< knowl id="ising-model" text="Ising" >}}, {{< knowl id="potts-model" text="Potts" >}}, {{< knowl id="xy-model" text="XY" >}}, and {{< knowl id="heisenberg-model" text="Heisenberg" >}} interactions.

## Physical interpretation
The interaction potential specifies **how local patterns contribute to energy**:
- which alignments are favored (ferromagnetic vs antiferromagnetic tendencies; see {{< knowl id="ferromagnetic-ising" text="ferromagnetic Ising" >}} and {{< knowl id="antiferromagnetic-ising" text="antiferromagnetic Ising" >}}),
- how strongly and how far spins influence each other (range and decay),
- whether external fields bias single sites (see {{< knowl id="external-field-coupling" text="external field coupling" >}}),
- and whether the system has continuous or discrete symmetry.

In equilibrium, $\Phi$ determines the competition between energy minimization and entropic fluctuations, shaping typical configurations and the possible emergence of multiple Gibbs states (see {{< knowl id="extremal-gibbs-measure" text="extremal Gibbs measures" >}} and {{< knowl id="phase-transition-gibbs" text="phase transitions" >}}).
