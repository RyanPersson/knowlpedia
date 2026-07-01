+++
id = "thermodynamics/prop-free-energy-convexity-temperature"
title = "Concavity of Helmholtz free energy in temperature"
kind = "knowl"
summary = "At fixed volume and composition, the Helmholtz free energy has nonpositive second derivative in temperature, with curvature controlled by ."
aliases = ["prop-free-energy-convexity-temperature", "Concavity of Helmholtz free energy in temperature"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/prop-free-energy-convexity-temperature.md"
+++

## Statement

Let $F(T,V,N)$ be the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] of a stable equilibrium system. At fixed $V,N$ and for $T>0$,
$$
\left(\frac{\partial^2 F}{\partial T^2}\right)_{V,N}
={}
-\frac{C_V}{T}
\le 0,
$$

where $C_V$ is the [[thermodynamics/heat-capacity-constant-volume|constant-volume heat capacity]].

Equivalently, $T\mapsto F(T,V,N)$ is concave (and $T\mapsto -F(T,V,N)$ is convex).

## Key hypotheses

- Equilibrium thermodynamics applies (see [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]]).
- $F$ is twice differentiable in $T$ at fixed $V,N$.
- Thermodynamic stability, in particular $C_V\ge 0$ (see [[thermodynamics/thermodynamic-stability|thermodynamic stability]] and [[thermodynamics/heat-capacity-constant-volume|$C_V$]]).
- Temperature $T>0$ (see [[thermodynamics/temperature-thermo|temperature]]).

## Key conclusions

- Curvature identity:
  $$
  \left(\frac{\partial^2 F}{\partial T^2}\right)_{V,N} \le 0.
  $$

- Since $S = -(\partial F/\partial T)_{V,N}$, it follows that
  $$
  \left(\frac{\partial S}{\partial T}\right)_{V,N} = \frac{C_V}{T} \ge 0,
  $$

  so entropy is nondecreasing with temperature at fixed $V,N$.
- The concavity implies a tangent-line bound: for any $T_0$,
  $$
  F(T,V,N) \le F(T_0,V,N) + \left(\frac{\partial F}{\partial T}\right)_{V,N}\Big|_{T_0}\,(T-T_0),
  $$

  i.e. $F$ lies below its tangent lines as a function of $T$ (at fixed $V,N$).

## Cross-links to definitions

- [[thermodynamics/helmholtz-free-energy|Helmholtz free energy $F$]]
- [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume $C_V$]]
- [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/thermodynamic-entropy|entropy]]
- [[thermodynamics/thermodynamic-stability|thermodynamic stability]]
