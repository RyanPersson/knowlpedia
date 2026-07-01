+++
id = "stat-mech/lee-yang-circle-theorem"
title = "Lee–Yang circle theorem"
kind = "knowl"
summary = "For ferromagnetic Ising models, zeros of the finite-volume partition function in the complex magnetic-field fugacity lie on the unit circle, implying analyticity for real nonzero field."
aliases = ["lee-yang-circle-theorem", "Lee–Yang circle theorem"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/lee-yang-circle-theorem.md"
+++

## Statement

Let $\Lambda$ be finite and consider the ferromagnetic [[stat-mech-lattice/ising-model|Ising model]] with couplings $J_{ij}\ge 0$ and a **uniform** external magnetic field $h\in\mathbb{C}$:
$$
H_\Lambda(\sigma)
= -\sum_{\{i,j\}\subset\Lambda} J_{ij}\,\sigma_i\sigma_j - h\sum_{i\in\Lambda}\sigma_i.
$$

Let $Z_\Lambda(h)$ be the associated [[stat-mech-lattice/partition-function-lattice|partition function]].

Introduce the complex fugacity variable
$$
z := e^{-2h}.
$$

Up to a nonvanishing prefactor, $Z_\Lambda(h)$ becomes a polynomial in $z$ (of degree $|\Lambda|$).

**Lee–Yang circle theorem.**
All zeros of this polynomial lie on the unit circle:
$$
Z_\Lambda(h)=0 \quad\Longrightarrow\quad |z|=1.
$$

Equivalently, $Z_\Lambda(h)$ has no zeros for $\mathrm{Re}(h)\ne 0$.

## Key hypotheses and conclusions

### Hypotheses
- Finite volume $\Lambda$.
- Ising spins $\sigma_i\in\{-1,+1\}$.
- Ferromagnetic couplings $J_{ij}\ge 0$.
- A single (uniform) external field $h$ treated as a complex parameter.
- Partition function context: [[stat-mech-lattice/partition-function-lattice|partition function]], [[stat-mech-lattice/pressure-lattice|pressure]].

### Conclusions
- **Location of zeros:** zeros in the fugacity variable $z=e^{-2h}$ lie on $|z|=1$.
- **Analyticity for real nonzero field:** for real $h\ne 0$, $z$ is positive real and not on the unit circle, hence $Z_\Lambda(h)\ne 0$. Consequently the finite-volume pressure $\frac{1}{|\Lambda|}\log Z_\Lambda(h)$ is analytic in $h$ for real $h\ne 0$.
- **Constraint on phase transitions:** any nonanalyticity in the thermodynamic limit as a function of real $h$ can only occur at $h=0$ (a key input into uniqueness/analyticity results; compare [[stat-mech/corollary-uniqueness-analyticity|uniqueness/analyticity corollary]]).


The theorem is proved by showing that the Ising partition function defines a polynomial with a strong stability property inherited from ferromagnetism. One classical approach uses inductive “contraction” arguments (e.g. Asano-type contractions) that preserve the zero-free region and ultimately force all zeros onto the unit circle.

In applications, Lee–Yang zeros provide a powerful route from finite-volume polynomial structure to thermodynamic analyticity and the study of symmetry breaking at $h=0$ (see [[stat-mech-lattice/phase-transition-gibbs|phase transitions]]).
