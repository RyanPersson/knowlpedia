+++
id = "stat-mech/isothermal-isobaric-partition-function"
title = "Isothermal–isobaric partition function"
kind = "knowl"
summary = "Normalization of the NPT ensemble; Laplace transform of the canonical partition function and generator of the Gibbs free energy."
aliases = ["isothermal-isobaric-partition-function", "Isothermal–isobaric partition function"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/isothermal-isobaric-partition-function.md"
+++

The **isothermal–isobaric partition function** $\Delta(\beta,p,N)$ is the normalization constant of the [[stat-mech/isothermal-isobaric-ensemble|isothermal–isobaric (NPT) ensemble]], which describes equilibrium at fixed inverse temperature $\beta$, fixed pressure $p$, and fixed particle number $N$, with fluctuating volume.

It is naturally expressed in terms of the [[stat-mech/partition-function-canonical|canonical partition function]] $Z(\beta,V,N)$ by integrating over all volumes with the pressure weight:
$$
\Delta(\beta,p,N) = \int_{0}^{\infty} dV\; e^{-\beta pV}\, Z(\beta,V,N).
$$

Mathematically, $\Delta$ is a Laplace transform of $Z$ with respect to $V$.

## Physical meaning of the weight

In the NPT ensemble, microstates carry Boltzmann weight for the combination $H+pV$, where $H$ is the system [[stat-mech/hamiltonian-function-classical|Hamiltonian]]. The factor $e^{-\beta pV}$ expresses mechanical equilibrium with a pressure reservoir: larger volumes are penalized by the work term $pV$ in the effective energy.

## Gibbs free energy from Δ

The partition function $\Delta$ generates the [[thermodynamics/gibbs-free-energy|Gibbs free energy]]:
$$
G(T,p,N) = -k_B T \ln \Delta(\beta,p,N),
$$

where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]] and $\beta = 1/(k_B T)$. This matches the thermodynamic fact that $G$ is the natural potential at fixed $(T,p,N)$, i.e. after Legendre transforming the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] with respect to volume.

In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], $G$ is extensive and one often uses $g = \lim_{N\to\infty} G/N$.

## Generating formulas for volume statistics

The logarithm of $\Delta$ generates equilibrium averages (see [[stat-mech/construction-observables-from-log-z|observables from log partition functions]]), in particular for the volume:

**Mean volume**
$$
\langle V\rangle = -\frac{\partial \ln \Delta}{\partial(\beta p)}.
$$

**Volume fluctuations**
$$
\mathrm{Var}(V) = \frac{\partial^{2} \ln \Delta}{\partial(\beta p)^{2}}.
$$

These relations connect volume fluctuations to mechanical response, providing a fluctuation–response expression for the isothermal compressibility (compare [[stat-mech/susceptibility-stat-mech|susceptibilities in statistical mechanics]]).

## Relation to other ensembles

The NPT normalization $\Delta$ is to the [[stat-mech/isothermal-isobaric-ensemble|NPT ensemble]] what $Z$ is to the [[stat-mech/canonical-ensemble|canonical ensemble]] and what $\Xi$ (see [[stat-mech/grand-partition-function|grand partition function]]) is to the [[stat-mech/grand-canonical-ensemble|grand-canonical ensemble]]: each partition function both normalizes the corresponding equilibrium measure and generates the appropriate thermodynamic potential via $-k_B T\ln(\cdot)$.
