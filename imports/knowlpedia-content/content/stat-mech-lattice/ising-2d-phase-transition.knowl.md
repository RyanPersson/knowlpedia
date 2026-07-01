+++
id = "stat-mech-lattice/ising-2d-phase-transition"
title = "2D Ising model: finite-temperature phase transition"
kind = "knowl"
summary = "Square-lattice Ising model with Onsager’s critical temperature, spontaneous magnetization below Tc, and diverging correlation length at criticality."
aliases = ["ising-2d-phase-transition", "2D Ising model: finite-temperature phase transition"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/ising-2d-phase-transition.md"
+++

## Prerequisites and notation

- Model definition: [[stat-mech-lattice/ising-model|Ising model]], [[stat-mech-lattice/ferromagnetic-ising|ferromagnetic Ising interaction]]
- Gibbs formalism: [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]], [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]], [[stat-mech-lattice/dlr-equation|DLR equations]]
- Phase transition notions: [[stat-mech-lattice/phase-transition-gibbs|phase transition (Gibbs measure non-uniqueness)]], [[stat-mech-lattice/order-parameter|order parameter]]
- Correlations: [[stat-mech/correlation-length|correlation length]], [[stat-mech/structure-factor|structure factor]]

We consider spins $\sigma_x\in\{-1,+1\}$ on $\mathbb{Z}^2$ (or on an $L\times L$ torus for finite volume).

## Example: 2D square-lattice nearest-neighbor Ising model

### Hamiltonian
For a finite region $\Lambda\subset\mathbb{Z}^2$,
$$
H_\Lambda(\sigma) = -J\sum_{\langle x,y\rangle\subset\Lambda} \sigma_x\sigma_y - h\sum_{x\in\Lambda}\sigma_x,
\qquad J>0,
$$

where $\langle x,y\rangle$ are nearest-neighbor edges.

### Critical temperature
At zero field $h=0$, the 2D nearest-neighbor model has a critical inverse temperature
$$
\beta_c J = \frac{1}{2}\log(1+\sqrt{2}),
\qquad T_c = \frac{1}{k_B\beta_c}.
$$

For $T>T_c$ the equilibrium state is unique; for $T<T_c$ there are (at least) two distinct infinite-volume Gibbs measures corresponding to the two magnetized phases.

### Spontaneous magnetization (order parameter)
The magnetization per site (in the thermodynamic limit) is the natural [[stat-mech-lattice/order-parameter|order parameter]]:
$$
m(\beta) = \lim_{h\downarrow 0}\lim_{|\Lambda|\to\infty}\frac{1}{|\Lambda|}\sum_{x\in\Lambda}\langle \sigma_x\rangle_{\Lambda,\beta,h}.
$$

At $h=0$, the exact spontaneous magnetization for $\beta>\beta_c$ is
$$
m(\beta) = \left(1-\sinh^{-4}(2\beta J)\right)^{1/8},
\qquad \beta>\beta_c,
$$

and $m(\beta)=0$ for $\beta\le \beta_c$. This sharp onset is a hallmark of a phase transition and contrasts with [[stat-mech-lattice/ising-1d-no-phase-transition|the 1D chain]].

### Correlation length and criticality
For $T\neq T_c$, correlations decay exponentially and define a finite [[stat-mech/correlation-length|correlation length]] $\xi(T)$; at criticality $T=T_c$ the correlation length diverges, and correlations decay by a power law. Equivalently, the small-$k$ behavior of the [[stat-mech/structure-factor|structure factor]] becomes singular at $T_c$.

### Thermodynamic singularities
The free energy density is nonanalytic at $T_c$. A standard thermodynamic signature is the specific heat: in 2D it diverges logarithmically at criticality (in contrast to the smooth behavior in 1D).

### Gibbs-measure viewpoint (DLR and coexistence)
Below $T_c$, distinct infinite-volume Gibbs measures $\mu^+$ and $\mu^-$ solve the [[stat-mech-lattice/dlr-equation|DLR equations]] and satisfy
$$
\mu^+(\sigma_0)=+m(\beta),\qquad \mu^-(\sigma_0)=-m(\beta).
$$
This non-uniqueness is the equilibrium meaning of a [[stat-mech-lattice/phase-transition-gibbs|phase transition]].
