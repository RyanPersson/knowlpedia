+++
id = "thermodynamics/enthalpy"
title = "Enthalpy"
kind = "knowl"
summary = "A thermodynamic potential that is especially convenient for constant-pressure processes and flow systems."
aliases = ["enthalpy"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/enthalpy.md"
+++

## Definition and physical meaning

For a [[thermodynamics/thermodynamic-system|thermodynamic system]] with [[thermodynamics/internal-energy-thermo|internal energy]] $U$, [[thermodynamics/pressure-thermo|pressure]] $p$, and [[thermodynamics/volume-thermo|volume]] $V$, the **enthalpy** is the [[thermodynamics/state-function|state function]]
$$
H \equiv U + pV.
$$

Physically, the $pV$ term accounts for the mechanical “flow work” needed to create space for the system in its [[thermodynamics/surroundings-environment|surroundings]]. This makes $H$ a natural energy-like quantity for processes at approximately constant ambient pressure, and for [[thermodynamics/open-system|open systems]] where material crosses a [[thermodynamics/system-boundary|system boundary]].

## Differential form and natural variables

Using the [[thermodynamics/first-law-thermodynamics|first law of thermodynamics]] for a simple compressible system (only $p\,dV$ mechanical work and possible particle exchange), one obtains
$$
dH = T\,dS + V\,dp + \mu\,dN,
$$

where $S$ is the [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]], $T$ the [[thermodynamics/temperature-thermo|temperature]], $N$ the [[thermodynamics/particle-number|particle number]], and $\mu$ the [[thermodynamics/chemical-potential-thermo|chemical potential]]. (For mixtures, replace $\mu\,dN$ by $\sum_i \mu_i\,dN_i$.)

This shows that $H$ is naturally expressed as $H(S,p,N)$ (for a single-component simple compressible system), with
- $T = \left(\partial H/\partial S\right)_{p,N}$,
- $V = \left(\partial H/\partial p\right)_{S,N}$,
- $\mu = \left(\partial H/\partial N\right)_{S,p}$.

## Constant-pressure heating identity

With the [[thermodynamics/pressure-volume-work-sign-convention|usual $p\,dV$ work sign convention]] (so that $dU = \delta Q - p\,dV + \mu\,dN$), the enthalpy change simplifies to
$$
dH = \delta Q + V\,dp + \mu\,dN.
$$

For a [[thermodynamics/closed-system|closed system]] with fixed $N$ at constant pressure ($dp=0$), this reduces to
$$
\Delta H = Q_p,
$$
i.e. the heat absorbed at constant pressure equals the enthalpy change.

## Relation to Legendre transforms

If the system admits a [[thermodynamics/fundamental-relation-energy|fundamental relation]] $U(S,V,N)$, then $H$ is obtained by a [[convex-analysis/legendre-transform|Legendre transform]] that trades the extensive variable $V$ for its conjugate intensive variable $p$ (defined by $p = -(\partial U/\partial V)_{S,N}$).
