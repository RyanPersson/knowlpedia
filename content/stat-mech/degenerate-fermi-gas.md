---
title: "Degenerate Fermi gas (ideal Fermi gas at low temperature)"
description: "Ground-state thermodynamics and low-temperature expansions of the ideal Fermi gas: Fermi energy, pressure, and heat capacity."
---

## Example: ideal Fermi gas in $d=3$

Consider $N$ noninteracting spin-$1/2$ fermions of mass $m$ in volume $V$ at number density $n=N/V$. The system is naturally treated in the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}; at low temperature it is “degenerate,” meaning $T\ll T_F$ (defined below).

### Zero-temperature (ground-state) formulas

The Fermi momentum and Fermi energy are
$$
k_F=(3\pi^2 n)^{1/3}, \qquad \varepsilon_F=\frac{\hbar^2 k_F^2}{2m}
=\frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}.
$$

Define the Fermi temperature $T_F=\varepsilon_F/k_B$.

At $T=0$ (filled Fermi sea),
$$
\frac{U_0}{N}=\frac{3}{5}\varepsilon_F,
\qquad
P_0=\frac{2}{5}n\,\varepsilon_F.
$$

This finite pressure at $T=0$ is the “degeneracy pressure.”

### Low-temperature corrections (Sommerfeld behavior)

For $T\ll T_F$, the leading temperature corrections are quadratic in $T$:
$$
\frac{U}{N}=\frac{3}{5}\varepsilon_F\left[1+\frac{5\pi^2}{12}\left(\frac{T}{T_F}\right)^2+o\!\left(\frac{T}{T_F}\right)^2\right],
$$

and the constant-volume heat capacity is linear in $T$:
$$
C_V \sim \frac{\pi^2}{2}N k_B \frac{T}{T_F}.
$$

### Thermodynamic interpretation

- The {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}} and {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} follow from derivatives of the {{< knowl id="pressure-log-partition-density" text="pressure (log-partition density)" >}} / free energy density in the thermodynamic limit.
- The low-$T$ linear behavior of {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="$C_V$" >}} is a characteristic signature of Fermi statistics.

### Prerequisites / cross-links

- {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}, {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}
- {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}, {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}
