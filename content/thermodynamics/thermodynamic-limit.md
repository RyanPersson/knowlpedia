---
title: "Thermodynamic limit"
description: "The large-system limit in which size goes to infinity at fixed densities, making macroscopic thermodynamics well-defined and boundary effects negligible."
---

The **thermodynamic limit** is a limiting procedure (not a physical process) in which a sequence of larger and larger {{< knowl id="thermodynamic-system" text="thermodynamic systems" >}} is considered while keeping intensive control parameters and densities fixed.

**Definition (continuum form).** For a system in a container of volume $V$ with {{< knowl id="particle-number" text="particle number" >}} $N$, the thermodynamic limit is typically
$$
V\to\infty,\qquad N\to\infty,\qquad \rho=\frac{N}{V}\ \text{fixed},
$$

and similarly for other extensive quantities so that quantities like {{< knowl id="number-density" text="number density" >}} $\rho$, {{< knowl id="energy-density" text="energy density" >}} $u=U/V$, and {{< knowl id="entropy-density" text="entropy density" >}} $s=S/V$ approach well-defined limits.

(For lattice systems one often replaces $V$ by the number of sites $|\Lambda|$ and sends $|\Lambda|\to\infty$, with choices encoded by {{< knowl id="boundary-condition-convention-lattice" text="boundary condition conventions" >}}.)

**Physical interpretation.** Real macroscopic matter has an enormous number of degrees of freedom, and bulk measurements are insensitive to microscopic details at the boundary. The thermodynamic limit idealizes this by making surface-to-volume effects vanish, so that equilibrium properties become “bulk” properties. This is the regime in which the {{< knowl id="extensivity-postulate" text="extensivity postulate" >}} and {{< knowl id="additivity-postulate" text="additivity postulate" >}} are operationally accurate.

**Key consequences.**
- **Well-defined intensive thermodynamics.** Many quantities become sharply defined functions of {{< knowl id="intensive-variable" text="intensive variables" >}} and densities, leading to a clean {{< knowl id="equation-of-state" text="equation of state" >}}.
- **Boundary-condition independence (in typical stable models).** Bulk potentials per volume or per particle often converge to limits that do not depend on container shape or boundary conditions; when this happens, the limiting objects are captured by {{< knowl id="thermodynamic-limit-state-function" text="thermodynamic-limit state functions" >}}.
- **Phase transitions require the limit.** Non-analytic behavior of thermodynamic potentials (sharp phase transitions) is excluded in many finite systems but can emerge when the thermodynamic limit is taken.
- **Conventions matter.** Precise statements depend on how the limit is taken; see {{< knowl id="thermodynamic-limit-convention" text="thermodynamic limit conventions" >}} and, for ensembles, {{< knowl id="canonical-ensemble-convention" text="canonical ensemble conventions" >}} and {{< knowl id="grand-canonical-ensemble-convention" text="grand canonical ensemble conventions" >}}.
