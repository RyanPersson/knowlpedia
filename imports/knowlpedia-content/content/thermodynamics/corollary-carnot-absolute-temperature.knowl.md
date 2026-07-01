+++
id = "thermodynamics/corollary-carnot-absolute-temperature"
title = "Carnot theorem implies an absolute temperature scale"
kind = "knowl"
summary = "Carnot's theorem yields a temperature function with for reversible engines, defining absolute temperature up to units."
aliases = ["corollary-carnot-absolute-temperature", "Carnot theorem implies an absolute temperature scale"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/corollary-carnot-absolute-temperature.md"
+++

Consider a reversible heat engine operating between two reservoirs, “hot” and “cold,” with reservoir temperatures in the sense of [[thermodynamics/temperature-thermo|thermodynamic temperature]].

## Statement
Assume [[stat-mech/carnot-theorem|Carnot's theorem]]: all reversible engines between the same two reservoirs have the same efficiency, and no engine can exceed it.

Then there exists a positive temperature function $T$ (unique up to an overall multiplicative constant) such that for every reversible engine between the two reservoirs,
$$
\frac{Q_H}{Q_C}=\frac{T_H}{T_C},
$$

where $Q_H$ is the heat absorbed from the hot reservoir and $Q_C$ is the heat rejected to the cold reservoir (both taken as positive magnitudes).

Equivalently, the efficiency of a reversible (Carnot) engine is
$$
\eta_{\mathrm{rev}} = 1-\frac{T_C}{T_H},
$$
i.e. the [[stat-mech/carnot-efficiency-formula|Carnot efficiency formula]].

## Key hypotheses
- The reservoirs remain at fixed temperatures during each cycle.
- The engine cycle is reversible (no entropy production).
- Carnot's theorem holds (as a consequence of the [[thermodynamics/second-law-thermodynamics|second law]]).

## Key conclusions
- For reversible engines, the heat ratio $Q_H/Q_C$ depends only on the reservoir temperatures.
- This defines an **absolute temperature** scale (Kelvin scale) up to the choice of units.
