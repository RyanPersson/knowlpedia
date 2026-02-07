---
title: "Quasistatic process"
description: "A thermodynamic process carried out slowly enough that the system stays arbitrarily close to equilibrium at each stage."
---

A **quasistatic process** is a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}} executed slowly enough that the system remains arbitrarily close to {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}} throughout. Equivalently, the system can be described at every instant by a well-defined {{< knowl id="thermodynamic-state" text="thermodynamic state" >}}, so macroscopic {{< knowl id="state-variable" text="state variables" >}} (such as temperature and pressure) exist along the entire path.

## Physical interpretation
“Quasistatic” is a controlled idealization based on **separation of time scales**: external driving is slow compared with the system’s internal relaxation times, so spatial gradients (in temperature, pressure, chemical potential, etc.) are negligible within the system at each moment. In practice, a process is quasistatic to the extent that the system remains near equilibrium and its state variables can be treated as meaningful functions of time.

## Key properties and useful relations
Because a quasistatic process admits an equilibrium description at each step, differential expressions take their equilibrium form. For a simple compressible system, the mechanical work element can be written using the {{< knowl id="pressure-thermo" text="thermodynamic pressure" >}} $P$ and {{< knowl id="volume-thermo" text="volume" >}} $V$:
$$
\delta W = P\,dV
$$

with the overall sign determined by the {{< knowl id="pressure-volume-work-sign-convention" text="$P\,dV$ sign convention" >}}.

A quasistatic process is **not automatically** a {{< knowl id="reversible-process" text="reversible process" >}}. Dissipative mechanisms (friction, viscosity, electrical resistance, inelasticity) can persist even in the slow-driving limit, making the process {{< knowl id="irreversible-process" text="irreversible" >}} despite being quasistatic. Quasistatic motion ensures the *state* is well-defined along the path; reversibility is the stronger condition that the path can be retraced without net change to system and surroundings.

Many equilibrium identities are derived by considering quasistatic variations of {{< knowl id="state-function" text="state functions" >}}, including the {{< knowl id="maxwell-relation" text="Maxwell relations" >}}.
