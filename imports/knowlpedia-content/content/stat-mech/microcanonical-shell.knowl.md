+++
id = "stat-mech/microcanonical-shell"
title = "Microcanonical shell"
kind = "knowl"
summary = "Thin region of phase space defined by an energy window, representing the accessible microstates of an isolated system at fixed energy."
aliases = ["microcanonical-shell", "Microcanonical shell"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/microcanonical-shell.md"
+++

Let $\Gamma$ be a classical [[stat-mech/phase-space-classical|phase space]] with Liouville [[stat-mech/phase-space-volume-element|volume element]] $d\Gamma$, and let $H(x)$ be the [[stat-mech/hamiltonian-function-classical|Hamiltonian]]. Fix an energy value $E$ and an energy resolution (window width) $\Delta E>0$.

The **microcanonical shell** at energy $E$ with width $\Delta E$ is the subset
$$
\Sigma_{E,\Delta E} \;=\; \big\{x\in\Gamma:\; E \le H(x)\le E+\Delta E\big\}.
$$

A common symmetric convention is $\{x:\, |H(x)-E|\le \Delta E/2\}$; the physics is unchanged as long as $\Delta E$ is small on macroscopic scales but large compared to microscopic level spacing (in quantum settings).

The “ideal” energy surface $\Sigma_E=\{x:\,H(x)=E\}$ has codimension one in $\Gamma$ and therefore has zero Liouville volume, which is why the shell (a *thickened* surface) is typically used in defining probabilities.

## Phase-space volume of the shell
The Liouville volume of $\Sigma_{E,\Delta E}$ is
$$
\Omega(E,\Delta E) \;=\; \int_{\Gamma}\mathbf{1}\!\left\{E\le H(x)\le E+\Delta E\right\}\, d\Gamma.
$$

In terms of the [[stat-mech/density-of-states|density of states]] $g(E)$, for small $\Delta E$ one has the approximation
$$
\Omega(E,\Delta E) \;\approx\; g(E)\,\Delta E.
$$

## Physical interpretation
A classical isolated system evolves at constant energy (up to experimental resolution), so its accessible [[stat-mech/microstate-classical|microstates]] lie (approximately) in $\Sigma_{E,\Delta E}$. The microcanonical shell is the geometric object on which the [[stat-mech/microcanonical-measure|microcanonical measure]] places equal a priori weight.

In practice one may further restrict the shell by other conserved quantities (e.g., total momentum), but the defining idea remains: the shell encodes the accessible region in phase space given macroscopic constraints.
