+++
id = "stat-mech/bose-einstein-condensation"
title = "Bose–Einstein condensation (ideal Bose gas)"
kind = "knowl"
summary = "Ideal-gas Bose–Einstein condensation: critical temperature, condensate fraction, and thermodynamic signatures."
aliases = ["bose-einstein-condensation", "Bose–Einstein condensation (ideal Bose gas)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/bose-einstein-condensation.md"
+++

## Example: ideal Bose gas in $d=3$

Consider $N$ noninteracting bosons of mass $m$ in a cubic box of volume $V$ (periodic boundary conditions). Thermodynamic behavior is described via the [[stat-mech/canonical-ensemble|canonical ensemble]] (or, equivalently for this system, a grand-canonical viewpoint).

### Key scales and formulas

Define the thermal de Broglie wavelength
$$
\lambda_T=\sqrt{\frac{2\pi \hbar^2}{m k_B T}} .
$$

For the ideal Bose gas, the excited-state density saturates as the fugacity approaches $1$:
$$
n_{\mathrm{ex}}(T)=\frac{1}{\lambda_T^3}\,\zeta\!\left(\frac{3}{2}\right),
\qquad n=\frac{N}{V}.
$$

Hence the critical temperature $T_c$ is determined by $n=n_{\mathrm{ex}}(T_c)$:
$$
T_c=\frac{2\pi \hbar^2}{m k_B}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}.
$$

For $T<T_c$, a macroscopic fraction occupies the one-particle ground state (the condensate):
$$
\frac{N_0}{N}=1-\left(\frac{T}{T_c}\right)^{3/2},
\qquad (T<T_c).
$$

### Thermodynamic consequences

- The [[stat-mech/pressure-log-partition-density|pressure (log-partition density)]] for the ideal Bose gas becomes independent of density below $T_c$ (extra particles go into the condensate rather than increasing pressure).
- The internal energy is carried by excited modes, giving $U\propto V T^{5/2}$ for $T<T_c$, so the [[thermodynamics/heat-capacity-constant-volume|$C_V$]] scales like $V T^{3/2}$ in the condensed phase.
- The transition can be diagnosed through standard [[stat-mech-lattice/tfae-phase-transition-indicators|phase transition indicators]] (non-analyticity in thermodynamic potentials in the thermodynamic limit).

### Prerequisites / cross-links

- [[stat-mech/partition-function-canonical|canonical partition function]], [[stat-mech/free-energy-statistical|statistical free energy]], [[stat-mech/ensemble-average|ensemble averages]]
- [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]]
- [[thermodynamics/pressure-thermo|pressure]]
