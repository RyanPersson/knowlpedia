+++
id = "thermodynamics/grand-potential"
title = "Grand potential"
kind = "knowl"
summary = "A thermodynamic potential natural for fixed , , and chemical potential."
aliases = ["grand-potential", "Grand potential"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/grand-potential.md"
+++

## Definition and physical meaning

For a [[thermodynamics/thermodynamic-system|thermodynamic system]] with [[thermodynamics/internal-energy-thermo|internal energy]] $U$, [[thermodynamics/temperature-thermo|temperature]] $T$, [[thermodynamics/thermodynamic-entropy|entropy]] $S$, [[thermodynamics/chemical-potential-thermo|chemical potential]] $\mu$, and [[thermodynamics/particle-number|particle number]] $N$, the **grand potential** is the [[thermodynamics/state-function|state function]]
$$
\Omega \equiv U - TS - \mu N.
$$

Equivalently, $\Omega = F - \mu N$ in terms of the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F$. It is the natural thermodynamic potential for an [[thermodynamics/open-system|open system]] that can exchange both energy (as heat) and particles with large reservoirs that fix $T$ and $\mu$, while the volume $V$ is controlled.

## Differential form and natural variables

For a simple compressible single-component system,
$$
d\Omega = -S\,dT - p\,dV - N\,d\mu,
$$

where $p$ is the [[thermodynamics/pressure-thermo|pressure]] and $V$ the [[thermodynamics/volume-thermo|volume]].

Thus $\Omega$ is naturally a function of $(T,V,\mu)$, and it generates:
- $S = -\left(\partial \Omega/\partial T\right)_{V,\mu}$,
- $p = -\left(\partial \Omega/\partial V\right)_{T,\mu}$,
- $N = -\left(\partial \Omega/\partial \mu\right)_{T,V}$.

At fixed $(T,V,\mu)$, equilibrium corresponds to minimizing $\Omega$ (the appropriate analog of minimizing [[thermodynamics/helmholtz-free-energy|$F$]] at fixed $(T,V,N)$).

## Pressure relation in the thermodynamic limit

For a uniform macroscopic system satisfying standard [[thermodynamics/thermodynamic-limit|thermodynamic limit]] assumptions, $\Omega$ is extensive in $V$ and one has the important identity
$$
\Omega = -pV,
$$

which makes $\Omega$ a convenient generator of the [[thermodynamics/equation-of-state|equation of state]] in grand-canonical settings.

## Relation to Legendre transforms and the grand-canonical ensemble

Starting from $F(T,V,N)$, the grand potential is obtained by a [[convex-analysis/legendre-transform|Legendre transform]] that trades the extensive $N$ for its conjugate intensive variable $\mu$.

In statistical mechanics (using the [[thermodynamics/grand-canonical-ensemble-convention|grand-canonical ensemble convention]] and [[thermodynamics/logarithm-convention-natural|natural logarithm convention]]),
$$
\Omega = -k_B T \ln \Xi,
$$

where $\Xi$ is the grand partition function, $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]], and the temperature can also be packaged via the [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta$.
