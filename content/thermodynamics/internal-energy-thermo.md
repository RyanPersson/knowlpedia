---
title: "Internal energy"
description: "A state function giving the energy stored in a thermodynamic system (excluding bulk kinetic and potential energies)."
---

The **internal energy** $U$ is a {{< knowl id="state-function" text="state function" >}} that assigns to each {{< knowl id="thermodynamic-state" text="equilibrium state" >}} of a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} the amount of energy stored in its microscopic degrees of freedom (molecular motion, interactions, chemical bonding, etc.), excluding the macroscopic kinetic energy of the system’s center of mass and any macroscopic potential energy due to external fields that one chooses to treat separately.

**Physical interpretation.**  
Internal energy is the energy “inside” the system associated with its microstate: random thermal motion, intermolecular potential energy, internal excitations, and (depending on modeling choices) chemical and field energies. It is the quantity that changes when the system is heated, compressed, stirred with friction, undergoes a phase change, or reacts chemically—once the bookkeeping of heat/work/matter exchange is fixed.

**Thermodynamic definition via the first law.**  
Changes in internal energy are constrained by the {{< knowl id="first-law-thermodynamics" text="first law of thermodynamics" >}}:
$$
dU = \delta Q - \delta W,
$$

where $\delta Q$ is the {{< knowl id="heat-inexact-differential" text="heat inexact differential" >}} and $\delta W$ is the {{< knowl id="work-inexact-differential" text="work inexact differential" >}}. The precise sign in front of $\delta W$ depends on the adopted {{< knowl id="work-sign-convention" text="work sign convention" >}}; the key structural point is that $U$ is a state function while heat and work are {{< knowl id="path-function" text="path functions" >}}.

A useful special case is a process carried out with an {{< knowl id="adiabatic-wall" text="adiabatic wall" >}}, for which $\delta Q = 0$ across that boundary; then changes in $U$ are accounted for purely by work transfer (again with sign determined by convention).

**Natural variables and differential form (simple compressible system).**  
For a single-component simple compressible system, $U$ is naturally viewed as a function of {{< knowl id="thermodynamic-entropy" text="entropy" >}} $S$, {{< knowl id="volume-thermo" text="volume" >}} $V$, and {{< knowl id="particle-number" text="particle number" >}} $N$:
$$
U = U(S,V,N).
$$
Its total differential can be written
$$
dU = T\,dS - P\,dV + \mu\,dN,
$$

where $T$ is {{< knowl id="temperature-thermo" text="temperature" >}}, $P$ is {{< knowl id="pressure-thermo" text="pressure" >}}, and $\mu$ is {{< knowl id="chemical-potential-thermo" text="chemical potential" >}}. This “energy representation” is closely tied to the {{< knowl id="fundamental-relation-energy" text="fundamental relation in energy form" >}}.

**Extensivity and Euler-type relations.**  
In macroscopic thermodynamics, $U$ is typically {{< knowl id="extensive-variable" text="extensive" >}} and compatible with the {{< knowl id="extensivity-postulate" text="extensivity postulate" >}} (often along with an {{< knowl id="additivity-postulate" text="additivity postulate" >}}). When $U(S,V,N)$ is a {{< knowl id="homogeneous-function-degree-one" text="homogeneous function of degree one" >}} in its extensive arguments, one obtains the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}} connecting $U$ to its conjugate intensities; consistency of these relations is encoded by the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}}.

**Connection to other thermodynamic potentials.**  
Internal energy generates other commonly used potentials by Legendre-type rearrangements of natural variables, such as {{< knowl id="enthalpy" text="enthalpy" >}}, {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}}, {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}}, and the {{< knowl id="grand-potential" text="grand potential" >}}. These are convenient when the environment controls different intensive variables (for example via a {{< knowl id="thermal-reservoir" text="thermal reservoir" >}} fixing temperature or a {{< knowl id="work-reservoir" text="work reservoir" >}} fixing an external pressure).

**Statistical-mechanics bridge.**  
In the canonical description (see {{< knowl id="canonical-ensemble-convention" text="canonical ensemble conventions" >}}), the thermodynamic internal energy corresponds to the {{< knowl id="expectation" section="probability" text="expectation" >}} of the microscopic energy under the Boltzmann distribution set by $\beta = 1/(k_B T)$, linking $U$ directly to temperature and the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}}.
