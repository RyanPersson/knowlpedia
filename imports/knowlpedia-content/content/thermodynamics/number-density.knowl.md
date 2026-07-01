+++
id = "thermodynamics/number-density"
title = "Number density"
kind = "knowl"
summary = "Particle number per volume, n = N/V, an intensive measure of concentration."
aliases = ["number-density", "Number density"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/number-density.md"
+++

The **number density** $n$ is the [[thermodynamics/particle-number|particle number]] per [[thermodynamics/volume-thermo|volume]]. It is a central intensive descriptor of a material’s concentration.

For a homogeneous system with particle number $N$ and volume $V$, the **number density** is
$$
n \equiv \frac{N}{V}.
$$

Equivalently, $N = nV$ for a homogeneous equilibrium state.

In spatially varying situations (e.g., local equilibrium), one often uses a field $n(\mathbf{r})$ such that integrating over the volume gives the total particle number.

## Physical interpretation
Number density tells you how tightly packed particles are in space. Holding $n$ fixed while taking the [[thermodynamics/thermodynamic-limit|thermodynamic limit]] keeps the “bulk” state of matter comparable as the system size grows.

Because it is a ratio of two [[thermodynamics/extensive-variable|extensive variables]], $n$ is a [[thermodynamics/intensive-variable|typical intensive variable]] and is an example of a [[thermodynamics/specific-quantity|specific quantity]] (per volume).

## Key relations
- **Equation of state viewpoint:** Many [[thermodynamics/equation-of-state|equations of state]] express [[thermodynamics/pressure-thermo|pressure]] as a function of [[thermodynamics/temperature-thermo|temperature]] and number density, $p=p(T,n)$. For an ideal gas this becomes $p = n k_B T$, where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]].

- **Link to chemical potential:** In many systems the [[thermodynamics/chemical-potential-thermo|chemical potential]] can be viewed (holding temperature fixed) as encoding how the free energy changes with density, so $n$ is often the natural “composition” variable in equilibrium thermodynamics.
