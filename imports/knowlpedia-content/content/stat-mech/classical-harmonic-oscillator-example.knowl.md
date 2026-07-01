+++
id = "stat-mech/classical-harmonic-oscillator-example"
title = "Classical harmonic oscillator in the canonical ensemble"
kind = "knowl"
summary = "Phase-space partition function and thermodynamics of a classical harmonic oscillator; a standard illustration of equipartition."
aliases = ["classical-harmonic-oscillator-example", "Classical harmonic oscillator in the canonical ensemble"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/classical-harmonic-oscillator-example.md"
+++

## Model
Consider a one-dimensional classical harmonic oscillator with coordinate $q\in\mathbb{R}$ and momentum $p\in\mathbb{R}$,
with Hamiltonian
$$
H(p,q)=\frac{p^2}{2m}+\frac12 m\omega^2 q^2 .
$$

We place the system in the [[stat-mech/canonical-ensemble|canonical ensemble]] at inverse temperature $\beta=1/(k_B T)$.

## Canonical partition function
Using the classical phase-space definition of the [[stat-mech/partition-function-canonical|canonical partition function]],
with the usual $1/h$ normalization,
$$
Z_1(\beta)=\frac{1}{h}\int_{\mathbb{R}}\int_{\mathbb{R}} e^{-\beta H(p,q)}\,dp\,dq .
$$
The Gaussian integrals factor:
$$
\int_{\mathbb{R}} e^{-\beta p^2/(2m)}\,dp=\sqrt{\frac{2\pi m}{\beta}},\qquad
\int_{\mathbb{R}} e^{-\beta m\omega^2 q^2/2}\,dq=\sqrt{\frac{2\pi}{\beta m\omega^2}}.
$$
Hence
$$
Z_1(\beta)=\frac{1}{h}\,\frac{2\pi}{\beta\omega}=\frac{1}{\beta\hbar\omega},
$$

using $h=2\pi\hbar$. (Changing the phase-space normalization shifts $F$ and $S$ by constants, but does not change $U$ or $C_V$.)

## Thermodynamic functions
The [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] is
$$
F(\beta)=-\beta^{-1}\ln Z_1(\beta)=k_B T\,\ln(\beta\hbar\omega).
$$
The [[thermodynamics/internal-energy-thermo|internal energy]] is
$$
U(\beta)=-\frac{\partial}{\partial\beta}\ln Z_1(\beta)=\frac{1}{\beta}=k_B T .
$$

The [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] (canonical identity $S=k_B(\ln Z+\beta U)$) is
$$
S(\beta)=k_B\bigl(\ln Z_1(\beta)+\beta U(\beta)\bigr)=k_B\Bigl(1-\ln(\beta\hbar\omega)\Bigr).
$$
The heat capacity at constant volume (see [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]]) is
$$
C_V=\left(\frac{\partial U}{\partial T}\right)=k_B .
$$

## Equipartition and basic averages
As [[stat-mech/ensemble-average|ensemble averages]] under the canonical Gibbs density, equipartition yields
$$
\Bigl\langle \frac{p^2}{2m}\Bigr\rangle=\frac12 k_B T,\qquad
\Bigl\langle \frac12 m\omega^2 q^2\Bigr\rangle=\frac12 k_B T,
$$
so
$$
\langle p^2\rangle = m k_B T,\qquad
\langle q^2\rangle = \frac{k_B T}{m\omega^2}.
$$

## Many independent oscillators
For $N$ independent (distinguishable) classical oscillators of the same frequency,
$$
Z_N(\beta)=\bigl(Z_1(\beta)\bigr)^N,\qquad
U_N = N k_B T,\qquad
C_V = N k_B.
$$
