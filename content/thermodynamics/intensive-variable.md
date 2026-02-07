---
title: "Intensive variable"
description: "A thermodynamic variable that does not scale with system size and typically equalizes between subsystems at equilibrium."
---

## Definition and physical interpretation

An **intensive variable** is a {{< knowl id="state-variable" text="state variable" >}} whose value does **not** scale with the overall size of the {{< knowl id="thermodynamic-system" text="system" >}}. Concretely, under a uniform rescaling of extensive quantities (e.g. doubling the amount of material so that $S$, $V$, and $N$ all double), intensive variables remain unchanged in the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}}.

This contrasts with an {{< knowl id="extensive-variable" text="extensive variable" >}}, which scales linearly with system size (entropy $S$, volume $V$, particle number $N$, internal energy $U$, and so on).

Intensive variables act like “generalized forces” that drive exchanges between weakly interacting subsystems. At equilibrium they equalize:
- {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}} enforces equality of {{< knowl id="temperature-thermo" text="temperature" >}} $T$.
- {{< knowl id="mechanical-equilibrium" text="mechanical equilibrium" >}} enforces equality of {{< knowl id="pressure-thermo" text="pressure" >}} $p$.
- {{< knowl id="chemical-equilibrium" text="chemical equilibrium" >}} enforces equality of {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} $\mu$.

## Conjugate derivatives from the fundamental relation

If a single-component simple compressible system admits a {{< knowl id="fundamental-relation-energy" text="fundamental relation" >}} $U(S,V,N)$, the standard intensive variables arise as partial derivatives:
$$
T = \left(\frac{\partial U}{\partial S}\right)_{V,N},
\qquad
p = -\left(\frac{\partial U}{\partial V}\right)_{S,N},
\qquad
\mu = \left(\frac{\partial U}{\partial N}\right)_{S,V}.
$$

These relations explain why intensive variables appear as natural control parameters in thermodynamic potentials such as the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} (natural in $T$), the {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}} (natural in $T$ and $p$), the {{< knowl id="enthalpy" text="enthalpy" >}} (natural in $p$), and the {{< knowl id="grand-potential" text="grand potential" >}} (natural in $T$ and $\mu$).

## Homogeneity, Euler, and Gibbs–Duhem

When the system satisfies extensivity so that $U(S,V,N)$ is a {{< knowl id="homogeneous-function-degree-one" text="homogeneous function of degree one" >}}, the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}} takes the form
$$
U = TS - pV + \mu N,
$$

showing $U$ as a sum of intensive–extensive products.

A key consequence is that the intensive variables are not all independent: their allowed variations are constrained by the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}} (single component),
$$
S\,dT - V\,dp + N\,d\mu = 0,
$$
which encodes that changing one intensive variable generally forces changes in the others when the composition is fixed.
