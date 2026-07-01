+++
id = "stat-mech-lattice/lattice-hamiltonian"
title = "Lattice Hamiltonian"
kind = "knowl"
summary = "The finite-volume energy function on lattice spin configurations induced by an interaction potential (and possibly an external field and boundary condition)."
aliases = ["lattice-hamiltonian", "Lattice Hamiltonian"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/lattice-hamiltonian.md"
+++

Fix a [[stat-mech-lattice/spin-space|spin space]] $S$ and a finite region $\Lambda$ of the lattice (see [[discrete-structures/finite-box-lattice|finite box]] in [[discrete-structures/lattice-zd|the integer lattice]]). A **lattice Hamiltonian in volume** $\Lambda$ is an energy function that assigns a real number (or $+\infty$ in hard-constraint models) to each [[stat-mech-lattice/spin-configuration|spin configuration]] $\sigma_\Lambda \in S^\Lambda$, typically depending also on an exterior configuration (a [[stat-mech-lattice/boundary-condition-lattice|boundary condition]]) $\eta_{\Lambda^c}$.

Given an [[stat-mech-lattice/interaction-potential-phi|interaction potential]] $\Phi = (\Phi_X)$, the standard finite-volume Hamiltonian with boundary condition $\eta$ is
$$
H_\Lambda^\Phi(\sigma_\Lambda \mid \eta)
:= \sum_{\substack{X \subset \mathbb{Z}^d \\ X \cap \Lambda \neq \emptyset}} \Phi_X(\sigma_\Lambda \eta_{\Lambda^c}),
$$

where each $\Phi_X$ depends only on the spins in $X$.

An **external field** is usually incorporated via single-site terms (see [[stat-mech-lattice/external-field-coupling|external field coupling]]), e.g. by including appropriate $\Phi_{\{i\}}$.

## Key properties
- **Locality:** If $\Phi$ has finite range (see [[stat-mech-lattice/finite-range-interaction-lattice|finite-range interaction]]), then changing $\sigma$ far from $\Lambda$ (in the boundary condition) does not affect $H_\Lambda^\Phi$ except near the boundary.
- **Additivity over interaction sets:** The Hamiltonian is a sum of local contributions. For nearest-neighbor models (see [[discrete-structures/nearest-neighbor-zd|nearest-neighbor structure]]), the sum reduces to edges and sites.
- **Translation invariance:** If $\Phi$ is translation invariant (see [[stat-mech-lattice/translation-invariant-interaction|translation-invariant interaction]]), then $H_\Lambda^\Phi$ is covariant under lattice shifts (up to boundary effects).
- **Boundary dependence:** Different boundary conditions $\eta$ encode different ways the exterior influences $\Lambda$. This dependence is essential in the study of [[stat-mech-lattice/phase-transition-gibbs|phase transitions]] and in defining [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] via the [[stat-mech-lattice/dlr-equation|DLR equation]].
- **Connection to Gibbs weights:** The Hamiltonian generates Boltzmann weights $\exp(-\beta H_\Lambda^\Phi)$, where $\beta$ is the [[thermodynamics/inverse-temperature-beta|inverse temperature]]. These weights define the [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] and the [[stat-mech-lattice/partition-function-lattice|lattice partition function]].

## Physical interpretation
The lattice Hamiltonian encodes the **microscopic energetics**: which local patterns are energetically favored (low energy) or suppressed (high energy). Competing terms in $H_\Lambda$ (e.g. interaction vs field, ferro- vs antiferromagnetic couplings) determine typical configurations, the presence of order parameters (see [[stat-mech-lattice/order-parameter|order parameter]]), and whether multiple equilibrium phases can coexist (see [[stat-mech-lattice/pure-phase|pure phases]] and [[stat-mech-lattice/mixture-gibbs-measures|mixtures of Gibbs measures]]).
