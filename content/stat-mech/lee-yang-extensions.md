---
title: "Lee–Yang Theorem and Extensions"
description: "Lee–Yang location of partition-function zeros for ferromagnets and the notion of the Lee–Yang property; consequences for analyticity and phase transitions."
---

## Prerequisites

- {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}}
- {{< knowl id="ferromagnetic-ising" section="stat-mech-lattice" text="ferromagnetic Ising interactions" >}}
- {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}}
- {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions for Gibbs measures" >}}
- {{< knowl id="tfae-phase-transition-indicators" section="stat-mech-lattice" text="phase transition indicators" >}}
- {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}}

## Finite-volume Lee–Yang circle theorem (Ising ferromagnets)

Let $\Lambda$ be a finite set of sites and consider Ising spins $\sigma_x\in\{\pm 1\}$ with ferromagnetic couplings $J_{xy}\ge 0$.
The finite-volume partition function at inverse temperature $\beta$ and external field $h\in\mathbb{C}$ is
$$
Z_\Lambda(\beta,h)
={}
\sum_{\sigma\in\{\pm1\}^\Lambda}
\exp\!\left(
\beta\sum_{\{x,y\}} J_{xy}\sigma_x\sigma_y
+\beta h\sum_{x\in\Lambda}\sigma_x
\right).
$$

Introduce the “Lee–Yang variable”
$$
z = e^{-2\beta h}.
$$

Using $\sum_x \sigma_x = |\Lambda| - 2N_-(\sigma)$ (where $N_-(\sigma)$ counts the number of $-1$ spins), one can factor
$$
Z_\Lambda(\beta,h) = e^{\beta h|\Lambda|}\,P_\Lambda(z),
$$

where $P_\Lambda$ is a polynomial of degree $|\Lambda|$ with strictly positive real coefficients.

**Lee–Yang circle theorem (one standard form).**  
For ferromagnetic couplings $J_{xy}\ge 0$, every zero of the polynomial $P_\Lambda(z)$ lies on the unit circle:
$$
P_\Lambda(z)=0 \quad\Longrightarrow\quad |z|=1.
$$

Equivalently, every zero of $Z_\Lambda(\beta,h)$ as a function of $h$ satisfies $\mathrm{Re}(h)=0$.

## Consequences for analyticity and phase transitions

- For real external field $h\neq 0$, the Lee–Yang theorem places the finite-volume zeros away from the real axis, and this is a key input to proving analyticity of the thermodynamic free energy/pressure for $h\neq 0$ (compare {{< knowl id="pressure-log-partition-density" text="pressure/log-partition density" >}}).
- In ferromagnets, non-analyticity in the thermodynamic limit can only occur through an accumulation of zeros approaching the real axis. The Lee–Yang picture therefore links:
  - the onset of non-analyticity at $h=0$,
  - and the emergence of {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}}
  (see also {{< knowl id="tfae-phase-transition-indicators" section="stat-mech-lattice" text="phase transition indicators" >}}).

## Extensions: Lee–Yang property as a structural condition

Many generalizations are most cleanly phrased via a **Lee–Yang property**.

**Definition (Lee–Yang property, informal but standard).**  
A spin system with ferromagnetic interactions is said to have the Lee–Yang property if, for every finite volume $\Lambda$, the partition function as a function of complex external field $h$ has no zeros off the imaginary axis (equivalently, after exponentiation, the corresponding polynomial zeros lie on the unit circle in the Lee–Yang variable).

This property is robust under several constructions (often proved by correlation inequalities and contraction arguments), leading to extensions such as:

1. **General graphs and inhomogeneous fields.**  
   The circle theorem holds for Ising ferromagnets on arbitrary finite graphs, not just boxes in $\mathbb{Z}^d$, and with site-dependent complex fields (after an appropriate multivariate formulation).

2. **Lattice-gas formulation.**  
   Under the standard mapping between the Ising model and a lattice gas (see {{< knowl id="lattice-gas-ising-mapping" section="stat-mech-lattice" text="lattice gas–Ising mapping" >}}), Lee–Yang zeros can be interpreted as zeros in a fugacity-like variable, tying the theorem directly to analyticity properties of the grand potential.

3. **Continuous-spin ferromagnets and other single-site measures.**  
   For certain continuous-spin ferromagnets (and more general single-site distributions), one can prove an analogous zero-location statement provided the single-site measure satisfies an appropriate “Lee–Yang admissibility” condition (typically formulated via properties of its Laplace transform).

## How Lee–Yang theory is used in practice

In many models, one uses Lee–Yang zero control to establish:

- analyticity away from $h=0$ (no phase transition for $h\neq 0$),
- constraints on where phase transitions can occur,
- and information about critical behavior from the way zeros approach the real axis in the thermodynamic limit (again aligning with {{< knowl id="tfae-phase-transition-indicators" section="stat-mech-lattice" text="phase transition indicators" >}}).
