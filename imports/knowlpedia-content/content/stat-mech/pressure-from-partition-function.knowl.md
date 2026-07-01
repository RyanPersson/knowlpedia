+++
id = "stat-mech/pressure-from-partition-function"
title = "Pressure from the partition function"
kind = "knowl"
summary = "In equilibrium, pressure is obtained by differentiating log Z (or log Ξ) with respect to volume at fixed temperature (and chemical potential if applicable)."
aliases = ["pressure-from-partition-function", "Pressure from the partition function"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/pressure-from-partition-function.md"
+++

**Definition (canonical pressure).**
In the [[stat-mech/canonical-ensemble|canonical ensemble]], the pressure is defined thermodynamically by
$$
p = -\left(\frac{\partial F}{\partial V}\right)_{T,N},
$$

where $F$ is the [[stat-mech/free-energy-statistical|statistical free energy]]. Using $F=-k_B T\ln Z$ with the [[stat-mech/partition-function-canonical|canonical partition function]] $Z(\beta,V,N)$, this becomes the standard partition-function formula
$$
p = \frac{1}{\beta}\left(\frac{\partial}{\partial V}\ln Z(\beta,V,N)\right)_{\beta,N}.
$$
This identity is one of the central instances of [[stat-mech/construction-observables-from-log-z|obtaining observables from log Z]].

**Grand canonical form.**
In the [[stat-mech/grand-canonical-ensemble|grand canonical ensemble]], with [[stat-mech/grand-partition-function|grand partition function]] $\Xi(\beta,\mu,V)$,
$$
p = \frac{1}{\beta}\left(\frac{\partial}{\partial V}\ln \Xi(\beta,\mu,V)\right)_{\beta,\mu}.
$$

For homogeneous systems in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], $\ln \Xi$ is extensive in $V$, and one commonly writes the equivalent scaling relation
$$
p = \frac{1}{\beta V}\,\ln \Xi(\beta,\mu,V)
\quad\text{(in the limit of large }V\text{, under translation invariance).}
$$

**Physical interpretation.**
Pressure measures the reversible work required to change volume: $dW_{\text{rev}} = -p\,dV$. The partition function $Z$ (or $\Xi$) encodes how the weighted count of microstates changes when the accessible configuration space expands or contracts. Differentiating $\ln Z$ with respect to $V$ extracts precisely that response, producing the macroscopic force per area. This statistical definition is consistent with [[thermodynamics/pressure-thermo|thermodynamic pressure]].

**Example (ideal gas).**
For a classical ideal gas, $Z(\beta,V,N)$ is proportional to $V^N$, so $\ln Z = N\ln V + \text{(terms independent of }V)$, and the formula above yields
$$
pV = Nk_B T.
$$

**Lattice systems note.**
On a lattice in a finite region [[discrete-structures/finite-box-lattice|finite box]] $\Lambda$, “volume” is $|\Lambda|$. One often defines the (dimensionless) pressure/free-energy density as $\lim_{|\Lambda|\to\infty} |\Lambda|^{-1}\ln Z_\Lambda$, which is the lattice analogue of the continuum scaling behind the formulas above.
