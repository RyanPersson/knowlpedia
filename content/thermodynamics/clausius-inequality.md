---
title: "Clausius inequality"
description: "Integral inequality for heat exchange that quantifies irreversibility and leads to the definition of entropy."
---


Consider a {{< knowl id="cyclic-process" text="cyclic process" >}} in which a system exchanges heat $\delta Q$ with its surroundings (see {{< knowl id="heat-inexact-differential" text="heat" >}}). Let $T_{\mathrm{b}}$ denote the {{< knowl id="temperature-thermo" text="boundary temperature" >}} at which each heat element crosses the system boundary (e.g., the temperature of a {{< knowl id="thermal-reservoir" text="thermal reservoir" >}} supplying that heat), understood on the {{< knowl id="absolute-temperature-scale" text="absolute temperature scale" >}}. The Clausius inequality states that
$$
\oint \frac{\delta Q}{T_{\mathrm{b}}}\le 0.
$$
Equality holds if and only if the cycle is {{< knowl id="reversible-process" text="reversible" >}}; strict inequality indicates a genuinely {{< knowl id="irreversible-process" text="irreversible" >}} cycle.

A useful special case is a cycle exchanging finite heats $Q_i$ with reservoirs at fixed temperatures $T_i$:
$$
\sum_i \frac{Q_i}{T_i}\le 0.
$$

## Physical interpretation

The inequality expresses the content of the {{< knowl id="second-law-thermodynamics" text="second law" >}} in a form that directly compares heat transfers at different temperatures: heat exchanged at lower temperature carries a larger “entropy weight” $\delta Q/T$. The strictness of the inequality measures how much irreversibility is present in the cycle.

## Key relations

- **Entropy as a state function.** For a reversible process between equilibrium states $A$ and $B$, the integral of $\delta Q/T_{\mathrm{b}}$ is path-independent. This motivates defining the {{< knowl id="thermodynamic-entropy" text="entropy" >}} change by
  $$
  S(B)-S(A)=\int_A^B \frac{\delta Q_{\mathrm{rev}}}{T},
  $$
  where the subscript “rev” emphasizes evaluation along a reversible path (so the boundary and system temperatures coincide).

- **Inequality for general processes.** For any process between equilibrium states,
  $$
  S(B)-S(A)\ge \int_A^B \frac{\delta Q}{T_{\mathrm{b}}},
  $$
  with equality only in the reversible limit.

- **Entropy production form.** Writing
  $$
  \Delta S - \int \frac{\delta Q}{T_{\mathrm{b}}} = S_{\mathrm{gen}},
  $$

  the Clausius inequality is equivalent to $S_{\mathrm{gen}}\ge 0$.

- **Adiabatic implication.** If the system is thermally insulated by an {{< knowl id="adiabatic-wall" text="adiabatic wall" >}} so that $\delta Q=0$, then $\Delta S\ge 0$ for a closed system, with equality only for a reversible adiabatic (isentropic) change.
