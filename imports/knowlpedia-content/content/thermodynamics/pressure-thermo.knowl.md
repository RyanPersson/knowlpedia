+++
id = "thermodynamics/pressure-thermo"
title = "Pressure"
kind = "knowl"
summary = "The intensive mechanical variable conjugate to volume, governing compressive work and encoded in the equation of state."
aliases = ["pressure-thermo", "Pressure"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/pressure-thermo.md"
+++

## Definition and physical interpretation

In thermodynamics, **pressure** $p$ is an [[thermodynamics/intensive-variable|intensive variable]] that characterizes the system’s mechanical tendency to expand or contract against its [[thermodynamics/system-boundary|boundary]]. For a uniform isotropic fluid in [[thermodynamics/mechanical-equilibrium|mechanical equilibrium]], it coincides with the familiar force-per-area on a surface element, averaged over microscopic fluctuations.

Thermodynamically, pressure is defined as the variable conjugate to [[thermodynamics/volume-thermo|volume]] in the energy balance for a simple compressible system.

## Thermodynamic definition via fundamental differentials

For a single-component simple compressible system with state described by $(S,V,N)$, the differential form of the fundamental relation (see [[thermodynamics/internal-energy-thermo|internal energy]] and the [[thermodynamics/first-law-thermodynamics|first law]]) is
$$
dU = T\,dS - p\,dV + \mu\,dN.
$$

Here $p$ is defined by the partial derivative
$$
p = -\left(\frac{\partial U}{\partial V}\right)_{S,N}.
$$

Equivalently, in the entropy representation $S=S(U,V,N)$,
$$
\frac{p}{T}=\left(\frac{\partial S}{\partial V}\right)_{U,N}.
$$
These definitions make sense at [[thermodynamics/thermodynamic-equilibrium|equilibrium]]; away from equilibrium, “pressure” may require additional structure (e.g., stress tensors) and may not be a single state variable.

## Work and sign conventions

For a quasistatic compression/expansion, the mechanical work contribution is
$$
\delta W = -p\,dV
$$

under the standard [[thermodynamics/pressure-volume-work-sign-convention|pressure–volume work sign convention]] (consistent with the general [[thermodynamics/work-sign-convention|work sign convention]] and the fact that [[thermodynamics/work-inexact-differential|work is path-dependent]]). With this choice, expansion ($dV>0$) corresponds to work done **by** the system, so $\delta W<0$.

## Relations to free energies and response functions

Pressure can be expressed as a derivative of thermodynamic potentials obtained by a [[convex-analysis/legendre-transform|Legendre transform]]:

- From the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F(T,V,N)=U-TS$,
  $$
  p = -\left(\frac{\partial F}{\partial V}\right)_{T,N}.
  $$

- From the [[thermodynamics/gibbs-free-energy|Gibbs free energy]] $G(T,p,N)=U-TS+pV$,
  $$
  V = \left(\frac{\partial G}{\partial p}\right)_{T,N}.
  $$

A key linear response quantity controlled by pressure is the [[thermodynamics/isothermal-compressibility|isothermal compressibility]]
$$
\kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_{T,N},
$$

which must satisfy $\kappa_T\ge 0$ for [[thermodynamics/thermodynamic-stability|thermodynamic stability]].

Finally, pressure is tied to the [[thermodynamics/equation-of-state|equation of state]] $p=p(T,V,N)$ (or equivalent forms), which encodes material-specific information beyond the general structure of the laws.
