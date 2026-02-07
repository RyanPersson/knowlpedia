---
title: "Work reservoir"
description: "An idealized environment that exchanges energy as work while keeping a generalized force effectively constant."
---

A **work reservoir** is an idealized part of the {{< knowl id="surroundings-environment" text="surroundings" >}} that can exchange energy with a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} **as work** while maintaining (approximately) constant “driving” parameters—typically one or more {{< knowl id="intensive-variable" text="intensive" >}} generalized forces such as an externally imposed pressure, force, torque, electric potential, etc.

The key idealization is *stiffness/size*: the reservoir is so large (or so strongly constrained) that the generalized force(s) it applies do not change appreciably when it gives or absorbs a finite amount of work. Physically, examples include:
- a weight-and-pulley or gravitational field acting as a mechanical work store,
- a piston with weights producing an (approximately) fixed external {{< knowl id="pressure-thermo" text="pressure" >}},
- a large battery acting as an (approximately) fixed voltage source.

Work exchange is described by the {{< knowl id="work-inexact-differential" text="inexact differential of work" >}} $\delta W$, emphasizing that work depends on the {{< knowl id="thermodynamic-process" text="process" >}} (it is a {{< knowl id="path-function" text="path function" >}}), not just the endpoints.

**General form (conjugate pairs).**  
Many work interactions can be written schematically as
$$
\delta W = \sum_i Y_i\,dX_i,
$$

where each $X_i$ is an {{< knowl id="extensive-variable" text="extensive" >}} “displacement-like” variable and each $Y_i$ is its conjugate intensive “force-like” variable. A work reservoir is often modeled as fixing one or more $Y_i$ values externally.

**PV-work as the canonical example.**  
For boundary work involving {{< knowl id="volume-thermo" text="volume" >}} $V$, an external pressure $P_{\text{ext}}$ set by the work reservoir gives
$$
W = \int P_{\text{ext}}\,dV.
$$

If $P_{\text{ext}}$ is constant, then $W = P_{\text{ext}}(V_f - V_i)$. Whether $W$ is counted positive for “work done by the system” or “work done on the system” depends on the site’s {{< knowl id="work-sign-convention" text="work sign convention" >}} and, for PV work in particular, the {{< knowl id="pressure-volume-work-sign-convention" text="pressure–volume work convention" >}}.

**Process dependence and reversibility.**  
In a {{< knowl id="quasistatic-process" text="quasistatic process" >}}, the system’s internal pressure can track the externally imposed pressure closely; in the ideal reversible limit, they coincide throughout (see {{< knowl id="reversible-process" text="reversible" >}} vs. {{< knowl id="irreversible-process" text="irreversible" >}}).

Work reservoirs are often paired with energy bookkeeping via the {{< knowl id="first-law-thermodynamics" text="first law" >}}, which relates work and heat exchanges to changes in {{< knowl id="internal-energy-thermo" text="internal energy" >}}. For controlled heat exchange at fixed temperature instead, one uses a {{< knowl id="thermal-reservoir" text="thermal reservoir" >}}.
