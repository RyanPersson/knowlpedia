---
title: "Microcanonical measure"
description: "Uniform probability measure on the microcanonical energy shell, expressing equal a priori probability for accessible microstates."
---

Fix a classical {{< knowl id="phase-space-classical" text="phase space" >}} $\Gamma$ with Liouville {{< knowl id="phase-space-volume-element" text="volume element" >}} $d\Gamma$, and a {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}} $H(x)$. For energy $E$ and window $\Delta E>0$, let $\Sigma_{E,\Delta E}$ be the {{< knowl id="microcanonical-shell" text="microcanonical shell" >}}.

## Definition (finite-thickness shell)
The **microcanonical measure** is the normalized restriction of Liouville measure to the shell:
$$
\mu_{E,\Delta E}(A)
\;=\;
\frac{1}{\Omega(E,\Delta E)}\int_{\Gamma}\mathbf{1}_A(x)\,\mathbf{1}_{\Sigma_{E,\Delta E}}(x)\, d\Gamma,
$$
where
$$
\Omega(E,\Delta E)
\;=\;
\int_{\Gamma}\mathbf{1}_{\Sigma_{E,\Delta E}}(x)\, d\Gamma
$$

is the shell volume. This makes $\mu_{E,\Delta E}$ a {{< knowl id="probability-measure" section="probability" text="probability measure" >}} on $\Gamma$.

Equivalently, the microcanonical density with respect to $d\Gamma$ is
$$
\rho_{E,\Delta E}(x)
\;=\;
\frac{\mathbf{1}_{\Sigma_{E,\Delta E}}(x)}{\Omega(E,\Delta E)}.
$$

## Definition (delta-function energy surface)
Formally, one can write a “surface” version concentrated on $H(x)=E$:
$$
\mu_E(dx)
\;=\;
\frac{\delta\!\big(E-H(x)\big)}{g(E)}\, d\Gamma,
$$

where $g(E)$ is the {{< knowl id="density-of-states" text="density of states" >}} ensuring normalization.

## Ensemble averages
Given an observable $A:\Gamma\to\mathbb{R}$ (a function of the {{< knowl id="microstate-classical" text="microstate" >}}), its microcanonical {{< knowl id="ensemble-average" text="ensemble average" >}} is
$$
\langle A\rangle_{\mathrm{mc}}
\;=\;
\int_{\Gamma} A(x)\, \mu_{E,\Delta E}(dx).
$$

This is the same object as the {{< knowl id="expectation" section="probability" text="expectation" >}} of $A$ under the probability distribution $\mu_{E,\Delta E}$.

## Invariance and equilibrium meaning
Because Hamiltonian time evolution preserves Liouville volume (Liouville’s theorem) and conserves energy, the microcanonical measure is stationary under the dynamics restricted to the shell. In the equilibrium picture, it encodes “equal a priori probability” among accessible microstates at fixed energy.

## Entropy connection
The associated microcanonical {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}} is captured by the {{< knowl id="boltzmann-entropy-microcanonical" text="Boltzmann entropy" >}}
$$
S(E,\Delta E) \;=\; k_B \ln \Omega(E,\Delta E),
$$

with {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann's constant" >}} $k_B$.
