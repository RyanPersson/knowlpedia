---
title: "Grand partition function"
description: "Normalization of the grand-canonical ensemble; generates the grand potential, mean particle number, and fluctuations."
---


The **grand partition function** $\Xi(\beta,V,\mu)$ is the normalization constant of the {{< knowl id="grand-canonical-ensemble" text="grand-canonical ensemble" >}}, appropriate when a system can exchange both energy and particles with reservoirs that fix inverse temperature $\beta$ and chemical potential $\mu$ (see {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}}).

For a quantum system with Hamiltonian $H$ and particle-number operator $\hat N$, it is
$$
\Xi(\beta,V,\mu) = \mathrm{Tr}\,\exp\!\big[-\beta\,(H-\mu \hat N)\big].
$$

Equivalently, in terms of canonical partition functions (see {{< knowl id="partition-function-canonical" text="canonical partition function" >}}) at fixed $N$,
$$
\Xi(\beta,V,\mu) = \sum_{N=0}^{\infty} e^{\beta \mu N}\, Z(\beta,V,N).
$$

Introducing the fugacity $z = e^{\beta\mu}$, this becomes $\Xi = \sum_{N\ge 0} z^N Z(\beta,V,N)$.

## Role in the grand-canonical ensemble

The grand-canonical probability weight of a microstate $s$ with energy $E_s$ and particle number $N_s$ is proportional to
$$
e^{-\beta(E_s-\mu N_s)},
$$

and division by $\Xi(\beta,V,\mu)$ ensures the probabilities sum to $1$.

This “energy minus chemical work” structure mirrors the thermodynamic combination $U-\mu N$ at fixed $(T,V,\mu)$, which is the natural setting for the {{< knowl id="grand-potential" section="thermodynamics" text="grand potential" >}}.

## Grand potential and pressure

The grand partition function generates the grand potential:
$$
\Omega(T,V,\mu) = -k_B T \ln \Xi(\beta,V,\mu),
$$

with $k_B$ the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}}. For homogeneous systems in the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, the pressure is obtained from $\Omega \approx -pV$, equivalently from the volume scaling of $\ln\Xi$:
$$
p = \frac{k_B T}{V}\,\ln \Xi(\beta,V,\mu)
\quad\text{(in the thermodynamic limit, up to boundary corrections).}
$$
This is one instance of {{< knowl id="pressure-from-partition-function" text="pressure from partition functions" >}}.

## Generating formulas for averages and fluctuations

As with other ensembles, $\ln \Xi$ generates equilibrium expectations (see {{< knowl id="construction-observables-from-log-z" text="observables from log partition functions" >}} and {{< knowl id="construction-fluctuation-formulas-log-z" text="fluctuation formulas from log partition functions" >}}).

**Mean particle number**
$$
\langle N\rangle = \frac{\partial \ln \Xi}{\partial(\beta \mu)}.
$$

**Particle-number fluctuations**
$$
\mathrm{Var}(N) = \frac{\partial^2 \ln \Xi}{\partial(\beta \mu)^2}.
$$

**Mean energy**
Using differentiation with respect to $\beta$ at fixed $\mu$,
$$
\langle E\rangle - \mu \langle N\rangle = -\frac{\partial \ln \Xi}{\partial \beta}.
$$

These identities encode both equilibrium thermodynamics and linear response in the grand-canonical setting, and they are the basis for expressing susceptibilities such as the particle-number compressibility in terms of fluctuations.
