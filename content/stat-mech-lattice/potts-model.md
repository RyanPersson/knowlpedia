---
title: "Potts model"
description: "q-state lattice spin model with permutation symmetry, generalizing the Ising model and closely related to the random-cluster model."
---


The **Potts model** is a lattice spin system in which each site carries one of $q$ discrete states (“colors”). It generalizes the {{< knowl id="ising-model" text="Ising model" >}} from two spin values to $q\ge 2$ values.

Let $\Lambda$ be a finite subset of $\mathbb{Z}^d$ (or a finite graph) and fix an integer $q\ge 2$. A {{< knowl id="spin-configuration" text="spin configuration" >}} is a map $\sigma:\Lambda\to\{1,2,\dots,q\}$, i.e. the {{< knowl id="spin-space" text="spin space" >}} is $\{1,\dots,q\}$. With boundary condition $\eta$ on $\Lambda^c$, a standard nearest-neighbor {{< knowl id="lattice-hamiltonian" text="Hamiltonian" >}} is
$$
H_\Lambda(\sigma\mid \eta)
={}
-J\sum_{\langle x,y\rangle:\, x,y\in\Lambda}\mathbf{1}\{\sigma_x=\sigma_y\}
-J\sum_{\substack{\langle x,y\rangle:\\ x\in\Lambda,\,y\notin\Lambda}}\mathbf{1}\{\sigma_x=\eta_y\}
-\sum_{x\in\Lambda} h_{\sigma_x},
$$

where $J\in\mathbb{R}$ controls the interaction and $(h_1,\dots,h_q)$ is an {{< knowl id="external-field-coupling" text="external field" >}} favoring certain states.

At inverse temperature $\beta$, the associated {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} is proportional to $\exp(-\beta H_\Lambda(\sigma\mid\eta))$, normalized by the {{< knowl id="partition-function-lattice" text="partition function" >}}.

## Key properties

- **Ferromagnetic vs antiferromagnetic.**
  - If $J>0$, equal neighboring spins are favored (ferromagnetic Potts).
  - If $J<0$, unequal neighbors are favored (antiferromagnetic Potts), tying the model to graph coloring constraints at low temperature.

- **Symmetry.** With $h_a\equiv 0$, the model is invariant under permutations of the $q$ states (the symmetry group is $S_q$). Ordered phases correspond to selecting a preferred state, captured by an {{< knowl id="order-parameter" text="order parameter" >}} such as the deviation of state densities from $1/q$.

- **Reduction to Ising at $q=2$.** For $q=2$, the Potts model is equivalent (after a simple reparameterization and additive energy shift) to the {{< knowl id="ising-model" text="Ising model" >}}.

- **Random-cluster (Fortuin–Kasteleyn) representation.** In the ferromagnetic case, the Potts model is tightly linked to the {{< knowl id="random-cluster-model" text="random-cluster model" >}}: the Potts partition function can be rewritten as a sum over bond configurations with a cluster weight $q$. This connection is a key tool for studying {{< knowl id="phase-transition-gibbs" text="phase transitions" >}} and correlations.

- **Correlations and criticality.** Two-point correlations (see {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation functions" >}}) can exhibit long-range order or critical decay depending on dimension, $q$, and the sign of $J$. In two dimensions, the ferromagnetic model has especially rich and well-understood critical behavior.

## Physical interpretation

The Potts model describes systems with **multiple equivalent local states**, such as:
- multi-orientational “spins” in magnetic or structural phase transitions,
- domain formation with $q$ possible labels,
- simplified models of ordering where the order parameter selects one of several symmetry-related states.

The ferromagnetic model captures **domain alignment** (neighboring sites prefer the same state), while the antiferromagnetic model captures **competition** (neighbors prefer different states), often leading to frustration and highly constrained low-temperature structure.
