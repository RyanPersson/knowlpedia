---
title: "Thermal reservoir"
description: "An idealized heat bath that can exchange heat while remaining at (essentially) fixed temperature."
---

A **thermal reservoir** (or *heat bath*) is an idealized part of the {{< knowl id="surroundings-environment" text="surroundings" >}} that can exchange energy with a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} **as heat** while maintaining an (effectively) constant {{< knowl id="temperature-thermo" text="temperature" >}} $T_R$. Operationally, it is a macroscopic body with such a large heat capacity (and fast internal relaxation) that exchanging a finite amount of heat produces a negligible change in its temperature, so it stays in (approximate) internal {{< knowl id="thermodynamic-equilibrium" text="equilibrium" >}} at all times.

Physically, a thermal reservoir models a very large environment (e.g., a large water bath, a laboratory “thermostat,” or an effectively infinite environment) that fixes temperature via the {{< knowl id="zeroth-law-thermodynamics" text="zeroth law" >}}: when the system is placed in contact with the reservoir through a {{< knowl id="diathermal-wall" text="diathermal wall" >}}, it can relax toward {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}} with $T = T_R$ (provided other constraints don’t prevent equilibration).

A reservoir is typically assumed to exchange *only heat* with the system (no matter transfer, and no controlled work transfer). If the coupling allows energy transfer as heat, the transferred amount is described by the {{< knowl id="heat-inexact-differential" text="inexact differential of heat" >}} $\delta Q$.

**Key relations (constant-$T_R$ idealization).**  
Let $Q$ denote the net heat absorbed by the system from the reservoir over some interaction. Under the reservoir idealization, the reservoir’s entropy change is
$$
\Delta S_R = -\frac{Q}{T_R},
$$

because the reservoir remains at temperature $T_R$ while its energy decreases by $Q$.

Combined with the {{< knowl id="second-law-thermodynamics" text="second law" >}}, this yields a standard “system + reservoir” entropy balance:
$$
\Delta S_{\text{total}} = \Delta S_{\text{system}} + \Delta S_R
= \Delta S_{\text{system}} - \frac{Q}{T_R} \ge 0,
$$

with equality in the reversible limit (see {{< knowl id="clausius-inequality" text="Clausius inequality" >}} and {{< knowl id="reversible-process" text="reversible process" >}}). This is one of the main practical reasons thermal reservoirs are useful: they convert the second law into a concrete inequality involving $Q$ and $T_R$.

In statistical mechanics language, a thermal reservoir is what underlies the canonical description: the reservoir fixes the system’s temperature, equivalently fixing the {{< knowl id="inverse-temperature-beta" text="inverse temperature" >}} $\beta = 1/(k_B T_R)$ with {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}} $k_B$ (see {{< knowl id="canonical-ensemble-convention" text="canonical ensemble conventions" >}}).

Contrast: a {{< knowl id="work-reservoir" text="work reservoir" >}} idealizes controlled exchange of work rather than heat.
