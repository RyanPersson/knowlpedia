---
title: "Isothermal–isobaric partition function"
description: "Normalization of the NPT ensemble; Laplace transform of the canonical partition function and generator of the Gibbs free energy."
---


The **isothermal–isobaric partition function** $\Delta(\beta,p,N)$ is the normalization constant of the {{< knowl id="isothermal-isobaric-ensemble" text="isothermal–isobaric (NPT) ensemble" >}}, which describes equilibrium at fixed inverse temperature $\beta$, fixed pressure $p$, and fixed particle number $N$, with fluctuating volume.

It is naturally expressed in terms of the {{< knowl id="partition-function-canonical" text="canonical partition function" >}} $Z(\beta,V,N)$ by integrating over all volumes with the pressure weight:
$$
\Delta(\beta,p,N) = \int_{0}^{\infty} dV\; e^{-\beta pV}\, Z(\beta,V,N).
$$

Mathematically, $\Delta$ is a Laplace transform of $Z$ with respect to $V$.

## Physical meaning of the weight

In the NPT ensemble, microstates carry Boltzmann weight for the combination $H+pV$, where $H$ is the system {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}}. The factor $e^{-\beta pV}$ expresses mechanical equilibrium with a pressure reservoir: larger volumes are penalized by the work term $pV$ in the effective energy.

## Gibbs free energy from Δ

The partition function $\Delta$ generates the {{< knowl id="gibbs-free-energy" section="thermodynamics" text="Gibbs free energy" >}}:
$$
G(T,p,N) = -k_B T \ln \Delta(\beta,p,N),
$$

where $k_B$ is the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}} and $\beta = 1/(k_B T)$. This matches the thermodynamic fact that $G$ is the natural potential at fixed $(T,p,N)$, i.e. after Legendre transforming the {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} with respect to volume.

In the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, $G$ is extensive and one often uses $g = \lim_{N\to\infty} G/N$.

## Generating formulas for volume statistics

The logarithm of $\Delta$ generates equilibrium averages (see {{< knowl id="construction-observables-from-log-z" text="observables from log partition functions" >}}), in particular for the volume:

**Mean volume**
$$
\langle V\rangle = -\frac{\partial \ln \Delta}{\partial(\beta p)}.
$$

**Volume fluctuations**
$$
\mathrm{Var}(V) = \frac{\partial^{2} \ln \Delta}{\partial(\beta p)^{2}}.
$$

These relations connect volume fluctuations to mechanical response, providing a fluctuation–response expression for the isothermal compressibility (compare {{< knowl id="susceptibility-stat-mech" text="susceptibilities in statistical mechanics" >}}).

## Relation to other ensembles

The NPT normalization $\Delta$ is to the {{< knowl id="isothermal-isobaric-ensemble" text="NPT ensemble" >}} what $Z$ is to the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} and what $\Xi$ (see {{< knowl id="grand-partition-function" text="grand partition function" >}}) is to the {{< knowl id="grand-canonical-ensemble" text="grand-canonical ensemble" >}}: each partition function both normalizes the corresponding equilibrium measure and generates the appropriate thermodynamic potential via $-k_B T\ln(\cdot)$.
