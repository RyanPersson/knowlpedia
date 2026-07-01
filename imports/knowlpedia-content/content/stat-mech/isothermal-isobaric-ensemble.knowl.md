+++
id = "stat-mech/isothermal-isobaric-ensemble"
title = "Isothermal–isobaric (NPT) ensemble"
kind = "knowl"
summary = "Equilibrium ensemble for fixed particle number, temperature, and pressure, with fluctuating volume."
aliases = ["isothermal-isobaric-ensemble", "Isothermal–isobaric (NPT) ensemble"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/isothermal-isobaric-ensemble.md"
+++

The **isothermal–isobaric ensemble** (often called the **NPT ensemble**) describes a [[thermodynamics/thermodynamic-system|thermodynamic system]] in contact with reservoirs that fix the **temperature** (see [[thermodynamics/temperature-thermo|temperature]]) and the **pressure** (see [[thermodynamics/pressure-thermo|pressure]]), while the **particle number** $N$ is held fixed. In this setting the **volume** $V$ is not fixed; it is a fluctuating quantity determined by mechanical equilibrium with the pressure reservoir.

Microscopically, one convenient classical description takes **microstates** (see [[stat-mech/microstate-classical|microstate]]) as a pair consisting of a point $x$ in [[stat-mech/phase-space-classical|phase space]] *and* a volume parameter $V>0$. The energy of a microstate is given by a [[stat-mech/hamiltonian-function-classical|Hamiltonian function]] $H(x;V)$, and integration over microstates uses the [[stat-mech/phase-space-volume-element|phase-space volume element]] at fixed $V$ together with an outer integration over $V$.

## Probability weight

Let $\beta$ denote the inverse temperature (see [[thermodynamics/inverse-temperature-beta|inverse temperature]]), with $\beta = 1/(k_B T)$ where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]]. In the NPT ensemble, the unnormalized weight of a microstate $(x,V)$ is proportional to
$$
\exp\!\big[-\beta\big(H(x;V) + pV\big)\big],
$$
so the probability density has the schematic form
$$
\mathbb{P}(dx\,dV) \propto e^{-\beta(H(x;V)+pV)}\,dx\,dV,
$$

where $dx$ denotes the phase-space measure at fixed $V$.

The combination $H+pV$ is the **enthalpy-like** quantity that plays the role of “effective energy” when pressure is imposed rather than volume.

## Normalization and thermodynamic potential

The normalization constant of the NPT distribution is the [[stat-mech/isothermal-isobaric-partition-function|isothermal–isobaric partition function]] $\Delta(\beta,p,N)$. It can be expressed as a Laplace transform of the [[stat-mech/partition-function-canonical|canonical partition function]] $Z(\beta,V,N)$:
$$
\Delta(\beta,p,N) = \int_{0}^{\infty} dV\, e^{-\beta pV}\, Z(\beta,V,N).
$$

In equilibrium statistical mechanics, $\Delta$ generates the [[thermodynamics/gibbs-free-energy|Gibbs free energy]] through
$$
G(T,p,N) = -k_B T \,\ln \Delta(\beta,p,N),
$$

up to conventions that become irrelevant in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]]. This matches the thermodynamic Legendre structure: NPT is the natural ensemble for $G$ (compare with the [[stat-mech/canonical-ensemble|canonical ensemble]] which is natural for the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]]).

## Averages and fluctuations

Ensemble averages are defined as in any [[stat-mech/ensemble-average|ensemble average]]: for an observable $A(x,V)$,
$$
\langle A\rangle_{NPT} = \frac{1}{\Delta(\beta,p,N)}\int_{0}^{\infty} dV \int dx\; A(x,V)\, e^{-\beta(H(x;V)+pV)}.
$$

Derivatives of $\ln\Delta$ generate moments of $V$:
$$
\langle V\rangle = -\frac{\partial \ln \Delta}{\partial(\beta p)},
\qquad
\mathrm{Var}(V) = \frac{\partial^{2} \ln \Delta}{\partial(\beta p)^{2}}.
$$
In particular, the isothermal compressibility can be read from volume fluctuations:
$$
\kappa_T
= -\frac{1}{\langle V\rangle}\left(\frac{\partial \langle V\rangle}{\partial p}\right)_T
= \frac{\beta\,\mathrm{Var}(V)}{\langle V\rangle}.
$$

These relations are instances of general fluctuation–response identities (see [[stat-mech/construction-fluctuation-formulas-log-z|fluctuation formulas from log partition functions]]).
