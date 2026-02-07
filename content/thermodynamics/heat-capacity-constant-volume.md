---
title: "Heat capacity at constant volume"
description: "A response function measuring how internal energy changes with temperature when volume (and composition) are held fixed."
---

For a closed, simple {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} in {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}}, the **heat capacity at constant volume** is the {{< knowl id="response-function-thermo" text="response function" >}}
that quantifies how the {{< knowl id="internal-energy-thermo" text="internal energy" >}} changes with the {{< knowl id="temperature-thermo" text="temperature" >}} when the {{< knowl id="volume-thermo" text="volume" >}} is fixed (and the composition is fixed, e.g. fixed {{< knowl id="particle-number" text="particle number" >}} $N$ for a single-component system).

The heat capacity at constant volume is
$$
C_V \equiv \left(\frac{\partial U}{\partial T}\right)_{V,N}.
$$

Because $U$ and $T$ are {{< knowl id="state-function" text="state functions" >}} (for equilibrium states), $C_V$ is a property of the equilibrium {{< knowl id="thermodynamic-state" text="state" >}}.

A useful equivalent form follows from the {{< knowl id="fundamental-relation-energy" text="fundamental energy differential" >}} for a simple compressible system,
which implies that at fixed $V$ and $N$ one has $dU = T\,dS$. Hence
$$
C_V
= T\left(\frac{\partial S}{\partial T}\right)_{V,N},
$$

where $S$ is the {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}}.

## Physical interpretation
Along a {{< knowl id="quasistatic-process" text="quasistatic" >}}, {{< knowl id="reversible-process" text="reversible" >}} process in which $V$ and $N$ are held fixed, the heat increment satisfies
$$
\delta Q_{\rm rev} = C_V\,dT.
$$

This is why $C_V$ is often described as “the heat required per unit temperature rise at constant volume”: the container is effectively rigid, so there is no $p\,dV$ expansion and the energy input shows up entirely as a change in internal energy.

## Key relations and properties
- **Extensivity:** $C_V$ is typically an {{< knowl id="extensive-variable" text="extensive" >}} quantity. One often uses a {{< knowl id="specific-quantity" text="specific" >}} or per-particle form such as $c_V = C_V/N$ (or per unit mass).

- **Free-energy curvature:** In terms of the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} $F(T,V,N)$, one has
  $$
  C_V = -\,T\left(\frac{\partial^2 F}{\partial T^2}\right)_{V,N}.
  $$

- **Stability (typical sign):** For stable single-phase equilibrium states, one expects $C_V \ge 0$; this is tied to {{< knowl id="thermodynamic-stability" text="thermodynamic stability" >}} and can be viewed as a consequence of {{< knowl id="entropy-concavity-stability" text="entropy concavity" >}} (or equivalently {{< knowl id="energy-convexity-stability" text="energy convexity" >}} in appropriate variables).

- **Difference from constant-pressure heat capacity:** The difference between $C_V$ and the {{< knowl id="heat-capacity-constant-pressure" text="constant-pressure heat capacity" >}} is
  $$
  C_P - C_V = \frac{T\,V\,\alpha^2}{\kappa_T},
  $$

  where $\alpha$ is the {{< knowl id="thermal-expansion-coefficient" text="thermal expansion coefficient" >}} and $\kappa_T$ is the {{< knowl id="isothermal-compressibility" text="isothermal compressibility" >}}.

- **Fluctuation formula (statistical mechanics):** In the canonical description at fixed $T$, $V$, and $N$, $C_V$ can be written in terms of the {{< knowl id="variance" section="probability" text="variance" >}} of the energy as a random variable:
  $$
  C_V = \frac{1}{k_B T^2}\left(\langle E^2\rangle - \langle E\rangle^2\right),
  $$

  where $k_B$ is the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}} and $\langle\cdot\rangle$ denotes the ensemble {{< knowl id="expectation" section="probability" text="expectation" >}}.
