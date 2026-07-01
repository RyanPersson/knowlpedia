+++
id = "stat-mech-lattice/onsager-2d-ising-solution"
title = "Onsager solution of the 2D Ising model (zero field)"
kind = "knowl"
summary = "Exact infinite-volume free energy for the 2D nearest-neighbor Ising model on the square lattice and identification of the critical point."
aliases = ["onsager-2d-ising-solution", "Onsager solution of the 2D Ising model (zero field)"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/onsager-2d-ising-solution.md"
+++

## Context
The [[stat-mech-lattice/ising-model|Ising model]] on the 2D square lattice is the canonical exactly solvable interacting lattice system exhibiting a genuine [[stat-mech-lattice/phase-transition-gibbs|phase transition]] at positive temperature.

Consider the nearest-neighbor ferromagnet (see [[stat-mech-lattice/ferromagnetic-ising|ferromagnetic Ising]]) with Hamiltonian
$$
H(\sigma) = -J\sum_{\langle i,j\rangle}\sigma_i\sigma_j ,
\qquad \sigma_i\in\{-1,+1\},\quad J>0,
$$
in finite volume with partition function (see [[stat-mech/partition-function-canonical|canonical partition function]])
$$
Z_\Lambda(\beta)=\sum_{\sigma_\Lambda}\exp\bigl(-\beta H_\Lambda(\sigma)\bigr).
$$

The (Helmholtz) free energy density is the thermodynamic limit (see [[stat-mech/free-energy-statistical|statistical free energy]])
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

equivalently at $T_c=J/(k_B K_c)$ (using [[thermodynamics/temperature-thermo|temperature]]).

## Key consequences
- **Second-order transition:** the free energy is nonanalytic at $T_c$, yielding a continuous transition with a logarithmic divergence of the specific heat:
  $$
  C_V(T)\sim -A\log|T-T_c| \quad \text{as } T\to T_c,
  $$

  where $C_V$ is the [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]].
- **Spontaneous magnetization (Yang):** below $T_c$ the [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] is strictly positive and has the closed form
  $$
  m(\beta)=\bigl(1-\sinh^{-4}(2K)\bigr)^{1/8}
  \quad \text{for } K>K_c,
  $$

  while $m(\beta)=0$ for $K\le K_c$.
- **Exact critical data:** the solution provides a benchmark for [[stat-mech/universality-class|universality class]] ideas, [[stat-mech/critical-exponent|critical exponents]], and [[stat-mech/scaling-relation-exponents|scaling relations]].

## Prerequisites and connections (cross-links)
- Lattice setup and Gibbs measures: [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]], [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]], [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]].
- Thermodynamic potentials: [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]], [[stat-mech/pressure-log-partition-density|pressure as log-partition density]].
- Order parameters and transitions: [[stat-mech-lattice/order-parameter|order parameter]], [[stat-mech-lattice/phase-transition-gibbs|phase transition indicators]].
