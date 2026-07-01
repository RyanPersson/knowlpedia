+++
id = "stat-mech-lattice/thermodynamic-limit-pressure-lattice"
title = "Thermodynamic limit of pressure (lattice)"
kind = "knowl"
summary = "The existence and properties of the pressure in the infinite-volume limit for lattice systems."
aliases = ["thermodynamic-limit-pressure-lattice", "Thermodynamic limit of pressure (lattice)"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/thermodynamic-limit-pressure-lattice.md"
+++

For a lattice system on a finite region $\Lambda \subset \mathbb{Z}^d$ at inverse temperature $\beta$, the **pressure** (or log-partition density) is
$$
p_\Lambda(\beta) = \frac{1}{|\Lambda|} \log Z_\Lambda(\beta),
$$

where $Z_\Lambda$ is the [[stat-mech/partition-function-canonical|partition function]].

## Thermodynamic limit

Under standard conditions (translation-invariant interactions with suitable decay), the limit
$$
p(\beta) = \lim_{\Lambda \nearrow \mathbb{Z}^d} p_\Lambda(\beta)
$$

exists and is independent of the sequence of regions $\Lambda$ and of [[stat-mech-lattice/boundary-condition-lattice|boundary conditions]].

## Properties

- $p(\beta)$ is a convex function of $\beta^{-1}$.
- Derivatives of $p$ with respect to parameters yield thermodynamic densities (energy, magnetization, etc.).
- Non-analyticity of $p(\beta)$ signals a [[stat-mech-lattice/phase-transition-gibbs|phase transition]].

The pressure is closely connected to the [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] and its [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume limit]]; see also the general notion of [[thermodynamics/thermodynamic-limit|thermodynamic limit]].
