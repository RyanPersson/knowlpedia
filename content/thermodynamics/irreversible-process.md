---
title: "Irreversible process"
description: "A real process that cannot be exactly reversed without leaving net changes in the system or surroundings, producing entropy."
---

An **irreversible process** is a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}} that **cannot** be reversed so as to restore both the system and the surroundings to their initial conditions. Equivalently, an irreversible process involves dissipation and produces positive entropy in the combined system-plus-environment, in contrast to a {{< knowl id="reversible-process" text="reversible process" >}}.

## Physical interpretation
Irreversibility is the generic case in nature. It arises whenever the process is driven by **finite gradients** (temperature differences, pressure differences, chemical potential differences) or includes dissipative mechanisms such as friction, viscosity, diffusion, mixing, inelastic deformation, or chemical reaction. These mechanisms degrade organized energy transfers into more “disordered” microscopic energy distributions, making exact retracing impossible without additional net changes in the environment.

A process can be {{< knowl id="quasistatic-process" text="quasistatic" >}} and still irreversible—for example, a very slow compression with friction: the system remains near equilibrium (so $P$ and $T$ are well-defined), yet mechanical energy is dissipated as heat.

## Key entropy inequalities
Irreversibility is quantified by the {{< knowl id="second-law-thermodynamics" text="second law" >}} through the {{< knowl id="clausius-inequality" text="Clausius inequality" >}}. For any process connecting equilibrium states,
$$
\Delta S \ge \int \frac{\delta Q}{T_{\mathrm{b}}},
$$

where $T_{\mathrm{b}}$ is the temperature at the boundary where heat $\delta Q$ crosses the {{< knowl id="system-boundary" text="boundary" >}}. Equality holds only for a reversible process.

A common entropy balance form is
$$
\Delta S = \int \frac{\delta Q}{T_{\mathrm{b}}} + S_{\mathrm{gen}},
$$

with entropy generation $S_{\mathrm{gen}} \ge 0$, and $S_{\mathrm{gen}} > 0$ for irreversible processes.

For an {{< knowl id="isolated-system" text="isolated system" >}} ($\delta Q = 0$ and no matter transfer), this reduces to
$$
\Delta S = S_{\mathrm{gen}} \ge 0,
$$
capturing the tendency toward {{< knowl id="thermodynamic-equilibrium" text="equilibrium" >}}.
