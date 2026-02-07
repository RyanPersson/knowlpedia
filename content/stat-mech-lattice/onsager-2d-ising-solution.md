---
title: "Onsager solution of the 2D Ising model (zero field)"
description: "Exact infinite-volume free energy for the 2D nearest-neighbor Ising model on the square lattice and identification of the critical point."
---

## Context
The {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}} on the 2D square lattice is the canonical exactly solvable interacting lattice system exhibiting a genuine {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transition" >}} at positive temperature.

Consider the nearest-neighbor ferromagnet (see {{< knowl id="ferromagnetic-ising" section="stat-mech-lattice" text="ferromagnetic Ising" >}}) with Hamiltonian
$$
H(\sigma) = -J\sum_{\langle i,j\rangle}\sigma_i\sigma_j ,
\qquad \sigma_i\in\{-1,+1\},\quad J>0,
$$
in finite volume with partition function (see {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}})
$$
Z_\Lambda(\beta)=\sum_{\sigma_\Lambda}\exp\bigl(-\beta H_\Lambda(\sigma)\bigr).
$$

The (Helmholtz) free energy density is the thermodynamic limit (see {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}})
$$
f(\beta)= -\frac{1}{\beta}\lim_{|\Lambda|\to\infty}\frac{1}{|\Lambda|}\log Z_\Lambda(\beta),
$$
when the limit exists.

## Theorem (Onsager, zero external field)
Let $K=\beta J$ and define the modulus
$$
k(K)=\frac{2\sinh(2K)}{\cosh^2(2K)}.
$$
For the 2D square-lattice Ising model at zero field, the infinite-volume free energy density exists and satisfies the exact formula
$$
-\beta f(\beta)
={}
\ln\!\bigl(2\cosh(2K)\bigr)
+\frac{1}{2\pi}\int_0^\pi
\ln\!\left(
\frac{1+\sqrt{1-k(K)^2\sin^2\theta}}{2}
\right)\,d\theta.
$$
Moreover, the nonanalyticity occurs precisely at
$$
\sinh\!\bigl(2K_c\bigr)=1
\qquad\Longleftrightarrow\qquad
K_c=\frac12\ln(1+\sqrt2),
$$

equivalently at $T_c=J/(k_B K_c)$ (using {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}).

## Key consequences
- **Second-order transition:** the free energy is nonanalytic at $T_c$, yielding a continuous transition with a logarithmic divergence of the specific heat:
  $$
  C_V(T)\sim -A\log|T-T_c| \quad \text{as } T\to T_c,
  $$

  where $C_V$ is the {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="heat capacity at constant volume" >}}.
- **Spontaneous magnetization (Yang):** below $T_c$ the {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}} is strictly positive and has the closed form
  $$
  m(\beta)=\bigl(1-\sinh^{-4}(2K)\bigr)^{1/8}
  \quad \text{for } K>K_c,
  $$

  while $m(\beta)=0$ for $K\le K_c$.
- **Exact critical data:** the solution provides a benchmark for {{< knowl id="universality-class" section="stat-mech" text="universality class" >}} ideas, {{< knowl id="critical-exponent" section="stat-mech" text="critical exponents" >}}, and {{< knowl id="scaling-relation-exponents" section="stat-mech" text="scaling relations" >}}.

## Prerequisites and connections (cross-links)
- Lattice setup and Gibbs measures: {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}}, {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}}, {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}}.
- Thermodynamic potentials: {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}, {{< knowl id="pressure-log-partition-density" section="stat-mech" text="pressure as log-partition density" >}}.
- Order parameters and transitions: {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}, {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transition indicators" >}}.
