+++
id = "stat-mech/two-level-system-paramagnet"
title = "Example: two-level paramagnet (noninteracting spins)"
kind = "knowl"
summary = "Canonical solution for N independent two-level magnetic moments in a field: partition function, magnetization, Curie law, energy, and heat capacity."
aliases = ["two-level-system-paramagnet", "Example: two-level paramagnet (noninteracting spins)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/two-level-system-paramagnet.md"
+++

Consider $N$ independent spins (or magnetic moments) in a uniform magnetic field $B$. Each spin has two energy levels
$$
E_\pm = \mp \mu B,
$$
so the system is a canonical-ensemble model (see [[stat-mech/canonical-ensemble|canonical ensemble]]) with a simple discrete spectrum.

## Partition function
For inverse temperature $\beta=1/(k_B T)$ (with $T$ the [[thermodynamics/temperature-thermo|temperature]]), the single-spin partition function is
$$
z(\beta,B)=e^{\beta\mu B}+e^{-\beta\mu B}=2\cosh(\beta\mu B),
$$

hence the $N$-spin [[stat-mech/partition-function-canonical|canonical partition function]] is
$$
Z(\beta,B)=z(\beta,B)^N=\big(2\cosh(\beta\mu B)\big)^N.
$$

## Free energy and magnetization
The [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] is
$$
F(T,B)=-Nk_B T\log\!\big(2\cosh(\beta\mu B)\big).
$$

The magnetization is the field derivative of $F$:
$$
M = -\left(\frac{\partial F}{\partial B}\right)_T = N\mu\,\tanh(\beta\mu B).
$$

The susceptibility is
$$
\chi=\left(\frac{\partial M}{\partial B}\right)_T
= N\beta\mu^2\,\mathrm{sech}^2(\beta\mu B),
$$

and for high temperature (small $\beta\mu B$) this gives **Curie’s law**
$$
\chi \approx \frac{N\mu^2}{k_B T}.
$$

## Energy, heat capacity, entropy
The [[thermodynamics/internal-energy-thermo|internal energy]] is
$$
U = -\frac{\partial}{\partial\beta}\log Z = -N\mu B\,\tanh(\beta\mu B).
$$

Differentiating in $T$ gives the heat capacity at fixed $B$:
$$
C = \left(\frac{\partial U}{\partial T}\right)_B
= N k_B(\beta\mu B)^2\,\mathrm{sech}^2(\beta\mu B).
$$
The [[thermodynamics/thermodynamic-entropy|entropy]] can be written as
$$
S = -\left(\frac{\partial F}{\partial T}\right)_B
= N k_B\Big[\log\!\big(2\cosh x\big)-x\tanh x\Big],
\qquad x=\beta\mu B.
$$

Prerequisites: [[stat-mech/canonical-ensemble|canonical ensemble]], [[stat-mech/partition-function-canonical|partition function]], [[stat-mech/ensemble-average|ensemble averages]], and [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]].
