+++
id = "stat-mech-lattice/heisenberg-model"
title = "Heisenberg model"
kind = "knowl"
summary = "O(3)-symmetric lattice spin model with vector spins on the sphere, modeling isotropic magnetism and continuous-symmetry ordering in statistical mechanics."
aliases = ["heisenberg-model", "Heisenberg model"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/heisenberg-model.md"
+++

In the context of classical lattice spin systems, the **Heisenberg model** (often called the O(3) model) is a continuous-spin model in which each site carries a three-dimensional unit vector.

Let $\Lambda\subset\mathbb{Z}^d$ be finite. A [[stat-mech-lattice/spin-configuration|spin configuration]] is a map $S:\Lambda\to\mathbb{S}^2\subset\mathbb{R}^3$, where the [[stat-mech-lattice/spin-space|spin space]] is the unit sphere $\mathbb{S}^2$. A standard nearest-neighbor [[stat-mech-lattice/lattice-hamiltonian|Hamiltonian]] is
$$
H_\Lambda(S)
={}
-J\sum_{\langle x,y\rangle:\, x,y\in\Lambda} S_x\cdot S_y
-\sum_{x\in\Lambda}\mathbf{h}\cdot S_x,
\qquad J\in\mathbb{R},
$$

with external field $\mathbf{h}\in\mathbb{R}^3$ (an [[stat-mech-lattice/external-field-coupling|external-field coupling]]). Boundary effects can be incorporated via a [[stat-mech-lattice/boundary-condition-lattice|boundary condition]].

At inverse temperature $\beta$, the [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] is proportional to $\exp(-\beta H_\Lambda(S))$ with respect to product surface measure on $(\mathbb{S}^2)^\Lambda$, normalized by the [[stat-mech-lattice/partition-function-lattice|partition function]].

*(Remark: “Heisenberg model” is also used for a quantum spin system; this knowl refers to the classical O(3) lattice model.)*

## Key properties

- **Continuous O(3) symmetry.** For $\mathbf{h}=0$, the model is invariant under global rotations $S_x\mapsto R S_x$ with $R\in\mathrm{O}(3)$. This makes it a central example for studying [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]] and Goldstone-mode fluctuations.

- **Ferromagnetic vs antiferromagnetic.**
  - $J>0$ favors alignment ($S_x\approx S_y$), producing ferromagnetic order in sufficiently high dimension/low temperature.
  - $J<0$ favors antiparallel neighbors, and the nature of ordering depends strongly on lattice geometry (bipartite vs frustrated).

- **Dimensional effects (short-range interactions).** For finite-range, translation-invariant interactions (see [[stat-mech-lattice/finite-range-interaction-lattice|finite-range interactions]]), continuous symmetry suppresses conventional long-range order in low dimensions, while in higher dimensions one can have multiple [[stat-mech-lattice/pure-phase|pure phases]] and nontrivial [[stat-mech-lattice/phase-transition-gibbs|phase transitions]].

- **Correlations and response.** The behavior of [[stat-mech/correlation-function-two-point|two-point correlations]], the [[stat-mech/correlation-length|correlation length]], and the [[stat-mech/susceptibility-stat-mech|susceptibility]] are central diagnostics of ordering and criticality.

- **Relation to other O(n) models.** The [[stat-mech-lattice/xy-model|XY model]] is the O(2) analogue with spins on $\mathbb{S}^1$, and many structural arguments (symmetries, spin waves, low-dimensional constraints) parallel between O(2) and O(3).

## Physical interpretation

The Heisenberg model is a basic model for **isotropic classical magnetism**, where local magnetic moments can point in any direction in $\mathbb{R}^3$ and energetically prefer to align (ferromagnet) or anti-align (antiferromagnet). Its continuous symmetry makes it a standard laboratory for:
- how long-range order depends on dimension,
- how low-energy collective excitations affect correlations,
- how ordered phases are described by [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] (often extremal ones; see [[stat-mech-lattice/extremal-gibbs-measure|extremal Gibbs measures]]).
