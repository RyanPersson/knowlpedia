---
title: "External-field coupling"
description: "A term in the lattice Hamiltonian that couples spins to a prescribed field, biasing configurations and breaking symmetries."
---

In a lattice spin system with configuration $\sigma$ (see {{< knowl id="spin-configuration" text="spin configuration" >}}), an **external field coupling** is an additive contribution to the {{< knowl id="lattice-hamiltonian" text="lattice Hamiltonian" >}} of the form
$$
H_\Lambda^{\text{field}}(\sigma_\Lambda)= -\sum_{x\in\Lambda} h_x \, m(\sigma_x),
$$
where:
- $(h_x)_{x\in\Lambda}$ is a prescribed real-valued field,
- $m:\mathcal S\to\mathbb{R}$ is a single-site “magnetization” observable (e.g. $m(\sigma_x)=\sigma_x$ for Ising spins $\sigma_x\in\{-1,+1\}$).

The full finite-volume Hamiltonian typically combines interaction and field terms:
$$
H_\Lambda(\sigma_\Lambda\mid \eta)= H_\Lambda^{\Phi}(\sigma_\Lambda\mid \eta) + H_\Lambda^{\text{field}}(\sigma_\Lambda),
$$

where $H_\Lambda^{\Phi}$ comes from an {{< knowl id="interaction-potential-phi" text="interaction potential $\Phi$" >}} and may depend on a {{< knowl id="boundary-condition-lattice" text="boundary condition" >}} $\eta$.

## Cross-links
- The field enters the {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} through the Boltzmann weight and affects the {{< knowl id="partition-function-lattice" text="partition function" >}}.
- Derivatives of the {{< knowl id="pressure-lattice" text="pressure" >}} with respect to a uniform field yield magnetization and susceptibilities (compare {{< knowl id="susceptibility-stat-mech" section="stat-mech" text="susceptibility" >}}).
- In the {{< knowl id="ising-model" text="Ising model" >}}, a uniform field breaks the $\mathbb{Z}_2$ spin-flip symmetry and selects a phase.

## Key properties
1. **Bias and symmetry breaking.** A nonzero field typically breaks any global symmetry under which $m(\sigma_x)$ changes sign (e.g. spin-flip in the Ising model).
2. **Conjugate variable.** The field is thermodynamically conjugate to the order parameter: for a uniform field $h$, the derivative of the infinite-volume pressure with respect to $h$ (when it exists) gives the bulk magnetization.
3. **Uniqueness-enhancing effect.** In many models, a nonzero uniform field eliminates phase coexistence and yields a unique infinite-volume Gibbs measure (model-dependent but common in ferromagnets).
4. **Spatially varying fields.** If $h_x$ varies with $x$, translation invariance is explicitly broken and one can model inhomogeneities or pinning.

## Physical interpretation
The external field represents an imposed environment (e.g. a magnetic field) that energetically favors spins aligned with it. It is the standard control knob for probing response: by varying $h$ one measures how the system’s macroscopic magnetization changes, and one can distinguish spontaneous ordering (nonzero magnetization as $h\to 0$) from field-induced ordering (magnetization only when $h\neq 0$), connecting to {{< knowl id="spontaneous-magnetization" text="spontaneous magnetization" >}}.
