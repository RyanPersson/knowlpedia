---
title: "First law of thermodynamics"
description: "Energy conservation in thermodynamics: the change in internal energy equals heat added plus work done on the system (with specified sign conventions)."
---

The **first law of thermodynamics** is the statement of **energy conservation** for a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}}. It postulates the existence of a state function—{{< knowl id="internal-energy-thermo" text="internal energy" >}}—whose change accounts for energy transferred via heat and work during a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}}.

**Definition (closed system form).** For a {{< knowl id="closed-system" text="closed system" >}} undergoing any process between equilibrium states,
$$
\Delta U = Q + W,
$$

where $Q$ is the net energy transferred as {{< knowl id="heat-inexact-differential" text="heat" >}} and $W$ is the net energy transferred as {{< knowl id="work-inexact-differential" text="work" >}}. In differential form this is written
$$
dU = \delta Q + \delta W.
$$

The precise sign of $W$ depends on the chosen {{< knowl id="work-sign-convention" text="work sign convention" >}}; likewise, how pressure–volume contributions are recorded is fixed by the {{< knowl id="pressure-volume-work-sign-convention" text="pressure–volume work convention" >}}.

**Physical interpretation.** The system’s microscopic energy content can change only by exchanging energy with the {{< knowl id="surroundings-environment" text="surroundings" >}}. The first law does not say *how* that energy exchange must occur; it only asserts that all exchanges add up consistently into a conserved accounting.

**Heat and work are path-dependent.** While $U$ is a {{< knowl id="state-function" text="state function" >}} (so $\Delta U$ depends only on the endpoints), $Q$ and $W$ are {{< knowl id="path-function" text="path functions" >}}: their values depend on the details of the process. This is why one writes $\delta Q$ and $\delta W$ rather than exact differentials.

**Useful consequences and special cases.**
- **Cyclic processes.** For a {{< knowl id="cyclic-process" text="cyclic process" >}}, $\Delta U=0$, hence the net heat and work balance:
  $$
  \oint \delta Q + \oint \delta W = 0.
  $$
- **Mechanical work example.** In a quasistatic compression/expansion, work is often dominated by pressure–volume exchange involving {{< knowl id="pressure-thermo" text="pressure" >}} and {{< knowl id="volume-thermo" text="volume" >}}; the sign and exact form follow the adopted conventions referenced above.
- **Particle exchange.** For an {{< knowl id="open-system" text="open system" >}} where {{< knowl id="particle-number" text="particles" >}} cross the {{< knowl id="system-boundary" text="system boundary" >}}, energy can also be transported with matter. In equilibrium thermodynamics this contribution is commonly organized using the {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} and a {{< knowl id="chemical-work-convention" text="chemical work convention" >}}; a common bookkeeping form is
  $$
  dU = \delta Q + \delta W + \mu\, dN,
  $$
  with the understanding that what is counted as “work-like” versus “heat-like” depends on the chosen convention and description.

Together with the {{< knowl id="second-law-thermodynamics" text="second law" >}}, the first law anchors the structure of equilibrium thermodynamics by linking measurable transfers ($Q,W$) to changes in a state property ($U$).
