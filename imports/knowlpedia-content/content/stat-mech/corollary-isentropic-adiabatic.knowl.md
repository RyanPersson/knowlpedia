+++
id = "stat-mech/corollary-isentropic-adiabatic"
title = "Isentropic processes are reversible adiabatic processes"
kind = "knowl"
summary = "Along reversible processes between equilibrium states, if and only if ."
aliases = ["corollary-isentropic-adiabatic", "Isentropic processes are reversible adiabatic processes"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/corollary-isentropic-adiabatic.md"
+++

Let $S$ be [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] and $T$ the [[thermodynamics/temperature-thermo|temperature]].

## Statement
For any reversible process between equilibrium states,
$$
dS = \frac{\delta Q_{\mathrm{rev}}}{T}.
$$
Consequently:
- If the process is **adiabatic** ($\delta Q_{\mathrm{rev}}=0$ along the path), then it is **isentropic** ($dS=0$, hence $\Delta S=0$).
- Conversely, if a reversible process is **isentropic** ($dS=0$), then $\delta Q_{\mathrm{rev}}=0$ and the process is adiabatic.

More generally, for an adiabatic process not assumed reversible,
$$
\Delta S \ge 0,
$$
with equality if and only if the adiabatic process is reversible.

## Key hypotheses
- The system passes through [[thermodynamics/thermodynamic-equilibrium|equilibrium]] states, so $S$ and $T$ are well-defined along the path.
- The process is reversible in the standard thermodynamic sense (no dissipation).
- “Adiabatic” means no heat exchange: $\delta Q=0$.

## Key conclusions
- In equilibrium thermodynamics, **isentropic** is equivalent to **reversible adiabatic**.
- Any irreversibility in an adiabatic transformation produces entropy: $\Delta S>0$.
