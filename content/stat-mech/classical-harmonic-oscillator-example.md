---
title: "Classical harmonic oscillator in the canonical ensemble"
description: "Phase-space partition function and thermodynamics of a classical harmonic oscillator; a standard illustration of equipartition."
---

## Model
Consider a one-dimensional classical harmonic oscillator with coordinate $q\in\mathbb{R}$ and momentum $p\in\mathbb{R}$,
with Hamiltonian
$$
H(p,q)=\frac{p^2}{2m}+\frac12 m\omega^2 q^2 .
$$

We place the system in the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} at inverse temperature $\beta=1/(k_B T)$.

## Canonical partition function
Using the classical phase-space definition of the {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}},
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
The {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} is
$$
F(\beta)=-\beta^{-1}\ln Z_1(\beta)=k_B T\,\ln(\beta\hbar\omega).
$$
The {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} is
$$
U(\beta)=-\frac{\partial}{\partial\beta}\ln Z_1(\beta)=\frac{1}{\beta}=k_B T .
$$

The {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} (canonical identity $S=k_B(\ln Z+\beta U)$) is
$$
S(\beta)=k_B\bigl(\ln Z_1(\beta)+\beta U(\beta)\bigr)=k_B\Bigl(1-\ln(\beta\hbar\omega)\Bigr).
$$
The heat capacity at constant volume (see {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="heat capacity at constant volume" >}}) is
$$
C_V=\left(\frac{\partial U}{\partial T}\right)=k_B .
$$

## Equipartition and basic averages
As {{< knowl id="ensemble-average" section="stat-mech" text="ensemble averages" >}} under the canonical Gibbs density, equipartition yields
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
