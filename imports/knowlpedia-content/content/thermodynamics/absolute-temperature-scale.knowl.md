+++
id = "thermodynamics/absolute-temperature-scale"
title = "Absolute temperature scale"
kind = "knowl"
summary = "A temperature scale defined (up to an overall constant) by reversible heat-engine performance; realized as the Kelvin scale."
aliases = ["absolute-temperature-scale", "Absolute temperature scale"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/absolute-temperature-scale.md"
+++

## Definition and physical interpretation

An **absolute temperature scale** assigns to each [[thermodynamics/thermodynamic-equilibrium|equilibrium]] state a positive number $T>0$ such that for any two [[thermodynamics/thermal-reservoir|thermal reservoirs]] at temperatures $T_H$ and $T_C$, a [[thermodynamics/reversible-process|reversible]] engine operating between them satisfies the Carnot relation
$$
\frac{Q_H}{Q_C}=\frac{T_H}{T_C},
$$

where $Q_H$ is the heat absorbed from the hot reservoir and $Q_C$ is the heat delivered to the cold reservoir (both taken as positive magnitudes). This characterization is a consequence of the [[thermodynamics/second-law-thermodynamics|second law]] and the existence of reversible cycles.

Physically, the scale is “absolute” because it does not depend on the properties of any particular substance (unlike a gas thermometer calibration); instead, it is tied to universal constraints on cyclic energy conversion. The notion of “same temperature” is operationally captured by [[thermodynamics/thermal-equilibrium|thermal equilibrium]] and formalized by the [[thermodynamics/zeroth-law-thermodynamics|zeroth law]], while the **numerical** scale is fixed by the second law.

## Entropy-based characterization

For a simple compressible system described by a [[thermodynamics/fundamental-relation-entropy|fundamental relation]] $S=S(U,V,N)$, the absolute temperature can be defined intrinsically by
$$
\frac{1}{T}=\left(\frac{\partial S}{\partial U}\right)_{V,N}.
$$

Equivalently, if one uses the energy representation $U=U(S,V,N)$ (see [[thermodynamics/fundamental-relation-energy|energy fundamental relation]]), then
$$
T=\left(\frac{\partial U}{\partial S}\right)_{V,N}.
$$

This makes explicit that $T$ is the variable thermodynamically conjugate to [[thermodynamics/thermodynamic-entropy|entropy]].

## Key properties and conventions

- **Scale uniqueness:** The Carnot characterization fixes temperature only up to a **multiplicative constant**. Choosing units (Kelvin) fixes that constant; in statistical mechanics this choice is often packaged into the value of the [[thermodynamics/boltzmann-constant|Boltzmann constant]] $k_B$.

- **Inverse temperature:** It is common to use the [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta=1/(k_B T)$, especially under the [[thermodynamics/canonical-ensemble-convention|canonical ensemble convention]].

- **Absolute zero:** The scale has a natural lower bound at $T=0$ (“absolute zero”), tied to unattainability statements of the [[thermodynamics/third-law-thermodynamics|third law]]. The operational meaning is subtle: $T=0$ is a limiting concept rather than an ordinary equilibrium point.

- **Natural units:** In some conventions (see [[thermodynamics/natural-units-convention|natural units]]), one sets $k_B=1$, so temperature has the same units as energy and $\beta=1/T`.
