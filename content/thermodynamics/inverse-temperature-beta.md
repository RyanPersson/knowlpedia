---
title: "Inverse temperature β"
description: "The parameter conjugate to energy; central in canonical and grand-canonical equilibrium formulas."
---

## Definition (and physical meaning)

The **inverse temperature** $\beta$ is defined by
$$
\beta \equiv \frac{1}{k_B T},
$$

where $T$ is {{< knowl id="temperature-thermo" text="temperature" >}} and $k_B$ is the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}}.

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

Thus $\beta$ is the derivative of the **dimensionless entropy** $S/k_B$ with respect to {{< knowl id="internal-energy-thermo" text="internal energy" >}} at fixed {{< knowl id="volume-thermo" text="volume" >}} and {{< knowl id="particle-number" text="particle number" >}}.

Equality of $\beta$ across subsystems is the equilibrium condition for energy exchange, i.e. {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}} in the {{< knowl id="zeroth-law-thermodynamics" text="zeroth law" >}} sense.

## Canonical-ensemble role

In the {{< knowl id="canonical-ensemble-convention" text="canonical ensemble convention" >}}, equilibrium weights take the form
$$
p_i = \frac{e^{-\beta E_i}}{Z(\beta)},
$$

where $E_i$ are microstate energies and $Z(\beta)$ is the partition function.

The {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} can be expressed in terms of $Z$ by
$$
F = -k_B T \ln Z(\beta).
$$

Writing thermodynamic relations in terms of $\beta$ often makes the underlying convex/dual structure explicit; for example, passing between entropy and free energy is a {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} between conjugate variables (energy versus temperature/inverse temperature).

## Common convention: natural units

Under the {{< knowl id="natural-units-convention" text="natural units convention" >}} with $k_B=1$, the definition reduces to $\beta=1/T$, and entropies are treated as dimensionless.
