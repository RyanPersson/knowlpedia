---
title: "Euler Relation in Thermodynamics"
description: "For an extensive system, Euler’s theorem gives an algebraic relation linking energy to its conjugate intensive variables."
---

## Definition and physical interpretation

Consider a single-phase {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} whose equilibrium states admit a {{< knowl id="fundamental-relation-energy" text="fundamental relation in the energy representation" >}} of the form $U=U(S,V,N)$, with $(S,V,N)$ being {{< knowl id="extensive-variable" text="extensive variables" >}}.

If $U(S,V,N)$ is {{< knowl id="homogeneous-function-degree-one" text="homogeneous of degree one" >}} (i.e. extensive, as assumed in the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}} with negligible boundary contributions), then Euler’s theorem implies the **Euler relation**
$$
U = T S - P V + \mu N .
$$

Here $T$, $P$, and $\mu$ are the conjugate {{< knowl id="intensive-variable" text="intensive variables" >}}: the {{< knowl id="temperature-thermo" text="temperature" >}} $T$, {{< knowl id="pressure-thermo" text="pressure" >}} $P$, and {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} $\mu$, while $S$ is the {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}}, $V$ the {{< knowl id="volume-thermo" text="volume" >}}, and $N$ the {{< knowl id="particle-number" text="particle number" >}}.

Physically, the relation says that for an extensive system the internal energy is a sum of “intensive $\times$ extensive” contributions. The sign of the mechanical term matches the chosen {{< knowl id="pressure-volume-work-sign-convention" text="pressure–volume work sign convention" >}} (and the chemical term matches the {{< knowl id="chemical-work-convention" text="chemical work convention" >}}).

An equivalent form in the entropy representation $S=S(U,V,N)$ is
$$
S = \frac{1}{T}U + \frac{P}{T}V - \frac{\mu}{T}N .
$$

## Key consequences

- Combining the Euler relation with the definitions of common {{< knowl id="state-function" text="state functions" >}} gives useful identities, e.g. using the definitions of {{< knowl id="enthalpy" text="enthalpy" >}}, {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}}, and {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}}:
  $$
  H=U+PV=TS+\mu N,\qquad
  F=U-TS=-PV+\mu N,\qquad
  G=U-TS+PV=\mu N.
  $$

- Differentiating the Euler relation and comparing with the exact differential from the {{< knowl id="first-law-thermodynamics" text="first law" >}},
  $$
  dU = T\,dS - P\,dV + \mu\,dN,
  $$
  yields the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}}, which constrains the intensive variables.
