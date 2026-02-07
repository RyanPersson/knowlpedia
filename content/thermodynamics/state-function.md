---
title: "State function"
description: "A quantity determined solely by the thermodynamic state, so its change depends only on endpoints."
---

A **state function** is a function $X$ defined on the set of admissible {{< knowl id="thermodynamic-state" text="thermodynamic states" >}} such that, for any process taking the system from state A to state B, the change $\Delta X = X(B)-X(A)$ depends only on the endpoints and not on the particular {{< knowl id="thermodynamic-process" text="process path" >}}.

Equivalently, the differential $dX$ is an **exact differential**: its integral along a path in state space is path-independent.

**Physical interpretation.** State functions represent properties that can be assigned to the system “at an instant” in equilibrium—stored energy, entropy, or thermodynamic potentials encoding equilibrium constraints. They are contrasted with {{< knowl id="path-function" text="path functions" >}} such as {{< knowl id="heat-inexact-differential" text="heat" >}} and {{< knowl id="work-inexact-differential" text="work" >}}, which describe energy transfer *during* a process.

**Key properties**
- **Path independence:** for any two paths from A to B,
  $\int_{\text{path 1}} dX = \int_{\text{path 2}} dX = X(B)-X(A)$.
- **Cyclic integral vanishes:** for any {{< knowl id="cyclic-process" text="cycle" >}},
  $\oint dX = 0$.
- **Exactness generates Maxwell-type relations:** when a thermodynamic potential is written in terms of its natural variables, equality of mixed partial derivatives yields {{< knowl id="maxwell-relation" text="Maxwell relations" >}}.

**Common thermodynamic state functions.** Important examples include {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$, {{< knowl id="thermodynamic-entropy" text="entropy" >}} $S$, {{< knowl id="enthalpy" text="enthalpy" >}} $H$, {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} $F$, {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}} $G$, and (for {{< knowl id="open-system" text="open systems" >}}) the {{< knowl id="grand-potential" text="grand potential" >}} $\Omega$. Many thermodynamic potentials are related by a {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} that exchanges an extensive variable for its conjugate intensive variable.

**Connection to statistical mechanics.** In the canonical ensemble (fixed $T,V,N$), the Helmholtz free energy is linked to the partition function $Z$ by
$$
F = -k_B T \ln Z,
$$

with $k_B$ the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}}. This makes $F$ a generating object for equilibrium averages and response functions.
