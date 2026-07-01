+++
id = "thermodynamics/euler-relation-thermodynamics"
title = "Euler Relation in Thermodynamics"
kind = "knowl"
summary = "For an extensive system, Euler’s theorem gives an algebraic relation linking energy to its conjugate intensive variables."
aliases = ["euler-relation-thermodynamics", "Euler Relation in Thermodynamics"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/euler-relation-thermodynamics.md"
+++

## Definition and physical interpretation

Consider a single-phase [[thermodynamics/thermodynamic-system|thermodynamic system]] whose equilibrium states admit a [[thermodynamics/fundamental-relation-energy|fundamental relation in the energy representation]] of the form $U=U(S,V,N)$, with $(S,V,N)$ being [[thermodynamics/extensive-variable|extensive variables]].

If $U(S,V,N)$ is [[thermodynamics/homogeneous-function-degree-one|homogeneous of degree one]] (i.e. extensive, as assumed in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]] with negligible boundary contributions), then Euler’s theorem implies the **Euler relation**
$$
U = T S - P V + \mu N .
$$

Here $T$, $P$, and $\mu$ are the conjugate [[thermodynamics/intensive-variable|intensive variables]]: the [[thermodynamics/temperature-thermo|temperature]] $T$, [[thermodynamics/pressure-thermo|pressure]] $P$, and [[thermodynamics/chemical-potential-thermo|chemical potential]] $\mu$, while $S$ is the [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]], $V$ the [[thermodynamics/volume-thermo|volume]], and $N$ the [[thermodynamics/particle-number|particle number]].

Physically, the relation says that for an extensive system the internal energy is a sum of “intensive $\times$ extensive” contributions. The sign of the mechanical term matches the chosen [[thermodynamics/pressure-volume-work-sign-convention|pressure–volume work sign convention]] (and the chemical term matches the [[thermodynamics/chemical-work-convention|chemical work convention]]).

An equivalent form in the entropy representation $S=S(U,V,N)$ is
$$
S = \frac{1}{T}U + \frac{P}{T}V - \frac{\mu}{T}N .
$$

## Key consequences

- Combining the Euler relation with the definitions of common [[thermodynamics/state-function|state functions]] gives useful identities, e.g. using the definitions of [[thermodynamics/enthalpy|enthalpy]], [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]], and [[thermodynamics/gibbs-free-energy|Gibbs free energy]]:
  $$
  H=U+PV=TS+\mu N,\qquad
  F=U-TS=-PV+\mu N,\qquad
  G=U-TS+PV=\mu N.
  $$

- Differentiating the Euler relation and comparing with the exact differential from the [[thermodynamics/first-law-thermodynamics|first law]],
  $$
  dU = T\,dS - P\,dV + \mu\,dN,
  $$
  yields the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]], which constrains the intensive variables.
