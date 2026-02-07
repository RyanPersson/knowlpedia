---
title: "Heat capacity at constant pressure"
description: "A response function measuring how enthalpy changes with temperature when pressure (and composition) are held fixed."
---

For a simple {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} in {{< knowl id="thermodynamic-equilibrium" text="equilibrium" >}}, the **heat capacity at constant pressure** is a {{< knowl id="response-function-thermo" text="response function" >}}
that quantifies how much the system’s energy-like content must change to raise the {{< knowl id="temperature-thermo" text="temperature" >}} while keeping the {{< knowl id="pressure-thermo" text="pressure" >}} fixed (and keeping composition fixed, e.g. fixed {{< knowl id="particle-number" text="particle number" >}} $N$).

It is defined by the partial derivative
$$
C_P \equiv \left(\frac{\partial H}{\partial T}\right)_{p,N},
$$

where $H$ is the {{< knowl id="enthalpy" text="enthalpy" >}},
$$
H \equiv U + pV,
$$

with $U$ the {{< knowl id="internal-energy-thermo" text="internal energy" >}} and $V$ the {{< knowl id="volume-thermo" text="volume" >}}.

Using the standard differential for $H$ for a simple compressible system, at fixed $p$ and $N$ one has $dH = T\,dS$, so an equivalent form is
$$
C_P
= T\left(\frac{\partial S}{\partial T}\right)_{p,N},
$$
in terms of the {{< knowl id="thermodynamic-entropy" text="entropy" >}}.

## Physical interpretation
Along a {{< knowl id="quasistatic-process" text="quasistatic" >}}, {{< knowl id="reversible-process" text="reversible" >}} process at fixed pressure,
$$
\delta Q_{\rm rev} = C_P\,dT.
$$

Compared with heating at fixed volume (see {{< knowl id="heat-capacity-constant-volume" text="constant-volume heat capacity" >}}), maintaining constant pressure generally allows the system to expand as it warms. Part of the supplied heat is then “spent” on the $p\,dV$ expansion, which is why $C_P$ is typically larger than $C_V$ in stable single-phase regions.

## Key relations and properties
- **Extensivity:** $C_P$ is typically {{< knowl id="extensive-variable" text="extensive" >}}; one often uses a {{< knowl id="specific-quantity" text="specific" >}} form such as $c_P = C_P/N$ (or per unit mass).

- **Gibbs free-energy curvature:** In terms of the {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}} $G(T,p,N)$, one has
  $$
  C_P = -\,T\left(\frac{\partial^2 G}{\partial T^2}\right)_{p,N}.
  $$

- **Difference from $C_V$:** For a simple compressible system,
  $$
  C_P - C_V = \frac{T\,V\,\alpha^2}{\kappa_T},
  $$

  involving the {{< knowl id="thermal-expansion-coefficient" text="thermal expansion coefficient" >}} $\alpha$ and the {{< knowl id="isothermal-compressibility" text="isothermal compressibility" >}} $\kappa_T$.

- **Inequality (typical):** In stable single-phase regions with $\kappa_T>0$, one usually has $C_P \ge C_V$, consistent with {{< knowl id="thermodynamic-stability" text="stability" >}}.

- **Fluctuation formula (statistical mechanics):** In the isothermal–isobaric description (fixed $T$, $p$, $N$), $C_P$ is proportional to the {{< knowl id="variance" section="probability" text="variance" >}} of the enthalpy as a random variable:
  $$
  C_P = \frac{1}{k_B T^2}\left(\langle H^2\rangle - \langle H\rangle^2\right),
  $$

  where $k_B$ is the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}} and $\langle\cdot\rangle$ is an ensemble {{< knowl id="expectation" section="probability" text="expectation" >}}.
