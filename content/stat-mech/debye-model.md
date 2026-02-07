---
title: "Debye model"
description: "Phonon continuum approximation with a Debye cutoff; produces the low-temperature heat capacity law and the high-temperature Dulong–Petit limit."
---

## Physical setup
The Debye model treats lattice vibrations as a continuum of quantized normal modes (phonons) with approximately linear dispersion $\omega\approx v_s|k|$ at small $|k|$ in three dimensions.
Instead of $3N$ identical modes as in the {{< knowl id="einstein-solid" text="Einstein solid" >}}, one uses a distribution of frequencies up to a cutoff $\omega_D$ chosen so that the total number of modes is $3N$.

Thermodynamic quantities are computed in the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} at temperature $T$.

## Debye density of states
In the isotropic 3D Debye approximation, the vibrational density of states is taken as
$$
g(\omega)=\frac{9N}{\omega_D^3}\,\omega^2,\qquad 0\le \omega\le \omega_D,
$$

and $g(\omega)=0$ for $\omega>\omega_D$.

Define the Debye temperature
$$
\Theta_D=\frac{\hbar\omega_D}{k_B}.
$$

## Internal energy and free energy
For each mode of frequency $\omega$, the mean energy is that of a {{< knowl id="quantum-harmonic-oscillator-example" text="quantum harmonic oscillator" >}}:
$$
u_\omega(T)=\frac{\hbar\omega}{2}+\frac{\hbar\omega}{e^{\beta\hbar\omega}-1}.
$$
Thus
$$
U(T)=\int_0^{\omega_D} g(\omega)\,u_\omega(T)\,d\omega.
$$

The zero-point contribution $\frac12\int_0^{\omega_D} g(\omega)\hbar\omega\,d\omega$ is independent of $T$ and does not affect $C_V$.

A convenient free-energy representation (up to an additive zero-point constant) is
$$
F(T)=k_B T \int_0^{\omega_D} g(\omega)\,\ln\!\bigl(1-e^{-\beta\hbar\omega}\bigr)\,d\omega.
$$

## Heat capacity formula
Differentiating $U(T)$ gives the Debye heat capacity (see {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="heat capacity at constant volume" >}}):
$$
C_V(T)=9N k_B\left(\frac{T}{\Theta_D}\right)^3
\int_0^{\Theta_D/T} \frac{x^4 e^x}{(e^x-1)^2}\,dx,
\qquad x=\beta\hbar\omega.
$$

## Low- and high-temperature limits
- Low temperature $T\ll \Theta_D$ (upper limit $\Theta_D/T\to\infty$):
  $$
  \int_0^\infty \frac{x^4 e^x}{(e^x-1)^2}\,dx=\frac{4\pi^4}{15},
  $$
  hence
  $$
  C_V(T)\sim \frac{12\pi^4}{5}N k_B\left(\frac{T}{\Theta_D}\right)^3,
  $$

  giving the $T^3$ law.

- High temperature $T\gg \Theta_D$:
  $$
  C_V(T)\to 3N k_B,
  $$
  recovering the Dulong–Petit limit (also captured by {{< knowl id="einstein-solid" text="Einstein solid" >}}).

## Conceptual takeaway
Relative to the Einstein model, the key change is the abundance of low-frequency modes (the $\omega^2$ density of states), which produces a power-law rather than exponential suppression of thermal excitations at low $T$.
