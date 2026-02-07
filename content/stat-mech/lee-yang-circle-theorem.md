---
title: "Lee–Yang circle theorem"
description: "For ferromagnetic Ising models, zeros of the finite-volume partition function in the complex magnetic-field fugacity lie on the unit circle, implying analyticity for real nonzero field."
---

## Statement

Let $\Lambda$ be finite and consider the ferromagnetic {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}} with couplings $J_{ij}\ge 0$ and a **uniform** external magnetic field $h\in\mathbb{C}$:
$$
H_\Lambda(\sigma)
= -\sum_{\{i,j\}\subset\Lambda} J_{ij}\,\sigma_i\sigma_j - h\sum_{i\in\Lambda}\sigma_i.
$$

Let $Z_\Lambda(h)$ be the associated {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="partition function" >}}.

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
- Partition function context: {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="partition function" >}}, {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="pressure" >}}.

### Conclusions
- **Location of zeros:** zeros in the fugacity variable $z=e^{-2h}$ lie on $|z|=1$.
- **Analyticity for real nonzero field:** for real $h\ne 0$, $z$ is positive real and not on the unit circle, hence $Z_\Lambda(h)\ne 0$. Consequently the finite-volume pressure $\frac{1}{|\Lambda|}\log Z_\Lambda(h)$ is analytic in $h$ for real $h\ne 0$.
- **Constraint on phase transitions:** any nonanalyticity in the thermodynamic limit as a function of real $h$ can only occur at $h=0$ (a key input into uniqueness/analyticity results; compare {{< knowl id="corollary-uniqueness-analyticity" text="uniqueness/analyticity corollary" >}}).


The theorem is proved by showing that the Ising partition function defines a polynomial with a strong stability property inherited from ferromagnetism. One classical approach uses inductive “contraction” arguments (e.g. Asano-type contractions) that preserve the zero-free region and ultimately force all zeros onto the unit circle.

In applications, Lee–Yang zeros provide a powerful route from finite-volume polynomial structure to thermodynamic analyticity and the study of symmetry breaking at $h=0$ (see {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions" >}}).
