+++
id = "thermodynamics/thermal-expansion-coefficient"
title = "Thermal expansion coefficient"
kind = "knowl"
summary = "A response function measuring the fractional change of volume with temperature at fixed pressure (and composition)."
aliases = ["thermal-expansion-coefficient", "Thermal expansion coefficient"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermal-expansion-coefficient.md"
+++

The **thermal expansion coefficient** (more precisely, the **isobaric volumetric expansion coefficient**) is a [[thermodynamics/response-function-thermo|response function]]
that quantifies how a system’s [[thermodynamics/volume-thermo|volume]] changes with [[thermodynamics/temperature-thermo|temperature]] when the [[thermodynamics/pressure-thermo|pressure]] is held fixed.

For fixed composition (e.g. fixed [[thermodynamics/particle-number|particle number]] $N$),
$$
\alpha \equiv \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_{p,N}.
$$

## Physical interpretation
For a small quasistatic change at fixed pressure, the definition implies
$$
\frac{dV}{V} = \alpha\,dT.
$$

So $\alpha$ is the **fractional volume increase per unit temperature increase** at constant pressure. Most materials have $\alpha>0$ in ordinary ranges, but $\alpha$ can be negative in anomalous regimes (thermal contraction upon heating).

In terms of the [[thermodynamics/number-density|number density]] $n=N/V$ at fixed $N$, the same physics can be expressed as
$$
\alpha = -\frac{1}{n}\left(\frac{\partial n}{\partial T}\right)_{p,N}.
$$

## Key relations and properties
- **From an equation of state:** If an [[thermodynamics/equation-of-state|equation of state]] is given as $p=p(T,V,N)$, then holding $p$ fixed and differentiating implicitly yields
  $$
  \alpha
  = -\frac{1}{V}\,
    \frac{\left(\frac{\partial p}{\partial T}\right)_{V,N}}
         {\left(\frac{\partial p}{\partial V}\right)_{T,N}}
  = \kappa_T\left(\frac{\partial p}{\partial T}\right)_{V,N},
  $$

  where $\kappa_T$ is the [[thermodynamics/isothermal-compressibility|isothermal compressibility]].

- **Maxwell relation form:** Using the [[thermodynamics/gibbs-free-energy|Gibbs free energy]] differential and the [[thermodynamics/maxwell-relation|Maxwell relations]], one obtains
  $$
  \left(\frac{\partial V}{\partial T}\right)_{p,N}
  = -\left(\frac{\partial S}{\partial p}\right)_{T,N},
  $$
  hence
  $$
  \alpha = -\frac{1}{V}\left(\frac{\partial S}{\partial p}\right)_{T,N}.
  $$

- **Links to heat capacities and compressibilities:** For a simple compressible system,
  $$
  C_P - C_V = \frac{T\,V\,\alpha^2}{\kappa_T},
  $$

  connecting $\alpha$ with the [[thermodynamics/heat-capacity-constant-pressure|constant-pressure heat capacity]] $C_P$, the [[thermodynamics/heat-capacity-constant-volume|constant-volume heat capacity]] $C_V$, and $\kappa_T$.

  The difference between [[thermodynamics/isothermal-compressibility|isothermal]] and [[thermodynamics/adiabatic-compressibility|adiabatic]] compressibilities can likewise be written as
  $$
  \kappa_T - \kappa_S = \frac{T\,V\,\alpha^2}{C_P}.
  $$

- **Stability consistency:** In stable single-phase equilibrium, the identities above are consistent with $C_P \ge C_V$ and $\kappa_T \ge \kappa_S$, reflecting [[thermodynamics/thermodynamic-stability|thermodynamic stability]].
