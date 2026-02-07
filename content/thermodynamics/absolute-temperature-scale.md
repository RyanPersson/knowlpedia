---
title: "Absolute temperature scale"
description: "A temperature scale defined (up to an overall constant) by reversible heat-engine performance; realized as the Kelvin scale."
---

## Definition and physical interpretation

An **absolute temperature scale** assigns to each {{< knowl id="thermodynamic-equilibrium" text="equilibrium" >}} state a positive number $T>0$ such that for any two {{< knowl id="thermal-reservoir" text="thermal reservoirs" >}} at temperatures $T_H$ and $T_C$, a {{< knowl id="reversible-process" text="reversible" >}} engine operating between them satisfies the Carnot relation
$$
\frac{Q_H}{Q_C}=\frac{T_H}{T_C},
$$

where $Q_H$ is the heat absorbed from the hot reservoir and $Q_C$ is the heat delivered to the cold reservoir (both taken as positive magnitudes). This characterization is a consequence of the {{< knowl id="second-law-thermodynamics" text="second law" >}} and the existence of reversible cycles.

Physically, the scale is “absolute” because it does not depend on the properties of any particular substance (unlike a gas thermometer calibration); instead, it is tied to universal constraints on cyclic energy conversion. The notion of “same temperature” is operationally captured by {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}} and formalized by the {{< knowl id="zeroth-law-thermodynamics" text="zeroth law" >}}, while the **numerical** scale is fixed by the second law.

## Entropy-based characterization

For a simple compressible system described by a {{< knowl id="fundamental-relation-entropy" text="fundamental relation" >}} $S=S(U,V,N)$, the absolute temperature can be defined intrinsically by
$$
\frac{1}{T}=\left(\frac{\partial S}{\partial U}\right)_{V,N}.
$$

Equivalently, if one uses the energy representation $U=U(S,V,N)$ (see {{< knowl id="fundamental-relation-energy" text="energy fundamental relation" >}}), then
$$
T=\left(\frac{\partial U}{\partial S}\right)_{V,N}.
$$

This makes explicit that $T$ is the variable thermodynamically conjugate to {{< knowl id="thermodynamic-entropy" text="entropy" >}}.

## Key properties and conventions

- **Scale uniqueness:** The Carnot characterization fixes temperature only up to a **multiplicative constant**. Choosing units (Kelvin) fixes that constant; in statistical mechanics this choice is often packaged into the value of the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}} $k_B$.

- **Inverse temperature:** It is common to use the {{< knowl id="inverse-temperature-beta" text="inverse temperature" >}} $\beta=1/(k_B T)$, especially under the {{< knowl id="canonical-ensemble-convention" text="canonical ensemble convention" >}}.

- **Absolute zero:** The scale has a natural lower bound at $T=0$ (“absolute zero”), tied to unattainability statements of the {{< knowl id="third-law-thermodynamics" text="third law" >}}. The operational meaning is subtle: $T=0$ is a limiting concept rather than an ordinary equilibrium point.

- **Natural units:** In some conventions (see {{< knowl id="natural-units-convention" text="natural units" >}}), one sets $k_B=1$, so temperature has the same units as energy and $\beta=1/T`.
