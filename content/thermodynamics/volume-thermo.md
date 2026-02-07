---
title: "Volume"
description: "An extensive size variable of a thermodynamic system, conjugate to pressure and central to compressive work."
---

## Definition and physical interpretation

The **volume** $V$ of a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} is an {{< knowl id="extensive-variable" text="extensive variable" >}} that measures the system’s spatial size and, in macroscopic equilibrium thermodynamics, serves as a state coordinate for “simple compressible” systems. Operationally, $V$ is determined by the system’s {{< knowl id="system-boundary" text="boundary" >}} (e.g., the container’s geometry for a fluid) and is well-defined when the macroscopic state is stationary and reproducible.

Volume is thermodynamically conjugate to {{< knowl id="pressure-thermo" text="pressure" >}}: changing $V$ against $p$ is the prototypical mechanical mode of energy exchange.

## Role in the fundamental differential and work

For a simple compressible system in {{< knowl id="thermodynamic-equilibrium" text="equilibrium" >}}, the fundamental differential in the energy representation $U=U(S,V,N)$ is
$$
dU = T\,dS - p\,dV + \mu\,dN.
$$

The appearance of $-p\,dV$ identifies $V$ as the coordinate whose quasistatic change produces pressure–volume work under the {{< knowl id="pressure-volume-work-sign-convention" text="standard sign convention" >}}.

Because {{< knowl id="work-inexact-differential" text="work is path-dependent" >}}, knowing only the initial and final volumes does not generally determine the mechanical work; it does so only under specified process conditions (e.g., quasistatic with a known $p(V)$ relation).

## Extensivity, additivity, and densities

For macroscopic matter with short-range interactions, volume is typically **additive** across weakly coupled subsystems (see {{< knowl id="additivity-postulate" text="additivity" >}}) and scales linearly under “copying” of the system (see the {{< knowl id="extensivity-postulate" text="extensivity postulate" >}}). These properties underlie the use of densities such as

- {{< knowl id="number-density" text="number density" >}} $n = N/V$,
- {{< knowl id="energy-density" text="energy density" >}} $u = U/V$,
- {{< knowl id="entropy-density" text="entropy density" >}} $s = S/V$.

When long-range forces or strong surface effects matter, $V$ can remain a useful geometric variable, but extensivity/additivity may fail or require careful thermodynamic-limit conventions (see {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}}).

## Relations to response functions and equations of state

Material behavior is encoded in an {{< knowl id="equation-of-state" text="equation of state" >}} relating $V$ to other state variables, e.g. $p=p(T,V,N)$ or $V=V(T,p,N)$. Two standard response coefficients that quantify how volume reacts to changes in intensive controls are:

- {{< knowl id="isothermal-compressibility" text="isothermal compressibility" >}}
  $$
  \kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_{T,N},
  $$
- {{< knowl id="thermal-expansion-coefficient" text="thermal expansion coefficient" >}}
  $$
  \alpha = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_{p,N}.
  $$

Stability and equilibrium constraints (see {{< knowl id="thermodynamic-stability" text="stability" >}}) restrict these derivatives; for example, $\kappa_T\ge 0$ is required for mechanical stability.
