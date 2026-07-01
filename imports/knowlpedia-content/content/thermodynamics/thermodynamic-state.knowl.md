+++
id = "thermodynamics/thermodynamic-state"
title = "Thermodynamic state"
kind = "knowl"
summary = "The macroscopic condition of a system specified by a complete set of state variables (typically in equilibrium)."
aliases = ["thermodynamic-state", "Thermodynamic state"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermodynamic-state.md"
+++

The **thermodynamic state** of a [[thermodynamics/thermodynamic-system|thermodynamic system]] is its macroscopic condition at an instant, characterized (within a chosen level of description) by the values of a complete set of [[thermodynamics/state-variable|state variables]] together with the relevant constraints (fixed boundary, fixed composition, specified external parameters, etc.).

In classical thermodynamics one most often restricts attention to [[thermodynamics/thermodynamic-equilibrium|equilibrium states]], where macroscopic observables are time-independent and the system simultaneously satisfies [[thermodynamics/thermal-equilibrium|thermal]], [[thermodynamics/mechanical-equilibrium|mechanical]], and (when composition can change) [[thermodynamics/chemical-equilibrium|chemical equilibrium]]. Many microscopic configurations (microstates) typically correspond to a single thermodynamic state because they share the same macroscopic state variables.

**Physical interpretation and statistical mechanics.** In equilibrium statistical mechanics, an equilibrium thermodynamic state is represented by an ensemble: a [[probability/probability-measure|probability measure]] over microstates. Macroscopic observables are modeled as [[probability/random-variable|random variables]], and their thermodynamic values correspond to [[probability/expectation|expectations]] (or other typical values) under that measure.

**States and processes.** The set of admissible states forms a state space. A [[thermodynamics/thermodynamic-process|thermodynamic process]] is a path through this space, while a [[thermodynamics/cyclic-process|cyclic process]] is a closed path returning the system to the same state. A [[thermodynamics/quasistatic-process|quasistatic process]] idealizes a process as a continuous sequence of equilibrium states, so state variables remain well-defined along the path.

**State postulate (common form).** For a simple compressible single-component system of fixed composition, an equilibrium state can be specified by two independent state variables (for example, [[thermodynamics/temperature-thermo|temperature]] and [[thermodynamics/volume-thermo|volume]], or [[thermodynamics/pressure-thermo|pressure]] and temperature), together with an [[thermodynamics/equation-of-state|equation of state]] and a [[thermodynamics/fundamental-relation-energy|fundamental relation]]. Quantities determined solely by the state are [[thermodynamics/state-function|state functions]], while transfers such as heat and work are [[thermodynamics/path-function|path functions]].
