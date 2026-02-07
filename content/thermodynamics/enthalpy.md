---
title: "Enthalpy"
description: "A thermodynamic potential that is especially convenient for constant-pressure processes and flow systems."
---

## Definition and physical meaning

For a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} with {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$, {{< knowl id="pressure-thermo" text="pressure" >}} $p$, and {{< knowl id="volume-thermo" text="volume" >}} $V$, the **enthalpy** is the {{< knowl id="state-function" text="state function" >}}
$$
H \equiv U + pV.
$$

Physically, the $pV$ term accounts for the mechanical “flow work” needed to create space for the system in its {{< knowl id="surroundings-environment" text="surroundings" >}}. This makes $H$ a natural energy-like quantity for processes at approximately constant ambient pressure, and for {{< knowl id="open-system" text="open systems" >}} where material crosses a {{< knowl id="system-boundary" text="system boundary" >}}.

## Differential form and natural variables

Using the {{< knowl id="first-law-thermodynamics" text="first law of thermodynamics" >}} for a simple compressible system (only $p\,dV$ mechanical work and possible particle exchange), one obtains
$$
dH = T\,dS + V\,dp + \mu\,dN,
$$

where $S$ is the {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}}, $T$ the {{< knowl id="temperature-thermo" text="temperature" >}}, $N$ the {{< knowl id="particle-number" text="particle number" >}}, and $\mu$ the {{< knowl id="chemical-potential-thermo" text="chemical potential" >}}. (For mixtures, replace $\mu\,dN$ by $\sum_i \mu_i\,dN_i$.)

This shows that $H$ is naturally expressed as $H(S,p,N)$ (for a single-component simple compressible system), with
- $T = \left(\partial H/\partial S\right)_{p,N}$,
- $V = \left(\partial H/\partial p\right)_{S,N}$,
- $\mu = \left(\partial H/\partial N\right)_{S,p}$.

## Constant-pressure heating identity

With the {{< knowl id="pressure-volume-work-sign-convention" text="usual $p\,dV$ work sign convention" >}} (so that $dU = \delta Q - p\,dV + \mu\,dN$), the enthalpy change simplifies to
$$
dH = \delta Q + V\,dp + \mu\,dN.
$$

For a {{< knowl id="closed-system" text="closed system" >}} with fixed $N$ at constant pressure ($dp=0$), this reduces to
$$
\Delta H = Q_p,
$$
i.e. the heat absorbed at constant pressure equals the enthalpy change.

## Relation to Legendre transforms

If the system admits a {{< knowl id="fundamental-relation-energy" text="fundamental relation" >}} $U(S,V,N)$, then $H$ is obtained by a {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} that trades the extensive variable $V$ for its conjugate intensive variable $p$ (defined by $p = -(\partial U/\partial V)_{S,N}$).
