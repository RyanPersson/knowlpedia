+++
id = "thermodynamics/prop-entropy-concavity-energy"
title = "Entropy is concave in energy (at fixed V,N)"
kind = "knowl"
summary = "For fixed volume and particle numbers, the thermodynamic entropy S(U,V,N) is concave as a function of internal energy U; equivalently, stable equilibrium implies nonnegative heat capacity at constant volume."
aliases = ["prop-entropy-concavity-energy", "Entropy is concave in energy (at fixed V,N)"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/prop-entropy-concavity-energy.md"
+++

## Statement
Let $S(U,V,N)$ denote the [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] of an equilibrium [[thermodynamics/thermodynamic-system|thermodynamic system]] as a function of [[thermodynamics/internal-energy-thermo|internal energy]] $U$, with $V,N$ held fixed. Under the usual stability/additivity assumptions of equilibrium thermodynamics, $S(\,\cdot\,,V,N)$ is concave:
for any $U_1,U_2$ and any $\lambda\in[0,1]$,
$$
S\!\big(\lambda U_1+(1-\lambda)U_2,\,V,\,N\big)\ \ge\ \lambda S(U_1,V,N)+(1-\lambda)S(U_2,V,N).
$$

If $S$ is twice differentiable in $U$, this is equivalent to
$$
\frac{\partial^2 S}{\partial U^2}(U,V,N)\le 0.
$$

## Key hypotheses
- Equilibrium description is valid (see [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]]).
- Additivity/weak coupling for composite systems and entropy maximization consistent with the [[thermodynamics/second-law-thermodynamics|second law]].
- Fixed $(V,N)$ throughout.

## Conclusions
- $S(U,V,N)$ is concave in $U$ at fixed $(V,N)$.
- If differentiable, $1/T = \partial S/\partial U$ with [[thermodynamics/temperature-thermo|temperature]] $T$; concavity implies $T$ is nondecreasing in $U$.
- In particular, the [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]] satisfies $C_V=(\partial U/\partial T)_{V,N}\ge 0$ (a standard facet of [[thermodynamics/thermodynamic-stability|thermodynamic stability]]).
