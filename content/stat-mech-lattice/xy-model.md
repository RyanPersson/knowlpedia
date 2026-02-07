---
title: "XY model"
description: "O(2)-symmetric lattice spin model with planar (angle) spins on the circle, featuring continuous symmetry and (in 2D) a Kosterlitz–Thouless transition."
---


The **XY model** (also called the planar rotor or O(2) model) is a lattice spin system with **continuous** spins taking values on the unit circle. It is a canonical example of a model with continuous symmetry in the setting of {{< knowl id="configuration-space-lattice" text="lattice configuration spaces" >}}.

Let $\Lambda\subset\mathbb{Z}^d$ be finite. A spin configuration can be represented either by angles $\theta_x\in[0,2\pi)$ or by unit vectors
$$
S_x=(\cos\theta_x,\sin\theta_x)\in\mathbb{S}^1\subset\mathbb{R}^2.
$$

A standard nearest-neighbor {{< knowl id="lattice-hamiltonian" text="Hamiltonian" >}} with an {{< knowl id="external-field-coupling" text="external field" >}} $\mathbf{h}\in\mathbb{R}^2$ is
$$
H_\Lambda(\theta)
={}
-J\sum_{\langle x,y\rangle:\, x,y\in\Lambda}\cos(\theta_x-\theta_y)
-\sum_{x\in\Lambda}\mathbf{h}\cdot(\cos\theta_x,\sin\theta_x),
\qquad J\in\mathbb{R}.
$$
More generally one can include boundary terms via a {{< knowl id="boundary-condition-lattice" text="boundary condition" >}}.

At inverse temperature $\beta$, the {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} has density proportional to $\exp(-\beta H_\Lambda(\theta))$ with respect to the product of uniform measures on $\mathbb{S}^1$, normalized by the {{< knowl id="partition-function-lattice" text="partition function" >}}.

## Key properties

- **Continuous O(2) symmetry.** When $\mathbf{h}=0$, the Hamiltonian is invariant under global rotations $\theta_x\mapsto \theta_x+\alpha$. This is a prototypical setting for {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}} questions.

- **Low-dimensional constraints (short-range case).** For finite-range, translation-invariant interactions (see {{< knowl id="finite-range-interaction-lattice" text="finite-range interactions" >}} and {{< knowl id="translation-invariant-interaction" text="translation invariance" >}}), continuous symmetry strongly constrains ordering in low dimensions:
  - in $d=1$ there is no phase transition and correlations are short-ranged;
  - in $d=2$ there is no conventional long-range magnetization, but there can be a topological phase transition (below).

- **Kosterlitz–Thouless (KT) transition in $d=2$ (ferromagnetic case).** In two dimensions with $J>0$ and $\mathbf{h}=0$, the model exhibits a KT transition: correlations change from exponential decay at high temperature to **power-law decay** at low temperature. This is reflected in the behavior of the {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point function" >}} and the effective {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}.

- **Order parameter nuances.** The usual vector magnetization is not always the right diagnostic in low dimensions for continuous symmetry. Depending on dimension, one often studies correlation decay, helicity modulus (stiffness), or vortex statistics rather than a nonzero magnetization.

## Physical interpretation

The XY model represents **planar spins** or **phases**:
- planar magnetic moments constrained to rotate in a plane,
- phase variables of a complex order parameter (e.g. superfluid films, superconducting arrays, Josephson junction networks),
- classical rotors with nearest-neighbor alignment.

Its hallmark is the interplay between **continuous symmetry**, **spin-wave fluctuations**, and (in 2D) **topological defects** (vortices), producing phase behavior not captured by discrete-spin models like the {{< knowl id="ising-model" text="Ising model" >}}.
