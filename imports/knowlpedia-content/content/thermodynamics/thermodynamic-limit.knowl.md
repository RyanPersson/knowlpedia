+++
id = "thermodynamics/thermodynamic-limit"
title = "Thermodynamic limit"
kind = "knowl"
summary = "The large-system limit in which size goes to infinity at fixed densities, making macroscopic thermodynamics well-defined and boundary effects negligible."
aliases = ["thermodynamic-limit", "Thermodynamic limit"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermodynamic-limit.md"
+++

The **thermodynamic limit** is a limiting procedure (not a physical process) in which a sequence of larger and larger [[thermodynamics/thermodynamic-system|thermodynamic systems]] is considered while keeping intensive control parameters and densities fixed.

**Definition (continuum form).** For a system in a container of volume $V$ with [[thermodynamics/particle-number|particle number]] $N$, the thermodynamic limit is typically
$$
V\to\infty,\qquad N\to\infty,\qquad \rho=\frac{N}{V}\ \text{fixed},
$$

and similarly for other extensive quantities so that quantities like [[thermodynamics/number-density|number density]] $\rho$, [[thermodynamics/energy-density|energy density]] $u=U/V$, and [[thermodynamics/entropy-density|entropy density]] $s=S/V$ approach well-defined limits.

(For lattice systems one often replaces $V$ by the number of sites $|\Lambda|$ and sends $|\Lambda|\to\infty$, with choices encoded by [[thermodynamics/boundary-condition-convention-lattice|boundary condition conventions]].)

**Physical interpretation.** Real macroscopic matter has an enormous number of degrees of freedom, and bulk measurements are insensitive to microscopic details at the boundary. The thermodynamic limit idealizes this by making surface-to-volume effects vanish, so that equilibrium properties become “bulk” properties. This is the regime in which the [[thermodynamics/extensivity-postulate|extensivity postulate]] and [[thermodynamics/additivity-postulate|additivity postulate]] are operationally accurate.

**Key consequences.**
- **Well-defined intensive thermodynamics.** Many quantities become sharply defined functions of [[thermodynamics/intensive-variable|intensive variables]] and densities, leading to a clean [[thermodynamics/equation-of-state|equation of state]].
- **Boundary-condition independence (in typical stable models).** Bulk potentials per volume or per particle often converge to limits that do not depend on container shape or boundary conditions; when this happens, the limiting objects are captured by [[thermodynamics/thermodynamic-limit-state-function|thermodynamic-limit state functions]].
- **Phase transitions require the limit.** Non-analytic behavior of thermodynamic potentials (sharp phase transitions) is excluded in many finite systems but can emerge when the thermodynamic limit is taken.
- **Conventions matter.** Precise statements depend on how the limit is taken; see [[thermodynamics/thermodynamic-limit-convention|thermodynamic limit conventions]] and, for ensembles, [[thermodynamics/canonical-ensemble-convention|canonical ensemble conventions]] and [[thermodynamics/grand-canonical-ensemble-convention|grand canonical ensemble conventions]].
