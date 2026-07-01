+++
id = "thermodynamics/first-law-thermodynamics"
title = "First law of thermodynamics"
kind = "knowl"
summary = "Energy conservation in thermodynamics: the change in internal energy equals heat added plus work done on the system (with specified sign conventions)."
aliases = ["first-law-thermodynamics", "First law of thermodynamics"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/first-law-thermodynamics.md"
+++

The **first law of thermodynamics** is the statement of **energy conservation** for a [[thermodynamics/thermodynamic-system|thermodynamic system]]. It postulates the existence of a state function—[[thermodynamics/internal-energy-thermo|internal energy]]—whose change accounts for energy transferred via heat and work during a [[thermodynamics/thermodynamic-process|thermodynamic process]].

**Definition (closed system form).** For a [[thermodynamics/closed-system|closed system]] undergoing any process between equilibrium states,
$$
\Delta U = Q + W,
$$

where $Q$ is the net energy transferred as [[thermodynamics/heat-inexact-differential|heat]] and $W$ is the net energy transferred as [[thermodynamics/work-inexact-differential|work]]. In differential form this is written
$$
dU = \delta Q + \delta W.
$$

The precise sign of $W$ depends on the chosen [[thermodynamics/work-sign-convention|work sign convention]]; likewise, how pressure–volume contributions are recorded is fixed by the [[thermodynamics/pressure-volume-work-sign-convention|pressure–volume work convention]].

**Physical interpretation.** The system’s microscopic energy content can change only by exchanging energy with the [[thermodynamics/surroundings-environment|surroundings]]. The first law does not say *how* that energy exchange must occur; it only asserts that all exchanges add up consistently into a conserved accounting.

**Heat and work are path-dependent.** While $U$ is a [[thermodynamics/state-function|state function]] (so $\Delta U$ depends only on the endpoints), $Q$ and $W$ are [[thermodynamics/path-function|path functions]]: their values depend on the details of the process. This is why one writes $\delta Q$ and $\delta W$ rather than exact differentials.

**Useful consequences and special cases.**
- **Cyclic processes.** For a [[thermodynamics/cyclic-process|cyclic process]], $\Delta U=0$, hence the net heat and work balance:
  $$
  \oint \delta Q + \oint \delta W = 0.
  $$
- **Mechanical work example.** In a quasistatic compression/expansion, work is often dominated by pressure–volume exchange involving [[thermodynamics/pressure-thermo|pressure]] and [[thermodynamics/volume-thermo|volume]]; the sign and exact form follow the adopted conventions referenced above.
- **Particle exchange.** For an [[thermodynamics/open-system|open system]] where [[thermodynamics/particle-number|particles]] cross the [[thermodynamics/system-boundary|system boundary]], energy can also be transported with matter. In equilibrium thermodynamics this contribution is commonly organized using the [[thermodynamics/chemical-potential-thermo|chemical potential]] and a [[thermodynamics/chemical-work-convention|chemical work convention]]; a common bookkeeping form is
  $$
  dU = \delta Q + \delta W + \mu\, dN,
  $$
  with the understanding that what is counted as “work-like” versus “heat-like” depends on the chosen convention and description.

Together with the [[thermodynamics/second-law-thermodynamics|second law]], the first law anchors the structure of equilibrium thermodynamics by linking measurable transfers ($Q,W$) to changes in a state property ($U$).
