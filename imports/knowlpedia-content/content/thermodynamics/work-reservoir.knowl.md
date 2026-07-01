+++
id = "thermodynamics/work-reservoir"
title = "Work reservoir"
kind = "knowl"
summary = "An idealized environment that exchanges energy as work while keeping a generalized force effectively constant."
aliases = ["work-reservoir", "Work reservoir"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/work-reservoir.md"
+++

A **work reservoir** is an idealized part of the [[thermodynamics/surroundings-environment|surroundings]] that can exchange energy with a [[thermodynamics/thermodynamic-system|thermodynamic system]] **as work** while maintaining (approximately) constant “driving” parameters—typically one or more [[thermodynamics/intensive-variable|intensive]] generalized forces such as an externally imposed pressure, force, torque, electric potential, etc.

The key idealization is *stiffness/size*: the reservoir is so large (or so strongly constrained) that the generalized force(s) it applies do not change appreciably when it gives or absorbs a finite amount of work. Physically, examples include:
- a weight-and-pulley or gravitational field acting as a mechanical work store,
- a piston with weights producing an (approximately) fixed external [[thermodynamics/pressure-thermo|pressure]],
- a large battery acting as an (approximately) fixed voltage source.

Work exchange is described by the [[thermodynamics/work-inexact-differential|inexact differential of work]] $\delta W$, emphasizing that work depends on the [[thermodynamics/thermodynamic-process|process]] (it is a [[thermodynamics/path-function|path function]]), not just the endpoints.

**General form (conjugate pairs).**
Many work interactions can be written schematically as
$$
\delta W = \sum_i Y_i\,dX_i,
$$

where each $X_i$ is an [[thermodynamics/extensive-variable|extensive]] “displacement-like” variable and each $Y_i$ is its conjugate intensive “force-like” variable. A work reservoir is often modeled as fixing one or more $Y_i$ values externally.

**PV-work as the canonical example.**
For boundary work involving [[thermodynamics/volume-thermo|volume]] $V$, an external pressure $P_{\text{ext}}$ set by the work reservoir gives
$$
W = \int P_{\text{ext}}\,dV.
$$

If $P_{\text{ext}}$ is constant, then $W = P_{\text{ext}}(V_f - V_i)$. Whether $W$ is counted positive for “work done by the system” or “work done on the system” depends on the site’s [[thermodynamics/work-sign-convention|work sign convention]] and, for PV work in particular, the [[thermodynamics/pressure-volume-work-sign-convention|pressure–volume work convention]].

**Process dependence and reversibility.**
In a [[thermodynamics/quasistatic-process|quasistatic process]], the system’s internal pressure can track the externally imposed pressure closely; in the ideal reversible limit, they coincide throughout (see [[thermodynamics/reversible-process|reversible]] vs. [[thermodynamics/irreversible-process|irreversible]]).

Work reservoirs are often paired with energy bookkeeping via the [[thermodynamics/first-law-thermodynamics|first law]], which relates work and heat exchanges to changes in [[thermodynamics/internal-energy-thermo|internal energy]]. For controlled heat exchange at fixed temperature instead, one uses a [[thermodynamics/thermal-reservoir|thermal reservoir]].
