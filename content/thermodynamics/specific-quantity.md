---
title: "Specific quantity"
description: "An intensive quantity formed by dividing an extensive variable by an extensive reference amount (mass, particle number, or volume)."
---

A **specific quantity** is a “per-unit-amount” version of an {{< knowl id="extensive-variable" text="extensive variable" >}}. Dividing by an appropriate extensive reference makes the result independent of system size (for homogeneous systems), so specific quantities are typically {{< knowl id="intensive-variable" text="intensive" >}}.

Let $X$ be an {{< knowl id="extensive-variable" text="extensive variable" >}} and let $Y>0$ be an extensive reference measure of system size (commonly mass $m$, {{< knowl id="particle-number" text="particle number" >}} $N$, or {{< knowl id="volume-thermo" text="volume" >}} $V$). The **specific quantity of $X$ per $Y$** is
$$
x \equiv \frac{X}{Y}.
$$

When the system is homogeneous (no macroscopic gradients), scaling the system by a factor $\lambda$ multiplies both $X$ and $Y$ by $\lambda$, so the ratio $x$ is unchanged; this is why $x$ behaves as an {{< knowl id="intensive-variable" text="intensive variable" >}}.

## Physical interpretation
Specific quantities encode material properties “per unit amount,” which is often what experiments control or what constitutive laws use. For example, energy per particle compares energetic content to the number of particles present, while energy per volume compares energetic content to occupied space.

## Common thermodynamic examples
- **Per particle:** $U/N$ (specific internal energy per particle), $S/N$ (entropy per particle).
- **Per volume (densities):** {{< knowl id="number-density" text="number density" >}} $N/V$, {{< knowl id="energy-density" text="energy density" >}} $U/V$, {{< knowl id="entropy-density" text="entropy density" >}} $S/V$.
- **Per mass (common engineering usage):** $U/m$, $S/m$, and the specific volume $V/m$.

## Key property: weighted averaging under composition
If a system is partitioned into two parts $A$ and $B$ with the same definition of $x=X/Y$, then
$$
x_{\text{tot}}=\frac{X_A+X_B}{Y_A+Y_B}
= \frac{Y_A}{Y_A+Y_B}\,x_A+\frac{Y_B}{Y_A+Y_B}\,x_B.
$$

So a specific quantity is an average of subsystem values weighted by the reference amount $Y$.
