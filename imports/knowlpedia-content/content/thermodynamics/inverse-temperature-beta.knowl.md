+++
id = "thermodynamics/inverse-temperature-beta"
title = "Inverse temperature β"
kind = "knowl"
summary = "The parameter conjugate to energy; central in canonical and grand-canonical equilibrium formulas."
aliases = ["inverse-temperature-beta", "Inverse temperature β"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/inverse-temperature-beta.md"
+++

## Definition (and physical meaning)

The **inverse temperature** $\beta$ is defined by
$$
\beta \equiv \frac{1}{k_B T},
$$

where $T$ is [[thermodynamics/temperature-thermo|temperature]] and $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]].

**Physical interpretation:** $\beta$ measures “how costly energy is” in equilibrium. Large $\beta$ corresponds to low temperature, meaning high-energy configurations are strongly suppressed; small $\beta$ corresponds to high temperature, meaning energy differences are comparatively less important.

## Thermodynamic meaning

From the thermodynamic definition of temperature in the entropy representation,
$$
\left(\frac{\partial S}{\partial E}\right)_{V,N} = \frac{1}{T},
$$
it follows immediately that
$$
\beta = \left(\frac{\partial}{\partial E}\frac{S}{k_B}\right)_{V,N}.
$$

Thus $\beta$ is the derivative of the **dimensionless entropy** $S/k_B$ with respect to [[thermodynamics/internal-energy-thermo|internal energy]] at fixed [[thermodynamics/volume-thermo|volume]] and [[thermodynamics/particle-number|particle number]].

Equality of $\beta$ across subsystems is the equilibrium condition for energy exchange, i.e. [[thermodynamics/thermal-equilibrium|thermal equilibrium]] in the [[thermodynamics/zeroth-law-thermodynamics|zeroth law]] sense.

## Canonical-ensemble role

In the [[thermodynamics/canonical-ensemble-convention|canonical ensemble convention]], equilibrium weights take the form
$$
p_i = \frac{e^{-\beta E_i}}{Z(\beta)},
$$

where $E_i$ are microstate energies and $Z(\beta)$ is the partition function.

The [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] can be expressed in terms of $Z$ by
$$
F = -k_B T \ln Z(\beta).
$$

Writing thermodynamic relations in terms of $\beta$ often makes the underlying convex/dual structure explicit; for example, passing between entropy and free energy is a [[convex-analysis/legendre-transform|Legendre transform]] between conjugate variables (energy versus temperature/inverse temperature).

## Common convention: natural units

Under the [[thermodynamics/natural-units-convention|natural units convention]] with $k_B=1$, the definition reduces to $\beta=1/T$, and entropies are treated as dimensionless.
