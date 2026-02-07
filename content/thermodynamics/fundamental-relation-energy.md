---
title: "Fundamental relation (energy representation)"
description: "The internal energy function U(S,V,N,...) that generates temperature, pressure, and chemical potential by differentiation."
---

In the **energy representation**, the **fundamental relation** is the equilibrium internal energy written as a function of the extensive variables:
$U = U(S,V,N,\dots)$,
with $S$ the {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}}, $V$ the {{< knowl id="volume-thermo" text="volume" >}}, and $N$ the {{< knowl id="particle-number" text="particle number" >}} (plus any other extensive conserved quantities). Knowing this single state function determines all equilibrium thermodynamics for a system in {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}}.

**Physical interpretation.** The function $U(S,V,N,\dots)$ tells you the energy cost of “building” a macrostate with given entropy, size, and composition. Its derivatives are the intensive variables that govern exchange of energy, volume, and particles across the {{< knowl id="system-boundary" text="system boundary" >}}.

**Generating derivatives.** The differential form is
$$
dU = T\,dS - P\,dV + \mu\,dN + \cdots ,
$$
which defines
- $T=\left(\frac{\partial U}{\partial S}\right)_{V,N,\dots}$ ({{< knowl id="temperature-thermo" text="temperature" >}})
- $-P=\left(\frac{\partial U}{\partial V}\right)_{S,N,\dots}$ ({{< knowl id="pressure-thermo" text="pressure" >}})
- $\mu=\left(\frac{\partial U}{\partial N}\right)_{S,V,\dots}$ ({{< knowl id="chemical-potential-thermo" text="chemical potential" >}})

An {{< knowl id="equation-of-state" text="equation of state" >}} can be obtained by re-expressing these derivatives in terms of $(T,V,N)$ or other convenient independent variables.

**Key properties.**
- **Extensivity as homogeneity.** For additive macroscopic systems, $U$ is extensive and ideally {{< knowl id="homogeneous-function-degree-one" text="homogeneous of degree one" >}} in $(S,V,N,\dots)$, implying the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}} and leading to the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}} among intensive variables.
- **Convexity and stability.** Stability in the energy representation corresponds to appropriate convexity properties of $U$ (as a function of extensive variables), connecting to {{< knowl id="energy-convexity-stability" text="energy convexity (stability)" >}} and constraining measurable {{< knowl id="response-function-thermo" text="response functions" >}}.
- **Link to work/heat differentials.** Along a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}}, the first law relates changes in $U$ to {{< knowl id="heat-inexact-differential" text="heat" >}} and {{< knowl id="work-inexact-differential" text="work" >}} via {{< knowl id="first-law-thermodynamics" text="the first law" >}}.
