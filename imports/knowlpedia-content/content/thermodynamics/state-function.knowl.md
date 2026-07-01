+++
id = "thermodynamics/state-function"
title = "State function"
kind = "knowl"
summary = "A quantity determined solely by the thermodynamic state, so its change depends only on endpoints."
aliases = ["state-function", "State function"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/state-function.md"
+++

A **state function** is a function $X$ defined on the set of admissible [[thermodynamics/thermodynamic-state|thermodynamic states]] such that, for any process taking the system from state A to state B, the change $\Delta X = X(B)-X(A)$ depends only on the endpoints and not on the particular [[thermodynamics/thermodynamic-process|process path]].

Equivalently, the differential $dX$ is an **exact differential**: its integral along a path in state space is path-independent.

**Physical interpretation.** State functions represent properties that can be assigned to the system “at an instant” in equilibrium—stored energy, entropy, or thermodynamic potentials encoding equilibrium constraints. They are contrasted with [[thermodynamics/path-function|path functions]] such as [[thermodynamics/heat-inexact-differential|heat]] and [[thermodynamics/work-inexact-differential|work]], which describe energy transfer *during* a process.

**Key properties**
- **Path independence:** for any two paths from A to B,
  $\int_{\text{path 1}} dX = \int_{\text{path 2}} dX = X(B)-X(A)$.
- **Cyclic integral vanishes:** for any [[thermodynamics/cyclic-process|cycle]],
  $\oint dX = 0$.
- **Exactness generates Maxwell-type relations:** when a thermodynamic potential is written in terms of its natural variables, equality of mixed partial derivatives yields [[thermodynamics/maxwell-relation|Maxwell relations]].

**Common thermodynamic state functions.** Important examples include [[thermodynamics/internal-energy-thermo|internal energy]] $U$, [[thermodynamics/thermodynamic-entropy|entropy]] $S$, [[thermodynamics/enthalpy|enthalpy]] $H$, [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F$, [[thermodynamics/gibbs-free-energy|Gibbs free energy]] $G$, and (for [[thermodynamics/open-system|open systems]]) the [[thermodynamics/grand-potential|grand potential]] $\Omega$. Many thermodynamic potentials are related by a [[convex-analysis/legendre-transform|Legendre transform]] that exchanges an extensive variable for its conjugate intensive variable.

**Connection to statistical mechanics.** In the canonical ensemble (fixed $T,V,N$), the Helmholtz free energy is linked to the partition function $Z$ by
$$
F = -k_B T \ln Z,
$$

with $k_B$ the [[thermodynamics/boltzmann-constant|Boltzmann constant]]. This makes $F$ a generating object for equilibrium averages and response functions.
