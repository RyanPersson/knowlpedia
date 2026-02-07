---
title: "Reversible process"
description: "An idealized process that can be reversed leaving no net change in the system and surroundings, implying zero entropy production."
---

A **reversible process** is a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}} that can be reversed by an infinitesimal change in external conditions so that **both** the system and the {{< knowl id="surroundings-environment" text="surroundings" >}} are restored exactly to their initial states. Operationally, a reversible process proceeds through a continuous family of equilibrium states and contains **no dissipative effects** (no friction, viscosity, finite-temperature-difference heat flow, diffusion, etc.).

Every reversible process is {{< knowl id="quasistatic-process" text="quasistatic" >}}, but the converse need not hold.

## Physical interpretation
Reversibility is a limiting idealization: the system is always (and everywhere) arbitrarily close to {{< knowl id="thermodynamic-equilibrium" text="equilibrium" >}}, and the driving “forces” are infinitesimal. Intuitively, a reversible process is one that can be run backward without leaving “footprints” in the environment—no wasted work and no net spreading of energy into unavailable forms.

## Key entropy relation
The hallmark of reversibility is **zero entropy production**. For a reversible transfer of heat with the system at {{< knowl id="temperature-thermo" text="temperature" >}} $T$, the change in the {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}} $S$ satisfies the Clausius equality:
$$
dS = \frac{\delta Q_{\mathrm{rev}}}{T}.
$$

Between two equilibrium states $A \to B$ along a reversible path,
$$
\Delta S = \int_{A}^{B} \frac{\delta Q_{\mathrm{rev}}}{T}.
$$
This is the equality case of the {{< knowl id="clausius-inequality" text="Clausius inequality" >}}, a core consequence of the {{< knowl id="second-law-thermodynamics" text="second law" >}}.

For a reversible {{< knowl id="cyclic-process" text="cycle" >}}, the system returns to its initial state, and the entropy balance implies
$$
\oint \frac{\delta Q_{\mathrm{rev}}}{T} = 0.
$$

## Extremal work principle (common thermodynamic use)
Under fixed reservoir constraints, reversible processes are the benchmark for “best possible” performance: they deliver **maximum** work output (or require **minimum** work input) compared with any irreversible alternative connecting the same equilibrium endpoints.

This benchmark is often expressed using free energies. For example, in an isothermal setting (fixed $T$) the maximum useful work is tied to the decrease of the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}}; at fixed $T$ and $P$, it is tied to the decrease of the {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}}, with the notion of “useful” excluding boundary $P\,dV$ work as specified by the {{< knowl id="pressure-volume-work-sign-convention" text="$P\,dV$ convention" >}}.
