---
title: "Energy density"
description: "Internal energy per volume, u = U/V, useful for continuum descriptions and density-based thermodynamic relations."
---

The **energy density** is the {{< knowl id="internal-energy-thermo" text="internal energy" >}} per {{< knowl id="volume-thermo" text="volume" >}}. It is an intensive “per-volume” form of energy that is especially natural in continuum and local-equilibrium settings.

For a homogeneous system with internal energy $U$ and volume $V$, the **energy density** is
$$
u \equiv \frac{U}{V}.
$$

Equivalently, $U = uV$ in a homogeneous equilibrium state.

When the system is not homogeneous, one often considers a local field $u(\mathbf{r})$ whose volume integral gives the total energy.

## Physical interpretation
Energy density measures how much internal energy is stored in a unit volume of material. It is a {{< knowl id="specific-quantity" text="specific quantity" >}} (per volume), and—like other densities—remains unchanged if you scale the system size at fixed bulk state, consistent with the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}}.

## Key relations (one-component simple system)
Energy density becomes particularly transparent when paired with {{< knowl id="entropy-density" text="entropy density" >}} and {{< knowl id="number-density" text="number density" >}}. Define $s=S/V$ and $n=N/V$. Then extensivity of $U$ (via the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}}) implies the per-volume Euler form
$$
u = Ts - p + \mu n,
$$

with $T$, $p$, and $\mu$ the conjugate {{< knowl id="intensive-variable" text="intensive variables" >}} ({{< knowl id="temperature-thermo" text="temperature" >}}, {{< knowl id="pressure-thermo" text="pressure" >}}, {{< knowl id="chemical-potential-thermo" text="chemical potential" >}}). Rearranging gives a useful identity for pressure in density variables:
$$
p = Ts + \mu n - u.
$$

Moreover, treating $u$ as a function of $(s,n)$ gives the differential (“Gibbs”) form
$$
du = T\,ds + \mu\,dn,
$$
which is the density version of the {{< knowl id="first-law-thermodynamics" text="first law" >}} for homogeneous matter expressed in natural variables.
