---
title: "Heisenberg model"
description: "O(3)-symmetric lattice spin model with vector spins on the sphere, modeling isotropic magnetism and continuous-symmetry ordering in statistical mechanics."
---


In the context of classical lattice spin systems, the **Heisenberg model** (often called the O(3) model) is a continuous-spin model in which each site carries a three-dimensional unit vector.

Let $\Lambda\subset\mathbb{Z}^d$ be finite. A {{< knowl id="spin-configuration" text="spin configuration" >}} is a map $S:\Lambda\to\mathbb{S}^2\subset\mathbb{R}^3$, where the {{< knowl id="spin-space" text="spin space" >}} is the unit sphere $\mathbb{S}^2$. A standard nearest-neighbor {{< knowl id="lattice-hamiltonian" text="Hamiltonian" >}} is
$$
H_\Lambda(S)
={}
-J\sum_{\langle x,y\rangle:\, x,y\in\Lambda} S_x\cdot S_y
-\sum_{x\in\Lambda}\mathbf{h}\cdot S_x,
\qquad J\in\mathbb{R},
$$

with external field $\mathbf{h}\in\mathbb{R}^3$ (an {{< knowl id="external-field-coupling" text="external-field coupling" >}}). Boundary effects can be incorporated via a {{< knowl id="boundary-condition-lattice" text="boundary condition" >}}.

At inverse temperature $\beta$, the {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} is proportional to $\exp(-\beta H_\Lambda(S))$ with respect to product surface measure on $(\mathbb{S}^2)^\Lambda$, normalized by the {{< knowl id="partition-function-lattice" text="partition function" >}}.

*(Remark: “Heisenberg model” is also used for a quantum spin system; this knowl refers to the classical O(3) lattice model.)*

## Key properties

- **Continuous O(3) symmetry.** For $\mathbf{h}=0$, the model is invariant under global rotations $S_x\mapsto R S_x$ with $R\in\mathrm{O}(3)$. This makes it a central example for studying {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}} and Goldstone-mode fluctuations.

- **Ferromagnetic vs antiferromagnetic.**
  - $J>0$ favors alignment ($S_x\approx S_y$), producing ferromagnetic order in sufficiently high dimension/low temperature.
  - $J<0$ favors antiparallel neighbors, and the nature of ordering depends strongly on lattice geometry (bipartite vs frustrated).

- **Dimensional effects (short-range interactions).** For finite-range, translation-invariant interactions (see {{< knowl id="finite-range-interaction-lattice" text="finite-range interactions" >}}), continuous symmetry suppresses conventional long-range order in low dimensions, while in higher dimensions one can have multiple {{< knowl id="pure-phase" text="pure phases" >}} and nontrivial {{< knowl id="phase-transition-gibbs" text="phase transitions" >}}.

- **Correlations and response.** The behavior of {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlations" >}}, the {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}, and the {{< knowl id="susceptibility-stat-mech" section="stat-mech" text="susceptibility" >}} are central diagnostics of ordering and criticality.

- **Relation to other O(n) models.** The {{< knowl id="xy-model" text="XY model" >}} is the O(2) analogue with spins on $\mathbb{S}^1$, and many structural arguments (symmetries, spin waves, low-dimensional constraints) parallel between O(2) and O(3).

## Physical interpretation

The Heisenberg model is a basic model for **isotropic classical magnetism**, where local magnetic moments can point in any direction in $\mathbb{R}^3$ and energetically prefer to align (ferromagnet) or anti-align (antiferromagnet). Its continuous symmetry makes it a standard laboratory for:
- how long-range order depends on dimension,
- how low-energy collective excitations affect correlations,
- how ordered phases are described by {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}} (often extremal ones; see {{< knowl id="extremal-gibbs-measure" text="extremal Gibbs measures" >}}).
