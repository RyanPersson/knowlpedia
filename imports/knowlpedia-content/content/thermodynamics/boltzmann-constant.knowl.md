+++
id = "thermodynamics/boltzmann-constant"
title = "Boltzmann constant"
kind = "knowl"
summary = "Physical constant that converts between temperature and energy scales and between dimensionless and thermodynamic entropy."
aliases = ["boltzmann-constant", "Boltzmann constant"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/boltzmann-constant.md"
+++

## Definition (and physical meaning)

The **Boltzmann constant** $k_B$ is the proportionality constant that links thermal energy scales to [[thermodynamics/temperature-thermo|temperature]] and converts between a dimensionless entropy (a logarithm of a count or probability) and the thermodynamic [[thermodynamics/thermodynamic-entropy|entropy]] measured in J/K.

In SI units,
$$
k_B = 1.380649\times 10^{-23}\ \mathrm{J\,K^{-1}},
$$
with this numerical value fixed by the SI definition of the kelvin.

**Physical interpretation:** $k_B T$ sets the characteristic energy scale of thermal fluctuations at temperature $T$. Whenever you see $k_B T$ in a formula, it is marking the “typical” thermal energy available per microscopic degree of freedom.

## Core appearances in thermodynamics and statistical mechanics

- **Temperature as an energy scale.** In equilibrium statistical mechanics, the inverse-temperature parameter is defined by
  $$
  \beta=\frac{1}{k_B T},
  $$

  where $\beta$ is the [[thermodynamics/inverse-temperature-beta|inverse temperature]].

- **Entropy as a logarithm times $k_B$.** If $\Omega$ counts compatible microstates (in an appropriate coarse-grained sense), the thermodynamic entropy is often written as
  $$
  S = k_B \ln \Omega.
  $$

  More generally, $S/k_B$ is a natural dimensionless entropy, comparable in form to [[probability/shannon-entropy|Shannon entropy]] when probabilities are used.

- **Thermodynamic derivatives.** Since $\partial S/\partial E = 1/T$, one can equivalently write
  $$
  \frac{\partial}{\partial E}\left(\frac{S}{k_B}\right)=\beta,
  $$

  connecting $k_B$ directly to the thermodynamic definition of temperature.

## Conventions and unit choices

Many formulas simplify under the [[thermodynamics/natural-units-convention|natural units convention]] where $k_B=1$. In that convention, temperature has units of energy, $\beta=1/T$, and entropy is treated as dimensionless. If you also adopt a fixed logarithm convention (often [[thermodynamics/logarithm-convention-natural|natural logarithms]]), then restoring SI units amounts to re-inserting the appropriate factors of $k_B$.
