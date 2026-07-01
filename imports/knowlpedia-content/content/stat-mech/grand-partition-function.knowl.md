+++
id = "stat-mech/grand-partition-function"
title = "Grand partition function"
kind = "knowl"
summary = "Normalization of the grand-canonical ensemble; generates the grand potential, mean particle number, and fluctuations."
aliases = ["grand-partition-function", "Grand partition function"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/grand-partition-function.md"
+++

The **grand partition function** $\Xi(\beta,V,\mu)$ is the normalization constant of the [[stat-mech/grand-canonical-ensemble|grand-canonical ensemble]], appropriate when a system can exchange both energy and particles with reservoirs that fix inverse temperature $\beta$ and chemical potential $\mu$ (see [[thermodynamics/chemical-potential-thermo|chemical potential]]).

For a quantum system with Hamiltonian $H$ and particle-number operator $\hat N$, it is
$$
\Xi(\beta,V,\mu) = \mathrm{Tr}\,\exp\!\big[-\beta\,(H-\mu \hat N)\big].
$$

Equivalently, in terms of canonical partition functions (see [[stat-mech/partition-function-canonical|canonical partition function]]) at fixed $N$,
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

This “energy minus chemical work” structure mirrors the thermodynamic combination $U-\mu N$ at fixed $(T,V,\mu)$, which is the natural setting for the [[thermodynamics/grand-potential|grand potential]].

## Grand potential and pressure

The grand partition function generates the grand potential:
$$
\Omega(T,V,\mu) = -k_B T \ln \Xi(\beta,V,\mu),
$$

with $k_B$ the [[thermodynamics/boltzmann-constant|Boltzmann constant]]. For homogeneous systems in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], the pressure is obtained from $\Omega \approx -pV$, equivalently from the volume scaling of $\ln\Xi$:
$$
p = \frac{k_B T}{V}\,\ln \Xi(\beta,V,\mu)
\quad\text{(in the thermodynamic limit, up to boundary corrections).}
$$
This is one instance of [[stat-mech/pressure-from-partition-function|pressure from partition functions]].

## Generating formulas for averages and fluctuations

As with other ensembles, $\ln \Xi$ generates equilibrium expectations (see [[stat-mech/construction-observables-from-log-z|observables from log partition functions]] and [[stat-mech/construction-fluctuation-formulas-log-z|fluctuation formulas from log partition functions]]).

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
