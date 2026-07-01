+++
id = "thermodynamics/specific-quantity"
title = "Specific quantity"
kind = "knowl"
summary = "An intensive quantity formed by dividing an extensive variable by an extensive reference amount (mass, particle number, or volume)."
aliases = ["specific-quantity", "Specific quantity"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/specific-quantity.md"
+++

A **specific quantity** is a “per-unit-amount” version of an [[thermodynamics/extensive-variable|extensive variable]]. Dividing by an appropriate extensive reference makes the result independent of system size (for homogeneous systems), so specific quantities are typically [[thermodynamics/intensive-variable|intensive]].

Let $X$ be an [[thermodynamics/extensive-variable|extensive variable]] and let $Y>0$ be an extensive reference measure of system size (commonly mass $m$, [[thermodynamics/particle-number|particle number]] $N$, or [[thermodynamics/volume-thermo|volume]] $V$). The **specific quantity of $X$ per $Y$** is
$$
x \equiv \frac{X}{Y}.
$$

When the system is homogeneous (no macroscopic gradients), scaling the system by a factor $\lambda$ multiplies both $X$ and $Y$ by $\lambda$, so the ratio $x$ is unchanged; this is why $x$ behaves as an [[thermodynamics/intensive-variable|intensive variable]].

## Physical interpretation
Specific quantities encode material properties “per unit amount,” which is often what experiments control or what constitutive laws use. For example, energy per particle compares energetic content to the number of particles present, while energy per volume compares energetic content to occupied space.

## Common thermodynamic examples
- **Per particle:** $U/N$ (specific internal energy per particle), $S/N$ (entropy per particle).
- **Per volume (densities):** [[thermodynamics/number-density|number density]] $N/V$, [[thermodynamics/energy-density|energy density]] $U/V$, [[thermodynamics/entropy-density|entropy density]] $S/V$.
- **Per mass (common engineering usage):** $U/m$, $S/m$, and the specific volume $V/m$.

## Key property: weighted averaging under composition
If a system is partitioned into two parts $A$ and $B$ with the same definition of $x=X/Y$, then
$$
x_{\text{tot}}=\frac{X_A+X_B}{Y_A+Y_B}
= \frac{Y_A}{Y_A+Y_B}\,x_A+\frac{Y_B}{Y_A+Y_B}\,x_B.
$$

So a specific quantity is an average of subsystem values weighted by the reference amount $Y$.
