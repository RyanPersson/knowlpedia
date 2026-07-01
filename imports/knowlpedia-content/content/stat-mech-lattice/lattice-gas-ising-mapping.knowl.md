+++
id = "stat-mech-lattice/lattice-gas-ising-mapping"
title = "Lattice gas ↔ Ising model mapping"
kind = "knowl"
summary = "Exact change of variables between occupation variables n∈{0,1} and Ising spins σ∈{±1}, relating chemical potential to magnetic field and liquid–gas coexistence to spin-flip symmetry."
aliases = ["lattice-gas-ising-mapping", "Lattice gas ↔ Ising model mapping"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/lattice-gas-ising-mapping.md"
+++

## Prerequisites and notation

- Lattice Hamiltonians: [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]]
- Ising basics: [[stat-mech-lattice/ising-model|Ising model]], [[stat-mech-lattice/order-parameter|order parameter]]
- Gibbs formalism: [[stat-mech/canonical-ensemble|canonical ensemble]], [[stat-mech/partition-function-canonical|partition function]]

Let $\Lambda$ be a finite graph/lattice with coordination number $z$ (e.g. $z=4$ for the square lattice).

## Example: nearest-neighbor lattice gas and its Ising representation

### Lattice-gas variables and Hamiltonian
A lattice gas uses occupation numbers $n_x\in\{0,1\}$ with Hamiltonian
$$
H_{\Lambda}^{\mathrm{LG}}(n)
= -\varepsilon\sum_{\langle x,y\rangle} n_x n_y \;-\; \mu\sum_{x\in\Lambda} n_x,
$$

where $\varepsilon>0$ is an attractive interaction and $\mu$ is the chemical potential.

### Change of variables to spins
Define Ising spins $\sigma_x\in\{-1,+1\}$ by
$$
n_x=\frac{1+\sigma_x}{2}
\quad\Longleftrightarrow\quad
\sigma_x = 2n_x-1.
$$
Then
$$
n_x n_y = \frac{1}{4}\bigl(1+\sigma_x+\sigma_y+\sigma_x\sigma_y\bigr).
$$

### Resulting Ising Hamiltonian
Substituting into $H_{\Lambda}^{\mathrm{LG}}$ and collecting terms yields
$$
H_{\Lambda}^{\mathrm{LG}}(n)
= -J\sum_{\langle x,y\rangle}\sigma_x\sigma_y \;-\; h\sum_{x\in\Lambda}\sigma_x \;+\; \text{constant},
$$
with parameters
$$
J=\frac{\varepsilon}{4},
\qquad
h=\frac{\mu}{2}+\frac{\varepsilon z}{4}.
$$
Thus the lattice gas in the grand-canonical ensemble is exactly an [[stat-mech-lattice/ising-model|Ising model]] in a field.

### Dictionary of observables
- Density $\rho$ vs magnetization $m$:
  $$
  \rho=\langle n_x\rangle = \frac{1+\langle \sigma_x\rangle}{2} = \frac{1+m}{2}.
  $$

- Compressibility and response correspondences follow similarly by differentiating with respect to $\mu$ and $h$.

### Coexistence line as zero field (particle–hole symmetry)
The Ising spin-flip symmetry corresponds to particle–hole symmetry in the lattice gas. The coexistence curve is the line where the effective field vanishes:
$$
h=0 \quad\Longleftrightarrow\quad \mu = -\frac{\varepsilon z}{2}.
$$
On this line, the two Ising phases (for dimensions where symmetry breaking occurs) correspond to high-density “liquid” and low-density “gas” phases. In particular, the 2D lattice gas inherits the phase transition of [[stat-mech-lattice/ising-2d-phase-transition|the 2D Ising model]].

### Consequence: universality and order parameters
Because the mapping is exact, critical behavior (exponents, scaling forms) is shared between the lattice gas and the Ising model in the same dimension; the order parameter can be taken as $\rho-\tfrac12$ or equivalently $m$ (see [[stat-mech-lattice/order-parameter|order parameter]]).
