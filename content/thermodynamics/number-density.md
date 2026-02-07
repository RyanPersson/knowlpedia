---
title: "Number density"
description: "Particle number per volume, n = N/V, an intensive measure of concentration."
---

The **number density** $n$ is the {{< knowl id="particle-number" text="particle number" >}} per {{< knowl id="volume-thermo" text="volume" >}}. It is a central intensive descriptor of a material’s concentration.

For a homogeneous system with particle number $N$ and volume $V$, the **number density** is
$$
n \equiv \frac{N}{V}.
$$

Equivalently, $N = nV$ for a homogeneous equilibrium state.

In spatially varying situations (e.g., local equilibrium), one often uses a field $n(\mathbf{r})$ such that integrating over the volume gives the total particle number.

## Physical interpretation
Number density tells you how tightly packed particles are in space. Holding $n$ fixed while taking the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}} keeps the “bulk” state of matter comparable as the system size grows.

Because it is a ratio of two {{< knowl id="extensive-variable" text="extensive variables" >}}, $n$ is a {{< knowl id="intensive-variable" text="typical intensive variable" >}} and is an example of a {{< knowl id="specific-quantity" text="specific quantity" >}} (per volume).

## Key relations
- **Equation of state viewpoint:** Many {{< knowl id="equation-of-state" text="equations of state" >}} express {{< knowl id="pressure-thermo" text="pressure" >}} as a function of {{< knowl id="temperature-thermo" text="temperature" >}} and number density, $p=p(T,n)$. For an ideal gas this becomes $p = n k_B T$, where $k_B$ is the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}}.

- **Link to chemical potential:** In many systems the {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} can be viewed (holding temperature fixed) as encoding how the free energy changes with density, so $n$ is often the natural “composition” variable in equilibrium thermodynamics.
