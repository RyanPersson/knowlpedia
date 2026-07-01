+++
id = "thermodynamics/quasistatic-process"
title = "Quasistatic process"
kind = "knowl"
summary = "A thermodynamic process carried out slowly enough that the system stays arbitrarily close to equilibrium at each stage."
aliases = ["quasistatic-process", "Quasistatic process"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/quasistatic-process.md"
+++

A **quasistatic process** is a [[thermodynamics/thermodynamic-process|thermodynamic process]] executed slowly enough that the system remains arbitrarily close to [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]] throughout. Equivalently, the system can be described at every instant by a well-defined [[thermodynamics/thermodynamic-state|thermodynamic state]], so macroscopic [[thermodynamics/state-variable|state variables]] (such as temperature and pressure) exist along the entire path.

## Physical interpretation
“Quasistatic” is a controlled idealization based on **separation of time scales**: external driving is slow compared with the system’s internal relaxation times, so spatial gradients (in temperature, pressure, chemical potential, etc.) are negligible within the system at each moment. In practice, a process is quasistatic to the extent that the system remains near equilibrium and its state variables can be treated as meaningful functions of time.

## Key properties and useful relations
Because a quasistatic process admits an equilibrium description at each step, differential expressions take their equilibrium form. For a simple compressible system, the mechanical work element can be written using the [[thermodynamics/pressure-thermo|thermodynamic pressure]] $P$ and [[thermodynamics/volume-thermo|volume]] $V$:
$$
\delta W = P\,dV
$$

with the overall sign determined by the [[thermodynamics/pressure-volume-work-sign-convention|$P\,dV$ sign convention]].

A quasistatic process is **not automatically** a [[thermodynamics/reversible-process|reversible process]]. Dissipative mechanisms (friction, viscosity, electrical resistance, inelasticity) can persist even in the slow-driving limit, making the process [[thermodynamics/irreversible-process|irreversible]] despite being quasistatic. Quasistatic motion ensures the *state* is well-defined along the path; reversibility is the stronger condition that the path can be retraced without net change to system and surroundings.

Many equilibrium identities are derived by considering quasistatic variations of [[thermodynamics/state-function|state functions]], including the [[thermodynamics/maxwell-relation|Maxwell relations]].
