+++
id = "thermodynamics/clausius-inequality"
title = "Clausius inequality"
kind = "knowl"
summary = "Integral inequality for heat exchange that quantifies irreversibility and leads to the definition of entropy."
aliases = ["clausius-inequality", "Clausius inequality"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/clausius-inequality.md"
+++

Consider a [[thermodynamics/cyclic-process|cyclic process]] in which a system exchanges heat $\delta Q$ with its surroundings (see [[thermodynamics/heat-inexact-differential|heat]]). Let $T_{\mathrm{b}}$ denote the [[thermodynamics/temperature-thermo|boundary temperature]] at which each heat element crosses the system boundary (e.g., the temperature of a [[thermodynamics/thermal-reservoir|thermal reservoir]] supplying that heat), understood on the [[thermodynamics/absolute-temperature-scale|absolute temperature scale]]. The Clausius inequality states that
$$
\oint \frac{\delta Q}{T_{\mathrm{b}}}\le 0.
$$
Equality holds if and only if the cycle is [[thermodynamics/reversible-process|reversible]]; strict inequality indicates a genuinely [[thermodynamics/irreversible-process|irreversible]] cycle.

A useful special case is a cycle exchanging finite heats $Q_i$ with reservoirs at fixed temperatures $T_i$:
$$
\sum_i \frac{Q_i}{T_i}\le 0.
$$

## Physical interpretation

The inequality expresses the content of the [[thermodynamics/second-law-thermodynamics|second law]] in a form that directly compares heat transfers at different temperatures: heat exchanged at lower temperature carries a larger “entropy weight” $\delta Q/T$. The strictness of the inequality measures how much irreversibility is present in the cycle.

## Key relations

- **Entropy as a state function.** For a reversible process between equilibrium states $A$ and $B$, the integral of $\delta Q/T_{\mathrm{b}}$ is path-independent. This motivates defining the [[thermodynamics/thermodynamic-entropy|entropy]] change by
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

- **Adiabatic implication.** If the system is thermally insulated by an [[thermodynamics/adiabatic-wall|adiabatic wall]] so that $\delta Q=0$, then $\Delta S\ge 0$ for a closed system, with equality only for a reversible adiabatic (isentropic) change.
