+++
id = "thermodynamics/energy-density"
title = "Energy density"
kind = "knowl"
summary = "Internal energy per volume, u = U/V, useful for continuum descriptions and density-based thermodynamic relations."
aliases = ["energy-density", "Energy density"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/energy-density.md"
+++

The **energy density** is the [[thermodynamics/internal-energy-thermo|internal energy]] per [[thermodynamics/volume-thermo|volume]]. It is an intensive “per-volume” form of energy that is especially natural in continuum and local-equilibrium settings.

For a homogeneous system with internal energy $U$ and volume $V$, the **energy density** is
$$
u \equiv \frac{U}{V}.
$$

Equivalently, $U = uV$ in a homogeneous equilibrium state.

When the system is not homogeneous, one often considers a local field $u(\mathbf{r})$ whose volume integral gives the total energy.

## Physical interpretation
Energy density measures how much internal energy is stored in a unit volume of material. It is a [[thermodynamics/specific-quantity|specific quantity]] (per volume), and—like other densities—remains unchanged if you scale the system size at fixed bulk state, consistent with the [[thermodynamics/thermodynamic-limit|thermodynamic limit]].

## Key relations (one-component simple system)
Energy density becomes particularly transparent when paired with [[thermodynamics/entropy-density|entropy density]] and [[thermodynamics/number-density|number density]]. Define $s=S/V$ and $n=N/V$. Then extensivity of $U$ (via the [[thermodynamics/euler-relation-thermodynamics|Euler relation]]) implies the per-volume Euler form
$$
u = Ts - p + \mu n,
$$

with $T$, $p$, and $\mu$ the conjugate [[thermodynamics/intensive-variable|intensive variables]] ([[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], [[thermodynamics/chemical-potential-thermo|chemical potential]]). Rearranging gives a useful identity for pressure in density variables:
$$
p = Ts + \mu n - u.
$$

Moreover, treating $u$ as a function of $(s,n)$ gives the differential (“Gibbs”) form
$$
du = T\,ds + \mu\,dn,
$$
which is the density version of the [[thermodynamics/first-law-thermodynamics|first law]] for homogeneous matter expressed in natural variables.
