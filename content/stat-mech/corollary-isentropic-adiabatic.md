---
title: "Isentropic processes are reversible adiabatic processes"
description: "Along reversible processes between equilibrium states, if and only if ."
---

Let $S$ be {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} and $T$ the {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.

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
- The system passes through {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="equilibrium" >}} states, so $S$ and $T$ are well-defined along the path.
- The process is reversible in the standard thermodynamic sense (no dissipation).
- “Adiabatic” means no heat exchange: $\delta Q=0$.

## Key conclusions
- In equilibrium thermodynamics, **isentropic** is equivalent to **reversible adiabatic**.
- Any irreversibility in an adiabatic transformation produces entropy: $\Delta S>0$.

