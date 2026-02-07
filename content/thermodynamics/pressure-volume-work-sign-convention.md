---
title: "Pressure–volume work sign convention"
description: "Fixes the sign of work and how it appears in the first law."
---

## Definition and physical meaning

In this blog we adopt the {{< knowl id="work-sign-convention" text="thermodynamic work sign convention" >}} in which $\delta W>0$ denotes **work done by the system on the surroundings**. For the mechanical work associated with motion of a {{< knowl id="system-boundary" text="system boundary" >}} under an external pressure, the **pressure–volume work** is defined by
- **Pressure–volume work (by the system):** $\delta W_{PV} := P_{\mathrm{ext}}\, dV$.

Here $V$ is the {{< knowl id="volume-thermo" text="system volume" >}} and $P_{\mathrm{ext}}$ is the pressure exerted by the {{< knowl id="surroundings-environment" text="surroundings" >}} on the boundary. Physically:
- if the system **expands** ($dV>0$), it pushes back the surroundings and does **positive** work, $\delta W_{PV}>0$;
- if the system is **compressed** ($dV<0$), the surroundings do work on the system and $\delta W_{PV}<0$.

Because work depends on the path, $\delta W_{PV}$ is an instance of {{< knowl id="work-inexact-differential" text="inexact work" >}} rather than a {{< knowl id="state-function" text="state function" >}}.

## Appearance in the first law

With the {{< knowl id="first-law-thermodynamics" text="first law" >}} written as
$dU = \delta Q - \delta W$,
the $P\,dV$ contribution implies (when pressure–volume work is the only mechanical work)
$$
dU = \delta Q - P_{\mathrm{ext}}\, dV.
$$

For a {{< knowl id="quasistatic-process" text="quasistatic" >}} and {{< knowl id="reversible-process" text="reversible" >}} process, $P_{\mathrm{ext}}$ equals the system {{< knowl id="pressure-thermo" text="pressure" >}} $P$, so one may write $dU=\delta Q-P\,dV$.

## Key relations and diagnostics

- **Closed-cycle work:** over a {{< knowl id="cyclic-process" text="cycle" >}},
  $$
  W_{PV} = \oint P_{\mathrm{ext}}\, dV,
  $$

  which geometrically is the signed area enclosed in the $P$–$V$ plane (positive for the usual clockwise “engine” cycle under this convention).

- **Connection to enthalpy:** using {{< knowl id="enthalpy" text="enthalpy" >}} $H=U+PV$ and $dU=\delta Q-P\,dV$ (reversible, $PV$-only),
  $$
  dH = \delta Q + V\, dP.
  $$

  In particular, at constant pressure ($dP=0$) one gets $dH=\delta Q$, which underlies the interpretation of heat at constant pressure.

- **Translation to the opposite convention:** some texts define work as **done on** the system, writing $dU=\delta Q+\delta W^{(\mathrm{on})}$. In that convention the same physics is represented by $\delta W^{(\mathrm{on})}_{PV}=-P_{\mathrm{ext}}\, dV$.
