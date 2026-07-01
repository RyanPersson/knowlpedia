+++
id = "stat-mech/quantum-harmonic-oscillator-example"
title = "Quantum harmonic oscillator in thermal equilibrium"
kind = "knowl"
summary = "Exact Gibbs-state partition function, energy, entropy, and heat capacity for the quantum harmonic oscillator; classical and low-temperature limits."
aliases = ["quantum-harmonic-oscillator-example", "Quantum harmonic oscillator in thermal equilibrium"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/quantum-harmonic-oscillator-example.md"
+++

## Model and Gibbs state
Let $H$ be the quantum harmonic oscillator Hamiltonian with spectrum
$$
E_n=\hbar\omega\left(n+\frac12\right),\qquad n=0,1,2,\dots
$$

Thermal equilibrium at inverse temperature $\beta$ is described by the [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs state]]
$$
\rho_\beta = \frac{e^{-\beta H}}{Z(\beta)},
$$
a [[quantum-foundations/density-operator|density operator]].

## Quantum partition function
The [[stat-mech-quantum/quantum-partition-function|quantum partition function]] is the geometric series
$$
Z(\beta)=\sum_{n=0}^\infty e^{-\beta E_n}
=\sum_{n=0}^\infty e^{-\beta\hbar\omega(n+1/2)}
=\frac{e^{-\beta\hbar\omega/2}}{1-e^{-\beta\hbar\omega}}
=\frac{1}{2\sinh(\beta\hbar\omega/2)}.
$$

## Free energy, mean energy, and heat capacity
The free energy (compare [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]]) is
$$
F(\beta)=-\beta^{-1}\ln Z(\beta)
=\frac{\hbar\omega}{2}+\beta^{-1}\ln\!\bigl(1-e^{-\beta\hbar\omega}\bigr).
$$
The mean energy is
$$
U(\beta)=-\frac{\partial}{\partial\beta}\ln Z(\beta)
=\frac{\hbar\omega}{2}+\frac{\hbar\omega}{e^{\beta\hbar\omega}-1}.
$$
It is often convenient to introduce the Bose occupation number
$$
\bar n(\beta)=\frac{1}{e^{\beta\hbar\omega}-1},
\qquad\text{so that}\qquad
U=\hbar\omega\left(\bar n+\frac12\right).
$$
The heat capacity at constant volume (see [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]]) is
$$
C_V=\frac{\partial U}{\partial T}
= k_B(\beta\hbar\omega)^2\,\frac{e^{\beta\hbar\omega}}{(e^{\beta\hbar\omega}-1)^2}.
$$

## Entropy
The thermodynamic entropy can be computed as the [[quantum-foundations/von-neumann-entropy|von Neumann entropy]]
$$
S(\beta)=-k_B\,\mathrm{Tr}(\rho_\beta\ln\rho_\beta).
$$
For a single oscillator this evaluates to the standard bosonic form
$$
S(\beta)=k_B\Bigl[(\bar n+1)\ln(\bar n+1)-\bar n\ln \bar n\Bigr],
$$

and it also agrees with the canonical identity $S=k_B(\ln Z+\beta U)$.

## Classical and low-temperature limits
- High-temperature limit $\beta\hbar\omega\ll 1$:
  $$
  Z(\beta)\sim \frac{1}{\beta\hbar\omega},\qquad
  U(\beta)\sim k_B T,\qquad
  C_V\sim k_B,
  $$
  matching the [[stat-mech/classical-harmonic-oscillator-example|classical harmonic oscillator]].

- Low-temperature limit $\beta\hbar\omega\gg 1$:
  $$
  U(\beta)\to \frac{\hbar\omega}{2},\qquad
  C_V \sim k_B(\beta\hbar\omega)^2 e^{-\beta\hbar\omega},
  $$
  showing exponential suppression of thermal excitations.
