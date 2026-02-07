---
title: "Isothermal–isobaric (NPT) ensemble"
description: "Equilibrium ensemble for fixed particle number, temperature, and pressure, with fluctuating volume."
---


The **isothermal–isobaric ensemble** (often called the **NPT ensemble**) describes a {{< knowl id="thermodynamic-system" section="thermodynamics" text="thermodynamic system" >}} in contact with reservoirs that fix the **temperature** (see {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}) and the **pressure** (see {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}}), while the **particle number** $N$ is held fixed. In this setting the **volume** $V$ is not fixed; it is a fluctuating quantity determined by mechanical equilibrium with the pressure reservoir.

Microscopically, one convenient classical description takes **microstates** (see {{< knowl id="microstate-classical" text="microstate" >}}) as a pair consisting of a point $x$ in {{< knowl id="phase-space-classical" text="phase space" >}} *and* a volume parameter $V>0$. The energy of a microstate is given by a {{< knowl id="hamiltonian-function-classical" text="Hamiltonian function" >}} $H(x;V)$, and integration over microstates uses the {{< knowl id="phase-space-volume-element" text="phase-space volume element" >}} at fixed $V$ together with an outer integration over $V$.

## Probability weight

Let $\beta$ denote the inverse temperature (see {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}}), with $\beta = 1/(k_B T)$ where $k_B$ is the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}}. In the NPT ensemble, the unnormalized weight of a microstate $(x,V)$ is proportional to
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

The normalization constant of the NPT distribution is the {{< knowl id="isothermal-isobaric-partition-function" text="isothermal–isobaric partition function" >}} $\Delta(\beta,p,N)$. It can be expressed as a Laplace transform of the {{< knowl id="partition-function-canonical" text="canonical partition function" >}} $Z(\beta,V,N)$:
$$
\Delta(\beta,p,N) = \int_{0}^{\infty} dV\, e^{-\beta pV}\, Z(\beta,V,N).
$$

In equilibrium statistical mechanics, $\Delta$ generates the {{< knowl id="gibbs-free-energy" section="thermodynamics" text="Gibbs free energy" >}} through
$$
G(T,p,N) = -k_B T \,\ln \Delta(\beta,p,N),
$$

up to conventions that become irrelevant in the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}. This matches the thermodynamic Legendre structure: NPT is the natural ensemble for $G$ (compare with the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} which is natural for the {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}).

## Averages and fluctuations

Ensemble averages are defined as in any {{< knowl id="ensemble-average" text="ensemble average" >}}: for an observable $A(x,V)$,
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

These relations are instances of general fluctuation–response identities (see {{< knowl id="construction-fluctuation-formulas-log-z" text="fluctuation formulas from log partition functions" >}}).
