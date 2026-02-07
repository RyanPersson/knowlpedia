---
title: "Pressure from the partition function"
description: "In equilibrium, pressure is obtained by differentiating log Z (or log Ξ) with respect to volume at fixed temperature (and chemical potential if applicable)."
---

**Definition (canonical pressure).**  
In the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}, the pressure is defined thermodynamically by
$$
p = -\left(\frac{\partial F}{\partial V}\right)_{T,N},
$$

where $F$ is the {{< knowl id="free-energy-statistical" text="statistical free energy" >}}. Using $F=-k_B T\ln Z$ with the {{< knowl id="partition-function-canonical" text="canonical partition function" >}} $Z(\beta,V,N)$, this becomes the standard partition-function formula
$$
p = \frac{1}{\beta}\left(\frac{\partial}{\partial V}\ln Z(\beta,V,N)\right)_{\beta,N}.
$$
This identity is one of the central instances of {{< knowl id="construction-observables-from-log-z" text="obtaining observables from log Z" >}}.

**Grand canonical form.**  
In the {{< knowl id="grand-canonical-ensemble" text="grand canonical ensemble" >}}, with {{< knowl id="grand-partition-function" text="grand partition function" >}} $\Xi(\beta,\mu,V)$,
$$
p = \frac{1}{\beta}\left(\frac{\partial}{\partial V}\ln \Xi(\beta,\mu,V)\right)_{\beta,\mu}.
$$

For homogeneous systems in the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, $\ln \Xi$ is extensive in $V$, and one commonly writes the equivalent scaling relation
$$
p = \frac{1}{\beta V}\,\ln \Xi(\beta,\mu,V)
\quad\text{(in the limit of large }V\text{, under translation invariance).}
$$

**Physical interpretation.**  
Pressure measures the reversible work required to change volume: $dW_{\text{rev}} = -p\,dV$. The partition function $Z$ (or $\Xi$) encodes how the weighted count of microstates changes when the accessible configuration space expands or contracts. Differentiating $\ln Z$ with respect to $V$ extracts precisely that response, producing the macroscopic force per area. This statistical definition is consistent with {{< knowl id="pressure-thermo" section="thermodynamics" text="thermodynamic pressure" >}}.

**Example (ideal gas).**  
For a classical ideal gas, $Z(\beta,V,N)$ is proportional to $V^N$, so $\ln Z = N\ln V + \text{(terms independent of }V)$, and the formula above yields
$$
pV = Nk_B T.
$$

**Lattice systems note.**  
On a lattice in a finite region {{< knowl id="finite-box-lattice" section="discrete-structures" text="finite box" >}} $\Lambda$, “volume” is $|\Lambda|$. One often defines the (dimensionless) pressure/free-energy density as $\lim_{|\Lambda|\to\infty} |\Lambda|^{-1}\ln Z_\Lambda$, which is the lattice analogue of the continuum scaling behind the formulas above.
