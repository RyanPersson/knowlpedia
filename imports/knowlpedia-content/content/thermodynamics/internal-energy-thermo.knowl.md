+++
id = "thermodynamics/internal-energy-thermo"
title = "Internal energy"
kind = "knowl"
summary = "A state function giving the energy stored in a thermodynamic system (excluding bulk kinetic and potential energies)."
aliases = ["internal-energy-thermo", "Internal energy"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/internal-energy-thermo.md"
+++

The **internal energy** $U$ is a [[thermodynamics/state-function|state function]] that assigns to each [[thermodynamics/thermodynamic-state|equilibrium state]] of a [[thermodynamics/thermodynamic-system|thermodynamic system]] the amount of energy stored in its microscopic degrees of freedom (molecular motion, interactions, chemical bonding, etc.), excluding the macroscopic kinetic energy of the system’s center of mass and any macroscopic potential energy due to external fields that one chooses to treat separately.

**Physical interpretation.**
Internal energy is the energy “inside” the system associated with its microstate: random thermal motion, intermolecular potential energy, internal excitations, and (depending on modeling choices) chemical and field energies. It is the quantity that changes when the system is heated, compressed, stirred with friction, undergoes a phase change, or reacts chemically—once the bookkeeping of heat/work/matter exchange is fixed.

**Thermodynamic definition via the first law.**
Changes in internal energy are constrained by the [[thermodynamics/first-law-thermodynamics|first law of thermodynamics]]:
$$
dU = \delta Q - \delta W,
$$

where $\delta Q$ is the [[thermodynamics/heat-inexact-differential|heat inexact differential]] and $\delta W$ is the [[thermodynamics/work-inexact-differential|work inexact differential]]. The precise sign in front of $\delta W$ depends on the adopted [[thermodynamics/work-sign-convention|work sign convention]]; the key structural point is that $U$ is a state function while heat and work are [[thermodynamics/path-function|path functions]].

A useful special case is a process carried out with an [[thermodynamics/adiabatic-wall|adiabatic wall]], for which $\delta Q = 0$ across that boundary; then changes in $U$ are accounted for purely by work transfer (again with sign determined by convention).

**Natural variables and differential form (simple compressible system).**
For a single-component simple compressible system, $U$ is naturally viewed as a function of [[thermodynamics/thermodynamic-entropy|entropy]] $S$, [[thermodynamics/volume-thermo|volume]] $V$, and [[thermodynamics/particle-number|particle number]] $N$:
$$
U = U(S,V,N).
$$
Its total differential can be written
$$
dU = T\,dS - P\,dV + \mu\,dN,
$$

where $T$ is [[thermodynamics/temperature-thermo|temperature]], $P$ is [[thermodynamics/pressure-thermo|pressure]], and $\mu$ is [[thermodynamics/chemical-potential-thermo|chemical potential]]. This “energy representation” is closely tied to the [[thermodynamics/fundamental-relation-energy|fundamental relation in energy form]].

**Extensivity and Euler-type relations.**
In macroscopic thermodynamics, $U$ is typically [[thermodynamics/extensive-variable|extensive]] and compatible with the [[thermodynamics/extensivity-postulate|extensivity postulate]] (often along with an [[thermodynamics/additivity-postulate|additivity postulate]]). When $U(S,V,N)$ is a [[thermodynamics/homogeneous-function-degree-one|homogeneous function of degree one]] in its extensive arguments, one obtains the [[thermodynamics/euler-relation-thermodynamics|Euler relation]] connecting $U$ to its conjugate intensities; consistency of these relations is encoded by the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]].

**Connection to other thermodynamic potentials.**
Internal energy generates other commonly used potentials by Legendre-type rearrangements of natural variables, such as [[thermodynamics/enthalpy|enthalpy]], [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]], [[thermodynamics/gibbs-free-energy|Gibbs free energy]], and the [[thermodynamics/grand-potential|grand potential]]. These are convenient when the environment controls different intensive variables (for example via a [[thermodynamics/thermal-reservoir|thermal reservoir]] fixing temperature or a [[thermodynamics/work-reservoir|work reservoir]] fixing an external pressure).

**Statistical-mechanics bridge.**
In the canonical description (see [[thermodynamics/canonical-ensemble-convention|canonical ensemble conventions]]), the thermodynamic internal energy corresponds to the [[probability/expectation|expectation]] of the microscopic energy under the Boltzmann distribution set by $\beta = 1/(k_B T)$, linking $U$ directly to temperature and the [[thermodynamics/boltzmann-constant|Boltzmann constant]].
