---
title: "Einstein solid"
description: "Crystal model of independent identical quantum oscillators; yields an explicit heat capacity curve with the Dulong–Petit high-temperature limit."
---

## Model
The Einstein solid models a crystal of $N$ atoms as $3N$ independent quantum harmonic oscillators, all with the same frequency $\omega_E$ (three vibrational modes per atom).
Thermal equilibrium is taken in the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} at temperature $T$.

This is essentially the {{< knowl id="quantum-harmonic-oscillator-example" text="quantum harmonic oscillator" >}} replicated $3N$ times.

## Partition function
Let $Z_{\mathrm{osc}}(\beta)$ be the single-oscillator partition function:
$$
Z_{\mathrm{osc}}(\beta)=\frac{e^{-\beta\hbar\omega_E/2}}{1-e^{-\beta\hbar\omega_E}}.
$$
Independence gives
$$
Z_N(\beta)=\bigl(Z_{\mathrm{osc}}(\beta)\bigr)^{3N}.
$$

## Free energy, internal energy, and entropy
The {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} is
$$
F(\beta)=-\beta^{-1}\ln Z_N(\beta)
=3N\left(\frac{\hbar\omega_E}{2}+\beta^{-1}\ln\!\bigl(1-e^{-\beta\hbar\omega_E}\bigr)\right).
$$
The {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} is
$$
U(\beta)=-\frac{\partial}{\partial\beta}\ln Z_N(\beta)
=3N\left(\frac{\hbar\omega_E}{2}+\frac{\hbar\omega_E}{e^{\beta\hbar\omega_E}-1}\right).
$$

Let $\bar n = (e^{\beta\hbar\omega_E}-1)^{-1}$. Then the entropy can be written as
$$
S(\beta)=3N k_B\Bigl[(\bar n+1)\ln(\bar n+1)-\bar n\ln\bar n\Bigr],
$$
consistent with {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} in the canonical setting.

## Heat capacity
The heat capacity at constant volume (see {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="heat capacity at constant volume" >}}) is
$$
C_V
=3N k_B(\beta\hbar\omega_E)^2\,\frac{e^{\beta\hbar\omega_E}}{(e^{\beta\hbar\omega_E}-1)^2}.
$$

Defining the Einstein temperature $\Theta_E=\hbar\omega_E/k_B$, this becomes
$$
C_V = 3N k_B\left(\frac{\Theta_E}{T}\right)^2
\frac{e^{\Theta_E/T}}{(e^{\Theta_E/T}-1)^2}.
$$

## Limiting behavior and interpretation
- High temperature $T\gg \Theta_E$:
  $$
  C_V \to 3N k_B,
  $$
  reproducing the Dulong–Petit law.

- Low temperature $T\ll \Theta_E$:
  $$
  C_V \sim 3N k_B\left(\frac{\Theta_E}{T}\right)^2 e^{-\Theta_E/T},
  $$

  which decays exponentially and therefore misses the observed $T^3$ law in many crystalline solids.

The {{< knowl id="debye-model" text="Debye model" >}} modifies the mode spectrum to recover the correct low-temperature behavior.
