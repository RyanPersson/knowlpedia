---
title: "Kelvin–Planck statement"
description: "No cyclic heat engine can convert heat from a single thermal reservoir completely into work."
---


A heat engine is a device that executes a {{< knowl id="cyclic-process" text="cycle" >}} while exchanging heat with one or more {{< knowl id="thermal-reservoir" text="thermal reservoirs" >}} and exchanging work with a {{< knowl id="work-reservoir" text="work reservoir" >}}. The Kelvin–Planck statement of the {{< knowl id="second-law-thermodynamics" text="second law" >}} says:

> It is impossible to construct a device that operates in a cycle whose sole net effect is to absorb heat from a single thermal reservoir and deliver an equivalent amount of work.

Equivalently, no heat engine can have 100% efficiency when it interacts with only one reservoir; if net work is produced, some heat must be rejected to additional surroundings at a lower temperature.

## Physical interpretation

The statement rules out a “perpetual motion machine of the second kind”: energy conservation (the {{< knowl id="first-law-thermodynamics" text="first law" >}}) alone would allow a cyclic device with $\Delta U=0$ to turn all absorbed heat into work, but the second law forbids this complete conversion. A temperature difference is a necessary resource for extracting sustained work from heat.

## Key relations

- **Energy balance over a cycle.** For a cyclic engine, $\Delta U=0$, so net work output equals net heat absorbed. If the engine absorbs heat $Q_h>0$ from a hot reservoir and rejects heat $Q_c>0$ to a colder reservoir (here $Q_h,Q_c$ are magnitudes), then
  $$
  W_{\text{out}} = Q_h - Q_c,
  $$

  and Kelvin–Planck requires $Q_c>0$ whenever $W_{\text{out}}>0$.

- **Equivalent formulations.** Violating Kelvin–Planck would allow a cyclic device that, when combined appropriately, violates the {{< knowl id="clausius-statement-second-law" text="Clausius statement" >}} (moving heat from cold to hot with no work input), and vice versa. Both are captured quantitatively by the {{< knowl id="clausius-inequality" text="Clausius inequality" >}}.

- **Temperature dependence in the reversible limit.** For an ideal {{< knowl id="reversible-process" text="reversible" >}} engine operating between two reservoirs, the limiting performance depends only on their {{< knowl id="absolute-temperature-scale" text="absolute temperatures" >}}, reflecting that the second law ties work extraction to temperature differences rather than to detailed material properties.
